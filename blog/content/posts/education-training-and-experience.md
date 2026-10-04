---
title: "Education, Training, and Experience"
date: 2026-10-12
draft: false
tags: ["compliance", "life-sciences"]
shape: teardown
origin: thread
reach: adjacent
summary: "Part 11 has a clause requiring that the people who develop, maintain, or use a system be qualified for their assigned tasks. An agent now sits in the develop seat, and every regulatory text written since says the human checking its output must be qualified without saying in what."
---

Part 11 has a clause that never makes the slide. It's paragraph (i) of [11.10](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11/subpart-B/section-11.10), after the audit trail and the signature controls everyone quotes:

> Determination that persons who develop, maintain, or use electronic record/electronic signature systems have the education, training, and experience to perform their assigned tasks.

Three verbs, one triad, one determination. Take them in order.

Develop, maintain, or use. In 1997 those were three groups of people, and a shop could point at each one. Point at an agent pipeline and the first seat has no person in it. The model develops. A person maintains the prompts and the guards. A person uses what comes out, which in [the pipeline I built](/posts/agent-world-reinventing-part-11/) means approving the spec the agent works from. The clause asks for a determination about the developer, and the only document describing the developer's education is a model card the shop didn't write, attached to a model with a [retirement date](/posts/sixty-days-notice/). So the determination has nowhere to go but the other two seats. Whatever competence the clause expected to find spread across three roles now has to be found in two, and mostly in the last one.

Education, training, and experience. The triad is older than Part 11. The drug GMP rule, [211.25](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-B/section-211.25), asks the same three, or any combination of them, of each person engaged in manufacturing, and adds a sentence Part 11 leaves out: training shall be in the particular operations that the employee performs. Not training in general. Training in the thing you do. For the person in the use seat, the particular operation is reading a diff a model wrote and deciding whether it merges.

Name the course.

Two regulatory texts written since the models arrived name the human and stop there. The [draft Annex 22](https://health.ec.europa.eu/document/download/5f38a92d-bb8e-4264-8898-ea076e926db6_en?filename=mp_vol4_chap4_annex22_consultation_guideline_en.pdf) keeps LLMs out of critical GMP applications and, for everything else, puts "personnel with adequate qualification and training" in charge of confirming the output is suitable for its intended use. The EU AI Act's [Article 4](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-4), applicable since February 2025, requires providers and deployers to ensure "a sufficient level of AI literacy" among their staff, "taking into account their technical knowledge, experience, education and training". The same triad, in a different order, in a law about a different thing. The Commission's own [Q&A](https://digital-strategy.ec.europa.eu/en/faqs/ai-literacy-questions-answers) on that article adds that there is no need for a certificate, no obligation to measure what anyone knows, and that an internal record of trainings will do.

Read the three together and the credential comes into focus. It's a line in a training record. A course title, a date, a signature. Adequate, sufficient, appropriate. Each text requires the qualification and leaves the content to the shop, which is the normal arrangement: the regulator names the requirement and the shop writes the curriculum. A lab can write down what an analyst has to know about a method because the method is theirs and its failure modes are catalogued.

What the use seat has to know about an agent is where this pipeline's diffs go wrong. That catalogue exists too. It's the set of changes the guards held, plus the set that got through and shouldn't have, and it lives in one place, the pipeline's own history. No general course contains it, because it's different for every pipeline and it changes when the model does.

So the determination the clause asks for looks like this. Take a diff the agent produced and the guard held. Strip the verdict. Hand it to the reviewer. If they find the defect, the training record gets a line that says what they demonstrated, on which pipeline, under which model ID. If they don't, the shop has learned something about its approval step before an incident teaches it.

The third word is the hard one. Experience in the particular operation accrues one reviewed diff at a time, and for an unattended pipeline those diffs are production changes. The reviewer gets qualified on the job, by the job, and the record of it is the merge log.

Two training records sit behind every merged agent change. The developer's is a model card someone else wrote, due to expire on a date the vendor set. The reviewer's is a signature under an SOP. Neither shows anyone catching a bad diff.
