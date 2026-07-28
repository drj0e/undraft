---
title: "Category 5 All the Way Down"
date: 2026-08-04
draft: false
tags: ["platform-engineering", "compliance"]
summary: "The language of platform extraction points down: layer, plumbing, infrastructure. GAMP's category table sorts software by who wrote it, not where it sits, and that mismatch belongs in the extraction pitch."
---

Platform extraction comes with a vocabulary, and all of it points down. Layer. Plumbing. Infrastructure. The words carry a promise: this code is on its way to becoming like the operating system, settled and boring, less watched rather than more. I've been [pulling a storage platform out of an application](/posts/your-app-is-wearing-a-platforms-clothes/) at work, so I've been saying these words for months.

The shop I do this in runs under GxP, and validation planning there starts from [GAMP 5](https://guidance-docs.ispe.org/doi/book/10.1002/9781946964571) and its [software categories](https://intuitionlabs.ai/articles/gamp-5-categories-explained). Category 1 is infrastructure, the operating systems and database engines and middleware everything runs on. Category 3 covers products used as shipped, category 4 products you configure. Category 5 is code you wrote, and it owes the most evidence of the four: specifications, source review, structured testing, the whole lifecycle. There is no category 2. Firmware lost its seat when GAMP 5 replaced GAMP 4.

Look at the sort key. Software earns the cheap end of that table by being bought, standard, and widely run, its failure modes found on other shops' budgets. It earns the expensive end by being written by you. Altitude appears nowhere in the scheme. A custom layer at the bottom of the stack owes exactly what a custom app at the top owes.

Which undoes the promise in the vocabulary. The storage layer was custom code while it lived inside the application, and it stays custom code standing beside it. Category 5 before the extraction, category 5 after. The refactor moves it down the diagram and zero rows in the table.

That asymmetry deserves its own line in the extraction pitch. A commercial product doing the same job would walk in as category 3 or 4: assess the supplier, then verify your configuration and test your uses of it. The in-house layer owes all of that plus the lifecycle evidence underneath, for as long as the code lives, with every validated consumer holding a stake in it. Same job, same position in the stack, a full category apart, and the difference keys on one fact: who wrote it. You can buy your way down the table. You can't refactor your way down it.

The [second edition](https://www.spectroscopyonline.com/view/understanding-and-interpreting-new-gamp-5-software-categories) softened the table's edges in 2022. Categories are a continuum now, real systems mix components from several of them, and critical thinking is supposed to beat checklist categorization. All of which is sensible, and none of which reads a bespoke storage layer as an operating system. The continuum runs on the axis the table always had: how many hands besides yours have hardened this code.

So the diagram and the validation plan will describe the same extraction in two vocabularies. In one, the apps got thinner and a platform slid underneath them. In the other there is no underneath. Just more category 5 than you had last quarter, with your name on every line.
