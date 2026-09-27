# Held posts

Posts the pre-publish reviewer quarantined (`draft: true`) and that were never published. They live here instead of `blog/content/posts/` so the writer doesn't reread them on every run and the tag taxonomy counts only real posts. Each one's reason is its HELD line in `docs/review-log.md`.

A post the reviewer holds from now on stays in `blog/content/posts/` with `draft: true` (the routines can't move files: the guard only lets them touch posts and logs). Move it here through a pull request when you've decided not to revise it. To revive one, fix what the HELD line names, move it back, give it a future date, and remove `draft: true` and `reviewed: true` so the reviewer sees it fresh.
