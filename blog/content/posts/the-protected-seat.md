---
title: "The Protected Seat"
date: 2026-10-05
draft: false
tags: ["automation", "code-quality"]
shape: question
origin: thread
reach: adjacent
summary: "A blameless postmortem is a trade: the engineer who broke it gives a full account of what they did and saw, and in return the account can't be used against them. When an agent wrote the change, its account is already in the transcript. The person whose account isn't is the one who approved the run."
---

Blameless names a trade. John Allspaw's [2012 post](https://www.etsy.com/codeascraft/blameless-postmortems) set the terms: the engineer closest to the failure gives a detailed account of what actions they took at what time, what effects they observed, what they expected, what they assumed, and how they understood the timeline as it ran. In exchange, nothing in that account gets them punished. Drop the second half and the first half dries up. An engineer expecting a reprimand, in his words, is disincentivized to give the details necessary to get an understanding of the mechanism, pathology, and operation of the failure.

Now the change was written by an agent. Its account is sitting in the transcript, every tool call timestamped, the assumptions it stated before each step still there to read. The postmortem gets the testimony for free and there is no one in the seat to protect. The trade looks finished. Read the run, write the timeline, fix the prompt. One writer has already called that last step a [root cause fallacy](https://tianpan.co/blog/2026-04-19-blameless-sre-postmortems-ai-failure-taxonomy), and I think the trouble starts earlier than the fix.

The transcript holds the agent's account. It holds no one else's.

Every merged agent change has a second person in it. In the pipeline I built, that seat is concrete: the [approval gate](/posts/agent-world-reinventing-part-11/) binds a sign-off to a hash of the spec, so a person approved the spec the agent worked from, and that approval is the nearest thing to a signature the result carries. What did they read before approving? How far into it? What did they take on faith because the guard was green? Those are the questions Allspaw's list exists to get answered, and no log answers them. They live in a person, the same way an author's [reasons](/posts/the-author-you-cant-ask/) used to.

<mark>Blame will land on that person, because blame lands on the nearest human, and it will do to an approver what it did to an author.</mark> An approver who expects "you approved it" to end their week reports a review more careful than the one that happened. The postmortem's root cause becomes "the agent added a flag that doesn't exist," a new rule goes into the guard, and the finding that the approval was a glance never gets written down anywhere.

A second pressure pushes the same way. Blaming a person costs the team something, which is why the practice had to be invented at all. Blaming the agent costs nothing. It can be done in the first sentence of the doc, and it ends the inquiry in the same place blaming an engineer did. The SRE book's line is that [you can't fix people, but you can fix systems and processes](https://sre.google/sre-book/postmortem-culture/). You can't fix the model either, and every system and process around it was built by a person.

So the protection moves to the approver. That much I'm sure of. What I can't work out is whether the protection survives the move.

For a human author, blameless assumes the honest account describes a slip the system made easy. Everyone involved, as the SRE book puts it, had good intentions and did the right thing with the information they had. The approver's honest account is different in kind. "I read the summary and trusted the green checks" is no slip. At the volume an agent produces, it's the steady state, and I've [argued](/posts/generation-got-cheap-review-didnt/) that a better model leaves that where it is. A postmortem that protects that account has to record, as a finding, that the approval step in this pipeline doesn't do what the org believes it does. And the next incident has to record it again.

I don't know what a blameless process does with an honest account that isn't a mistake.
