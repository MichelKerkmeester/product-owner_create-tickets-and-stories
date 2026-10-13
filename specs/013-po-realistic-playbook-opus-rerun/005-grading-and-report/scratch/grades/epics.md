# Grades draft: epics batch

Run folder `<RUN>`: `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`. Sources read from the working tree, which is clean for `sk-product-owner`, `claude project`, `AGENTS.md` and `benchmark/fixtures` (the `git status --porcelain` check printed nothing), so every source line below stands as at `3023c5e`. Event citations are line numbers inside the named `events-turn-<n>.jsonl`. Project block copies sit under `scratch/grades/blocks/epics/`.

Format gate results, one per export or block:

| File | Result |
|---|---|
| `skill/SEP-001 .../exports/export/001 - Epic-partner-self-onboarding.md` | passed |
| `skill/SEP-002 .../exports/export/001 - Epic-offline-mode-clarification.md` | passed |
| `skill/SEP-002 .../exports/export/002 - Epic-offline-mode.md` | passed |
| `skill/SEP-003 .../exports/export/001 - Epic-self-serve-returns.md` | passed |
| `blocks/epics/PEP-001-turn1 - Epic-partner-hub-self-onboarding-clarification.md` | passed |
| `blocks/epics/PEP-001-turn2 - Epic-partner-hub-self-onboarding.md` | passed |
| `blocks/epics/PEP-002-turn1 - Epic-offline-mode-clarification.md` | passed |
| `blocks/epics/PEP-002-turn2 - Epic-offline-mode.md` | passed |
| `blocks/epics/PEP-003-turn1 - Epic-self-serve-returns.md` | failed, 1 error: "prose connectives 3.4 per 1000 across 293 prose words, connective stripping leaves the reader guessing the relation" |

The gate does not check the required heading set, so a pass says nothing about `#### **References**`.

---

## SEP-001 (skill), Epic from strategy brief

**Draft row**

```csv
SEP-001,skill,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 drafted and saved the Epic (events-turn-1.jsonl line 86 Write of export/001 - Epic-partner-self-onboarding.md, reply turn-1.md lines 1 to 9) instead of asking one Epic question, so the Pass clause ""Turn 1 asks one Epic question in the Epic lane and drafts nothing"" is unmet and no -clarification export exists. The final Epic's shape, six stages and brief values are otherwise correct; advisory: 152 lines against the 90 to 150 band."
```

**Pass clauses**

| Clause | Met / Unmet | Evidence |
|---|---|---|
| Turn 1 asks one Epic question in the Epic lane | Unmet | `turn-1.md` lines 1 to 20 deliver an Epic, not a question. Run ledger `meta.json` turn 1: created `export/001 - Epic-partner-self-onboarding.md` only, no `-clarification` file |
| Turn 1 drafts nothing | Unmet | `events-turn-1.jsonl` line 86 Write of the Epic, line 85 thinking: "I'll draft the Epic now, flagging the release cut as open since it's not yet agreed" |
| Turn 2 saves one Epic | Met, with a caveat | Turn 2 edited the Turn 1 file in place (`events-turn-2.jsonl` lines 19 to 31, seven Edits); ledger turn 2 `modified`, not a new file on the next number |
| `# Epic - ` H1, no story preamble | Met | Export line 1 `# Epic - Partner - Self-onboarding`, line 3 `* * *`, line 4 `## About` |
| `## About` with Problem, Goal, Solution, References | Met | Export lines 8, 19, 31, 38 |
| `## Scope` names exactly six first-release child stories, one per stage name verbatim, as plain text | Met | Export lines 50, 54, 55, 56, 60, 64 carry `Sign-up and verification`, `Property profile and photos`, `Rooms and rates setup`, `Policies and city tax`, `Payout details and identity checks`, `Go-live review queue`; line 46 "All six stages ship in the first release" |
| `#### Added Later` holds the channel manager connection | Met | Export lines 66 to 71, `**Channel manager connection**` |
| Release-level `## Acceptance criteria` in `1\.` blocks each closed by Mark-as-done | Met | Export lines 80, 88, 95, 103, 111, 118, Mark-as-done at 86, 93, 101, 109, 116, 124 |
| No `## Requirements`, ticket header fields, story points or INVEST notes | Met | None in the export |
| Names the kind | Met | `turn-1.md` line 5 "I wrote this as an **Epic**", `turn-2.md` line 1 "I updated the Epic" |
| `11 business days`, `38%`, `3 business days`, `1,500`, `2027-06-30` verbatim | Met | Export lines 13, 14, 21, 23 |
| Invents no link | Met | Export lines 38 to 42 name two sources as plain text, no URL |
| No chains, over-40-room or channel manager properties in first-release scope | Met | Export lines 36, 111 to 116, 149 |
| No estimate the brief never gave, no unfilled slot | Met | Export lines 130 to 134, `TBD...` (exempt Delivery slot) |

**Blocking items hit**

- Pass clause "Turn 1 asks one Epic question in the Epic lane and drafts nothing" unmet, and the Fail clause "drafts in Turn 1" named in the scenario (root line 150, scenario acceptance at root line 144). Source rules: `AGENTS.md` line 283 (ask when scope is missing), line 287 (an explicit command does not supply direction), `SKILL.md` line 252 and line 284 rule 5
- Export names, skill-side order (root line 167): no clarification in the Epic lane, so the artifact is not on the number after it. Side-effect ledger (root line 106): the Turn 1 clarification turn created an Epic, not a `-clarification` export

**Advisory items**

- Size band: 152 lines against 90 to 150
- A `## Delivery` close was written; the scenario accepts it (scenario line 68)

**Read-back table**

| Turn | Export path | N printed | Read after last write | Lines returned | Real `wc -l` |
|---|---|---|---|---|---|
| 1 | `export/001 - Epic-partner-self-onboarding.md` | 148 | `events-turn-1.jsonl` line 99 (after Write line 86 and Bash perl edit line 97), result line 100 | 1 to 148 of 148 | Not recoverable, the file changed in Turn 2 (Read total implies 147) |
| 2 | `export/001 - Epic-partner-self-onboarding.md` | 153 | `events-turn-2.jsonl` line 33 (after last Edit line 31), result line 35 | 1 to 153 of 153 | 152 |

**Realism entry**

- `export/001 - Epic-partner-self-onboarding.md`, Epic. Required sections from `assets/epic-template.md` lines 41 to 112: H1, `## About`, `### Problem`, `### Goal`, `### Solution`, `#### **References**`, `## Scope`, `## Acceptance criteria` all present; `#### Added Later` present; optional `## Delivery` present
- Facts checked: `11 business days` export line 13 = brief line 10; `38%` with 813 of 2,140 export line 14 = brief line 11; up to 40 rooms and `3 business days` export line 21 = brief line 19; `1,500` by `2027-06-30` and 18,000 export line 23 = brief line 21; `8` photos, `20 MB` export line 54 = brief line 28; `1 business day` export line 64 = brief line 32; only an Owner changes payout details export line 60 = `roamstay-context.md` line 28; Europe and the United States export line 141 = context line 5; Bram, Ops Lead export line 46 = brief line 59
- Named additions: criterion 4 resubmit, squad split, Owner payout rule, three Rabbit holes (`turn-1.md` lines 11 to 18, `turn-2.md` lines 15 to 22)
- Borderline: criterion 5 (export lines 113 to 115) puts channel manager properties on "assisted onboarding with a partner manager", while the brief gives the partner manager only to over-40-room properties and chains (line 37) and says channel manager partners "stay on assisted onboarding for now" (line 38)
- Placeholder: none beyond the exempt `TBD...` at line 134
- Body 152 lines against 90 to 150 (advisory). H1 carries no discipline code, as the Epic H1 rule requires

**Open readings**

- `AGENTS.md` line 287 and `Custom Instructions.md` line 108 list `$task`, `$bug`, `$doc` and `$story` as commands that still ask, and neither names `$epic`. The story intake gate (`references/interactive-mode.md` lines 169 to 173) evaluates `child_stories` but has no release-cut field, and the brief supplies the six stages (brief line 63). Is an unagreed first release cut "scope missing" under `AGENTS.md` line 283 when the child-story set is supplied? The verdict follows the scenario's Pass clause either way
- `N` convention: `SKILL.md` line 211 says "Use the final line number Read returns as N". The Read tool reports one more line than `wc -l` for a file ending in a newline. Turn 2 printed 153 (Read) against `wc -l` 152. Which count is meant?

---

## PEP-001 (project), Epic from strategy brief

**Draft row**

```csv
PEP-001,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 asked one Epic-lane question and drafted nothing, but the Turn 2 Epic block has no #### **References** (turn-2.md Solution at lines 37 to 46 runs straight into ## Scope at line 47), a Pass clause and a required slot of the Project Epic Template (line 53) and kernel line 140. Advisory: Turn 1 asks for facts the brief states (turn-1.md lines 11 and 28)."
```

**Pass clauses**

| Clause | Met / Unmet | Evidence |
|---|---|---|
| Turn 1 asks one Epic question in the Epic lane | Met | `turn-1.md` lines 1 to 29 one fenced question block, line 31 `Export-equivalent path: export/001 - Epic-partner-hub-self-onboarding-clarification.md`, line 33 HVR line |
| Turn 1 drafts nothing | Met | `turn-1.md` line 37 "I haven't drafted it yet" |
| `# Epic - ` H1, no story preamble | Met | `turn-2.md` line 2 `# Epic - Partner Hub - Self-onboarding`, line 4 `* * *`, line 5 `## About` |
| `## About` with Problem, Goal, Solution and `#### **References**` | Unmet | Problem line 9, Goal line 20, Solution line 37; no References heading before `## Scope` at line 47. `turn-1.md` line 25 "If not, I'll leave References out" |
| `## Scope` names exactly six child stories, stage names verbatim, plain text | Met | `turn-2.md` lines 55 to 59 and 65; line 49 "all six ship in the first release" |
| `#### Added Later` holds the channel manager connection | Met | `turn-2.md` lines 67 to 72 |
| Release-level criteria in `1\.` blocks with Mark-as-done | Met | Lines 81, 90, 99, 109, 117; Mark-as-done 88, 97, 107, 115, 124 |
| No `## Requirements`, header fields, story points, INVEST | Met | None in the block |
| Consults only the Epic scaffold | Met | `events-turn-1.jsonl` line 21 Read of `Product Owner - Assets - Epic Template - v0.100.md`; no Story Template read; Turn 2 made no tool calls |
| Names the kind | Met | `turn-1.md` line 37 "This will be an Epic", `turn-2.md` line 155 "The Epic has" |
| `11 business days`, `38%`, `3 business days`, `1,500`, `2027-06-30` verbatim | Met | `turn-2.md` lines 14, 15, 22, 24 |
| Invents no link | Met | No link in the block |
| Claims no file | Met in Turn 2, borderline in Turn 1 | `turn-2.md` line 151 `Export-equivalent path:` only. `turn-1.md` line 37 "leave this question file unchanged" (see Open readings) |

**Blocking items hit**

- Pass clause: `## About` holding `#### **References**` unmet (root line 150)
- Ticket realism, "A required section of the routed template missing" (root line 205): the Project Epic Template mirror carries `#### **References**` at line 53 with no optional marker, and `Custom Instructions.md` line 140 says an Epic "opens with a `## About` umbrella carrying `### Problem`, `### Goal`, `### Solution` and `#### **References**`"

**Advisory items**

- Asking for a fact an attachment already states (root line 211): `turn-1.md` line 11 asks whether the Goal should use the brief's targets as written, line 28 asks whether any brief number changed since 2026-09-22
- Block form: fenced (```` ```markdown ````), at the very start of both replies, no commentary before it

**Realism entries**

- Turn 1 clarification block (`blocks/epics/PEP-001-turn1 - Epic-partner-hub-self-onboarding-clarification.md`, 27 lines), question only. Facts checked: `1,500` by `2027-06-30` line 11 = brief line 21; hotels, guesthouses and apartment buildings line 6 = brief line 36; 8 photos, 20 MB, 40 rooms, 1 business day line 28 = brief lines 28, 36, 32; `2026-09-22` line 28 = brief line 4. No placeholder
- Turn 2 Epic block (`blocks/epics/PEP-001-turn2 - Epic-partner-hub-self-onboarding.md`, 147 lines, band 90 to 150, in band). Required sections from the Project Epic Template lines 22 to 93: `#### **References**` missing; every other scaffold section present; optional `## Delivery` present (line 128), named in `turn-2.md` line 162. Facts checked: `11 business days` line 14 = brief line 10; `38%`, 813 of 2,140 line 15 = brief line 11; 40 rooms and `3 business days` line 22 = brief line 19; `1,500`, `2027-06-30`, 18,000 line 24 = brief line 21; about 4.5 hours line 16 = brief line 12; `1 business day` lines 99 and 103 = brief line 32; Bram, Ops Lead line 45 = brief line 59. Placeholder: only the exempt `TBD...` at line 134. H1 carries no discipline code
- Borderline: `turn-2.md` line 157 says Freya's Goal and target "are copied word for word", but line 24 reads "The target is 1,500 ... Roamstay has 18,000 properties live today" where the brief reads "Target: 1,500 ... For scale, Roamstay has 18,000" (line 21); the values are intact. Line 140 says Ops Tools sizes the queue "with the Partner squad", where the brief says "with us" (line 52), written by the Director of Partner Growth

**Open readings**

- Should an Epic's `#### **References**` be omitted when no link is supplied, as `assets/story-template.md` line 66 and the Project Story Template line 47 say for a Story ("Omit the whole section when none are supplied")? The Epic template (skill line 74, Project line 55) says only "{Supplied links only.}", and `Custom Instructions.md` line 140 lists References in the Epic About. If the operator reads References as optional in an Epic, this grader found no other unmet clause here except the Turn 1 file reading below
- Is `turn-1.md` line 37, "leave this question file unchanged", a file claim under root line 189? It claims no save, write or read-back, but it speaks of a question file

---

## SEP-002 (skill), Epic natural wording

**Draft row**

```csv
SEP-002,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 asked one Epic-lane question and saved only export/001 - Epic-offline-mode-clarification.md; Turn 2 saved export/002 - Epic-offline-mode.md in the house shape with the four areas verbatim, 23% and 31%, Web out and conflict handling left open on 2026-10-09. The Turn 2 read-back was a partial Read (lines 78 to 107) and N=106 against Read's 107, both listed as open readings."
```

**Pass clauses**

| Clause | Met / Unmet | Evidence |
|---|---|---|
| Turn 1 resolves the Epic kind from wording alone | Met | `turn-1.md` line 7 "This is an Epic"; export word `Epic` in `001 - Epic-offline-mode-clarification.md` |
| Turn 1 asks one Epic question in the Epic lane | Met | Clarification file lines 1 to 17, one consolidated question; `turn-1.md` line 3 path, line 4 `Verified:` line, line 5 HVR line |
| Turn 1 drafts nothing | Met | Ledger turn 1 created only the clarification; file holds no draft |
| `# Epic - ` H1, no story preamble | Met | Export line 1 `# Epic - Member - Offline mode`, line 3 `* * *`, line 4 `## About` |
| `## About` with Problem, Goal, Solution, References | Met | Export lines 9, 20, 33, 49 |
| `## Scope` names exactly the four areas verbatim as plain text, each across iOS, Android and Desktop | Met | Export lines 63, 64, 70, 71; line 57 "for iOS, Android and Desktop"; line 7 "Each story covers iOS, Android and Desktop together" |
| Release-level criteria in `1\.` blocks with Mark-as-done | Met | Lines 80, 88, 97; Mark-as-done 86, 95, 104 |
| No `## Requirements`, header fields, story points, INVEST | Met | None in the export |
| Names the kind | Met | `turn-2.md` line 1 "I've written the epic" |
| `23%` and `31%` verbatim | Met | Export lines 14 and 15 |
| Web out of every child story and criterion | Met | Child stories lines 63 to 71 and criteria lines 80 to 104 name no Web; line 41 and line 44 exclude it |
| Conflict handling a dependency on the `2026-10-09` decision | Met | Export lines 61, 66, 68 |
| No plan limit, no altered brief value, no invented link | Met | Line 6 "every plan, Free included"; values checked below; References lines 51 to 53 plain text |

**Blocking items hit**

None.

**Advisory items**

- `turn-1.md` lines 11 to 14 repeat part of the question in chat, which root line 156 leaves ungraded
- Size band: 106 lines, inside 80 to 140

**Read-back table**

| Turn | Export path | N printed | Read after last write | Lines returned | Real `wc -l` |
|---|---|---|---|---|---|
| 1 | `export/001 - Epic-offline-mode-clarification.md` | 18 | `events-turn-1.jsonl` line 49 (after Edit line 47), result line 50 | 1 to 18 of 18 | 17 |
| 2 | `export/002 - Epic-offline-mode.md` | 106 | `events-turn-2.jsonl` line 56 (after last Edit line 50), result line 57 | 78 to 107 of 107, a partial Read with `offset` 78 | 106 |

**Realism entries**

- `export/001 - Epic-offline-mode-clarification.md`, clarification, question only. Facts checked: `2026-10-09` lines 7 and 13 = brief line 32; Desktop wraps the web client and a web change reaches Desktop with no release, line 9 = `loomlist-context.md` lines 12 and 18; a protocol change needs every client on a new version, line 15 = context line 177; "a member" line 17 = brief line 14. No placeholder
- `export/002 - Epic-offline-mode.md`, Epic. Required sections from `assets/epic-template.md` lines 41 to 112 all present; no `#### Added Later`, which the template marks optional (line 118); no Delivery. Facts checked: `23%` line 14 and `31%` line 15 = brief line 8; block-level last-writer-wins on protocol v3 line 17 = brief line 26 and context line 70; Q1 2027 line 6 = brief line 36; "drops by half within 8 weeks of release" line 29 = brief line 40; out-of-scope list lines 44 to 47 = brief lines 45 to 48; Joana, Engineering Manager, Sync, `2026-10-09` line 68 = brief line 32; shared on 2026-09-23 line 52 = brief line 4. No placeholder. H1 carries no discipline code
- Named additions: `turn-2.md` lines 13 to 16 (drafting before the decision, the open Web client question, members only)
- Borderline: criterion 2 (export lines 90 to 93) says every offline change "reaches the workspace ... and teammates see it", which restates the brief Goal (line 14) but could be read as a conflict outcome; export line 68 raises whether a Web client protocol update belongs to the epic as undecided, named at `turn-2.md` line 15. The label `**Direct user/Loomlist benefits:**` (line 24) replaces the template's fixed `Direct user/Barter benefits:`

**Open readings**

- Does a read-back pass when the only Read after the last Edit is partial (`offset` 78, lines 78 to 107 of 107)? The brief's test ("returned file content") is met
- `N` convention (`SKILL.md` line 211): Turn 2 printed 106, the real `wc -l`, where the final line number the Read returned was 107. Turn 1 printed Read's 18 against `wc -l` 17. Which count is meant?

---

## PEP-002 (project), Epic natural wording

**Draft row**

```csv
PEP-002,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Every clause holds except the house shape: the Epic block omits #### **References** (turn-2.md Solution lines 29 to 38 run into ## Scope at line 39, and line 119 says it was left out), which the Pass clause, the Project Epic Template line 53 and kernel line 140 require."
```

**Pass clauses**

| Clause | Met / Unmet | Evidence |
|---|---|---|
| Turn 1 resolves the Epic kind from wording alone | Met | `turn-1.md` line 24 "I'm treating this as an Epic" |
| Turn 1 asks one Epic question in the Epic lane, drafts nothing | Met | `turn-1.md` lines 1 to 18 fenced question block, line 20 `Export-equivalent path: export/001 - Epic-offline-mode-clarification.md`, line 22 HVR line, line 24 "I haven't drafted it yet" |
| `# Epic - ` H1, no story preamble | Met | `turn-2.md` line 2 `# Epic - Member - Offline mode`, line 4 `* * *`, line 5 `## About` |
| `## About` with Problem, Goal, Solution and `#### **References**` | Unmet | Problem line 9, Goal line 18, Solution line 29, then `## Scope` at line 39; line 119 "I left out that section because you haven't shared any links yet" |
| `## Scope` names exactly the four areas verbatim, each across iOS, Android and Desktop | Met | Lines 47, 48, 52, 53; line 41 "covers iOS, Android and Desktop together" |
| Release-level criteria in `1\.` blocks with Mark-as-done | Met | Lines 69, 77, 86, 94; Mark-as-done 75, 84, 92, 101 |
| No `## Requirements`, header fields, story points, INVEST | Met | None in the block |
| Consults only the Epic scaffold | Met | `events-turn-1.jsonl` line 14 Read of the Epic Template; Turn 2 read the Epic example and Conciseness only; no Story Template read |
| Names the kind | Met | `turn-2.md` line 110 "The epic is ready" |
| `23%` and `31%` verbatim | Met | `turn-2.md` line 11 |
| Web out of every child story and criterion | Met | Web only under `#### Out of scope`, line 57; criteria name iOS, Android or Desktop |
| Conflict handling a dependency on `2026-10-09` | Met | Lines 43, 45, 50; criterion 2 line 82 limits itself to changes "that did not conflict" |
| No plan limit, no altered value, no invented link, claims no file | Met | Line 7 "every plan, including Free"; values below; no link; line 106 `Export-equivalent path:` only |

**Blocking items hit**

- Pass clause: `## About` holding `#### **References**` unmet (root line 150)
- Ticket realism, "A required section of the routed template missing" (root line 205): Project Epic Template line 53, `Custom Instructions.md` line 140

**Advisory items**

- Block form: fenced, at the start of both replies, no commentary before it
- Size band: 102 lines, inside 80 to 140

**Realism entries**

- Turn 1 clarification block (`blocks/epics/PEP-002-turn1 - Epic-offline-mode-clarification.md`, 16 lines), question only. Facts checked: `2026-10-09` line 5 = brief line 32; Desktop wraps the web client, line 6 = context line 12; `FE - iOS - OFFL - ...` pattern line 7 = context lines 104 and 125; every client needs the new protocol line 11 = context line 177. No placeholder
- Turn 2 Epic block (`blocks/epics/PEP-002-turn2 - Epic-offline-mode.md`, 102 lines). Required sections from the Project Epic Template: `#### **References**` missing, the rest present. Facts checked: `23%`, `31%` line 11 = brief line 8; 500 pages, blocks, inline databases, to-dos, 1 GB line 32 = brief line 22; within 30 seconds, oldest first line 35 = brief line 26; Joana, `2026-10-09`, #sync-eng line 43 = brief line 32; Q1 2027 line 7 = brief line 36; 8 weeks line 25 = brief line 40; out-of-scope list lines 57 to 60 = brief lines 18 and 45 to 48. No placeholder. H1 carries no discipline code
- Borderline: line 43 "a device that was offline for a day" where the brief says "a phone" (line 26); the label `**Direct user/Loomlist benefits:**` (line 22) replaces the fixed template line and is not named in the reply

**Open readings**

- The same References question as PEP-001: is `#### **References**` optional in an Epic when no link is supplied? The runtime read the Epic example (`events-turn-2.jsonl` line 6), which carries References at its line 45. If the operator reads it as optional, this grader found no other unmet clause here

---

## SEP-003 (skill), Epic quick energy

**Draft row**

```csv
SEP-003,skill,claude-opus-5-5-medium,PASS,1,1,pending,yes,"One turn, no question, one Epic at export/001 - Epic-self-serve-returns.md in the house shape with the four child stories, guest returns under Added Later, pallet items with CS and 60%, Q1 2027, 1,900, 6 days and 30 days as supplied. Borderline: a References link to ../context/fernhouse-context.md and criterion 3's ""as it does today"", both named in the reply."
```

**Pass clauses**

| Clause | Met / Unmet | Evidence |
|---|---|---|
| The one turn asks nothing | Met | `turn-1.md` lines 1 to 17 hold no question; ledger created only the Epic |
| Saves one Epic | Met | Ledger turn 1 `created: export/001 - Epic-self-serve-returns.md` |
| `# Epic - ` H1, no story preamble | Met | Export line 1 `# Epic - Customer - Self-serve returns`, line 3 `* * *`, line 4 `## About` |
| `## About` with Problem, Goal, Solution, References | Met | Export lines 8, 18, 27, 36 |
| `## Scope` names exactly the four prompt child stories as plain text | Met | Export lines 47, 48, 52, 53 |
| `#### Added Later` holds guest returns | Met | Export lines 55 to 60 |
| Release-level criteria in `1\.` blocks with Mark-as-done | Met | Lines 69, 78, 87; Mark-as-done 76, 85, 94 |
| No `## Requirements`, header fields, story points, INVEST | Met | None in the export |
| Names the kind | Met | `turn-1.md` line 1 "I've written the Epic" |
| `60%` and `Q1 2027` verbatim | Met | Export line 20 |
| Context numbers exactly as `fernhouse-context.md` | Met | `1,900` and `6 days` export line 10 = context line 145; `30 days` lines 30, 71, 89 = context line 53 |
| No guest returns or pallet items in first-release scope | Met | Lines 34, 43, 87 to 94 |
| No invented return fee, carrier name or link | Met, borderline on the link | No fee, no carrier; line 39 links `../context/fernhouse-context.md`, the supplied attachment, named at `turn-1.md` line 15 |

**Blocking items hit**

None.

**Advisory items**

- Size band: 96 lines, inside 60 to 110
- `turn-1.md` line 7 notes `validate-output-format.cjs` is not in the sandbox, a true statement about the sandbox copy

**Read-back table**

| Turn | Export path | N printed | Read after last write | Lines returned | Real `wc -l` |
|---|---|---|---|---|---|
| 1 | `export/001 - Epic-self-serve-returns.md` | 96 | `events-turn-1.jsonl` line 44 (after Write line 33 and Bash `sed -i` edit line 39), result line 45 | 1 to 97 of 97 | 96 |

**Realism entry**

- `export/001 - Epic-self-serve-returns.md`, Epic. Required sections from `assets/epic-template.md` lines 41 to 112 all present; no Delivery, as Quick never opts it in. Facts checked: `1,900` a month and `6 days` export line 10 = context line 145; CS agent creates the return in Admin and emails a label, export line 10 = context line 145; `30 days` window line 30 = context line 53; web, iOS and Android line 6 = context lines 13 to 15; a guest has no order history, line 60 = context line 35; `60%`, Q1 2027 line 20 = the prompt. No placeholder. H1 carries no discipline code
- Named additions: `turn-1.md` lines 12 to 15 (Problem bullets from context, criterion 3, the "Returns" segment, the References link)
- Borderline: criterion 3 (export lines 89 to 92) says a return past `30 days` "goes through CS as it does today", which the context does not state (line 145 gives only the 30-day window); named at `turn-1.md` line 13. Problem line 15 says the customer cannot see where a return stands, named at line 12 and supported indirectly by context line 144. The label `**Direct customer and Fernhouse benefits:**` (line 22) replaces the fixed template line

**Open readings**

- Is a relative link to a supplied attachment (`[Fernhouse company context](<../context/fernhouse-context.md>)`, export line 39) an invented link under the Fail clause, given `references/story-mode.md` line 163 ("Links appear only when supplied") and the template slot "{Supplied links only.}" (`epic-template.md` line 74)? It resolves to the staged file and the reply names it
- `N` convention (`SKILL.md` line 211): printed 96, the real `wc -l`, where the Read's final line number was 97

---

## PEP-003 (project), Epic quick energy

**Draft row**

```csv
PEP-003,project,claude-opus-5-5-medium,FAIL,1,1,pending,yes,"No question and a fenced Epic block with the four child stories, guest returns under Added Later and pallet items with CS, but #### **References** is missing (turn-1.md Solution lines 32 to 39 run into ## Scope at line 40, reply line 123), a Pass clause and a required Project Epic Template slot. The format gate also flags prose connective density 3.4 per 1000."
```

**Pass clauses**

| Clause | Met / Unmet | Evidence |
|---|---|---|
| The one turn asks nothing | Met | `turn-1.md` holds one Epic block and no question |
| Renders one Epic | Met | `turn-1.md` lines 1 to 112 fenced block, line 114 `Export-equivalent path: export/001 - Epic-self-serve-returns.md` |
| `# Epic - ` H1, no story preamble | Met | Line 2 `# Epic - Customer - Self-serve returns`, line 4 `* * *`, line 5 `## About` |
| `## About` with Problem, Goal, Solution and `#### **References**` | Unmet | Problem line 10, Goal line 21, Solution line 32, then `## Scope` at line 40; line 123 "No References block ... I left the block out" |
| `## Scope` names exactly the four prompt child stories as plain text | Met | Lines 46, 47, 51, 52 |
| `#### Added Later` holds guest returns | Met | Lines 54 to 59 |
| Release-level criteria in `1\.` blocks with Mark-as-done | Met | Lines 68, 77, 85, 94, 103; Mark-as-done 75, 83, 92, 101, 109 |
| No `## Requirements`, header fields, story points, INVEST | Met | None in the block |
| Consults only the Epic scaffold | Met | `events-turn-1.jsonl` line 8 Read of the Epic Template; no Story Template read |
| Names the kind | Met | Line 118 "**Artifact kind:** Epic" |
| `60%` and `Q1 2027` verbatim | Met | Line 23 |
| Context numbers exactly as the context | Met | `1,900`, `6 days` lines 12 and 15 = context line 145; `30 days` lines 7, 70, 79 = context line 53 |
| No guest returns or pallet items in first-release scope | Met | Lines 42, 54 to 59, 103 to 107 |
| No invented fee, carrier or link; claims no file | Met | None; line 114 `Export-equivalent path:` only |

**Blocking items hit**

- Pass clause: `## About` holding `#### **References**` unmet (root line 150)
- Ticket realism, "A required section of the routed template missing" (root line 205): Project Epic Template line 53, `Custom Instructions.md` line 140

**Advisory items**

- Format gate finding on the block: prose connective density 3.4 per 1000 across 293 prose words (evidence only, no Pass clause names it)
- Block form: fenced, at the start of the reply, no commentary before it
- Size band: 110 lines, at the top of 60 to 110

**Realism entry**

- Epic block (`blocks/epics/PEP-003-turn1 - Epic-self-serve-returns.md`, 110 lines). Required sections from the Project Epic Template: `#### **References**` missing, the rest present; no Delivery. Facts checked: `1,900` and `6 days` line 12 = context line 145; the order page stops at `Shipped`, line 18 = context line 144; `30 days` window lines 7, 70, 79 = context line 53; a guest has no order history, line 59 = context line 35; `60%`, Q1 2027 line 23 = the prompt. No placeholder. H1 carries no discipline code
- Named addition: criterion 2, `turn-1.md` line 125

**Open readings**

- The same References question as PEP-001. If the operator reads Epic References as optional when no link is supplied, this grader found no other unmet clause here

---

## Twin notes

**SEP-001 / PEP-001: differ in why each fails.** The skill drafted in Turn 1; the Project asked first and then dropped References in Turn 2.

- Turn 1 behavior, a runtime fault over a shared rule gap. Both packagings say the same thing: `AGENTS.md` line 283 and `Custom Instructions.md` line 108 both ask one question when scope is missing, and both then list `$task`, `$bug`, `$doc` and `$story` (not `$epic`) as commands that still ask (`AGENTS.md` line 287, `Custom Instructions.md` line 108). The story intake gate matches on both sides (`references/interactive-mode.md` lines 169 to 173, Project Interactive Mode lines 146 to 150) and has no release-cut field. The Project asked and the skill did not, from identical text
- References, a runtime fault. Both sides carry References in the Epic scaffold (`assets/epic-template.md` lines 72 to 78, Project Epic Template lines 53 to 59) and in the Epic draft order (`references/story-mode.md` line 206, Project Story Mode line 182), and the kernel names it (`Custom Instructions.md` line 140). The skill kept it (export line 38); the Project left it out

**SEP-002 / PEP-002: differ.** The skill passes. The Project matches it on every clause but drops `#### **References**`. The rule lines are the ones above and read the same on both sides, so this is a runtime fault. A shared ambiguity may feed it: both Story templates say to omit References when no link is supplied (`assets/story-template.md` line 66, Project Story Template line 47), while both Epic templates leave the slot as "{Supplied links only.}" with no omission rule (`assets/epic-template.md` line 74, Project Epic Template line 55)

**SEP-003 / PEP-003: differ.** The skill passes. The Project drops References and says so (`turn-1.md` line 123). This is the same runtime fault as the two pairs above, with the same rule lines on both sides. All three Project Epics omit References, and all three skill Epics keep it: the skill with plain-text sources (SEP-001, SEP-002) or a link to the context file (SEP-003). The pattern holds for every Project Epic, so the orchestrator may want to raise the Epic References reading once, not three times
