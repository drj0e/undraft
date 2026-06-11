---
title: "Two Consumers Don't Make a Platform"
date: 2026-06-11
draft: false
tags: ["architecture", "platform-engineering"]
summary: "I argued the way to find a platform's real boundary was to watch the second team that wanted in. The catch I keep running into: two consumers tell you what they have in common, and that's not the same thing as what the platform is."
---

A while back I argued that [our storage app was a platform wearing an app's clothes](/posts/your-app-is-wearing-a-platforms-clothes/), and that the way to find the real boundary was to wait for a second team that wanted in and watch where they pushed back. I still think that's the right move. I've also started to distrust it, and the reason is subtle enough to be worth naming before you build on it.

The second consumer doesn't tell you what your platform is. It tells you what your first two consumers don't have in common. Those sound like the same fact. They aren't, and the gap between them is where a harvested platform quietly goes wrong.

Martin Fowler's [Harvested Platform](https://martinfowler.com/bliki/HarvestedFramework.html) is still the right instinct. You don't design the platform up front. You build the app, wait until a second app shows up with overlapping needs, and extract the shared part. He says that beats guessing in advance, and I think he's right. The trouble is what "extract the shared part" smuggles in.

Two consumers give you exactly one comparison. Anything both need reads as platform. Anything only one needs reads as app. The classifier feels principled right up until you notice it runs on a sample size of two.

<mark>A sample of two can't tell the difference between a requirement and a coincidence.</mark>

Two teams might both want the same thing for reasons that won't generalize past them. Or both might happen not to need a capability a third team would treat as non-negotiable, so you file that capability under app logic, strip it out, and hand the third consumer the job of rebuilding it. The intersection of two use cases is not the shape of the platform. It only looks like it while two is all you have.

The pain shows up in predictable places. Endpoints that assume a workflow sequence one team has and another doesn't. Fields in the data model that exist for someone else's compliance requirement. Metadata that encodes a file-naming convention only the first team follows. None of that is hard to spot by category. What's hard is saying, case by case, whether a given thing is the platform's to keep or the first app's to shed.

This is the trap sitting underneath the [Thinnest Viable Platform](https://teamtopologies.com/key-concepts-content/what-is-a-thinnest-viable-platform-tvp). Thin is the right goal. But thin measured against two consumers can cut muscle and call it fat.

Some of the opinions baked into a storage layer look like application logic and are the only reason the storage is safe to use at all. Access control. Lifecycle. The validation that protects the bytes instead of one team's naming convention. If neither of the first two consumers leans on one of those, the two-consumer classifier says it's app logic and should go. It would be wrong, and you wouldn't find out until a team that needed it showed up and couldn't self-serve.

Evan Bottcher's [litmus test](https://martinfowler.com/articles/talk-about-platforms.html), whether a consumer can self-serve without inheriting opinions they didn't ask for, tells you when you've failed. It doesn't tell you which opinions to keep. It's a test, not a map.

You can't wait for the third consumer, because the second one needs an answer now and waiting isn't free. And you can't generalize honestly from two. What's left is less satisfying than a rule and more honest than pretending two is enough. Extract the intersection. Then add back the capabilities that are structurally load-bearing even when only one consumer currently names them, because the cost of wrongly cutting access control is nothing like the cost of wrongly keeping it. Then treat the boundary itself as provisional and version it, so moving the line later is an announced change instead of a break the next consumer absorbs in silence. It's the same discipline I argued for at the [data seam](/posts/how-many-samples-do-we-have/), pointed at a different seam.

Harvesting is never one event, and that's what gets lost when people repeat Fowler's rule like a finish line. The first consumer shapes the app. The second reshapes it into a platform. A third will reshape it again. The only part you actually control is whether your current guesses are written down somewhere the next team can push on them, or buried deep enough that the next team inherits them in silence.

So the move isn't to design the platform. It's to propose one, on the evidence of two teams, and say provisional out loud, so the third team arrives at a boundary it can move instead of a wall it has to live behind.
