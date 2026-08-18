# Lochlann Strategies v17.3.0 — Test Report

**Date:** August 18, 2026  
**Baseline:** v17.2.2 company-first Home  
**Scope:** Broader growth positioning, page copy, metadata, structured data, modification dates, and release packaging

## Result

**PASS — no blocking structural or packaging defects found.**

## Structural and content validation

- All seven full HTML pages parsed successfully; each contains exactly one H1.
- All local `href`, `src`, and `srcset` targets resolve.
- All six JSON-LD graphs parse as valid JSON and use the revised Organization, Service, OfferCatalog, and Person vocabulary.
- Page descriptions, Open Graph descriptions, X descriptions, page-level schema descriptions, and titles are aligned where applicable.
- All six canonical pages use `dateModified: 2026-08-18`; all six sitemap entries use the matching date.
- Metadata description lengths range from 123 to 156 characters on canonical pages.
- No explicit prospective-employer reference or superseded strategic-account, OEM, built-environment, or internal-business-line positioning remains.
- The 404 page preserves `noindex, follow`; `sectors.html` remains a canonical redirect to Experience.

## Code, assets, and local HTTP validation

- The unchanged JavaScript passed `node --check`.
- CSS lexical structure is balanced; the stylesheet itself is unchanged from the validated v17.2.2 baseline.
- The seven full pages, `sectors.html`, sitemap, robots file, stylesheet, JavaScript, representative WebP imagery, and social-preview image returned HTTP 200 with expected content types from a local server.
- The final ZIP passed archive-integrity testing and contains the site files at the archive root.

## Responsive-risk review

- No CSS, JavaScript, image dimensions, navigation, or layout structure changed.
- The two Home hero explanatory paragraphs are shorter in aggregate than the v17.2.2 mobile-validated baseline.
- The revised operating-arc label is shorter than its predecessor.
- Longer card and narrative copy sits in auto-height or `min-height` containers rather than fixed-height text boxes.
- The mobile mission panel retains the content-driven height correction introduced for Safari.
- A live desktop review confirmed the unchanged v17.2.2 visual system; final production portrait and landscape checks remain included in the deployment instructions.
