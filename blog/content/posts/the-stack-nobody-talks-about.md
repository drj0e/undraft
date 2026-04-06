---
title: "The Stack Nobody Talks About"
date: 2026-04-05
draft: false
tags: ["ai-tooling", "architecture", "automation"]
summary: "The model is not the system. The system is everything required to make model output selectable, constrainable, auditable, and stoppable. I spent a month building that system. Here's what it actually looks like."
---

A few weeks ago I wrote about [the missing verification layer](/posts/who-watches-the-watcher/) in AI code generation. The argument: nobody's building the pipeline between "agent wrote code" and "code is safe to ship."

I built that pipeline. It works. And it immediately exposed the next problem, and the one after that, and the one after that.

The model is not the system. The system is everything required to make model output selectable, constrainable, auditable, affordable, and stoppable. I've spent the past month building that system across two projects: one that generates and guards code, and one that orchestrates autonomous workflows through GitHub Actions. The takeaway is simple: once you go past interactive pair-programming, reliability stops being a model-quality problem and becomes a systems-design problem.

Each layer I built exists because the layer below it wasn't enough.

## Trusting the output

I [covered this in detail](/posts/who-watches-the-watcher/) last time. The short version is a seven-stage guard pipeline, ordered from cheapest checks to most expensive. Empty diff. Scope enforcement. Compilation. Structural invariants. Orphan detection. Cross-session identity tracking. Only after the deterministic stages pass does a separate AI reviewer evaluate whether the changes match the original intent.

Most agent problems are caught without burning a single token. The ordering matters. By the time the expensive stage runs, the changeset already passes every binary check I could think of.

GitGuardian arrived at a [similar pattern](https://blog.gitguardian.com/automated-guard-rails-for-vibe-coding/) for security validation. Cursor's [FastRender experiment](https://cursor.com/blog/scaling-agents) ran 2,000 concurrent agents across a million lines of code. At that scale, this layer stops being optional.

But a guard pipeline only protects you after a task is chosen. It says nothing about whether the task was worth doing.

## Trusting the task

When an agent runs unattended, someone still has to pick the work. If the task is vague, the agent interprets it creatively. If the task is already done, the agent finds something else to do anyway. If the task has unmet dependencies, the agent works around them in ways you didn't want.

I built a structured markdown backlog where each task carries a title, scope, constraints, acceptance criteria, and status. An operator script reads the backlog, finds the highest-priority unblocked item, validates that it has enough substance to act on, and sets up the workspace: clean git state, feature branch, snapshot of the starting position.

The agent doesn't decide what to work on. The system decides. The agent executes within those boundaries.

This matters more as task horizons expand. Anthropic's [2026 Agentic Coding Trends Report](https://resources.anthropic.com/2026-agentic-coding-trends-report) notes agents now average 20 autonomous actions before requiring human input, with session lengths up from 4 minutes to 23 minutes. Longer runs make bad task selection more expensive. The backlog and operator layer exists because the guard pipeline doesn't care what the agent was supposed to be doing. It only cares whether the output is structurally sound. Those are different questions.

## Trusting the operation

Guard pipeline validates output. Operator selects tasks. The system runs overnight on a schedule. Now the failures have nothing to do with code quality or task selection.

An agent that burns through your API budget at 2am. An agent that pushes to a shared branch because nothing enforced dry-run. An agent that runs the same task twice because the last run didn't update status. An agent that acts on a spec someone edited after it was approved.

Deny by default. Require explicit opt-in for anything with side effects. That's the principle. The implementation is scheduled execution through GitHub Actions and cron, per-agent budget caps with hard stops, dry-run as the default, append-only audit logs, and approval gates with hash-based validation so a spec change automatically invalidates the approval.

Simon Willison's [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) frames the trust model: private data, untrusted content, external communication. If your agent touches any two of those three, you need every gate I just described. Very few people are shipping this operational layer as a coherent product. Most of us are assembling it from parts.

## The part that gets weird

The guard pipeline self-shipped features in one session. In a later session, it composed on its own prior output without being told those features existed. The system maintains persistent awareness of what it has built, so when a new task requires capabilities from a previous run, the agent can discover them through context and build on top of them.

The operator scripts that select tasks and create branches were themselves refined through the same backlog-driven process they orchestrate. I added a task to improve the task selector. The system selected that task, built the improvement, and the guard pipeline validated it before it merged.

The stack is no longer just supporting the work. It is participating in the loop that shapes, constrains, and improves the next version of itself. This isn't theoretical self-improvement. It's bounded compounding: agent writes code, guard pipeline validates it, and validated code becomes context for the next run. Each session compounds on the last, but only through the same gates everything else passes through.

## Where this actually stands

The infrastructure-to-useful-output ratio is humbling. More engineering hours went into making agents reliable than the agents have saved. That math might flip eventually. It hasn't flipped yet.

The ecosystem is catching up. Anthropic is documenting the patterns. GitGuardian is shipping guardrails for the output layer. But the full operational stack, selection, constraint, memory, budgets, approval, is still almost entirely custom work.

Past a certain point, you are not adopting an agent. You are operating a stack. The agent is just the part people can see.
