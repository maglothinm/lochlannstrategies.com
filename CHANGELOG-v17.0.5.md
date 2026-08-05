# Changelog — v17.0.5

## Final typography normalization

### Preserved

- H1, H2, and H3 sizing and responsive behavior.
- Lead paragraph sizing.
- Font families, font loading, and editorial display style.
- Navy, ivory, teal-gray, and gold color system.
- Page architecture, spacing system, imagery, animation, navigation, and mobile Safari layout correction.
- All page copy, SEO metadata, structured data, and JavaScript.

### Refined

- Increased eyebrow, kicker, index, and small-label typography to a more consistent 11–12 pixel visual range.
- Increased desktop navigation, header action, mobile navigation details, buttons, and text links.
- Increased image captions, proof-strip descriptions, tags, output labels, disclaimers, evidence notes, and lifecycle labels.
- Increased supporting card, operating-step, principle, cadence, founder-lens, contact-prompt, and footer copy.
- Strengthened the faintest muted notes by moving selected text from `--muted-2` to `--muted`.
- Increased the small `Strategies` brand line while retaining its subordinate relationship to `Lochlann`.
- Moved image captions inward and upward enough to clear the diagonal clipping geometry at desktop and mobile widths.

### Hierarchy rule retained

Subordinate proof elements may remain visually larger than their labels when the proof itself is the marketable payload—for example metrics, organization names, contact identity, or decision statements. Routine descriptive text remains subordinate to its governing heading.

## Deployment behavior

The installer:

- Replaces only `assets/lochlann-v17.0.2.css`.
- Updates only the stylesheet cache key to `v=17.0.5` in site HTML files.
- Leaves the JavaScript cache key and all other file contents unchanged.
- Creates a timestamped backup beside the repository unless `--no-backup` is specified.
- Is idempotent and safe to run again.
