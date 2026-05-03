---
title: "The Step Between the Catalog and the Vector"
date: 2026-04-23
draft: false
tags: ["ai-tooling", "architecture", "data"]
summary: "Enterprise data strategy has moved its destination from 'break the silos' to 'vectorize everything.' The step in between is the layer that makes vectors actually work, and it's the one most roadmaps quietly skip."
---

Enterprise data strategy has changed its destination. A few years ago the target was a unified data platform: break the silos, get to a single source of truth. Today the target is vector-readiness. Make the data AI-ready. Embed everything.

The step between those two didn't go away.

Embeddings inherit whatever structure exists in the source data. Whatever shape it's in when you vectorize it is the shape it carries into the model. If your systems agree on what a customer is, your embeddings will too. If they don't, the embeddings encode the disagreement. The silos don't disappear. They move into the vector space, where they're harder to see and harder to debug.

This isn't a reason to slow down on vectors. Embeddings are useful. They make semantic search work, they power retrieval-augmented generation, they let AI systems find relationships keyword search would miss. The point isn't to delay them. It's to make sure they land on something they can stand on.

## What the Middle Step Is

Between raw data and useful embeddings, there's a layer that answers three questions: what do I have, where did it come from, and what does it mean. Some teams call this a catalog. Some call it a semantic layer. Some call it the data foundation. The name matters less than the work, which is making your data legible to something that isn't you.

If you can describe your core entities clearly, if you can trace where the data originates, if the relationships between things are written down somewhere instead of living in the heads of three senior engineers, you have most of what you need. The remaining work is almost always smaller than standing up a vector database.

Once that foundation is in place, vectors become what they're supposed to be. A layer that amplifies clarity, not one that's asked to invent it. The demos get better. The answers get more consistent. The system holds up when people ask harder questions, because the meaning was there before the math ran.

That's the data side. The [operational side](/posts/the-stack-nobody-talks-about/) is its own missing layer, and most teams aren't shipping that one either.

If there's an AI initiative on your roadmap, ask those three questions before you ask which vector database to use. If the answers are clear, you're ready. If they aren't, no embedding strategy is going to fix that for you.

That's the step. Not instead of vectorizing. Before it.
