---
title: "Every Request Weighs the Same"
date: 2026-07-21
draft: false
tags: ["platform-engineering", "leadership"]
summary: "An internal platform has no price, so it can't rank the work fairly and it can't refuse anything cleanly. Every 'no' turns political, and the roadmap ends up set by whoever escalates best."
reviewed: true
---

Two teams want the same sprint. One needs a field added to the shared schema, the other needs a rate limit lifted, and both are real work that will not fit in the same two weeks. The tiebreaker is not which one is worth more. It's which lead is willing to walk into the shared VP's office and make it his problem.

That's the moment an internal platform shows what it's missing. It has no price.

A vendor ranks those two requests the boring way. Whichever one comes attached to more revenue wins, and the answer is legible to everyone in the room because the currency is shared. You have no currency. So the ranking falls to whoever can spend the most political capital, and political capital is not correlated with value. It's correlated with tenure, with proximity to the person who decides, with how much a given lead enjoys a fight.

I've written that adoption on an internal platform [isn't a vote](/posts/nobody-chose-your-platform/). This is the same missing signal doing its damage on the other side of the desk. Without a price you can't read demand, and you also can't refuse it. A vendor's "no" is cheap because it arrives with a reason nobody can argue: this doesn't pay. Your "no" has to be rebuilt from scratch every single time, because there's no shared number to point at, and "we're out of capacity" is not a reason a captive consumer accepts. They aren't paying you. From where they sit your capacity is a fixed cost their org already funded, so any "no" reads as you choosing someone else over them.

When there's no price, escalation becomes the price. It's the only mechanism left that converts one team's want into pressure the platform team has to answer. So the rational move for every consumer is to escalate earlier and louder, because the quiet, patient, technically correct request loses to the one that reached a director by Tuesday. You've trained your most important consumers to route their roadmap through your management chain, and then you wonder why the backlog reads like a list of grievances instead of a plan.

Escalation is not a price. It's what you get where the price used to be.

The platform team feels this as a roadmap it doesn't own. Every sprint is the union of whoever yelled, and there's no principled way to say "this quarter we build the thing that helps the most teams," because "most teams" and "loudest team" are different sets and only one of them has a channel straight to you. [The tax I described before](/posts/the-platform-tax/) was the cost of changing a shared surface once other people lean on it. This is a second bill on the same counter: without a way to price access, you lose the right to prioritize your own work.

The mature move is uncomfortable, and most orgs flinch at it. Manufacture a currency. Give each consuming team a fixed budget of platform capacity, or run a chargeback, or force requests to trade against a shared cap so teams have to rank their own asks before the asks ever reach you. The mechanism matters less than the property it restores. Once a request costs the asking team something, they stop sending all of them, and the ones they do send show up pre-sorted by the only party who actually knows their relative worth.

Teams hate this. Internal billing feels like bureaucracy invented to slow them down, and the complaints are loud and immediate. But the complaint is the signal that it's working. A free platform can't say no with a reason, so it says no with politics. A priced one says no with a number, and a number is the only "no" a captive consumer can't take personally.

You didn't escape the market when you built the platform internally. You stopped printing the price. The bill still comes due, in a roadmap set by whoever escalates best, and that's a worse currency than money, because at least money is worth the same to everyone spending it.
