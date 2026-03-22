# Undraft Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Get the Undraft translation engine working in a Claude Project and a Hugo blog deployed to GitHub Pages with a custom domain, producing the first published post.

**Architecture:** System prompt in a Claude Project handles translation. Blog is a Hugo static site deployed via GitHub Pages. Repo tracks prompt versions, friction patterns, and blog content. No application code — the prompt is the product.

**Tech Stack:** Claude Project (translation engine), Hugo (static site generator), GitHub Pages (hosting), Git (version control)

---

**Prerequisites:** Git, GitHub CLI (`gh`), and a package manager (winget, choco, or scoop) are installed. `gh auth login` has been completed. Blog content lives in the same repo as the prompt and design docs (under `blog/`).

---

## Phase 1: Translation Engine

Phase 1 and Phase 2 run in parallel. Buy the domain (Task 5) during Week 1 while you're testing the prompt. Don't wait for Phase 1 to finish before starting Phase 2.

### Task 1: Initialize the repo

**Files:**
- Create: `.gitignore`
- Existing: `README.md`, `claude.md`, `undraft design.md`, `undraft-system-prompt.md`

- [ ] **Step 1: Initialize git repo**

```bash
cd undraft
git init
```

- [ ] **Step 2: Create .gitignore**

```
# Hugo build output
public/
resources/_gen/

# OS files
.DS_Store
Thumbs.db
desktop.ini

# Editor files
*.swp
*.swo
*~
.vscode/
.idea/

# Hugo local server
hugo_stats.json
```

- [ ] **Step 3: Stage and commit all existing files**

```bash
git add .gitignore README.md claude.md "undraft design.md" undraft-system-prompt.md
git commit -m "Initial commit: design docs, system prompt, and README"
```

---

### Task 2: Create the friction patterns scratch file

**Files:**
- Create: `friction-patterns.md`

- [ ] **Step 1: Create friction-patterns.md**

```markdown
# Friction Patterns

Track recurring patterns from the Friction Report across inputs. When a pattern shows up more than once, log it here with the date and a short example. By end of Phase 1, the top 3-5 recurring habits should be identified.

This file serves two purposes:
1. Self-improvement data — makes you aware of your defaults
2. Future blog material — "the five ways I consistently undermine my own writing"

## Patterns

| Pattern | Category | Count | First Seen | Example |
|---------|----------|-------|------------|---------|
| | | | | |

## Top Recurring Habits (fill in after 10+ inputs)

1.
2.
3.
4.
5.
```

- [ ] **Step 2: Commit**

```bash
git add friction-patterns.md
git commit -m "Add friction patterns tracking file for Phase 1"
```

---

### Task 3: Set up the Claude Project

This task is manual — it happens in the Claude web UI, not in code.

- [ ] **Step 1: Create a new Claude Project**

Go to [claude.ai](https://claude.ai). Create a new project called "Undraft".

- [ ] **Step 2: Paste the system prompt**

Open `undraft-system-prompt.md`. Copy everything below the first `---` line (starting from "You are Undraft, a personal communication tool..."). Paste it into the project's system prompt field (Project Instructions).

- [ ] **Step 3: Add the voice rules**

Open `claude.md`. Copy the full contents. Append it to the system prompt after the content from the previous step (below a `---` separator). Do not use project knowledge/uploaded documents for this — it needs to be in the system prompt for reliable instruction-following.

- [ ] **Step 4: Test with a throwaway input**

Paste something short and low-stakes — a recent Slack message or a quick observation about a technical decision. Verify you get back Core Point, Up, Peers, and Friction Report sections. Don't worry about quality yet — just confirm the structure is right.

---

### Task 4: Run 10+ real inputs and iterate the prompt

This task is the core of Phase 1. It happens over days, not in one sitting.

- [ ] **Step 1: Collect real inputs**

Over the next 1-2 weeks, paste real inputs into the Undraft Claude Project as they come up. Prioritize:
- Architecture decisions or technical tradeoffs you need to explain
- Things you just figured out or learned
- Post-meeting notes or frustrations
- Status updates going to leadership

Aim for at least 10 real inputs.

- [ ] **Step 2: Evaluate each output**

For each input, check:
- Does the Core Point nail what you meant?
- Would you send the Up version to your boss without cringing?
- Would your peers respect the Peers version?
- Does the Friction Report catch real patterns (not just noise)?
- Does either output sound like AI wrote it? Check against the kill list in `claude.md`.

- [ ] **Step 3: Log friction patterns**

After each Friction Report, update `friction-patterns.md`. If a category (defensive, self-erasing, vague, etc.) shows up more than once, increment the count and add an example.

- [ ] **Step 4: Iterate the system prompt**

When output is wrong, fix it in the prompt. Common issues to watch for:
- Up version sounds too corporate → tighten the "no corporate sludge" rules
- Peers version loses technical depth → add more "keep" rules
- Friction Report is too noisy → adjust sensitivity
- Output is too long for short inputs → reinforce the "match weight" rule

Make edits in `undraft-system-prompt.md` in the repo first, then paste into the Claude Project. This keeps version history.

- [ ] **Step 5: Commit prompt iterations**

After each meaningful prompt change:

```bash
git add undraft-system-prompt.md
git commit -m "Tune prompt: [what you changed and why]"
```

- [ ] **Step 6: Check the success gate**

After 10+ inputs:
- Do outputs consistently pass the "would I send this" test for Up?
- Do outputs consistently pass the "would my peers respect this" test for Peers?
- Are the top 3-5 friction patterns identified in `friction-patterns.md`?

If yes, Phase 1 is done. If no, keep iterating.

- [ ] **Step 7: Commit final friction patterns**

```bash
git add friction-patterns.md
git commit -m "Phase 1 complete: top friction patterns identified"
```

---

## Phase 2: Blog + First Post

### Task 5: Buy the domain

- [ ] **Step 1: Pick and buy a domain**

Pick a domain name. Keep it simple — your name, a short brand, whatever you'll stick with. Buy it from a registrar (Namecheap, Cloudflare, Squarespace — doesn't matter). $12/year.

Do this during Week 1, while you're still testing the prompt in Phase 1. The spec says "buy a custom domain in week 1" and means it.

Don't overthink this. You can always add a better domain later. The point is having one.

- [ ] **Step 2: Note the domain for DNS setup later**

You'll configure DNS to point at GitHub Pages in Task 7. For now, just have the domain purchased and accessible in your registrar's dashboard.

---

### Task 6: Set up Hugo blog

**Files:**
- Create: Hugo site structure under `blog/` in the repo

- [ ] **Step 1: Install Hugo**

```bash
# Verify the package ID first
winget search hugo
# Then install (package ID may vary — check the search results)
winget install Hugo.Hugo.Extended
# or: choco install hugo-extended
# or: scoop install hugo-extended
```

Verify:
```bash
hugo version
```

Expected: version string with "extended" in it.

- [ ] **Step 2: Create Hugo site in the repo**

```bash
cd undraft
hugo new site blog
```

This creates a `blog/` directory with the Hugo structure.

- [ ] **Step 3: Pick and install a theme**

Use a clean, readable theme. PaperMod is a good default — fast, minimal, good typography.

```bash
cd blog
git submodule add https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
```

- [ ] **Step 4: Configure hugo.toml**

Replace `blog/hugo.toml` with:

```toml
baseURL = "https://YOURDOMAIN.com/"
languageCode = "en-us"
title = "Joe Capozzoli"
theme = "PaperMod"

[params]
  author = "Joe Capozzoli"
  description = "Architecture, AI, and the things that actually happen when you build enterprise software."
  ShowReadingTime = true
  ShowPostNavLinks = true
  ShowCodeCopyButtons = true

[params.homeInfoParams]
  Title = "Joe Capozzoli"
  Content = "Lead Enterprise Architect. Writing about architecture decisions, production AI, and what I'm learning along the way."

[menu]
  [[menu.main]]
    name = "Posts"
    url = "/posts/"
    weight = 1
  [[menu.main]]
    name = "About"
    url = "/about/"
    weight = 2
```

Replace `YOURDOMAIN.com` with your actual domain.

- [ ] **Step 5: Test locally**

```bash
cd blog
hugo server -D
```

Open `http://localhost:1313` in a browser. Verify the site loads with the theme applied.

- [ ] **Step 6: Commit**

```bash
cd undraft
git add blog/
git commit -m "Set up Hugo blog with PaperMod theme"
```

---

### Task 7: Deploy to GitHub Pages

- [ ] **Step 1: Create GitHub repo**

```bash
cd undraft
gh repo create undraft --private --source=. --push
```

(Make it private initially. You can make it public later if you want to open-source the prompt work.)

- [ ] **Step 2: Create GitHub Actions workflow for Hugo**

Create `.github/workflows/hugo.yml`:

```yaml
name: Deploy Hugo site to Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

defaults:
  run:
    working-directory: ./blog

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: recursive
          fetch-depth: 0
      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v3
        with:
          hugo-version: "latest"
          extended: true
      - name: Build
        run: hugo --minify
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./blog/public

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

- [ ] **Step 3: Enable GitHub Pages**

Go to the GitHub repo Settings > Pages. Set source to "GitHub Actions".

- [ ] **Step 4: Configure custom domain**

In your registrar's DNS settings, add:
- A CNAME record: `www` pointing to `YOUR_GITHUB_USERNAME.github.io`
- Four A records pointing to GitHub's IPs:
  ```
  185.199.108.153
  185.199.109.153
  185.199.110.153
  185.199.111.153
  ```

Create `blog/static/CNAME`:
```
YOURDOMAIN.com
```

In GitHub repo Settings > Pages, enter your custom domain and enable "Enforce HTTPS".

- [ ] **Step 5: Commit and push**

```bash
cd undraft
git add .github/ blog/static/CNAME
git commit -m "Add GitHub Actions deploy workflow and custom domain"
git push
```

- [ ] **Step 6: Verify deployment**

Wait for the GitHub Actions workflow to complete:
```bash
gh run list --limit 1
```

Visit your domain in a browser. Verify the Hugo site loads.

---

### Task 8: Publish the first post

**Files:**
- Create: `blog/content/posts/<your-topic-slug>.md` (replace with actual topic)

- [ ] **Step 1: Pick the best Phase 1 output**

Review your Undraft outputs from Phase 1. Pick the one that has the strongest public point — an architecture tradeoff, something you learned, a decision you made and why. The Peers version is your starting draft.

- [ ] **Step 2: Create the post**

```bash
cd blog
hugo new posts/your-post-title.md
```

This creates the file with Hugo frontmatter. Edit it:

```markdown
---
title: "Your Actual Title"
date: 2026-03-XX
draft: false
tags: ["architecture", "whatever-fits"]
---

[Paste your Peers output here. Edit it. Make it yours. The bot drafts, you own the final voice.]
```

- [ ] **Step 3: Preview locally**

```bash
cd blog
hugo server
```

Check `http://localhost:1313`. Read the post. Does it sound like you? Would you put your name on it?

- [ ] **Step 4: Commit and deploy**

```bash
cd undraft
git add blog/content/posts/
git commit -m "Publish first post: [topic]"
git push
```

- [ ] **Step 5: Cross-post to LinkedIn**

Go to LinkedIn. Write a short intro (2-3 sentences about what the post covers and why you wrote it). Link to the blog post. Post it.

This is manual. Don't automate this yet.

- [ ] **Step 6: Check the Phase 2 success gate**

- Blog is live on a custom domain? ✓/✗
- One post is published? ✓/✗
- LinkedIn has a link to it? ✓/✗

---

## Phase 3: The Flywheel

### Task 9: Establish the rhythm

Phase 3 is not a build task — it's a habit task. There's nothing to deploy. The work is using Undraft daily and publishing regularly.

- [ ] **Step 1: Set up the daily dump habit**

Bookmark the Undraft Claude Project. When a meeting ends, when you figure something out, when you make a tradeoff — paste the raw thought in. 5-10 minutes. Don't edit. Don't polish. Dump and go.

- [ ] **Step 2: Start mid-week deliberate writing sessions**

2-3 times per week, spend 30 minutes on something deliberate. A Viva Engage post, an architecture rationale, a response to a leadership question. This is different from the daily dump — you're writing for a specific audience and purpose, using Undraft to get there faster.

- [ ] **Step 3: Start weekly Viva Engage posts**

Pick a day (e.g., Friday). Take one of the week's Up or Peers outputs — whichever fits the internal audience — and post it to Viva Engage. Even 3-4 paragraphs counts. Consistency matters more than length.

- [ ] **Step 4: Run the weekend review**

Every weekend (or whenever you have an hour), review the week's Undraft outputs. Ask:
- Did any of these have a public point?
- Is there a post in here?

If yes, feed the raw input back through Undraft, take the Peers output, edit it into a blog post, publish.

If no, that's fine. Not every week produces a post.

- [ ] **Step 5: Get a peer review**

By mid-Phase 3 (around week 4-5), share a draft with 1-2 people you trust before publishing. Not for approval — for calibration. Ask: "Does this land the way I think it does? Am I missing context that's obvious to me?"

- [ ] **Step 6: Survive a gap**

When the heavy work week hits and writing doesn't happen — and it will — the recovery protocol is: do one raw dump. Not a blog post. One dump into Undraft. That's the flywheel restarting.

- [ ] **Step 7: Check the Phase 3 success gate**

- Published 3-4 blog posts? ✓/✗
- Recovered from at least one week where writing didn't happen? ✓/✗
- Weekly Viva Engage posts happening? ✓/✗
- At least one draft reviewed by a trusted peer before publishing? ✓/✗

---

## Phase 4: Evaluate and Adapt

### Task 10: Identify and address the bottleneck

- [ ] **Step 1: Diagnose**

At week 6, ask yourself:
- Is the bottleneck publishing mechanics? (Drafts exist but getting them onto the blog is annoying.)
- Is the bottleneck content generation? (Not enough raw material, or the prompt isn't producing usable output.)
- Is there no bottleneck? (System is working.)

- [ ] **Step 2: Act on the diagnosis**

If publishing mechanics: automate. Move the workflow to Claude Code, set up automated deploys, add cross-posting scripts.

If content generation: go back to the prompt. Tune it. Test more input types. Make the Friction Report sharper.

If no bottleneck: leave it alone.

- [ ] **Step 3: Self-assessment**

Are you catching your own patterns before the Friction Report flags them? If yes, the tool is training you. If no, either the Friction Report needs to be sharper or you need to read it more carefully. Review `friction-patterns.md` — are the top patterns still showing up at the same rate, or are you self-correcting?

- [ ] **Step 4: Evaluate audience tier decisions**

- Does Lobby need to become a default tier? (Have you been requesting it frequently?)
- Does Peers voice work for external/blog audiences, or does a distinct Blog/Public tier need to exist?
- Should any new tiers be added?

- [ ] **Step 5: Update the system prompt and design doc**

Commit whatever changes Phase 4 produces:

```bash
git add undraft-system-prompt.md "undraft design.md"
git commit -m "Phase 4: [what changed and why]"
git push
```

- [ ] **Step 6: Check the Phase 4 success gate**

- The actual bottleneck has been identified and addressed? ✓/✗
- Publishing friction is low enough that the constraint is "do I have something worth saying" not "how do I get it out there"? ✓/✗
