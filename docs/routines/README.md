# Routine prompts

The two scheduled Claude routines that run the blog pipeline. The prompts are configured in claude.ai (Routines), which keeps no history; these files are the versioned copy. Change the file, then paste it into the routine, so the diff here is the record of what the routine was told and when.

| File | Routine | Schedule |
|---|---|---|
| `writer.md` | Blog post draft candidate | `0 13 */3 * *` (13:00 UTC every third day of the month) |
| `reviewer.md` | Blog pre-publish reviewer (fixed) | `30 13 * * *` (13:30 UTC daily) |
| `scout.md` | Blog topic scout | `50 11 * * 0` (11:50 UTC Sundays) |

Everything below the `---` line in each file is the prompt, verbatim, with one redaction: `<INBOX_FOLDER_ID>` stands for the Drive folder ID of the Undraft inbox. The live routines carry the real ID. This repo is public, and the ID is left out so the inbox isn't one link-share away from the internet. Keep that folder shared with no one.
