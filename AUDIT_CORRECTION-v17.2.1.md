# Lochlann Strategies v17.2.1 — Audit Correction

**Date:** August 13, 2026  
**Scope:** Home-page operating-map component

## What the prior audit missed

The v17.2.0 audit checked structure, responsiveness, accessibility, metadata, rendering, and message cohesion, but it did not apply a strict enough component-level value test to the circular operating map. The map was hidden below 700 CSS pixels and therefore appeared acceptable in the tested phone portrait views. At common iPhone landscape widths, however, it switched on as a large desktop-style visual. More importantly, even when technically rendered correctly, it did not earn its space.

## Value-added test

A major component should remain only when it does at least one important job better than the surrounding content: improve comprehension, establish proof, create meaningful differentiation, direct the visitor, or materially strengthen the brand experience.

The operating map failed that test:

- Its spatial relationships did not communicate a real sequence, dependency, or decision model.
- The section heading, lead, and four practical steps already conveyed the idea more clearly.
- Its accompanying paragraph duplicated those same points.
- It added no proof, buyer relevance, or conversion value.
- In landscape Safari it became the dominant object on the screen and interrupted the page rather than advancing it.
- Its concentric-circle treatment carried an avoidable target/radar association inconsistent with prior brand decisions.

## Corrective decision

The operating map and its duplicate explanatory copy were removed **without replacement**. The useful content remains: the section thesis, concise lead, and four decision-to-delivery steps. Spacing was tightened so the page moves directly from the argument to the useful detail.

## Process correction

Future site audits should apply the value-added gate to every major section, visual, animation, proof strip, and callout before assessing polish or responsiveness. Passing technical tests is not enough; a component must justify its presence.
