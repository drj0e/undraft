# Undraft

I have plenty to say about the work I do. The problem was never substance. It was the translation. Raw technical thinking doesn't map cleanly to a Slack message for your boss or a blog post for your peers. The friction of figuring out how to say it without sounding like a showboater or a corporate drone meant I just... didn't say it. The work stayed invisible.

Undraft fixes that. Paste in whatever you've got. A meeting dump, an architecture note, a rant about a bad decision, something you figured out at 2am. You get back versions for different audiences. It keeps the substance. It keeps the voice. It flags where you're being defensive, self-erasing, or vague.

It's a system prompt in a Claude Project. No app. No code. The prompt is the product.

## What's in this repo

`undraft-system-prompt.md` is the system prompt. Everything below the `---` line goes into a Claude Project. That's the tool.

`claude.md` has the voice rules and the kill list. It's a catalog of AI writing tells that are banned from all output. If the output sounds like a LinkedIn post or a press release, these rules are what catch it.

`undraft design.md` is the design doc. Problem statement, output modes, phases, success criteria. Reference material for understanding why things work the way they do. Not needed to use the tool.

`friction-patterns.md` is a scratch file for tracking which Friction Report patterns repeat across inputs. Over time, it builds a picture of your communication habits.

## Setup

Create a Claude Project called "Undraft" at claude.ai. Open `undraft-system-prompt.md`, copy everything below the first `---` line, paste it into the project's system prompt. Then append the full contents of `claude.md` below it, separated by a `---`. Start a conversation and paste in something real.

## Output modes

Every input produces four sections by default.

**Core Point** is 1-3 sentences of what you're actually saying underneath all the words. Gut check on your own thinking.

**Up** is translated for leadership. Outcome-led, direct, no buzzwords, no performative enthusiasm. Your leadership is technical, so it keeps the substance. But it leads with what happened and why it matters.

**Peers** is translated for senior engineers, architects, and tech leads. Full technical depth. Preserves the tradeoffs, the learning journey, the "I tried X first and it didn't work" parts. Closest to your natural voice, just organized.

**Friction Report** goes through the original input and flags specific patterns: defensive framing, inflation, self-erasure, vagueness, abrasiveness, performative language, misread risk. This is the most valuable output. It teaches you your own patterns over time.

**Lobby** is opt-in. Add `AUDIENCE: cross-functional` to your input when writing for PMs, QA, marketing, or other non-technical partners.

## Steering it

You can add optional tags before your raw dump to steer the output:

```
AUDIENCE: [who this is for]
CONTEXT: [what prompted this]
INTENT: [what you want the reader to do or feel]
```

Or skip the tags and just paste. It'll figure it out.

Mid-conversation, you can adjust: "too corporate," "too raw," "pull back the anger," "shorter," "more detail."

## What this is not

Not an app. Not a publishing pipeline. Not a writing improver. It's a translation system for someone who has things worth saying but gets stuck on the part where you have to say them in a way that lands with a specific audience. The prompt is the product. If it works, the platform can evolve. Get the translation right first.
