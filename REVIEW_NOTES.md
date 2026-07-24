# Professional Review Notes — Version 14.0

## Brand direction

The site presents Lochlann Strategies as a selective executive advisory firm, not a volume consultancy. Visual distinction comes from editorial typography, measured spacing, restrained brass rules, and controlled dark panels rather than icons, diagrams, arrows, or decorative graphics.

## Technical finding behind the failed mobile view

The supplied iPhone screenshot showed the new HTML structure rendered with an incompatible older stylesheet. The evidence was the combination of a visible skip link, desktop navigation on a mobile viewport, an oversized legacy headline treatment, and uncontained columns. The new HTML and the local release stylesheet did not share the same class names.

Version 14 prevents that mismatch by assigning release-specific filenames to CSS and JavaScript. It also adds explicit containment and wrapping rules for mobile Safari.

## Acceptance standard

- No horizontal document overflow at 320, 375, 390, 414, 430, 768, 1024, or 1440 CSS pixels.
- Mobile navigation is closed on load and remains inside the viewport when open.
- Skip link is visually hidden except during keyboard focus.
- No heading, button, link, or email address exceeds its content column.
- All internal links and referenced assets resolve.
- JavaScript is optional; core content and navigation work without it.
