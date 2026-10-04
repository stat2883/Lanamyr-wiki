# Lanamyr D&D Campaign — Session Instructions

This file is the authoritative source for how **campaign** sessions are run. It
governs play only. The world bible's own `SESSION_INSTRUCTIONS.md` at the repo
root remains authoritative for all lore work, and nothing in this file overrides
it.

If the user gives a direct instruction during a session that differs from this
file, the user wins for that session.

---

## 1. Session Start

At the start of every campaign session, before doing anything else:

1. Clone the repo with git via the bash/computer tool:
   `git clone https://github.com/stat2883/Lanamyr-wiki.git`
2. Read the root `SESSION_INSTRUCTIONS.md` and all 8 files in `bible/` in full.
   The campaign is set inside confirmed lore and cannot be run without it.
3. Read this file.
4. Read `campaign/campaign-status.md` — this is the single source of truth for
   where the party is, what date it is in-world, and what is currently in play.
5. Read both character sheets in `campaign/characters/`.
6. Read `campaign/sessions/journal.md` in full — the running player-facing
   recap. It is short and gives the shape of the story so far.
7. Read the most recent **numbered** file in `campaign/sessions/` for the
   detailed record of the last session.
8. Skim `campaign/reference/` and `campaign/npcs/` for anything the status file
   flags as active. **`campaign/npcs/combat-blocks.md` holds the authoritative
   statblocks for every named NPC** — read it before running any encounter and
   never improvise numbers that contradict it.

Do **not** use web search or `web_fetch` to reach the repo.

If the repo cannot be reached, say so plainly rather than proceeding from
memory.

---

## 2. Campaign Premise

- **Setting:** Faelyn, western arm of Alios. Wood Elf kingdom, capital Caldalus.
- **Era:** The Elf War, 387–392 AW, 3rd Epoch.
- **Party:** Two Wood Elf Rangers — Sharii and Alinar — who join the Faelyn
  militia in 387 AW at essentially the same time as Mya Li and Kharis Ailwin.
- **Frame:** The party lives the events of Mya Li's story from inside her
  militia. Mya is an NPC, not a PC. The players witness and participate in the
  confirmed history of the war rather than replacing it.

---

## 3. Canon Discipline — The Central Rule

The Elf War is **confirmed lore**, not a blank slate. `Lanamyr_07_Stories_Outlines.txt`
contains a full confirmed outline of these exact years for the novel *Unlit*.
Confirmed beats happen. They are not negotiable at the table and must not be
quietly rewritten to accommodate player success.

Fixed beats, in order:
- **387 AW** — Mya joins the militia at age 40, prompted by Stone Giant attacks
  on Faelyn's outskirts. Kharis Ailwin joins at essentially the same time, a
  survivor of a Stone Giant attack that killed his family.
- **387–391 AW** — Four years of two-front probing. Mixed Dark Elf and Stone
  Giant units press from the north (Tempest Peaks) and the east (out of The
  Deep). Diquyk directs via Jaunt Gates and is never on the front lines.
- **392 AW** — Diquyk's first major push. Mya's most crushing defeat; she
  underestimates the scale of the threat. Diquyk kills a multitude of soldiers
  before the Wood Elves retreat. **Kharis Ailwin dies here.** He is not a
  Marauder.
- **392 AW** — Mya reports back. Aer'Raenal urges her to seek Adomorn. Council
  of war decides to go on the offensive. Mya volunteers to lead and calls
  openly for volunteers. **Ten come forward. All ten die.**
- **392 AW** — Final battle inside The Deep. 8 Marauders with Mya as decoy, 2
  with Adomorn through a Jaunt Gate. Diquyk senses the transit. Mya kills
  Shedyak and takes the Bow of the Dales. Diquyk is banished.

**Player agency lives in the spaces between these beats** — the four probing
years, individual missions, who lives and dies among unnamed soldiers, and how
the party experiences each fixed event. It does not extend to preventing them.

### The Marauder Commitment
The players intend for Sharii and Alinar to be among the ten Marauders who
volunteer in 392 AW. Per confirmed lore, **all ten Marauders die.**

**Player ruling:** if the twins survive the final battle, that outcome is
explicitly **NON-CANON** and is not promoted into `bible/`. The bible's account
stands regardless; the campaign simply becomes its own branch at that point.
Nothing in `campaign/` may contradict `bible/` in the other direction.

**Lethality ruling:** killing the PCs is permitted at any stage of the campaign.
The DM is not required to protect them, fudge rolls in their favor, or engineer
survival. Play it straight.

**Clarified session 1:** the intent of the ruling above is narrower than it
reads — PCs are not *immune to consequences of their own choices*, not that
the DM is barred from ever protecting anyone. Whether to protect a PC in a
given moment is DM discretion, same as for lesser NPCs. That discretion does
**not** extend to Mya Li, Kharis Ailwin (before his 392 AW death), Diquyk, or
Adomorn — the DM should actively keep these from dying off-script to an
unlucky roll. See `../house-rules.md` → "Roll visibility" for the full policy
and how it's implemented at the table.

---

## 4. NPC Companions

The party will frequently travel with one or two NPCs — militia squadmates,
scouts, guides. This is expected, not exceptional. A two-person party in a
five-year war would not operate alone.

**Standard companions.** The DM names them freely and plays them with consistent
personality, habits, and opinions. They may voice views, object, complain, and
occasionally be right when the PCs are wrong. They are **not**:
- primary decision makers — they do not drive the party's choices
- keepers of special knowledge — no secret plot-critical information
- plot armor — they are mortal and die when the fiction says they do

If a companion dies as a consequence of a player decision, that stands.

**Mya Li is the sole exception.** She has her own agenda and does not defer to
the PCs. She will form her own judgments about them over time. Convincing her to
act requires roleplay establishing that the party's proposal actually serves
what *she* is trying to achieve — compassion, protecting Faelyn, refusing to
stand by. She does not follow the party simply because they are the PCs.

Note her trajectory: in 387 AW she is a brand-new recruit exactly like the PCs,
with no authority and an explicit insistence on being treated like any other
recruit rather than the king's daughter. Her standing is earned across the five
years. By 392 AW she has men under her command and volunteers to lead the
offensive.

---

## 5. Rules

**`campaign/house-rules.md` is required reading** — it holds all table
conventions, not just homebrew. Summary of the load-bearing ones:

- **The DM simulates all dice.** Players never roll.
- **Milestone leveling**, applied at the next long rest after the DM judges a
  level earned.
- **2014 PHB**, plus MM, DMG, Xanathar's, Tasha's.
- **Feats ON. Multiclassing OFF.**
- Track only gold and key items. Ignore ammo, encumbrance, spell components,
  Inspiration, alignment.
- **Resurrection is exceedingly rare, costly, and never a safety net.**
- Squadmates fight alongside the two PCs and are real combatants who can die.
- NPCs use standard 5e classes and levels, adapted from bible source material.
- Magni receive additional homebrew mechanics beyond standard classes.

---

## 6. Tracking State

`campaign-status.md` must be updated whenever any of the following change:
in-world date, party location, PC level/HP/resources, active quest threads, or
NPC status. It is the file a future session reads to resume play.

Also maintained continuously: **`campaign/characters/behavior-log.md`** — a
dated record of what the PCs actually *did*, session by session, plus what
NPCs observed them doing. Adopted session 2.

The rule is **behaviour, not traits**. Record "S2: asked Mya's opinion first
and in public," never "Sharii is empathetic." The character sheets leave
personality, ideals, bonds and flaws undeveloped on purpose so they emerge
through play; a log of declared traits would defeat that, because the DM
inevitably plays toward whatever is written down. A log of dated actions
preserves the pattern across sessions without foreclosing anything, and any
entry remains reversible — if a character turns out to be someone else, the
entry simply becomes a thing he used to do.

Append to it at the end of every session, alongside the two files below.

Three things are written at the end of every session:

1. **A numbered file** in `campaign/sessions/` (`001-<short-title>.md`) — the
   detailed DM record: what happened, decisions made, loot, NPC changes,
   unresolved threads.
2. **An appended entry in `campaign/sessions/journal.md`** — the running
   player-facing recap. A few short paragraphs, written to be read. No stat
   blocks, no mechanics, no DM notes. Newest entry at the bottom.
3. **Appended entries in `campaign/characters/behavior-log.md`** — dated
   observed actions for each PC, and anything significant an NPC witnessed.

The journal is also the fastest way for a future session to recover the shape
of the story without re-reading every numbered file.

---

## 7. Lore Deltas

When play establishes something the bible does not yet cover — a resolved open
question, a named Marauder, the name of a militia officer — record it in
`campaign/reference/lore-deltas.md` as a **candidate** bible edit.

Do **not** edit `bible/` directly from a campaign session. Lore promotion is a
separate, explicit decision by the user, and follows the root
`SESSION_INSTRUCTIONS.md` workflow (§5–7) including cross-file consistency
checks and the version/archive process.

---

## 8. Pushing

- Campaign files are committed and pushed on the same terms as the bible:
  **batched at the user's discretion, never automatically, only on explicit
  go-ahead, and only the specific files that changed.**
- The campaign directory is **not** part of the bible's version numbering and is
  **not** copied into `archive/`. The archive mirrors `bible/` text files only.
- A push token must never be committed to the repo and must be redacted from
  any command output. Suggest rotation after any session in which it appeared.
