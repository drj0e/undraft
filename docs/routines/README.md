# Routine prompts

The two scheduled Claude routines that run the blog pipeline. The prompts are configured in claude.ai (Routines), which keeps no history; these files are the versioned copy. Change the file, then paste it into the routine, so the diff here is the record of what the routine was told and when.

| File | Routine | Schedule |
|---|---|---|
| `writer.md` | Blog post draft candidate | `0 13 */3 * *` (13:00 UTC every third day of the month) |
| `reviewer.md` | Blog pre-publish reviewer (fixed) | `30 13 * * *` (13:30 UTC daily) |

Everything below the `---` line in each file is the prompt, verbatim.
