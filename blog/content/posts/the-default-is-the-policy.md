---
title: "The Default Is the Policy"
date: 2026-08-08
draft: false
tags: ["data", "platform-engineering"]
summary: "A storage platform can enforce any retention clock you hand it. What it can't do is know which clock a record is on, and the only moment that answer can enter the system is the write. So the real policy decision is a schema token: required, or defaulted?"
---

How long is the platform allowed to keep this record?

Every storage system answers that question for every record it holds, even when the answer was never chosen by anyone. Accept a write, say nothing about retention, and the record stays indefinitely, because staying is the thing durable storage promises. In a regulated shop, indefinitely is [one of the two ways to be wrong](/posts/required-to-delete-this/): some records carry a keep-floor measured in decades, others a delete-ceiling with obligations attached. When I wrote about those two clocks, the prescription was a delete-by date stamped on every record at creation, derived from what the record is and why it was collected. It didn't say where those inputs come from.

Start with who can't supply them.

The platform can't, and not for lack of machinery. S3 will [expire objects on a schedule](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) once a lifecycle rule names the day count, and [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) will refuse every delete until a retain-until date passes. Floor and ceiling, both commodity enforcement. What the platform is missing is the input. Retention hangs on why a record was collected, and bytes don't carry a why. [Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) will scan a bucket and tell you which objects contain personal data, which is worth knowing and still answers a different question. The same assay result can be a trial record with a decades-long floor in one workflow and disposable scratch output in another, byte for byte the same file. Content scanning tops out at what. The clock is set by why, and why belongs to [the owner, not the custodian](/posts/data-governance-that-survives-an-inspection/). A storage platform is the custodian, by construction.

Time doesn't help either. A record's purpose is present in the system at exactly one point: the write, when the workflow producing the record is the code making the call. If the write doesn't capture it, no system holds it afterward, and reconstructing it later means inferring purpose from content and location. Content, see above, can't carry it.

So the storage platform I've been [extracting at work](/posts/your-app-is-wearing-a-platforms-clothes/) needs a retention class on its write path, and the governance question compresses into one schema decision: `NOT NULL`, or `DEFAULT`.

Defaulted is the polite build. Consumers onboard without friction, callers written before the field existed keep working, and the platform team gets thanked for keeping the change invisible. The bill is the meaning of that clause. From the first write onward, the default is the operating retention policy for every record whose producing team never engaged the question. It was decided by whoever wrote the migration and reviewed by whoever approved the pull request. It appears in no retention schedule, because a `DEFAULT` clause doesn't look like policy, it looks like hygiene. The binder governs the records somebody thought about. The default governs the rest.

Required is the rude build. Writes without a class bounce, and teams learn their integration is blocked on a field they don't know how to fill in. Watch what that bounce produces, though. A team that knows its records' purpose types one value and never thinks about it again. A team that can't fill the field has surfaced one of two facts: either a retention decision exists somewhere and never reached the people writing against the API, or it was never made at all. Both are findings. The 400 didn't create the gap, it caught it, while the code that knows the record's purpose is still open in an editor and the team that owns the workflow is still staffed. The refusals even arrive in priority order, because record types being written today bounce today.

Data contracts already have a slot for this. The [Data Contract Specification](https://datacontract-specification.com/) carries a retention section stating how long data will be available, and where a producing team has an answer, writing it there is exactly right. A slot is not a gate, though. The contract records answers that exist. It has nothing to say about the write that shows up with the question unanswered, and every record this post worries about arrives exactly that way.

The pressure, when it comes, will point one direction. Consuming teams will ask the platform to pick a safe value for them, which is the custodian being asked to write policy on the owner's behalf. Adoption numbers will make the required field look like the obstacle. And relaxing it is a one-line migration that ships in an afternoon, while defending it is an argument that has to be won over and over.

Retention is the version of this I'm standing in, not the end of it. Residency is the same shape. So is sensitivity classification. Per-record questions the platform can enforce but can't answer will keep arriving dressed as API details, and each one ends up as either a required field or a default. The field starts the argument while the answer can still be found. The default postpones it until the people who had the answer are gone.
