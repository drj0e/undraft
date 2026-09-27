#!/usr/bin/env python3
"""Deterministic pre-publish gate for blog posts.

Runs in CI before the Hugo build. Fails the job (blocking deploy) if any post
in blog/content/posts/ violates a mechanical rule. These are the binary checks
that need no judgment: front matter, tags against the taxonomy, at most two
<mark> tags (zero is fine), no em-dashes, no leftover placeholders, a tight
high-precision AI-tell list (plus an era-gated tic list added later, so
grandfathered history keeps building), and internal links that actually
resolve.

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

# Phrase-form rhetorical tics, banned the same way but only for posts dated
# after TIC_ERA — a couple of live posts contain them ("worth naming",
# "worth sitting with") and published history doesn't get edited for style,
# so a blanket ban would wedge the build on immutable posts. Same
# grandfathering pattern as REVIEW_ERA. These are the single-phrase tells;
# their frequency/structure cousins (negation flips, "that's the ___",
# closer templates) can't be hard-failed by regex and live in
# scripts/check_tics.py + the reviewer instead.
TIC_ERA = "2026-07-18"
TIC_KILL = [
    r"\bsit(?:ting|s)? with (?:that|this|it|the discomfort)\b",
    r"\bworth naming\b",
    r"\bnot nothing\b",
    r"\bthe punch ?line\b",
    r"\byou already know(?:\s*[.!?,]| the answer| what to| how this)",
    r"\b(?:that'?s|that is|this is|is) the whole (?:point|game|thing|story|job|pitch)\b",
    r"\bis the entire [a-z]",
    r"\bthe entire (?:point|game|thing|story|job|pitch|business model) is\b",
]
REQUIRED_FIELDS = ["title", "date", "tags", "summary"]
# Argument shape and provenance, tracked so check_diversity.py can see the
# feed's skeleton the way tags let it see themes. Required for posts dated
# after SHAPE_ERA; older posts may carry them (backfilled) or not.
SHAPE_ERA = "2026-09-27"
SHAPES = {"analogy", "argument", "story", "teardown", "question", "note"}
ORIGINS = {"thread", "inbox"}
# Internal links, relative or absolute to the site's own domain. Absolute ones
# used to skip the resolve check entirely.
_POST_LINK = re.compile(
    r"\]\((?:https?://(?:www\.)?josephcapozzoli\.com)?/posts/([^/)#?]+?)/?(?:[#?][^)]*)?\)"
)


def dead_link_targets(body, slugs, draft_slugs):
    """Internal-link slugs in `body` that won't resolve on the built site.

    A slug with no file is dead. So is a slug whose post is `draft: true`:
    Hugo doesn't build drafts, so the file exists in the repo but the URL
    404s. Returns (slug, reason) pairs.
    """
    out = []
    for slug in _POST_LINK.findall(body):
        if slug not in slugs:
            out.append((slug, "resolves to no post"))
        elif slug in draft_slugs:
            out.append((slug, "points at a draft (held) post, which 404s live"))
    return out


def tic_hits(body):
    """Era-gated tic phrases found in `body` (already lowercased or not)."""
    low = body.lower()
    return [m.group(0).strip() for m in
            (re.search(p, low) for p in TIC_KILL) if m]


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


# --- Advisory self-citation checks (non-blocking) ------------------------------
# These never fail the build. A regex can't decide whether a paraphrase of a
# prior post is faithful, so it doesn't try. It surfaces the spots a human (and
# the model reviewer) must verify, and flags the one shape that IS mechanical:
# a citing post that lists a strict subset of a list in the post it links to.

_CLAIM_CUE = re.compile(
    r"\b(?:I (?:listed|argued|said|wrote|covered|called|described|noted|"
    r"mentioned|explained|made the case)|months? back|weeks? back|"
    r"a few weeks ago|last time|previously|earlier)\b",
    re.IGNORECASE,
)
_INTERNAL_LINK = re.compile(r"\]\(/posts/([^/)]+?)/?\)")
# A run of three or more comma-separated single words, optional "and/or" before
# the last item: "selectable, constrained, audited, and stoppable". The
# negative lookahead keeps the middle run from swallowing ", and X" so the final
# item lands in the trailing conjunction group instead of being dropped.
_LIST = re.compile(
    r"[A-Za-z][\w-]*(?:,\s+(?!(?:and|or)\b)[A-Za-z][\w-]*){2,}"
    r"(?:,?\s+(?:and|or)\s+[A-Za-z][\w-]*)?"
)


def _sentences(text):
    flat = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'\[])", flat)
    return [p for p in parts if p.strip()]


def _stem(word):
    w = word.lower().strip(".,;:!?\"'()[]")
    for suf in ("ability", "ibility", "able", "ible", "ation", "ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            return w[: -len(suf)]
    return w


def _list_items(text):
    """Every 3+ item comma-list in `text`, each as its list of head words."""
    out = []
    for m in _LIST.finditer(text):
        parts = re.split(r",\s*(?:and\s+|or\s+)?|\s+(?:and|or)\s+", m.group(0))
        items = [p.strip() for p in parts if p.strip() and p.strip().lower() not in ("and", "or")]
        if len(items) >= 3:
            out.append(items)
    return out


def find_self_citations(body):
    """Sentences that claim what a prior (internal-linked) post said.

    Returns the sentence text for each, so the reviewer/human can confirm the
    claim against the linked post rather than trusting the paraphrase.
    """
    hits = []
    for s in _sentences(body):
        if _INTERNAL_LINK.search(s) and _CLAIM_CUE.search(s):
            hits.append(s.strip())
    return hits


def find_subset_enumerations(body, target_bodies):
    """Citing lists that are a strict subset of a list in the post they link to.

    `target_bodies` maps slug -> that post's body. For each sentence that holds
    both an internal link and a comma-list, if the cited post contains a longer
    list whose members are a strict superset (by word stem), report the dropped
    member(s) -- the exact failure where a recap quietly shrinks a prior list.
    """
    hits = []
    for s in _sentences(body):
        slugs = _INTERNAL_LINK.findall(s)
        if not slugs:
            continue
        for citing in _list_items(s):
            cset = {_stem(w) for w in citing}
            for slug in slugs:
                tbody = target_bodies.get(slug)
                if not tbody:
                    continue
                for target in _list_items(tbody):
                    tmap = {_stem(w): w for w in target}
                    tset = set(tmap)
                    if cset < tset:  # strict subset: citing dropped member(s)
                        hits.append({
                            "slug": slug,
                            "citing": citing,
                            "target": target,
                            "missing": [tmap[st] for st in tset - cset],
                        })
                        break
    return hits


def main():
    allowed = load_allowed_tags()
    today = datetime.date.today().isoformat()
    posts = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")))
    slugs = {os.path.splitext(os.path.basename(p))[0] for p in posts}
    draft_slugs = set()
    for p in posts:
        with open(p, encoding="utf-8") as f:
            fm0, _ = split_front_matter(f.read())
        if fm0 and (field(fm0, "draft") or "").strip().lower() == "true":
            draft_slugs.add(os.path.splitext(os.path.basename(p))[0])
    errors = []
    bodies = {}

    for path in posts:
        name = os.path.basename(path)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        fm, body = split_front_matter(text)
        if fm is None:
            errors.append(f"{name}: no front matter")
            continue
        bodies[os.path.splitext(name)[0]] = body

        for fld in REQUIRED_FIELDS:
            if field(fm, fld) is None:
                errors.append(f"{name}: missing front-matter field '{fld}'")

        tags = re.findall(r'"([^"]+)"', field(fm, "tags") or "")
        if not 2 <= len(tags) <= 4:
            errors.append(f"{name}: {len(tags)} tags, must be 2-4 -> {tags}")
        for t in tags:
            if t not in allowed:
                errors.append(f"{name}: tag '{t}' not in taxonomy")

        # Highlighting is optional and should be uneven across the feed. A post
        # with no <mark> is fine (and common); the cap stops a post from turning
        # into a highlighter mess. Variety of placement is enforced at the feed
        # level by check_diversity.py, not here.
        post_date = (field(fm, "date") or "")[:10]
        for fld, allowed_vals in (("shape", SHAPES), ("origin", ORIGINS)):
            val = (field(fm, fld) or "").strip().strip('"')
            if val and val not in allowed_vals:
                errors.append(f"{name}: {fld} '{val}' not one of {sorted(allowed_vals)}")
            elif not val and post_date > SHAPE_ERA:
                errors.append(f"{name}: missing '{fld}' (required after {SHAPE_ERA})")

        n_mark = len(re.findall(r"<mark>", body))
        if n_mark > 2:
            errors.append(f"{name}: {n_mark} <mark> tags, cap is 2 (0 is fine)")

        if "—" in body:
            errors.append(f"{name}: contains em-dash (banned)")

        if "[JOE" in body or "SOURCE NEEDED" in body:
            errors.append(f"{name}: leftover placeholder ([JOE or SOURCE NEEDED)")

        low = body.lower()
        for pat in KILL:
            m = re.search(pat, low)
            if m:
                errors.append(f"{name}: banned phrase '{m.group(0).strip()}'")

        if post_date > TIC_ERA:
            for hit in tic_hits(body):
                errors.append(f"{name}: banned tic phrase '{hit}' "
                              f"(post-{TIC_ERA} posts; see CLAUDE.md Rhetorical Tics)")

        is_draft = (field(fm, "draft") or "false").strip().lower() == "true"

        # A held post linking to another held post breaks nothing live, so
        # drafts only need their links to exist.
        for slug, reason in dead_link_targets(
                body, slugs, set() if is_draft else draft_slugs):
            errors.append(f"{name}: internal link /posts/{slug}/ {reason}")

        # Enforced review: a reviewer-era post may not go live unreviewed.
        is_reviewed = (field(fm, "reviewed") or "false").strip().lower() == "true"
        if not is_draft and REVIEW_ERA < post_date <= today and not is_reviewed:
            errors.append(
                f"{name}: live (dated {post_date}) but never reviewed "
                f"(no 'reviewed: true'); the reviewer must clear it before its date"
            )

    # Advisory pass: surfaces self-citations to verify and flags subset-list
    # recaps. Never changes the exit code -- judgment belongs to the reviewer.
    dropped = []
    citations = []
    for slug, body in sorted(bodies.items()):
        if slug in draft_slugs:
            continue  # held posts never ship; their citations aren't work
        for hit in find_subset_enumerations(body, bodies):
            dropped.append((slug, hit))
        for sentence in find_self_citations(body):
            citations.append((slug, sentence))

    if dropped:
        print("\nADVISORY -- possible dropped list member (verify against source):")
        for slug, hit in dropped:
            print(f"  - {slug}.md cites /posts/{hit['slug']}/ listing "
                  f"{hit['citing']}, but that post lists {hit['target']}; "
                  f"missing: {', '.join(hit['missing'])}")
    if citations:
        print("\nADVISORY -- self-citations to verify against the linked post:")
        for slug, sentence in citations:
            short = sentence if len(sentence) <= 140 else sentence[:137] + "..."
            print(f"  - {slug}.md: {short}")

    if errors:
        print("\nPOST GATE FAILED ({} issue(s)):".format(len(errors)))
        for e in errors:
            print("  - " + e)
        sys.exit(1)
    print(f"\nPost gate passed: {len(posts)} posts clean.")


if __name__ == "__main__":
    main()
