# Lanamyr — Session Instructions

This file is the authoritative source for how Lanamyr sessions are run. The
project instructions contain only what is needed to locate this repository and
find this file; everything else lives here.

If anything in this file conflicts with a stale instruction elsewhere, this file
wins. If the user gives a direct instruction during a session that differs from
this file, the user wins for that session — this file is the default, not a cage.

Edits to this file take effect on the **next** session. Changing it mid-session
does not retroactively change behavior already underway.

---

## 1. Session Start

At the start of every session, before doing anything else:

1. Clone the repo with git via the bash/computer tool:
   `git clone https://github.com/stat2883/Lanamyr-wiki.git`
   Cloning a public repo over https needs no token. A token is only required
   later, for pushing.
2. Read this file.
3. Read all 8 bible files in full from the local clone.

Do **not** use web search or `web_fetch` to reach the repo. The repo is not
reliably indexed by search, and `web_fetch` can only open URLs that already
appear in a prior search result or in the user's own message — both of which
will fail here.

Read all 8 files in full rather than relying on keyword search. A subtle
contradiction can hide in a file a search would never surface.

If the repo cannot be reached, say so plainly rather than proceeding from
memory or guessing at the lore.

---

## 2. Repository Structure

The repository is **bible-only**. There is no wiki, website, or published pages
layer. Tracked content is:

- `bible/` — the world bible, 8 topic files:
  1. `Lanamyr_01_Maps_Reference.txt`
  2. `Lanamyr_02_Overview_Cosmology.txt`
  3. `Lanamyr_03_Geography.txt`
  4. `Lanamyr_04_Races.txt`
  5. `Lanamyr_05_Kingdoms_History.txt`
  6. `Lanamyr_06_Characters_Items.txt`
  7. `Lanamyr_07_Stories_Outlines.txt`
  8. `Lanamyr_08_Open_Questions.txt`
- `bible/maps/` — reference map images
- `archive/` — browsable snapshots of past bible versions (see §6)
- `README.md` — short description of the repo
- `SESSION_INSTRUCTIONS.md` — this file

Do **not** create Jekyll or site scaffolding — layouts, nav data, stylesheets,
per-topic HTML pages, and so on — unless explicitly asked to rebuild a wiki.

---

## 3. Maps

Map images live in `bible/maps/`. Filenames identify what each shows:

| File | Shows |
|---|---|
| `Lanamyr_Continents.jpg` | Elevation |
| `Lanamyr_Features.jpg` | Named features |
| `Lanamyr_Islands.jpg` | Islands and archipelagos |
| `Lanamyr_Sundering.jpg` | Race origin points |
| `Lanamyr_Temperature.jpg` | Temperature gradient |
| `Lanamyr_Precipitation.jpg` | Rainfall |
| `Lanamyr_Biomes.jpg` | Biomes (read with `Biome_Legend.png`) |
| `Lanamyr_Epoch1.jpg` | 1st Epoch territories |
| `Lanamyr_Epoch3.jpg` | 3rd Epoch kingdoms |

Full descriptions of each are in `Lanamyr_01_Maps_Reference.txt`.

**All map borders are approximations defined by natural geographic features.**

---

## 4. Lore Status

- **Confirmed lore is locked in.** Do not contradict, quietly reinterpret, or
  "improve" it.
- **Tentative lore is flagged as such** and remains subject to change.

---

## 5. Tracking Changes and GitHub Updates

Files are edited directly via git commit and push — no download/re-upload step.
Even so, updates are **batched at the user's discretion**, never pushed
automatically.

- Keep a running log of confirmed changes as the session progresses, organized
  by which file(s) each change affects.
- After each confirmed change, ask whether to push now or keep batching.
  Accept "not yet" and continue accumulating.
- Push only on an explicit go-ahead.
- When pushing, commit and push **only the specific files that actually
  changed** — never the full repo — with a clear commit message summarizing
  what changed.
- If a session appears to be wrapping up, or the user signals they're done,
  proactively flag any confirmed-but-unpushed changes and ask whether to push
  before ending. Unpushed changes exist only in the conversation and will
  otherwise be lost.

**Token:** pushing requires a valid GitHub personal access token scoped to this
repo. If none has been provided in the session, ask for one before attempting to
push. The token must **never** be committed to the repo. Redact it from any
command output. Suggest the user rotate it after the session if it appeared in
conversation.

**Git identity:** if git prompts for an author identity, ask the user rather
than guessing at an email address.

---

## 6. Archive / Version Snapshots

`archive/` holds browsable snapshots of past bible versions. Its purpose is
convenient browsing on GitHub — git history already preserves everything, but
clicking into a folder is far friendlier than navigating commits.

Conventions:

- Subfolders are named `v001`, `v002`, `v003` — three digits, zero-padded.
- **Text files only.** Do not copy `bible/maps/` into snapshots; the images are
  large and rarely change.
- Snapshots capture the state of the bible **as it was before** the session's
  changes. Pull the files from the last commit (`git show HEAD:path`) rather
  than from the working copy, so in-progress edits don't leak into the archive.
- This file is workflow, not lore, and is **not** included in snapshots.

Workflow at session end, when there are changes to push:

1. Copy the 8 current (pre-change) bible text files into the next `archive/vNNN/`.
2. Apply the session's changes to the working files in `bible/`.
3. Bump the version number in both the title line and the end marker of **all
   8 files**, not only the ones that changed. The bible is versioned as a set,
   so `archive/v002/` means "the whole bible at v002." Letting files drift to
   different numbers breaks that.
4. Commit and push the archive folder and the updated working files.

Version markers use the same three-digit form as the folders: `v002`.

**Version history note:** the original single-document bible reached v27 before
being split into the 8 topic files, which restarted numbering at v1.
`archive/v001/` is the snapshot of that v1 state.

---

## 7. Cross-File Consistency

Splitting the bible by topic means some information is intentionally duplicated
across files. Examples:

- A character's age appears in both `Characters_Items` and the Timeline in
  `Kingdoms_History`.
- A race's origin point appears in both `Races` and `Maps_Reference`.
- Lifespans appear in `Overview_Cosmology`; the races themselves in `Races`.
- Story details appear in both `Stories_Outlines` and `Characters_Items`.
- Resolved open questions must be updated in `Open_Questions` **and** in every
  topic file that references the same thread.

When tracking a change or addition, identify **every** file that could contain a
duplicate or related reference — not just the most obviously relevant one — and
include all of them in the pending log together.

Each file's header lists which other files to cross-check. Use it.

---

## 8. Compiling a New Master Version

When asked to compile a single combined bible document (not the everyday
working files):

1. Re-read all 8 current topic files in full before compiling.
2. Write the entire combined document fresh in a **single `create_file` call**.
   Never use targeted edits on a document of this size.
3. Increment the version number in both the title line and the end marker.
4. Save to `/mnt/user-data/outputs/` and present the file for download.

If the user also wants it committed to the repo, do so on request. This is an
occasional deliverable, not a substitute for keeping the topic files current.

---

## 9. General

- Session focus is **lore and story building** — adding to, refining, and
  expanding the `bible/` files.
- When the user writes **DQ**, this refers to **Diquyk Lockwood**.
- All map borders are approximations defined by natural geographic features.
- Confirmed lore is locked. Tentative lore is flagged and subject to change.
- Flag contradictions and arithmetic errors when noticed, rather than papering
  over them.
