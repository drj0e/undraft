---
title: "How Many Samples Do We Have?"
date: 2026-05-28
draft: false
tags: ["data", "architecture"]
summary: "Someone asked how many samples we have and three systems gave three different numbers. Working out why an org needs vocabulary, ontology, a semantic layer, a catalog, and contracts all at once, and why the piece everything depends on is the one nobody owns."
---

Someone asked how many samples we have. It should have been a one-line query. Instead I got three numbers from three systems, none of them matching, and a meeting.

Around the same time, management wanted a semantic layer. I wanted a data catalog. Someone in a planning doc had written that we really ought to have data contracts. And I couldn't actually explain, out loud, why we needed all of these things, which one came first, or who was supposed to build any of them. I just knew we were short on all of them at once.

So I sat down to work it out. This is me working it out.

The first question is why we need all these separate things. They sound like the same thing described by four different vendors.

They're not. Each one answers a different question, and "how many samples do we have" needs all of them to have an answer.

Start with the word itself. What is a sample? The vial that showed up at the loading dock? If I split that vial into ten aliquots and freeze them separately, do I have one sample or eleven? If I run one specimen through two assays, is that one sample or two? If I pool five aliquots back into a single tube, what happened to my count? Is a sample that's been fully consumed still a sample? Is a control a sample? Every one of those is a real question with a real answer, and the answer is a decision somebody has to make. That set of decisions is the vocabulary. It's the agreement on what the words mean.

Then there's how the words relate to each other. A subject gives multiple specimens. A specimen splits into multiple aliquots. Aliquots get pooled, split again, derived into new things. Sample, specimen, aliquot, subject, batch. Those aren't synonyms. They're a family tree, and most of the org uses them interchangeably in conversation and then wires them together differently in every system. Writing down that family tree, the entities and how they connect, is the ontology. Not the academic kind. Just: here is what these things are, and here is how they hang off each other.

Now the report. The dashboard says 50,000 samples. Fifty thousand of what? Physical containers sitting in freezers? Logical sample records? Distinct specimens, regardless of how many tubes they got split into? The number means nothing until you know which definition it encoded and which tables it ran against. The thing that maps the agreed-on words to the actual columns in the actual database is the semantic layer. It's the translation between what people say and where the data lives.

And where does the data live? Sample information sits in the LIMS, in instrument exports, in the electronic lab notebook, in the freezer inventory. Four places, four shapes, four owners. The thing that tells you what exists, where it is, and where it came from is the catalog. It's the map of the territory.

Last one. When the inventory team renames a status, or quietly changes what "available" means by splitting it into consumed and depleted and archived, every count downstream shifts and nobody gets told. The thing that's supposed to hold the line at that boundary, the producer promising the consumer that the shape and meaning won't change without warning, is the contract.

Five things. Five different questions. You need all of them because "how many samples" touches all five, and a gap in any one is enough to hand you three numbers and a meeting.

So where do you start? This is where it got interesting for me, because the order you want is the reverse of the order that works.

Management asks for the semantic layer. Of course they do. It's the visible one, the one that produces the dashboard, the one you can fund and point at in a review. But the semantic layer is an output. It translates meaning. It cannot translate a meaning that nobody has agreed on yet. You can't build the layer that maps "active sample" to a query until someone with the authority to decide has said what an active sample is. Start at the top and what you build is a very sophisticated machine for encoding a disagreement.

Which leads to the question that actually matters: who defines what? And this one doesn't have a technical answer. Defining what a sample is looks like a data problem, so it lands on the data team. But the data team can't make that call. They can build anything you describe. They can't tell you whether a consumed aliquot still counts, because that isn't a modeling decision. It's a decision about how the business thinks about its own work. When the data team makes it anyway, by default, you get what we had: four reasonable definitions, none of them official, all of them running in production somewhere.

So who owns this? That's the whole problem, and it took me embarrassingly long to see. The chain runs from meaning at the bottom to dashboards at the top. The bottom belongs to the people doing the science. The top belongs to the data and platform teams. There's a seam running right through the middle that nobody designed. It's just where one org's responsibility stops and the next one's starts. The vocabulary is on one side. Every tool that depends on the vocabulary is on the other.

That's why it rots. Every time the bench changes how it works, or the platform team ships a new system, one side of the seam moves and the other doesn't hear about it. The catalog goes stale. The contracts start to lie. The semantic layer keeps confidently returning a number that used to be true.

The difficulty was never technical. It's that the thing everything depends on sits in the one place with no owner.

## The way out runs backwards

Everybody points at the top of the chain. You start at the bottom, and you start by naming a person. Not a tool, not a project. A person who is allowed to decide what a sample is and whose decision sticks. Someone on the science side, with enough standing to end the argument. If that seat doesn't exist, nothing above it holds, and no amount of tooling saves you. This is the step everyone skips, because it isn't technical, it's uncomfortable, and it can't be bought.

Then write down the vocabulary, and keep it small. Not every entity in the building. The handful that actually matter: sample, specimen, aliquot, subject. Get those defined and agreed by the person who is now allowed to agree to them. A short document everyone honors beats a perfect one nobody finished.

Then the relationships, the lightweight ontology. How those few things hang off each other, what derives from what, parent and child. Enough that two people reading it would draw the same picture. No more than that.

Now, finally, the tools have something to stand on. The catalog is cataloging real definitions instead of guessing at them. The semantic layer is translating an agreement instead of inventing one. This is where the data team gets to run, and where the money actually buys something, because it's pointed at meaning that already exists.

Contracts come last, and they go at the seams. Once the meaning is settled and the tools encode it, the contract is what keeps the bench and the platform from drifting apart again without anyone noticing. It's what makes the agreement survive the next reorg.

The steps are easy to write down. They're brutal to do, and almost all of the difficulty sits in the first one, because the first one isn't a task you can hand to engineers. It's a person agreeing to be accountable for a definition, and to defend it the next time someone wants an exception.

The catalog, the semantic layer, the contract tooling. You can buy every bit of that. The agreement on what a sample is, you have to earn, and it's the only piece nobody put on a roadmap.

So the question was never which semantic layer. It was who gets to decide what a sample is. If you can't name that person, you don't have a tooling gap. You have your actual first project.
