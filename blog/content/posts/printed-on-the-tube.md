---
title: "Printed on the Tube"
date: 2026-09-08
draft: false
tags: ["data", "architecture"]
summary: "A sample ID like SITE04-PRT19-2021-00381 is four definitions promoted into a key. The audit trail can correct any column in the record and can't touch the key, and then the key gets printed on a tube that sits in a freezer for decades. No steward ever gets to retire that one."
---

`SITE04-PRT19-2021-00381`

Read that as a sample ID and it tells a story before you open a single record. Collected at site four, under protocol nineteen, in 2021, the three hundred eighty-first tube. Four facts, no lookup. That story is the whole pull of a smart key, and the pull is strongest at the freezer door, where the person holding the tube has gloves on and no keyboard.

Now read it as a schema.

Each segment is a column that got promoted into the key. SITE04 is a foreign key into a site table. PRT19 points at a protocol. 2021 is a date column truncated to the year. Every one of them is a claim about the sample, and every one of them rests on a definition of the kind I've been [arguing has to be retirable](/posts/record-is-not-the-definition/): what counts as a site, which protocol a specimen belongs to after two protocols merge, what "collected" means for an aliquot derived a year later.

A column can absorb a definition changing. The site gets renumbered, someone updates the row, the audit trail records who changed it and when, and the record is accurate again while the history stays intact. That's the [ALCOA+](/posts/data-governance-that-survives-an-inspection/) bargain, and it's a good one. The key can't take that bargain. It's the value every other row points at. Change it and you don't get a corrected record, you get a new record and an orphaned history. So the stale fact stays. SITE04 goes on asserting that the sample came from site four, in a field that will outlive every table around it.

So a smart key holds facts that can be wrong and unfixable at the same time, which no other part of a regulated record is permitted to do. The audit trail promises that every value is either right or corrected with a trail. The key sits outside that promise by construction, because the machinery that corrects values is the same machinery that isn't allowed to touch keys.

Then it goes in the freezer. The tube gets a label, the label gets the ID, and the ID inherits the record's retention, which in this industry [runs to decades](/posts/required-to-delete-this/), in a box at minus eighty where no migration script has ever run. Renaming a column is a ticket. Changing a key is a relabeling campaign across every rack, and the campaign has to touch the rack that hasn't been opened since 2021.

Three different fields hit this wall years ago and wrote down the same rule. GS1 calls a GTIN a non-significant number: no part of it relates to any classification or conveys any information, and it has to be recorded and processed in its entirety. ([GS1](https://www.gs1.org/standards/gs1-healthcare-gtin-allocation-rules-standard/current-standard)) Kimball's warehouse design wants dimension keys to be meaningless integers rather than "awkward 'smart' keys" assembled from source-system codes. ([Kimball Group](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/dimension-surrogate-key/)) And the life-science identifier guidance in PLOS Biology says to avoid embedding meaning, favor opaque identifiers, and carry the meaning in metadata, because collections and scientific understanding both evolve and embedded meaning goes stale with them. ([McMurry et al., 2017](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2001414))

That last paper leaves a door open for meaning that is "indisputable, unchangeable and also useful," and the door is where the trouble gets in. Every segment in the ID above looked unchangeable on the day someone picked the format. A site number looks permanent until a site closes and its studies transfer to another one. A protocol code looks permanent until an amendment folds two protocols into one. Unchangeable is a prediction, and a key is where a wrong prediction can't be revised.

I argued a couple of months back that meaning has to [live in the identifier](/posts/agents-dont-read-the-glossary/), because an agent binds to the name and never reads the glossary. That still holds, with a boundary I didn't draw at the time. The identifier that should carry meaning is the column name. A name is renamable, and a rename is a migration with a diff and a reviewer. A key value is copied into every child record, every export, and every label, and nothing renames it. Put meaning in a name and the steward can retire it with one migration. Put meaning in a key and the steward gets to watch it go wrong.

Every hyphen in an ID format is a definition that got frozen without anyone deciding to freeze it. The site, the protocol, and the year all have columns waiting for them, where being wrong is a condition the system already knows how to fix.
