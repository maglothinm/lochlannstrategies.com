# Lochlann Strategies v17.2.1 — Test Report

**Test date:** August 13, 2026  
**Test target:** Final v17.2.1 deployment directory  
**Result:** **PASS**

## Purpose of this corrective test

This release specifically verifies that the circular Home-page operating map and its duplicate explanation are absent at every tested width, including the wide, short viewport class that exposed the component after an iPhone Safari orientation change. It also confirms that the useful section thesis and four practical steps remain intact.

## Static validation

- All eight HTML files retain valid HTML5 doctypes and unique IDs.
- Every principal/error page retains one `main` landmark and one `h1`; the legacy `sectors.html` redirect remains intentionally minimal.
- Every local stylesheet, script, image, `srcset` candidate, and internal page reference resolves inside the package.
- All packaged content images retain intrinsic dimensions.
- JSON-LD blocks and `sitemap.xml` parse successfully.
- The v17.2.1 stylesheet parses without errors and contains no broken local `url()` references.
- The v17.2.1 JavaScript passes syntax validation.
- Public HTML and CSS contain no `operating-map`, `operating-canvas`, “ONE OUTCOME,” “One connected outcome,” or route-animation residue.
- The Home page still contains exactly four need-to-delivery steps.
- No public page references the superseded v17.2.0 CSS or JavaScript filenames.

## Rendered test matrix

Twenty-one page/viewport cases were rendered in system Chromium. The standard matrix covered all seven public/error pages at phone and desktop widths, plus the Home page at compact-phone, tablet, laptop, and four iPhone-shaped portrait/landscape dimensions.

| Test class | Viewports |
|---|---|
| Standard phone and desktop | 390 × 844; 1,440 × 900 |
| Additional responsive widths | 320 × 700; 768 × 1,024; 1,024 × 768 |
| iPhone-shaped cases | 390 × 844; 844 × 390; 852 × 393; 932 × 430 |

The tests found:

- No horizontal overflow.
- No browser console errors or uncaught JavaScript errors.
- No removed graphic or duplicate explanatory text in the rendered DOM.
- Four retained operating steps at every Home-page viewport.
- Correct menu focus, `aria-expanded`, background `inert`, Escape-close, and focus behavior in the landscape case.

## Orientation-change regression test

The Home page was loaded at 390 × 844, scrolled to the affected section, and changed in-place to 844 × 390. After the change:

- The operating map count remained zero.
- The removed “ONE OUTCOME” wording remained absent.
- Horizontal overflow remained zero.
- All four practical steps remained present.
- “The customer hears one promise” and “Test the opportunity” remained the section heading and first step.
- The mobile navigation continued to function correctly.

## Test-method limitations

A native iOS Safari/WebKit executable was not available in the container, so the rendered orientation tests used Chromium with iPhone-style viewport dimensions, device scale, touch behavior, and the current Safari user-agent string. Because the correction removes the component from the HTML and its styling from the CSS—rather than merely hiding it at a breakpoint—the graphic cannot reappear through Safari-specific layout behavior. Final confirmation on the user’s actual iPhone remains the production-device check.

The container browser also blocked direct local navigation. Render checks therefore used self-contained copies of the pages with the production HTML, CSS, and JavaScript inlined. Actual packaged image paths, candidates, dimensions, and CSS asset references were verified separately by static checks; same-aspect placeholders were used during layout rendering.

## Machine-readable results

See `test-results-v17.2.1.json` for the complete static and rendered measurements.
