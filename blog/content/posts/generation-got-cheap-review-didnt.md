---
title: "Generation Got Cheap. Review Didn't."
date: 2026-07-18
draft: false
tags: ["ai-tooling", "leadership"]
summary: "The pitch for autonomous coding is a multiplier on how fast you write code. But writing was never the part a human has to stand behind, and the part they do stand behind got no cheaper, and probably got worse."
reviewed: true
---

The pitch for autonomous coding is a multiplier. Ten times the code in a tenth of the time, so the team ships ten times as much. The arithmetic is clean, and it quietly drops the one number that decides whether any of it is real.

Somebody still has to decide the code is correct. That step didn't get faster. It probably got slower.

Generation and verification were always two jobs wearing one coat, because the person writing the code was also the person who understood it. You verified as you went. Understanding came free with authorship; you never got a separate bill for it. Split the two, hand generation to a machine, and the bill for understanding arrives on its own, addressed to whoever reads the diff. It was always there. It used to be bundled into the typing.

Making generation cheap does nothing to that bill.

If anything it inflates it. Reviewing code you wrote an hour ago is fast, because you still hold the intent in your head. Reviewing code a process generated and then dropped means rebuilding the intent from the artifact alone, [with no author to ask](/posts/the-author-you-cant-ask/) why this line and not the obvious other one. That's slower per line than reviewing a teammate's pull request, and a teammate's pull request was never the fast part of anyone's week.

This is Amdahl's law wearing a hoodie. Speed one stage of a process up by however much you like, and your total speedup is capped by the stage you left alone. If verification was a third of the honest effort and you drive generation to zero, the ceiling is a 3x gain, and only if verification cost holds perfectly still. It didn't hold still. It rose, because the reader lost the context that used to come attached to writing the thing.

There's a measurement here that should have landed harder than it did. METR ran a randomized controlled trial in 2025 with experienced open-source developers working on their own mature repositories. With AI tools allowed, they took [19% longer](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) to finish. The slowdown isn't even the interesting part. The interesting part is that the same developers, after the fact, estimated the tools had sped them up by about 20%. They felt generation get faster, because generation is the visible, keyboard-shaped part of the job. They didn't feel the reading and correcting and re-reading eat the gain back, because that cost is diffuse and never looks like work.

That gap between felt and measured is the whole thing in a single number. The multiplier is loud and the denominator is silent. A wall of correct-looking code appears in seconds and it feels like getting something for nothing. The hours you then spend confirming it's actually correct don't file themselves under the cost of that code. They just feel like a normal week filling up.

So the ceiling on an agent-heavy team isn't generation throughput. It's how much code a human can actually stand behind in a day, and that number is small, and it does not move when the model gets better at writing. A stronger model raises the volume of plausible code and leaves the verification budget exactly where it sat. You can widen the mouth of the funnel as far as you want. The neck is one person reading carefully, and they were already busy.

This wrecks the first metric everyone reaches for. Lines shipped, pull requests merged, points closed, all of it counts the top of the funnel, the part that just became cheap and therefore stopped meaning anything. A team can double its merged volume and lose ground, if the extra volume is code nobody has genuinely stood behind and the debugging arrives next quarter with interest. Measure an agent-heavy team by output and you're measuring the exact thing that stopped being scarce.

Which points the real work somewhere unglamorous. It isn't better generation. It's anything that lowers the cost of trusting a change without a person rereading every line of it. The cheap deterministic gates I keep [circling back to](/posts/who-watches-the-watcher/) are one swing at that: let a machine vouch for the boring properties so the human spends attention only where no machine can. Provenance is another. Tests that actually pin behavior instead of decorating it are another. Every one of them is the same move, buying down the cost of belief, and not one of them is what the demos are selling.

The teams that come out ahead won't be the ones generating the most. They'll be the ones who worked out how to trust a diff nobody reread, and that is a harder problem than writing the diff, which is precisely why no one is on stage demonstrating it.
