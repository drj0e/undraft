---
title: "Sixty Days' Notice"
date: 2026-09-27
draft: false
tags: ["ai-tooling", "compliance"]
summary: "A model vendor's deprecation page puts a retirement date on every model it serves, with about sixty days between the notice and the day requests start failing. An approval bound to a hash of the spec voids itself when the spec changes and never hears about the executor changing."
---

Between the notice that a model is deprecated and the morning requests to it start failing, the last four rounds on [one vendor's deprecation page](https://platform.claude.com/docs/en/about-claude/model-deprecations) ran between 60 and 62 days. The page promises at least 60. Every model still marked active has a tentative retirement date beside it, phrased "not sooner than" a day in 2026 or 2027.

Read that page from inside a regulated shop and it stops being release notes. It's a change-control calendar, written by someone else, with the dates already filled in.

Annex 11 asks that any change to a computerised system, configuration included, be made [in a controlled manner in accordance with a defined procedure](https://health.ec.europa.eu/system/files/2016-11/annex11_01-2011_en_0.pdf). The draft Annex 22 that went out for consultation in July 2025 is the first EU GMP text written for AI, and its opening move is to hold the model still. Critical applications get static models only. Models that adapt during use are out, and so are generative models and LLMs, which the draft [allows in non-critical roles](https://gmpinsiders.com/annex-22-draft-regulatory-guidance-on-ai-use-in-gmp/) with a qualified human reading the output. The regulator wants to validate a thing that stays the thing it validated.

A hosted model is the opposite object. The vendor tells you, in a table, that it will be replaced, and roughly when.

Last month I argued that assurance for agent-written change has to move from the diff to the process, the way manufacturing [moved it from the part to the line](/posts/one-page-from-1924/). A qualified process is an argument about one specific process. Somewhere in the argument for an agent pipeline sits a model ID, and that string has an end date on a page the pipeline never reads.

The approval gate I built binds a sign-off to a [hash of the spec](/posts/agent-world-reinventing-part-11/), so an edit after approval voids it. The hash reaches the question. The executor that will answer it, a model plus a prompt plus a set of tools, sits outside the hash, and the first of those three changes on the vendor's schedule. Bump the model string and every approval in the queue still validates, because the thing it signed hasn't moved. Only the thing that reads it has.

A supplier change you can decline is an ordinary change-control event. This one comes with a retirement date, so the assessment has a deadline the shop didn't set, and refusing means the pipeline stops.

Two things follow. The audit line for every run should carry the model ID next to the actor, so a merged diff traces to the executor that wrote it and not only to a service account. And the model string belongs under change control as a configuration item, so a bump reopens whatever qualification evidence the pipeline has instead of riding through as a version pin.

Evidence that has to be re-earned every sixty days is evidence you can only afford if a script produces it. A qualification that takes a person a week gets done once, and then the retirement date lands and the replacement goes live under the old paperwork.

That same vendor page offers a usage export, broken down by API key and model, for finding which of your applications still calls the deprecated one. Until the audit line carries the model ID, that export is the only inventory of your executor you have, and the vendor keeps it.
