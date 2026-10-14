# Lochlann Strategies — v17.5.4 refinement

**Date:** October 14, 2026  
**Scope:** Wording, endorsement presentation, About search metadata, structured-data maintenance, and regression QA.

## Changes

- **Home:** Replaced the awkward “Success delivery” sentence. The revised copy describes direct involvement across federal requirements and acquisition, capture/proposals, sales operations, and international program delivery, with engagement scope shaped around the client's priorities, team and schedule.
- **About search presentation:** Title changed to “Michael Maglothin | Executive Growth & Capture Leadership.” Matched the Open Graph and Twitter title and the page schema `name`, and clarified the summary description. The visible “Founder & Principal” role remains.
- **Endorsements:** Retained the four most substantive prior-role quotations: one on About and three on Experience. Removed the three weaker secondary callouts and their unused CSS.
- **Privacy:** Quotes identify professional position and functional/industry context, not the recommender's name or a company name. The four public attribution styles are President · Global Security Technology; Senior Director · Security Solutions; Senior Director · Federal Business Development; Vice President · Secure Network Solutions. The customer-trust quotation has a clearly indicated trailing omission to avoid identifying the employer; original source wording is otherwise preserved.
- **Context:** Maintained the disclaimer distinguishing endorsements about previous employment from Lochlann client work or organizational endorsement.
- **Structured data:** Corrected `dateModified` to an ISO 8601 timestamp with offset on Home, About and Experience (`2026-10-14T14:50:52-04:00`). Updated sitemap `lastmod` values for those three meaningfully changed pages.
- **Cache:** Refreshed the endorsement stylesheet cache-busting query to `v=17.5.4` without changing its asset path or other site design.

## Quality assurance

Automated static and real-browser QA was added under `tests/site_qa.py` and `.github/workflows/site-qa.yml`.

**Result:** PASS — [GitHub Actions run 38619449679](https://github.com/maglothinm/lochlannstrategies.com/actions/runs/38619449679).

- 14 responsive Chromium cases: seven pages × 1440×1000 desktop / 390×844 mobile.
- No horizontal overflow, JavaScript console/page errors or failed first-party requests reported in the tested cases.
- Mobile navigation opening and asynchronous closing verified.
- Endorsement cards and three-column/one-column responsive layout verified.
- Local asset/fragment references, headings and IDs, JSON-LD, SEO metadata consistency, timezone-aware dates, sitemap updates, and exact endorsement count verified.
- Render screenshots and the machine-readable result are available as the `lochlann-site-qa` workflow artifact (retained 14 days).

The first QA attempt exposed an incorrect immediate menu-close assertion in the new test harness. The site intentionally delays applying `hidden` by 320 ms; the test was corrected to wait for the transition, then passed.

The browser checks were against the PR's checked-out website served locally on the Actions runner. They do not independently verify live GitHub Pages cache propagation or measure production traffic, search placement, or Lighthouse performance.
