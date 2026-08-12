# Lochlann Strategies v17.1.0 — Review Notes

## Editorial review

- Rewrote all six principal pages in a direct, professionally colloquial voice.
- Gave each page a distinct role: Home states the value; Capabilities defines the work; Approach explains the engagement; Experience establishes the record; About tells the career story; Contact lowers the barrier to starting.
- Replaced abstract consulting shorthand with concrete language about customer needs, account choices, capture, teaming, commercial decisions, site readiness, ownership, and delivery.
- Kept prior roles separate from Lochlann client results and avoided unsupported outcome claims.
- Added an initial-contact warning for classified, export-controlled, source-selection-sensitive, proprietary, and other restricted information.

## Technical continuity

- Preserved the v17.0.4 visual system, images, stylesheet, JavaScript, responsive behavior, fixed header, mobile drawer, reveal motion, reduced-motion handling, and iPhone Safari content-panel fix.
- Preserved the public Home, Capabilities, Approach, Experience, About, Contact, and 404 URLs.
- Added `sectors.html` as an immediate canonical, no-index redirect to Experience so the obsolete public page no longer exposes legacy content.

## Acceptance tests completed

- Parsed every HTML page and confirmed one `main`, one `h1`, and no duplicate IDs on each rendered page.
- Verified every local page, stylesheet, script, image, icon, and source reference.
- Parsed all JSON-LD and the XML sitemap; confirmed matching descriptions across standard, Open Graph, and X metadata.
- Rendered all principal pages plus 404 at 320, 390, 768, 1024, and 1440 CSS pixels with no horizontal overflow, broken images, fixed-header drift, or browser console errors.
- Verified mobile-menu opening, focus entry, background inertness, Escape closing, body-scroll release, and focus restoration.
- Inspected the revised desktop and mobile hero layouts plus the Home mission panel, Approach principle, Experience caption, About career section, and Contact card.
- Confirmed the packaged visual assets are byte-for-byte identical to the v17.0.4 baseline.
- Confirmed the obsolete Sectors URL is absent from the sitemap and redirects to Experience.
