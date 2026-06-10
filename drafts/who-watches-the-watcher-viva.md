---
title: "Who Watches the Watcher? (Viva Engage version)"
target: viva-engage
draft: false
date: 2026-03-22
---

I've been spending a lot of time with AI coding agents lately, and I keep running into the same problem: everyone is focused on the generation layer. Almost nobody is focused on the verification layer.

Generation is no longer the interesting problem. The harder problem starts when you let an agent operate on a real codebase. It will define scope more aggressively than you intended. Ask it to fix security issues, and it may fix every issue it can find, including ones that introduce regressions because it doesn't understand the architectural or operational reasons something was built that way.

It optimizes for the prompt. The damage often comes from everything the prompt failed to constrain.

The evidence is building. [METR gave experienced developers](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) AI tools on their own repos. They took 19% longer while believing they were 20% faster. [Amazon had four Sev-1 production incidents in 90 days](https://www.getautonoma.com/blog/amazon-vibe-coding-lessons), including a 6-hour outage, with internal documents linking the trend to AI-assisted changes. Generation works. Nobody's reliably verifying the output.

The most effective guardrails usually aren't AI at all. Does it compile? Did it stay within the files it was supposed to touch? Did it violate structural rules? Does the diff contain meaningful changes? Deterministic checks with binary answers. In my experience, they catch north of 80% of the problems without another model call. AI-based review is most useful as the last stage, not the first.

An auditor can audit their own books. We don't let them. The same logic applies here.

The middle of the pipeline is underbuilt: the opinionated verification layer between "the agent wrote code" and "this is ready for a human to review or merge." Code generation is getting commoditized. The real value is in reliably determining whether the output is safe, constrained, and ready to ship.

Curious how other teams are handling this. If you're using AI coding tools, who or what is verifying the output? Is it a defined process, a dedicated toolchain, or just whoever happens to review the PR?
