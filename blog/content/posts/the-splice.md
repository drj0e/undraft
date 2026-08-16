---
title: "The Splice"
date: 2026-08-17
draft: false
tags: ["data", "architecture"]
summary: "When a steward improves a definition, every chart that crosses the change date becomes two series drawn as one line. Accounting and the BLS each have a formal answer for that moment. Dashboards have a default."
---

A trend that crosses a definition change is two series drawn as one line.

Definitions move; a steward improving one is the system doing its job. A while back I argued the fix for what that does to old numbers: [stamp every figure](/posts/the-answer-has-no-audit-trail/) with the version of the definition that produced it, so a figure in an old deck stays legible. The stamp turns out to be the easy half. It can tell you which points on a chart ran under the old meaning and which under the new. It says nothing about the segment drawn between them, and something gets drawn there whether or not anyone decides what it means.

Fields that live on their time series treat this moment as a formal event with a menu.

Accounting picks the expensive option. Under [IAS 8](https://www.ifrs.org/issued-standards/list-of-standards/ias-8-accounting-policies-changes-in-accounting-estimates-and-errors/), a change in accounting policy applies retrospectively: comparative figures are restated as if the new policy had always been in force. Last year's column gets recomputed under this year's meaning before the two are allowed to sit side by side.

The BLS picks the careful one. The published CPI stands as it stood; a methods improvement counts from its start date forward. Readers who need a consistent history get a separate, labeled series instead, the [R-CPI-U-RS](https://www.bls.gov/opub/mlr/1999/article/cpi-research-series-using-current-methods-1978-98.htm), which estimates the index from 1978 on as if today's methods had been in place the whole time. The break stays visible in the official record, and the consistent version stands next to it, marked as the estimate it is.

Restate the past under the current meaning, or freeze the past and publish the consistent history beside it. Both options cost real work, because both treat comparability as something a person manufactures rather than something a chart inherits. What neither field allows is what a dashboard does out of the box: compute each point under whatever the meaning was that day, connect the dots, and let the slope present itself as evidence.

No point on that chart is wrong. Every dot is correct under the rule in force the day it ran. The trouble is the segment joining the last point computed under the old meaning to the first computed under the new one. No definition ever governed that stretch of the line, and it's the stretch a reader takes as the finding, because the eye goes to slope.

So a definition change needs one more entry in the steward's change record: what happens to history. Restated, with a name on the recomputation and a date it lands. Or broken, with the break drawn on every chart that crosses it, where a reader will hit it.

Restated is a decision. Broken is a decision. A splice is the absence of one, executed at render time.
