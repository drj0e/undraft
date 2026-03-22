---
title: "Who Watches the Watcher?"
date: 2026-03-22
draft: false
tags: ["ai-tooling", "architecture", "code-quality"]
summary: "Code generation is a commodity. The defensible value is knowing whether the output is safe to ship, and almost nobody is building for that."
---

Code generation is a commodity. The defensible value isn't "my agent writes better code." It's "my system can tell you whether the code is safe to ship." Almost nobody is building for that. The demo is always the generation, never the check.

The tools that do exist sit at the extremes. On one end, real-time interception, catching dangerous operations as they happen. On the other, post-push review, looking at code only after a human opens a PR. That pipeline between "agent wrote code" and "code is ready to merge," the opinionated, layered system that actually decides if the output is trustworthy? It doesn't exist yet.

That gap is where the problems live. When you point an agent at a real codebase, it defines its own boundaries of action. Tell it to improve security and it'll make every change it considers a security improvement. Some of those changes will break your application, not because the fixes were wrong in isolation, but because the agent has no concept of why the code was written that way.

The agent optimized for what you asked. The damage comes from what you didn't specify.

The evidence keeps piling up. Cursor turned hundreds of agents loose to [generate a browser in Rust](https://cursor.com/blog/scaling-agents). An outside observer [checked the CI](https://www.theregister.com/2026/01/22/cursor_ai_wrote_a_browser/): 88% failure rate, not a single clean commit in the last hundred. A Replit agent [wiped a production database](https://www.theregister.com/2025/07/15/replit_ai_agent_database/) with 1,200 executive records, then created 4,000 fake profiles to cover its tracks. Google's [2024 DORA report](https://dora.dev/research/2024/ai-preview/) found that every 25% increase in AI adoption correlates with a 7.2% drop in delivery stability. [METR gave experienced developers](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) AI tools on their own repos. They took 19% longer while believing they were 20% faster.

The generation works. Nobody's reliably verifying the output.

The shape of the answer isn't complicated. Does it compile? Did it stay within the files it was assigned? Did it break any structural invariants? Does the diff contain real changes? Run those first. Deterministic questions with binary answers. In my experience, they catch north of 80% of the problems agents introduce without burning a single token. Then, and only then, run the AI-based semantic review asking whether the changes match the original intent. Each stage is cheaper than the next. Most problems never reach the expensive stage.

Most teams skip all of this. Let the agent generate, maybe run tests, hope a human catches the rest.

An auditor can audit their own books. We don't let them. When the same AI that wrote the code evaluates the code, it's inclined to find its own work reasonable. A guard pipeline needs checks that are genuinely external to the generation process. Checks that don't care how clever the solution is, only whether it meets hard criteria.

Billions going into making agents write better code. Almost nothing going into making the output trustworthy at the point of merge. When somebody builds for this, the generation layer becomes interchangeable overnight.
