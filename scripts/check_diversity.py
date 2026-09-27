#!/usr/bin/env python3
"""Feed-level diversity check.

Catches what the per-post checks miss: the same theme stacking up across
consecutive posts. The lint gate checks one post in isolation; the reviewer
checks one post against others for recycling. Neither looks at the publish
*sequence* and notices "that's three compliance posts in a row." This does.
Tags are the theme proxy.

This is an advisory tool for the two routines, NOT a deploy gate. Thematic
variety is a quality property, not a correctness one, and blocking the whole
site over it (especially over immutable already-published history) would be
wrong. The writer runs it to avoid creating a clash; the reviewer runs it to
reschedule a queued post that clashes.

Exit 1 if a clash involves a not-yet-live (future-dated) post — i.e. something
still actionable. Exit 0 otherwise.
"""
import sys, re, glob, os
from datetime import date

POSTS_DIR = "blog/content/posts"
BACKLOG = "docs/topic-backlog.md"
BACKLOG_STALE_DAYS = 28
SHARED_TAG_THRESHOLD = 2   # consecutive posts sharing this many tags = clash
WINDOW = 5                 # trailing window for heavy-theme detection
HEAVY = 3                  # a tag this many times in the window = heavy


def load():
    posts = []
    for path in glob.glob(os.path.join(POSTS_DIR, "*.md")):
        with open(path, encoding="utf-8") as f:
            t = f.read()
        dm = re.search(r"(?m)^date:\s*(\d{4}-\d{2}-\d{2})", t)
        if not dm:
            continue
        # Held posts (draft: true) never reach the feed, so they can't
        # clash with, wear out, or set the shape for anything.
        if re.search(r"(?m)^draft:\s*true\b", t):
            continue
        sm = re.search(r"(?m)^shape:\s*\"?([a-z]+)", t)
        om = re.search(r"(?m)^origin:\s*\"?([a-z]+)", t)
        rm = re.search(r"(?m)^reach:\s*\"?([a-z]+)", t)
        tm = re.search(r"(?m)^tags:\s*(.+)$", t)
        tags = re.findall(r'"([^"]+)"', tm.group(1)) if tm else []
        # Body = everything after the second front-matter fence. Used to locate
        # the <mark> so we can see if every recent post highlights in the same spot.
        body = t.split("\n---", 1)[1] if t.startswith("---") else t
        body = body.split("\n---", 1)[1] if body.startswith("---") else body
        marks = [m.start() for m in re.finditer(r"<mark>", body)]
        blen = max(len(body), 1)
        posts.append({
            "slug": os.path.splitext(os.path.basename(path))[0],
            "date": dm.group(1),
            "tags": tags,
            "shape": sm.group(1) if sm else None,
            "origin": om.group(1) if om else None,
            "reach": rm.group(1) if rm else None,
            "n_mark": len(marks),
            # position of the first mark as a fraction through the body (None if no mark)
            "mark_pos": (marks[0] / blen) if marks else None,
        })
    posts.sort(key=lambda p: (p["date"], p["slug"]))
    return posts


def allowed_reach(prior):
    """Reach values the next post may take, given earlier posts' reach, oldest first.

    Unlabeled history counts as core: every post before the field existed sat
    inside an established thread. Branching is paced, not forced: a post must
    step out (adjacent or new) only when none of the last three did, and `new`
    is allowed at most once in any six posts, so the feed widens slowly instead
    of lurching.
    """
    prior = [r or "core" for r in prior]
    allowed = {"core", "adjacent", "new"}
    if len(prior) >= 3 and all(r == "core" for r in prior[-3:]):
        allowed.discard("core")
    if "new" in prior[-5:]:
        allowed.discard("new")
    return allowed


def load_backlog(path=BACKLOG):
    """Backlog items as dicts: id, reach, status, added (date or None)."""
    items = []
    if not os.path.exists(path):
        return items
    with open(path, encoding="utf-8") as f:
        text = f.read()
    for m in re.finditer(r"(?m)^### (\S+) \| (core|adjacent|new) \| (.+?)\s*$", text):
        block = text[m.end():text.find("\n### ", m.end()) if "\n### " in text[m.end():] else len(text)]
        am = re.search(r"(?m)^- added:\s*(\d{4}-\d{2}-\d{2})", block)
        tm = re.search(r"(?m)^- thesis:\s*(.+)$", block)
        items.append({
            "id": m.group(1), "reach": m.group(2), "status": m.group(3).strip(),
            "added": am.group(1) if am else None,
            "thesis": tm.group(1).strip() if tm else "",
        })
    return items


def main():
    posts = load()
    today = date.today().isoformat()

    print("Timeline (date | tags | slug):")
    for p in posts:
        flag = " [live]" if p["date"] <= today else " [queued]"
        print(f"  {p['date']} | {', '.join(p['tags'])} | {p['slug']}{flag}")
    print()

    clashes = []
    for a, b in zip(posts, posts[1:]):
        shared = sorted(set(a["tags"]) & set(b["tags"]))
        if len(shared) >= SHARED_TAG_THRESHOLD:
            actionable = a["date"] > today or b["date"] > today
            clashes.append((a, b, shared, actionable))

    if clashes:
        print("CLUSTERING (consecutive posts sharing %d+ tags):" % SHARED_TAG_THRESHOLD)
        for a, b, shared, actionable in clashes:
            kind = "ACTIONABLE" if actionable else "historical"
            print(f"  [{kind}] {a['slug']} ({a['date']}) <-> {b['slug']} ({b['date']}) share {shared}")
    else:
        print("No consecutive-theme clustering.")

    tail = posts[-WINDOW:]
    freq = {}
    for p in tail:
        for t in p["tags"]:
            freq[t] = freq.get(t, 0) + 1
    heavy = {t: n for t, n in freq.items() if n >= HEAVY}
    if heavy:
        order = sorted(heavy.items(), key=lambda kv: -kv[1])
        print(f"HEAVY THEME across last {len(tail)} posts: " + ", ".join(f"{t} x{n}" for t, n in order))

    # Formatting monotony: is every recent post highlighting one sentence in the
    # same place? That reads as a template, not a person. Advisory only — variety
    # is taste, and you can't "fix" already-published history — so this never
    # changes the exit code; it just tells the writer to break the pattern.
    def band(pos):
        if pos is None:
            return "none"
        return "early" if pos < 0.34 else ("mid" if pos < 0.67 else "late")

    recent = posts[-3:]
    if len(recent) == 3:
        print()
        print("Highlight placement (last 3):")
        for p in recent:
            where = band(p["mark_pos"])
            pct = "" if p["mark_pos"] is None else f" (~{round(p['mark_pos']*100)}%)"
            print(f"  {p['date']} | {p['n_mark']} mark, {where}{pct} | {p['slug']}")
        all_marked = all(p["n_mark"] >= 1 for p in recent)
        bands = {band(p["mark_pos"]) for p in recent}
        if all_marked and len(bands) == 1:
            print("  FORMATTING MONOTONY: 3 in a row highlight in the same "
                  f"position ({bands.pop()}). Next post: no <mark>, or a clearly "
                  "different placement and structure.")
        elif all_marked:
            print("  NOTE: 3 in a row carry a highlight. A post with no <mark> "
                  "would vary the feed.")

    # Argument-shape rotation. Tags catch "three compliance posts in a row";
    # this catches "nine posts in a row that argue by analogy to another
    # field", which no tag or phrase check can see. The next post's shape
    # must differ from both of the last two.
    print()
    print("Shape and origin (last 6):")
    for p in posts[-6:]:
        flag = " [queued]" if p["date"] > today else ""
        print(f"  {p['date']} | {p['shape'] or '?':9s} | {p['origin'] or '?':6s} | {p['slug']}{flag}")
    shape_streak = False
    for i, p in enumerate(posts):
        prior = {q["shape"] for q in posts[max(0, i - 2):i] if q["shape"]}
        if p["date"] > today and p["shape"] in prior:
            shape_streak = True
            print(f"  [ACTIONABLE] SHAPE REPEAT: {p['slug']} is '{p['shape']}', "
                  "same as one of the two posts before it.")
    banned = sorted({p["shape"] for p in posts[-2:] if p["shape"]})
    if banned:
        print("  NEXT POST: shape must not be " + " or ".join(banned) + ".")
    inbox = sum(1 for p in posts[-6:] if p["origin"] == "inbox")
    print(f"  inbox-origin posts in last 6: {inbox}")

    # Reach: how far a post sits from the established threads. See CLAUDE.md
    # Blog Post Rule 13. Inbox posts are exempt from the rule (Joe's real
    # material outranks branching) but still count as history.
    print()
    print("Reach (last 6):")
    for p in posts[-6:]:
        flag = " [queued]" if p["date"] > today else ""
        print(f"  {p['date']} | {p['reach'] or '(core)':9s} | {p['slug']}{flag}")
    reach_bad = False
    for i, p in enumerate(posts):
        if p["date"] <= today or p["origin"] == "inbox":
            continue
        ok = allowed_reach([q["reach"] for q in posts[:i]])
        if (p["reach"] or "core") not in ok:
            reach_bad = True
            print(f"  [ACTIONABLE] REACH: {p['slug']} is '{p['reach'] or 'core'}', "
                  f"but the feed needed {' or '.join(sorted(ok))}.")
    nxt = allowed_reach([p["reach"] for p in posts])
    print("  NEXT POST: reach must be " + " or ".join(sorted(nxt))
          + " (inbox posts exempt).")

    backlog = load_backlog()
    print()
    print("Topic backlog (open items):")
    if not any(it["status"] == "open" for it in backlog):
        print("  (none open)")
    if backlog:
        stale = []
        for it in backlog:
            if it["status"] != "open":
                continue
            age = (date.fromisoformat(today) - date.fromisoformat(it["added"])).days if it["added"] else None
            fits = "fits" if it["reach"] in nxt else "    "
            print(f"  {fits} {it['id']} | {it['reach']:8s} | {age if age is not None else '?'}d | {it['thesis'][:90]}")
            if age is not None and age > BACKLOG_STALE_DAYS:
                stale.append(it["id"])
        if stale:
            print(f"  STALE (> {BACKLOG_STALE_DAYS} days, the scout should expire them): " + ", ".join(stale))

    actionable = any(a for *_, a in clashes) or shape_streak or reach_bad
    print()
    print("RESULT:", "clash on a queued post (actionable)" if actionable else "ok")
    sys.exit(1 if actionable else 0)


if __name__ == "__main__":
    main()
