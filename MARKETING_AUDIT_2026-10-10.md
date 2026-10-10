# Lochlann Strategies — Marketing audit and implementation
**Date:** 10 October 2026  
**Scope:** Current public-facing website source and search presentation; no prior chat review.  
**Target:** Executive buyers needing additional hands-on capacity in federal growth, capture, teaming, customer entry, and complex program transition.

## Findings and changes

| Finding | Remedy applied | Where |
| --- | --- | --- |
| The home hero was collegial but too broad to qualify a prospective client. | Clarified government/mission-technology offer, direct-principal model, and relevant markets. | Home |
| The homepage first asked visitors to browse capabilities, not make contact. | Promoted "Discuss an opportunity" as primary hero CTA; reinforced contact at page close. | Home |
| Measurable prior-role experience was largely located away from the first visit. | Added three attributable evidence cards and a link to full context; maintained an explicit prior-employer, non-client disclaimer. | Home, Experience |
| Services described categories more than concrete work products. | Reworked six service descriptions and added an illustrative deliverables panel. | Capabilities |
| Engagement options could better describe retained outputs. | Clarified scope, working model, stakeholder plan, milestone plan, and handoff package. | Approach |
| Generic page titles limited clarity in search listings. | Set distinct, topic-led titles and descriptions across six core pages, synchronizing Open Graph, Twitter cards, and page JSON-LD. | All primary pages |
| Footer copy implied that Lochlann should choose strategy for the client. | Shifted to hands-on capacity alongside existing leadership. | All primary pages |

## Guardrails

- Preserve the existing crest, dark visual identity, graphics, navigation, responsive behavior, and contact email.
- Do not imply former employers, agencies, or governments are current Lochlann clients or endorsers.
- Preserve existing site schema graph, person references, canonical URLs, image cards, and sitemap.
- Do not add unverifiable testimonials, client logos, conversion statistics, certifications, or awards.
- No third-party analytics/form processor was added without account settings and privacy requirements.

## Repository QA performed

- JSON-LD parsed for each of the six indexed pages, including ProfilePage and valid DateTime values.
- Six main pages and the legacy sectors page each have one H1 and one main element.
- Relative HTML page links and fragment anchors resolved within the checked pages.
- New stylesheet referenced where needed, responsive overrides included, and CSS braces balanced.
- Section, article, figure, aside, main, and div opening/closing counts matched.
- CNAME, .nojekyll, robots.txt, site.webmanifest, and sitemap.xml remained present.
- Primary homepage CTA points to contact.html.

## Publish checks and measurement

After publication, inspect the actual page at desktop and narrow-mobile sizes for hero wrapping, evidence-card spacing, focus navigation, links, and contact behavior. Confirm GitHub Pages delivery of the new stylesheet. The external web fetch was unreliable during this audit, so the source checks do not establish real-browser performance, accessibility scoring, actual enquiries, or Lighthouse/Core Web Vitals scores.

Search engine snippets may continue to show earlier content until recrawling. In Search Console, request indexing for Home, Capabilities, Approach, and Experience after deployment and watch coverage, titles, impressions, and organic clicks. The primary business outcome to monitor is qualified enquiries, especially direct contact from Home; tracking requires an analytics or event-measurement solution to be connected separately.
