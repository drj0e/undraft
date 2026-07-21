---
title: "A Read Answer to a Write Problem"
date: 2026-07-30
draft: false
tags: ["data", "architecture"]
summary: "Naming a system of record settles which copy to believe after two numbers already disagree. The fork itself gets created at write time, by every screen that leaves a copied field editable."
reviewed: true
---

Somewhere in an architecture wiki near you sits a sentence like this: "The LIMS is the system of record for sample data."

Notice when that sentence gets read. Two reports disagree, someone asks which count to trust, and the wiki supplies the ruling. Believe the LIMS. The badge is an arbitration device, and it comes out of the drawer after the numbers have already split.

The split happens earlier, at write time, where the badge has no reach, because a badge on a system says nothing about a field.

Walk through how a fork gets made. A sample's status is mastered in the LIMS. An integration copies it into the freezer inventory tool so the people standing at the freezers can see it without a second login. Useful, and obviously worth doing. But the inventory tool is a normal application with normal forms, so the copied status renders in an editable widget like every other value on the screen. Nothing stops a tech who spots a stale status from correcting it right there, on the screen they already have open, and a visible edit box next to a wrong value is a standing invitation to do exactly that. It only has to happen once. The correction never travels back, the fact now has two writable homes, and the two drift.

When [three systems gave me three counts of our samples](/posts/how-many-samples-do-we-have/), the diagnosis was mostly semantic: an unsettled grain, an empty steward seat, four defensible definitions of a sample running in production. Settling all of that still leaves this hole open. A settled definition forks as cleanly as a contested one. Two writable homes will disagree about a perfectly defined field, and the glossary can't break the tie, because both values are well-formed answers to the same well-defined question. One of them is stale, and staleness leaves no mark on a value.

The mismatch is granularity. The badge gets granted once, at the system level, in a document. Write authority gets enforced field by field, screen by screen, inside the permission model of every application that holds a copy. Declaring a system of record costs one sentence. Honoring the declaration costs a read-only flag on every screen where a copied field appears, in systems the declaring team doesn't own, for the sake of a consistency argument those teams never signed. The sentence gets written. The flags sit in somebody else's backlog.

Master data management, the discipline that takes this fork most seriously, resolves it with [survivorship rules](https://profisee.com/blog/mdm-survivorship/): when copies disagree, a rule picks which value survives into the golden record, attribute by attribute. Even the cleanup crew works at field grain. And it still works after the fork, choosing between two values that have already diverged. Better arbitration, still arbitration.

For the badge to mean anything it has to be translated down to the grain where writes happen. A field gets one writable home. Every other place it shows up is visibly a copy: read-only, stamped with where it came from and when it was last refreshed. Boring work, with no milestone worth a slide. The wiki sentence keeps its job either way. There are just fewer disputes left for it to settle.
