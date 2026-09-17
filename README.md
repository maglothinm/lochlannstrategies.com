# Lochlann Strategies Website

Static production repository for **lochlannstrategies.com**.

## Release

**v17.4.1 — ProfilePage DateTime Correction**  
Release date: September 17, 2026

This maintenance release corrects the Google Search Console warning for an invalid `dateModified` value in Profile page structured data. It retains the complete v17.4.0 executive-career evidence update and makes no visible design or copy changes.

### Primary changes

- The About page is explicitly identified as a Schema.org `ProfilePage`.
- Its `mainEntity` continues to reference Michael Maglothin’s `Person` entity.
- `dateModified` now uses a full ISO 8601 DateTime with a UTC offset: `2026-09-17T07:53:00-04:00`.
- All other page-level `dateModified` values also use complete timezone-qualified DateTime values.
- Sitemap `lastmod` dates are current for Home, About, and Experience.
- The v17.4.0 executive chronology, prior-role scale, evidence modules, metadata, visual system, and company-first positioning are preserved.

## Deployment

This repository has no build step.

1. Extract the ZIP.
2. Upload or commit **the contents at the ZIP root** to the GitHub repository root.
3. Keep `CNAME`, `.nojekyll`, and the `assets/` directory intact.
4. Allow GitHub Pages to publish the commit.
5. In Google Search Console, open the Profile page issue and select **Validate Fix** after the updated About page is live.

## Primary pages

- `index.html` — Home
- `services.html` — Capabilities
- `engagements.html` — Approach
- `experience.html` — Experience and prior-role evidence
- `about.html` — Michael Maglothin, executive chronology, and ProfilePage markup
- `contact.html` — Contact
- `404.html` — Not-found page

## Validation

See `TEST_REPORT-v17.4.1.md`, `BROWSER_QA-v17.4.1.md`, and the accompanying JSON result files.

## Repository note

A ZIP archive does not include the existing Git `.git` directory or commit history. GitHub retains history when these files are committed to the existing repository.
