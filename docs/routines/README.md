# Routine prompts

The two scheduled Claude routines that run the blog pipeline. The prompts are configured in claude.ai (Routines), which keeps no history; these files are the versioned copy. Change the file, then paste it into the routine, so the diff here is the record of what the routine was told and when.

| File | Routine | Schedule |
|---|---|---|
| `writer.md` | Blog post draft candidate | `0 13 */3 * *` (13:00 UTC every third day of the month) |
| `reviewer.md` | Blog pre-publish reviewer (fixed) | `30 13 * * *` (13:30 UTC daily) |
| `scout.md` | Blog topic scout | `50 11 * * 0` (11:50 UTC Sundays) |

Everything below the `---` line in each file is the prompt, verbatim, with one redaction: `<INBOX_FOLDER_ID>` stands for the Drive folder ID of the Undraft inbox. The live routines carry the real ID. This repo is public, and the ID is left out so the inbox isn't one link-share away from the internet. Keep that folder shared with no one.

## What routines may push

The routines push straight to `main`, and the writer and scout follow these prompt files from the repo. So `scripts/guard_protected.py`, run as the `guard` job of the deploy workflow, holds direct pushes to the files routines legitimately write: posts, `docs/review-log.md`, `docs/tag-taxonomy.md`, `docs/inbox-log.md`, and `docs/topic-backlog.md`. A direct push that touches anything else (these prompts, `claude.md`, scripts, templates, the workflows) without a merged pull request is reverted, its deploy is blocked, and an issue is opened. Change protected files through a PR, including your own edits. The lint separately rejects posts containing scripts, frames, forms, or event handlers, since the site renders raw HTML.

One gap GitHub doesn't let a personal repo close: a push's workflows run from that push's own `.github/`, so a push that rewrites the deploy workflow itself can switch the guard off.
