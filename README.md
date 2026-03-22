# Undraft

A personal communication translation tool for turning raw technical thinking into audience-appropriate output. Not a writing improver — a translation system for people who have substance but lack a reliable process for making it legible.

Takes messy input (meeting dumps, architecture notes, rants, things you just figured out) and produces versions for different audiences without removing the struggle, the nuance, or the voice.

## What's in this repo

| File | What it is |
|------|-----------|
| `undraft-system-prompt.md` | The system prompt. Paste everything below the `---` line into a Claude Project. This is the product. |
| `undraft design.md` | Design doc covering the problem, workflow, output modes, phases, and success criteria. Reference material, not needed for the tool to work. |
| `claude.md` | Voice models, banned AI writing tells, and operating rules. Defines what good output looks like and what patterns to kill. Also serves as project instructions for Claude Code. |

## Setup

1. Create a new Claude Project called "Undraft" at [claude.ai](https://claude.ai)
2. Open `undraft-system-prompt.md`
3. Copy everything below the first `---` line
4. Paste it into the project's system prompt (Project Instructions)
5. Also paste the contents of `claude.md` into the project knowledge or system prompt — this gives the model the voice rules and kill list
6. Start a conversation. Paste in raw input. Get back translations.

## Output modes

Every input produces four outputs by default:

- **Core Point** — 1-3 sentences. What you're actually saying.
- **Up** — Translated for leadership. Outcome-led, direct, no corporate sludge.
- **Peers** — Translated for senior engineers and architects. Full technical depth, preserves tradeoffs and learning journey.
- **Friction Report** — Line-by-line callouts of defensive, inflated, self-erasing, vague, abrasive, or performative patterns.

**Lobby** (cross-functional partners) is available on request by adding `AUDIENCE: cross-functional` to your input.

## Steering the output

Optional tags you can add before your raw dump:

```
AUDIENCE: [who this is for — skip for all default modes]
CONTEXT: [what prompted this — a meeting, a decision, a win]
INTENT: [what you want the reader to DO or FEEL]
```

Tone adjustments mid-conversation: "too corporate," "too raw," "pull back the anger," "shorter," "more detail."

## What this is not

Not a blog. Not a publishing pipeline. Not an app. It's a system prompt in a Claude Project. If the translation works, the platform can evolve. Get the prompt right first.
