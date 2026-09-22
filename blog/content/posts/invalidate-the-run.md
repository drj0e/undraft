---
title: "Invalidate the Run"
date: 2026-09-23
draft: false
tags: ["ai-tooling", "code-quality"]
summary: "A PCR plate carries a tube the lab already knows is positive, and if that tube comes back negative the whole run is thrown out. A guard pipeline only ever grades real diffs, so a night of all-green can't tell you the guards are working from the guards being off."
---

Every plate that goes through a diagnostic PCR run carries a tube with nothing to learn from. It's the positive control, RNA the lab already knows will light up, and the CDC's instructions for its COVID panel say what to do if it doesn't: when any control fails to perform as expected, the run should be invalidated and re-tested. ([FDA](https://www.fda.gov/media/134922/download)) Every patient result on the plate goes out with it, including the ones that read the way you hoped.

The tube says nothing about any patient. Its only job is to catch the day the assay stops detecting.

Now the report a guard pipeline hands back after an overnight run. Every diff green. A working pipeline produces that on a good night. A broken one produces it every night, whether a rule stopped loading or a semantic review timed out and returned its default, and both read as a run with nothing to report. What would separate them is a diff the pipeline was obligated to reject, and no such diff went through.

Antivirus solved this with a file. The EICAR test file is 68 bytes of printable ASCII that does nothing but print its own name when run, and any scanner that supports it is expected to flag it as though it were malware. ([EICAR](https://www.eicar.org/download-anti-malware-testfile/)) Drop it in a directory and you learn, in one step, whether the scanner is running and whether it's watching where you think it's watching.

The nearest thing software testing has is mutation testing, which Google runs at a scale that settles the feasibility question: nearly 17 million mutants across 760,000 changes, 2 million of them surfaced to developers in code review. ([Petrović and Ivanković, ICSE 2018](https://research.google/pubs/state-of-mutation-testing-at-google/)) It answers a different question, though. A mutant grades the test suite, one layer, and the finding goes to a person so they can write the missing test. The positive control asks whether the detector as deployed tonight, every layer from lint to the hidden checks, fires at all. Not how good the instrument is. Whether it's on.

So the control for a guard pipeline is a known-bad diff, written once by whoever owns the pipeline rather than by the agent, and replayed on every run through the same path the real diffs take. A change that deletes a test, another that writes to a path the policy forbids, a third carrying a string shaped like a credential. Each has one correct verdict, and the rule from the plate applies without translation: a green on the control invalidates the run, every real diff in it included.

Nothing in the stack I built carries one. Every diff it has graded was real, and the only way I find out a verdict was wrong is an escape surfacing later. I've already [gone looking](/posts/not-useful/) for a signal on rules that fire when they shouldn't. This is the other column, rules that stay silent when they should fire, and it doesn't have to wait for an escape.

In 1950 two pathologists, Stanley Levey and E. R. Jennings, proposed putting Shewhart's control chart to work in the clinical lab. What goes on the chart, run after run, is the control. ([Wikipedia](https://en.wikipedia.org/wiki/Laboratory_quality_control))
