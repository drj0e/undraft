---
title: "The Diff Never Had a Price"
date: 2026-07-26
draft: false
tags: ["ai-tooling", "compliance", "life-sciences"]
summary: "The agent pitch prices a change by what it costs to produce. A validated GxP system never priced changes that way, and the regulated world already renegotiated the real price once, before agents showed up."
reviewed: true
---

What does a one-line change cost in a validated system?

Wrong question, and the wrongness is the point. <mark>The line was never the thing with the price on it.</mark> In a GxP shop the priced object is the validated state: the standing, evidence-backed argument that this system, as configured, does what it claims, provably, to an inspector's satisfaction. A change costs whatever it takes to re-earn that argument. Impact assessment, change control, regression evidence proportionate to risk, sign-offs. Whether the diff took a week to write or fell out of a model in seconds changes none of it.

So the agent pitch lands strangely on the platform I work on. Elsewhere the story is that [generation got cheap and review didn't](/posts/generation-got-cheap-review-didnt/). Here the pitch skips two bills, not one. Free generation pointed at a change-control process is a rounding error on a rounding error. Nobody in regulated software was waiting on typing.

The regulated world has already renegotiated this price once, and not for AI. [GAMP 5's second edition](https://ispe.org/pharmaceutical-engineering/january-february-2023/what-you-need-know-about-gampr-5-guide-2nd-edition) told an industry buried in scripted test evidence to apply critical thinking and put the rigor where the risk is instead of everywhere. Then last September the FDA [finalized its Computer Software Assurance guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/computer-software-assurance-production-and-quality-management-system-software), three years after the draft: assurance effort commensurate with risk, unscripted testing acceptable for lower-risk functions, wall-to-wall scripted protocols no longer the default posture. It's written for device production and quality software, and the rest of regulated software reads it the way you read a neighbor's zoning ruling. That door was opened for automated test tooling and faster release cadences. Agent-written code will walk through the same door, because nothing in the framework asks who authored a change. It only asks what the change can break.

Which sounds like the regulated world is ready for agents. It isn't, and the gap is arithmetic, not attitude.

Risk-based assurance still prices per change. Assess this change's risk, pick this change's evidence, file this change's record. That calibration assumes changes are scarce, and for the entire history of the discipline they were, because engineers were expensive and change volume limited itself. The quality system could afford to have a person think about each one. An agent fleet doesn't raise the risk of any individual change. It multiplies the count of changes, and the count is the one term in the equation nobody renegotiated.

CSA spent three years settling how much evidence one change deserves. Agents ask what a quality system does when the changes outrun the people assessing them. The next renegotiation won't be about how much scrutiny a change gets. It'll be about whether "a change" can stay the unit of account at all.
