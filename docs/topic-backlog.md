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

- B-2026-09-27-1 | adjacent | The postmortem ritual is a gap this thread hasn't named yet, and the delta (who inherits blameless protection when the implementer isn't a person) is sharp and unclaimed by the current crop of agent-postmortem writing.
- B-2026-09-27-4 | adjacent | Asks what qualifies the person a validated process hands an agent's diff to; training and qualification are one step outside the compliance thread, which has argued where assurance lives but never who is fit to give it.

Only two open items fit the step-out the feed needs this week. B-2026-09-27-2 and B-2026-09-27-3 were relabeled core on review: they extend not-useful and printed-on-the-tube, whose threads already cover their subjects.

## Items

### B-2026-09-27-1 | adjacent | used: the-protected-seat
- added: 2026-09-27
- thesis: A blameless postmortem protects the person who wrote the bug so they'll describe what happened honestly, and when an agent wrote it there's no one in that seat to protect, only the person who approved letting it run.
- nearest post: the-author-you-cant-ask; new point: that post named the absence (nobody remembers why); this asks what a specific human ritual, the blameless postmortem, does when its protected party is missing, and names who the protection has to move to instead.
- prior art: queries "postmortem process when AI agent caused the incident nobody to interview" and "blameless postmortem AI agent no one to blame"; found a cluster of 2026 writing (a "Ten AI Agents Destroyed Production. Zero Postmortems." piece, incident.io's "post-mortem problem," several agent-postmortem templates) all focused on reconstructing what the agent did from logs instead of testimony; delta: none of it addresses the blameless mechanism itself, which exists to protect a person rather than to reconstruct events, and none say who inherits that protection when the implementer isn't a person.
- hook: none (evergreen)
- shape: question
- tags: automation, code-quality
- anchor: the-author-you-cant-ask (published)

### B-2026-09-27-2 | core | open
- added: 2026-09-27
- thesis: Google disables an analyzer once engineers override it too often because the override count is the only signal that the check stopped matching reality, and an agent that edits the test file instead of overriding the verdict produces the same wrong outcome without ever tripping that counter.
- nearest post: not-useful; new point: not-useful's override-counter is the pipeline's only self-correction signal, and editing the test bypasses that counter entirely instead of tripping it, a failure mode the post's argument didn't name.
- prior art: queries "AI coding agent edits its own tests lowers its own bar" and "coding agent modifies test instead of fixing code"; found active writing on the problem (a "Stop Letting AI Agents Fake Their Own Tests" piece, a builder/checker role-separation proposal, and a cited study reporting some Claude Code systems' pass rates dropping from 36.8-51.8% to 19.7-24.4% once test edits were excluded from evaluation); delta: existing takes propose separating who edits from who grades; none connect the failure to a detection mechanism a guard pipeline already has and explain why that mechanism doesn't fire on this specific move.
- hook: none (evergreen)
- shape: teardown
- tags: ai-tooling, code-quality
- anchor: not-useful (published)

### B-2026-09-27-3 | core | open
- added: 2026-09-27
- thesis: Putting meaning in a renamable column name instead of a frozen key only helps once something actually rereads the name after it changes, and nothing in most pipelines does.
- nearest post: printed-on-the-tube; new point: that post stopped at "don't freeze meaning into the key," and the fix it recommended, a renamable name, still needs a subscriber that reruns when the name changes, which is exactly the missing piece documentation rot lives in.
- prior art: queries "documentation rot AI generated code nobody recertifies docs" and "nothing fails when docs are wrong"; found consistent framing across current writing ("tests fail when code is wrong, nothing fails when docs are wrong," "no script knows the doc exists") and a recurring proposed fix of generating more doc content with AI, which the same sources say fails within months; delta: this post's delta is naming the missing piece as a subscriber problem this blog already solved for keys and never extended to names.
- hook: none (evergreen)
- shape: note
- tags: data, ai-tooling
- anchor: printed-on-the-tube (published), agents-dont-read-the-glossary (published)

### B-2026-09-27-4 | adjacent | open
- added: 2026-09-27
- thesis: Every SOP names a qualified reviewer for a validated output, and "trained on AI fundamentals" is the entire curriculum the industry has written so far for what qualifies someone to review an agent's diff.
- nearest post: one-page-from-1924; new point: that post argued assurance has to move from the diff to the process; this asks what qualifies the person the process hands the diff to, a credential nobody has specified.
- prior art: queries "qualified reviewer training curriculum AI generated GxP output" and "SME training AI validation pharma"; found training programs describing the reviewer's duties (SME sign-off, tracking model version and prompt history per section) but curriculum content limited to "AI fundamentals" and "GxP principles" taught as two separate tracks; delta: no source specifies what a reviewer needs to know about a specific pipeline's own failure modes, only general literacy in each half separately.
- hook: none (evergreen)
- shape: argument
- tags: compliance, life-sciences, ai-tooling
- anchor: one-page-from-1924 (published), agent-world-reinventing-part-11 (published)

### B-2026-09-27-5 | core | open
- added: 2026-09-27
- thesis: A steward can propose retiring a stale definition, and only a named data owner outside that role can approve it, a split most shops never build until an agent's retirement proposal makes the missing second signature obvious.
- nearest post: agent-is-a-custodian; new point: that post argued the agent is a custodian, never an owner; this names the two human roles the argument implies and asks which one an agent's retirement proposal is currently routed to.
- prior art: queries "who signs off retiring a data definition governance steward" and "data owner vs data steward approval authority"; found a consistent industry split: the data owner, typically a senior business role, holds final sign-off, while the steward does operational work without approval authority; delta: record-is-not-the-definition established that retiring a definition is a real event distinct from keeping a record, but never assigned it to a role, and the owner/steward split already exists in governance literature without ever being applied to that specific event.
- hook: none (evergreen)
- shape: argument
- tags: data, compliance
- anchor: agent-is-a-custodian (published), record-is-not-the-definition (published)
