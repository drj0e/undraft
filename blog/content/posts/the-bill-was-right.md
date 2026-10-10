---
title: "The Bill Was Right"
date: 2026-10-18
draft: false
tags: ["data", "platform-engineering", "leadership"]
shape: argument
origin: thread
reach: core
summary: "GitHub's agent adoption metrics undercounted for a stretch this year while the invoice stayed correct, and the difference between the two numbers is who would have noticed. An adoption chart with no such person on it isn't a measurement yet."
reviewed: true
---

Who would have noticed, inside a week, if your agent adoption number had started undercounting?

On October 6 GitHub answered that for its own customers. Several IDEs had moved Copilot's agent sessions onto the Copilot SDK. The sessions stopped saying which editor they came from, so the usage metrics couldn't place them. Most of that activity was left out of the reports. Some was filed under the command-line tool. The notice puts the consequence in two sentences: ["Billing isn't affected. This issue only changed how agent activity was attributed in usage metrics, not what you were charged."](https://github.blog/changelog/2026-10-06-update-your-ide-to-restore-agent-activity-in-copilot-usage-metrics/)

Same sessions. Two numbers. The number with money attached was right the whole time. The one on the adoption dashboard fell while the usage it was supposed to measure kept growing, and the notice opens with that chart's shape: agent activity falling while Copilot usage kept growing.

An invoice has two readers who lose when it's wrong. The vendor loses revenue on an undercount, the customer pays for an overcount, and each side employs someone to catch the other. Now walk the distribution list for the adoption chart and look for the reader who loses when it undercounts. The platform team that picked the tool wants the line up. The leadership that funded the seats wants it up. The vendor wants it up. A dip reads as rollout lag and a rise gets a slide. The chart can be wrong for as long as the fix takes and cost that whole list nothing.

I argued in June that a captive platform's adoption chart [isn't a vote](/posts/nobody-chose-your-platform/). This is a step before that. It isn't a measurement either, until every absence in it has a status.

The vendor's own data has one, a layer down. GitHub's reconciliation page describes an `Unknown` value that appears "when telemetry from the IDE client lacks sufficient detail to categorize the activity," then adds that ["Unknown values are excluded from dashboard visualizations but appear in API and NDJSON data for completeness."](https://docs.github.com/en/copilot/reference/copilot-usage-metrics/reconciling-usage-metrics) The status exists in the export and the chart drops it. The agent sessions never even reached Unknown. They were dropped, or counted as something else, so on the dashboard the zero and the "we couldn't place this" were the same pixel.

Last month I wrote about the paper record that [refuses an empty box](/posts/a-blank-without-initials/). That was a rule about one cell. It survives aggregation. A total over rows that hold unrecorded absences inherits every one of them, and the chart shows the total.

Operators have already worked through the local version of this. A September guide for Prometheus users works through [telling a healthy zero from a dead exporter](https://oneuptime.com/blog/post/2026-09-29-healthy-zero-no-data-absence-timestamps-heartbeats/view): initialize counters so zero is reported instead of assumed, alert on absence over a window, carry a heartbeat tied to real work. All of it got built because the person reading that dashboard is on call, and a flat zero at three in the morning costs them either sleep or an outage. An adoption dashboard costs its reader nothing, and the vendor's substitute for that machinery is a sentence on a reference page: "If you notice missing users or unexpectedly low adoption numbers, verify IDE telemetry settings before troubleshooting other causes." The number can be wrong in exactly the direction that looks like a finding, and the first cause to rule out is your own clients.

The fix ships per editor through November, and the notice says the missing data can't be backfilled, so the recovery will be gradual rather than a single jump. For the next two months the agent line on those dashboards climbs as developers update. Some of those slides will call it adoption.

So, for each adoption number you send up the chain, name the person who would have noticed within a week if the clients had stopped identifying themselves. If the only honest answer is the billing team, add a row the chart doesn't have, sessions the report couldn't place, and put it on the same slide as the line.
