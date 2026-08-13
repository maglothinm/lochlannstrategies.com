# Lochlann Strategies v17.2.1 — Value-Filter Correction

This corrective release starts from v17.2.0 and removes the Home-page circular operating map after a stricter component-level value review. The graphic was technically functional but did not improve comprehension, establish proof, differentiate Lochlann, guide the visitor, or justify the space it consumed—especially when it appeared as a dominant desktop-style element in iPhone landscape orientation.

## Corrective decision

- The operating map is removed.
- Its duplicate explanatory paragraph is also removed.
- Nothing decorative replaces either element.
- The useful section thesis and four practical decision-to-delivery steps remain.
- Shared CSS and JavaScript are versioned as v17.2.1 for reliable cache invalidation.

See `AUDIT_CORRECTION-v17.2.1.md` for the value-added assessment, `CHANGELOG-v17.2.1.md` for the exact changes, and `TEST_REPORT-v17.2.1.md` for final validation. The original `ADVANCED_AUDIT-v17.2.0.md` remains in the package as the historical baseline and should be read together with the correction.

## Deployment

Upload the **contents of this directory** to the existing GitHub Pages repository root in one commit, replacing the prior site files. Include `sectors.html`. Preserve any repository-only `CNAME` file.

No build process, package manager, external font service, JavaScript framework, or third-party runtime dependency is required.
