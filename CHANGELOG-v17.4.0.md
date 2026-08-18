# Lochlann Strategies — v17.4.0 Patch Package

**Baseline:** v17.3.0  
**Release date:** August 18, 2026

## Purpose

Make executive scale, chronology, sales-operations leadership, federal capture experience, and complex-program delivery easier for consulting buyers, recruiters, and hiring executives to verify without converting Lochlann into a personal résumé website.

## Patch behavior

- Verifies the expected v17.3.0 page anchors before editing.
- Creates a timestamped rollback copy of every changed or generated file.
- Is idempotent: rerunning replaces its own marked sections instead of duplicating them.
- Aborts and restores the prior files if validation fails.
- Produces a full deployment ZIP from the selected current repository.
