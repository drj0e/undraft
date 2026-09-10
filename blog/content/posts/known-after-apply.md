---
title: "Known After Apply"
date: 2026-09-12
draft: false
tags: ["ai-tooling", "automation"]
summary: "Dry-run is the default in the operational layer I built around an unattended coding agent, and I've been reading more into that flag than it can deliver. A dry run is faithful up to the first side effect the agent reads the result of. After that it's a run through a world the agent made up."
reviewed: true
---

Dry-run is the default in the [operational layer](/posts/the-stack-nobody-talks-about/) I built around an unattended coding agent. Anything with a side effect is opt-in. I wrote that down as a safety property, and I've been treating the flag as though it told me what a run would do.

It tells me what the first step would do.

Terraform thought harder about rehearsal than any tool I use, and what it refuses to promise is the instructive part. `terraform plan` [makes no changes](https://developer.hashicorp.com/terraform/cli/commands/plan) to real infrastructure; it works out the difference between the state you have and the state you declared and shows you the diff. Where a value will only be decided by the cloud at creation time, an ID, an address, the plan prints `(known after apply)` in that slot. Martin Atkins's [write-up of those unknowns](https://log.martinatkins.me/2021/06/14/terraform-plan-unknown-values/) calls them placeholders for values Terraform cannot know until the apply step, there so the plan can be explicit about which values it can predict and which it can't. The rehearsal is honest because it labels its own guesses.

An agent computes its plan during the run, one step at a time, from whatever the last step returned. Push the branch, read what CI said, decide. Open the pull request, read the review bot, decide. Stub out the push and there is no CI result to read, so whatever the agent does next is conditioned on a reply it never got. A dry run of an agent is accurate exactly as far as the first side effect whose output the agent reads back. From that line on it's a transcript of a run through a world the agent invented. Terraform prints its parenthetical once per attribute it can't know. An agent's dry run, held to the same standard, would print it on every line after the first write.

Kubernetes met the same fact from the other direction. A [server-side dry run](https://kubernetes.io/blog/2019/01/14/apiserver-dry-run-and-kubectl-diff/) puts a request through defaulting, validation, and the whole admission chain and skips only the write to storage. Some of the code in that chain calls out, though. Admission webhooks can have side effects of their own, so the API server honors a dry run only when every webhook has declared it has none. Someone had to go through the steps and say which ones were dry.

Same job for an agent. List the side effects a run can take: push a branch, open a pull request, post a comment, call a real API with a real key, send a notification. Then split the list on one question. Does the agent read anything back? A notification is a pure write; the loop never looks at it again, and a stub covers it completely. A push is also a read, because the next decision depends on what CI says about it. Everything in that second column sits outside what the flag can rehearse.

The usual answer is a sandbox, a real run against a throwaway copy, and it's the right answer wherever the copy is faithful. Git is easy. A local clone holds everything the agent cares about. A review bot's comment, a live service's response, the URL a freshly opened PR hands back for the next step: each of those needs a double, and the double's replies are what the agent conditions on. A rehearsal against a double is only as accurate as the double's replies.

The default stays. Go down the side-effect list, mark every entry the agent reads back from, and count. That's how many places the rehearsal should have said known after apply and didn't.
