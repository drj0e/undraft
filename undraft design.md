# Undraft: Design Document

## Problem Statement

Senior technical leaders who do real, hard work often have an inverse relationship between substance and visibility. The people with the most to say communicate the least, because:

1. They distrust corporate performance language and refuse to use it
2. They associate self-promotion with the people who do it badly
3. Raw technical thinking doesn't translate cleanly to leadership, public, or cross-functional audiences
4. The friction of "how do I say this without sounding like an asshole / a braggart / a pushover" stops them from writing at all
5. Blank-page paralysis kills output even when there's plenty of real material

The result: real work stays invisible. Career progress, influence, and external reputation lag behind actual capability.

**Undraft** is a personal AI translation layer that takes raw, honest, messy input and produces audience-appropriate output — without removing the struggle, the nuance, or the voice of the person who did the work.

It is not a writing improver. It is a translation system for people who have substance but lack a reliable process for making that substance legible.

---

## Core Design Principles

1. **Translate, don't shrink.** The hard parts, the failures, the trial-and-error — these ARE the substance. Remove clutter, not reality.
2. **Preserve intent over polish.** If a rewrite changes what the author meant, it failed, no matter how clean it sounds.
3. **The friction report is the product.** Showing someone WHERE their writing will be misread is more valuable than rewriting it for them.
4. **No corporate sludge.** If the output could have been written by a comms department, it's wrong.
5. **Reduce friction, not standards.** Make it easier to START writing, not easier to write badly.

---

## Workflow: How You Actually Use This

### Daily Loop (5-15 minutes)

```
Raw input (voice dump, notes, frustration, journal entry)
    ↓
Paste into Undraft
    ↓
Get back:
  - Core Point (what you're actually saying)
  - Up (translated for leadership)
  - Peers (translated for senior technical audience)
  - Friction Report (what's defensive, inflated, vague, etc.)
    ↓
Use the version you need, or iterate
```

### Input Types

You don't need special formatting. Just dump. But if you want to steer the output, you can use optional tags:

```
AUDIENCE: [who this is for — skip if you want all modes]
CONTEXT: [what prompted this — a meeting, a decision, a frustration, a win]
INTENT: [what you want the reader to DO or FEEL after reading]

[your raw dump here — any format, any length, any level of mess]
```

### Output Modes

**Default (produced on every input):**

| Mode | What It Does | When To Use |
|------|-------------|-------------|
| **Core Point** | 1-3 sentences. What you're actually saying underneath all the words. | Always produced first. Reality check on your own thinking. |
| **Up** | Translated for leadership (director-level and above). Outcome-led, removes defensiveness, keeps substance, does not dumb down. | Slack messages to leadership, email updates, status reports, internal presentations. |
| **Peers** | Translated for senior engineers, architects, tech leads. Direct, technically precise, preserves the learning journey and tradeoffs. Closest to the author's natural voice but organized. | Architecture discussions, technical write-ups, peer Slack channels, blog drafts. |
| **Friction Report** | Line-by-line callouts of what's defensive, inflated, self-erasing, vague, or likely to be misread. | Always produced last. The most valuable output. Teaches you your own patterns over time. |

**Opt-in (produced when requested via AUDIENCE tag):**

| Mode | What It Does | When To Use |
|------|-------------|-------------|
| **Lobby** | Cross-functional partners (PM, QA, marketing, non-technical stakeholders). Same substance, adjusted vocabulary. Doesn't assume deep technical context. | When the input is going to a cross-functional audience. Evaluate in Phase 3 for promotion to default. |

### Phase 2 Modes (add after MVP is validated)

| Mode | What It Does | When To Use |
|------|-------------|-------------|
| **Blog/Public** | Keeps the struggle and lessons. Written for an external audience of peers. | Publishing, content, building reputation. |
| **Executive Summary** | Short, outcome-led, decision-friendly. | When leadership needs the 30-second version. |

---

## Input/Output Formats

### Input: Anything

The system should handle all of these without special formatting:

- Stream-of-consciousness text dumps
- Bullet point lists of observations
- Copy-pasted Slack rants
- Architecture decision notes
- Post-meeting frustration journals
- Voice transcription dumps (messy grammar is fine)
- Code comments or PR descriptions that need to become human-readable
- "Here's what happened and why I'm pissed about it" narratives

### Output: Structured Markdown

Every response follows this structure:

```markdown
## Core Point
[1-3 sentences: what you're actually saying]

## Up
[Translated for leadership — outcome-led, direct, no corporate sludge]

## Peers
[Translated for senior technical audience — full depth, tradeoffs, learning journey]

## Friction Report
[Line-by-line callouts with categories]

Categories:
- 🛡️ DEFENSIVE: sounds like you're pre-justifying
- 📢 INFLATED: overselling the result or your role
- 👻 SELF-ERASING: hiding your contribution or minimizing real work
- 🌫️ VAGUE: the reader won't know what you mean
- 🔥 ABRASIVE: the point will get lost because the tone is too hot
- 🎭 PERFORMATIVE: sounds like corporate theater
- ⚠️ MISREAD RISK: likely to be interpreted differently than intended
```

---

## MVP Feature Set

### Include Now

1. **System prompt in a Claude Project** — no code, no build, no deployment
2. **Four output modes**: Core Point, Up, Peers, Friction Report (plus Lobby as opt-in)
3. **Audience inference** — if you don't specify, it guesses from context
4. **Pattern tracking** — the friction report flags recurring patterns
5. **Tone calibration** — responds to "too corporate" / "too raw" / "pull back the anger" type feedback
6. **Input flexibility** — handles any format without requiring structure

### Explicitly Do NOT Build Yet

- Blog/public mode (add when you've validated the core loop)
- Executive summary mode
- Voice input pipeline (just paste transcripts for now)
- Integration with repos, CI, or other tools
- Template library
- Multi-turn editing workflows (keep it single-pass with iteration)
- Publishing pipeline
- Analytics or dashboards

---

## Platform Decision: Claude Project

**Why a Claude Project and not something else:**

| Option | Verdict |
|--------|---------|
| Custom GPT | Wrong ecosystem. You're on Claude. |
| Local tool / CLI | Overengineering. You don't need offline access for writing. |
| Repo workflow | Adds friction. The whole point is reducing friction. |
| Lightweight app | Build cost with no validated demand yet. |
| Claude Project | Zero build cost. Persistent system prompt. Iterate the prompt, not code. Test today. |

**Migration path if it works:** If you validate the workflow and want to scale it, the system prompt becomes the core of a Claude Code integration or API-backed tool. The prompt IS the product. Get it right first.

---

## Phases and Timeline

Two parallel tracks from day one. Track 1: get the translation engine right. Track 2: stand up a publishing destination so there's somewhere real to put the output. Neither track waits for the other.

### Phase 1 — Translation Engine (Weeks 1-2)

Rework the system prompt to produce two audience tiers by default: **Up** (leadership — director-level and above) and **Peers** (senior engineers, architects, tech leads). Keep Core Point and Friction Report. Drop the current Raw Truth / Professional split in favor of this elevator model. Add **Lobby** (cross-functional partners) as an opt-in tier when the input specifies that audience.

Set up a Claude Project with the updated prompt. Test daily with real inputs — architecture tradeoffs, things you just figured out, post-meeting dumps. Tune the prompt based on what comes back wrong. Keep the prompt versioned in the repo so iterations are tracked and you're not editing in a web UI with no history.

Maintain a scratch file (`friction-patterns.md`) that tracks which Friction Report categories repeat across inputs. Every time a pattern shows up more than once, log it. By end of Phase 1, the top 3-5 recurring communication habits should be identified. This serves two purposes: it's self-improvement data that makes the Friction Report smarter over time, and it's future blog material. "Here are the five ways I consistently undermine my own writing" is a post that writes itself.

**Success gate:** 10+ real inputs processed. Outputs consistently pass the "would I send this" test for Up and the "would my peers respect this" test for Peers. Top 3-5 friction patterns identified and logged.

### Phase 2 — Blog + First Post (Weeks 2-3, overlapping with Phase 1)

Stand up a blog using Hugo. Hugo is the right choice: single Go binary, no dependency chain, no runtime, no temptation to yak-shave on build tooling. Pick a clean theme. Ship it.

Buy a custom domain in week 1. A domain is $12/year and it's the difference between experimenting and publishing. The psychological commitment matters. Point it at GitHub Pages and move on.

Take one of the best Phase 1 outputs and turn it into the first published post. It doesn't have to be perfect. It has to exist.

**Success gate:** Blog is live on a custom domain. One post is published. LinkedIn has a link to it.

### Phase 3 — The Flywheel (Weeks 3-6)

Establish the rhythm:

- **Daily (5-10 min):** Raw dumps into Undraft. Meeting just ended, figured something out, made a tradeoff call. Paste, get translations, move on.
- **Mid-week (30 min, 2-3x):** Deliberate writing. Drafting a Viva Engage post, an architecture rationale, a response to a leadership question.
- **Weekend (1 hour):** Review the week's outputs. Which dumps have a public point? Pick one, feed it back through for the Peers voice, edit, publish.

Post to Viva Engage weekly, even if short. Two posts in six weeks is too sparse to test whether internal visibility compounds. Weekly presence — even a few paragraphs on "here's what I learned this week" or "here's a decision we made and why" — builds the pattern of someone who shares what they know. The compound effect of regular internal presence is faster than the external blog.

By mid-Phase 3, start sharing drafts with 1-2 trusted peers before publishing. Not for approval — for calibration. The Friction Report catches your patterns. A human reader catches what it can't: things that land differently than intended, missing context that's obvious to you but invisible to the reader. This is a feedback loop the tool can't replace.

This cadence will collapse during heavy work weeks. Product investigations, sprint commitments, production incidents — these will eat the writing time and that's fine. The plan expects this. The measure of success isn't an unbroken streak. It's recovery speed. When the heavy week ends, how fast do you get back to the rhythm? A week off followed by a weekend review session is healthy. Three weeks off with mounting guilt is a failure mode. Define "getting back on the horse" concretely: the first thing you do after a gap is one raw dump. Not a full blog post. One dump. The flywheel restarts from the smallest motion.

**Success gate:** Published 3-4 posts AND recovered from at least one week where writing didn't happen. Weekly Viva Engage posts happening. At least one draft has been reviewed by a trusted peer before publishing.

### Phase 4 — Evaluate and Adapt (Weeks 6-10)

Do not pre-commit to specific automation at this stage. At week 6 you won't know yet whether the bottleneck is publishing friction or content generation. These are different problems with different solutions.

If publishing mechanics are the bottleneck — you have drafts sitting around because getting them onto the blog or LinkedIn is annoying — then automate the pipeline. Move to Claude Code, automate deploys, add cross-posting.

If content generation is the bottleneck — you're not producing enough raw material or the prompt isn't giving you usable output — then the prompt needs work, not the pipeline. Go back to the translation engine and tune it.

If neither is the bottleneck and the system is working, leave it alone. Don't build infrastructure for a problem you don't have.

Evaluate whether Lobby needs to be promoted from opt-in to default based on actual usage. Evaluate whether Peers voice works for external/public audiences or whether a distinct Street/Public tier is needed for the blog.

**Success gate:** The actual bottleneck has been identified and addressed. Publishing friction is low enough that the constraint is "do I have something worth saying" not "how do I get it out there."

### Across All Phases — Feedback Loops

The tool has a built-in feedback loop (the Friction Report). But a tool can only catch patterns it's been told to look for. Three additional feedback loops run alongside:

1. **Friction pattern tracking** (Phase 1 onward) — the scratch file that logs recurring patterns. Review it monthly. Update the system prompt to address patterns that keep showing up.
2. **Peer review** (Phase 3 onward) — trusted humans reading drafts before publish. Catches blind spots the tool can't see.
3. **Self-assessment** (Phase 4) — are you catching your own patterns before the Friction Report flags them? If yes, the tool is training you. If no, the Friction Report needs to be sharper or you need to read it more carefully.

The end state isn't perpetual dependence on the tool. It's building the muscle until you start catching your own defensive framing, self-erasure, and inflation before you even paste the dump in. The tool should make itself less necessary over time.

---

## Blogging / Content Pipeline (Phase 2)

Once the core loop is working, the content pipeline looks like this:

```
Daily use of Undraft
    ↓
Accumulate Peers outputs in a notes folder
    ↓
Weekly: review Peers outputs, identify 1-2 that have a public point
    ↓
Feed back into Undraft with AUDIENCE: Blog/Public
    ↓
Get a Blog/Public draft that preserves struggle and lessons
    ↓
Edit manually (the bot drafts, you own the final voice)
    ↓
Publish
```

**Content types that naturally emerge from this workflow:**

- "What I learned building X" (architecture writeups with real mistakes)
- "The problem with Y" (opinion pieces grounded in experience)
- "Here's how I actually solved Z" (practical technical content)
- Meta-content: "I built a bot to help me stop sounding like corporate sludge" (this project itself)

**Voice preservation in public content:**

The blog mode should follow these rules:
- Keep the chronology of discovery (what you tried first, what failed, what worked)
- Include the "I was wrong about X" moments — these are the most valuable parts
- Don't retroactively make yourself look smarter than you were
- Technical depth is a feature, not a bug — your audience is peers, not recruiters

---

## How To Test the MVP

1. Create a new Claude Project called "Undraft"
2. Paste the system prompt (see companion file: `undraft-system-prompt.md`)
3. Take a real piece of raw input — a Slack message you wrote today, a frustration from a meeting, an architecture note
4. Paste it in with no formatting
5. Evaluate: Does the Core Point actually capture what you meant? Does the Up version sound like you or like corporate sludge? Does the Peers version preserve the technical depth and tradeoffs? Does the Friction Report catch real patterns?
6. Iterate the system prompt based on what's wrong

**First test inputs to try:**
- A Slack message where you were frustrated about a technical decision
- An architecture note explaining why you chose approach A over B
- A status update you'd send to leadership about an enterprise product or AI workflow tool
- A raw dump about something you learned building an internal tool

---

## Success Criteria

After one week of use, you should be able to answer YES to:

1. Am I actually using this daily? (If not, the friction is still too high)
2. Does the Core Point extraction consistently nail what I meant?
3. Has the Friction Report taught me at least one pattern I didn't see in myself?
4. Have I sent at least one Up output that I wouldn't have written from scratch?
5. Do the outputs sound like me, not like a writing assistant?

If you can't answer yes to all five after a week, the system prompt needs work — not the platform, not the features.