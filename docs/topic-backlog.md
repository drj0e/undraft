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

- B-2026-10-10-1 | core | This week's verified hook with a window still open: the vendor's own changelog says agent activity fell out of adoption reports for months, can't be backfilled, and stays wrong per IDE until November, while the bill was right the whole time. Shape is argument, which the NEXT POST line allows.
- B-2026-10-10-4 | adjacent | The step out: vendor evaluation has never appeared here, and two verification programs published 2026-09-17 and 2026-10-06 show the supplier qualifying the customer, which is the regulated supplier assessment running backwards.
- B-2026-10-10-2 | core | Strongest delta of the week: the missing check behind Plugin4Shell is installation qualification, a step validated shops already run, and two of four agents still had no fix at disclosure.

One adjacent item this week, short of the quota. Candidates that looked like a step out were labeled core on review: NIST's comment summary on agent authorization extends agent-is-a-custodian, Copilot's local sandboxing extends B-2026-10-04-2, and Haiku 5.5 is sixty-days-notice's next row. Nothing expired: the oldest open items were added 2026-09-27. The network policy was open on this run, so the hooks last week's scout could not load were checked on 2026-10-10 and hold: B-2026-10-04-2's primaries (Manifold, 2026-09-01; Glow Labs at glow.io/blogs/how-ai-agents-exposed-developer-screenshots-from-leading-tech-companies, 2026-09-29, with the 93% personal-account figure), B-2026-10-04-4's changelog (Balanced default from 2026-09-28 for new and existing repositories), and B-2026-10-04-5's release (Package 62, 2026-09-25). Those items' text is left as written.

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

### B-2026-10-04-1 | core | used: before-the-replacement-had-a-name
- added: 2026-10-04
- thesis: A deprecation notice names the replacement model, and acceptance criteria for moving to it count as evidence only if they were written and dated before that notice, which is what a predetermined change control plan requires of device makers and what an eval suite assembled after the email cannot be.
- nearest post: sixty-days-notice; new point: that post said re-earned evidence has to come from a script and put the model string under change control; this says what the script has to contain and when its criteria have to be dated, and names the regulator's form for exactly that, the PCCP's modification protocol with pre-specified acceptance criteria.
- prior art: queries "predetermined change control plan PCCP applied to LLM agent pipeline model version update validation" and "LLM model change regression acceptance criteria pre-specified before replacement model validated workflow pharma"; found PCCP explainers written for device makers (description of modifications, modification protocol with acceptance criteria, impact assessment), one regression-testing article for validated workflows that calls version-specific regression prudent, and an arXiv preprint on preregistering analyses before the next LLM release to avoid p-hacking; delta: none hand a pipeline owner the test, which is to check the date on every acceptance criterion in the model-change protocol against the date of the notice that named the replacement, and to treat a criterion written after it as a description of the new model's behavior rather than a requirement it met.
- hook: [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) (verified 2026-10-04): on 2026-09-30 the vendor notified developers that claude-sonnet-4-5-20250929 retires on 2026-11-30 with claude-sonnet-5-5 as the recommended replacement, three days after sixty-days-notice published, and the same page advises testing applications with the new model before the retirement date, which is criteria written after the replacement is known. Deadline 2026-11-30. A second this-week angle exists if the writer can confirm it on fda.gov: trade coverage says CDRH's FY2027 guidance agenda, posted 2026-10-01, lists finalizing the AI-enabled device lifecycle guidance as a priority (fda.gov was not reachable from the scout's network).
- shape: argument
- tags: compliance, ai-tooling, life-sciences
- anchor: sixty-days-notice and one-page-from-1924 (published); the FDA final guidance "Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions" (Federal Register 2024-28361, 2024-12-04; fda.gov and federalregister.gov were not reachable from the scout's network, so the writer confirms the three-part structure on the page before quoting it).

### B-2026-10-04-2 | adjacent | used: both-ends-of-the-run
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

### B-2026-10-10-1 | core | open
- added: 2026-10-10
- thesis: An adoption dashboard that spells "no agent activity" and "activity it couldn't attribute" the same way is a blank without initials, and the number in the same system that stayed right through months of it was the bill.
- nearest post: a-blank-without-initials; new point: that post put the four absences in a nullable column at the record grain; this puts the same absence in the metric that gets reported up, where an unattributed session reads as a zero, and names the test the bill passes and the dashboard fails: someone would have noticed if it were wrong. Also extends nobody-chose-your-platform, which argued the chart isn't a vote; this says it isn't a measurement either until an absence has a status.
- prior art: queries "Copilot usage metrics undercounted agent activity months adoption dashboards wrong billing correct lesson" and "usage telemetry gap cannot be backfilled adoption dashboard instrumentation lesson platform team metrics"; found the vendor's own changelog, one adoption-funnel pull request that separates "not measured" from zero, an arXiv adoption-telemetry paper (a twice-a-week sampler and a restructured workflow look the same on a usage dashboard), and edtech writing on dashboards that can't compensate for missing collection; delta: none connect the metric-side absence to the record rule that an absence needs a status and a reason, and none hand over the test: for each adoption number you report up, name who would have noticed within a week if a client version stopped identifying itself, and if the answer is only the billing team, the number has no reader.
- hook: [Update your IDE to restore agent activity in Copilot usage metrics](https://github.blog/changelog/2026-10-06-update-your-ide-to-restore-agent-activity-in-copilot-usage-metrics/) (verified 2026-10-10): several IDEs moved agent sessions to the Copilot SDK without identifying which IDE they came from; "Most of that activity was left out of reports, and some was counted as Copilot CLI activity"; billing was not affected; "We can't backfill missing data"; fixes land per IDE from now through November 2026, so the dashboards stay wrong for weeks after the notice.
- shape: argument
- tags: data, leadership, platform-engineering
- anchor: a-blank-without-initials and nobody-chose-your-platform (published); the changelog above.

### B-2026-10-10-2 | core | open
- added: 2026-10-10
- thesis: Installation qualification exists to compare what got installed with what was specified, and four coding agents shipped a plugin pin as the specification with no step that ever ran the comparison.
- nearest post: agent-world-reinventing-part-11; new point: that post bound approval to a hash of the spec and found Part 11 waiting; this finds the second half of the regulated pattern, the IQ, which checks the artifact that arrived against the one that was approved, and shows that a pin without that check is a request rather than a control.
- prior art: queries "AIR Security Plugin4Shell disclosure blog pinned commit branch name coding agents", "verify git checkout landed on pinned commit rev-parse HEAD after clone supply chain branch named like SHA" and "installation qualification verify installed software version checksum matches specification IQ purpose GAMP"; found the disclosure and its write-ups, which already prescribe comparing `git rev-parse HEAD` to the pin, and IQ descriptions in which the supplier records a hash before shipping and the site verifies it after install; delta: none name the missing check as the IQ step validated shops already run, and the test is to list every install or update step in your pipeline (plugins, skills, MCP servers, the model string) and ask which of them compares the installed identity to the pin and fails on mismatch.
- hook: [Plugin4Shell](https://air.security/blog-posts/plugin4shell) (AIR Security, 2026-09-17; verified 2026-10-10): "Every affected agent checks out the pinned commit but never checks that it actually landed there"; background auto-update is the default in Claude Code and Codex; Claude Code fixed in 2.1.179, Codex in 0.146.0, Copilot had no fix at disclosure, Gemini CLI will not be patched. Three weeks old, so not a this-week hook; the unpatched status is the live part.
- shape: teardown
- tags: ai-tooling, compliance, security (proposed new tag; B-2026-10-04-2 also carries it, so two open items now share it)
- anchor: agent-world-reinventing-part-11 and sixty-days-notice (published); the disclosure above.

### B-2026-10-10-3 | core | open
- added: 2026-10-10
- thesis: Most governance programs keep no record of the definitions they refused, and the clinical data standard ships a denied-requests file with the reason for each no and the existing term to use instead, every quarter.
- nearest post: record-is-not-the-definition; new point: that post said governance programs are built to add and can't retire; this names the third operation, refusing, and argues a refusal has to be written where the next requester will find it, with a mapping, or it gets re-requested until it is granted by attrition.
- prior art: queries "data governance glossary log of rejected definition requests denied requests decision record business glossary" and "CDISC controlled terminology new term request denied reasons requests denied file explained"; found decision-record templates with a rejected status, one governed-glossary piece arguing each term should carry what was disputed and decided, and CDISC's FAQ pointing to its denied-requests list with reasons and mappings; delta: none make the refusal an artifact addressed to future requesters, and the test is: when your steward last said no to a new field or term, where is the no written, and does it name the term to use instead.
- hook: none (evergreen). The quarterly release that carried the latest denied-requests update, Package 62, is dated 2026-09-25 on [CDISC's controlled terminology page](https://www.cdisc.org/standards/terminology/controlled-terminology) (verified 2026-10-10); the file itself sits behind a member login, so the post should lean on the FAQ's description and CDISC's published examples of denial reasons rather than the file's contents.
- shape: argument
- tags: data, life-sciences
- anchor: record-is-not-the-definition and a-blank-without-initials (published; the latter already cites SDTMIG); [CDISC Controlled Terminology FAQs](https://www.cdisc.org/kb/articles/controlled-terminology-faqs) (verified 2026-10-10), FAQ 7 on rejected requests and FAQ 12 on the quarterly changes log.

### B-2026-10-10-4 | adjacent | open
- added: 2026-10-10
- thesis: A model vendor now qualifies its life-sciences and security customers before unblocking the model, so the supplier questionnaire runs backwards, and the regulated shop's file on that supplier has to be assembled from what the vendor volunteers.
- nearest post: sixty-days-notice; new point: that post read the deprecation page as a change-control calendar the vendor keeps; this asks what else a supplier assessment of a hosted model can hold when the supplier can't be audited and is the party doing the verifying, and lists the artifacts (deprecation page, usage export, program terms, data-retention conditions) that stand in for the audit.
- prior art: queries "AI model vendor verification program verifies customers credentials oversight inverted supplier qualification GxP supplier audit" and "verified organization program AI API access trust and safety enterprise what the vendor checks about the customer"; found supplier-qualification guides running one way (risk tiering, questionnaires, change notification and uptime commitments for hosted AI) and coverage of vendor-side organization verification (government ID, KYB checks) framed as fraud control; delta: nothing puts the two directions in one frame, and the test is to write down what the vendor required you to prove, then what you required the vendor to prove, and read Annex 11's supplier clause against the second list.
- hook: [Expanding the Cyber Verification Program](https://www.anthropic.com/news/cyber-verification-program) (2026-10-06, verified 2026-10-10): tiers for defense, red-team and specialized access; the vendor will "verify all applicants and request proof of the required security controls"; "Data retention is required for organizations enrolled in the program so that we can monitor for cyber misuse". Alongside [Introducing the Life Sciences Verification Program](https://www.anthropic.com/news/life-sciences-verification-program) (2026-09-17, verified 2026-10-10), which reviews research credentials, security standards and ethical research oversight for drug discovery, clinical development and manufacturing use, with high-risk access renewed every six months.
- shape: argument
- tags: compliance, life-sciences, ai-tooling
- anchor: sixty-days-notice and one-page-from-1924 (published); the two program pages above; [EU GMP Annex 11](https://health.ec.europa.eu/system/files/2016-11/annex11_01-2011_en_0.pdf) section 3, suppliers and service providers (verified 2026-10-10). Reach: no published post is about supplier qualification; sixty-days-notice mentions a supplier change once, as a change-control event.

### B-2026-10-10-5 | core | open
- added: 2026-10-10
- thesis: Larson's factory loop refuses to pick up a task until the project has a written goal, a measurement and a live dashboard, and that precondition is what separates a pile of passed task criteria from a process whose output anyone can judge.
- nearest post: the-stack-nobody-talks-about; new point: that post gave every task acceptance criteria before the agent starts; this says task criteria answer whether each change did what was asked and never whether the asks were right, and shows a loop that makes a project-level measurement a gate on task-level work, with the agent auditing the human's artifacts before the human audits the agent's.
- prior art: queries "software factory pattern Justin McCarthy coding agents loop on a goal" and "agent loop refuses to start work until project goal has metrics dashboard RFC precondition agent-driven development"; found the pattern's lineage (McCarthy's February 2026 essay, Stripe's Minions, a loop-engineering preprint on /loop and /goal commands with machine-checkable completion conditions) and loop-safety guides that want a goal predicate as the stop condition; delta: none put the precondition on the human's side of the loop, and the test is to ask what your agent does when the goal has no measurement: start anyway, or stop and ask for one.
- hook: [Trying the Software Factory pattern.](https://lethain.com/software-factory-experiment/) (Will Larson, 2026-09-20; verified 2026-10-10): step one of his /linear-project-loop checks that the project has an RFC covering goals, measurement and approach plus a dashboard or queries tracking progress, and helps create them if missing. Twenty days old, so evergreen rather than a this-week hook.
- shape: argument
- tags: automation, ai-tooling, leadership
- anchor: the-stack-nobody-talks-about and the-harness-that-forgets (published); Larson's post above. Both loops are public, so no invented experience is needed.
