# Lanamyr Wiki — Style Guide

This file documents the *presentation* conventions for the GitHub Pages wiki
(HTML structure, formatting rules, sidebar nav, site architecture) — as
distinct from the `bible/` files, which hold the *lore*. Read this at the
start of any session that will touch wiki pages. Claude maintains this file:
when a new formatting or structural decision gets made, update this doc in
the same push as the change that prompted it. The user doesn't need to
remember or restate these conventions — that's the point of writing them
down.

If a formatting question comes up that isn't covered here, resolve it,
apply it, and add it here so it doesn't have to be re-decided next session.

================================================================================
SITE ARCHITECTURE (JEKYLL)
================================================================================

The site runs on Jekyll (via GitHub Pages' native support — no separate build
tooling needed). Key files:

- `_config.yml` — site config, sets `baseurl: /Lanamyr-wiki`.
- `_data/nav.yml` — the SINGLE SOURCE OF TRUTH for the sidebar nav. Every
  group and link shown in the sidebar is defined here, once.
- `_includes/nav.html` — renders `nav.yml` as the sidebar `<nav>` markup, and
  automatically marks the current page's link with `class="current"` by
  comparing `page.url` to each item's `url`. This is why every page's
  `permalink` front matter must exactly match its own url — see below.
- `_layouts/default.html` — the shared page chrome: `<head>`, sidebar wrapper,
  `.content-card` wrapper, and the category-bar / crumb rendering.

**Never hand-edit sidebar nav markup inside an individual page file.** There
isn't any — every page's nav comes from the shared include. To add, rename,
reorder, or remove a sidebar entry, edit `_data/nav.yml` only.

Every content page is Jekyll front matter + body only — no repeated
boilerplate. Required front matter on every page:

```yaml
layout: default
title: "Page Title — Lanamyr"      # full <title> text, exactly as it should render
permalink: /path/to/this-file.html # must exactly match the file's own path
category: overview                 # one of: overview, geography, races, kingdoms,
                                    # characters, items, stories, open
```

Optional front matter, used on granular pages nested one level below an
index page (e.g. a specific race, kingdom, or character):

```yaml
crumb_parent: "Races"
crumb_parent_url: "/races/index.html"
crumb_current: "Wood Elves"
```

================================================================================
SIDEBAR NAV RULES
================================================================================

The sidebar is reserved for:
- The Home link.
- One representative "sample" page per section (currently: Wood Elves,
  Faelyn, Mya Li).
- Each section's "All X &rarr;" index page.

Granular pages — individual races/kingdoms/characters/locations beyond the
one representative sample, and standalone reference pages like the Epoch
timelines — are NOT added to the sidebar. They're reached via in-content
links and breadcrumbs only. Existing examples: `locations/monowi-inn.html`,
`overview/epoch-1-timeline.html` / `epoch-2-timeline.html` /
`epoch-3-timeline.html`.

This keeps the sidebar from growing unbounded as granular pages accumulate.
If a page should be a full nav-level entry instead, that's a deliberate call
to make with the user, not a default.

================================================================================
BULLET LISTS VS. PROSE
================================================================================

RULE: When a paragraph strings together three or more bolded
"Term — description" fragments back to back (or a clearly run-on two),
convert it to a plain bulleted list:

```html
<ul>
  <li><strong>Term</strong> — description</li>
  <li><strong>Term</strong> — description</li>
</ul>
```

No extra CSS class needed — plain `<ul><li>` already matches the site's
existing look (see `races/wood-elves.html`'s "Notable Wood Elves" list, the
original precedent for this pattern).

EXCEPTIONS — stay as prose:
- A single item (nothing to enumerate).
- Sentences already using natural list grammar with commas/"and" — e.g.
  "X (Y), X (Y), and X (Y)." (see `geography/continents.html`'s "Major
  islands" paragraph).
- Bolded terms embedded in genuine narrative sentences, not a repeated
  enumeration pattern (see `overview/cosmology.html`, `overview/epochs.html`,
  `open-questions/index.html`'s "Character threads").
- A joint sentence describing two entities together as one unit (e.g. "Elsie
  and Alita run the inn" on `characters/index.html`).

Applied so far to: `kingdoms/index.html`, `races/index.html` (restructured
into ancestry &rarr; race family &rarr; subtype bullets under `<h3>`
headings), `characters/index.html`, `items/index.html`,
`geography/locations.html`.

================================================================================
FACT-ROW VS. BULLETS VS. PROSE
================================================================================

`.fact-row` (a `.k` / `.v` pair, styled as a label + value line) is for:
- Structured facts at the top of a granular entry — Origin, Kingdom,
  Lifespan, etc. (see `races/wood-elves.html`, `characters/mya-li.html`,
  `kingdoms/faelyn.html`).
- Chronological timeline entries — year in `.k`, event in `.v` (see
  `overview/epoch-1-timeline.html`, `epoch-2-timeline.html`,
  `epoch-3-timeline.html`, and the summary table on `overview/epochs.html`).

Bullets are for enumerated lists of comparable items with a name + short
description (see the bullet-list rule above).

Plain prose is for narrative explanation, single facts, and short lists that
already read naturally as a sentence.

================================================================================
PAGE STRUCTURE CONVENTIONS
================================================================================

Standard order within `.content-card` (category-bar and crumb are rendered
automatically by the layout from front matter — don't add them manually):

1. `<h1>` — page title.
2. `<span class="tag">` (and `<span class="tag tentative">` for undecided
   lore) directly under the `<h1>`.
3. `.fact-row` block, if applicable.
4. `<h2>` sections for major content divisions.
5. `<h3>` sections for sub-groupings within an `<h2>` (e.g. race families
   under an ancestry heading on `races/index.html`).
6. `.related` box at the end, titled "Related", with a bulleted list of
   2-4 links to other relevant pages. Every page should have one.

================================================================================
CROSS-PAGE ANCHORS
================================================================================

Use `id="..."` on an `<h2>`/`<h3>` when another page needs to deep-link to
that specific section. Existing anchors: `#abaculus` and `#heavens-oak` in
`items/index.html` and `geography/locations.html` respectively, `#sundering`
in `overview/epochs.html`, `#guardians` in `stories/index.html`.

A broken anchor link fails silently — no 404, it just lands at the top of
the target page. Before adding a new anchor cross-link, confirm the `id`
actually exists on the target, and add it to the `anchor_checks` list in
`tools/validate_jekyll.py` so future changes can't silently break it.

================================================================================
IMAGES
================================================================================

Reference map images directly from `bible/maps/` (e.g.
`src="../bible/maps/Lanamyr_Continents.jpg"`) rather than copying them
elsewhere. This means uploading a replacement file at that same path
automatically updates every page that references it — no page edit needed.
See `geography/maps.html` for the pattern.

================================================================================
VALIDATING BEFORE A PUSH
================================================================================

There's no Ruby/Jekyll available in the Claude session environment (and
rubygems.org isn't on the network allowlist to install it), so GitHub Pages'
own build on push is the only authoritative test. `tools/validate_jekyll.py`
simulates the parts of Jekyll that are easy to get subtly wrong by hand:
permalink uniqueness, `_data/nav.yml` links resolving to real pages, the
current-page nav highlight matching exactly one entry (zero for pages
correctly excluded from the sidebar), and cross-page anchors resolving.

Run it from the repo root before pushing any change that touches front
matter, `_data/nav.yml`, or cross-page anchors:

```
pip install pyyaml --break-system-packages   # if not already available
python3 tools/validate_jekyll.py
```

It exits non-zero and lists every problem found if something's wrong.

================================================================================
OPEN STYLE QUESTIONS
================================================================================

(None currently. Add an item here if a formatting question comes up mid-
session and isn't resolved before the session ends, so it isn't re-litigated
from scratch next time.)
