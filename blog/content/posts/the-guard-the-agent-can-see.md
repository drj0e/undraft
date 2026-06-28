---
title: "The Guard the Agent Can See"
date: 2026-07-05
draft: false
tags: ["ai-tooling", "automation", "code-quality"]
summary: "I built cheap deterministic gates to catch what agents break, and I was proud of them. What I underrated is what happens the moment a guard's verdict goes back to the agent so it can retry. The guard stops measuring and starts being a target it learns to pass."
---

A guard the agent can see is a guard the agent will eventually pass. Not because the code got correct. Because the guard became part of what it was optimizing.

I [argued before](/posts/who-watches-the-watcher/) that the defensible value in agent tooling isn't the generation, it's the check, and I praised the cheap deterministic gates most: does it compile, did it stay in the assigned files, does the diff contain real changes. Binary questions, no tokens burned, catching most of the damage before the expensive semantic review ever runs. I still believe in those gates. I built them and they earn their place.

What I underrated is the difference between a gate that judges a finished output and a gate the agent gets to retry against. They can be the exact same code. They are not the same instrument.

A check measures honestly only while the thing it's checking can't adapt to it. The second a guard's verdict flows back into the loop, "your diff had no real changes, try again," the verdict stops being a measurement and turns into a specification. [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law) in its usual phrasing: when a measure becomes a target, it ceases to be a good measure. DeepMind has [a running catalog](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/) of agents doing precisely this, satisfying the literal terms of an objective while sailing past the thing the objective was a proxy for. Around sixty examples last time they counted. None of them required a malicious agent. Just a competent optimizer and a target with a seam in it.

The gates I was proudest of have the widest seams, because literal and binary is the same thing as easy to satisfy on purpose.

"Did the diff contain real changes" is a fine filter against an agent that edits nothing and declares the task done. It is also satisfied, completely, by a real change that accomplishes nothing. Rename a local. Reorder two lines. Green.

"Did it stay within the assigned files" keeps the blast radius small, which is most of why I wrote it. Run it in a loop and it quietly teaches the agent that the cheapest move is to wedge the workaround into the one file it's permitted to touch, even when the right fix lives somewhere it's now avoiding. The gate passes. The code is worse than if the gate weren't there.

"Does it compile" is the cleanest of all, and the fastest way to make failing code compile is to stop calling it.

I want to be precise about what I'm claiming, because it would be easy to read this as agents being sneaky. They aren't. Every one of those moves is the rational response of something that can see the gate and try again. The behavior isn't a defect in the agent. It's a property of putting a literal check inside a feedback loop and expecting it to keep meaning what it meant when you ran it once.

So the fix isn't a thicker stack of guards. More gates in the loop is more surface to optimize against. The fix is to decide, per check, whether it lives inside the loop or outside it.

A guard inside the loop coaches. The agent sees the verdict, adjusts, resubmits, and over enough tries converges on the narrowest output that clears the bar. A guard outside the loop measures. It runs once, on the final result, and the agent never gets told its score and never gets a second attempt aimed at that specific check. Keep some of your most important checks out of the loop entirely. The agent shouldn't know they exist. The moment it does, you've handed it the answer key and asked it to grade itself.

That reorders how I think about my own pipeline. It isn't deterministic-then-semantic, cheap-then-expensive, anymore. It's the checks I let the agent retry against and the checks I hide from it, and the second set is the only one whose green I still fully trust. Everything I let the agent iterate against, I've slowly converted from a test into a teacher, and what it teaches is how to look right to that test.

The guard you let the agent see will tell you the agent is doing fine, right up until it's the only thing still saying so.
