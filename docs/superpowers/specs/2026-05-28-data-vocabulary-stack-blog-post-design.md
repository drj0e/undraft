# Blog Post Design: "How Many Samples Do We Have?"

## Overview

~1,200 word blog post written as a learning exercise: a senior technical leader stops to untangle why an org needs all of these overlapping data concepts at once (vocabulary, ontology, semantic layer, catalog, contract), where you're supposed to start, and who owns what. Structured as a reverse-rainbow arc: a reasonable-sounding ask pulls the reader down into the tangle, the diagnosis sits at the bottom, and a practical dig-out climbs back out. A single running example — "how many samples do we have?" — threads every layer.

## Thesis

These data concepts form a dependency chain you have to build bottom-up. The reason it's so hard to get them working together and keep them that way is that ownership of the chain runs straight across the tech/business seam, so no single person owns the whole thing. The buyable layers (catalog, semantic layer, contract tooling) all sit on top of the one piece you can't buy: an agreement on what the words mean. And nobody's been assigned to own that piece.

## Relationship to Prior Post

Adjacent to "The Step Between the Catalog and the Vector" (2026-04-23), which argued that vectors need a catalog/semantic foundation underneath them. That post was AI-facing and said "do the foundation first." This post is not about AI at all. It asks the harder follow-up: why does that foundation never come together and stay together, even when people try? Cross-link to the catalog/vector post as the AI-facing companion rather than overlapping it. Do NOT restate its argument.

## Title

Working title: "How Many Samples Do We Have?"

The title is the running example and the question that detonates across all five layers. Open to revision during drafting. Alternatives considered:
- "The Word Nobody Owns"
- "Five Words for One Thing"
- "What Is a Sample?"

## Tags

- `data` (existing tag)
- `architecture` (existing tag)

Drop `ai-tooling` deliberately — this post isn't AI-centric, and keeping it off lets the post stand on its own rather than reading as another AI piece.

## Audience

Primary: Technical leaders in data-heavy orgs who keep hearing "semantic layer" and "data catalog" in the same breath and aren't sure why they need both or where to start.
Secondary: Data engineers and architects who own a slice of this chain and keep watching it rot at the seams. Anyone who has tried to answer a "simple" counting question and discovered no two systems agree.

## Tone

Julia Evans learning-exercise voice: written from inside the confusion, not after mastering it. "I had to stop and work this out" is the credibility, not a war story. No scar required — the pressure signal is the moment the pile of words started feeling tangled (management wants a semantic layer, I want a catalog, why both?). Honest about not having had this cleanly sorted before sitting down to think it through. The dig-out is confident but not a corporate playbook.

## Naming Constraints

- Keep the domain example generic and industry-standard: "a LIMS," "an ELN," "freezer/sample inventory," "bench scientists," "instrument exports," "assays," "aliquots." These are common lab-informatics terms, not employer or product specifics.
- Per CLAUDE.md employer rules: no employer name, no internal project or product names, no internal org structure. "At work," "the platform I work on," "a scientific data platform" are the allowed framings if work context is needed at all. Prefer not needing it.
- The tech/business "seam" should be described by function (bench, lab ops/inventory, analytics), never by real team names or titles.

## The Running Example

"How many samples do we have?" A question that sounds like a one-line SQL query and turns out to have no single answer. It develops through the post and exposes each layer in turn:

- **Vocabulary** — what counts as a sample? The physical vial that arrived, the aliquots split off it, or the logical record? Split one tube into ten aliquots: one sample or eleven? Run one specimen through two assays: one or two? Is a consumed sample still a sample? Is a control?
- **Ontology** — sample vs specimen vs aliquot vs batch vs subject. One subject, many specimens; one specimen, many aliquots; aliquots get pooled back together. Parent/child lineage is the whole game, and the org uses these words interchangeably.
- **Semantic layer** — the report says 50,000 samples. Physical containers, logical records, or distinct specimens? Mapped against which system's tables?
- **Catalog** — sample data lives in the LIMS, the instrument exports, the ELN, and the freezer inventory. Which is the source of truth? Where did the 50,000 come from?
- **Contract** — inventory renames a status or changes what "available" means (consumed vs depleted vs archived) and the count silently shifts under everyone downstream.

Seam reveal: nobody can answer "how many samples do we have" because no one is *allowed* to decide what a sample is. The bench, lab ops, and analytics each have a number, and each is right in their own world.

## Structure (reverse-rainbow arc)

### Opening — the reasonable ask (~150 words)

Management wants a semantic layer. I want a catalog. Someone mentioned we should really have data contracts. I stopped and realized I couldn't cleanly say why we need all of these, which one comes first, or who's supposed to build them. So I tried to work it out. Land the running example early: it started with someone asking how many samples we have, and three systems giving three different numbers.

### The descent — the four questions (~500 words)

Walk the four questions in the order you actually hit them. Define each term in a line as it becomes necessary, never up front as a glossary.

1. *Why do we need all of these?* Because each answers a different question and they're not substitutes. Introduce the five terms here, each tied to the sample example (see Running Example section). This is where the reader feels the pile.
2. *Where do you start?* The reveal: the order management asks for is the reverse of the order you can build in. The semantic layer is the visible, fundable thing, so it gets asked for first — but it's an output. You can't translate a meaning you haven't agreed on. You start at vocabulary, the least glamorous end.
3. *Who defines what?* Definitions are a business act wearing a technical costume. The data team can build the semantic layer but cannot decide what a sample is. When it tries, you get four definitions and a standoff.
4. *Who owns what?* The chain crosses the seam. The bottom (meaning) belongs to the bench/business; the middle and top (catalog, semantic layer, contracts) belong to tech. No one owns the whole chain, so it never fully coheres and it rots the moment either side moves.

### The bottom — the diagnosis (~100 words)

State it plainly as its own beat: the difficulty was never technical. The chain has to be built bottom-up, but ownership runs across a seam nobody designed, so the foundation everything depends on is the one piece with no owner. This is the low point of the U.

### The dig-out — climbing back up the chain backwards (~300 words)

The work runs in the opposite direction from the funding and the org chart. Everyone points at the top; you start at the bottom. Written as prose with clear sequence, not a bullet checklist. Each step gets a real sentence or two.

1. **Name who's allowed to decide what a sample is.** Before any tool. A single accountable seat on the business/bench side. Everything downstream hangs on this.
2. **Start at vocabulary, and keep it small.** The handful of entities that actually matter (sample, specimen, aliquot, subject), not the hundred that could. Definitions agreed by the person from step 1.
3. **Write down how they relate.** The ontology, lightweight — the parent/child lineage between the few things that matter, not a formal model nobody reads.
4. **Now the buyable layers land on something.** The catalog and semantic layer stop being asked to invent meaning and start just translating it. This is where tech runs ahead and where the tools finally earn their cost.
5. **Contracts last, at the seams,** to keep the agreement from rotting when one side moves.

### Closing — past the dig-out (~100 words)

The steps are easy to list and hard to do, and the reason is that step one isn't a technical task. It's a person agreeing to be accountable for a definition. The catalog, the semantic layer, the contract tooling — those you can buy. The agreement on what a sample is, you have to earn, and it's the only piece nobody's been assigned. So the real first question was never "which semantic layer." It's "who's allowed to decide what a sample is." If you can't name that person, that's the project.

Closing line must land on accountability as the work and tools as the easy part — specific to this argument, not a generic closer. [REFINE DURING DRAFTING]

## Output Weight Check

Input from the author was conversational across several messages, but the author explicitly asked for ~1,200 words, a descriptive treatment, and a running example threaded throughout. The length is author-directed, not prompt inflation. The substance comes from a real, genuinely ambiguous domain entity that exposes all five layers without padding.

## What This Post Is NOT

- Not a glossary or a definitions reference. Terms are defined in-flow, only as needed.
- Not a restate of "The Step Between the Catalog and the Vector." That post was AI-facing and said "build the foundation first." This one asks why the foundation never coheres and shows the dig-out.
- Not a tooling comparison or a vendor evaluation.
- Not an AI post. `ai-tooling` is deliberately off the tag list.
- Not a war story. No disaster is required; the pressure signal is the tangle itself.
