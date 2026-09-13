---
title: "Sunset Dates Are for Strangers"
date: 2026-09-14
draft: false
tags: ["platform-engineering", "leadership"]
summary: "A vendor deprecates by announcing a date because it can't see its callers. An internal platform can read every caller and open a pull request against it, and most platform teams copy the vendor's playbook anyway. The part of the migration that lever can't cover is the consumer's sign-off."
reviewed: true
---

Go through your platform's consumers one at a time and check a single permission on each repo: can the platform team open a pull request there?

That answer says more about your next deprecation than anything in the deprecation notice.

I wrote in July that an internal platform [can't send the 410](/posts/the-410-you-cant-send/), and that the date slips because the only enforcement available is a peer asking a peer. I still think that's right. I also framed it around the wrong lever. A vendor sunsets by announcement because announcement is all a vendor has. Every integration against a public API lives in a repository the vendor will never read, on a deploy schedule it will never learn, owned by a team it will never meet. A header with a date in it is the only instrument that reaches all of them at once.

Your callers are in the building. They're on the same code host, and the platform team can search for every call to the old surface and have the count by lunch. So the lever an internal platform holds is one no vendor gets to hold: it can write the migration itself.

Google made that a rule in 2012. Under the Churn Rule, ["infrastructure teams must do the work to move their internal users to new versions themselves or do the update in place, in backward-compatible fashion."](https://abseil.io/resources/swe-book/html/ch01.html) The large-scale changes chapter of the same book says why: nobody likes unfunded mandates, and ["centralizing the migration and accounting for its costs is almost always faster and cheaper than depending on individual teams to organically migrate."](https://abseil.io/resources/swe-book/html/ch22.html) Their tool for it, Rosie, takes one sweeping change, shards it along project and ownership boundaries, and pushes each shard through its own test, review, and submit. At the peak of the move from `scoped_ptr` to `std::unique_ptr`, that machinery was landing more than 700 independent changes a day, touching more than 15,000 files.

Put the two playbooks next to each other. The vendor's: we announce, you migrate, and on the date you're on your own. Google's: we migrate you. These aren't two philosophies. They're one obligation, solved with whatever lever the party holding it could reach. A vendor holds a date. An internal platform holds write access.

Then the internal team sits down and writes a deprecation notice anyway. Migration guide, a date, a reminder, a slipped date. The posture was borrowed from parties who had no other option, by a team that does.

The objection arrives immediately: we don't have a monorepo. The tooling for that case already exists. Sourcegraph's [Batch Changes](https://sourcegraph.com/docs/batch-changes) ships a change across many repositories and code hosts, opening a pull request on each and tracking them until they merge. The mechanism was never the scarce part. What Google's rule assumes is three grants, and only the first of them is technical.

Visibility. The platform team can read every consumer, which at Google comes from a monorepo where every engineer sees almost all of the code, and elsewhere comes from an org-wide read on the code host.

Write. The platform team can push a branch and open a pull request against a consumer's repo. This is a permission that gets granted only after somebody asks for it, and it is the difference between a deprecation you announce and one you perform.

Approval. Somebody on the consumer's side has to accept the change. Google shrank this step for mechanical work: global reviewers with pattern-based tooling look over the shards and approve the ones that match what they expect, so the owning teams aren't each asked to re-learn the same mechanical edit.

That third one is where the rule stops porting to the shop I work in. A validated consumer's system is [its own priced object](/posts/the-diff-never-had-a-price/), and a change to it is the consumer's change no matter whose keyboard produced the diff. The platform team can write it, test it, and open it. It cannot assess the impact, sign it, or release it, because an inspector asks the owner of the system and the platform team isn't that. So the migration lands in the consumer's change queue instead of their backlog. Still a long way from where the vendor's model leaves you. The consumer's share of the work shrinks from doing the migration to reviewing and releasing one somebody else wrote, and that second job is a fraction of the first.

It also changes what the extraction estimate should say. The question I posed in July was whether you could ever turn a surface off. The number that belongs next to it is how many consumers' change-control cycles a platform migration enters, and whether the platform team is staffed to author the diff for every one of them. Deprecation moves from a request in a consumer's backlog to a line on the platform team's roadmap, with a cost you can put in a planning doc, which the announcement model never produced.

A merged pull request isn't a deployed one. The old surface stays up until the last consumer ships, and their release cadence is theirs. What changes is where you wait: on a branch that's already merged and sitting in somebody's release train, instead of on a ticket that has been re-prioritized out of three consecutive quarters.

The sunset header was written for callers the vendor would never meet. Yours have a repo you can clone.
