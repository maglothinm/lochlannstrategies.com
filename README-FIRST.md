# Lochlann Strategies v17.4.0 — Apply This Update

This is a **drop-in patch for the current v17.3.0 repository**, not a replacement website assembled from an older release. It modifies only the content needed for executive-career evidence and adds one supplemental stylesheet.

## Easiest option: generate a ready-to-upload ZIP

1. Unzip this package.
2. Double-click `GENERATE-READY-ZIP.command`.
3. It downloads the current public `main` branch, applies the update, validates it, and places `lochlann-site-v17.4.0-executive-career-evidence.zip` in Downloads.
4. Upload the **contents** of that generated ZIP to the GitHub repository root in one commit. Preserve any repository-only `CNAME` file.

## Apply to an existing local repository

1. Double-click `apply-v17.4.0.command`.
2. Select the local folder containing the current Lochlann repository.
3. The patch creates a timestamped rollback folder, validates the result, and generates the same deployment ZIP beside the selected repository.

## Terminal option

```bash
python3 apply-v17.4.0.py /path/to/lochlannstrategies.com
```

No Python packages are required. The patch uses only the Python standard library.

## What changes

- Home: changes the career CTA to `View Michael’s Executive Background` and links to the new About chronology.
- About: adds career chronology and three executive operating tracks.
- Experience: replaces generic proof with executive-scale proof and adds three attributable prior-role evidence modules.
- SEO: broadens About/Experience descriptions and corrects duplicated structured-data knowledge terms.
- Styling: adds `assets/lochlann-v17.4.0-career-evidence.css`; the existing base CSS and JavaScript remain unchanged.

## What does not change

- Company-first Home hierarchy and primary headline.
- Navigation, imagery, crest, theme, animation, forms, contact information, or other pages.
- No public résumé, job-seeking language, fabricated client proof, or restoration of S2 Global by name.
