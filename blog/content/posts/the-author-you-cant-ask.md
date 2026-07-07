---
title: "The Author You Can't Ask"
date: 2026-07-14
draft: false
tags: ["automation", "code-quality"]
summary: "Run git blame on a line an autonomous agent wrote and it points at a service account. The commit is spotless. The one thing debugging actually needs, a person who remembers why, already exited."
reviewed: true
---

You hit a line you don't understand, so you run `git blame` on it. That's the reflex, and it's worth being honest about what the reflex is for. Blame turns a confusing line into a name. The line was never the answer. The person the line points at is.

Run it on a line an autonomous agent wrote and it points at a service account.

The commit is real. It passed review, or passed whatever we call review now. It's been in main for weeks doing its job. And the thing that wrote it was a scheduled run that finished, dropped its context, and doesn't exist anymore. There's no one to ask why this line instead of the obvious other one. The reason it reads the way it reads was never written down, because reasons don't live in the diff. They live in the author, and the author was a process that already exited.

We keep arguing about whether agent code is correct. Guards, tests, the review that isn't quite review, all of it aimed at the output. [I've spent enough time there.](/posts/the-guard-the-agent-can-see/) Correctness is the tractable half. The half nobody costed is that debugging was never only about the code. It was about the author.

"Why is this here" is a question you ask a person. So is "is it safe to change," "what did this replace," "what breaks if I pull it out." Each one assumes a human at the far end of the blame line who remembers, or can rebuild, an intent. Blame, the review thread, the ping to whoever last touched the file, the comment that says why and not what. None of those are records. They're routing. They exist to carry a question to the one person who can answer it.

Autonomous authorship leaves the record spotless and cuts the routing. The commit is intact, the message is fine, the history reads clean. The question still forms. It just has nowhere to go.

A bug you can't ask about, you have to reverse-engineer.

That cost never lands when the agent writes the code. It lands months later, when someone inherits the line, forms the oldest question in maintenance, and finds the blame pointing at something that can't be paged. They're reading it cold and guessing at intent, which is the exact archaeology the whole social layer of engineering grew up to spare them.

We graded these systems on whether they could produce a correct diff with nobody watching. Nobody graded whether the diff could still be questioned after the thing that wrote it was gone. The first is a demo. The second is every week for the next five years, and it's the one that decides whether autonomous code is an asset or a mystery with your name on the maintenance rotation.
