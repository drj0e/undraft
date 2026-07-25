---
title: "Keep the Transcript"
date: 2026-08-02
draft: false
tags: ["automation", "code-quality"]
summary: "The author-you-can't-ask post got one thing wrong. An agent's reasoning does get written down, token by token, in the session transcript. Then we keep the code forever and let the only explanation expire."
---

A merged agent commit leaves three artifacts behind. The diff, which will outlive every machine involved in producing it. The commit message. And, from the politer tools, a [Co-authored-by trailer](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors) naming the agent. The transcript of the run that produced all three is not on that list, and it's the only one of the four with an expiration date.

A couple of weeks back I wrote about [the author you can't ask](/posts/the-author-you-cant-ask/): blame on an agent-written line points at a service account, the reasons behind the line were never written down, and the process that held them is gone. That diagnosis was imported from human authorship, and it fits humans better than it fits agents. A human's reasons stay in their head until someone forces a design doc out of them. An agent's reasons leave its head by construction. It plans in text. It narrates the approach it tried first, the test failure that moved it to the second one, the retry after a guard bounced the diff. Every question that post said had nowhere to go has an answer sitting in the session log at the instant the commit lands, in more detail than any human author would ever volunteer.

Then the run ends, and that record goes wherever the vendor keeps session logs, on whatever retention schedule the vendor picked, in an account the repository has never heard of.

As a records decision this is upside down. The half we keep for the life of the repository is the output, which a model could produce again on demand. The half we let expire is the deliberation, and no rerun recovers it. A fresh run generates fresh reasoning about today's repo, not a memory of what last month's run was weighing.

The near-fixes each save the wrong slice. The trailer is attribution, and attribution was never scarce; blame already names the service account. Pasting the prompt into the PR description saves the question, and the question is the least informative part of the exchange; the part a maintainer will want is the middle, where the first approach died. The append-only audit log in [my own pipeline](/posts/agent-world-reinventing-part-11/) comes closest and still misses. It records every action and every guard verdict, because I built it to prove what happened. Audits ask what. Maintainers ask why.

The mechanics are the easy part. Git has carried [notes](https://git-scm.com/docs/git-notes) for years, a channel for attaching data to a commit without changing the commit. Archive the transcript with the repo's other artifacts, key it by commit hash, leave the pointer in a note. The property worth engineering for is retention parity: the explanation should live exactly as long as the code it explains, and every hop that leaves the repo's custody, a SaaS account, a laptop, a dashboard behind someone's login, is a place the trail will eventually break.

The author you can't ask was keeping a diary the whole time. We shred it on schedule.
