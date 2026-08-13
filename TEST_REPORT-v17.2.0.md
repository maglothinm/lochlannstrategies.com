> **Historical report:** Superseded for deployment by `TEST_REPORT-v17.2.1.md`. The v17.2.1 correction adds the missing component-value review and orientation-change regression coverage.

# Lochlann Strategies v17.2.0 — Test Report

**Test date:** August 12, 2026  
**Test target:** Final v17.2.0 deployment directory  
**Result:** **PASS**

## Coverage

The final package was validated as a static GitHub Pages site and rendered through a routed local origin in system Chromium. The test matrix covered all seven public/error pages at phone and desktop widths, plus the Home page and selected content pages at additional breakpoint widths.

| Viewport | Width | Pages rendered |
|---|---:|---:|
| Phone compact | 320 px | 1 |
| Phone | 390 px | 7 |
| Tablet | 768 px | 3 |
| Laptop | 1,024 px | 3 |
| Desktop | 1,440 px | 7 |
| **Total** |  | **21 page/viewport renders** |

## Automated static checks

- Every public/error page has an HTML5 doctype, one `main` landmark, one `h1`, and no duplicate IDs.
- Every local stylesheet, script, image, `srcset` candidate, and internal page reference resolves inside the package.
- Every local raster image has intrinsic width and height attributes.
- Large content images have responsive `srcset` and `sizes` values.
- The v17.2 stylesheet has no broken local `url()` references.
- The v17.2 JavaScript passes `node --check` syntax validation.
- Principal-page canonical URLs, descriptions, robots metadata, social-image metadata, and linked JSON-LD graphs parse and align.
- The sitemap parses as XML and contains exactly the six canonical principal URLs.
- `robots.txt` points to the canonical sitemap.
- No public file retains the prior CSS/JavaScript reference, prior social card filename, or superseded “enterprise mobilization” wording.

## Rendered checks

- No horizontal overflow was detected at any tested width.
- Every rendered image completed with positive natural dimensions.
- No browser console errors or uncaught page errors were recorded.
- The 320- and 390-pixel Home pages retained the full headline and lead without clipping.
- The 960-pixel mobile WebP derivatives were selected on the 320- and 390-pixel Home renders.
- The mobile menu opened with the correct `aria-expanded` state, moved focus inside the menu, applied `inert` to the main content, closed on Escape, and restored focus to the menu button.
- Reduced-motion media behavior was enabled during rendering.

## Visual inspection

Desktop and phone screenshots of Home, About, and Contact were inspected after rendering. The final build preserves the established navy/gold system, headline hierarchy, image cropping, fixed navigation, and CTA treatment. The longer principal-led Home lead remains readable at 390 pixels, the need-to-delivery section retains clear stage separation, and the new social card is legible at its native 1,200 × 630 dimensions.

## Limitations

This was a deterministic local static/rendered validation, not a production-network Lighthouse measurement and not a native Safari/WebKit run. It verifies package integrity, responsive behavior, rendering, interaction, and asset selection before deployment. Live caching, CDN behavior, search recrawl timing, and third-party social-preview caches must be confirmed after publication.

## Machine-readable results

The package includes `test-results-v17.2.0.json`, containing the dimensions, overflow measurements, document heights, titles, and rendered image results for all 21 page/viewport checks.
