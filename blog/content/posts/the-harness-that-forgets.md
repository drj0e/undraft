---
title: "The Harness That Forgets"
date: 2026-05-03
draft: false
tags: ["ai-tooling", "architecture", "automation"]
summary: "Birgitta Böckeler's harness-engineering framework treats iteration as human work. Someone watches, notices, edits the rules. That assumption breaks the moment agents run overnight. The next move is sensors with memory."
---

A few weeks back, [Birgitta Böckeler at Thoughtworks formalized](https://martinfowler.com/articles/harness-engineering.html) what a lot of us have been building piecemeal: the harness around a coding agent is a system of guides (steering it before it acts) and sensors (catching what it does wrong). Computational checks first, inferential checks second. Distribute them across the change lifecycle. Iterate the harness whenever the same problem shows up twice. [OpenAI's team describes the same shift](https://openai.com/index/harness-engineering/): "the discipline shows up more in the scaffolding rather than the code."

The framework is right. The iteration step is where it needs a sequel.

In her model, iteration is human work. *Whenever an issue happens multiple times, the feedforward and feedback controls should be improved.* A person watches, notices, edits the rules. That assumption breaks the moment you stop watching.

In the [operational layer I described last time](https://josephcapozzoli.com/posts/the-stack-nobody-talks-about/), agents run overnight on schedules, across multiple repos, on a budget. Nobody is sitting there spotting the third occurrence of the same misunderstood instruction. By morning, the same broken changeset shape has produced four rejections across three repos. The harness held. It also forgot.

<mark>A pipeline that resets every run is not a regulator.</mark> It is a checkpoint.

## The cheapest checks are also the dumbest

Computational-first ordering is a cost win. Empty diff. Compilation. Scope. Structural invariants. Run those before you run anything that costs a token, and most agent mistakes never reach the expensive stage. [I covered why](https://josephcapozzoli.com/posts/who-watches-the-watcher/) in the first post and Böckeler covers it more rigorously in hers. Nobody serious disagrees on the ordering.

The part nobody talks about is that those cheap checks are stateless. They don't know what they rejected yesterday. They reject the same thing today, and the agent burns the same tokens generating it, and the operator burns the same minutes triaging it. The compounding cost isn't in the gate. It's in the work the gate keeps repelling.

A few examples of what a sensor with memory could surface that a stateless one cannot:

- This file has been touched by three failed runs this week. Maybe the spec is wrong, not the agent.
- This invariant gets violated more often than it did a month ago. Drift, but slow.
- The semantic reviewer already rejected this approach, with this specific reason, on this codebase. Stop generating it.

Computational-first is a cost optimization. Memory is a learning optimization. The two compose. Most pipelines stop at the first.

## Sensors as state, not as runs

Most teams treat the guard pipeline as a series of independent runs. CI passes or fails. The judge says ship or don't ship. Pass-fail-pass-fail with no accumulation.

Treat the same sensors as state and the picture changes. Every rejection is a labeled example: agent did X, reviewer said Y, pipeline returned Z. Stored in a ledger keyed by file, intent, and changeset shape, that ledger becomes a private benchmark of how *this* agent fails on *this* codebase. After a few hundred runs you can cluster the failures, surface the patterns, and feed them forward as new guides. The keying is where this gets hard, and most teams will get it wrong before they get it right.

This is Böckeler's steering loop, but the human's role shifts. Instead of noticing the patterns, the human approves them. The system finds repeats. The human promotes them to rules. The system invalidates rules that stop firing.

The point isn't autonomy. It's leverage. The harness gets sharper without anyone editing it by hand.

## The behavior gap is still there

Böckeler is honest about what's hard. Maintainability and architecture-fitness harnesses use existing tooling. The behavior harness is the elephant: *did this changeset actually do what was asked?* AI-generated tests aren't trustworthy enough yet. The harness can't replace the human review step.

Memory doesn't solve this. It just makes it less expensive to be wrong.

What it can do is route attention. The system learns which changeset shapes correlate with later defects, and which intents tend to be misinterpreted. That's not behavior verification. It's behavior triage. Triage is what your time is actually short on.

The unsexy claim is the right one: a regulator with memory doesn't replace the human reviewer. It tells the human reviewer where to look first.

## Why this isn't a feature

You don't bolt memory onto a guard pipeline by adding a database. The pipeline has to be designed around persistent state from the start. Stages need to read prior decisions before running. Rejections need to be machine-readable, not stack traces. The semantic reviewer has to be able to ask: *have I seen this before, and what happened.*

Most existing tools were never built for this. Linters don't know what last week's lint runs found. Test runners don't know which tests failed in adjacent commits. CI systems forget everything between green and red. They're checkpoints.

When the harness becomes a learning system, the components inside it have to support that. The retrofit is painful. The greenfield version is straightforward. That asymmetry is going to determine who ships it first.

## The asset, not the cost

There's a version of this that gets philosophical about emergent behavior and self-improving systems. Skip it. The boring version is the right version.

The harness is a long-lived engineering asset. Assets that don't accumulate value over time aren't really assets. They're recurring costs. Build the guard. Order the checks cheap-to-expensive. Then give the whole thing a memory.

The teams that figure this out first will look like they have better agents. They won't. They'll have a regulator that reads its own notes.
