---
title: "The Third Row"
date: 2026-08-20
draft: false
tags: ["data", "architecture"]
summary: "A record in the LIMS, a record in the notebook, and the claim that both name the same physical vial. The first two have owners. The third lives in a crosswalk table, written by a match rule that shipped as ETL code."
---

Run a LIMS next to an electronic lab notebook for a couple of years and a table grows in the space between them:

```sql
CREATE TABLE sample_xref (
    lims_id    varchar NOT NULL,
    eln_id     varchar NOT NULL,
    loaded_at  timestamp
);
```

Every row is a sentence: sample 4471 in the LIMS and sample S-2209 in the notebook are the same physical vial.

Look at what kind of sentence that is. The LIMS record is an observation, made and owned by the LIMS. The notebook record is an observation, made and owned by the notebook. The claim that the two describe one object is not an observation. It's a ruling, it concerns both systems at once, and a fact about both belongs to neither, which is how it ends up out here, a third row about the first two, in a table whose only provenance column says when the batch job ran.

When [three systems gave me three counts of our samples](/posts/how-many-samples-do-we-have/), the diagnosis was unsettled definitions, and the fix was a steward with authority over what the words mean. [The write-time fork](/posts/a-read-answer-to-a-write-problem/) was a second hole with a second fix, one writable home per field. Close both and a cross-system count still has to decide which records name the same thing before it can count anything, and that decision runs entirely through this table. <mark>The count is exactly as true as the crosswalk, and the crosswalk was never anyone's to keep true.</mark>

So who writes the rows? A match rule inside the integration that moves data between the two systems: barcode equality on the lucky pairs, name plus collection date plus freezer position on the rest. It was authored by whoever built the pipeline, and it was reviewed the way pipelines get reviewed. Does the join key look right, does the incremental load complete. Whether the pairs are the same vials is not a question a pull request can see.

Record linkage, the discipline this belongs to, got [its formal theory in 1969](https://doi.org/10.1080/01621459.1969.10501049), and the Fellegi-Sunter decision rule returns three verdicts, not two: link, non-link, and a middle band the math declines to settle, routed to a person for clerical review. The paper defines an optimal rule as the one that holds both error rates while sending the fewest pairs to that person. Serious MDM suites still honor the design, and a match review queue with a steward at the end of it is a standard feature in them. The crosswalk between two lab systems almost never passes through one. It gets a threshold. Above it links, below it doesn't, and the middle band, the part of the output the theory says a person owes a decision, lands in whichever verdict the cutoff happens to assign.

Both remaining ways of being wrong move the count. A false link folds two vials into one. A missed link splits one vial into two. Neither error marks a record anywhere: every row in the LIMS stays correct, every row in the notebook stays correct, and the wrongness sits in the pairing, where no review of either system can reach it.

Treating the pairing as a decision costs three columns and a procedure: who asserted the match, what it was based on, and a path to retract it when a tech reports that the vial in their hand disagrees with the join. And the middle band needs somewhere to land, which is less work than it sounds, because the seat already exists. Deciding whether two records name one vial takes the same authority as deciding what a sample is.

The reason to add those columns now is how long the rows live. A LIMS that gets retired takes its screens and its records into the archive. It does not take the crosswalk, because the printed labels in the freezers still carry its numbers, and whatever replaces it has to answer for every one of them. Each generation of systems hands its identity claims down to the next, intact and unexamined. The freezer doesn't get migrated.
