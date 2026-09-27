#!/usr/bin/env python3
"""Queue and date planner for the writer routine.

The veto surface only works if a post sits in the queue long enough for a
person to read its preview issue. The writer used to pick its date as "2-4
days after the latest post", which says nothing about today: once the queue
drained, that rule put new posts one or two days out and the veto window
collapsed from a week to a day. This does the date math so the model doesn't:

  - MIN_LEAD: a new post is dated at least this many days after today.
  - GAP: 2-4 days after the latest scheduled post, and not the same gap the
    latest post used (a fixed offset is a clock, and a clock is a bot tell).
  - MAX_QUEUE: at this many queued posts, skip the run. The buffer is full;
    writing more only pushes posts further out.

Prints the queue, the allowed dates, and a final DECISION line the routine
acts on. Exit 0 whether it says WRITE or SKIP (skipping is a normal outcome);
non-zero only when it finds no posts at all, which means it's looking in the
wrong place.
"""
import datetime as dt
import glob
import os
import re
import sys

# Resolved from this file, so running from the wrong directory can't find
# zero posts and report an empty queue.
POSTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                         "blog", "content", "posts")
# Six, not five: the preview issue opens when the reviewer stamps the post,
# which can slip a day behind the writer, and the build publishes at 13:10 UTC
# on the post's date. Six days out leaves Joe about five to veto.
MIN_LEAD = 6
GAP_MIN, GAP_MAX = 2, 4
MAX_QUEUE = 3


def load(posts_dir=POSTS_DIR):
    """(date, slug) for every non-draft post, oldest first."""
    out = []
    for path in glob.glob(os.path.join(posts_dir, "*.md")):
        with open(path, encoding="utf-8") as f:
            t = f.read()
        m = re.search(r"(?m)^date:\s*(\d{4}-\d{2}-\d{2})", t)
        if not m or re.search(r"(?m)^draft:\s*true\b", t):
            continue
        out.append((dt.date.fromisoformat(m.group(1)),
                    os.path.splitext(os.path.basename(path))[0]))
    return sorted(out)


def plan(dates, today):
    """Allowed publish dates for the next post, or [] when the run should skip.

    `dates` is every non-draft post date. Returns (allowed, queued, reason).
    """
    queued = [d for d in dates if d > today]
    if len(queued) >= MAX_QUEUE:
        return [], queued, f"queue full ({len(queued)} queued, max {MAX_QUEUE})"
    latest = max(dates) if dates else today
    prev_gap = (dates[-1] - dates[-2]).days if len(dates) >= 2 else None
    floor = today + dt.timedelta(days=MIN_LEAD)
    candidates = [latest + dt.timedelta(days=g) for g in range(GAP_MIN, GAP_MAX + 1)]
    allowed = [d for d in candidates
               if d >= floor and (d - latest).days != prev_gap]
    if not allowed:
        # The queue is thin, so the lead floor wins over the gap rule. Offer a
        # small spread past the floor so the date still isn't a fixed offset.
        allowed = [floor + dt.timedelta(days=i) for i in range(3)]
    return allowed, queued, None


def main():
    today = dt.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else dt.date.today()
    posts = load()
    if not posts:
        sys.exit(f"FATAL: no posts found in {POSTS_DIR}; not planning a date blind.")
    allowed, queued, skip = plan([d for d, _ in posts], today)
    print(f"today: {today}")
    print(f"queued (future-dated, not held): {len(queued)}")
    for d, s in posts:
        if d > today:
            print(f"  {d} ({(d - today).days}d out) {s}")
    if posts:
        d, s = posts[-1]
        print(f"latest scheduled: {d} {s}")
    if skip:
        print(f"DECISION: SKIP, {skip}. Do not write a post this run.")
    else:
        print("ALLOWED DATES: " + ", ".join(d.isoformat() for d in allowed))
        print("DECISION: WRITE, date the post with one of the allowed dates.")


if __name__ == "__main__":
    main()
