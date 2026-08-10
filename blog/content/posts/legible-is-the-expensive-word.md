---
title: "Legible Is the Expensive Word"
date: 2026-08-13
draft: false
tags: ["data", "life-sciences"]
summary: "A 25-year retention rule sounds like a storage problem, and storage mostly solves itself. The regulation also says legible, and legible means something can still open the file in 2051."
---

In 1986 the BBC marked the 900th birthday of the Domesday Book by compiling a new one: a survey of British life with contributions from around a million people, published on [LaserDiscs in a format called LV-ROM](https://en.wikipedia.org/wiki/BBC_Domesday_Project). By 2002 the discs were close to unreadable. The players that could spin them had nearly vanished, and it took an emulation project by two universities to get the data back out. The 1086 original is ink on parchment, and you can still read it.

Sixteen years against nine hundred.

That gap is waiting inside every long retention clock, including the one I've [pointed at before](/posts/required-to-delete-this/): the EU Clinical Trials Regulation requires a trial master file to be archived for [at least 25 years](https://www.legislation.gov.uk/eur/2014/536/article/58?view=plain) after a trial ends, and the condition it sets is that the content stay available and legible the whole time. Engineers hear a storage requirement, and the storage is nearly free; an object store holds bytes intact for decades without anyone thinking about them. Legible is the expensive word. It means that in 2051 a piece of software still has to open the file, interpret it, and put something in front of an inspector that a human can read. Bytes survive on neglect; legibility needs a reader, and every reader is software with a service life nowhere near the record's.

The natural reader is the application that wrote the record, and nothing about the clock keeps it running. Systems get replaced, vendors get acquired, licenses lapse. When a system is decommissioned its records move to an archive, and the archive inherits files without the software that knew what they meant. Instrument data is the sharpest version: lab instruments write proprietary formats that the vendor's own software reads, a problem large enough that pharma companies and instrument vendors [formed a consortium](https://www.allotrope.org/asm) to convert lab output into an open, human-readable model. The retention clock keeps running after the instrument leaves the bench, after the license expires, sometimes after the vendor stops existing.

Archivists have been in this business for decades, and their playbook has three moves, none of which is buying more storage. Choose a self-contained format at write time: [PDF/A](https://www.pdf-tools.com/pdf-knowledge/all-about-pdf-a-long-term-archiving/) exists because an ordinary PDF can lean on fonts and resources outside itself, and the archival profile forbids depending on anything the file doesn't carry. Migrate: convert the records to a fresh format before the old reader dies, on a cadence, for as long as the clock runs. Emulate: rebuild the dead reader in software, which is what rescued the Domesday discs and is no one's plan A for an inspection. In a GxP shop the middle move weighs more than it sounds, because converting validated records is a controlled change with evidence attached. Every migration owed across the 25 years got scheduled the day someone picked the format.

That reframes what a storage platform promises when it takes custody of a regulated record. Handing the bytes back intact is a promise the platform can keep alone. Legible depends on a reader the platform doesn't own, and the place the difference surfaces is the decommissioning plan: systems retire and their records don't. If the plan says "export to the archive," the question missing from the checklist is what opens the export twenty years from now.

Parchment bundles the record and its reader into a single object; eyes are backward compatible. Every digital format splits that bundle, and the clock runs on both halves. The monks never made a format decision. Theirs is the one that held.
