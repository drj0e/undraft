#!/usr/bin/env python3
"""Feed-level rhetorical-tic check.

The lint gate bans words and phrases that are wrong in any register. This
checks the other kind of tell: *moves* — argument shapes and sentence rhythms
that are fine once and become a template through repetition. A negation flip
("X isn't Y. It's Z.") is good writing exactly once per post. In seventeen of
the first twenty-five posts it's a fingerprint. No single post is wrong; the
feed is. So this looks at the feed, the same way check_diversity.py does for
themes.

Two tiers:
  ROTATION — moves with a per-post budget and a wear limit across recent
             posts. Flagged when one post leans on a move twice, or when the
             move shows up in most of the trailing window.
  HARD     — structural cliches with no budget (chained "no X, no Y",
             "don't call it X, call it Y", "the X is real, and..."). Any hit
             in a not-yet-live post is actionable. The single-phrase cousins
             of these ("sit with that", "worth naming") are era-gated hard
             fails in lint_posts.py, not here.

Also classifies the closing paragraph of each post, because the closer is
where the template shows first: flip-family endings ("The teams that X won't
be the ones Y...") three posts in a row reads as a machine signing off.

Advisory, same contract as check_diversity.py: exit 1 only when a flag lands
on a queued (future-dated) post — something still editable. Live history is
printed for awareness and is not work; you don't edit published posts for
style. The writer routine runs this before drafting to know what's worn out;
the reviewer runs it per docs/review-checklist.md before stamping.
"""
import sys, re, glob, os
from datetime import date

POSTS_DIR = "blog/content/posts"
WINDOW = 8  # trailing posts considered for wear

# --- Rotation moves: (key, label, regex, per-post flag threshold, wear count)
# A move "wears out" when it appears in `wear` or more of the last WINDOW posts.
_FLIP = (
    r"(?:'re not|is not|isn'?t|are not|aren'?t|was not|wasn'?t|won'?t be|"
    r"is never|was never|never was)\s[^.!?]{0,60}[.!?]\s+"
    r"(?:it'?s|it is|it'?ll|they'?re|they are|they'?ll|that'?s|you'?re)\s"
    r"|\bnot because [^.!?]{2,60}[.!?]\s+because\b"
)
ROTATION = [
    ("flip", "negation flip (X isn't Y. It's Z.)", _FLIP, 2, 5),
    ("christen", "'That's the ___' christening", r"\bthat'?s the [a-z-]+\b", 2, 5),
    ("nobody", "'nobody' as intensifier", r"\bnobody\b", 3, 6),
    ("one-x", "'the one X that Y'",
     r"\bthe one [a-z-]+ (?:that|nobody|the|you|in|left|who|which)\b", 2, 4),
    ("hush", "quietly/silently", r"\b(?:quietly|silently)\b", 2, 5),
    ("load", "'load-bearing'", r"\bload[- ]bearing\b", 2, 4),
    ("moment", "'the moment ...'", r"\bthe moment\b", 2, 5),
]

# --- Hard structural cliches: any occurrence flagged, actionable when queued.
HARD = [
    ("no-chain", "'no X, no Y' chain", r"\bno [a-z][\w-]*(?: [\w-]+)?, no [a-z]"),
    ("didnt-chain", "'did not X, did not Y' chain",
     r"\b(?:did not|didn'?t) [a-z][^.!?]{0,40}?, (?:did not|didn'?t)\b"),
    ("dont-verb-it", "'Don't VERB it ... VERB it'",
     r"\bdon'?t (call|name|label|file|frame|ship) (?:it|this|that)\b"
     r"[^.!?]{0,80}[.!?]\s+\1 (?:it|this|that)\b"),
    ("real-and", "'the X is real, and/but/not ...'", r"\bis real,? (?:and|but|not)\b"),
]

# --- Closer shapes. "flip" here is the negated-expectation ending: deny the
# obvious reading, then supply the real one. It closes at least ten of the
# first twenty-five posts, four of them with the identical "the teams that..."
# scaffold, which is why it gets its own streak check.
_CLOSER_FLIP = re.compile(
    _FLIP
    + r"|\bthe (?:teams|ones|companies|people) that\b[^.!?]{0,80}\b(?:aren'?t|won'?t|isn'?t|weren'?t)\b"
    + r"|\bwon'?t be [^.!?]{2,60}[.!?]\s+(?:it'?ll|they'?ll)\b",
    re.IGNORECASE,
)


def closer_shape(paragraph):
    if _CLOSER_FLIP.search(paragraph):
        return "flip"
    if paragraph.rstrip().endswith("?"):
        return "question"
    return "plain"


def load():
    posts = []
    for path in glob.glob(os.path.join(POSTS_DIR, "*.md")):
        with open(path, encoding="utf-8") as f:
            t = f.read()
        dm = re.search(r"(?m)^date:\s*(\d{4}-\d{2}-\d{2})", t)
        if not dm:
            continue
        body = t.split("\n---", 1)[1] if t.startswith("---") else t
        body = body.split("\n---", 1)[1] if body.startswith("---") else body
        paras = [p.strip() for p in body.split("\n\n") if p.strip()]
        posts.append({
            "slug": os.path.splitext(os.path.basename(path))[0],
            "date": dm.group(1),
            "body": body.lower(),
            "closer": paras[-1] if paras else "",
        })
    posts.sort(key=lambda p: (p["date"], p["slug"]))
    return posts


def snippets(rx, body, limit=3):
    return [m.group(0).strip()[:70] for m in rx.finditer(body)][:limit]


def main():
    posts = load()
    today = date.today().isoformat()
    for p in posts:
        p["queued"] = p["date"] > today
    actionable = False

    print("Per-post rotation counts (slug | move: n):")
    counts = {key: [] for key, *_ in ROTATION}
    breaches = []
    for p in posts:
        row = []
        for key, label, pat, cap, wear in ROTATION:
            rx = re.compile(pat, re.IGNORECASE)
            n = len(rx.findall(p["body"]))
            counts[key].append((p, n))
            if n:
                row.append(f"{key}: {n}")
            if n >= cap:
                breaches.append((p, label, n, snippets(rx, p["body"])))
        flag = " [queued]" if p["queued"] else ""
        print(f"  {p['date']} | {p['slug']}{flag} | " + (", ".join(row) or "-"))

    if breaches:
        print("\nPER-POST BUDGET BREACHES (a move used twice+ in one post):")
        for p, label, n, snips in breaches:
            kind = "ACTIONABLE" if p["queued"] else "historical"
            actionable |= p["queued"]
            print(f"  [{kind}] {p['slug']}: {label} x{n}")
            for s in snips:
                print(f"      > {s}")

    tail_posts = posts[-WINDOW:]
    worn = []
    for key, label, pat, cap, wear in ROTATION:
        tail = [(p, n) for p, n in counts[key] if p in tail_posts]
        hit = [(p, n) for p, n in tail if n > 0]
        if len(hit) >= wear:
            queued_hit = any(p["queued"] for p, _ in hit)
            worn.append((label, hit, queued_hit))
            actionable |= queued_hit
    if worn:
        print(f"\nWORN MOVES (in too many of the last {min(WINDOW, len(posts))} posts):")
        for label, hit, queued_hit in worn:
            kind = "ACTIONABLE" if queued_hit else "historical"
            who = ", ".join(p["slug"] for p, _ in hit)
            print(f"  [{kind}] {label}: {len(hit)} posts ({who})")
            print("      next post's budget for this move is zero.")

    hard_hits = []
    for p in posts:
        for key, label, pat in HARD:
            rx = re.compile(pat, re.IGNORECASE)
            if rx.search(p["body"]):
                hard_hits.append((p, label, snippets(rx, p["body"])))
                actionable |= p["queued"]
    if hard_hits:
        print("\nHARD STRUCTURAL CLICHES:")
        for p, label, snips in hard_hits:
            kind = "ACTIONABLE" if p["queued"] else "historical"
            print(f"  [{kind}] {p['slug']}: {label}")
            for s in snips:
                print(f"      > {s}")

    print("\nCloser shapes (last 5):")
    recent = posts[-5:]
    for p in recent:
        flag = " [queued]" if p["queued"] else ""
        print(f"  {p['date']} | {closer_shape(p['closer']):8s} | {p['slug']}{flag}")
    streak = posts[-3:]
    if len(streak) == 3 and all(closer_shape(p["closer"]) == "flip" for p in streak):
        queued_hit = any(p["queued"] for p in streak)
        kind = "ACTIONABLE" if queued_hit else "historical"
        actionable |= queued_hit
        print(f"  [{kind}] CLOSER STREAK: 3 in a row end on a negation flip. "
              "The next closer must be a different shape: a plain fact, an "
              "instruction, an image, or an open question.")

    print()
    print("RESULT:", "tic on a queued post (actionable)" if actionable else "ok")
    sys.exit(1 if actionable else 0)


if __name__ == "__main__":
    main()
