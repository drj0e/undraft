# Topic Backlog

Candidate posts, refilled weekly by the scout routine (`docs/routines/scout.md`) and drawn down by the writer. It exists so the blog widens on purpose: the scout looks one step past the established threads every week, and `scripts/check_diversity.py` tells the writer when the next post has to step out (CLAUDE.md Blog Post Rule 13).

The repo is public. Items are theses and public sources only: never anything from Joe's Drive, work, or inbox notes.

## Format

Each item is a `###` heading `<id> | <reach> | <status>` followed by fields. `check_diversity.py` parses the heading and the `added` and `thesis` lines, so keep those exact.

- **id**: `B-YYYY-MM-DD-n` (the scout run's date, then 1, 2, 3...).
- **reach**: `core`, `adjacent`, or `new` (CLAUDE.md Blog Post Rule 13).
- **status**: `open`, `used: <post-slug>` (set by the writer), or `expired: <reason>` (set by the scout; items open longer than 28 days expire, since a weekly hook goes stale).
- Fields: `added`, `thesis` (one sentence), `nearest post` (slug, and the new point this makes that the post doesn't), `prior art` (the search query run and what it found, and the operative delta), `hook` (a verified link, and why this week), `shape` (suggested, not binding), `anchor` (the published fact or public source that lets Joe write it without inventing experience).

Exactly this syntax (shown indented here so the parser skips it; real items start at the left margin). Plain `- field: value` lines, no bold, or the parser silently loses the date and the item never expires:

    ### B-2026-10-04-1 | adjacent | open
    - added: 2026-10-04
    - thesis: One sentence stating the claim the post would make.
    - nearest post: some-published-slug; new point: what this says that it doesn't
    - prior art: queries "..." and "..."; found ...; delta: ...
    - hook: [Page title](https://example.com/primary-source) (verified 2026-10-04), why it matters this week, or none (evergreen)
    - shape: teardown
    - tags: data, compliance
    - anchor: the published post or public source that lets Joe write this

## This week

(The scout's top three open items, most promising first.)

## Items

