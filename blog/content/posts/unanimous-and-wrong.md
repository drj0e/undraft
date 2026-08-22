---
title: "Unanimous and Wrong"
date: 2026-08-24
draft: false
tags: ["data", "life-sciences"]
summary: "Warehouse operations checks its records against the shelf on a rotating schedule and knows its match rate. A data stack checks records against records, so it can agree with itself completely and still be wrong about what's in the freezer."
---

Sixty-five percent of a retailer's inventory records were wrong. That's from a 2008 study that [checked nearly 370,000 records across 37 stores](https://pubsonline.informs.org/doi/10.1287/mnsc.1070.0789) against physical audits of the shelves. Not wrong against another system. Wrong against the stock itself.

I've blamed two things so far for wrong sample counts: [definitions that were never settled](/posts/how-many-samples-do-we-have/) and [copies that stayed writable](/posts/a-read-answer-to-a-write-problem/). Both diagnoses hold up. Both also assume the mistake lives somewhere in the records, and every fix they prescribe, the steward, the single writable home, the read-only stamp, compares data with data. Run all of it and the stack agrees with itself. Whether the agreed count matches the tubes is a question no part of the stack can ask, because asking requires an independent source of the answer, and every source the stack owns sits downstream of the same writes.

The drift needs no software bug. A box goes back one shelf lower after a defrost. A tube shatters, and the cleanup finishes before anyone reaches a keyboard. The record stays consistent across every copy, and false.

The quality frameworks name this and then look away. DAMA's six dimensions define [accuracy](https://www.dama-uk.org/resources/the-six-primary-dimensions-for-data-quality-assessment) as the degree to which data correctly describes the real-world object it represents. Now look at what a data quality dashboard computes: completeness, uniqueness, validity, consistency, timeliness. Everything a query can score. Accuracy, the dimension that would need an observation of the world, gets approximated by checking against a reference dataset, which is one more record, nearer the world but still not it. The definition asks for the freezer. The metric answers with another database.

Warehousing refused that substitute. [Cycle counting](https://en.wikipedia.org/wiki/Cycle_count) sends a person to count a small rotating slice of stock against the record, continuously, fast-moving items more often than slow ones, with the match rate tracked as a standing operational number. The 65 percent exists because the retailer's audits made the comparison at all. On my side of the fence I can name the systems that would disagree with each other about a tube. I cannot name the process that would notice the tube itself missing.

Retail runs this discipline over stock it could reorder by Thursday. A freezer holds specimens with no reorder path, counted by systems that only ever check each other.

A stack can reach perfect consensus about a tube that isn't there.
