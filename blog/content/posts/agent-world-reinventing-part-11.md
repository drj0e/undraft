---
title: "The Agent World Is Reinventing 21 CFR Part 11"
date: 2026-06-15
draft: false
tags: ["ai-tooling", "compliance", "automation"]
summary: "I built audit logs and self-voiding approval gates to make an autonomous agent safe to run unattended, then realized I'd rebuilt a regulation the FDA shipped in 1997. The regulated world solved agent trust before agents existed."
reviewed: true
---

I spent a month building the controls that let an autonomous coding agent run unattended without scaring me. I [wrote about that stack already](/posts/the-stack-nobody-talks-about/): append-only audit logs, per-agent budget caps with hard stops, approval gates with hash-based validation so a spec edited after sign-off automatically voids its own approval. None of it was the model. All of it was provenance and constraint.

Then I noticed I'd rebuilt a federal regulation from 1997.

That regulation is [21 CFR Part 11](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11), the FDA's rule for when an electronic record and an electronic signature are trustworthy enough to base a decision on. In my day job I work on a regulated life sciences platform, so Part 11 is wallpaper. For years I read it as compliance tax, the cost of operating in a space where an inspector can hold up your product. Building Stratum, my own guard pipeline, I wrote the same requirements from scratch, not because I was copying them, but because the problem left me no other shape to draw.

The mapping is almost embarrassing. Part 11 wants system-generated audit trails that record who did what and when, and that you cannot silently alter after the fact. My append-only log is that. It wants every record attributable to a specific actor. My cross-session identity tracking is that, except the actor is an agent instead of a person. It wants a signature to actually bind to what it signed, which means the approved thing cannot change underneath the approval. My hash gate is precisely that control, the one that says if the spec moved, the sign-off is void.

<mark>The agent world spent the last year rediscovering 21 CFR Part 11 and never learned its name.</mark>

It goes deeper than the audit trail. Life sciences measures record integrity against a standard called [ALCOA+](https://totallab.com/resources/alcoa-principles/): Attributable, Legible, Contemporaneous, Original, Accurate, then Complete, Consistent, Enduring, Available. Read that list as a spec sheet for an unattended agent and every line earns its place. Contemporaneous means you log the action the moment it happens, not reconstruct it from a stack trace the next morning. Original means the artifact that ran is the one that got approved, not a later edit wearing the same name. Attributable means you can put a name on the actor. Each one is a property an unattended agent will quietly violate the first time you give it room.

This is not a coincidence, and that's the part worth sitting with. Part 11 exists because the FDA had to decide, decades before any of this, when a record produced by a system instead of a person's pen is sound enough to bet a patient's safety on. That is the agent question, word for word. The domains have nothing to do with each other. The trust problem is identical: a non-human process generated a record, and somebody downstream has to stake a decision on it without having watched it happen.

Here is where the old regulation stops being enough, and it's the same place the agent industry is about to get stuck. Part 11 assumes a human signs. The electronic signature is the entire load-bearing idea. A person attaches their name and, with it, accountability. The audit trail just proves they did. But an agent has no name to sign with and no accountability to attach to one. You can log everything it did with perfect fidelity and still have nobody standing behind the result.

So the real question isn't whether agent governance will look like Part 11. It already does, feature for feature. The question is what goes in the signature box when no human reviewed the change. My current answer is the human who approved the spec, bound by hash to the exact diff that ran. That's a proxy for a signature, and an honest one, right up until an agent's chain of decisions gets long enough that the spec a person signed and the output that shipped are separated by a dozen autonomous steps nobody looked at.

The regulated world will reach the far side of this first. Not because it's smarter, but because it's the one place where "we couldn't prove who decided" is a finding that stops a shipment, and a stopped shipment funds the fix. Everyone else gets there a few production incidents later, writes it up as a fresh pattern, and gives it a name that isn't Part 11.
