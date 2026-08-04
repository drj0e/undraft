---
title: "Exactly These Actions"
date: 2026-08-11
draft: false
tags: ["ai-tooling", "automation"]
summary: "Terraform can promise 'exactly these actions' because apply executes a saved plan instead of thinking again. My agent pipeline's dry-run default makes no such promise, and I've stopped pretending it does."
---

Run `terraform plan -out=tfplan` and Terraform writes what it intends to do into a file. Hand that file to `terraform apply` and two things vanish: the confirmation prompt, and the tool's freedom to reconsider. The [plan output](https://developer.hashicorp.com/terraform/cli/commands/plan) says it plainly: "To perform exactly these actions, run the following command to apply." Passing the file [is the approval](https://developer.hashicorp.com/terraform/cli/commands/apply). Apply decides nothing; the decisions are in the file, and execution replays them. If the world moved between plan and apply, the run fails as stale instead of adapting around the difference.

I keep returning to that design, because my own agent pipeline has had a dry-run default since I built it, and I imported the flag's meaning from the wrong kind of tool.

Dry-run entered my [operational stack](/posts/the-stack-nobody-talks-about/) as a posture: deny side effects unless explicitly opted in, watch what the agent would do before letting it do anything. The template is the `--dry-run` flag on a migration script or a cron job. For those tools the flag is honest, because the two runs walk the same code path with the writes switched off in one. The rehearsal predicts the performance. The performer can't improvise.

An agent improvises by construction. It derives its plan fresh each run from everything in front of it: the task, the repo as it stands this minute, the output of each tool call, the retry that happened this time and didn't happen last time. Hand it the same task twice and you can get two different plans, both defensible, neither a rerun of the other. There's no determinism knob to rescue this. Temperature zero doesn't even make the model's own output reproducible in practice, because [inference results shift with how the server batches traffic](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/). And a perfectly reproducible model would still replan against a repo that moved overnight.

So the dry run I approve and the wet run I then launch share a prompt, not a path. A dry run of a script is a preview. A dry run of an agent is a sample: one draw from the space of runs the task can produce, and the draw I inspected is already gone.

Which makes "approved after dry-run" a strange sentence. What did the approval attach to?

Terraform's answer transfers cleanly. Split planning from execution and make the plan the artifact. Let the dry run produce a plan worth the name: the files it will touch, the commands it will run, the diffs it intends. Bind the approval to that file, the same move as the [hash-gated spec approvals](/posts/agent-world-reinventing-part-11/) already in my pipeline, pushed one level down, from "this is the task I authorized" to "these are the actions I authorized." Then the wet run stops being a second improvisation and becomes an executor. It performs the plan. A step that no longer applies means the plan is stale, and a stale plan is a stop and a fresh approval, the same as Terraform refusing to apply against drifted state.

The objection writes itself: mid-run adaptation is the reason to use an agent instead of a script. Keep the adaptation. Move it. Adaptation during planning costs a rejected plan. Adaptation during execution costs whatever the action costs, and it spends an approval that was granted to a different run.

Terraform's promise is three words: exactly these actions. It took a plan format, a state file, and a refusal to think at apply time to make them true. None of the agent stacks I've used can say them yet, mine included.
