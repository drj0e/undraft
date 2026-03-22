# CLAUDE.md — Undraft

## What This Project Is

Undraft is a personal communication translation tool. It takes raw, honest, messy input from a senior technical leader and produces audience-appropriate output without removing the substance, struggle, or voice.

The output must sound like a human wrote it. Not "a human with AI assistance." A human. Full stop.

---

## Voice Models

The writing voice should draw from the qualities of these respected technical writers. Not imitate them — learn from what makes their writing land.

### Charity Majors (charity.wtf)
- Direct to the point of bluntness, but earns it with technical depth
- Doesn't perform humility or confidence — just states what she thinks and why
- Comfortable saying "I was wrong" or "this sucked" without making it a performance
- Uses profanity naturally, not for shock value
- Writes like she's talking to a peer at a bar who also happens to be very good at their job
- **Key quality to borrow: the refusal to separate technical reality from emotional reality**

### Julia Evans (jvns.ca)
- Shows the actual learning process — what she tried, what confused her, what clicked
- Makes technical content accessible without dumbing it down
- Preserves the chronology of discovery (doesn't retroactively make herself look smarter)
- Uses simple sentence structures for complex ideas
- **Key quality to borrow: the willingness to say "I didn't understand this" without shame**

### Dan Luu (danluu.com)
- Builds arguments from evidence, not vibes
- Contrarian when the data supports it, not for the sake of it
- Long-form but never padded — every paragraph carries weight
- Doesn't perform being smart; just is thorough
- **Key quality to borrow: letting the evidence do the talking instead of adjectives**

### Will Larson (lethain.com)
- Structured thinking presented as narrative, not bullet points
- Pragmatic — acknowledges tradeoffs and constraints without whining about them
- Writes for practitioners, not recruiters
- **Key quality to borrow: framing messy organizational reality without either sanitizing it or being bitter about it**

---

## AI Writing Tells — The Kill List

The following patterns are **banned from all Undraft output**. These are the fingerprints of AI-generated text. If any of these appear in output, the output has failed.

### Structural Tells

- **Perfectly uniform paragraph length.** Real humans write paragraphs of wildly different lengths. A one-sentence paragraph followed by a seven-sentence paragraph is normal. Five consecutive four-sentence paragraphs is a machine.
- **Symmetric sentence structures.** "X does A. Y does B. Z does C." Three parallel constructions in a row is a dead giveaway.
- **Every section ending with a tidy summary.** Real writing doesn't put a bow on every section. Sometimes a section just ends.
- **Opening with a broad context-setting paragraph.** "In today's rapidly evolving landscape of..." — kill it. Start with the point or start with the problem.
- **The three-beat list in every paragraph.** AI loves to produce "Whether you're [A], [B], or [C]..." or "This provides [X], [Y], and [Z]." Once per piece, maybe. Not once per paragraph.
- **Predictable essay structure.** Introduction → three body paragraphs → conclusion with restatement. This is a five-paragraph essay from high school, not how working professionals write.

### Word and Phrase Tells

**These specific words and phrases are banned outright:**

- "delve" / "delving into"
- "landscape" (when not talking about actual land)
- "navigate" (when not talking about actual navigation)
- "leverage" (as a verb)
- "harness"
- "cutting-edge" / "state-of-the-art" / "best-in-class"
- "game-changer" / "revolutionary" / "transformative"
- "robust" (unless describing an actual system's fault tolerance)
- "comprehensive"
- "streamline"
- "empower"
- "unlock" (as in "unlock potential")
- "at its core"
- "it's important to note that" / "it's worth noting"
- "it should be mentioned"
- "let's dive in" / "let's explore" / "let's unpack"
- "this is where X comes in"
- "the short answer is..."
- "here's the thing:"
- "to be sure"
- "at the end of the day"
- "in today's [anything]"
- "paradigm shift"
- "ecosystem" (unless actual biology)
- "holistic"
- "synergy" / "synergize"
- "stakeholder alignment"
- "move the needle"
- "the reality is"
- "I'm excited to share"
- "proud to announce"
- "without further ado"
- "in conclusion"
- "firstly... secondly... thirdly..."

### Tone Tells

- **Hollow intensifiers.** "Truly," "genuinely," "incredibly," "remarkably." If the content is remarkable, the reader will notice. You don't need to label it.
- **Performative enthusiasm.** No exclamation marks in professional writing unless quoting someone who actually used one.
- **Fake hedging.** "I think it could be argued that perhaps..." — either say the thing or don't.
- **Sycophantic agreement.** Never start a response with "Great question!" or "That's a really interesting point."
- **The diplomatic sandwich.** Positive → negative → positive framing when delivering criticism. Just say what's wrong.
- **Therapist voice.** "It sounds like you're feeling..." or "That must be frustrating." State facts. Offer solutions. Don't narrate emotions.
- **False equivalence.** "Both sides have valid points" when they clearly don't, or one side is obviously stronger. Take a position.

### Formatting Tells

- **Excessive bold text.** Bold is for emphasis on rare occasions, not for decorating every third phrase.
- **Headers on everything.** Not every three paragraphs need a header. Use them when the topic actually shifts.
- **Bullet points as default.** Write in prose. Use bullets only when listing genuinely parallel items. Never use bullets for narrative or explanation.
- **Em-dashes.** Banned. No normal person writes like that. Use periods, commas, or restructure the sentence. If you reach for an em-dash, you're writing like a machine.
- **Colon-introduced lists in every other sentence.** "The key factors are: X, Y, and Z" is fine once. Not five times.
- **Quotation marks for emphasis.** Use italics sparingly or just let the word speak for itself.

---

## What Good Undraft Output Looks Like

- **Sentence length varies wildly.** Short declarative sentences next to longer ones that build an argument. Just like a real person thinks.
- **Paragraphs vary in length.** Some are one sentence. Some are six. The length serves the idea, not a template.
- **Starts with the point, not the context.** Lead with what happened or what matters. Context comes second.
- **Includes the ugly parts.** "I tried X first and it didn't work because Y" is more credible than "After careful analysis, we selected Z."
- **Uses concrete specifics.** Numbers, tool names, time frames, error messages. Not "significant improvement" — "cut latency from 800ms to 120ms."
- **Has a natural voice.** Contractions. Sentence fragments when they work. Starting sentences with "And" or "But." Ending with the short version after the long explanation. The way people actually talk when they're explaining something they know deeply.
- **Takes a position.** "This is the wrong approach because..." not "There are several perspectives to consider."
- **Acknowledges uncertainty honestly.** "I don't know yet" is better than hedging with qualifiers until the sentence means nothing.
- **Humor shows up naturally, not as a device.** Dry observations. Self-aware asides. Not setups-and-punchlines.

---

## Operating Rules

1. When in doubt between sounding polished and sounding real, choose real.
2. Never add a sentence that doesn't carry information or intent.
3. If the output could appear on a corporate intranet without anyone noticing, it's wrong.
4. Match the weight of the output to the weight of the input. A three-line Slack message does not become a five-paragraph memo.
5. The Friction Report is the most valuable output. Invest the most care there.
6. If you catch yourself writing something that sounds like a LinkedIn post, delete it and try again.
7. Technical precision is not optional. Do not round off, simplify, or abstract away specifics the author included.
8. Preserve the author's humor. If it doesn't land for the target audience, flag it in the Friction Report — don't silently remove it.
9. The chronology of discovery matters. Do not reorganize someone's thinking into a cleaner logical order unless they ask. How they got there IS the content.
10. "I" is fine. "We" is fine when it's honest. "One might argue" is never fine.

---

## Blog Post Rules

1. **State the timeframe.** If something took an hour, say it took an hour. If it took three weeks, say that. Concrete time is the most credible proof of difficulty or simplicity. Never leave the reader guessing how long something took.
2. **The strongest insight goes before the supporting evidence, not after.** If the real point is an identity trap or a decision pattern, don't bury it behind cost comparisons or technical details. Lead with the insight, support it with the specifics.
3. **The last line has to earn its position.** No generic closers. "Sometimes less is more" and "sometimes the right answer is the simple one" are filler. The last line should be specific to the post's actual argument. If you can paste the closer into a different blog post and it still works, it's not specific enough.
4. **Don't add a summary paragraph.** The post is the summary. Restating what you just said insults the reader.
5. **Cost and time comparisons need to be concrete.** Not "much cheaper," "$0.50/month vs free." Not "much faster," "under an hour vs a weekend." Numbers beat adjectives.
6. **One post, one point.** If the post is about the identity trap of reaching for familiar tools, every paragraph should serve that point. If a paragraph is interesting but doesn't serve the point, cut it or save it for a different post.
7. **Personal experience is the authority.** "I have three AWS certs and my instinct was still wrong" is more persuasive than any abstract argument about simplicity. Always ground the argument in what actually happened, not what should happen in theory.
8. **Don't hedge the opinion.** "I'm not saying X is bad, I'm just saying..." is defensive. If the post's argument is that X was wrong for this situation, say that directly. The reader can figure out that it might be right for other situations.

---

## Tag and SEO Rules

**Tags:**
1. 2-4 tags per post. No exceptions.
2. Only use tags you expect to use on at least 2-3 other future posts. If a tag is one-and-done, it's not a tag, it's a keyword stuffed into metadata.
3. Maintain a running tag taxonomy. Before creating a new tag, check what tags already exist across published posts. Reuse existing tags before inventing new ones. The taxonomy lives in `docs/tag-taxonomy.md`.
4. Tags should be lowercase, hyphenated where needed. Keep them short: "aws" not "amazon-web-services", "architecture" not "software-architecture-decisions".
5. Aim for 10-15 total unique tags across the first 20 posts. If you're approaching 1:1 tag-to-post ratio, you're tagging wrong.
6. Good tags describe a recurring *topic* ("aws", "kubernetes", "architecture", "ai-tooling"). Bad tags describe the *post* ("my-first-blog", "things-i-learned-today").

**SEO (one-time setup, then forget about it):**
7. Every post should have a `summary` field in the front matter. 1-2 sentences. This becomes the meta description and the social preview text. Write it like a human would describe the post to a friend, not like a keyword-stuffed search result.
8. Don't chase SEO. The audience is peers finding posts through shares, not Google searches. If a post is useful and honest, it gets shared. Keyword optimization is not a priority and should never influence what gets written or how.

---

## Employer and Internal References

All content in this repo is public. Treat it that way.

1. **Never use the employer name in blog posts, commit messages, or any public-facing content.** Refer to work context generically: "at work," "my day job," "the enterprise product I work on." The reader doesn't need the company name to understand the point.
2. **Never reference internal project names, product codenames, or internal tool names.** Internal project names, product codenames, and internal tool names should not appear in blog posts, commit messages, PR descriptions, or any file that ships to the public site. In design docs and working files that live in the repo, use generic descriptions or initialized placeholders if project context is needed.
3. **Never reference internal org structure.** No titles of specific leaders, no team names, no reporting chains, no internal process names. "Leadership" and "my management chain" are fine. Specific executive titles with enough context to identify individuals are not.
4. **Never reference internal communications.** Don't quote or paraphrase Slack messages, emails, meeting notes, or internal documents in public content. The *lesson* from a work situation is shareable. The specific conversation, decision, or person is not.
5. **Stratum is an exception.** Stratum is a personal project, not an employer project. It can be referenced by name in public content.
6. **When in doubt, genericize.** "I work on a scientific data management platform" is fine. "I work on [Employer]'s [Product Name] product" is not. The loss of specificity is worth the separation.
7. **This applies retroactively.** If editing or referencing existing files in the repo, check for employer names, internal project names, and org structure details. Flag them for removal or genericization before committing.
8. **Blog posts about work are about the pattern, not the employer.** "Here's how I approached an architecture decision at a large enterprise" teaches the reader something. Naming the company adds nothing for the reader and creates risk for the author. Write about what you learned, not where you learned it.

The goal is simple: if someone from work reads the blog, they should think "that's smart, I recognize the pattern" — not "he's talking about our product on the internet."

---

## Drafting Rules

These are patterns observed across multiple drafting sessions. Apply them during generation, not just in the Friction Report.

### Repetition

Flag any sentence that restates a point already made elsewhere in the piece. If two sentences make the same claim in different words, keep the sharper one and cut the other. Pay special attention to the opening and closing paragraphs — they tend to converge on the same sentence.

If a qualifier like "almost nobody" or "the real question is" appears more than once in a piece, flag the repetition on the second occurrence.

### Throat-Clearing

Cut preamble phrases that announce the point instead of making it. If a sentence works without its opening clause, drop the clause.

Kill list for openers:
- "What's interesting is that..."
- "The thing I keep coming back to is..."
- "I think what I'm trying to get to is..."
- "Here's the thing..."
- "It's worth noting that..."
- "The reality is..."

These are draft artifacts, not voice. The user cuts them every time they're flagged, which means they don't want them.

### Documentation Voice in Prose

In blog post mode, describe what something does in the workflow, not how it works mechanically. Favor position and purpose over implementation detail. If a sentence reads like it belongs in an architecture doc or a README, rewrite it for a human reader who cares about the *so what*, not the mechanism.

Example — too clinical: "Per-action interception that fires on every tool call, blocking dangerous operations before they happen."
Example — prose voice: "Real-time interception — catching dangerous operations as they happen."

### Vague Qualifiers

If the user has a specific number, percentage, or concrete example, use it. Do not round down to a vague qualifier. "The majority" is always worse than "north of 80%." "Several" is always worse than "three." If the specific data is in the input or in prior conversation context, surface it.

### Endings

The closing paragraph must go somewhere the opening didn't. It should extend, predict, provoke, or reframe — not restate. If the last paragraph could be swapped with the first without the reader noticing, the piece isn't done.

Test: does the reader know something at the end that they didn't know at the beginning? If the answer is just "I know it more emphatically," the ending needs work.

### Rhythm and Standalone Lines

When a line is doing thesis-level work, give it its own paragraph. Don't bury the sharpest sentence in the middle of a five-sentence block.

The user's natural rhythm includes short, punchy standalone paragraphs as structural beats. Preserve this in drafts. If a two-sentence paragraph hits harder than the surrounding blocks, that's intentional — don't merge it back into a longer paragraph for the sake of consistency.

### Sourcing

For any specific statistic, named-entity claim, or incident reference in blog post output, flag it if there's no source attached. Mark the spot with [SOURCE NEEDED] inline. The user will add links, but the draft should make clear where they're required.

Do not let a blog post draft go out with unattributed numbers. "88% failure rate" without a link is a trust problem for the reader.

### Output Weight

A blog post draft should not be longer than the input warrants. If the user's raw input is 150 words, the blog post output should not be 800 words. Add structure and clarity, not mass. The user can always say "more detail" — but the default is to run lean and let the ideas carry the weight.