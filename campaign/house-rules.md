# House Rules & Lanamyr Adaptations

## Table Conventions

**Dice.** The DM simulates **all** rolls, for PCs and NPCs alike. Players never
roll. State results plainly, including bad ones — no fudging in the party's
favor. (See the lethality ruling in `CAMPAIGN_INSTRUCTIONS.md` §3.)

**Leveling.** **Milestone**, not XP. The DM decides when enough has been
accomplished to warrant a level, and then walks the players through the
advancement **at the party's next long rest**. Hit points always use the fixed
average (6 + Con mod).

**Sourcebooks in play:** Player's Handbook, Monster Manual, Dungeon Master's
Guide, Xanathar's Guide to Everything, Tasha's Cauldron of Everything.

**Tasha's optional class features: DECLINED.** Both PCs keep the PHB versions of
**Favored Enemy** and **Natural Explorer**. Deft Explorer and Favored Foe are
not in use. Rationale: the campaign is fought almost entirely in Faelyn's
forests, so Natural Explorer (Forest) sees constant use; and Favored Foe's
concentration requirement conflicts with Alinar's spells while Sharii's Favored
Enemy is tied to his unexplained dragon affinity. Do not revisit unless the
user raises it.

**Feats:** ON (optional rule). Each Ability Score Improvement may instead be
taken as a feat.

**Multiclassing:** **OFF.** May be revisited later by user decision. This is
load-bearing for Sharii — see below.

**Tracking.** Track only:
- The party's gold
- Key items: weapons, armor, magic items
Ignore entirely: ammunition, encumbrance, and **all** spell components. Ordinary
travelling gear (rope, bedrolls, waterskins, rations, torches, etc.) is simply
assumed to be present with someone in the group.

**Also ignored:** Inspiration, alignment.
**Used as written:** death saving throws.

**Time compression.** The campaign spans five years and cannot be played day by
day. The DM controls pacing: played scenes for engagements and consequential
moments, narrated montage across the quiet stretches, and gaps of several months
glossed over between major actions. Seasonal check-ins ("what did the brothers
do with those months?") are a natural place to hang leveling.

**Session end.** A session ends when the players say they are done for the day.
At that point the DM writes the session log to `sessions/`, updates
`campaign-status.md`, and pushes to GitHub so the next session starts clean.
Avoid ending mid-combat where possible.

**Party size.** Two PCs is well below 5e's assumed four, which breaks standard
encounter math. Squadmates are present for most engagements — realistic for
militia — and are treated as **real combatants, not scenery**. Encounters scale
to who is actually on the field. People standing next to the PCs can and do die.

**Free weapon switching.** Switching which equipped weapon(s) a PC is wielding
(e.g., longbow to shortswords) costs no action. Established session 1.

**Roll visibility.** From session 1 onward, the DM shows player-facing rolls
(PC attacks, saves, skill checks) in full, including the modifiers and raw
dice. NPC and monster rolls are **not** shown — kept under the hood, with
room for DM judgment on pacing and outcome.

**⚠ Scope, clarified session 1.** The original "no fudging in the party's
favor" line above, and the "play it straight" lethality ruling in
`CAMPAIGN_INSTRUCTIONS.md` §3, were both about one thing: **PCs are not
immune to the consequences of their own choices.** A death from a poor
decision is fine and will not be softened.

That is distinct from whether the DM ever protects anyone via the
hidden NPC rolls above. The actual policy:

- **Plot anchors — protected.** Mya Li, Kharis Ailwin (until his scripted
  392 AW death), Diquyk, and Adomorn are load-bearing to the story the
  players chose to tell. The DM should use hidden-roll discretion to keep
  them from dying prematurely or off-script to an unlucky roll. Their
  fates land on schedule, not by accident.
- **Everyone else — DM's call, serving the story.** Lesser NPCs (Wick,
  Neva, Ohren, Tam, Thale, etc.) and the **PCs themselves** are both left
  to DM discretion each time it comes up. There is no standing guarantee
  either way for these two groups — protect, or don't, whichever serves
  the moment. A PC dying to bad decisions remains always in bounds.

If this scope ever needs revisiting, raise it explicitly.

---

## Death and Resurrection

**Resurrection exists in Lanamyr but is exceedingly rare.** It is costly, and
the people capable of it are uncommon. It is never a routine option and must
never be treated as a safety net.

This is deliberate and load-bearing: the campaign's confirmed ending is that
**all ten Marauders die.** If the dead could be cheaply recovered, both Kharis
Ailwin's death and the Marauders' sacrifice lose their weight, and the bible's
account becomes difficult to explain.

**If a PC dies:** nothing is pre-decided. The options — pursuing a resurrection,
or rolling a new character into the same squadron, or taking over an established
NPC — are discussed with the player **at that time**.

*Note: the bible confirms clerics serve the twenty Irridae and that divine magic
functions, but says nothing about raising the dead. This ruling is campaign-side
and does not contradict confirmed lore. Logged in `reference/lore-deltas.md`.*

---

## Edition
**2014 PHB (5e "classic").** Confirmed by the user. Not the 2024 revision.

## Sorcerers and Magni — Ruling

Sorcerers exist in Lanamyr as a normal 5e class, bound by standard 5e mechanics
(spells known, slots, sorcery points). A **Magni** is the rare, magnified
version of the same phenomenon: full undiminished magical capacity inherited
from a progenitor line. Magni are not bound by normal spellcasting limits and
possess additional abilities beyond the class. Specific Magni mechanics are
built as needed — see the Diquyk section below.

---

## Unbidden — Sharii only

**Player-requested house rule.** Sharii has an innate, involuntary sensitivity
to magic, reflecting his lifelong unwanted pull toward the ambient current.

**Mechanics:**
- Not a spell. No slot, no action, no components, no ritual.
- Sharii **cannot invoke it, cannot suppress it, and cannot control it.**
- **The DM decides when it fires.** The player never rolls for it and never
  requests it.
- It yields **sensation, not information**: direction, rough intensity, and
  something of the flavor of the thing. Rarely the school. Never the spell's
  name.
- Strong or unfamiliar magic may leave him shaken, briefly disoriented, or
  unable to speak for a moment.

**Design intent — three consequences that must be preserved:**
1. **It fires at inconvenient times.** Mid-conversation, mid-ambush, mid-draw.
   Convenience would make it an ability instead of an affliction.
2. **It is unreliable as intelligence.** Sharii is usually right that something
   is there and frequently wrong about what. Acting on it is a judgment call,
   never a guarantee. This keeps it from trivializing mysteries.
3. **It is LOUDER than deliberate casting, not quieter.** An untrained person
   spilling into the ambient current is a flare, not a careful touch. Diquyk's
   signature ability is sensing others drawing on that current. Because Sharii
   does not choose to reach, he also cannot choose *not* to at the moment it
   matters most. Negligible risk in 387 AW while Diquyk directs remotely via
   Jaunt Gates; escalating risk as 392 AW approaches and Diquyk takes the field.

**Framing:** Sharii has no framework for this. No one in Lanamyr understands
what a Magni truly is. To him it is simply a thing that has happened to him his
whole life, that he has no name for, that he has told no one about, and that he
has spent decades trying to outrun by becoming very good at something else.

See `characters/Sharii.md` — whether he is a Magni is deliberately unresolved.

**Development is the DM's responsibility.** Multiclassing is OFF, so the player
cannot buy into sorcery mechanically. Per user decision, Sharii's abilities in
this direction are **developed by the DM over time, in whatever way fits the
story**. They are granted, not chosen. This keeps the thread out of the
player's hands, which is the point.

---

## Character Generation
- **Ability scores:** 4d6 drop lowest, with guardrails — any individual score
  below 8 is rerolled, and the six-score total must be at least 76.
- **Starting level:** 1, advancing to 2 before play begins.
- **Hit points on level up:** fixed average (6 + Con modifier) for both PCs,
  for all levels going forward. Player decision, applies permanently.

---

## Magic in Lanamyr

All magic users draw from the **ambient energy** that permeates everything.
Mechanically this does not change how spellcasting works at the table — it
changes the fiction and the vocabulary. There is no Weave; there is a current
that runs through all living things.

Consequences that matter in play:
- The ambient field is also what **masks the Abaculus**, which is why Creatures
  of Olum exist to destroy life. Characters do not know this.
- **Magni** tap the field directly without spells or rituals.
- Clerics and paladins serve one of the Irridae through faith, doctrine, and
  tradition. **No one in Lanamyr knows what the gods actually are** — not
  clergy, not the devout. Genuine faith is real and meaningful without that
  knowledge. Only Adomorn holds the truth.
- **No Irridae have been bound to Lanamyr since the Sundering.** Divine magic
  still functions; the domains were woven into creation and persist
  independently of their gods.

---

## Magni — Homebrew

A Magni receives the **full, undiminished magical capacity of their progenitor
line** rather than the muted inheritance every other descendant carries.
Drasu-descended Magni have a higher ceiling than Draak-descended ones.

Critically: a Magni inherits **capacity, not the mind behind it.** Drasu mental
fortitude — specifically the ability to resist the Abaculus in close proximity —
did not transfer. This is why Adomorn remains singular.

### Spell Theft (Diquyk's signature ability)

Diquyk senses others drawing on ambient energy, intercepts it mid-cast, steals
the spell, and stores it as blue flame. More stored = more devastating release.
Difficulty scales with the opponent's power.

**Proposed mechanics (draft — refine before Diquyk appears on-screen in 392 AW):**

- **Detection:** A Magni automatically senses any spell being cast within
  120 ft, and senses significant magical events (such as a Jaunt Gate transit)
  at much greater range. This is passive and always on.
- **Interception:** As a **reaction** to a spell being cast within range, the
  Magni makes an opposed check — Magni's spellcasting ability check vs. the
  caster's spellcasting ability check. On a success, the spell is stolen: it
  does not take effect, and the slot is expended as normal by the original
  caster.
- **Scaling:** The opposed check is made at disadvantage against a caster of
  significantly greater power (DM judgement — Adomorn was the hardest).
  Cantrips are trivially stolen; no check required against a caster of
  markedly lesser power.
- **Storage:** A stolen spell becomes **Charges** equal to the spell's level
  (cantrips = 1). Charges accumulate with no hard cap.
- **Release:** As an action, the Magni expends any number of Charges to release
  blue flame in a line or burst, dealing **2d6 force/fire damage per Charge**,
  Dexterity save for half. This is the ability that killed multiple Marauders in
  the final battle.
- **The Counter:** Switching to **physical combat cuts off the fuel supply.**
  A Magni with no spells to steal cannot replenish Charges. This is confirmed
  lore — it is exactly how Mya and Adomorn finally banished Diquyk — and it must
  remain a viable tactic.

Balance note: these numbers are deliberately frightening. Diquyk is possibly the
most powerful Magni ever born and is an unwinnable encounter for the party at
any level they will reach. He is a force of nature, not a boss fight.

---

## Adapting Lanamyr Races to 5e

Lanamyr race statistics are not in the bible. Default approach: use the closest
standard 5e statblock and reflavor, preserving bible-confirmed physical traits.

- **Wood Elf (PC race):** Standard 5e Wood Elf is a clean fit. Bible-confirmed:
  average height 5'7" male / 5'2" female, lean and slender, light tan skin, dark
  hair, dark eyes, native language **Aiwiya**, lifespan 250 years.
- **Dark Elf (antagonist):** Standard Drow, reflavored. Bible-confirmed: dark
  gray skin with deep purple hints, silver/gray/white hair, cloudy gray or pale
  blue eyes adapted to low light, more surface-averse than Dark Dwarves, from
  The Deep beneath the Tarantar Mountains. Native language **Ukuri**. During
  the Elf War they carry **magical and enchanted weapons supplied by Diquyk.**
- **Stone Giant (antagonist):** Standard 5e Stone Giant. Origin Tempest Peaks,
  directly north of Faelyn. Recruited by Diquyk with a promise of plunder —
  they respect strength above all.
- **Creatures of Olum:** See `campaign/bestiary/`. Not standard undead —
  corrupted living creatures, sickly gray-to-black with glowing red eyes, drawn
  mostly from wildlife (bears, deer, boars). Dissolve to harmless black dust on
  death. Age into large tentacled pack leaders that form birthing chambers.
