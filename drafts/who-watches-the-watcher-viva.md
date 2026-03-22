---
title: "Who Watches the Watcher? (Viva Engage version)"
target: viva-engage
draft: true
date: 2026-03-22
---

I've been spending a lot of time with AI coding agents lately, and I keep landing on the same problem: everyone's building the generation layer. Almost nobody's building the verification layer.

AI can write code. That's settled. But when you turn an agent loose on a real codebase, it defines its own scope. Tell it to fix security issues and it'll fix every one it finds, including changes that break your app because it doesn't understand why things were built that way. It optimized for what you asked. The damage comes from what you didn't specify.

The interesting thing I've found is that the most effective guardrails aren't AI at all. Does it compile? Did it stay within the files it was supposed to touch? Did it break any structural rules? Does the diff actually contain real changes? Deterministic checks with binary answers. They catch north of 80% of the problems without any additional model calls. The AI-based review should be the last stage, not the first.

The broader industry pattern looks the same. Tools exist at the extremes: real-time interception that catches dangerous operations as they happen, and post-push review that only looks at code after a human opens a PR. The middle, the opinionated pipeline between "agent wrote code" and "code is ready to merge," is mostly empty.

Code generation is becoming a commodity. The defensible value is being able to tell you whether the output is safe to ship.

Curious what this looks like for other teams. If you're using AI coding tools, who's checking the output? Is it a process, a tool, or just whoever happens to review the PR?
