---
title: "Hide a Check, Hire a Human"
date: 2026-08-11
draft: true
tags: ["ai-tooling", "code-quality"]
summary: "I argued that the checks an agent can't see are the only ones whose green you can fully trust. The part I skipped: when a hidden check fails, there's no agent left to hand the red to. That makes it a page, and pages have a budget."
reviewed: true
---

The morning after an overnight run, the verdicts arrive pre-sorted. Everything the agent could see is green, because any red it saw got retried until it wasn't. The checks it never saw are the only place a red can still be sitting, and only one reader is left for those.

A month back I argued for [splitting a guard pipeline in two](/posts/the-guard-the-agent-can-see/): checks the agent retries against, and checks it never learns exist. I still hold that line. What I skipped was the failure path of the hidden half.

An in-loop failure is self-service. The agent reads the verdict, adjusts, resubmits, and the whole exchange settles in tokens at 2am. An out-of-loop failure has no next step wired to it. Feeding it back is exactly what the design forbids, and the process that produced the diff [exited hours ago](/posts/the-author-you-cant-ask/) regardless. The red waits for a person.

In my pipeline, that person is me.

Operations already worked out what a signal like this costs. A signal consumed by a machine is a test. A signal whose only consumer is a human is a page, and the SRE book is strict about pages: [every page should be actionable](https://sre.google/sre-book/monitoring-distributed-systems/), and a responder has a few urgent reactions in them per day before fatigue takes over. None of that arithmetic cares that the sender is a guard pipeline instead of a production alert.

Which caps the hidden tier somewhere compute never enters. In-loop checks scale with the token budget. Hidden checks scale with mornings. Each new one is a standing claim on attention I had been counting as free, and a hidden check that fires weekly is a recurring meeting I put on my own calendar without noticing.

So the question of where a check belongs turns out to be the alerting question. When this goes red, will someone act on it that day? If yes, hide it and keep it out of the agent's reach. If the true answer is that the red will age in a log, two options remain: move the check into the loop and accept the coaching, or stop running it.

Count the hidden checks in your pipeline, then count the reds you actually cleared last month. Every check past that second number is a page you've chosen to sleep through.
