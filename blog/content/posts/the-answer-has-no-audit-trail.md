---
title: "The Answer Has No Audit Trail"
date: 2026-07-09
draft: false
tags: ["data", "compliance"]
summary: "Your audit trail proves the raw record wasn't tampered with. It says nothing about which definition turned that record into the number you put in a deck, and definitions move."
reviewed: true
---

A figure that leaves the system stops being data and becomes a quotation. You paste it into a board deck, a status email, a slide someone screenshots. From that second the number is frozen, and the definition that produced it keeps moving without it.

We built an entire discipline to keep the first half of that sentence honest. Almost none of it watches the second half.

The record is the thing governance guards. In a regulated shop the raw rows are attributable, contemporaneous, and [preserved for years](/posts/data-governance-that-survives-an-inspection/) whether or not anyone ever looks at them again. The audit trail exists to answer one question with certainty: was this record altered after the fact. It answers it well. A stability reading logged three years ago is exactly the bytes it was when it was logged, and you can prove it.

But the number in the deck was never the record. It was an answer computed from the record, and the computation ran through a definition. "Available samples" isn't a column you read. It's a rule the steward wrote about which rows count, and [that rule is a live object](/posts/record-is-not-the-definition/). It gets refined. Someone decides reserved specimens shouldn't count, or that a quarantine release should, and the definition moves to the better meaning. That is governance working, not failing.

Then the definition moves. The number you quoted last quarter stops matching what the same question returns today, and nothing anywhere recorded which version produced the figure on the slide. The raw rows are pristine. The audit trail is intact. The number is wrong now anyway, not because anyone tampered with anything, but because it answers a question that no longer means what it meant when you asked it.

The record has a version. The answer doesn't.

This stays invisible until two numbers meet. One figure sitting alone in an old deck is harmless; nobody recomputes it. The damage lands when someone sets this quarter beside last quarter and reads the delta as a trend. If the definition held steady between them, the delta is real. If it moved, the delta is part signal and part redefinition, and there is no way left to separate the two, because the one fact that would let you, which definition each number ran through, was never stored with either one.

So you get a line on a chart that looks like the samples went up, when what went up was the count of things the current definition is willing to call a sample. The trend is an artifact of a governance improvement nobody logged at the point it mattered.

The fix is unglamorous and almost nobody does it: stamp the answer, not just the record. Every figure that leaves the system carries the definition version it was computed under, the way every row carries who touched it and when. Then a number in an old deck is legible on its own terms. You can look at it and know it ran through v3 of "available sample," that v3 was retired in March, and that setting it next to a v5 number is comparing two different questions wearing the same label.

Governance doesn't do this because the whole apparatus points at the input. We version schemas, we version pipelines, we lock the raw record behind controls a regulator will inspect. The output walks out the door in a screenshot with no provenance at all, and we call the system compliant because the part that got inspected was clean.

The audit trail was built to answer whether a record was altered. The question that decides whether a slide is a finding or an artifact is what the number meant when you said it, and there is nothing in the stack that can answer that once the definition has moved on.
