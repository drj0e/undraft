---
title: "Two Consumers Don't Make a Platform"
date: 2026-06-10
draft: true
tags: ["architecture", "platform-engineering"]
summary: "I said a platform was hiding inside our storage app and I'd find the boundary by talking to the second team that needed it. Two months later that team has shown me every assumption we baked in, and I understand the line less cleanly than when I started."
---

A couple of months ago I [wrote that our storage app was a platform wearing an app's clothes](/posts/your-app-is-wearing-a-platforms-clothes/), and said I'd find the real boundary by talking to the second team that wanted in. I've done that. They were generous with their time and exact about where it hurt, and they pointed at every opinion we'd welded into the storage layer that they'd had to work around.

I came out of those conversations understanding the problem less cleanly than I went into them.

The second consumer doesn't tell you what your platform is. It tells you what your first two consumers don't have in common. Those sound like the same fact. They aren't, and the space between them is where a harvested platform quietly goes wrong.

The pain landed in the categories the [last post expected](/posts/your-app-is-wearing-a-platforms-clothes/): endpoints that assume a workflow sequence their use case doesn't have, fields in the data model that exist for someone else's compliance requirement, metadata that encodes a file-naming convention they don't follow. None of that surprised me by category. What surprised me was how hard it was, case by case, to say whether a given thing was ours to keep or theirs to be rid of.

Martin Fowler's [Harvested Platform](https://martinfowler.com/bliki/HarvestedFramework.html) is still the right instinct. You don't design the platform up front. You build the app, wait until a second app shows up with overlapping needs, and extract the shared part. He says that beats guessing in advance, and I think he's right. The trouble is what "extract the shared part" smuggles in.

Two consumers give you exactly one comparison. Anything both teams need reads as platform. Anything only one team needs reads as app. The classifier feels principled right until you notice it runs on a sample size of two.

<mark>A sample of two can't tell the difference between a requirement and a coincidence.</mark>

Two teams might both want the same thing for reasons that won't generalize past them. Or both might happen not to need a capability a third team would treat as non-negotiable, so you file that capability under app logic, strip it out, and hand the third consumer the job of rebuilding it. The intersection of two use cases is not the shape of the platform. It only looks like it while two is all you have.

This is the trap sitting underneath the [Thinnest Viable Platform](https://teamtopologies.com/key-concepts-content/what-is-a-thinnest-viable-platform-tvp). Thin is the right goal. But thin measured against two consumers can cut muscle and call it fat.

Some of the opinions in our storage layer look like application logic and are the only reason the storage is safe to use at all. Access control. Lifecycle. The validation that protects the bytes instead of one team's naming convention. If neither of my first two consumers leans on one of those, the two-consumer classifier will tell me it's app logic and should go. It would be wrong, and I wouldn't learn that until a team that needed it showed up and couldn't self-serve.

[JOE: what's one assumption the second team exposed where you genuinely couldn't tell, in the moment, whether it was platform or app?]

I can't wait for the third consumer, because the second one is blocked now and waiting isn't free. And I can't generalize honestly from two. Evan Bottcher's [litmus test](https://martinfowler.com/articles/talk-about-platforms.html), whether a consumer can self-serve without inheriting opinions they didn't ask for, tells me when I've failed. It doesn't tell me which opinions to keep. It's a test, not a map.

So what I'm landing on is less satisfying than a rule and more honest than pretending two is enough. Extract the intersection. Then add back the capabilities that are structurally load-bearing even when only one consumer currently names them, because the cost of wrongly cutting access control is nothing like the cost of wrongly keeping it. Then treat the boundary itself as provisional and version it, so moving the line later is an announced change instead of a break the next consumer absorbs in silence. It's the same discipline I argued for at the [data seam](/posts/how-many-samples-do-we-have/), pointed at a different seam.

[JOE: where's your line right now, pure intersection, or intersection plus a few judgment calls you're prepared to defend?]

Harvesting is never one event, and that's what gets lost when people repeat Fowler's rule like a finish line. The first consumer shaped the app. The second is reshaping it into a platform. A third will reshape it again. The only part I actually control is whether my current guesses are written down somewhere the next team can push on them, or buried deep enough that they inherit them the way the second team inherited ours.

So I'm not designing a platform yet. I'm proposing one, on evidence from two teams, and saying provisional out loud, so the third team arrives at a boundary it can move instead of a wall it has to live behind.
