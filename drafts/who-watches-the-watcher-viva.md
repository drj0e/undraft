---
title: "Who Watches the Watcher? (Viva Engage version)"
target: viva-engage
draft: false
date: 2026-03-22
---

I've been spending a lot of time with AI coding agents lately, and I keep running into the same problem: everyone is focused on the generation layer. Almost nobody is focused on the verification layer.

The interesting failures don't show up until you let an agent operate on a real codebase. It will define scope more aggressively than you intended. Ask it to fix security issues, and it may fix every issue it can find, including ones that introduce regressions because it doesn't understand the architectural or operational reasons something was built that way.

It optimizes for the prompt. The damage comes from everything the prompt failed to constrain.

The evidence is building. [METR gave experienced developers](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) AI tools on their own repos. They took 19% longer while believing they were 20% faster. [Amazon had four Sev-1 production incidents in 90 days](https://www.getautonoma.com/blog/amazon-vibe-coding-lessons), including a 6-hour outage, with internal documents linking the trend to AI-assisted changes. Generation works. Nobody's reliably verifying the output.

The most effective guardrails usually aren't AI at all. Does it compile? Did it stay within the files it was supposed to touch? Did it violate structural rules? Does the diff contain meaningful changes? Deterministic checks with binary answers. In my experience, they catch north of 80% of the problems without another model call. AI-based review earns its place as the last stage, not the first.

An auditor can audit their own books. We don't let them. The same logic applies to an agent grading its own output.

So the part of the pipeline I'd actually invest in is the one nobody demos: the opinionated layer that sits between an agent writing code and a human being able to trust it enough to merge. Generation keeps getting cheaper and the failure surface keeps sliding downstream, which means the scarce skill a year from now won't be getting an agent to write code. It'll be proving the output is safe to ship before anyone's name is on it.

Curious how other teams are handling this. If you're using AI coding tools, who or what is verifying the output? Is it a defined process, a dedicated toolchain, or just whoever happens to review the PR?
