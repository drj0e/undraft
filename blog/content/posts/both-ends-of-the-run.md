---
title: "Both Ends of the Run"
date: 2026-10-17
draft: false
tags: ["security", "architecture"]
shape: argument
origin: thread
reach: adjacent
summary: "Two September disclosures bracket the coding-agent session. One ran code before the first prompt, the other published to repositories the company never watched. A security review that inventories what the agent may do inside a session sees neither, so it needs two more lists."
---

Thirteen thousand screenshots is the count Glow Security put on it. Internal, pre-release images from more than 300 organizations, in over 900 public GitHub repositories, and in 93 percent of cases the repository sat under an employee's personal username. ([PixelLeak](https://glow.io/blogs/how-ai-agents-exposed-developer-screenshots-from-leading-tech-companies), September 29)

No prompt was injected. A developer asked a coding agent for a before-and-after screenshot of a UI change. The agent works in a terminal, and GitHub has no API for attaching an image to a pull request. So the agent solved it: it created a public repository to host the image and linked to it from the review. A small open-source tool exists for exactly that, its default backend creates public repositories, and about a third of the affected organizations had developers running it. The rest of the agents reinvented the workaround on their own.

Four weeks earlier, Manifold Security published the other September disclosure. [GitSpawn](https://www.manifold.security/blog/ai-coding-agents-git-hijack) (September 1): a repository's own `.git/config` can name a program under `core.fsmonitor`, and git runs that program during `git status`. Coding agents run `git status` at startup to gather context. In Manifold's words, open a folder with Claude Code and it runs git status before you type anything. The command ran as the user, outside the sandbox, with no approval prompt, and in one agent before the workspace-trust prompt was even shown. Seven agents, eight findings, four unpatched on the day it went out. Also their words: the vulnerability is not in the model, or in anything new.

Now put the two beside a security review of an agent setup, the kind the [OWASP cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html) lays out. Its controls are good ones. Sandbox the runtime, allowlist the commands, block the credential stores, never run auto-accept on an unfamiliar codebase. Sandbox, allowlist, approval prompt: each one wraps an action the agent takes after you've asked it for something. The nearest the sheet gets to the front end is rules files, which it calls security-critical configuration. A git config isn't a rules file. The session is the unit the review is written around, and the unit the permission model is written around too.

GitSpawn ran before the session had a first prompt. PixelLeak ran to a place the session's owner wasn't watching. One sits in front of the boundary, the other past it, and a review that inventories the middle sees neither.

I've been on the inside of that boundary myself. The operational layer I [built](/posts/the-stack-nobody-talks-about/) is deny-by-default, with explicit opt-in for side effects, and when I [listed](/posts/known-after-apply/) the side effects a run can take I got five: push a branch, open a pull request, post a comment, call an API, send a notification. Every entry happens after the first prompt. None of them is "create a repository," and none asks where the credential the agent holds is allowed to create one.

So the review needs two inventories, one at each end.

The first is everything that executes between opening the repository and the first prompt. Not what the agent is permitted to do. What runs on its own. Git configuration in the checkout. SessionStart hooks. Project settings the tool loads before trust is granted. Package scripts an install step triggers. The Claude Code changelog is a public record of how long that list runs: a 2.1.248 fix for the agents command skipping the workspace trust prompt when `CI` was set, a 2.1.268 fix for a respawned teammate picking up tools from a folder you hadn't trusted, a 2.1.281 fix for `claude --bg` running project hooks in a directory that hadn't passed the trust prompt. ([CHANGELOG.md](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)) Each of those is something that ran before the user said yes, and those are only the vendor's entries. The review's job is the shop's own: for this repository, on this machine, with these plugins, what starts when the folder opens. If the honest answer is "whatever the tool does," the pre-prompt surface has no owner.

The second inventory is every destination the agent's credentials can reach, with a column for who watches it. An agent running as the developer holds the developer's token, and that token reaches every place the developer can push, their own account included. Glow's remediation advice is to look beyond your own GitHub organization: repositories under employees' personal accounts, accounts of departed employees, releases, gists. That is the second inventory written backwards, after the fact. The review writes it forwards. Which accounts can this credential create something under? Which of those does anyone read? For most shops the second column has one entry, the org, and the token reaches three or four.

Simon Willison's [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) is private data, untrusted content, and external communication in one system. PixelLeak needed only the third, and no attacker. The agent was being helpful. It found the workaround a person would have found and would have known not to use, then published to the only place it could write.

Both ends come with a cheap test. For the front: open the repository with the agent, type nothing, and read the process list and the network log. Whatever appears is inventory one, and it ran under your name. For the back: list every destination the token can write to, and next to each, the person who would notice a new public repository there within a day.

The git status that ran when the folder opened has no line in the permission log. Neither does the repository the agent made to show you a screenshot.
