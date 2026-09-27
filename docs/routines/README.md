# Routine prompts

The scheduled Claude routines that run the blog pipeline. Each routine in claude.ai (Routines) holds a one-line prompt telling it to follow its file here, on `main`, so these files are the live prompts and their history is the record of what each routine was told and when. Change a prompt by changing its file through a pull request; the guard reverts direct pushes to this folder. Never paste a full prompt into the routine: it would silently stop following this file.

| File | Routine | Schedule |
|---|---|---|
| `writer.md` | Blog post draft candidate | `0 13 */3 * *` (13:00 UTC every third day of the month) |
| `reviewer.md` | Blog pre-publish reviewer (fixed) | `30 13 * * *` (13:30 UTC daily) |
| `scout.md` | Blog topic scout | `50 11 * * 0` (11:50 UTC Sundays) |

Everything below the `---` line in each file is the prompt. `<INBOX_FOLDER_ID>` stands for the Drive folder ID of the Undraft inbox; each routine's one-line prompt supplies the real ID. This repo is public, and the ID is left out so the inbox isn't one link-share away from the internet. Keep that folder shared with no one.

## What routines may push

The routines push straight to `main`, and the writer and scout follow these prompt files from the repo. So `scripts/guard_protected.py`, run as the `guard` job of the deploy workflow, holds direct pushes to the files routines legitimately write: posts, `docs/review-log.md`, `docs/tag-taxonomy.md`, `docs/inbox-log.md`, and `docs/topic-backlog.md`. A direct push that touches anything else (these prompts, `claude.md`, scripts, templates, the workflows) without a merged pull request is reverted, its deploy is blocked, and an issue is opened. Change protected files through a PR, including your own edits. The lint separately rejects posts containing scripts, frames, forms, or event handlers, since the site renders raw HTML.

One gap GitHub doesn't let a personal repo close: a push's workflows run from that push's own `.github/`, so a push that rewrites the deploy workflow itself can switch the guard off.
