# Blog Visual Identity & Feature Upgrade — Design

**Date:** 2026-06-09
**Status:** Approved
**Scope:** The public blog at josephcapozzoli.com (Hugo + PaperMod, `blog/` directory)

## Problem

The blog has taste but no signature. The current design (warm paper, Newsreader serif, Space Grotesk headings, thin gray rules, muted slate accent used only on hovers and tags) is the default look of a customized PaperMod blog. Nothing is oversized, nothing moves, no graphic device exists. The user's verdict: "style but flat."

## Decision

Commit to one loud move (a hot accent color used with intent) plus a small set of reader features and content surfaces. Direction chosen from three mockup candidates ("Loud Type," "Hot Accent," "The Broadsheet"): **Hot Accent**. Color chosen from four candidates shown in light and dark mode: **burnt orange**, on a try-and-see basis (it is a CSS variable swap to change later).

## 1. Visual identity — burnt orange signature

Replace the accent color and apply it deliberately. Everything not listed stays as-is.

- **Accent values:** `--accent: #e8501a` (light mode), `--accent: #ff6a35` (dark mode, tinted to avoid vibrating on near-black). Defined in `blog/assets/css/extended/theme.css`.
- **Top bar:** a 6px accent-colored bar across the very top of every page. Implemented in CSS (e.g., `body::before` fixed strip).
- **Post numbers:** homepage/post-list entries get a `№ NN` ordinal in Space Grotesk, accent-colored, newest post = highest number. Computed in a Hugo template override from the post's position in the date-ordered list of all posts, so numbers are stable and never manually maintained.
- **Marker highlight:** a styled `<mark>` element rendering as a hand-swiped accent underlay (transparent top half, ~25% accent bottom half via linear-gradient background). Usage rule: at most one highlighted sentence per post — the load-bearing line. Applied manually in post markdown.
- **Small accent moves:** active menu item, tag labels, blockquote rule, and link underlines inherit the new accent. Most of these already reference `--accent` and need no structural change.

## 2. Reader features

- **Search:** enable PaperMod's built-in client-side fuzzy search (Fuse.js). Requires: `outputs` config for home JSON in `hugo.toml`, a `blog/content/search.md` page with `layout: search`, and a Search menu entry.
- **Reading progress bar:** a thin accent-colored bar at the top of the viewport that fills with scroll progress. Posts (single pages) only. Small JS + CSS added via the existing `extend_head.html` partial. Visually it merges with the static top bar: the flag fills as the reader progresses.

## 3. Content surfaces

- **/projects/ page:** a home for things the user builds. First entry: Stratum (a personal project, explicitly cleared for public reference by name per CLAUDE.md). Each entry: name, one-paragraph description in the user's voice, status, link. Gets a "Projects" item in the main menu.
- **/now/ page:** a dated snapshot of current work and thinking (nownownow.com pattern). A skeleton draft is generated from repo context; **the user must rewrite/approve the words before it ships** (Undraft voice rules apply). Linked from the About page and footer, not the main menu. Final main menu: Posts, Projects, Tags, Search, About.

## 4. Social preview cards (OG images)

Auto-generated at build time using Hugo's native `images.Text` — no external services, no per-post manual work.

- **Card:** 1200×630. Paper background (`#f8f7f5`), burnt-orange bar, post title in Space Grotesk, author name + domain small in a corner.
- **Font:** a Space Grotesk TTF must be added to `blog/assets/` for `images.Text` to use.
- **Wiring:** generated image URL emitted in OpenGraph and Twitter Card meta via a partial override, replacing the current imageless share preview. Posts with an explicit `cover` image (none currently) would keep their own.
- This un-defers the previously parked "social preview images" decision.

## Out of scope (deliberate)

Analytics, newsletter, RSS changes, related posts, code block styling, post series grouping, homepage layout restructuring (the "Front Page" / "Index" / "Broadsheet" directions). All addable later without touching this work.

## Constraints

- Theme is a git submodule (`blog/themes/PaperMod`) — never edit theme files directly; all changes go through `blog/assets/css/extended/`, `blog/layouts/` overrides, and `hugo.toml`.
- All content in this repo is public; employer-reference rules in CLAUDE.md apply to the /now and /projects pages.
- Site deploys via GitHub Pages; OG image generation must work in the existing GitHub Actions Hugo build (needs Hugo extended version that supports `images.Text`, available since v0.106).

## Testing

- `hugo build` locally; verify no template errors and OG images appear in `public/`.
- Visual check of homepage, a post page, search page, /projects/, /now/ in light and dark mode via `hugo server`.
- Validate one generated OG card renders correctly (open the PNG from `public/`).
- Check share metadata with a card validator (or by inspecting `<meta property="og:image">` in built HTML).
