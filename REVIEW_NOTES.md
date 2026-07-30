# v16.3.2 Review Notes

## Retained from v16.3.1

- Predominantly dark navy, ink, and slate surfaces.
- Restrained brass accents, crest watermarks, imagery, wording, and page order.
- Semantic, indented, human-reviewable HTML.
- Safari-safe grid shrinking, wrapping, long-link handling, and horizontal-overflow protections.
- Animated hamburger-to-X control and reduced-motion support.
- No use of the word “conceptual” in public-facing HTML.

## Navigation change

- The site header now uses `position: fixed` rather than relying on `position: sticky`.
- The header spans the viewport and remains visible at every scroll position.
- The document receives a matching top offset via `padding-top: var(--header)`.
- The mobile navigation panel is explicitly positioned below the fixed header.
- Desktop navigation and the mobile hamburger remain continuously accessible without auto-hiding.

## Acceptance criteria

- Header remains at viewport top after scrolling on every page.
- Main content begins below the header at load.
- Mobile menu opens below the header and remains within the viewport.
- No horizontal overflow at 320, 375, 390, 414, 430, 768, 1024, or 1440 CSS pixels.
- Skip link remains visually hidden until keyboard focus.
- No imagery, wording, layout modules, or page URLs changed.
