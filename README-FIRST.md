# Lochlann Strategies v17.0.5 — Typography Normalization Update

This is a deployment update for the current v17.0.4 website baseline. It makes the final typography, legibility, and formatting refinements without changing page copy, images, navigation, JavaScript, metadata, or document structure.

## Apply on a Mac

1. Extract this ZIP somewhere separate from the website repository.
2. Double-click `apply-v17.0.5.command`.
3. Select the current `lochlannstrategies.com` repository folder when prompted.
4. Review the JSON completion report in Terminal, then commit and push the updated repository.

The installer creates a timestamped backup beside the website folder before it changes anything.

## Apply from Terminal

```bash
python3 apply-v17.0.5.py /path/to/lochlannstrategies.com
```

Compatibility check only:

```bash
python3 apply-v17.0.5.py --check /path/to/lochlannstrategies.com
```

## Manual application

1. Replace `assets/lochlann-v17.0.2.css` with the file in this update.
2. In every site HTML file, change only the stylesheet cache key:

```html
assets/lochlann-v17.0.2.css?v=17.0.4
```

to:

```html
assets/lochlann-v17.0.2.css?v=17.0.5
```

Do not change the JavaScript reference. It should remain `lochlann-v17.0.2.js?v=17.0.2`.

## Scope

- Display headings and the principal H1/H2/H3 scale are unchanged.
- The existing serif/sans-serif pairing and navy/ivory/gold palette are unchanged.
- Navigation, buttons, captions, labels, evidence notes, tags, supporting card copy, and footer text receive conservative size and contrast normalization.
- Image captions receive a safer inset so they do not collide with diagonal clipped corners.
- No substantive wording or information changes are included.

See `CHANGELOG-v17.0.5.md` and `QA-v17.0.5.json` for the exact scope and validation results.
