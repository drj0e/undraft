---
title: "The Platform Tax Lands on the Team That Built It"
date: 2026-06-28
draft: true
tags: ["architecture", "platform-engineering"]
summary: "The moment you harvest a platform out of an app, the app stops being something you can change quietly. That standing cost lands hardest on the team that built it, and most extraction plans never budget for it."
reviewed: true
---

Pulling a platform out of an app doesn't set the app free. It puts the app on a leash, and hands the other end to everyone who shows up next.

I've been [doing exactly that](/posts/your-app-is-wearing-a-platforms-clothes/) to a storage system at work: finding the seams, deciding which opinions belong to the platform and which belong to the first app that grew on top of it. Most of the writing about this treats it as an architecture problem. Draw the boundary, extract the shared parts, publish an interface. The before and after diagrams look almost identical. A box that used to sit inside another box now sits beside it.

What the diagrams don't show is what changed about your day.

Before the extraction, the storage internals belonged to my team. A field that needed renaming, a status enum that needed a new value, a validation rule that was too strict for a case we hadn't seen yet, all of it was a local edit. You change it, you ship it, you mention it in standup. The decision was private because the blast radius was private.

The moment a second consumer depends on that surface, the same edit is a contract change. [I argued before](/posts/two-consumers-dont-make-a-platform/) that the boundary should be provisional and versioned, so the next consumer can push on it instead of inheriting it in silence. That's still right. But versioning isn't free. It's the machinery that turns a thing you used to change in an afternoon into a thing you announce, deprecate, and migrate.

<mark>You don't pay for a platform in the extraction. You pay for it every time you can no longer change something quietly.</mark>

And the part that caught me off guard: your own first app is now one of the consumers. Usually the most demanding one, because it has more invested in the old shape than anyone. It grew up assuming it could reach straight into those internals. Now it has to ask. You spend the extraction work convincing yourself you're serving some future second team, and then notice the consumer you've inconvenienced most is yourself, six months ago.

This is why "should we extract a platform?" is the wrong first question. It gets filed as an architecture decision. It's a velocity decision. You're proposing to trade the first app's speed for the second app's existence, and sometimes that trade is obviously worth making. But teams rarely price it, because the extraction lands on a roadmap as a refactor with an end date, while the actual cost has no end date. Every future change to the shared surface carries coordination it didn't carry before, and it carries it for good.

That cost falls hardest on the people who used to be fastest. The team that built the storage layer knew it cold and could change it in their sleep. Extraction takes that fluency and converts it into process. Nobody writes that on the plan, because it doesn't look like work. It looks like the absence of work you used to do without thinking about it.

I'm not arguing against harvesting. The platform is real, the second consumer is real, and pretending otherwise doesn't make the storage layer any easier to reuse. I'm arguing that the honest pitch includes the bill. Not "we'll extract the shared parts and everyone self-serves." Closer to: we'll extract the shared parts, and from then on the team that moved fastest through this code moves at the speed of everyone who leans on it.

The teams that regret harvesting usually aren't the ones who drew the boundary in the wrong place. They're the ones who never noticed they'd hired themselves a customer.
