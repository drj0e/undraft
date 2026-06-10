# Blog Visual Identity & Feature Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give the blog a burnt-orange visual signature, search, a reading progress bar, /projects/ and /now/ pages, and build-time OG share cards.

**Architecture:** Hugo + PaperMod (theme is a git submodule — never edit files under `blog/themes/`). All changes go through `blog/assets/css/extended/theme.css`, override templates in `blog/layouts/`, content files in `blog/content/`, and `blog/hugo.toml`. OG cards are generated at build time with Hugo's `images.Text`/`images.Overlay` from a committed base PNG and a committed TTF font.

**Tech Stack:** Hugo extended (CI uses `latest`; `images.Text` needs ≥0.106), PaperMod, plain CSS/JS, PowerShell (one-time asset generation).

**Spec:** `docs/superpowers/specs/2026-06-09-blog-visual-identity-design.md`

**IMPORTANT — do not push.** Commit locally only. Pushing to `main` deploys the site via GitHub Actions. Task 8 ends with a user review gate: the user must approve the wording of `/projects/` and `/now/` before anything is pushed.

**Build commands (run from repo root `C:\Code\undraft`):**
- Build: `hugo -s blog --quiet` (exit 0, no output = success; writes to `blog/public/`, which is gitignored)
- Serve: `hugo -s blog server -p 1313` then open `http://localhost:1313`

---

### Task 0: Preflight

**Files:** none

- [ ] **Step 1: Verify Hugo is installed and extended**

Run: `hugo version`
Expected: output contains `extended` and version ≥ 0.120. If Hugo is missing, install with `winget install Hugo.Hugo.Extended` and re-verify.

- [ ] **Step 2: Verify clean baseline build**

Run: `hugo -s blog --quiet`
Expected: exit 0. If the baseline doesn't build, stop and report — do not proceed on a broken base.

---

### Task 1: Burnt orange accent, top bar, marker highlight, small accent moves (CSS only)

**Files:**
- Modify: `blog/assets/css/extended/theme.css`

- [ ] **Step 1: Swap the accent variables and add new ones**

In `blog/assets/css/extended/theme.css`, in the `:root` block, replace:

```css
    --accent: #5a7d8a;
```

with:

```css
    --accent: #e8501a;
    --accent-faint: rgba(232, 80, 26, 0.18);
    --accent-wash: rgba(232, 80, 26, 0.28);
```

In the `:root[data-theme="dark"]` block, replace:

```css
    --accent: #8fb8c9;
```

with:

```css
    --accent: #ff6a35;
    --accent-faint: rgba(255, 106, 53, 0.20);
    --accent-wash: rgba(255, 106, 53, 0.30);
```

- [ ] **Step 2: Add the top bar, marker highlight, and blockquote rule**

Append to the end of `blog/assets/css/extended/theme.css`:

```css
/* --- Accent top bar (the flag) --- */
body::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 6px;
    background: var(--accent);
    z-index: 999;
}

/* --- Marker highlight: one load-bearing line per post, max --- */
.post-content mark {
    background: linear-gradient(transparent 55%, var(--accent-wash) 55%);
    color: inherit;
    padding: 0 2px;
}
```

Then find the existing blockquote rule:

```css
.post-content blockquote {
    border-inline-start: none;
    background: var(--code-bg);
    padding: 28px 32px;
    margin: 32px 0;
    font-style: italic;
    font-size: 1.15rem;
    line-height: 1.6;
}
```

and change `border-inline-start: none;` to `border-inline-start: 3px solid var(--accent);`.

- [ ] **Step 3: Verify the build and visuals**

Run: `hugo -s blog --quiet`
Expected: exit 0.

Run `hugo -s blog server -p 1313`, open `http://localhost:1313`, and confirm: orange bar at the very top, orange link/tag/menu-active color throughout, blockquote in any post showing an orange left rule. Toggle dark mode and confirm the `#ff6a35` tint is used. Stop the server.

- [ ] **Step 4: Commit**

```bash
git add blog/assets/css/extended/theme.css
git commit -m "Swap accent to burnt orange, add top bar and marker highlight

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 2: Post numbers on the homepage list

**Files:**
- Create: `blog/layouts/_default/list.html` (override of `blog/themes/PaperMod/layouts/_default/list.html`)
- Modify: `blog/assets/css/extended/theme.css`

- [ ] **Step 1: Create the list template override**

Create `blog/layouts/_default/list.html` with this exact content. It is a copy of the PaperMod original with two additions, both marked `{{/* undraft */}}`: a `$total` count after the paginator, and a `№ NN` ordinal in the entry header (homepage only, newest post = highest number, stable across pagination):

```html
{{- define "main" }}

{{- if (and site.Params.profileMode.enabled .IsHome) }}
{{- partial "index_profile.html" . }}
{{- else }} {{/* if not profileMode */}}

{{- if not .IsHome | and .Title }}
<header class="page-header">
  {{- partial "breadcrumbs.html" . }}
  <h1>
    {{ .Title }}
    {{- if and (or (eq .Kind `term`) (eq .Kind `section`)) (.Param "ShowRssButtonInSectionTermList") }}
    {{- with .OutputFormats.Get "rss" }}
    <a href="{{ .RelPermalink }}" title="RSS" aria-label="RSS">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
        stroke-linecap="round" stroke-linejoin="round" height="23">
        <path d="M4 11a9 9 0 0 1 9 9" />
        <path d="M4 4a16 16 0 0 1 16 16" />
        <circle cx="5" cy="19" r="1" />
      </svg>
    </a>
    {{- end }}
    {{- end }}
  </h1>
  {{- if .Description }}
  <div class="post-description">
    {{ .Description | markdownify }}
  </div>
  {{- end }}
</header>
{{- end }}

{{- if .Content }}
<div class="post-content">
  {{- if not (.Param "disableAnchoredHeadings") }}
  {{- partial "anchored_headings.html" .Content -}}
  {{- else }}{{ .Content }}{{ end }}
</div>
{{- end }}

{{- $pages := union .RegularPages .Sections }}

{{- if .IsHome }}
{{- $pages = where site.RegularPages "Type" "in" site.Params.mainSections }}
{{- $pages = where $pages "Params.hiddenInHomeList" "!=" "true"  }}
{{- end }}

{{- $paginator := .Paginate $pages }}
{{- $total := len $pages }}{{/* undraft */}}

{{- if and .IsHome site.Params.homeInfoParams (eq $paginator.PageNumber 1) }}
{{- partial "home_info.html" . }}
{{- end }}

{{- $term := .Data.Term }}
{{- range $index, $page := $paginator.Pages }}

{{- $class := "post-entry" }}

{{- $user_preferred := or site.Params.disableSpecial1stPost site.Params.homeInfoParams }}
{{- if (and $.IsHome (eq $paginator.PageNumber 1) (eq $index 0) (not $user_preferred)) }}
{{- $class = "first-entry" }}
{{- else if $term }}
{{- $class = "post-entry tag-entry" }}
{{- end }}

<article class="{{ $class }}">
  {{- $isHidden := (.Param "cover.hiddenInList") | default (.Param "cover.hidden") | default false }}
  {{- partial "cover.html" (dict "cxt" . "IsSingle" false "isHidden" $isHidden) }}
  <header class="entry-header">
    {{- if $.IsHome }}{{/* undraft */}}
    {{- $num := sub $total (add (mul (sub $paginator.PageNumber 1) $paginator.PagerSize) $index) }}
    <span class="entry-number">№ {{ printf "%02d" $num }}</span>
    {{- end }}
    <h2 class="entry-hint-parent">
      {{- .Title }}
      {{- if .Draft }}
      <span class="entry-hint" title="Draft">
        <svg xmlns="http://www.w3.org/2000/svg" height="20" viewBox="0 -960 960 960" fill="currentColor">
          <path
            d="M160-410v-60h300v60H160Zm0-165v-60h470v60H160Zm0-165v-60h470v60H160Zm360 580v-123l221-220q9-9 20-13t22-4q12 0 23 4.5t20 13.5l37 37q9 9 13 20t4 22q0 11-4.5 22.5T862.09-380L643-160H520Zm300-263-37-37 37 37ZM580-220h38l121-122-18-19-19-18-122 121v38Zm141-141-19-18 37 37-18-19Z" />
        </svg>
      </span>
      {{- end }}
    </h2>
  </header>
  {{- if (ne (.Param "hideSummary") true) }}
  <div class="entry-content">
    <p>{{ .Summary | plainify | htmlUnescape }}{{ if .Truncated }}...{{ end }}</p>
  </div>
  {{- end }}
  {{- if not (.Param "hideMeta") }}
  <footer class="entry-footer">
    {{- partial "post_meta.html" . -}}
  </footer>
  {{- end }}
  <a class="entry-link" aria-label="post link to {{ .Title | plainify }}" href="{{ .Permalink }}"></a>
</article>
{{- end }}

{{- if gt $paginator.TotalPages 1 }}
<footer class="page-footer">
  <nav class="pagination">
    {{- if $paginator.HasPrev }}
    <a class="prev" href="{{ $paginator.Prev.URL | absURL }}">
      «&nbsp;{{ i18n "prev_page" }}&nbsp;
      {{- if (.Param "ShowPageNums") }}
      {{- sub $paginator.PageNumber 1 }}/{{ $paginator.TotalPages }}
      {{- end }}
    </a>
    {{- end }}
    {{- if $paginator.HasNext }}
    <a class="next" href="{{ $paginator.Next.URL | absURL }}">
      {{- i18n "next_page" }}&nbsp;
      {{- if (.Param "ShowPageNums") }}
      {{- add 1 $paginator.PageNumber }}/{{ $paginator.TotalPages }}
      {{- end }}&nbsp;»
    </a>
    {{- end }}
  </nav>
</footer>
{{- end }}

{{- end }}{{/* end profileMode */}}

{{- end }}{{- /* end main */ -}}
```

- [ ] **Step 2: Add the entry-number style**

Append to `blog/assets/css/extended/theme.css`:

```css
/* --- Homepage post numbers --- */
.entry-number {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 0.8rem;
    letter-spacing: 0.08em;
    color: var(--accent);
    display: block;
    margin-bottom: 6px;
}
```

- [ ] **Step 3: Verify the numbers in built output**

Run: `hugo -s blog --quiet`
Expected: exit 0.

Run: `grep -o "№ 0[0-9]" blog/public/index.html | sort -u` (or in PowerShell: `Select-String -Path blog\public\index.html -Pattern "№ 0\d" -AllMatches | ForEach-Object { $_.Matches.Value } | Sort-Object -Unique`)
Expected: `№ 01` through `№ 07`, with `№ 07` appearing first in the file (newest post, 7 published posts as of 2026-06-09). The numbers must NOT appear on `blog/public/posts/index.html` (that page is not home).

- [ ] **Step 4: Commit**

```bash
git add blog/layouts/_default/list.html blog/assets/css/extended/theme.css
git commit -m "Add numbered post ordinals to homepage list

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 3: Search

**Files:**
- Modify: `blog/hugo.toml`
- Create: `blog/content/search.md`

- [ ] **Step 1: Enable the JSON home output and add menu entries**

In `blog/hugo.toml`, add after the `enableRobotsTXT = true` line:

```toml
[outputs]
  home = ["HTML", "RSS", "JSON"]
```

Replace the whole `[menu]` block with (Projects entry is added now; its page arrives in Task 6 — the site builds fine with a menu link whose page doesn't exist yet, but Task 6 in this same plan provides it before anything ships):

```toml
[menu]
  [[menu.main]]
    name = "Posts"
    url = "/posts/"
    weight = 1
  [[menu.main]]
    name = "Projects"
    url = "/projects/"
    weight = 2
  [[menu.main]]
    name = "Tags"
    url = "/tags/"
    weight = 3
  [[menu.main]]
    name = "Search"
    url = "/search/"
    weight = 4
  [[menu.main]]
    name = "About"
    url = "/about/"
    weight = 5
```

- [ ] **Step 2: Create the search page**

Create `blog/content/search.md`:

```markdown
---
title: "Search"
layout: "search"
summary: "Search posts"
placeholder: "Search posts"
---
```

- [ ] **Step 3: Verify search works**

Run: `hugo -s blog --quiet`
Expected: exit 0, and `blog/public/index.json` exists with post entries (check: `Get-Content blog\public\index.json -TotalCount 1` shows JSON containing post titles).

Run `hugo -s blog server -p 1313`, open `http://localhost:1313/search/`, type "samples" — the data-modeling post should appear as a live result. Stop the server.

- [ ] **Step 4: Commit**

```bash
git add blog/hugo.toml blog/content/search.md
git commit -m "Enable client-side search and expand main menu

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 4: Reading progress bar

**Files:**
- Create: `blog/layouts/partials/extend_footer.html` (override; theme's version is empty)
- Modify: `blog/assets/css/extended/theme.css`

- [ ] **Step 1: Create the footer partial with the progress bar**

Create `blog/layouts/partials/extend_footer.html`. The Hugo condition limits it to post pages server-side (About and other single pages don't get it):

```html
{{- if and .IsPage (eq .Section "posts") }}
<div id="reading-progress" aria-hidden="true"></div>
<script>
    (function () {
        document.body.classList.add('has-progress');
        var bar = document.getElementById('reading-progress');
        function update() {
            var h = document.documentElement;
            var max = h.scrollHeight - h.clientHeight;
            bar.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
        }
        window.addEventListener('scroll', update, { passive: true });
        window.addEventListener('resize', update, { passive: true });
        update();
    })();
</script>
{{- end }}
```

- [ ] **Step 2: Style it — the static flag becomes the track on posts**

Append to `blog/assets/css/extended/theme.css`:

```css
/* --- Reading progress (posts only): flag fades to track, fill is full accent --- */
body.has-progress::before {
    background: var(--accent-faint);
}

#reading-progress {
    position: fixed;
    top: 0;
    left: 0;
    height: 6px;
    width: 0;
    background: var(--accent);
    z-index: 1000;
}
```

- [ ] **Step 3: Verify behavior**

Run `hugo -s blog server -p 1313`. On a post page: top bar starts as a faint orange track and fills with solid orange as you scroll to the bottom (100% width at page end). On the homepage and About: solid orange bar, no movement. Stop the server.

- [ ] **Step 4: Commit**

```bash
git add blog/layouts/partials/extend_footer.html blog/assets/css/extended/theme.css
git commit -m "Add reading progress bar on posts

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 5: /now/ page + links from About and footer

**Files:**
- Create: `blog/content/now.md`
- Modify: `blog/content/about.md`
- Modify: `blog/hugo.toml`

- [ ] **Step 1: Create the now page**

Create `blog/content/now.md`. This is a SKELETON in the user's general register, drawn from repo context. The HTML comment at the top is load-bearing — the user rewrites before push:

```markdown
---
title: "Now"
layout: "single"
summary: "What I'm working on right now."
---

<!-- USER REVIEW REQUIRED: rewrite in your own words before pushing. This is a skeleton drawn from repo context. -->

*Updated June 2026.*

Writing a series on data modeling and governance in scientific platforms. The current thread started with a question that sounds trivial and is not: "how many samples do we have?"

Iterating on Stratum, my guard pipeline for AI-generated code. The deterministic stages are stable; the interesting work right now is in what the system remembers between sessions.

Giving this blog an actual visual identity instead of a tasteful default.

Still running the 24-container homelab. Prometheus and Grafana keep me honest.
```

- [ ] **Step 2: Link from About**

In `blog/content/about.md`, append this as a new final paragraph (after the "same arguments I have." line):

```markdown
If you want the current snapshot instead of the bio, there's a [now page](/now/).
```

- [ ] **Step 3: Link from footer**

In `blog/hugo.toml`, after the existing LinkedIn `[[params.footerLinks]]` entry, add:

```toml
  [[params.footerLinks]]
    name = "Now"
    url = "/now/"
```

(No `external = true` — it's an internal link and the footer template only adds `target="_blank"` when `external` is set.)

- [ ] **Step 4: Verify**

Run: `hugo -s blog --quiet`
Expected: exit 0; `blog/public/now/index.html` exists; footer of any page contains a "Now" link; About page ends with the now-page link.

- [ ] **Step 5: Commit**

```bash
git add blog/content/now.md blog/content/about.md blog/hugo.toml
git commit -m "Add /now page, link it from About and footer

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 6: /projects/ page

**Files:**
- Create: `blog/content/projects.md`

- [ ] **Step 1: Create the projects page**

Create `blog/content/projects.md`. Stratum may be named (CLAUDE.md exception for personal projects). The description is drawn from the published posts "Who Watches the Watcher" and "The Stack Nobody Talks About" — no employer or internal references. The review comment is load-bearing:

```markdown
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
```

- [ ] **Step 2: Verify**

Run: `hugo -s blog --quiet`
Expected: exit 0; `blog/public/projects/index.html` exists; the "Projects" menu item (added in Task 3) now resolves; both internal post links work (check the hrefs exist in the built file).

- [ ] **Step 3: Commit**

```bash
git add blog/content/projects.md
git commit -m "Add projects page

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 7: Build-time OG share cards

**Files:**
- Create: `blog/assets/fonts/SpaceGrotesk-Bold.ttf` (downloaded, OFL-licensed)
- Create: `blog/assets/fonts/OFL.txt` (license)
- Create: `blog/assets/og-base.png` (generated once, committed)
- Create: `blog/assets/og-text-canvas.png` (generated once, committed)
- Create: `blog/layouts/partials/og-image.html`
- Create: `blog/layouts/partials/templates/opengraph.html` (override)
- Create: `blog/layouts/partials/templates/twitter_cards.html` (override)

- [ ] **Step 1: Download the font (with license)**

`images.Text` needs a static TTF on disk (Google Fonts CDN serves variable/woff2, which won't work). Run from repo root:

```powershell
New-Item -ItemType Directory -Force blog\assets\fonts
Invoke-WebRequest -Uri "https://github.com/floriankarsten/space-grotesk/raw/master/fonts/ttf/SpaceGrotesk-Bold.ttf" -OutFile "blog\assets\fonts\SpaceGrotesk-Bold.ttf"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/floriankarsten/space-grotesk/master/OFL.txt" -OutFile "blog\assets\fonts\OFL.txt"
```

Verify: `(Get-Item blog\assets\fonts\SpaceGrotesk-Bold.ttf).Length` is greater than 50000 (a real TTF, not an error page). If the URL 404s, fall back to downloading the family zip from https://fonts.google.com/specimen/Space+Grotesk and extracting the static Bold TTF; do not proceed with a variable font.

- [ ] **Step 2: Generate the base card and text canvas PNGs**

Run this PowerShell from repo root. It creates (a) the 1200×630 card background — paper color with a 24px burnt-orange bar baked in at the top — and (b) a 1040×400 transparent canvas the title gets rendered onto (this is how we get a right margin, since `images.Text` wraps at the canvas edge):

```powershell
Add-Type -AssemblyName System.Drawing

$bmp = New-Object System.Drawing.Bitmap(1200, 630)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.Clear([System.Drawing.ColorTranslator]::FromHtml("#f8f7f5"))
$brush = New-Object System.Drawing.SolidBrush([System.Drawing.ColorTranslator]::FromHtml("#e8501a"))
$g.FillRectangle($brush, 0, 0, 1200, 24)
$bmp.Save("blog\assets\og-base.png", [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose(); $brush.Dispose(); $bmp.Dispose()

$canvas = New-Object System.Drawing.Bitmap(1040, 400)
$canvas.Save("blog\assets\og-text-canvas.png", [System.Drawing.Imaging.ImageFormat]::Png)
$canvas.Dispose()
```

Verify both files exist and `blog\assets\og-base.png` opens as a paper-colored rectangle with an orange top bar.

- [ ] **Step 3: Create the og-image partial**

Create `blog/layouts/partials/og-image.html`. It returns a generated 1200×630 image resource for regular pages, or empty string otherwise. Title renders on the transparent canvas (so it wraps with an 80px right margin when overlaid at x=80), then both title and footer line composite onto the base:

```html
{{- $img := "" }}
{{- if .IsPage }}
{{- $base := resources.Get "og-base.png" }}
{{- $canvas := resources.Get "og-text-canvas.png" }}
{{- $font := resources.Get "fonts/SpaceGrotesk-Bold.ttf" }}
{{- if and $base $canvas $font }}
{{- $titleOpts := dict "color" "#1a1a1a" "size" 68 "linespacing" 14 "x" 0 "y" 0 "font" $font }}
{{- $text := $canvas.Filter (images.Text (.Title | plainify) $titleOpts) }}
{{- $footerOpts := dict "color" "#e8501a" "size" 30 "x" 80 "y" 540 "font" $font }}
{{- $card := $base.Filter (images.Overlay $text 80 140) (images.Text "Joe Capozzoli · josephcapozzoli.com" $footerOpts) }}
{{- $img = $card | resources.Copy (path.Join .RelPermalink "og.png") }}
{{- end }}
{{- end }}
{{- return $img }}
```

- [ ] **Step 4: Override the OpenGraph template**

Create `blog/layouts/partials/templates/opengraph.html` as an exact copy of `blog/themes/PaperMod/layouts/partials/templates/opengraph.html`, then replace this block:

```html
{{- if .Params.cover.image -}}
  {{- if (ne .Params.cover.relative true) }}
    <meta property="og:image" content="{{ .Params.cover.image | absURL }}">
  {{- else}}
    <meta property="og:image" content="{{ (path.Join .RelPermalink .Params.cover.image ) | absURL }}">
  {{- end}}
{{- else }}
  {{- with partial "_funcs/get-page-images" . }}
    {{- range . | first 6 }}
      <meta property="og:image" content="{{ .Permalink }}">
    {{- end }}
  {{- end }}
{{- end }}
```

with:

```html
{{- if .Params.cover.image -}}
  {{- if (ne .Params.cover.relative true) }}
    <meta property="og:image" content="{{ .Params.cover.image | absURL }}">
  {{- else}}
    <meta property="og:image" content="{{ (path.Join .RelPermalink .Params.cover.image ) | absURL }}">
  {{- end}}
{{- else }}
  {{- with partialCached "og-image.html" . .RelPermalink }}
    <meta property="og:image" content="{{ .Permalink }}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
  {{- end }}
{{- end }}
```

Everything else in the file stays byte-identical to the theme version.

- [ ] **Step 5: Override the Twitter card template**

Create `blog/layouts/partials/templates/twitter_cards.html` as an exact copy of the theme version, then replace this block:

```html
{{- else }}
{{- $images := partial "templates/_funcs/get-page-images" . }}
{{- with index $images 0 }}
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{{ .Permalink }}">
{{- else }}
  <meta name="twitter:card" content="summary">
{{- end }}
{{- end }}
```

with:

```html
{{- else }}
{{- with partialCached "og-image.html" . .RelPermalink }}
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{{ .Permalink }}">
{{- else }}
  <meta name="twitter:card" content="summary">
{{- end }}
{{- end }}
```

Everything else stays byte-identical to the theme version.

- [ ] **Step 6: Verify generated cards and metadata**

Note: PaperMod emits OpenGraph/Twitter metas only in production builds (`head.html` gates on `hugo.IsProduction`). A plain `hugo` build is production; `hugo server` is not. Verify against `blog/public/`, not the dev server.

Run: `hugo -s blog --quiet`
Expected: exit 0.

Check:
1. `Get-ChildItem blog\public\posts -Recurse -Filter og.png` lists one `og.png` per post (7 posts).
2. `Select-String -Path blog\public\posts\how-many-samples-do-we-have\index.html -Pattern "og:image"` shows a `<meta property="og:image" content="https://josephcapozzoli.com/posts/how-many-samples-do-we-have/og.png">` line plus width/height metas, and `twitter:card` is `summary_large_image`.
3. Open `blog\public\posts\how-many-samples-do-we-have\og.png` (Read tool can render PNGs): paper background, orange top bar, title in Space Grotesk wrapping inside the margins, orange byline bottom-left. If the title overflows or collides with the byline, adjust `size`/`y` values in `og-image.html` and rebuild until clean — check the longest title ("The Step Between the Catalog and the Vector") too.

- [ ] **Step 7: Commit**

```bash
git add blog/assets/fonts blog/assets/og-base.png blog/assets/og-text-canvas.png blog/layouts/partials/og-image.html blog/layouts/partials/templates/opengraph.html blog/layouts/partials/templates/twitter_cards.html
git commit -m "Generate OG share cards at build time

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 8: Full verification and user review gate

**Files:** none

- [ ] **Step 1: Clean full build**

Run: `hugo -s blog --quiet`
Expected: exit 0, no warnings about missing templates or resources.

- [ ] **Step 2: Visual sweep**

Run `hugo -s blog server -p 1313` and check, in light AND dark mode:
- Homepage: orange top bar, `№` numbers newest-first, menu shows Posts / Projects / Tags / Search / About
- A post: progress bar fills on scroll, blockquote rule, link color
- `/search/`: live results
- `/projects/` and `/now/`: render, footer "Now" link works, About links to /now
Stop the server.

- [ ] **Step 3: Report to user — DO NOT PUSH**

Everything is committed locally. Tell the user:
1. `/now/` and `/projects/` contain drafted text marked with `USER REVIEW REQUIRED` comments — they must rewrite/approve the words (Undraft voice rules) before pushing.
2. The marker highlight (`<mark>`) is live but unused — applying it to one load-bearing line per existing post is their editorial call.
3. Once they approve content, `git push` deploys everything via GitHub Actions.
