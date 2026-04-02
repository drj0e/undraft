---
title: "Your App Is Wearing a Platform's Clothes"
date: 2026-04-02
draft: true
tags: ["architecture", "platform-engineering"]
summary: "You built an app. It worked. Then a second team showed up and couldn't use it without inheriting every opinion you baked in. Congratulations, there's a platform hiding inside your application."
---

I work on a storage application. It stores files, manages metadata, enforces validation rules, runs approval workflows. It works. It's been working for a while.

Then a second team wanted to use it.

They didn't want the approval workflows. They didn't need the validation rules. They didn't care about the metadata schema we'd built around our specific use case. They just wanted to store files and get them back. But they couldn't, because all of that application logic is woven into the storage layer. You can't take the storage without taking the opinions.

That's when I realized: this isn't an app with a storage feature. It's a platform wearing an app's clothes.

Martin Fowler wrote about this in 2003. He called it a [Harvested Platform](https://martinfowler.com/bliki/HarvestedFramework.html). You build an app. A second app shows up with overlapping needs. The shared parts get extracted into a platform. He contrasts this with a Foundation Platform, building the platform first, and says the harvested approach "seems to work better in practice." You can't know what the platform should look like until at least two consumers have proven what they actually need. Before that, you're guessing. After that, you're harvesting.

Evan Bottcher has the [litmus test](https://martinfowler.com/articles/talk-about-platforms.html): can your consumers self-serve without inheriting opinions they didn't ask for? If not, you don't have a platform. You have an app that other people are forced to pretend is one.

Building the app as an app was the right call. The platform was invisible until the second consumer made it visible. That's not a failure. The unhealthy path is trying to design the platform before anyone needs it.

So now I'm finding the seams. We've spent the last few weeks on this. Talking to teams who already consume the system, asking them where it hurt. What did you have to adopt that you didn't want? What would you have built differently if you could have started from the storage layer alone? Where did the app's opinions force you into workarounds?

The answers show up everywhere. In the API structure, where endpoints assume a specific workflow. In the data model, where fields exist for one team's regulatory requirements but get inherited by everyone. In the metadata schemas that encode one group's organizational hierarchy as if it were universal truth.

Platform is the boring stuff. Store bytes. Attach metadata. Retrieve by query. Capabilities any consumer would want, with no opinions about what the bytes mean or what the metadata represents.

App is the rest. This file needs three approvals before it's visible. This metadata field is required for compliance. This naming convention reflects one team's org chart. Good opinions, necessary for the original use case. But opinions a second consumer shouldn't have to adopt.

Team Topologies calls the design target a [Thinnest Viable Platform](https://teamtopologies.com/key-concepts-content/what-is-a-thinnest-viable-platform-tvp): the smallest set of APIs and tools required to let consuming teams self-serve. Not the thickest thing you can imagine someone eventually needing. The thinnest thing that unblocks real consumers today.

I don't have the ending to this story yet. I'm still bucketing, still sitting with teams who can tell me exactly which opinions they were forced to inherit and which ones they actually needed. But the reframe itself changed how we work. The moment I stopped asking "what should we refactor?" and started asking "what would a second consumer need if they'd never seen our workflows?" the decisions got easier. Some things we thought were platform turned out to be one team's opinion dressed up as infrastructure. Some things we thought were app logic turned out to be the only reason the storage layer was usable at all.

You don't find the lines by staring at the code. You find them by asking the people who hit the walls.
