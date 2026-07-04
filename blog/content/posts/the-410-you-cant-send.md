---
title: "The 410 You Can't Send"
date: 2026-07-12
draft: false
tags: ["platform-engineering", "architecture"]
summary: "A public API can force you off an old version by making the endpoint go dark on a date. An internal platform has the same compatibility burden and no way to ever pull that lever, so nothing it ships ever gets retired."
---

A public API has a way to make you leave. It sets a `Sunset` header months out with a date attached, [tells every client](https://www.rfc-editor.org/rfc/rfc8594.html) when the endpoint stops answering, and on the appointed morning the old URL returns [`410 Gone`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/410). Not an error. A verdict: this existed, we removed it on purpose, stop calling. The caller has no appeal. They migrated or they broke, and the vendor priced that outcome in before shipping the deprecation.

An internal platform has the same compatibility burden and none of that machinery.

[I've written](/posts/the-platform-tax/) that the cost of harvesting a platform is that you can no longer change the shared surface without coordination. That's the tax on adding and altering. The half I underrated is that you can't subtract either. Every version of every surface you've ever shipped stays load-bearing, because the move that retires an old one doesn't exist for you.

Look at what the 410 actually is. It isn't a technical capability. Returning a status code is trivial. It's an enforcement mechanism backed by a relationship where the vendor owes the caller nothing past the terms, and the caller's only recourse is to go find another vendor. The sunset date has teeth because the consequence is impersonal. Nobody's manager gets a message. The endpoint just goes dark, and that was allowed.

Internally you can't send that. The team still calling v1 of your API is three desks over. When you set a decommission date, the enforcement isn't a status code. It's you, telling a colleague their thing breaks in March, then absorbing every reason it can't. They're mid-quarter. The one engineer who knew that integration left in April. The migration is real work nobody funded, and the person asking for it is a peer with no authority to compel it, escalating to a shared manager who weighs your cleanup against their roadmap and picks their roadmap.

So the date slips. The old surface stays up just until they migrate, and it never comes down, because the same facts are true again next quarter. You gave away the one lever that makes deprecation stick the day you made yourself reachable, and reachable is the entire promise of an internal platform.

What you end up with isn't versions. It's sediment. A public API keeps maybe two or three live versions because it can bury the rest. Yours keeps all of them, each one a shim you write around and test against and can never point at and call gone, on purpose, as of this date.

The question to answer before you extract isn't whether you can support the surface. It's whether you could ever turn one off. Inside a company the answer is usually no, which means every interface you publish is permanent from the moment it ships. Design the first one like you'll be feeding it long after everyone who asked for it has left the building.
