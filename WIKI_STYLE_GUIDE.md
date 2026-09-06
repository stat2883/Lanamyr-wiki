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

Optional front matter, used on granular pages nested one level below a
category page (e.g. a specific race, kingdom, or character):

```yaml
crumb_parent: "Drasu &amp; Descendent Races"
crumb_parent_url: "/races/drasu-descendent-races.html"
crumb_current: "Wood Elves"
```

================================================================================
SIDEBAR NAV RULES
================================================================================

The sidebar is reserved for:
- The Home link.
- A small number of distinct, meaningfully different category pages per
  section, OR a single umbrella page when a section's content doesn't yet
  divide into meaningful categories.

There is no generic "browse everything" index page for a large, growing
section — content is pre-sorted into meaningful categories from the start.
Compare the two current shapes side by side:

- **Categorized** (Overview, Geography, The Tapestry of Life, Kingdoms,
  Characters & Organizations, Stories): several sidebar links, each a
  distinct topic or category page. E.g. Kingdoms links to
  `kingdoms/alios.html`, `kingdoms/edura.html`, `kingdoms/utoa.html`, and
  `kingdoms/islands.html` — not one link to a combined kingdoms page.
  Characters & Organizations links to one page per major race
  (`characters/elves.html`, `characters/dwarves.html`, etc.), sorted
  alphabetically, plus `characters/organizations.html` for groups.
- **Umbrella** (Items & Relics, Open Questions): a single "All X &rarr;"
  link, used only while a section's content is small enough that splitting
  it into categories wouldn't help yet.

Granular pages one level below a category — an individual race, kingdom,
character, or location — are reached via in-content links and breadcrumbs
only, never a sidebar slot. Existing examples: `locations/monowi-inn.html`,
`races/wood-elves.html`, `kingdoms/faelyn.html`, `characters/mya-li.html`,
`overview/epoch-1-timeline.html` / `epoch-2-timeline.html` /
`epoch-3-timeline.html`, `stories/shadow-before-the-storm.html` (a third
story concept that hasn't earned its own sidebar slot alongside Unlit and
The Reluctant King — reachable only via links from those two pages).

WHY: the original "one sample + index" pattern (each section showing one
representative granular page alongside a combined index, e.g. Wood Elves +
All Races) was a bootstrap artifact from when the whole wiki had only 4
pages total, not an intentional long-term design. It was replaced in two
steps: first the sample links were dropped (Wood Elves, Faelyn, Mya Li),
leaving bare "All X" index pages; then Races, Kingdoms, Characters &
Organizations, and Stories were further split from one combined index page
into several meaningfully-distinct category pages, matching how Overview
and Geography already worked. Items & Relics and Open Questions haven't
been split yet because they don't currently hold enough distinct content
to justify it — the same way Kingdoms of Edura and Kingdoms of Utoa are
thin single-kingdom pages for now, simply because that's all the confirmed
lore currently supports.

Splitting a section's umbrella page into categories, or introducing a new
sidebar entry, is a deliberate call to make with the user, not a default to
reach for.

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
  and Alita run the inn" on `characters/humans.html`).

Applied so far to: `kingdoms/alios.html` and `kingdoms/islands.html`,
`races/drasu-descendent-races.html` and `races/draak-descendent-races.html`
(restructured into ancestry &rarr; race family &rarr; subtype bullets under
`<h3>` headings), `characters/organizations.html`, `items/index.html`,
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
   under an ancestry heading on `races/drasu-descendent-races.html`).
6. `.related` box at the end, titled "Related", with a bulleted list of
   2-4 links to other relevant pages. Every page should have one.

Kingdom pages (`kingdoms/alios.html`, `edura.html`, `utoa.html`,
`islands.html`) each get a "Lost to history" `<h2>` section for defunct or
dead kingdoms belonging to that continent/group, once that continent has
any to document — see Harrad and Nusul on `kingdoms/alios.html` for the
pattern. Edura, Utoa, and Islands don't have one yet simply because no
defunct kingdom has been placed there yet, not because the pattern doesn't
apply — add the section when one comes up, matching Alios's heading and
bullet-list format.

================================================================================
CROSS-PAGE ANCHORS
================================================================================

Use `id="..."` on an `<h2>`/`<h3>` when another page needs to deep-link to
that specific section. Existing anchors: `#abaculus` and `#heavens-oak` in
`items/index.html` and `geography/locations.html` respectively, `#sundering`
in `overview/epochs.html`, `#guardians` in `characters/organizations.html`.

A broken anchor link fails silently — no 404, it just lands at the top of
the target page. `tools/validate_jekyll.py` catches this automatically as
part of its link-graph check (see "Validating before a push" below) — no
need to hand-maintain a list of anchors anymore, just run it before pushing.

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
simulates the parts of Jekyll that are easy to get subtly wrong by hand, and
does more than a real Jekyll build would catch on its own:

- Permalink uniqueness and required front matter fields.
- `_data/nav.yml` links resolving to real pages.
- The current-page nav highlight matching exactly one entry (zero for pages
  correctly excluded from the sidebar).
- **A full link graph**, built automatically from every page's actual
  `href="..."` content — not a hand-maintained list. For every internal
  link found anywhere in any page's body, it checks the target page exists,
  and if the link includes a `#anchor`, that the target page actually has a
  matching `id="anchor"`.
- **Reachability** — every page must be linked from either `_data/nav.yml`
  or another page's body content. A page satisfying neither is a genuine
  dead page: the file exists and Jekyll would build it fine, but no reader
  could ever find its URL.

This means there's no need to manually `grep` the repo for stale links
before deleting or renaming a page — the reachability and link-graph checks
catch that automatically. Run it from the repo root before pushing any
change that touches front matter, `_data/nav.yml`, internal links, or page
deletions/renames:

```
pip install pyyaml --break-system-packages   # if not already available
python3 tools/validate_jekyll.py
```

It exits non-zero and lists every problem found if something's wrong.

================================================================================
EFFICIENT EDITING WORKFLOW
================================================================================

These sessions run against a usage budget, so tool-call efficiency matters,
not just correctness. A few habits that keep it efficient:

- BATCH THEN VALIDATE, NOT EDIT-CHECK-EDIT-CHECK. Make every planned change
  in a batch of work first, then run `tools/validate_jekyll.py` once at the
  end. Running the validator after every individual edit adds tool calls
  without adding confidence — the checks that matter (link resolution,
  reachability, anchor validity) only need to be correct once everything is
  in place, not verified after each intermediate step along the way.

- TRUST THE VALIDATOR FULLY — DON'T ALSO GREP AS A DOUBLE-CHECK. Its
  reachability and link-graph checks (see "Validating before a push" above)
  are comprehensive — they already do everything a manual `grep` sweep for
  stale links was doing by hand before this tool existed. Running a `grep`
  sweep on top of a passing validator run adds tool calls without adding
  coverage. If the validator passes, the links are good; move on.

- SCRIPT MECHANICAL CHANGES THAT REPEAT ACROSS FILES, DON'T REPEAT THE SAME
  EDIT BY HAND. When the same change applies to multiple files with the
  same surrounding text (e.g. a site-wide wording change, or — back before
  `_data/nav.yml` centralized the sidebar — adding the same nav link to
  every page), do it in one `sed`/`perl`/`python` pass across every affected
  file at once, not one `str_replace` call per file. Reserve individual
  `str_replace` calls for edits that are genuinely different per file
  (different surrounding context, different wording) — that's most of what
  cross-link retargeting during a restructure looks like, so it doesn't
  usually script well, but a same-text-everywhere change always should.

These habits don't change what gets built — only how many tool calls it
takes to get there.

================================================================================
OPEN STYLE QUESTIONS
================================================================================

STORIES SECTION SCOPE: the Stories section (`stories/unlit.html`,
`stories/reluctant-king.html`, and the unlisted
`stories/shadow-before-the-storm.html`) is reserved for actual planned/
outlined narrative works — not general lore. The Abaculus's history and the
Creation of Lanamyr stay in `overview/` (Cosmology & Magic, the Epoch
timelines) as reference material, not narrative. Decided for now; may be
revisited once material like the Abaculus's arc or the Creation of Lanamyr
gets an actual narrative treatment written, rather than staying summarized
as fact. Don't re-litigate this from scratch — check here first if it comes
up again.
