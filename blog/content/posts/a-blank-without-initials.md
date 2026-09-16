---
title: "A Blank Without Initials"
date: 2026-09-17
draft: false
tags: ["data", "life-sciences"]
summary: "Paper GMP records don't allow an empty box: you cross it out, write N/A, initial it, date it. The database that replaced the form has a type for the empty box, and it spells four different absences the same way. Every count you run picks one of the four for you."
reviewed: true
---

Not measured yet. Measured, and the instrument returned nothing. Not applicable to this kind of specimen. Measured, and the value lost somewhere between the instrument and the row. Four different things can have happened to one specimen's volume, and the row holds one spelling for all of them: NULL.

Paper never allowed that. The PIC/S data integrity guidance, in force [since July 2021](https://picscheme.org/docview/4234), says in its section on paper records that unused, blank fields within documents should be voided, crossed out. The shop-floor version adds the rest of the ritual: a record has [no blank entry fields](https://creoconsulting.com/data-integrity-paper-records-in-gxp/), and a field with nothing to put in it gets lined out or marked N/A, with initials and a date. The rule reads as tidiness, and it is doing definitional work. An empty box can mean skipped, inapplicable, lost, or filled in later by someone who shouldn't have been near it, and the cross-out collapses those into one attributable statement: this person, on this day, says nothing belongs here. The absence gets a record of its own.

The clinical data standard the FDA takes submissions in went further and gave the absence its own columns. When a test in an [SDTM](https://www.cdisc.org/standards/foundational/sdtmig/sdtmig-v3-3/html) dataset was not done, `--STAT` carries `NOT DONE` and `--REASND` carries why. The row for the measurement that never happened exists, with a status and a reason, and a reviewer can tell it apart from the row whose result went missing.

Then look at every other table in the building. SQL has one NULL, and Codd spent part of 1986 [arguing that one was not enough](https://dl.acm.org/doi/10.1145/16301.16303): a mark for missing-but-applicable, a mark for missing-but-inapplicable, and a four-valued logic to go with them. Forty years on, the standard still has one. So the LIMS, the inventory tool, and the warehouse all run on the absence the paper rulebook banned. A blank without initials, in every nullable column, by default.

The count is where it bites. `COUNT(*)` counts rows. `COUNT(volume)` [skips the rows where volume is null](https://www.postgresql.org/docs/current/functions-aggregate.html). Ask how many specimens have a recorded volume and the answer depends on which of the four absences the query treats as no volume, and the query author settled that by whether they typed a column name inside the parentheses. The four meanings never came up.

When [three systems gave me three counts](/posts/how-many-samples-do-we-have/), every grain question I listed was about a row that exists: is an aliquot a sample, is a consumed one, is a control. The rows that half-exist have a grain question of their own, and in a schema without a status column the type system answers it before a steward gets there.

The fix is the one the paper form already had. An absence is a record, with a status and a reason, the way the SDTM row has them. That's a column and a constraint, and it costs a migration on a table with forty consumers. Skipping it means every report off that table gets read by someone who has to hold the four meanings in their head, and nothing in the schema will ever tell the next reader they exist.

The initials on a crossed-out box were governance at the grain of one cell: a named person deciding what an absence meant. The move to a database kept the box and dropped the initials, and every NULL in the table has been waiting since for someone to write them back in.
