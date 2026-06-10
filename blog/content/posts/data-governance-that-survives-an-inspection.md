---
title: "Data Governance That Survives an Inspection"
date: 2026-06-09T00:00:00-05:00
tags: ["data", "life-sciences", "compliance"]
summary: "The samples post ended on seating a data steward. This is what you build around that seat in a regulated life sciences org: the roles you actually need, the order to do it in, and why the regulation is the only budget argument that ever works."
---

Last time I wrote about why three systems gave three different answers to "how many samples do we have," and it came down to a role almost nobody seats: the data steward, the person who decides what a word means and defends it the next time someone wants an exception. That post ended on appointing one. It treated governance as the standing function that keeps definitions honest while the org moves underneath them, and left it there. This is the next question. You've seated the steward. Now what do you build around that seat so it survives contact with a regulator?

Most data governance programs die the same way. Someone buys a catalog tool, a working group produces a policy binder, and six months later nobody can tell you who is accountable for the number on a batch release certificate. The binder sits on a shared drive. The tool gets renewed once out of guilt, then cancelled. The catalog became another place to store the confusion.

In life sciences you don't get to fail that quietly. The gap shows up during an inspection, in front of someone who can issue a Form 483 observation or a warning letter and, in the worst case, hold up your product. A recent IQVIA survey put it bluntly: only 31% of pharma companies have a fully implemented data governance strategy, which leaves nearly 70% running on partial coverage or none at all. ([IQVIA](https://www.iqvia.com/blogs/2024/02/navigating-the-data-deluge-through-data-governance))

So before the framework, the catalog, or the org chart, get one thing straight. Data governance is not a tooling problem. It is an accountability problem wearing a tooling costume. A catalog is a filing cabinet. Governance is knowing whose name is on the file and how you prove the contents are true.

## The regulation is your budget

Life sciences is different in a way most people get backwards. The regulation is not the obstacle to governance. It is the only argument that reliably gets it funded.

"Better data quality" loses every budget fight it enters, because it competes with shipping product. "We will fail our next GxP inspection on data integrity" wins, because everyone in the room has seen what a warning letter does to a launch timeline. Anchor the program to that, not to abstract data hygiene.

A handful of regulatory pillars define what "good" means, and you should be able to name all of them before you write a single policy:

- **GxP** is the umbrella for the Good Practice regulations: GMP (manufacturing), GLP (laboratory), GCP (clinical), GDP (distribution). If your data supports a GxP process, it is inspectable.
- **21 CFR Part 11** (US FDA) and **EU Annex 11** set the rules for electronic records and signatures: unique user authentication, system-generated audit trails, validated backups, and controls that prevent silent record alteration. ([AVS Life Sciences](https://www.avslifesciences.com/blog-post/master-fda-21-cfr-part-11-eu-annex-11-and-gamp-5-compliance))
- **GAMP 5**, from ISPE, is the de facto standard for validating the computerized systems those records live in. It is guidance, not law, but inspectors treat it as the expected approach. ([IntuitionLabs](https://intuitionlabs.ai/articles/gamp-5-computerized-system-validation-pharma))
- **ALCOA+** is the data integrity standard your records get measured against: Attributable, Legible, Contemporaneous, Original, Accurate, plus Complete, Consistent, Enduring, and Available. It is referenced directly in the FDA's 2018 data integrity guidance and the MHRA's 2018 GxP guidance. ([TotalLab](https://totallab.com/resources/alcoa-principles/))

Every policy you write should trace back to one of these. If a rule can't, ask why it exists.

## The roles, and who actually carries the weight

Governance runs on named people with real decision rights, not on a committee that meets quarterly to admire dashboards. The role set is well established (DAMA-DMBOK is the common reference point), and the titles matter less than the boundary between accountability and execution. ([DAMA](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/))

- **Executive sponsor**, usually a Chief Data Officer or a VP of Quality. Holds the budget and the authority to make a decision stick across functions. Without this, the program is a hobby. In one mid-size pharma turnaround, the first council didn't carry weight until it sat at executive VP level and data made it onto the executive agenda. ([HYGHT](https://hyght.ch/case-study/ls-interim-chief-data-officer/))
- **Data governance council**, the cross-functional body that sets policy, arbitrates disputes between domains, and prioritizes the work. Co-chaired by business and IT, with every line of business represented.
- **Data governance office / lead**, the person who runs the program day to day so the council doesn't have to. The secretariat, the convener, the one who keeps the issue log honest.
- **Data owners**, senior business leaders accountable for a data domain. The head of manufacturing owns batch data. Regulatory affairs owns submission data. They make the calls on access, definitions, and quality thresholds. They rarely have time for the day-to-day, which is the whole reason the next role exists.
- **Data stewards**, the practitioners who make governance real. They define the critical data elements, set and monitor quality rules, maintain the metadata, and resolve issues when a number doesn't reconcile. This is the load-bearing role, and it is the one organizations consistently underfund. <mark>A governance program with great owners and no stewards is a press release.</mark>
- **Data custodians**, the IT side: database administrators, platform engineers, the people who run the systems, provision access, and maintain backups under the stewards' direction.
- **Quality assurance**, who own validation, audit readiness, and the SOPs that turn policy into inspectable evidence.
- **Regulatory affairs**, who care about submission data standards like IDMP for product master data and CDISC for clinical, because that is the form the data has to take when it leaves the building.
- **Computer system validation specialists and information security**, who make the systems defensible under Part 11 and Annex 11 and keep patient and personal data inside GDPR and HIPAA lines.

One position you should hold firmly: data owners must be business leaders, not IT. If IT owns the data, no business decision about it ever sticks, because IT can't overrule the function that generates it. IT is the custodian. The business owns.

## The order to do it in

The biggest failure mode after "we bought a tool" is "we tried to govern everything at once." Don't. Sequence it.

1. **Find the wound and the sponsor.** Anchor the program to a specific risk or failure: an audit observation, a number nobody trusts for a submission, a domain that has burned you before. The wound is what gets you the sponsor, and the sponsor is what gets you everything else.
2. **Scope narrow.** Pick one regulated domain that hurts and govern that. Product master data for IDMP is a common and tractable starting point. Batch records are another. Enterprise-wide rollouts collapse under their own weight before they show value.
3. **Stand up the operating model.** Council, charter, and decision rights. Write the charter in plain language with a specific purpose ("improve the quality of data on the registration system"), not a generality. Map a RACI so every critical decision has exactly one accountable name. ([DataStrategyPros](https://www.datastrategypros.com/resources/data-governance-charter))
4. **Inventory and classify.** Identify your critical data elements, trace their lineage, and tag each as GxP or non-GxP. You cannot protect what you can't see, and you cannot prioritize if everything looks equally important.
5. **Write policies that trace to the regulation.** Anchor data quality rules to ALCOA+ and the relevant GxP requirement. A policy that can't name the regulation it serves is decoration.
6. **Make stewardship operational.** Assign named stewards per domain, stand up an issue log, define the quality rules, and run remediation as a real workflow with deadlines, not a backlog nobody owns.
7. **Measure against inspection risk.** Track data quality metrics that map to audit exposure, not vanity numbers. "Percentage of critical data elements with a defined owner and quality rule" beats "records processed."
8. **Validate and document.** Bring the systems under CSV per GAMP 5, with audit trails, electronic signatures, and access controls that satisfy Part 11 and Annex 11. In a regulated shop, undocumented governance is the same as no governance.
9. **Expand by maturity, one domain at a time.** Use the first domain as the proof, then move to the next. Governance grows by demonstrated value, never by mandate alone.

Communication is most of the job. One practitioner estimate puts data governance at 80 to 95 percent communication and the rest tooling, which sounds like an exaggeration until you watch a technically perfect program fail because nobody told the people entering the data why any of it mattered. ([IBM](https://www.ibm.com/think/insights/data-governance-strategy))

The test of whether you've actually built something isn't the size of the policy binder. It's whether a steward, asked who is accountable for a number and how they know it's accurate, can answer on the spot without convening a meeting. That is the question an inspector asks.

The samples post ended with a count that wasn't a count: you have as many samples as you have agreements about what a sample is. Governance is the machinery that turns those agreements into something an inspector will sign off on. The binder doesn't do that. A named human, backed by a regulation and a system that proves they're right, does.
