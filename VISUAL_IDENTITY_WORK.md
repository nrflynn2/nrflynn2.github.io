# Visual Identity & UX Work — Session Summary

This document summarizes the visual identity work completed on noahrflynn.com, including rationales behind each decision, so revisions can build on or diverge from these choices.

## Context

- **Site**: Jekyll + al-folio theme at noahrflynn.com
- **Owner**: Noah Flynn — Applied Scientist at AWS AI Labs, author of *Machine Learning for Drug Discovery*, adjunct faculty at UC Berkeley
- **Audience**: Academic peers, industry/recruiters, students — weighted equally
- **Aesthetic target**: Warm & approachable with technical polish
- **Color palette** (unchanged): Teal primary (`#0d9488` light / `#14b8a6` dark) + Amber accent (`#d97706` / `#f59e0b`)
- **Content cadence**: Moderate (~monthly updates planned)

## Priorities (approved order)

1. Custom favicon/logo — lowest risk, immediate brand impact
2. Homepage hero redesign — highest visual impact
3. Custom OG/social images — extends brand to social platforms

Deferred to a later phase (once regular content creation begins):
- Link-in-bio / social hub (e.g., `/links/` page, more platforms, footer social icons)
- Content expansion (`/now/`, `/talks/`, projects revival, reading list, "start here" narrative)
- Engagement & growth (newsletter activation, Giscus comments, analytics, email capture on book page, cross-posting)

---

## 1. Custom Favicon — Molecular Graph Mark

### Decision

A **stylized molecular/GNN graph** (not a monogram or hexagon) — 6 teal circles connected by 7 edges, asymmetric but balanced composition.

### Files created
- `assets/img/favicon.svg` — hand-authored SVG, transparent background, teal nodes/edges at `#0d9488` (darker) and `#14b8a6` (lighter) for subtle two-tone depth
- `assets/img/apple-touch-icon.png` (180×180) — rendered over a white background for iOS home-screen legibility
- `assets/img/favicon-32x32.png` and `assets/img/favicon-16x16.png` — transparent PNG fallbacks

### Files modified
- `_config.yml` line 15: `icon: ⚛️` → `icon: favicon.svg`
- `_includes/head.liquid` lines 60-67: replaced single `<link rel="shortcut icon">` with four `<link>` tags (SVG + 32×32 + 16×16 + apple-touch-icon)

### Rationale

- **Molecular graph over NF monogram**: The user explicitly chose the abstract molecular mark. It ties directly to Noah's computational biology / GNN work, making it topically distinctive. Initials are interchangeable; a molecular motif is professionally signature.
- **Two-tone teal nodes**: Uses the same light/dark teal tokens already in the site palette (`#0d9488` and `#14b8a6`), creating visual depth without adding a new color.
- **Asymmetric graph**: Organic/balanced composition (rather than a perfectly symmetric hexagon or benzene ring) avoids looking like a generic chemistry icon. Reads as "graph neural network" more than "chemistry class."
- **Transparent background for browser favicon, white for Apple**: Browser tabs often have dark/light themes, so transparency lets the mark adapt. iOS home-screen icons cannot be transparent, so the apple-touch-icon has an explicit white background.
- **SVG primary, PNG fallbacks**: SVG favicons are crisp at every size in modern browsers. PNG fallbacks cover older browsers and Apple devices.

### Generation approach

No ImageMagick / Cairo was available on the system, so PNG rasters were generated using **Pillow** drawing primitives directly (circles + lines) rather than rasterizing the SVG. This made the process dependency-light and kept the generation logic inline with the SVG geometry.

### Potential revisions to consider
- Try a monogram or hexagon variant to compare
- Explore different node counts (3, 4, 8 nodes) or layouts (tree, ring, path)
- Add subtle animation to the SVG (pulsing nodes) for a loading-screen variant
- Consider a single-color (flat teal) version for minimal contexts

---

## 2. Homepage Hero Redesign

### Decision

Replace the al-folio float-based profile layout with a **Bootstrap grid two-column hero**. Desktop: name/subtitle/bio/social on the left (col-md-7), circular profile photo on the right (col-md-5). Mobile: photo on top, text below, center-aligned. Teal accent divider separates hero from book feature card.

### Files modified
- `_layouts/about.liquid` — full restructure of the hero (lines 1-50 of new file). Wrapped hero in `<div class="hero-section row align-items-center">`; moved book-feature include from markdown content into the layout, below a `<hr class="hero-divider">`
- `_pages/about.md` — removed `{% include book-feature.html %}` (now in layout)
- `_sass/_themes.scss` — added `.hero-section`, `.hero-title`, `.hero-subtitle`, `.hero-bio`, `.hero-social`, `.hero-profile-col`, `.hero-divider`, `@keyframes fadeInUp`, and mobile overrides

### Design choices (desktop ≥768px)

```
┌─────────────────────────────────┬──────────────────┐
│  NOAH FLYNN                     │                  │
│  Applied Scientist, AWS AI Labs │   ┌──────────┐   │
│                                 │   │ circular │   │
│  Bio paragraph...               │   │ profile  │   │
│                                 │   │  photo   │   │
│  [social icons row]             │   └──────────┘   │
└─────────────────────────────────┴──────────────────┘
│ ── teal accent divider ──────────────────────────── │
│  [Book Feature Card]                                │
```

### Mobile (<768px)
Profile photo stacks on top (centered, max 220px wide), then name, subtitle, bio, social icons — all center-aligned.

### Rationale

- **Grid over float**: The al-folio default floats the profile image and wraps text around it. This produces reflow artifacts and makes the bio text compete with the image. A clean two-column grid separates concerns and is easier to style predictably.
- **Name at 2.5rem with tight letter-spacing (-0.02em)**: Larger and tighter than the al-folio default. "Warm & approachable" does not mean small/timid — a confident name signals authority while the rest of the page provides warmth.
- **Subtitle in secondary text color**: Uses `var(--global-text-color-light)` so "Applied Scientist, AWS AI Labs" is clearly secondary to the name. Creates hierarchy.
- **Social icons in hero + at page bottom**: User explicitly chose "both places." Hero placement makes socials discoverable without scroll; bottom placement is conventional and provides a second path.
- **fadeInUp animation (400ms, 10px translate, staggered 0.1s/0.2s delays)**: Subtle enough to be technical polish, not flashy. Only applied to bio content and social icons (not name/title) so the page never feels like it's "assembling."
- **Teal accent divider (3px border-top)**: Provides a branded visual break between hero and content. Uses `var(--global-theme-color)` so it automatically adapts to dark mode.
- **Profile photo max-width 220px**: The al-folio default (`width: 22%`) scales strangely on wide viewports. A fixed max keeps the photo prominent without overwhelming the name.
- **Book feature moved into layout**: The book is a first-class part of Noah's identity right now (actively promoting MEAP). Moving it from markdown content into the layout guarantees it always renders in the right place, and simplifies `about.md` to pure bio prose.
- **Mobile: photo on top**: Conventional for portrait-oriented landing pages. Users scan top-to-bottom on mobile; a face immediately creates connection before they read anything.

### Potential revisions to consider
- Try a full-width hero with background imagery (teal gradient or subtle pattern)
- Test a single-column centered layout on desktop (more "link-in-bio" feel)
- Experiment with a "featured" card slot in the hero (latest talk, news item, pinned blog post)
- Reduce name size if it feels too large in context
- Try an asymmetric layout (60/40 split or offset profile photo)
- Remove the fade animation if it feels unnecessary
- Add a subtle hover state on the profile photo (tilt, scale, ring) for playfulness

---

## 3. Custom OG/Social Sharing Images

### Decision

Three static 1200×630 PNG images with a consistent design system: left-to-right teal gradient background, white text, molecular graph mark in top-right corner, site URL in bottom-left. Generated via reproducible Python/Pillow script.

### Files created
- `assets/img/og/default.png` — site-wide fallback: "Noah Flynn" + subtitle + "Author of Machine Learning for Drug Discovery" + circular profile photo
- `assets/img/og/book.png` — book page: Manning book cover (left) + title + subtitle + author name
- `assets/img/og/publications.png` — publications page: "Publications" + name + "ML for drug discovery, NLU, foundation models" + molecular mark background pattern (3 marks at different sizes)
- `scripts/generate_og_images.py` — Pillow generation script (reproducible, version-controlled)
- `assets/img/book_cover_manning.png` — downloaded Manning MEAP cover art, used by the book OG image

### Files modified
- `_config.yml` line 65: `og_image: https://noahrflynn.com/assets/img/og/default.png` (absolute URL, as required by OG tags)
- `_pages/book.md` front matter: added `og_image: https://noahrflynn.com/assets/img/og/book.png`
- `_pages/publications.md` front matter: added `og_image: https://noahrflynn.com/assets/img/og/publications.png`
- `_includes/metadata.liquid` line 67: `twitter:card` content changed from `summary` → `summary_large_image` for full 1200×630 Twitter/X previews

### Design system (shared across all OG images)
- **Background**: Left-to-right teal gradient, `#0a645f` → `#14b8a6`
- **Primary text**: White (`#ffffff`), DejaVu Sans Bold at 42-56px
- **Secondary text**: White at 70% alpha, DejaVu Sans Regular at 22-28px
- **Molecular mark**: White at 70% alpha, top-right corner (scale 2.5x of favicon)
- **URL footer**: Bottom-left corner in white-dim, 22px regular
- **Text left margin**: 80px from image edge

### Rationale

- **Static images over dynamic generation**: Jekyll is a static site — no server to render images on demand. Dynamic OG generation (Vercel functions, GitHub Actions) adds infrastructure disproportionate to a small number of key pages. Static + reproducible script is the right tradeoff.
- **Python/Pillow script over Figma/Canva**: Version-controllable, re-runnable, programmatic consistency across images. Designers would favor Canva; engineers want it in code. The script also documents the design system implicitly.
- **Teal gradient background**: Uses the same palette as the site, creating continuity between the website and social previews. A left-to-right gradient (darker on left) adds visual depth where the primary text lives.
- **Molecular mark in corner**: Ties OG images to the favicon/brand. Subtle (white at 70% alpha) so it doesn't compete with content.
- **Per-page imagery**: Default image is the site-wide fallback. Book page features the actual book cover. Publications uses a pattern of molecular marks to signal "research."
- **Only 3 pages with custom OG images**: Book, publications, and site-wide default are highest-value. Blog posts can inherit the default for now; per-post OG images can be added later as a separate system (e.g., GitHub Action that generates OG images from post titles).
- **`summary_large_image` card**: Twitter/X "summary" cards are small square thumbnails. "summary_large_image" displays the full 1200×630, which is what all the work was done for.
- **Absolute URLs in front matter**: OG tags require absolute URLs; social platforms won't resolve relative paths. All `og_image` values use `https://noahrflynn.com/...`.

### Potential revisions to consider
- **Alternative background styles**: solid teal, radial gradient, pattern overlay, photo-background with overlay
- **Amber accent usage**: currently 100% teal — could incorporate the amber accent color to add warmth and match the site's secondary color
- **Alternative typography**: try Inter or a serif for more warmth; DejaVu was chosen because it's universally available
- **Per-blog-post OG images**: automate generation from post titles via GitHub Action
- **Author photo in more images**: consider adding the circular profile photo to the publications OG card
- **Light variant**: currently all dark-teal backgrounds. A light/cream variant could work for different contexts.

---

## Non-obvious implementation notes

- **ImageMagick was unavailable** on the dev machine, and cairosvg/svglib both require the Cairo C library (also missing). PNG favicon rasters were drawn with Pillow primitives directly from the SVG geometry (coordinates matched 1:1). This is why favicon PNGs and OG images share a Python/Pillow toolchain rather than an SVG-rasterization pipeline.
- **`book_cover.jpg`** in `assets/img/` is a 1×1 placeholder, not the actual book cover. The real Manning MEAP cover is fetched at render-time via external URL in `_includes/book-feature.html`. For the OG image, the cover was downloaded and saved as `book_cover_manning.png` so the script has a local source.
- **`.venv/`** was created via `uv venv` to install Pillow (matches the user's global "use UV for Python" preference).
- **Hero layout & al-folio upgrades**: Modifying `_layouts/about.liquid` means future al-folio theme updates may conflict with the new hero. Acceptable because the site already has multiple customizations (`_themes.scss`, `book-feature.html`).

---

## File inventory — new or modified

### Created
- `assets/img/favicon.svg`
- `assets/img/favicon-16x16.png`
- `assets/img/favicon-32x32.png`
- `assets/img/apple-touch-icon.png`
- `assets/img/book_cover_manning.png` (generation asset)
- `assets/img/og/default.png`
- `assets/img/og/book.png`
- `assets/img/og/publications.png`
- `scripts/generate_og_images.py`

### Modified
- `_config.yml` (favicon path, og_image)
- `_includes/head.liquid` (favicon link tags)
- `_includes/metadata.liquid` (twitter card type)
- `_layouts/about.liquid` (hero restructure, book feature moved in)
- `_pages/about.md` (removed book-feature include)
- `_pages/book.md` (added og_image front matter)
- `_pages/publications.md` (added og_image front matter)
- `_sass/_themes.scss` (hero styles, animation, mobile overrides)

---

## Verification checklist

1. **Favicon**: `docker-compose up`, open localhost:8080, verify mark shows in browser tab at multiple zoom levels. Test Chrome, Firefox, Safari.
2. **Hero**: Test at 1440px, 1024px, 768px, 375px viewport widths. Toggle dark mode. Confirm social icons appear both in hero and at page bottom. Confirm book feature card renders below teal divider.
3. **OG images**: Deploy, then paste URLs into [Twitter Card Validator](https://cards-dev.twitter.com/validator) and [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/). Verify large 1200×630 cards display.
4. **Regression**: Check blog, teaching, CV pages are unchanged.
