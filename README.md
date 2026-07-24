# Lochlann Strategies Website — Version 12.1

This package contains a static, deployment-ready website for Lochlann Strategies.

## Release focus

- Removed the decorative infographic layer that made the prior release feel repetitive.
- Eliminated the custom lifecycle diagram, contour backgrounds, strategic grid, placeholder founder monogram, and nonfunctional consulting icons.
- Rebuilt the visual hierarchy around typography, spacing, rules, restrained surfaces, and editorial composition.
- Retained a softer palette of ink, slate, muted blue-gray, stone, and warm ivory to avoid abrupt navy-to-white transitions.
- Replaced the duplicate homepage lifecycle graphics with one text-led decision-standard panel.
- Simplified cards into flat editorial sections without circular ornaments, large rounded corners, or shadows.
- Preserved semantic, human-reviewable source code with clear section comments and centralized design tokens.
- Kept JavaScript optional and limited to progressive enhancement.

## Files

- `index.html` — Home
- `services.html` — Advisory Areas
- `engagements.html` — Engagement Models
- `experience.html` — Executive Experience
- `about.html` — About Lochlann Strategies
- `contact.html` — Confidential Discussion
- `404.html` — Not-found page
- `assets/site.css` — Shared design system and responsive rules
- `assets/site.js` — Progressive enhancement only
- `assets/icons.svg` — Functional arrow, mail, and copy icons only
- `assets/favicon.png` — Brand mark
- `assets/lochlann-share-preview.jpg` — Social sharing image
- `robots.txt` and `sitemap.xml` — Search-engine support
- `REVIEW_NOTES.md` — Human-review conventions and change guidance

## Deployment

Upload the contents of this folder to the website root. Keep the `assets` directory beside the HTML files.

The site does not require a build process, package manager, framework, database, or server-side runtime. Any standard static web host should serve it directly.

## Local review

From this folder, run a simple local server:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/`.

## Contact data

The published contact address in this release is:

`michael@lochlannstrategies.com`
