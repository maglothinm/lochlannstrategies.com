# Lochlann Strategies v17.2.2 — Test Report

**Date:** August 13, 2026  
**Baseline:** v17.2.1 value-filter correction  
**Scope:** Company-first Home hero, principal proof, CTA hierarchy, mobile entry spacing, metadata alignment, and stylesheet cache versioning

## Result

**PASS — no blocking defects found.**

The Home page now establishes Lochlann’s offer before introducing Michael Maglothin, keeps his full name above the fold, presents Capabilities as the primary action, and preserves all v17.2.1 corrections.

## Structural and content validation

- All eight HTML files parsed without structural errors after the package’s longstanding XHTML-style void-element conventions were treated as formatting preferences.
- All local `href`, `src`, and `srcset` targets resolve.
- Every primary page contains one H1.
- All JSON-LD blocks parse as valid JSON.
- Home metadata, Open Graph, X description, and WebPage schema use the company-first description and retain Michael Maglothin by name.
- Home runtime order is: eyebrow → headline → Lochlann proposition → Michael principal proof → `See capabilities` → `Explore the experience`.
- The primary action points to `services.html`; the secondary action points to `experience.html`.
- No circular operating-map selectors or elements are present.

## Code and asset validation

- Shared CSS parsed successfully with CSS Tree Validator.
- Shared JavaScript passed `node --check`.
- Every HTML page references `assets/lochlann-v17.2.2.css?v=17.2.2`.
- The unchanged JavaScript remains `assets/lochlann-v17.2.1.js?v=17.2.1`.
- All primary pages and both versioned assets returned HTTP 200 with the expected content types from a local server.
- The lower-contrast principal proof remains WCAG AA compliant: 6.75:1 on the dark ink background and 4.86:1 against the lightest Home gradient color tested.

## Browser matrix

Headless Chromium was run with valid local sans-serif and serif fallback fonts. No console errors, page errors, failed requests, broken images, or document-level horizontal overflow occurred.

| Viewport | Result | Key observation |
| --- | --- | --- |
| 393 × 852 iPhone portrait | Pass | Both stacked actions are visible in the initial viewport; action block spans y=695–808. |
| 852 × 393 iPhone landscape | Pass | No horizontal overflow or clipping; actions follow normally below the short viewport. |
| 768 × 1024 tablet portrait | Pass | Copy and actions remain readable and fully within the first viewport. |
| 1440 × 1000 desktop | Pass | Company proposition, principal proof, image, operating arc, and both actions remain balanced in the split hero. |

At 393 × 852, the exact first-screen order and measurements were confirmed:

- H1: y=180–390
- Lochlann proposition: y=417–553
- Michael principal proof: y=567–666
- Actions: y=695–808
- Document width: 393 CSS pixels; scroll width: 393 CSS pixels

## Interaction validation

- Mobile menu opens, sets `aria-expanded=true`, reveals the drawer, and focuses the first navigation item.
- Escape closes the menu, restores `aria-expanded=false`, hides the drawer, and removes the body menu state.
- Live viewport change from 393 × 852 to 852 × 393 retains exact document width with no horizontal overflow and leaves the menu closed.

## Preservation checks

- The v17.2.1 circular operating map remains removed without replacement.
- The separate rectangular `From need to delivery` operating arc remains intact as a concise five-step image overlay.
- No other page copy, imagery, navigation structure, proof content, or engagement content changed.
