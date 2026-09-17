# Test Report — v17.4.1

Generated: September 17, 2026

Overall result: **PASS**

## Structured-data correction

- PASS — About is explicitly typed as `ProfilePage`.
- PASS — `ProfilePage.mainEntity` references Michael Maglothin’s `Person` entity.
- PASS — Profile page `dateModified` is `2026-09-17T07:53:00-04:00`.
- PASS — all seven page-level `dateModified` values are complete ISO 8601 DateTimes with timezone offsets.
- PASS — no date-only `dateModified` value remains.
- PASS — changed-page sitemap dates are current.

## Static checks

- PASS — primary pages present
- PASS — semantic HTML parses
- PASS — navigation present
- PASS — duplicate IDs absent
- PASS — JSON-LD parses
- PASS — local references resolve
- PASS — v17.4 career-evidence content remains present
- PASS — prohibited prior-employer names remain absent
- PASS — CSS braces balanced
- PASS — web manifest parses
- PASS — XML parses
- PASS — JavaScript syntax valid
- PASS — image files pass integrity checks

## Browser checks

- PASS — 14 of 14 desktop/mobile cases
- PASS — no document-level horizontal overflow
- PASS — no console or page errors
- PASS — no failed resource requests
- PASS — mobile navigation operates

## Package scope before checksum manifest

- HTML pages: 8
- Active assets: 23
- Files present before checksum manifest: 46

## Notes

- The ZIP contains complete repository-root contents, not an installer or patch.
- Visible content and styling are unchanged from v17.4.0.
- Git history is not included; the existing GitHub repository retains it when these files are committed.

See `test-results-v17.4.1.json`, `BROWSER_QA-v17.4.1.md`, and `browser-qa-results-v17.4.1.json` for detailed results.
