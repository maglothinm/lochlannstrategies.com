# Lochlann Strategies Website — Version 14.0

This is a deployment-ready static website release.

## What this release fixes

- Uses uniquely versioned CSS and JavaScript filenames so a browser or CDN cannot combine new HTML with an older, incompatible stylesheet.
- Preserves the clean editorial design with no diagrams, arrows, stock illustrations, or consulting-infographic devices.
- Keeps the continuous warm-ivory, stone, mist, muted-blue, navy, and brass palette.
- Adds explicit mobile-Safari containment for grids, long links, buttons, email addresses, and the navigation panel.
- Keeps the navigation collapsed without JavaScript through a native `details` element.
- Keeps every HTML page indented, semantic, and divided with review comments.

## Deployment

Upload **all files and folders in this package to the repository root in one release**.
The pages reference:

- `assets/lochlann-v14.0.css`
- `assets/lochlann-v14.0.js`

Older `assets/site.css` and `assets/site.js` files may remain in the repository; this release does not reference them. The new filenames are intentional cache-busting controls.

After GitHub Pages completes deployment, open the site in Safari and refresh once. The new filename means a destructive cache clear should not be required.
