# Pre-Publish Review Checklist

The standard the model reviewer (the daily "Blog pre-publish reviewer" routine) follows before stamping a post `reviewed: true`. It lives in the repo so the bar is version-controlled and auditable, the same way `review-log.md` is. The routine prompt should say: *"Follow docs/review-checklist.md. Log per the format there."*

Scope: future-dated, not-yet-live posts that lack `reviewed: true`. For each, work the checks below, then write one line to `docs/review-log.md`.

## Checks

1. **Self-citation fidelity (FAIL bar).** For every claim a post makes about what another post said, listed, or argued, open the cited post and verify the claim against it. This is not "is it roughly consistent" — it is "does it match."
   - Verify the **count and membership** of any enumeration. If the post recaps a list, it must have the same items the source listed. A recap that drops, adds, or substitutes a member is a **FAIL**, not an acceptable "simplification." Changing how complete a list looks changes what the reader concludes.
   - Watch for a **new idea framed as a forgotten one**: "I listed A, B, C and left one off." That is only faithful if the source listed exactly A, B, C as a closed set. If the source's list had other members, or never claimed to be complete, the framing is false even when each individual word checks out.
   - `scripts/lint_posts.py` prints two advisories that point you at the risky spots: "possible dropped list member" (a citing list that is a subset of the linked post's list) and "self-citations to verify." Treat every advisory line as a required check, not a suggestion. The script only surfaces; you decide.
   - **Worked example (the miss this check exists for):** *the-property-i-left-off-the-stack* recapped *the-stack-nobody-talks-about*'s "selectable, constrainable, auditable, affordable, and stoppable" as "selectable, constrained, audited, and stoppable" — silently dropping *affordable* — then presented "resumable" as the property it had "left off," though resumable was never on that list. The earlier review waved this through as "omits 'affordable' but does not contradict it, a simplification." That was the wrong call. Dropping a member to set up the hook is a FAIL.

2. **Substance recycling (FAIL bar).** Compare against the nearest prior post by theme. A fresh opening over a retread argument is still a retread. The post must carry one new load-bearing point the named neighbor does not make. Name that point in the log.

3. **External-source truth (FAIL bar).** Verify every statistic, named-entity claim, quote, and outbound link via WebFetch. An uncited number or a dead/misquoted link is a FAIL. (The deterministic gate already blocks leftover `[SOURCE NEEDED]`/`[JOE]` placeholders.)

4. **Feed clustering (NOTE only, never a hold).** Run `scripts/check_diversity.py`. Log a NOTE on an actionable clash, but do not hold — you cannot fix an adjacency with nothing to slot between.

5. **Rhetorical tics (fix-before-stamp bar).** Run `scripts/check_tics.py`. The deterministic gate already hard-fails the banned phrase forms (`TIC_KILL`); this covers the frequency moves a regex can't judge. If the post under review breaches a per-post budget, uses a move the trailing window has worn out, or extends a closer-shape streak (see CLAUDE.md "Rhetorical Tics — The Rotation List"), reword to break the pattern before stamping. Rewriting a flip or a closer is in the reviewer's scope; changing the argument is not. Log a NOTE naming the tic and the fix. If the post's whole structure is the tic — a flip in every section, a templated closer carrying the thesis — that is a **HELD** like any other failed bar. Flags on already-live posts are context, not work: published history does not get edited for style.

## Outcome

- All FAIL-bar checks pass → set `reviewed: true`; log `PASS` with a one-line rationale per dimension (facts / recycling / self-citation / consistency), naming what you verified.
- Any FAIL-bar check fails → set `draft: true` (quarantine); log `HELD` with the reason. The HELD/NOTE line is what triggers the email alert.

Log format mirrors existing entries, e.g.:
`- 2026-06-26 the-property-i-left-off-the-stack: HELD, self-citation: recaps the-stack-nobody-talks-about's 5-item list as 4, drops "affordable", and frames "resumable" as a left-off member it never was.`
