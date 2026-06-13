---
title: "The Agent Is a Custodian, Never an Owner"
date: 2026-06-19
draft: false
tags: ["ai-tooling", "compliance", "data"]
summary: "The whole agent-reliability project is trying to engineer the one thing a tool can't have: accountability. Data governance already named this. The agent is a custodian, and we keep trying to promote it to owner."
---

In a regulated shop, the database administrator never signs off that a batch number is correct. They run the system the number lives in. They provision access, take the backups, keep the lights on. The person who stakes their name on what the number *means*, in front of someone who can hold up a shipment, sits on the business side. Data management has a word for each of them. The one who runs the system is the custodian. The one who answers for the meaning is the owner. [DAMA's role model](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/) draws that line in ink, and [I've argued before](/posts/data-governance-that-survives-an-inspection/) that it's the load-bearing line in the whole discipline. If IT owns the data, no business decision about it ever sticks, because the custodian can't overrule the function that generated it.

I keep watching the agent industry try to erase that line.

Almost everything we build to make autonomous agents trustworthy is an attempt to promote a custodian into an owner. Better models, so the output needs less checking. Self-review, so the agent grades its own work. Confidence scores, so it can tell you when to believe it. Even the guard pipelines, [the kind I spent a month building](/posts/the-stack-nobody-talks-about/), belong to this family: layers of machinery whose unstated goal is to let the agent's output stand on its own with no human behind it.

It won't, and not because the machinery is weak. Because ownership isn't a property you can build into a tool.

An owner is the answer to one question: when this is wrong, whose name is on it? That question has a human-shaped hole in it. Not because humans are more accurate than agents, because often we aren't, but because accountability is a relationship between a decision and a person who can be held to it. You can make an agent more accurate. You cannot make it accountable, because there is nothing to hold. It has no career to risk, no license to lose, no signature that means anything once the shipment stops.

<mark>You can make a custodian arbitrarily reliable and it still won't be an owner, because the gap between them isn't competence, it's liability.</mark>

That's why "trust the agent" is a category error. It points the engineering at the one property a custodian definitionally lacks, and then acts surprised when no amount of model quality closes the gap.

The regulated world figured this out the long way. [21 CFR Part 11](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11) is built on the electronic signature, and the signature exists to bind a record to a person who is accountable for it. The audit trail is just the proof the binding held. [I noticed recently](/posts/agent-world-reinventing-part-11/) that agent governance has quietly rebuilt almost all of Part 11 without learning its name. What it can't rebuild is the signer. The custodian is doing the work and there's no owner in the room.

So the problem most teams are solving is the wrong one. The question isn't how to make the agent trustworthy enough to ship without a human. It's how to keep a human owner attached to output that arrives faster than any human can read it.

Those are different problems with different answers. The first is a model problem, and it's the one drawing the funding, because it promises to remove the human, and the human is the slow, expensive, unscalable part. The second is a governance problem, and it's the one that actually has to be solved, because the human is the only part that can be accountable. Spending on the first to avoid the second is how you end up with a system that produces beautiful, well-tested, fully-audited output that nobody will put their name on.

The shape of an answer is already visible, and it isn't a smarter agent. It's the owner/custodian split, ported across. The agent is the custodian: it executes, it logs, it stays in its lane. The human who authorized the work is the owner, and the system's only real job is to keep that authorization bound to what actually shipped, even when the agent took twenty steps the human never watched.

My current version of that binding is a person approving a spec, hashed to the exact diff that ran. It's a proxy for a signature, and an honest one, [as I've said](/posts/agent-world-reinventing-part-11/), right up until the chain of autonomous steps gets long enough that the spec a person signed and the output that shipped have almost nothing left in common. That's the open edge. Not making the agent better. Keeping the binding meaningful as the distance between the signature and the shipment grows.

Notice what this does to the role everyone assumes is obsolete. The job that survives the agent era isn't the one that writes the code. The agent does that now, faster than you, and the guard pipeline keeps it inside the lines. The job that survives is the owner, the person willing to put their name on output they didn't type and be wrong about it in public. We keep trying to automate that person away because they're the bottleneck. They're also the only part a regulator, a customer, or a court can address.

So when someone ships the first real agent-governance product, it won't be a more trustworthy model. It'll be the thing that keeps a named human bound to a machine's output at machine speed. And it'll look less like AI than like a signature.
