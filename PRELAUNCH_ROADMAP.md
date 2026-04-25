# Pre-Launch Roadmap — noahrflynn.com

Tracker for improvements brainstormed but **not yet implemented**. Review and triage before the initial public launch. Items are grouped by theme and annotated with effort, impact, and dependencies.

**Legend:**
- 🟢 low effort · 🟡 moderate effort · 🔴 high effort
- ⭐ high impact · ✨ medium impact · · low impact
- `[ ]` not started · `[~]` partially done · `[x]` done

---

## Quick wins before launch

These are low-effort, high-signal items that would noticeably polish the site.

- [ ] 🟢 ⭐ **Activate Giscus comments** — infrastructure is configured (`_config.yml`); just need `repo_id` and `category_id` from [giscus.app](https://giscus.app). Without these the comment widget silently fails.
- [ ] 🟢 ⭐ **Connect analytics** — Google Analytics, Plausible, or Pirsch (all templated in `_includes/scripts/analytics.liquid`). You can't optimize what you don't measure, and launch metrics are especially valuable.
- [ ] 🟢 ✨ **CV PDF download link** — al-folio supports `cv_pdf` front matter in `_pages/cv.md`. Either maintain a PDF manually or auto-generate from `_data/cv.yml`.
- [ ] 🟢 ✨ **Verify Amazon Nova arXiv ID** — `2506.12103` in `_bibliography/papers.bib` looks future-dated; confirm before launch.
- [ ] 🟢 ✨ **Custom 404 page** — brand the error page with personality and useful navigation back to key sections.
- [ ] 🟢 ✨ **GenCircuit-RL preprint** — fill in abstract and arXiv link once available (tracked in `CONTENT_GAPS.md`).

---

## Link-in-bio & social hub

Make the site the central hub across all social profiles.

- [ ] 🟡 ⭐ **`/links/` page** — dedicated mobile-optimized link-in-bio page with large tap targets. Use as your single URL across social profile bios instead of the homepage. Rationale: social bios get one link; the homepage is optimized for browsing, not for tapping from a phone.
- [ ] 🟢 ✨ **Social links in footer** — currently only in navbar (homepage) and about page. Adding them to the sticky footer ensures every page has a path to socials.
- [ ] 🟢 ✨ **Add more social platforms** — `_config.yml` supports 50+ platforms. Candidates: Bluesky, YouTube (if you record talks), ORCID (academic identity), Semantic Scholar, Medium/Substack.

---

## Content pages & architecture

Expand the site from "academic homepage" to "content hub."

- [ ] 🟡 ⭐ **`/now/` page** — [/now movement](https://nownownow.com/) style living page: current work, reading, thinking. Updates monthly. More personal than news items, good for SEO and return visitors.
- [ ] 🟡 ⭐ **`/talks/` page** — dedicated talks page with embedded video (PyTorch Conference recording), slides, related posts. You have 2 talks listed in `_data/cv.yml` already. Serves as a media kit.
- [ ] 🟡 ✨ **Revive projects page** — currently hidden (`nav: false`) with 10 placeholder projects. Curate 4-6 real projects (GenCircuit-RL, COMPASS, Amazon Nova, the book, the Berkeley course) with rich descriptions, links, and impact metrics.
- [ ] 🟡 ✨ **Reading list / resources page** — curated ML + drug discovery resources. Positions you as a thought leader and drives organic search traffic.
- [ ] 🔴 ✨ **"Start here" narrative page** — guided tour for different audiences (recruiters, students, collaborators, drug discovery professionals). Different entry points into your content.
- [ ] 🟡 ✨ **Cross-linking pass** — blog posts → publications, book page → related papers, teaching → posts about the course. Internal linking boosts SEO and on-site time.

---

## Blog foundation

Blog infrastructure is solid, but no personal posts exist yet.

- [ ] 🟡 ⭐ **First blog post** — any post. Removes the "empty blog" feel and validates the pipeline end-to-end. Suggested topic: a short announcement (book launch, course launch, or a paper walkthrough).
- [ ] 🔴 ⭐ **Blog series architecture** — themed series beat one-off posts for return traffic. Candidates: "Drug Discovery ML Explained", "Teaching Diaries" (from Berkeley course), "Paper Deep Dives" (your own publications).
- [ ] 🟢 · **Remove or rename sample template posts** — 29 al-folio template posts currently pad `_posts/`. Before launch, either delete or clearly label as examples. They currently clutter the blog index and tag cloud.
- [ ] 🟡 ✨ **Per-post OG images** — automate via GitHub Action that generates 1200×630 images from post titles on push. Infrastructure from the OG image system can be extended.

---

## Engagement & growth

Activate existing infrastructure to capture and retain attention.

- [ ] 🟡 ⭐ **Newsletter** — template is built (`_includes/scripts/newsletter.liquid`), configured for Loops.so. Pick Substack (discoverability) or Buttondown (simplicity + code-friendly), configure the endpoint, enable. Place signup on: homepage, blog post footers, book page.
- [ ] 🟡 ✨ **Email capture on book page** — "Get a free sample chapter" gate. Captures readers who aren't ready to buy yet. Builds your list.
- [ ] 🔴 ✨ **RSS → social cross-posting** — automate posting new blog entries to LinkedIn, X, and Medium/Substack. Multiplies each post's reach. Tools: IFTTT, Zapier, or a GitHub Action.

---

## Visual identity — next iteration

Visual identity Phase 1 shipped (favicon, hero, OG images). Potential Phase 2 work — see `VISUAL_IDENTITY_WORK.md` "potential revisions to consider" sections for full details.

- [ ] 🟡 ✨ **Test hero layout variants** — single-column centered, full-width with background imagery, featured content card slot in hero.
- [ ] 🟢 · **Favicon variants** — compare abstract molecular mark to monogram/hexagon alternatives once live.
- [ ] 🟡 ✨ **Amber accent in OG images** — currently 100% teal. Adding amber could warm them up and match the site's full palette.
- [ ] 🟡 · **Signature illustration style** — a consistent custom illustration vocabulary across blog post headers, project cards, etc.
- [ ] 🟢 · **Hover/focus states** — subtle interactions on profile photo, cards, and navigation for polish.

---

## Technical polish

- [ ] 🟢 · **Lighthouse performance audit** — Lighthouse Badger is already configured in CI. Review current scores and address low-hanging fruit before launch.
- [ ] 🟢 · **Broken link audit** — `broken-links.yml` GitHub Action exists. Confirm it passes before launch.
- [ ] 🟢 · **Accessibility audit** — `axe.yml` GitHub Action exists. Confirm it passes before launch.
- [ ] 🟢 · **Performance badges in footer** — flex Lighthouse scores subtly, or in repo README.
- [ ] 🟢 · **Review responsive images** — ImageMagick is configured to generate 480/800/1400px WebP variants. Confirm all hero/profile/publication preview images are taking advantage.

---

## Interactive / technical showcases

Opportunities to showcase technical range through the site itself.

- [ ] 🔴 ✨ **Interactive blog post** — use D3, Chart.js, Vega, or Mermaid (all available) to build a post with interactive molecular structures, ML training curves, or drug discovery pipeline diagrams. Demonstrates range in a way a static post can't.
- [ ] 🔴 · **Live publication metrics dashboard** — a small page that pulls citation counts, downloads, or altmetric scores for selected papers. Altmetric + Dimensions badges already enabled per-paper; this would aggregate.

---

## Launch readiness checklist

Before going public:

- [ ] All navigation links resolve (no 404s)
- [ ] At least 1 real blog post published
- [ ] Google Analytics or alternative tracking live
- [ ] OG images verified via Twitter Card Validator and Facebook Sharing Debugger
- [ ] Favicon displays correctly in Chrome/Firefox/Safari
- [ ] Dark mode tested on all pages
- [ ] Mobile layout tested at 375px viewport
- [ ] All publications have abstracts and DOI/arXiv links (or explicit "forthcoming")
- [ ] CV PDF downloadable (or explicitly not offered)
- [ ] Comments system (Giscus) either fully active or hidden
- [ ] Newsletter either active or hidden (no broken "subscribe" buttons)
- [ ] Sample/template blog posts removed or labeled
- [ ] `CONTENT_GAPS.md` reviewed; remaining gaps acceptable or scheduled

---

## Deferred indefinitely (unless priorities change)

Lower-priority ideas to revisit post-launch:

- Newsletter archive page
- Comment moderation dashboard
- Multi-language support
- Search beyond the built-in al-folio search
- Dedicated "press" or "media" page
- Podcast page (unless you start one)
