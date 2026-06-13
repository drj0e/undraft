#!/usr/bin/env python3
"""Deterministic pre-publish gate for blog posts.

Runs in CI before the Hugo build. Fails the job (blocking deploy) if any post
in blog/content/posts/ violates a mechanical rule. These are the binary checks
that need no judgment: front matter, tags against the taxonomy, exactly one
<mark>, no em-dashes, no leftover placeholders, a tight high-precision AI-tell
list, and internal links that actually resolve.

What this does NOT check, by design: whether the post is true, whether it
recycles an existing post's argument, or whether it's any good. Those need
judgment and are the model reviewer's job. This layer just guarantees the
dumb failures can't ship. Cheapest checks, no model call: the guard-pipeline
pattern from "The Stack Nobody Talks About".
"""
import sys, re, glob, os, datetime

POSTS_DIR = "blog/content/posts"
TAXONOMY = "docs/tag-taxonomy.md"
# Posts dated after this (the day the pre-publish reviewer went live) must carry
# 'reviewed: true' before they are allowed to go live. Older posts are
# grandfathered. This makes the model reviewer a hard gate, not best-effort: if
# it never stamped a post, that post cannot publish.
REVIEW_ERA = "2026-06-13"

# High-precision AI-tell phrases only. Context-independent, so safe to hard-fail.
# Intentionally omits words with legitimate uses on this blog (harness, landscape,
# navigate, robust, unlock, comprehensive) — the model reviewer judges those.
KILL = [
    r"\bdelv(?:e|ing|ed|es)\b",
    r"\bin conclusion\b",
    r"\bwithout further ado\b",
    r"\bit'?s worth noting\b",
    r"\bat the end of the day\b",
    r"\bgame[- ]changers?\b",
    r"\bparadigm shift\b",
    r"\bbest[- ]in[- ]class\b",
    r"\bcutting[- ]edge\b",
    r"\bstate[- ]of[- ]the[- ]art\b",
    r"\bmove the needle\b",
    r"\blet'?s (?:dive|explore|unpack)\b",
    r"\bi'?m excited to share\b",
    r"\bproud to announce\b",
    r"\bfirstly\b",
    r"\bsynergy\b",
]
REQUIRED_FIELDS = ["title", "date", "tags", "summary"]


def load_allowed_tags():
    tags = set()
    with open(TAXONOMY, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\s*\|\s*`([^`]+)`\s*\|", line)
            if m:
                tags.add(m.group(1).strip())
    if not tags:
        raise SystemExit(f"FATAL: no tags parsed from {TAXONOMY}")
    return tags


def split_front_matter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    return text[3:end], text[end + 4:]


def field(fm, name):
    m = re.search(rf"(?m)^{name}:\s*(.+?)\s*$", fm)
    return m.group(1) if m else None


def main():
    allowed = load_allowed_tags()
    today = datetime.date.today().isoformat()
    posts = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")))
    slugs = {os.path.splitext(os.path.basename(p))[0] for p in posts}
    errors = []

    for path in posts:
        name = os.path.basename(path)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        fm, body = split_front_matter(text)
        if fm is None:
            errors.append(f"{name}: no front matter")
            continue

        for fld in REQUIRED_FIELDS:
            if field(fm, fld) is None:
                errors.append(f"{name}: missing front-matter field '{fld}'")

        tags = re.findall(r'"([^"]+)"', field(fm, "tags") or "")
        if not 2 <= len(tags) <= 4:
            errors.append(f"{name}: {len(tags)} tags, must be 2-4 -> {tags}")
        for t in tags:
            if t not in allowed:
                errors.append(f"{name}: tag '{t}' not in taxonomy")

        n_mark = len(re.findall(r"<mark>", body))
        if n_mark != 1:
            errors.append(f"{name}: {n_mark} <mark> tags, must be exactly 1")

        if "—" in body:
            errors.append(f"{name}: contains em-dash (banned)")

        if "[JOE" in body or "SOURCE NEEDED" in body:
            errors.append(f"{name}: leftover placeholder ([JOE or SOURCE NEEDED)")

        low = body.lower()
        for pat in KILL:
            m = re.search(pat, low)
            if m:
                errors.append(f"{name}: banned phrase '{m.group(0).strip()}'")

        for slug in re.findall(r"\]\(/posts/([^/)]+?)/?\)", body):
            if slug not in slugs:
                errors.append(f"{name}: internal link /posts/{slug}/ resolves to no post")

        # Enforced review: a reviewer-era post may not go live unreviewed.
        post_date = (field(fm, "date") or "")[:10]
        is_draft = (field(fm, "draft") or "false").strip().lower() == "true"
        is_reviewed = (field(fm, "reviewed") or "false").strip().lower() == "true"
        if not is_draft and REVIEW_ERA < post_date <= today and not is_reviewed:
            errors.append(
                f"{name}: live (dated {post_date}) but never reviewed "
                f"(no 'reviewed: true'); the reviewer must clear it before its date"
            )

    if errors:
        print("POST GATE FAILED ({} issue(s)):".format(len(errors)))
        for e in errors:
            print("  - " + e)
        sys.exit(1)
    print(f"Post gate passed: {len(posts)} posts clean.")


if __name__ == "__main__":
    main()
