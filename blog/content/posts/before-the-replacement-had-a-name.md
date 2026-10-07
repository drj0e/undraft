---
title: "Before the Replacement Had a Name"
date: 2026-10-14
draft: false
tags: ["compliance", "automation", "life-sciences"]
shape: teardown
origin: thread
reach: core
summary: "A model vendor's deprecation notice names the replacement and tells you to test against it before the retirement date, so every criterion written inside that window was written knowing the answer. Device regulators already settled what counts instead: criteria dated before the change."
reviewed: true
---

Three days after I called the vendor's deprecation page a [change-control calendar](/posts/sixty-days-notice/), it got a new row. On September 30 the notice went out: `claude-sonnet-4-5-20250929` retires on November 30, and the recommended replacement is `claude-sonnet-5-5`. ([Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations))

The same page says what to do about it, in one sentence:

> To help measure the performance of replacement models on your tasks, consider thorough testing of your applications with the new models well before the retirement date.

A regulated shop has to read that as a qualification protocol, because nothing else arrives with the notice. It comes apart in four places.

"Measure the performance." Against what? A measurement with no pass line is a report. The sentence never says what a replacement has to score, so whatever it scores becomes the result.

"Thorough testing." Thorough is the shop's word to fill in, and the shop fills it in later, under a deadline, with the migration half done. Thoroughness defined after the test is whatever the test turned out to be.

"With the new models." The notice names the model. Every test written in response is written by someone who knows which model it will grade and can run that model while writing it. When a case fails, the case gets a second look before the model does. Not out of dishonesty. Out of wanting the migration finished.

"Well before the retirement date." Sixty days, and the window opens with the notice. The whole protocol lands inside the window, which puts it after the replacement is known. That ordering is the defect. The other three clauses are where it shows.

The FDA worked through the same ordering for devices and landed on the other side of it. Its [predetermined change control plan guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence), final since December 2024, lets the maker of an AI-enabled device change the model after clearance without a new submission, provided the plan for those changes was authorized with the device. The plan has three parts. A description of the modifications in scope. A modification protocol, with performance evaluation against pre-specified acceptance criteria. An impact assessment. The regulator reads the plan before any of the changes exist, and a change that stays inside it ships on the maker's say-so. A change outside it is a new submission.

The bargain is the date. Criteria accepted before the change are evidence. Criteria written after you've seen the change are a description of it.

A preprint from June made the same move for science. LLM-based studies are easy to p-hack, since a researcher can tune prompts and settings until the result appears, so the authors propose [preregistering the analysis plan along with a list of eligible future models](https://arxiv.org/abs/2606.27687), then running it on the first eligible model released afterward. That model doesn't exist at commitment time, so it can't be tuned against. Across 20 models from four providers, they found the protocol would have stopped the p-hack from carrying over in about three quarters of cases. Their problem is a hypothesis test and mine is qualification evidence, and the mechanism ports without edits. A criterion fixed before the replacement exists can't have been shaped by it.

The backlog in the pipeline I built gives every task its [acceptance criteria](/posts/the-stack-nobody-talks-about/) before the agent starts. The executor gets none. Its model string sits outside the approval hash, and nothing I've described holds a pass line for the model that takes over when the current one retires. Following the vendor's sentence, I'd write one in October, against a model named in September, and file the result as qualification.

So the question for any pipeline on a hosted model is the date on its eval suite, and git already knows it:

```
git log --diff-filter=A --date=short --format='%ad %s' -- evals/
```

An earliest commit before September 30 means you have a protocol, and the replacement gets graded by it. After, and what you have is a migration log the replacement helped write. No directory at all, and the sentence on the deprecation page is your protocol. The vendor wrote it.

A criterion that predates the notice needs three things the vendor's sentence leaves out. Which models are eligible to replace the current one, the way the device plan bounds its modifications. What each case has to score. And what a miss does: the pipeline keeps the old model until retirement day and then stops, and a person decides, on the record, whether the criterion was wrong or the pipeline is. Leave off that last part and you've rewritten the vendor's sentence with numbers in it.

The next row on that page will name a replacement too. Whatever grades it honestly was committed before it had a name.
