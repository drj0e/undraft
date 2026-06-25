---
title: "Agents Don't Read the Glossary"
date: 2026-07-02
draft: false
tags: ["data", "ai-tooling"]
summary: "When an agent generates a query, it binds to the column name, not the steward's definition. A misleading name used to be a nuisance a new hire tripped over once. Now it's a hazard that ships the wrong number every run."
reviewed: true
---

When an agent decides which column holds the number you asked for, what does it actually read?

The name. The type, if it's lucky. Almost never the definition.

A human analyst pulling the same report has a path to the steward. They hover the column, read the note that says `available_sample` counts specimens released from quarantine and excludes the destroyed and the reserved, and either trust it or go ask. The glossary entry exists for them, and they can be made to walk through it. An agent turning a question into SQL binds on the schema. It sees a column named `available_sample`, decides that matches "available samples," and writes the query. The definition the steward labored over sits one lookup away, unread, because nothing in the agent's path forces it through.

So the distance between what a column is named and what it means stops being a documentation problem and becomes an execution one.

For years a misleading name was a nuisance you could absorb. A new hire trips on it once, gets a number that looks off, asks someone, learns the gotcha, and never makes the mistake again. The trap gets paid down into institutional memory. The agent has no institutional memory and asks no one. It trips on the same name every run, confidently, and hands the wrong figure to whatever consumes its output, which is increasingly another agent that also won't ask.

I've [written about three systems giving three answers](/posts/how-many-samples-do-we-have/) to one question about samples. That was humans reconciling definitions they at least knew were in play. This is a sharper version of the same wound. The agent doesn't know a definition exists to be reconciled. It treats the name as the meaning, because the name is the only thing in front of it.

Which inverts a piece of governance advice I'd have filed under bikeshedding a year ago. "Rename the column so it says what it means" was always low-status polish; you wrote the real meaning into the catalog and left the identifier alone, because the handle didn't matter as long as the documentation did. When the consumer reads the catalog, the name can be sloppy. When the consumer reads only the schema, the name is the catalog.

The meaning has to migrate into the identifier, the type, the constraint, the things the machine can't route around on its way to an answer. That is expensive. Renaming a column forty queries depend on is exactly the kind of change governance programs flinch from. But the prose definition is now addressed to a reader who has left the building, and the steward writing more of it is doing careful work for an audience that isn't coming.
