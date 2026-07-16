---
title: "You're Required to Delete This"
date: 2026-07-23
draft: false
tags: ["data", "life-sciences"]
summary: "Storage is cheap, so the instinct is to keep everything. In a regulated shop that instinct is a second way to be out of compliance, because some records you're required to destroy on a clock."
reviewed: true
---

Storage is cheap, so the default engineering instinct is to keep everything. In a regulated shop that instinct isn't cautious. It's a second way to be out of compliance.

Two clocks run on the same record. One says keep. Under the EU Clinical Trials Regulation, the trial master file has to stay [available and legible for at least 25 years](https://www.legislation.gov.uk/eur/2014/536/article/58?view=plain) after the trial ends, and you don't get to shorten that because a study closed or a system got retired. The other clock says delete. GDPR's storage limitation principle says personal data may be [kept no longer than is necessary](https://gdpr-info.eu/art-5-gdpr/) for the purpose you collected it for. Past that point, holding it is the violation.

Same platform, same subject. Opposite obligations, each with teeth.

The industry reflex resolves this badly, by keeping. Deleting feels dangerous and keeping feels safe, because the failure mode of deletion is loud (you destroyed something you needed) and the failure mode of retention is silent (you're sitting on data you were required to purge, and nobody notices until a regulator asks). So the safe-seeming move is to never delete, and the safe-seeming move is wrong. It just fails quietly instead of loudly.

[I've written](/posts/record-is-not-the-definition/) that you're required to keep the record, and that's true. This is the other half of the same sentence, and it's the half engineers skip: some records you're required to destroy, on a schedule, and destruction is a positive act you have to perform on time, not the absence of keeping.

That changes what a storage platform owes you. A delete button isn't the feature. Every record needs a delete-by date attached the moment it's created, computed from what it is and why it was collected, and the platform has to act on that clock whether or not anyone remembers the record is there. Deletion has to be as scheduled, logged, and provable as retention. The audit trail that proves you held the batch result for 25 years is the same kind of artifact that has to prove you erased the identifiable data the day it aged out.

Almost no platform is built this way. We build for durability. We treat every write as forever and every delete as an exception a human requests, which is exactly backwards for the records that carry a maximum. Forever is a design default, and for regulated personal data it's a liability that compounds. The longer you hold it, the larger the thing you now have to explain.

The tell is one question. Ask your platform which records are past their delete-by date right now. If it can't answer, you're not keeping data safe. You're accumulating the exact thing you were obligated to be rid of, and calling it caution.
