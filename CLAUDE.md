# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal academic website for Noah Flynn (noahrflynn.com), built with the **al-folio** Jekyll theme on GitHub Pages. The site showcases publications, a book (*Machine Learning for Drug Discovery*), teaching, blog posts, and CV.

## Build & Development Commands

```bash
# Local development with Docker (preferred)
docker-compose up                    # Serves at localhost:8080 with LiveReload on :35729

# Without Docker (requires Ruby, Bundler, ImageMagick)
bundle install
bundle exec jekyll serve             # Serves at localhost:4000

# Production build
bundle exec jekyll build             # Outputs to _site/

# Deploy to GitHub Pages
bin/deploy                           # Builds with purgecss, pushes to gh-pages branch

# Code formatting
npx prettier --check .               # Check formatting (Liquid plugin included)
npx prettier --write .               # Fix formatting
```

## Architecture

- **Jekyll static site** using the al-folio academic theme (image: `amirpourmand/al-folio`)
- **GitHub Actions** auto-deploys on push to `master` via `.github/workflows/deploy.yml`
- **Pre-commit hooks** enforce trailing whitespace, EOF newlines, YAML validity, and file size limits

### Key content locations

| Content type | Location | Format |
|---|---|---|
| Pages | `_pages/` | Markdown with YAML front matter |
| Blog posts | `_posts/` | `YYYY-MM-DD-title.md` |
| Publications | `_bibliography/papers.bib` | BibTeX (use `selected: true` for homepage) |
| CV data | `_data/cv.yml` | YAML |
| News items | `_news/` | Markdown |
| Projects | `_projects/` | Markdown |

### Templating & styling

- **Layouts**: `_layouts/` (11 templates — `default`, `page`, `post`, `bib`, `distill`, etc.)
- **Includes**: `_includes/` — reusable Liquid partials. Custom components like `book-feature.html` live here.
- **SCSS**: `_sass/` — theme overrides go in `_themes.scss` (CSS custom properties like `--global-theme-color`). Custom color palette uses teal primary (`#0d9488` light / `#14b8a6` dark) and amber accent (`#d97706` / `#f59e0b`).
- **JavaScript**: `_includes/scripts/` — 30+ script includes for analytics, comments (Giscus), charts, math (MathJax), diagrams (Mermaid), etc.
- **Static assets**: `assets/` — images, CSS, JS, fonts, and third-party libraries.

### Configuration

`_config.yml` is the central configuration (~400 lines). It controls plugins (23 Jekyll plugins including jekyll-scholar, jekyll-jupyter-notebook, jekyll-minifier), social links, blog settings, image responsiveness, and more. The Docker entry point auto-restarts Jekyll when this file changes.

## Design Spec

`WEBSITE_IMPLEMENTATION_SPEC.md` contains finalized decisions on navigation, color palette, typography, page content, custom components (book feature card, newsletter signup), and SEO requirements. Consult it before making design or content changes.

## Content Gaps

`CONTENT_GAPS.md` tracks missing content and TODOs (preprints awaiting publication, missing images, etc.).

## Node Dependencies

Only used for Prettier formatting (not for the site build itself). Prettier is configured with `@shopify/prettier-plugin-liquid` at 150-char print width.
