---
title: "Approved Against What"
date: 2026-09-21
draft: false
tags: ["ai-tooling", "automation"]
summary: "Git, Terraform, and GitHub all let an approval expire when the world it was given in moves. The approval gate in my agent pipeline hashes the spec and nothing else, so a sign-off outlives the codebase it was written against. The file list the pipeline already keeps is the fix."
---

`git push --force-with-lease` will overwrite a branch on the server only if that branch is still where you last saw it. The docs call it [taking a lease on the ref](https://git-scm.com/docs/git-push): the push names the value you expect the remote to hold, and if someone moved it, the push is refused. Terraform does the same for a saved plan. Let another apply change the state between plan and apply, and the apply stops with [`Saved plan is stale`](https://github.com/hashicorp/terraform/issues/27827). GitHub's branch protection does it for code review: it [records the state of the diff](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) when a reviewer approves, and if the diff changes afterward, even because something else merged into the target branch, the approval is dismissed as stale.

Three tools, one rule. An approval carries a snapshot of the world it was given in, and it dies when the world moves.

The approval gate in [my own pipeline](/posts/agent-world-reinventing-part-11/) carries a snapshot of something else. It hashes the spec. A person signs off on a task, and if anyone edits the spec afterward the approval voids itself. That is what Part 11 asks for when it says a signature has to be [linked to its record](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11/subpart-B/section-11.70) so it can't be transferred to a different one. The sign-off can't be moved to a spec it wasn't given for.

It can be moved to a codebase it wasn't given for, and that move happens on its own.

Say the spec reads: add retries to the HTTP client wrapper. Approved Tuesday. Wednesday a colleague lands a refactor that splits the wrapper into two clients. Thursday night the agent runs. The hash matches, the approval is valid, and the person who gave it has never seen the repository the agent is now reading. The spec's meaning was a function of the code it was written against, and the gate never recorded which code that was. A plan is being applied to a state it wasn't computed from, the exact condition Terraform refuses to proceed under.

GitHub's stale-approval rule doesn't reach this case, because it keys on a diff, and at approval time there is no diff. The spec is signed before a branch exists. The pipeline holds the approval, so the pipeline has to hold the lease.

The obvious lease is too wide. Hash the whole tree at approval, and on a repo with any traffic every approval has expired by the time the nightly run starts. The approver re-signs each morning without reading, and a signature given that way binds to nothing.

The pipeline already keeps a narrower list. Every task names the files the agent is allowed to touch, and a diff that wanders outside them [gets bounced](/posts/who-watches-the-watcher/). Hash the contents of those files at approval time. Before the first token of the run, hash them again. Same: run. Different: stop, and show the approver what moved, which is the diff they would want to read before re-signing anyway. That approval breaks on exactly one event: someone else changed the thing the agent is about to change.

It has the same hole as git's version. A lease on the wrapper says nothing about the caller two directories over that the refactor also touched, the way `--force-with-lease` checks the branch you're pushing to and none of the branches built on it. People use it anyway, because the alternative is `--force`, and a lease that covers the files you name is a long way up from a signature that covers none of them.
