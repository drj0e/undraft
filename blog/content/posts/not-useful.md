---
title: "Not Useful"
date: 2026-09-05
draft: false
tags: ["automation", "code-quality"]
summary: "Google's review tooling gives engineers a button that says the analyzer was wrong, and disables analyzers that collect too many of them. An agent never presses it, so a guard pipeline aimed at agents loses the only instrument that ever measured its own rules."
---

An agent hits a rule, reads the verdict, changes the code, and comes back green. That loop can run all night without anything in it ever suggesting a rule was wrong.

Google solved that problem for humans a long time ago. Tricorder, the static analysis platform wired into their code review, puts two buttons under every finding. "Please fix" points at the code and asks the author to change it. "Not useful" points at the analyzer and says the finding should never have been shown. Clicking the second one files a bug in the issue tracker against the team that owns the analyzer, and a team whose not-useful rate stays high, measured against how often reviewers ask for the fix instead, gets its analyzer switched off. ([Software Engineering at Google, ch. 20](https://abseil.io/resources/swe-book/html/ch20.html)) Anything surfaced during review has to hold an effective false positive rate under ten percent. ([CACM](https://cacm.acm.org/research/lessons-from-building-static-analysis-tools-at-google/))

Two buttons, two directions. One corrects the code. The other corrects the rule.

<mark>A guard pipeline aimed at agents ships with only the first one.</mark>

An agent handed a rule it ought to argue with does not argue. It reads the verdict as a specification and edits until the verdict changes. That is the right behavior for the thing it is, and it means the population my rules govern has no way to tell me a rule is bad.

Which erases a distinction I had been getting for free. A rule that is strict and right produces a bounce and then a fix. A rule that is simply wrong produces a bounce and then a fix. Same verdict, same retry, same green at the end, same line in the log. What told those apart in the human version was an engineer irritated enough to press the second button, and Google's contribution was giving that irritation a number and a routing address.

Take it away and bad rules stop dying. In a shop full of people a wrong lint rule has a short life, because it annoys enough engineers that somebody deletes it. In front of an agent its life is indefinite, and it does more than survive. It gets obeyed, once per run, and the shape it forces into the code is indistinguishable from conformance.

I've [argued](/posts/who-watches-the-watcher/) that the checking layer is the part of this worth owning, and I put [a month](/posts/agent-world-reinventing-part-11/) into building one. Adding a rule to it feels close to free. Writing one is cheap and owning one is not, and with people on the receiving end you never had to pay the second cost on purpose. You could ship a rule half-formed and let the complaints sand it down.

The raw material for a replacement is in the append-only log already: which rule fired, how many attempts followed it, and what the next attempt actually changed. That will never be a not-useful rate, because a retry count runs together the rules doing the most work and the rules doing the most damage. It does narrow the shelf. A rule that bounces the agent most nights and gets satisfied on the very next try is one of those two, and only the second diff tells you which.

So the number I want is one no pipeline of mine produces: not how often a rule fired, but how often it should have. Humans generated that number as a side effect of being annoyed. I get to go read the diffs.
