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
        tm = re.search(r"(?m)^tags:\s*(.+)$", t)
        tags = re.findall(r'"([^"]+)"', tm.group(1)) if tm else []
        posts.append({
            "slug": os.path.splitext(os.path.basename(path))[0],
            "date": dm.group(1),
            "tags": tags,
        })
    posts.sort(key=lambda p: (p["date"], p["slug"]))
    return posts


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

    actionable = any(a for *_, a in clashes)
    print()
    print("RESULT:", "clash on a queued post (actionable)" if actionable else "ok")
    sys.exit(1 if actionable else 0)


if __name__ == "__main__":
    main()
