# Website Implementation Spec — FINAL DECISIONS

**For:** nrflynn2/nrflynn2.github.io (al-folio on GitHub Pages)
**Finalized:** March 2026

---

## Navigation Bar

```
Blog | Book | Publications | Teaching | CV
```

- al-folio site title ("Noah Flynn") on the far left serves as the home link
- Talks are a section within the CV page (promote to own nav item at 4+ talks)
- 5 items total — clean on desktop, collapses to hamburger on mobile

---

## Homepage Bio Copy

Use this as the `about` section on the homepage (the al-folio `_pages/about.md` file):

> I build AI systems at Amazon AWS AI Labs and wrote the textbook on machine learning for drug discovery. My day job is multi-agent frameworks and foundation models; my side of the desk is teaching, writing, and figuring out how ML can accelerate the way we find new medicines. I have a PhD in computational biology from Washington University in St. Louis (graph neural networks for drug metabolism), and I teach graduate ML and cheminformatics courses at UC Berkeley. This site is where I write about all of it.

**Social icons row (in order):** LinkedIn, X/Twitter, GitHub, Google Scholar, Email

- LinkedIn: https://www.linkedin.com/in/noahflynn/
- X: https://x.com/NoahF39228 (update if handle changes)
- GitHub: https://github.com/nrflynn2
- Google Scholar: https://scholar.google.com/citations?user=KsUG8GgAAAAJ&hl=en
- Email: noahrflynn@gmail.com

---

## Book Landing Page (`/book/`)

Custom standalone page — not a blog post. Layout:

### Content

**Title:** Machine Learning for Drug Discovery

**Subtitle:** Hands-on deep learning for pharmaceutical research — from molecular fingerprints to AlphaFold.

**Body copy:**

> This book teaches machine learning and deep learning through real case studies from drug discovery. Each chapter takes a published research problem — screening antimalarial compounds, predicting cancer drug targets, generating novel molecules — and walks you through reproducing and extending the methodology from scratch in PyTorch.
>
> No chemistry background required. If you know Python and basic ML, this book meets you where you are and builds up the domain knowledge as you go. If you're a pharmaceutical scientist learning ML, each chapter grounds abstract concepts in problems you already care about.
>
> Written during my PhD, refined while teaching at UC Berkeley, and built on the same research I do at AWS AI Labs. This is the book I wished I had when I started.

### Page elements (in order)

1. Book cover image (high-res, left-aligned or centered)
2. Title + subtitle
3. Body copy (3 paragraphs above)
4. **CTA buttons:**
   - "Get the Book →" → Manning affiliate link: `https://www.manning.com/books/machine-learning-for-drug-discovery?utm_source=flynn&utm_medium=affiliate&utm_campaign=book_flynn_machine_2_29_24&a_aid=flynn&a_bid=ddb44578&chan=mm_website`
   - "View Code →" → `https://github.com/nrflynn2/ml-drug-discovery`
   - Discount note: "Use code **au35fly** for 35% off"
5. **Chapter list / Table of contents** (populate from repo structure)
6. **Testimonials section** (empty initially — use a simple blockquote format, easy to add entries later)
7. **BibTeX citation block:**
   ```bibtex
   @book{flynn2025mldd,
     title     = {Machine Learning for Drug Discovery},
     author    = {Flynn, Noah},
     isbn      = {9781633437661},
     year      = {2025},
     publisher = {Manning Publications}
   }
   ```

---

## Homepage Layout

al-folio `_pages/about.md` with these sections in order:

1. **Hero:** Profile photo (left) + name, title, bio copy (above), social icons
2. **Book feature card** ← CUSTOM COMPONENT (see below)
3. **News:** 3–5 most recent items from `_news/` collection
4. **Latest blog posts:** 3 most recent entries with date, title, excerpt
5. **Selected publications:** 3–5 highlighted papers (BibTeX `selected: true`)

---

## Custom Components to Build

### 1. Book Feature Card (homepage)

A full-width card between the hero and news sections. Structure:

```
┌──────────────────────────────────────────────────┐
│  [Cover Image]  │  Machine Learning for           │
│                 │  Drug Discovery                  │
│                 │                                  │
│                 │  Hands-on ML and deep learning   │
│                 │  for pharmaceutical research.    │
│                 │  From molecular fingerprints     │
│                 │  to AlphaFold.                   │
│                 │                                  │
│                 │  [Get the Book →] [View Code →]  │
│                 │  Use code au35fly for 35% off    │
└──────────────────────────────────────────────────┘
```

- Responsive: stacks vertically on mobile (image on top, text below)
- CTA button uses amber accent color (`#d97706`)
- Implement as a reusable Jekyll include: `_includes/book-feature.html`

### 2. Newsletter Signup

Simple email input + subscribe button. Place in 3 locations:
- Homepage (below book feature or in sidebar)
- Blog post footers (every post)
- Book landing page (below CTA buttons)

Implement as: Substack embed (preferred) or Buttondown form
Implement as a reusable include: `_includes/newsletter-signup.html`

### 3. Talks Section in CV

Within the CV page (`_pages/cv.md` or `_data/cv.yml`), add a "Talks" section:

| Talk | Venue | Date |
|------|-------|------|
| Designing Medicines from Scratch: PyTorch Workflows for De Novo Drug Discovery | PyTorch Conference 2024 | Oct 2024 |

Include fields for: title, venue, date, slides link, video link, brief description.

---

## Color Palette

### Light Mode
| Role | Color | Hex |
|------|-------|-----|
| Primary | Teal | `#0d9488` |
| CTA / Accent | Amber | `#d97706` |
| Text | Near-black | `#1a1a2e` |
| Background | White | `#ffffff` |
| Secondary text / borders | Gray | `#6b7280` |
| Code block background | Light gray | `#f3f4f6` |

### Dark Mode
| Role | Color | Hex |
|------|-------|-----|
| Primary | Lighter teal | `#14b8a6` (adjust for contrast) |
| CTA / Accent | Amber | `#f59e0b` (slightly lighter for dark bg) |
| Text | Off-white | `#e5e7eb` |
| Background | Near-black | `#1a1a2e` |
| Secondary text / borders | Medium gray | `#9ca3af` |
| Code block background | Dark gray | `#2d2d3f` |

### Where to apply in al-folio
Override in `_sass/_themes.scss` or the equivalent theme variables file. al-folio uses CSS custom properties — update `--global-theme-color` and related variables.

---

## Typography

- Use al-folio defaults (system fonts or Roboto/Source Sans Pro)
- Ensure monospace font renders SMILES strings cleanly (Fira Code or JetBrains Mono preferred for code blocks)
- No custom font loading needed unless you have a strong preference

---

## Configuration Checklist (al-folio `_config.yml`)

These are config items, not custom code:

- [ ] Site title: "Noah Flynn"
- [ ] Site description: "Applied Scientist at AWS AI Labs. Author of Machine Learning for Drug Discovery."
- [ ] Profile photo: placeholder current headshot, update later
- [ ] Social links: LinkedIn, X, GitHub, Google Scholar, Email
- [ ] Google Analytics 4 or Plausible tracking ID
- [ ] Giscus comments: configure with nrflynn2.github.io repo Discussions
- [ ] Open Graph defaults: title, description, profile image
- [ ] Twitter Card: summary_large_image
- [ ] RSS feed: enabled (default in al-folio)
- [ ] `rel="canonical"` on blog posts (for POSSE)
- [ ] Light/dark mode toggle: enabled
- [ ] Search: enabled

---

## Pages to Build

| Page | Source | Notes |
|------|--------|-------|
| Homepage | `_pages/about.md` | Bio + book card + news + posts + selected pubs |
| Blog | `_pages/blog.md` (auto) | Paginated, tagged, al-folio default |
| Book | `_pages/book.md` | Custom layout — copy above |
| Publications | `_pages/publications.md` | BibTeX-driven from `_bibliography/papers.bib` |
| Teaching | `_pages/teaching.md` | UC Berkeley CHEM 274B + course repo link |
| CV | `_pages/cv.md` | Timeline format from `_data/cv.yml` + Talks section |

---

## Content to Port from Current Site

- [ ] All publications → `_bibliography/papers.bib` (14+ papers)
- [ ] Publication teaser images → `assets/img/publication_preview/`
- [ ] CV data → `_data/cv.yml`
- [ ] News items → `_news/` collection (markdown files)
- [ ] Profile photo → `assets/img/prof_pic.jpg`

---

## Teaching Page Content

**UC Berkeley CHEM 274B: Molecular Science & Software Engineering**

Adjunct faculty. Graduate-level course covering ML and cheminformatics for molecular science applications.

- Course repository: https://github.com/nrflynn2/swe-molecular-sciences
- Semesters taught: [populate with actual terms]

---

## SEO & Structured Data

al-folio handles most of this, but verify:

- [ ] JSON-LD for `Person` schema on homepage
- [ ] JSON-LD for `Book` schema on `/book/`
- [ ] JSON-LD for `Article` schema on blog posts
- [ ] `sitemap.xml` auto-generated
- [ ] `robots.txt` present
- [ ] Open Graph image defaults to profile photo (override per-page where needed)

---

## Implementation Order (for Claude Code)

1. Fork al-folio → configure `_config.yml` (site metadata, social links, analytics)
2. Set color palette in theme SCSS
3. Port publications to `papers.bib` + teaser images
4. Build CV page with `_data/cv.yml` (include Talks section)
5. Build Teaching page
6. Build Book landing page (custom layout)
7. Build homepage book feature card (custom include)
8. Add newsletter signup include
9. Configure Giscus comments
10. Set up blog infrastructure (tags, pagination, canonical URLs)
11. Deploy to GitHub Pages with custom domain
12. Test mobile responsiveness
13. Write and publish first blog post
