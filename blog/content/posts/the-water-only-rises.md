---
title: "The Water Only Rises"
date: 2026-09-01
draft: false
tags: ["platform-engineering", "compliance", "architecture"]
summary: "A shared platform ends up at the strictest requirement any of its consumers carries, and onboarding is when that gets decided. Vendors fence off the strict part. An internal platform team usually can't, and the mark only ever moves up."
---

Nothing about a shared platform averages.

Put two consumers on one surface and every property that matters resolves to the stricter of the two. Availability is the tighter target, because the platform being down is the platform being down. Retention is the longer floor. Change control is whichever process the more regulated consumer has to follow, applied to the code both of them sit on. There is no build of the platform that runs strict for one caller and loose for the other, because the part they share is the part underneath both.

Federal security categorization states this as a rule. FIPS 199 says the impact values assigned to an information system "shall be the highest values (i.e., high water mark) from among those security categories that have been determined for each type of information resident on the information system." One system, many kinds of information, and the categorization is the maximum across all of them. A low-impact information type never pulls the number back down. ([NIST](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.199.pdf))

Which is a fine rule when you know what sits on the system. A platform's answer to that question gets rewritten every time somebody onboards.

That reframes what extraction does. The pitch counts the duplication you stop paying for: one storage layer instead of four, one access model, one audit trail. What moves the other way is the share of your codebase governed by your strictest consumer. Code living inside one application answers to that application's users. The same code living in a shared core answers to the toughest rulebook in the set, and extraction is the move that relocates it. Consolidation and scope growth are one event seen from two sides.

Back when I noticed the [storage app was really a platform](/posts/your-app-is-wearing-a-platforms-clothes/), the second team wanted get and put and nothing else. Serve them get and put out of a core that a GxP consumer also depends on and the API stays as small as they asked for, while every change to it now moves at the speed of an impact assessment. They inherited nothing from the first app's workflow. They inherited its regulator.

The [coordination cost](/posts/the-platform-tax/) I've written about before is a negotiation with the other teams, and negotiations have give in them. A regulatory scope attaches to the code rather than to the relationship. There is no version where everyone agrees to be reasonable and it relaxes.

Vendors deal with this by fencing. AWS signs a business associate agreement that covers a published list of HIPAA-eligible services, and a service off that list can't touch protected health information even with the agreement in place. ([AWS](https://aws.amazon.com/compliance/hipaa-eligible-services-reference)) Read that as an engineering decision rather than a legal one and it's a company sorting its own surface area into the part that stands inside the strict regime and the part that is kept clear of it.

The fence is real work, and one standard is blunt about how much. PCI DSS lets you shrink the cardholder data environment by segmenting it, then makes you prove the segmentation with penetration testing at least every twelve months and after any change to the controls. Service providers get a shorter clock, six months, because one failed boundary at a shared provider exposes many customers at once. ([Strobes, on PCI DSS v4.0.1 requirements 11.4.5 and 11.4.6](https://strobes.co/blog/pci-dss-penetration-testing-requirements/)) Scope reduction is available. It's available as a recurring proof obligation, and the party serving everybody pays for it twice as often.

You can build that fence internally. It costs two deployments, two pipelines, two rotations, and a standing rule about which data is allowed where, funded out of a budget you justified by consolidating things.

The part that makes the internal version harder than the vendor's is direction. AWS can leave a service off the eligible list, and the customer who needs it goes elsewhere for that one workload. A platform team's regulated consumer is usually the team holding the mandate, the audit exposure, and the money, which makes them the caller you can least afford to turn away. And once they're on, the instrument for removing them is the same social enforcement that already makes [internal deprecation](/posts/the-410-you-cant-send/) go nowhere. The mark goes up on a Tuesday and stays there for the life of the platform.

So the question to settle before consumer N onboards is not whether the platform can serve their use case. It's which of their obligations become everyone's, whether you could ever get back down if you were wrong, and what the answer does to the change cost for the consumers already on the platform, who are not in the meeting.

The consumer that sets your high-water mark arrives as an ordinary integration request. Whoever approves it is picking the change process for every team that shows up after, including the ones that haven't been staffed yet.
