---
title: "Projects"
layout: "single"
summary: "Things I build outside the day job."
---

<!-- USER REVIEW REQUIRED: confirm the Stratum description is accurate and in your words before pushing. Add or remove entries as you see fit. -->

## Stratum

A guard pipeline for AI-generated code. Seven stages between "agent wrote code" and "code is safe to ship," ordered from cheapest to most expensive: empty diff, scope enforcement, compilation, structural invariants, orphan detection, cross-session identity tracking, and only then an AI reviewer checking the changes against the original intent. Most agent failures get caught without burning a single token.

Active. I've written about the thinking behind it in [Who Watches the Watcher](/posts/who-watches-the-watcher/) and [The Stack Nobody Talks About](/posts/the-stack-nobody-talks-about/).

## The homelab

24 containers behind Prometheus and Grafana. Partly a lab, partly a standing argument that architectural opinions are better when you've had to operate your own systems.
