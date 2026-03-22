---
title: "I Almost Over-Engineered a Blog with AWS"
date: 2026-03-22
draft: false
tags: ["aws", "github-pages", "infrastructure"]
---

I used to think publishing a personal site meant AWS, WAF, Route 53, and a weekend of debugging. Turns out it's a markdown file and `git push`.

My first AWS course was in 2018. The textbook had printed screenshots of the AWS console UI that you were supposed to follow along with before opening the actual console. Think about how insane that is. The AWS UI changes so frequently they'd need to republish the book every 45 minutes to keep it accurate. But that was the world, and I learned in it.

Since then I've picked up three AWS certs. Cloud Practitioner, SysOps Administrator, Solutions Architect Associate. I've spent years building things on AWS. So when I decided to start a blog, my brain went straight to the playbook I know.

The plan I almost executed looked like this:

- Elastic Beanstalk for the website
- Route 53 for DNS
- WAF for security
- ACM for the TLS cert
- A full build pipeline to deploy changes
- S3 and CloudFront if I went the "simpler" static route

That's a weekend project minimum. Route 53 hosted zone setup, DNS propagation alone takes hours, configuring CloudFront distributions, debugging IAM permissions when something doesn't connect right. I've done this before. Multiple times. And every time it felt like the reasonable way to host a website, because that's the toolset I know.

Here's what actually happened today.

I set up Hugo. Single Go binary, no dependency chain. Picked a theme. Wrote a config file. Total setup time for the static site generator was maybe 20 minutes.

Then deployment:

1. `git push`
2. GitHub Actions builds the site automatically
3. Added 5 DNS records in Cloudflare
4. Set the custom domain in the GitHub repo settings

That's it. The whole thing, domain purchase to live site, took under an hour. Updates going forward are: write a markdown file, push, live in 60 seconds. GitHub Pages is free. The domain was $10.46/year. The AWS route would have cost $0.50-2/month and a weekend I don't get back.

The trap is reaching for the tools you know instead of the tools the problem needs. I have three AWS certs. Of course my instinct was to use AWS. But the instinct was about my identity as someone who builds on AWS, not about what a blog actually requires. A personal blog with static content doesn't need Elastic Beanstalk. It doesn't need WAF. It doesn't need a build pipeline more complex than a 30-line GitHub Actions file.

Three certifications and years of muscle memory almost convinced me to mass over-provision a site that serves markdown files. The credentials didn't help me pick the right tool. They made it harder.
