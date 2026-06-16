---
title: "Keeping the Record Is Not Keeping the Definition"
date: 2026-06-23
draft: false
tags: ["data", "life-sciences"]
summary: "Every governance program is built to add definitions and none of them can retire one. In a regulated shop that gets worse, because the instinct to keep every record gets misread as a ban on ever deprecating a definition. They're different objects."
---

Every data governance program I've watched is built to add definitions. None of them is built to remove one.

You seat a steward, [as I keep insisting you have to](/posts/how-many-samples-do-we-have/), and the first thing they do is define a sample. Then a specimen. Then the handful of entities that carry real weight, and the lineage between them. The catalog fills up. The semantic layer accumulates measures. Every motion in the system is additive. The vocabulary only ever grows.

So the failure mode nobody plans for isn't drift. It's accumulation.

A wrong definition gets caught: somebody's number comes out strange and the steward gets pulled into a meeting. An obsolete one just sits there, still wired into a dashboard nobody opens, still technically correct against a question nobody asks anymore.

We give stewards the authority to define. We almost never give them the authority to retire. Those are not the same grant, and the second is harder to hand out, because retiring a definition means telling some team the thing they've counted on is going away. Adding makes you useful. Retiring makes you the person who broke a report.

<mark>A steward who can only add is not a governance function. They're a backlog with a job title.</mark>

In a regulated shop this gets worse, because the whole culture is built to keep everything. That instinct is correct for records and corrosive for definitions, and almost nobody separates the two.

You are required to keep the record. A batch result from 2019 stays attributable, legible, and [available years after the fact](/posts/data-governance-that-survives-an-inspection/). That's the Enduring and the Available in ALCOA+, and you do not get to delete it because the study closed. Fine. That's the record, and it is sacred.

The definition is a different object. It's the active meaning the org uses to count, report, and decide right now. Retiring a definition touches no stored record. The 2019 batch result keeps its original meaning, frozen, forever. What changes is that "available sample" stops being a live measure the business runs against. You aren't erasing history. You're declaring that one interpretation is no longer the current one.

Regulated orgs conflate these constantly. "We can't retire that, it's a controlled definition" is true about the record and false about the live meaning, and that one confusion is why the vocabulary in a life sciences shop bloats faster than almost anywhere else. The audit trail is the very thing that makes retiring safe. It preserves what the word used to mean, so dropping the live version costs you nothing you were obligated to keep.

So the maturity signal isn't the size of the catalog. It's whether the steward has ever retired anything. A program that has only grown its vocabulary hasn't been tested yet. The test is the first time a steward says this definition is done, we keep every record it produced and we stop using it to answer anything new, and the org lets them say it without flinching.

Before that day, what you have isn't governance. It's a very well documented pile.
