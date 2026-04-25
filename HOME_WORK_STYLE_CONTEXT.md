# Home + Work Style Integration Context

I am working on my personal academic website, an al-folio fork hosted on GitHub Pages. I want a restrained partial redesign, not a full Portage/site-wide rebuild.

## What I Like And Want To Keep

Use these design qualities from the previous redesign:

- Warm cream background and navy/teal academic palette
- Source Serif 4 for headings
- Source Sans 3 for body text
- IBM Plex Mono for small uppercase labels/eyebrows
- Pill buttons and understated CTA buttons
- Hairline dividers
- Work rows instead of Bootstrap project cards
- The Home page organization and layout:
  - Large editorial hero
  - “Now” section
  - Selected Work rows
  - Book promo band
- The Work page organization and layout:
  - Dense, scannable rows
  - Year / title / venue / type
  - Hover highlight using a warm surface color

## Scope

Only implement:

1. Brand color/font/button styling needed for the Home and Work pages.
2. Homepage redesign in `_pages/about.md` because al-folio uses it as `/`.
3. Work page redesign in `_pages/projects.md`, ideally with permalink `/work/`.
4. Any small reusable includes needed for those two pages, such as:
   - `_includes/eyebrow.html`
   - `_includes/work-row.html`
   - `_includes/book-mock.html` or similar
5. Minimal SCSS needed to support those pages.

## Do Not Change

Do not:

- Rebrand the blog to Portage
- Change `/blog/`, RSS, feed metadata, or blog post layout
- Change About/CV page
- Change Publications/BibTeX behavior
- Delete posts, projects, news, bibliography entries, or profile images
- Remove comments infrastructure
- Remove dark mode unless required by the existing implementation
- Replace nav/footer globally unless absolutely necessary
- Generate new favicons, OG images, manifests, or social avatars
- Remove al-folio attribution or license files
- Change social handles in `_config.yml`

## Design Tokens

Use these values, preferably as CSS variables or SCSS variables without overhauling unrelated theme code:

```scss
:root {
  --global-bg-color: #f4efe4;
  --global-card-bg-color: #fbf8f1;
  --global-code-bg-color: #fbf8f1;

  --global-text-color: #1f3a52;
  --global-text-color-light: #5b7388;

  --global-theme-color: #3a7088;
  --global-hover-color: #1f3a52;
  --global-highlight-color: #3a7088;

  --global-divider-color: #e0d9c9;
}
```

Fonts:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;500;600;700&family=Source+Sans+3:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
```

Typography:

```scss
body {
  font-family: "Source Sans 3", system-ui, -apple-system, sans-serif;
}

h1,
h2,
h3,
h4,
h5,
h6,
.post-title {
  font-family: "Source Serif 4", Georgia, serif;
  font-weight: 600;
  letter-spacing: 0;
}

code,
pre,
.mono,
.eyebrow {
  font-family: "IBM Plex Mono", ui-monospace, monospace;
}

.eyebrow {
  color: var(--global-theme-color);
  font-size: 0.6875rem;
  font-weight: 500;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}
```

## Component Styles

Use this general interaction language:

```scss
.pill,
.brand-button-primary,
.brand-button-ghost {
  border-radius: 999px;
  font-weight: 500;
  transition: all 160ms ease;
}

.brand-button-primary {
  background: var(--global-hover-color);
  color: #fff !important;
  border: 1px solid var(--global-hover-color);
}

.brand-button-primary:hover {
  background: var(--global-theme-color);
  border-color: var(--global-theme-color);
}

.brand-button-ghost {
  background: transparent;
  color: var(--global-text-color) !important;
  border: 1px solid var(--global-divider-color);
}
```

Work row:

```scss
.work-list {
  border-top: 1px solid var(--global-divider-color);
}

.work-row {
  display: grid;
  grid-template-columns: 80px minmax(0, 1fr) 200px 100px;
  gap: 1.5rem;
  padding: 1rem;
  border-bottom: 1px solid var(--global-divider-color);
  color: var(--global-text-color);
  text-decoration: none;
  transition: background 160ms ease;
}

.work-row:hover {
  background: var(--global-card-bg-color);
  color: var(--global-text-color);
  text-decoration: none;
}

.work-row-title {
  font-family: "Source Serif 4", Georgia, serif;
  font-size: 1.25rem;
  font-weight: 600;
}

.work-row-meta {
  color: var(--global-text-color-light);
  font-size: 0.875rem;
}
```

Mobile:

```scss
@media (max-width: 900px) {
  .home-hero,
  .book-band-inner,
  .work-row {
    grid-template-columns: 1fr;
  }
}
```

## Homepage Content Structure

Homepage should be:

1. Hero
   - Eyebrow: `Senior Research Scientist · Google`
   - Headline: `Scalable, robust AI — plainly written.`
   - Highlight `plainly written.` in teal
   - Lead:
     `I build agentic systems that generalize — across verticals, contexts, and the long tail of problems we ask research models to handle. This is where I publish what I learn.`
   - CTAs:
     - `Read Blog →` or existing blog label
     - `About me →`

2. Now section
   - Three short paragraphs:
     - `Starting as a Senior Research Scientist at Google, working on agentic frameworks that generalize across deep research, coding, and data science.`
     - `Finishing Machine Learning for Drug Discovery with Manning — a hands-on tour of the ML that powers modern pharma, including a deep AlphaFold case study.`
     - `Teaching graduate ML + cheminformatics at UC Berkeley as an adjunct.`

3. Selected Work
   - Use WorkRow include
   - Rows can link to `/book/`, `/publications/`, `/work/`, `/teaching/`, etc.

4. Book promo band
   - Navy background
   - Book mock or existing book cover
   - CTA to Manning
   - Secondary CTA to `/book/`

## Work Page

Replace the al-folio project card grid with a simple row list.

Recommended rows:

- 2026 — Machine Learning for Drug Discovery — Manning — Book
- 2026 — GenCircuit-RL — Research — Paper
- 2026 — DreamBench — Research — Paper
- 2025 — COMPASS — Research — Paper
- 2024 — Amazon Nova Family of Models — Amazon AGI — Model
- 2024 — Designing Medicines from Scratch — PyTorch Conference — Talk
- 2022 — ML + cheminformatics teaching — UC Berkeley — Teaching

Use existing content and links where available. Do not delete `_projects/`; just stop using the card grid on the Work page.

## New Chat Prompt

Use this prompt in the fresh chat/repository session:

```md
I’m starting from the original branch of my al-folio personal academic website. Please read `HOME_WORK_STYLE_CONTEXT.md` and implement only that scoped partial redesign.

Important: I only want the color/font/button styling plus the Home page and Work page layout changes. Do not rebrand the blog, do not change RSS/feed metadata, do not rewrite post layouts, do not delete posts/projects/news/bibliography, do not change About/CV/Publications, and do not replace global nav/footer beyond minimal styling needed.

Please:
1. Inspect the current al-folio structure first.
2. Add the minimal SCSS/includes needed for the Home and Work pages.
3. Redesign `_pages/about.md` as the homepage using the specified hero, Now section, Selected Work rows, and book band.
4. Redesign `_pages/projects.md` into the Work row layout, preferably at `/work/`, without deleting `_projects/`.
5. Preserve existing config values and social handles.
6. Run `bundle exec jekyll build` if the local Ruby environment supports it.
7. Summarize exactly what changed and what was intentionally left untouched.
```