---
title: "How Many Samples Do We Have?"
date: 2026-05-28
draft: false
tags: ["data", "architecture"]
summary: "Someone asked how many samples we have and three systems gave three different numbers. The dependency order behind vocabulary, ontology, semantic layers, catalogs, and contracts, and why the piece everything stands on is a role most orgs never seat: the data steward."
---

Someone asked how many samples we have. It should have been a one-line query. I got three numbers from three systems, none of them matching, and a meeting to reconcile them.

Around the same time, leadership wanted a semantic layer, I'd been pushing for a data catalog, and a planning doc had "adopt data contracts" sitting in it with no owner. Four initiatives. And if you'd stopped me in the hallway, I couldn't have given you a clean answer for why we needed all four, which one comes first, or who builds what. So before spending a budget cycle on the wrong end of it, I worked out the dependency order.

Here's the order. And here's why the whole thing is so hard to keep standing.

The first question is why we need all these separate things at all. They sound like the same thing described by four different vendors.

They're not. Each one answers a different question, and "how many samples do we have" needs every one of them answered before it has a number.

Start with the word. What is a sample? The vial that showed up at the loading dock? If I split that vial into ten aliquots and freeze them separately, do I have one sample or eleven? If I run one specimen through two assays, is that one row or two? If I pool five aliquots back into a single tube, what happens to the count? Is a fully consumed sample still a sample? Is a control? Every one of those is a question about grain: what does one row in the samples table actually represent. Until somebody decides, the table has no grain, and a table with no agreed grain cannot be counted. The set of those decisions, what the words mean and what *one* of a thing is, is your **vocabulary**: the controlled definitions everything downstream inherits.

Then there's how the words relate. A subject yields many specimens. A specimen splits into many aliquots. Aliquots pool, split again, and derive into new entities, each of which needs its own identity and a key that ties it back to its parent. Those words, sample and specimen and aliquot and subject and batch, aren't synonyms. They're a graph. Write that graph down, the entity types and the relationships between them, and you have an **ontology**. Not the academic kind. The working kind: the entities, their keys, and how lineage flows from parent to child. Most orgs use these five words interchangeably in conversation and then wire them together five different ways across five systems.

Now the report. The dashboard says 50,000 samples. Fifty thousand of what? Physical containers in freezers? Logical specimen records? Distinct samples regardless of how many tubes they were split into? The number is meaningless until you know which definition it encoded and which tables it ran against. The **semantic layer** is where you define a measure like "available sample" exactly once, against named tables, so every dashboard asking that question gets the same answer back. It's the translation from the vocabulary to the physical schema. Skip it and every analyst reimplements the definition in their own SQL, which is precisely how you end up with three numbers.

And where does the data live? Sample records sit in the LIMS, in instrument exports, in the electronic lab notebook, in the freezer inventory. Four systems, four schemas, four owners, and no standing agreement on which one is the system of record for a given field. The **catalog** is the inventory of all of it: what data exists, which system holds it, what each field means, and where it came from. It's the map, plus the lineage that proves the map is still current.

Last one. When the inventory team renames a status, or changes what "available" means by splitting it into consumed, depleted, and archived, every count downstream shifts and nobody gets a heads-up. A **data contract** is the versioned interface at that boundary. The producer commits to a schema and a set of semantics, and breaking either one becomes an announced, versioned change instead of a surprise your dashboard absorbs in silence.

Five things. Five different questions. You need all of them because "how many samples" touches all five, and a gap in any one is enough to hand you three numbers and a meeting. And none of the five is a build-once artifact. Each one is a living thing somebody has to keep true after it ships.

So where do you start? This is the part that matters, because the order you'll be asked for is the reverse of the order that works.

Leadership asks for the semantic layer. Of course they do. It's the visible one, the one that produces the dashboard, the one you can fund and point at in a review. But the semantic layer is an output. It translates meaning. It cannot translate a meaning nobody has agreed on yet. You can't define "available sample" as a measure until someone with the authority to decide has said what an available sample is. Start at the top and what you build is a very precise machine for encoding a disagreement.

Which leads to the question underneath all of it: who defines what? And this one has no technical answer. Defining what a sample is looks like a data problem, so it lands on the data team by default. We can model anything you describe. We cannot tell you whether a consumed aliquot still counts, because that isn't a modeling decision. It's a judgment about how the business treats its own work. The role that's supposed to make that call has a name: the **data steward**, the working front of what most orgs file under data governance. A steward owns the definitions for a data domain. They're accountable for what the words mean, they sign off on changes to them, and they sit close to the work, on the science side, not inside the data team. Most orgs publish a governance policy and never seat an actual steward. So the definition falls to whoever happened to write the query, and you get four reasonable definitions, none of them official, all of them running in production.

So who owns the chain end to end? Nobody, and that is the whole problem. It runs from meaning at the bottom to dashboards at the top. The bottom belongs to the people doing the science. The top belongs to the data and platform teams. There's a seam through the middle that nobody designed. It's just where one org's mandate ends and the next one's begins. The vocabulary sits on one side. Every tool that depends on the vocabulary sits on the other.

That's why it rots, and the rot is the part people underestimate. Defining a sample once is hard. Keeping that definition true for three years, through reorgs, new instruments, and a migration off the old LIMS, is harder, and it never finishes. Every time the bench changes how it works, or the platform team ships a new system, one side of the seam moves and the other doesn't hear about it. The catalog goes stale. The contracts start to lie. The semantic layer keeps confidently returning a number that used to be true.

This is what data governance actually is. Not the policy PDF. The standing function that keeps definitions, lineage, and contracts honest while the org moves underneath them. Treat it as a one-time project and you've signed up to rebuild the same foundation every couple of years. None of the hard part is technical. The modeling is tractable. The governance is the gap.

## The way out runs backwards

Everybody points at the top of the chain. You start at the bottom, and you start by seating a data steward. Not a tool, not a project. A named person on the science side with the authority to decide what a sample is and make the decision stick. If that seat is empty, nothing above it holds and no tooling will save you. This is the step everyone skips, because it's a governance problem, not an engineering one, and you can't buy your way past it.

Then the steward defines the vocabulary, and keeps it small. The handful of entities that carry real weight: sample, specimen, aliquot, subject. Pin the grain of each one. A short controlled definition everyone honors beats an exhaustive one nobody finished.

Then the relationships. The working ontology: the entity types, their keys, and the parent-to-child lineage. Enough that two engineers reading it would model the same graph, and no more than that.

Now the catalog and the semantic layer finally have something to stand on. The catalog inventories real definitions instead of guessing at them. The semantic layer encodes the steward's measures once, against the system of record, instead of reinventing them per query. This is where the data team gets to run, and where the spend actually buys something, because it's pointed at meaning that already exists.

Contracts come last, and they go at the seams. Once the meaning is settled and the tools encode it, the contract is the versioned boundary that keeps the bench and the platform from drifting apart again. It's what makes the agreement survive the next reorg and the next schema migration.

And then it isn't finished, because this part has no end state. The steward keeps the definitions current as new assays and instruments show up. Changes to what a sample means go through review instead of surfacing in a dashboard six months later. The catalog and the contracts get checked against reality on a cadence, not at a launch. That standing discipline is the governance, and it's the whole difference between a foundation that holds and one you quietly rebuild every two years.

The steps are easy to list and brutal to execute, and almost all of the difficulty sits in the first one, because the first one isn't an engineering task. It's getting a person to put their name on a definition and defend it the next time a team wants an exception.

The catalog, the semantic layer, the contract tooling: you can buy every bit of it. A data steward who will own what a sample is, and keep owning it as the org shifts around them, you have to appoint. That's the line nobody puts on a roadmap.

So the question was never which semantic layer. It was who gets to decide what a sample is. If you can't name that person, you don't have a tooling gap. You have your actual first project.
