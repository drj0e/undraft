# Blog Post Design: "Your App Is Wearing a Platform's Clothes"

## Overview

~1,000 word blog post about the pattern of discovering a platform hiding inside an application. Grounded in the author's current experience working on a storage application that has business workflow and metadata schemas baked into it, making it impossible for new consumers to use the storage layer without inheriting app-specific opinions.

## Thesis

Every sufficiently successful internal app eventually reveals a platform hiding inside it, and you only find out when a second consumer shows up and can't use the thing without inheriting all your opinions.

## Title

"Your App Is Wearing a Platform's Clothes"

## Tags

- `architecture` (existing tag)
- `platform-engineering` (new tag, expected reuse in future posts)

## Audience

Technical peers. People who might recognize this pattern in their own work.

## Tone

Personal experience as the anchor. References to established patterns woven in, not as literature review but as "here's what this is actually called." The author is in the middle of this, not writing a retrospective. Honest about not having all the answers yet.

## Structure

### Opening (~150 words)
Start with the concrete situation. Working on a storage application. It works fine for its original consumers. Then a second team wants to use it and can't, because consuming the storage means taking the approval workflows, the validation rules, the metadata schemas. The storage system isn't a storage system. It's an application that happens to store things, and now someone needs just the storage part.

No broad context-setting. No "in today's world of microservices." Start with the problem.

### The Pattern (~250 words)
Fowler named this in 2003: Harvested Platform. The idea is that platforms shouldn't be designed upfront (Foundation Platform). They should be extracted from working apps once a second consumer proves the need. The author's situation is textbook.

Reference Evan Bottcher's litmus test: if consumers can't self-serve without inheriting opinions they don't need, it's not a platform yet.

Key point: this isn't a failure. The app was right to be built as an app. The platform only becomes visible when someone else needs part of what you built. Fowler's whole argument is that this is the healthy path.

### Finding the Seams (~300 words)
The hard part isn't deciding to extract. It's deciding where to cut.

What's platform:
- Store bytes
- Attach metadata
- Retrieve by query

What's app:
- This file needs three approvals before it's visible
- This metadata field is required for regulatory reasons
- This naming convention reflects one team's mental model

Reference Team Topologies' Thinnest Viable Platform (TVP) as the design constraint: extract the thinnest thing that lets consumers self-serve. Not the thickest thing you can imagine someone needing.

The seam concept (Feathers, via Newman): a portion of code that can be treated in isolation. The seam here is the boundary between "store/retrieve data with metadata" and "enforce workflow rules on that data."

### The Trap (~200 words)
The inner platform effect is the risk on the other side. Once you start extracting, the temptation is to make the platform layer handle everything. That's how you end up building a worse version of the thing you're already running on.

The antidote is real consumers with real needs, not hypothetical ones.

Reference Larson's counterpoint: don't decompose unless the consumers genuinely have different non-functional requirements. Partial migrations are organizational debt.

### Closing (~100 words)
The author is still in the middle of this. The platform was always there. Nobody planned it. The second consumer just made it visible.

Specific forward-looking line about what the author is learning about where to draw the lines. Must go somewhere the opening didn't. No summary, no restatement, no generic closer.

## Key References (to cite in post)

- Martin Fowler, "Harvested Platform" (2003) - the pattern name
- Evan Bottcher, "What I Talk About When I Talk About Platforms" (martinfowler.com) - platform definition/litmus test
- Team Topologies, "Thinnest Viable Platform" - design constraint for extraction
- Will Larson, "Should we decompose our monolith?" (2024) - the counterpoint

## Secondary References (available if needed, don't force)

- Michael Feathers, *Working Effectively with Legacy Code* - seam concept
- Sam Newman, *Monolith to Microservices* - seam identification techniques
- Inner Platform Effect (Wikipedia/The Daily WTF) - the over-extraction anti-pattern

## Constraints

- ~1,000 words (lean, let the ideas carry the weight)
- Genericize all work references per employer rules (no company name, no product name, no internal project names)
- Follow all voice rules from CLAUDE.md (kill list, tone, formatting)
- 2 tags only
- Include summary field in front matter for SEO/social preview
- Flag any unattributed statistics with [SOURCE NEEDED]
- Personal experience is the authority, references support, not the other way around
