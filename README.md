# Lochlann Strategies v17.1.0 — Cohesive Copy Revision

This release keeps the v17.0.4 visual system and responsive behavior while rewriting the site around one connected story: Michael Maglothin has defined requirements, led pursuits, built teams, and carried complex programs into delivery. Lochlann applies that full-lifecycle experience to help leadership teams choose the right work, win it credibly, and deliver what they promised.

## v17.1.0 changes

- Rewrote all six principal pages in a more direct, professionally colloquial voice.
- Gave each page one clear job: Home explains the value; Capabilities defines the work; Approach shows how an engagement runs; Experience proves the background; About tells the career story; Contact makes it easy to begin.
- Replaced abstract phrases about operating systems, enterprise mobilization, bounded work, and delivery continuity with concrete language about customer needs, account choices, capture, teaming, ownership, site readiness, and delivery.
- Brought Michael Maglothin’s government-customer, prime-contractor, capture, partner-team, and program-delivery experience forward across the site.
- Standardized mobile navigation, calls to action, footer language, social metadata, and organization structured data.
- Updated the 404 page with simpler language and correct no-index handling.
- Added `sectors.html` as an immediate redirect to `experience.html`, replacing the obsolete public Sectors page without duplicating current content.
- Updated every principal sitemap entry to August 12, 2026.

## Visual and technical baseline

- Preserves the v17.0.4 dark navy identity, crest, imagery, fixed navigation, mobile Safari fix, responsive behavior, reveal motion, accessibility features, and GitHub Pages compatibility.
- Preserves one H1 and one main landmark per principal page, descriptive image text, canonical metadata, JSON-LD, sitemap, robots file, favicons, and social-share imagery.

## v17.0.4 revision

- Corrected the homepage Mission + Built Environment panel so the eyebrow and opening words cannot be clipped by the shaped frame on iPhone Safari or intermediate viewport widths.
- Made the panel height content-driven while preserving the desktop composition, image treatment, and clipped-corner geometry.
- Reduced excessive mobile headline wrapping and updated the stylesheet cache key to `v=17.0.4`.

## v17.0.3 revision

- Strengthened Michael Maglothin name-search relevance through the About-page title and H1, founder references, linked Person/Organization structured data, and sitemap updates.

## v17.0.2 revision

- Added U.S. Department of Energy between U.S. Air Force and Honeywell in both selected operating-environments presentations.
- Corrected the L3 employer name to L3Harris.
- Rebalanced the presentation for five entries, including a three-plus-two tablet layout and a one-column mobile layout.

## v17.0.1 revision

- Removed every public-facing reference to the requested prior employer.
- Removed the targeting reticle from the Home facility image.
- Rebalanced the selected operating-environments row for four organizations.

## Deployment

Upload the **contents of this directory** to the existing GitHub Pages repository root in one commit, replacing the prior website HTML and assets. The new `sectors.html` file must be included so the obsolete live page is overwritten. Preserve any repository-only file that may exist outside the package, especially `CNAME`.

The release-specific assets plus the `v=17.0.4` stylesheet cache key reduce the risk of Safari or GitHub Pages serving a mixed old/new cache state.

No build process, package manager, external font service, JavaScript framework, or third-party runtime dependency is required.
