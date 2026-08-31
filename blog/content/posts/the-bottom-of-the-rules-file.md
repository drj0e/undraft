---
title: "The Bottom of the Rules File"
date: 2026-09-04
draft: false
tags: ["automation", "code-quality"]
summary: "The same requirement can live in the instructions you hand an agent and in a gate that checks the output, and those two are not equally binding. The measurements on multi-instruction compliance say something stranger: every line you add to the file weakens the lines already in it."
---

In my pipeline, "don't touch files you weren't assigned" exists in two places. One is a sentence in the instructions the agent reads before it starts. The other is [a gate that reads the finished diff](/posts/who-watches-the-watcher/) and rejects it when a path is out of scope.

Same requirement, written twice. <mark>One of them holds every time. The other holds at a rate.</mark>

That a prompt is not a guarantee is not news to anybody running agents. What I had never done is treat the rate as an input to how the file gets written, and there are measurements on it now.

IFScale scales a business-writing task from ten verifiable instructions up to five hundred and runs it across twenty models. [At maximum density the best frontier models finish around 68%](https://arxiv.org/abs/2507.11538), and the misses aren't spread evenly: models favor the instructions that came earlier in the prompt. A separate benchmark, ManyIFEval, stops at ten instructions and finds [the odds of satisfying all of them tracking per-instruction accuracy raised to the power of the instruction count](https://openreview.net/forum?id=R6q67CDBCH), with per-instruction accuracy itself sagging as the count climbs. On the models in that study, ten at once left GPT-4o clearing all ten 15% of the time and Claude 3.5 Sonnet 44%.

Both papers are describing a property of models. Read them as a property of the file and the shape of the problem changes. The file has a capacity, and every line you add lowers the odds on the lines already sitting in it, including the ones you wrote first and have long since stopped thinking about.

Which changes what a guard is worth. I had been valuing each gate against the failure it catches, one at a time. But pulling a requirement out of the instructions and into code does something for the requirements it leaves behind. When the sentence about file paths comes out, everything still in there is competing with one less thing. A [PreToolUse hook that exits 2](https://code.claude.com/docs/en/hooks) blocks the tool call whatever the model had decided to do, and it hands the rest of the file a little of its capacity back.

The problem is which lines are eligible. A path is checkable, a file count is checkable, a build either succeeds or it doesn't. What can't move is the prose. When to stop and ask instead of picking one of two defensible readings. How much of the reasoning to put in a commit message. What to do on the third failed attempt. None of it has a verifier, which is precisely why it's written in English in a file, and it's the same set of lines paying for every new rule about paths and formatting.

So the rules you can enforce are the cheap ones, and they are crowding out the rules you can only ask for.

A line of English is the cheapest thing in this stack to write, so that is where a fix goes first. Nothing in the file marks where enforcement stops and preference begins. The agent reads straight through the boundary and honors both the same way, which is to say probably.
