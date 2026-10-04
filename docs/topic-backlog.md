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

- B-2026-10-04-1 | core | The only hook with a date on it: the vendor named a replacement model on 2026-09-30 and the old one stops answering on 2026-11-30, so a post about dating acceptance criteria before the notice lands while readers are inside that window. Shape is argument, which the NEXT POST line allows.
- B-2026-10-04-2 | adjacent | The step out the feed is due for: security review has never appeared here, and two September disclosures give it an anchor without any invented experience. Both primary pages were unreachable from the scout's network, so the writer verifies any figure on them before quoting it.
- B-2026-10-04-5 | core | Strongest evergreen delta: a public standard that retires terms on a schedule, taken apart into the three parts an internal glossary is missing.

One adjacent item this week, short of the quota. The other candidates that looked like a step out (vendor evaluation of a model supplier, an agent's identity model, a review-depth default, a watcher's attribution line) extend sixty-days-notice, the-author-you-cant-ask, the-default-is-the-policy or who-watches-the-watcher, so they were labeled core or killed. Nothing expired: every open item was added 2026-09-27. The scout's network policy blocked fda.gov, federalregister.gov, github.blog, docs.github.com, cdisc.org, evs.nci.nih.gov, nist.gov, picscheme.org and manifold.security on this run; hooks marked unverified below carry no figures from those pages.

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

### B-2026-09-27-3 | core | used: the-old-name-still-answers
- added: 2026-09-27
- thesis: Putting meaning in a renamable column name instead of a frozen key only helps once something actually rereads the name after it changes, and nothing in most pipelines does.
- nearest post: printed-on-the-tube; new point: that post stopped at "don't freeze meaning into the key," and the fix it recommended, a renamable name, still needs a subscriber that reruns when the name changes, which is exactly the missing piece documentation rot lives in.
- prior art: queries "documentation rot AI generated code nobody recertifies docs" and "nothing fails when docs are wrong"; found consistent framing across current writing ("tests fail when code is wrong, nothing fails when docs are wrong," "no script knows the doc exists") and a recurring proposed fix of generating more doc content with AI, which the same sources say fails within months; delta: this post's delta is naming the missing piece as a subscriber problem this blog already solved for keys and never extended to names.
- hook: none (evergreen)
- shape: note
- tags: data, ai-tooling
- anchor: printed-on-the-tube (published), agents-dont-read-the-glossary (published)

### B-2026-09-27-4 | adjacent | used: education-training-and-experience
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

### B-2026-10-04-1 | core | open
- added: 2026-10-04
- thesis: A deprecation notice names the replacement model, and acceptance criteria for moving to it count as evidence only if they were written and dated before that notice, which is what a predetermined change control plan requires of device makers and what an eval suite assembled after the email cannot be.
- nearest post: sixty-days-notice; new point: that post said re-earned evidence has to come from a script and put the model string under change control; this says what the script has to contain and when its criteria have to be dated, and names the regulator's form for exactly that, the PCCP's modification protocol with pre-specified acceptance criteria.
- prior art: queries "predetermined change control plan PCCP applied to LLM agent pipeline model version update validation" and "LLM model change regression acceptance criteria pre-specified before replacement model validated workflow pharma"; found PCCP explainers written for device makers (description of modifications, modification protocol with acceptance criteria, impact assessment), one regression-testing article for validated workflows that calls version-specific regression prudent, and an arXiv preprint on preregistering analyses before the next LLM release to avoid p-hacking; delta: none hand a pipeline owner the test, which is to check the date on every acceptance criterion in the model-change protocol against the date of the notice that named the replacement, and to treat a criterion written after it as a description of the new model's behavior rather than a requirement it met.
- hook: [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) (verified 2026-10-04): on 2026-09-30 the vendor notified developers that claude-sonnet-4-5-20250929 retires on 2026-11-30 with claude-sonnet-5-5 as the recommended replacement, three days after sixty-days-notice published, and the same page advises testing applications with the new model before the retirement date, which is criteria written after the replacement is known. Deadline 2026-11-30. A second this-week angle exists if the writer can confirm it on fda.gov: trade coverage says CDRH's FY2027 guidance agenda, posted 2026-10-01, lists finalizing the AI-enabled device lifecycle guidance as a priority (fda.gov was not reachable from the scout's network).
- shape: argument
- tags: compliance, ai-tooling, life-sciences
- anchor: sixty-days-notice and one-page-from-1924 (published); the FDA final guidance "Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions" (Federal Register 2024-28361, 2024-12-04; fda.gov and federalregister.gov were not reachable from the scout's network, so the writer confirms the three-part structure on the page before quoting it).

### B-2026-10-04-2 | adjacent | open
- added: 2026-10-04
- thesis: A security review of a coding-agent setup lists what the agent may do inside a session, and both of September's agent disclosures fell outside that list: one ran code before the first prompt appeared, the other published to repositories the organization never watched.
- nearest post: the-stack-nobody-talks-about; new point: that post drew the system as everything that makes model output selectable, constrainable, auditable, and stoppable, all of it inside the run; this says the review boundary has to start at clone and end at every destination the credentials can reach, and gives the two lists to write.
- prior art: queries "coding agent threat model what runs before first permission prompt security review session boundary" and "coding agent security review checklist what runs when repository opens where agent can publish outside organization monitoring"; found the current checklists (OWASP's secure-agent playbook, several 8- and 12-control lists) that name AGENTS.md, hooks, package scripts and CI workflows as trust surfaces and ask for egress allowlists, and Zenity's "permission boundary myth" piece arguing that permitted actions are the problem; delta: none pose the review as two inventories with a join, everything that executes between clone and first prompt and every place the agent's credentials can write that the organization's monitoring doesn't read, where the finding is whatever appears on the second list under a personal account.
- hook: Manifold Security's GitSpawn disclosure, 2026-09-01 ([primary](https://www.manifold.security/blog/ai-coding-agents-git-hijack)), and Glow Labs' PixelLeak report, 2026-09-29 (primary URL not located; [coverage in The Register, 2026-09-29](https://www.theregister.com/ai-and-ml/2026/09/29/ai-models-keep-posting-screenshots-showing-sensitive-data-from-inside-tech-companies/5299640)). Neither was reachable from the scout's network, so no counts from either are carried here; the writer verifies on the primary pages before quoting any. PixelLeak is the this-week half.
- shape: argument
- tags: ai-tooling, automation, security (proposed new tag; usable once a second open item carries it)
- anchor: the-stack-nobody-talks-about and agent-world-reinventing-part-11 (published); supporting: the Claude Code CHANGELOG.md on GitHub (verified 2026-10-04) records repeated fixes for hooks, status-line commands and background sessions that ran before workspace trust was accepted, which is the before-the-first-prompt surface described in a vendor's own words.

### B-2026-10-04-3 | core | open
- added: 2026-10-04
- thesis: A watcher whose notes go to the person rather than back to the agent, and which says "you" or "the main agent" for each decision it flags, records a fact a run transcript flattens: which party made each call.
- nearest post: who-watches-the-watcher; new point: that post asked who checks whether output is safe to ship; this is about where the checker's report goes and what it attributes, and argues the per-decision attribution is the part worth keeping even when the flags themselves are noise.
- prior art: queries "second agent monitors coding agent reports to human not to the agent flags decisions attribution oversight" and "agent oversight notes record whether human or agent made each decision responsibility attribution per decision"; found monitor-and-escalate designs (Partnership on AI's real-time failure detection paper, arXiv work on oversight capacity and approval fatigue), identity vendors' "decision attribution" (tracing an action to the identity and policy that allowed it), and agent decision records that log human approvals; delta: those attribute to a principal or record that an approval happened; none split, inside one session, the decisions the person typed from the decisions the agent took on its own, and the test is to pick any consequential action in your last transcript and say in one word who decided it.
- hook: [Claude Code changelog](https://code.claude.com/docs/en/changelog) (verified 2026-10-04): 2.1.287 (2026-10-01) added "You should know", a built-in mod where a side agent watches your back and flags things you or Claude might miss; 2.1.288 (2026-10-02) changed its notes to say "we", "the main agent" or "you" depending on who was responsible for a decision.
- shape: teardown
- tags: ai-tooling, automation, code-quality
- anchor: who-watches-the-watcher and the-author-you-cant-ask (published); the two changelog lines above. The held post the-guard-the-agent-can-see already owns the point that a verdict fed back to the agent becomes a target, so this item stays on attribution and does not re-argue that.

### B-2026-10-04-4 | core | open
- added: 2026-10-04
- thesis: Review depth became a vendor setting with a default, so a quality record that names the review step without naming the effort level it ran at describes a control the vendor can reset for every repository at once, and did on 2026-09-28.
- nearest post: the-default-is-the-policy; new point: that post argued a schema default is the retention policy because the write is the only moment the decision can enter the system; this says a review tool's default effort level is the review policy for the same reason, with the added fact that the vendor can rewrite it for existing repositories in one change, which a schema default can't.
- prior art: queries "AI code review effort level setting default depth policy who decides review thoroughness" and "AI code review effort level change control validated SDLC review depth setting documented quality system"; found vendor framing (Qodo's review effort modes, GitHub's effort-level changelogs), settings explainers, and general advice to tier review depth by risk; delta: none treat the effort level as a configuration item of the quality system, and the test is whether the shop's record of its review control names the level and whether anything in the shop logged 2026-09-28 as a change.
- hook: GitHub Changelog, ["Copilot code review: API support and new default effort level"](https://github.blog/changelog/2026-10-02-copilot-code-review-api-support-and-new-default-effort-level/) (2026-10-02) and "Upcoming changes to GitHub Copilot policies and billing" (2026-08-28), which per their own titles and multiple independent summaries make Balanced the default effort level for new and existing repositories and organizations from 2026-09-28, keeping an explicit Lite selection. Unverified: github.blog was not reachable from the scout's network, so the writer loads both pages before using the date or the existing-repositories detail.
- shape: argument
- tags: ai-tooling, code-quality, compliance
- anchor: the-default-is-the-policy, generation-got-cheap-review-didnt and not-useful (published).

### B-2026-10-04-5 | core | open
- added: 2026-10-04
- thesis: A standards body retires terms every quarter because each retirement ships inside a dated package with a changes file and a mapping instruction to the term that replaces it, and the governance programs that never retire a definition have the authority and lack the package.
- nearest post: record-is-not-the-definition; new point: that post argued retirement is a distinct event that governance programs never build; this names the three parts a working retirement has (a dated release, a diff file that lists retired terms, and a per-term replacement instruction) using a public standard that performs it on a schedule.
- prior art: queries "CDISC controlled terminology deprecated terms retired versioning lesson data governance retire definition" and "controlled terminology retired terms mapping instructions quarterly release why standards bodies can retire terms enterprises cannot"; found CDISC's controlled terminology FAQ and conference papers (PharmaSUG 2016 DS16, PhUSE 2012 PP24) describing the quarterly release, the changes file listing new, changed and retired terms with instructions for mapping retired terms, and sponsor up-versioning practices; nothing turns the mechanism into a prescription for an internal glossary; delta: the test is whether your glossary has a dated release and a "replaced by" field per term, because a retirement with nowhere to be written down never happens.
- hook: none (evergreen). Trade coverage reports a quarterly terminology package published 2026-09-25, but cdisc.org and evs.nci.nih.gov were not reachable from the scout's network, so that date is unverified.
- shape: teardown
- tags: data, life-sciences, compliance
- anchor: record-is-not-the-definition and a-blank-without-initials (published; the latter already cites SDTMIG); the CDISC Controlled Terminology FAQ (https://www.cdisc.org/kb/articles/controlled-terminology-faqs) and the NCI EVS changes files (https://evs.nci.nih.gov/ftp1/CDISC/), public but not loaded by the scout on 2026-10-04.
