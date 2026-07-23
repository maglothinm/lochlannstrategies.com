# Lochlann Strategies Website — Version 12.0

This package contains a static, deployment-ready website for Lochlann Strategies.

## Release focus

- Reworked the visual system around a quieter, more continuous palette.
- Replaced hard navy-to-white section changes with layered ink, slate, muted blue, mist, stone, warm ivory, and paper surfaces.
- Confined the darkest treatments primarily to the hero, contained contact panels, calls to action, and footer.
- Added a visual operating lifecycle, decision cards, engagement structures, an experience timeline, and restrained SVG linework.
- Standardized the header, navigation, contact pathway, and footer across all pages.
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
- `assets/icons.svg` — Shared SVG symbol library
- `assets/strategic-grid.svg` — Hero linework
- `assets/contours.svg` — Subtle section texture
- `assets/founder-perspective.svg` — About-page visual
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
