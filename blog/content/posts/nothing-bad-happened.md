---
title: "Nothing Bad Happened"
date: 2026-09-04
draft: false
tags: ["automation", "code-quality"]
summary: "Antivirus vendors ship a harmless 68-byte file so you can prove your scanner still fires. My guard pipeline has no equivalent, and a healthy morning and a broken one produce the same green board."
---

Sixty-eight bytes of printable ASCII, and any antivirus product worth its license is supposed to flag it:

```
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
```

Nothing dangerous is in there. It's a small DOS program that prints its own name and exits. EICAR and CARO assembled the string in the early nineties and vendors agreed to carry those exact 68 bytes in their signature databases as a known harmless threat, so anyone could confirm a scanner was installed, running, and reading the place they thought it was reading, without keeping live malware around to test with. ([EICAR](https://www.eicar.org/download-anti-malware-testfile/))

An industry does not manufacture a fake threat for fun. It does it because <mark>a detector that has stopped detecting produces exactly the output of a detector with nothing to find.</mark>

Stratum exists to say no to an agent. When I [sorted its checks](/posts/the-guard-the-agent-can-see/) into the ones an agent can retry against and the ones it never learns about, all of that reasoning was about what a check does when it fires. I gave no thought at all to the weeks when none of them do.

A test suite reports its own rot eventually, by accident. Delete an assertion and the gap surfaces the next time somebody breaks that behavior in a way the missing assertion would have caught. [Mutation testing](https://arxiv.org/abs/2102.11378) exists because eventually and by accident is not a schedule: seed a small artificial fault, see whether any test notices, score the suite on what it catches. Google published what it took to make that tractable across a monorepo their size.

A guard pipeline gets no version of that accidental feedback, because its healthy state is a green board. Most nights the agent does something reasonable, every gate passes, and I go make coffee. A guard that stopped running produces the identical morning.

The ways a check stops firing are boring. A rule matches on a path that a refactor renamed. A script exits zero when it crashes on its own bug. A stage globs for files, finds none, and reports a clean sweep of nothing. None of those announce themselves, and all three return the same color as a good diff.

The trap tightens as the agent gets better. A pipeline that rejects something most nights is at least demonstrating that it can. Suppose the model improves to where a real rejection becomes a monthly event. The evidence that my guards still work thins at the same rate my trust in the whole setup grows, and from where I sit both of those look like a green board.

So the artifact I'm missing is the specimen: an input each guard is required to reject, held fixed, run against that guard on the same cadence the guard runs against the agent. If the file-scope check fails to reject a diff reaching outside its assignment, the check is broken, and I want that on a Tuesday rather than during the run where it would have mattered.

Every guard I wrote has a shape of diff it exists to catch, and the pipeline meets that shape often enough to justify the guard. So the specimens come to me. Each one sits on my screen for the length of a rejection message, at the moment I have the least possible interest in it, because the guard did its job and the run needs restarting. Somebody had to design the EICAR file on purpose. Mine arrive for free, and I let every one of them scroll past.
