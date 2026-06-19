---
title: "The Property I Left Off the Stack"
date: 2026-06-26
draft: false
tags: ["automation", "architecture"]
summary: "Months ago I listed what a system needs before an agent can run unattended, and I left off the one that matters most after the first crash. A stop button handles the runaway. It does nothing for the run that dies on step nine of fourteen."
reviewed: true
---

Months back I [listed what a system needs](/posts/the-stack-nobody-talks-about/) before you let an agent run without watching it: the output has to be selectable, constrained, audited, and stoppable. I built all of it. I was proudest of the stop button, the budget caps and the hard kill, because the nightmare everyone pictures is the agent that won't quit.

I left one off. It's the one that decides whether "unattended" is a real word or a brochure word.

Resumable.

A stop button handles the runaway. It does nothing for the far more common case: the run that dies in the middle. The API times out on step nine of fourteen. A dependency 502s. The container gets recycled. Nothing dramatic, nothing dangerous, just a process that isn't there anymore when you check in the morning.

Now what?

If the answer is "read the logs, work out which steps already happened, undo the half-finished one by hand, and start it again from there," then you don't have an unattended system. You have a system that runs unattended until the first hiccup and then waits for you. The whole point was to stay out of the loop, and you're back in it, at the worst possible time, rebuilding state you never wrote down, on the assumption that the last run left things clean. It didn't. That's why it stopped.

The thing that makes a restart safe is idempotency, and it is unglamorous work. Every step that touches the world has to be safe to run twice. Re-running step nine can't open a second branch, post a second comment, charge a second time, write a second row. You either check whether the effect already happened before doing it, or you make the effect itself naturally repeatable. Both are tedious. Neither shows up in a demo, because demos always run start to finish.

Stoppable and resumable sound like the same virtue seen from opposite ends. They aren't. Stoppable is about your authority over the agent: can you make it quit. Resumable is about the agent's relationship to its own past: can it tell what it already did and pick up without redoing it. You can ship a flawless kill switch and still have a system that's useless after any interruption, because killing it cleanly and restarting it cleanly are different engineering problems. The first is permission. The second is memory plus arithmetic.

[I argued before](/posts/the-harness-that-forgets/) that overnight agents need sensors with memory, something that notices and carries state from one run to the next. Resumability is the narrowest, most boring version of that argument, and the one you trip over first. Before an agent can learn anything across a month of runs, it has to survive a single run that breaks halfway.

Here's what reorders the priority list. Of everything that can go wrong with an unattended agent, "it crashed partway" is not the rare case. It's the median case. Networks blink, quotas trip, machines get reclaimed. You will spend far more mornings cleaning up after an interrupted run than after a runaway one. We build the dramatic safety feature first and the common one last or never, because the runaway is scary and the half-finished run is just annoying.

Annoying scales worse than scary. A scary failure you fix once and harden against. An annoying one you pay every time it happens, in the exact minutes you built the system to hand back.
