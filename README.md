# Lochlann Strategies v16.3.2 — Fixed Navigation

This package retains the v16.3.1 dark navy, slate, brass, typography, imagery, copy, page architecture, navigation labels, URLs, and responsive behavior.

## Primary change

- Anchors the global header to the viewport so it remains available throughout scrolling.
- Keeps the full navigation visible on desktop and the animated hamburger control visible on mobile.
- Preserves the existing scrolled-state background and shadow.
- Positions the mobile menu directly beneath the fixed header.
- Adds the exact header-height offset to the document so page content is never hidden underneath it.
- Retains the v16.3.1 fighter-hangar and manufacturing imagery and all prior copy corrections.
- Uses cache-safe `lochlann-v16.3.2.css` and `lochlann-v16.3.2.js` assets.

## Deploy

Upload the contents of this directory to the existing GitHub Pages repository root in one commit, replacing the prior HTML, CSS, and JavaScript files. The release-specific asset filenames prevent Safari or GitHub Pages from combining the new HTML with an older cached stylesheet.
