# Grades draft: stories batch

Batch: `SST-001..SST-004` (skill) and `PST-001..PST-004` (Project), run `2026-09-25--manual-testing-playbook--claude-opus-5-5-medium`, Product Owner commit `3023c5e`.

`<RUN>` below is `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`. Scenario files are `AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/{skill,project}-story-modes/<slug>.md`, and every Pass/fail bullet sits on line 35 of its file. `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing, so sources were read from the working tree.

Format gate: `node validate-output-format.cjs --system product-owner <file>` from the Sync Loop folder, no `--write`. Every skill export and every Project block copy printed `Product Owner output format validation passed across 1 artifact file(s)` with exit code 0. Project block copies are in `scratch/grades/blocks/stories/`, named `<ID>-turn<n>-block<k>.md`.

Read-back note for every skill row: each export ends in a newline, so `wc -l` is one lower than the `totalLines` the Read tool reports. The rule (`SKILL.md` line 211, `AGENTS.md` line 46) takes `N` from the final line number Read returns, so the Read figure is the one `N` is checked against.

Shared finding behind six of the eight verdicts: in `SST-002..SST-004` and `PST-002..PST-004`, Turn 1 drafted the artifact without the one Story question the Pass clause requires. `AGENTS.md` line 287 and `Custom Instructions.md` line 108 both say `$story` still asks and waits. Twin notes and Open readings cover why both runtimes skipped it.

---

## SST-001 (skill) Story hard values

**Draft row**

```csv
SST-001,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 saved only the Story-lane question (turn-1.md line 3, read back by Read #12) and Turn 2 saved 002 - Story-free-cancellation-filter.md with all eight hard values in Requirements (export lines 48, 51, 56, 61, 67) and both Guest Support asks as constraints (lines 43, 50). Advisory: 143 file lines against the 70 to 130 band."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question that asks for the Guest Support asks | Met | `turn-1.md` lines 7 to 14, item 1 line 9 `please paste both exactly as Guest Support sent them`. Clarification export line 5 |
| T1 saves only that question in the Story lane | Met | `export/001 - Story-free-cancellation-filter-clarification.md`, 13 lines of question only. `meta.json` turn 1 ledger creates only that file |
| T1 reads it back | Met | `events-turn-1.jsonl` Write #9, Edit #11, then Read #12 of that path returned lines 1 to 14 of 14 |
| T1 replies with path, `Verified:` line and `HVR self-scan:` line | Met | `turn-1.md` lines 3, 4 (`Verified: read-back succeeded; 14 lines`), 5 |
| T1 writes no draft | Met | `turn-1.md` line 1 `I haven't written the Story yet`. No other file in the turn 1 ledger |
| T2 saves one Story on the next number | Met | `export/002 - Story-free-cancellation-filter.md`, turn 2 ledger creates only it. Clarification untouched (no Write or Edit to it in `events-turn-2.jsonl`) |
| T2 reads it back | Met | Last Edit #12, then Read #13 (offset 100) returned lines 100 to 144 of 144 |
| T2 names the Story kind | Met | `turn-2.md` line 1 `as a **Story**` |
| T2 carries the `HVR self-scan:` line | Met | `turn-2.md` line 5 |
| About, Problem, Solution, Expected outcomes, Requirements, numbered Given/When/Then criteria each closed by Mark-as-done | Met | Export lines 7, 13, 17, 21, 27, 80. Criteria 1 to 7 at lines 84 to 141, Mark-as-done lines 91, 100, 108, 117, 125, 133, 141 |
| `Free cancellation until 14 Oct`, `d MMM`, `No stays with free cancellation for these dates`, `Clear filter`, `filter_applied`, `filter_name`, `free_cancellation`, `8.13.0` verbatim in Requirements | Met | Export lines 48, 51, 56 (string and `Clear filter`), 61 (the three tracking values), 67 |
| `312 stays` and `14 days` verbatim or named as left out | Met | Line 38 ``` `312` stays ``` (backticks around the number only, see Open readings), line 49 `14 days before check-in` |
| Both Guest Support asks as constraints | Met | Line 50 `The deadline is the property's local date`, line 43 `The filter stays on when the guest opens a property and goes back to the results` |

**Blocking items hit:** None.

**Advisory items**

- Size band: 143 file lines (Read 144) against 70 to 130.
- Named additions, all covered by `turn-2.md` lines 13 to 16: criterion 6, criterion 7 (`events-collector`), the two expected outcomes.
- Borderline, not decisive: line 38 calls the Lisbon search `Reference search at the kickoff`. The notes say `Our test search` and were written after the kickoff (notes lines 4 and 20), so "at the kickoff" is a light inference.

**Read-back table**

| Turn | Export path | `N` printed | Read after last write, lines returned | `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - Story-free-cancellation-filter-clarification.md` | 14 | Read #12, lines 1 to 14 of 14 (after Edit #11) | 13 |
| 2 | `export/002 - Story-free-cancellation-filter.md` | 144 | Read #13, lines 100 to 144 of 144 (after Edit #12) | 143 |

**Realism entries**

- `export/001 - Story-free-cancellation-filter-clarification.md`, Story-lane clarification. No template sections apply, question only, no draft. Facts: names Tomas's notes of 2026-09-18 (notes line 4), the four exclusions (notes lines 47 to 50). No placeholder. 13 lines. Gate passed.
- `export/002 - Story-free-cancellation-filter.md`, Story. Required sections (skill `assets/story-template.md` lines 40 to 103): preamble, About, Problem, Solution, Expected outcomes, Requirements, Acceptance criteria all present. References omitted with no links supplied (template note, allowed). No `**Open:**` line, no Delivery, correct. Company facts: H1 `Guest - Search - Free cancellation filter` follows `roamstay-context.md` line 85. `filter_applied` with `filter_name` matches line 179. Filter sheet holds Price and Star rating today, line 138. `search-service` owned by Search, line 56. `events-collector`, line 184. No placeholder. 143 lines against 70 to 130 (advisory). Gate passed.

**Open readings**

- Does ``` `312` stays ``` (number backticked, word outside) satisfy "keeps `312 stays` verbatim"? Graded Met because the rendered text reads `312 stays`.
- The Turn 2 read-back was a partial Read (lines 100 to 144). The rule asks for a Read of the exact path that returns non-empty content, which it did. Should a partial Read count as the read-back?

---

## PST-001 (Project) Story hard values

**Draft row**

```csv
PST-001,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 rendered one fenced Story-lane question block asking for the Guest Support asks with its clarification label (turn-1.md lines 1 to 17) and no draft, and Turn 2 rendered the Story block with every hard value in Requirements (turn-2.md lines 44, 47, 52, 58, 63) and both asks (lines 39, 46), claiming no file. Advisory: block body 131 lines, one over the 70 to 130 band."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question that asks for the Guest Support asks | Met | Block `turn-1.md` lines 2 to 14, line 6 `Paste both asks as Guest Support wrote them` |
| T1 renders it as its own block | Met | Fenced ` ```markdown ` block, lines 1 to 15, at the very start of the reply |
| T1 `Export-equivalent path:` in the Story lane | Met | Line 17 `export/NNN - Story-free-cancellation-filter-clarification.md` |
| T1 `HVR self-scan:` line | Met | Line 19 |
| T1 renders no draft | Met | Line 21 `I've held off drafting until the two Guest Support asks arrive` |
| T2 renders one Story block with its `Export-equivalent path:` | Met | Fenced block lines 1 to 133, line 135 `export/NNN - Story-free-cancellation-filter.md` |
| T2 names the Story kind | Met | Line 139 `I wrote this as a **Story**` |
| T2 `HVR self-scan:` line | Met | Line 137 |
| T2 claims no file | Met | No saved, written, read-back or file wording outside the block in either turn |
| About, Problem, Solution, Expected outcomes, Requirements, numbered Given/When/Then criteria each closed by Mark-as-done | Met | Block lines 8, 12, 16, 20, 28, 76. Criteria 1 to 6 at lines 80 to 130, Mark-as-done lines 87, 96, 104, 113, 122, 130 |
| Eight hard values verbatim in Requirements | Met | Lines 44 (`Free cancellation until 14 Oct`), 47 (`d MMM`), 52 (empty-state string and `Clear filter`), 58 (`filter_applied`, `filter_name`, `free_cancellation`), 63 (`8.13.0`) |
| `312 stays` and `14 days` | Met | Line 37 ``` `312` stays ```, line 45 `` `14 days` `` |
| Both Guest Support asks as constraints | Met | Line 46 `The deadline is the date at the property's location, not the date on the guest's device`, line 39 `The filter stays on when the guest opens a property and goes back to the results` |

**Blocking items hit:** None.

**Advisory items**

- Size band: block body 131 lines against 70 to 130.
- Block form: fenced in both turns. No commentary before either block.
- Named additions, covered by `turn-2.md` lines 150 to 153: expected outcomes 2 and 3, the `And` line of criterion 2, criterion 3.
- Borderline, not decisive: criterion 2 (line 93) says `written in the guest's language` where the notes say locale. Requirements line 47 keeps the notes' `d MMM` in the guest's locale, and the reply asks about it (line 142).
- Line 46 adds `not the date on the guest's device`, which is the direct negation of the supplied ask and so not an addition (brief section 2).

**Realism entries**

- Block `PST-001-turn1-block1.md`, Story-lane clarification, fenced. Question only. Facts: the notes' exclusions (notes lines 47 to 50), the filter persistence rule (notes line 21), Ines's frames (notes line 52). No placeholder. 13 lines. Gate passed.
- Block `PST-001-turn2-block1.md`, Story. Required sections (Project `Product Owner - Assets - Story Template - v0.100.md`, scaffold identical to the skill asset): preamble, About, Problem, Solution, Expected outcomes, Requirements, Acceptance criteria present, References omitted with no links, no Delivery. Company facts: H1 matches `roamstay-context.md` line 85, `filter_applied`/`filter_name` line 179, Price and Star rating line 138, `search-service` line 56. No placeholder. 131 lines against 70 to 130 (advisory). Gate passed.

**Open readings**

- Same `312 stays` reading as `SST-001`.

---

## SST-002 (skill) Story forced delivery

**Draft row**

```csv
SST-002,skill,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 drafted and saved export/001 - Story-view-only-share-links.md with no Story question (turn-1.md lines 1 and 7: ""I didn't ask a question first""), so no clarification exists and Turn 2 edited 001 in place instead of saving on the next number. The **Open:** line also rewords `Do sub-pages inherit the link?` (export line 36). Advisory: 179 lines against 90 to 170, and N 176 printed against Read's 177."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question | Unmet | `turn-1.md` line 7 `I didn't ask a question first because the notes already give the role, the value and every requirement` |
| T1 saves only that question in the Story lane | Unmet | Turn 1 ledger creates `export/001 - Story-view-only-share-links.md`, a full Story. No `-clarification` file exists |
| T1 reads it back | Unmet | No clarification to read. Read #12 read back the Story |
| T1 replies with path, `Verified:` and `HVR self-scan:` for the question | Unmet | The lines at 3 to 5 belong to the Story, not a question |
| T1 no draft | Unmet | `turn-1.md` line 1 `I've written the Story from Kofi's notes and saved it` |
| T2 saves one Story on the next number | Unmet | Turn 2 ledger modifies `export/001 - Story-view-only-share-links.md` only (Edits #2 to #5). No new number |
| T2 reads it back | Met | Read #6, lines 1 to 180 of 180, after the last Edit #5 |
| T2 names the Story kind | Met | `turn-2.md` line 1 `It's still a Story` |
| T2 `HVR self-scan:` line | Met | `turn-2.md` line 5 |
| About, Problem, Solution, Expected outcomes, Requirements, criteria with Mark-as-done, closing `## Delivery` with Estimation, Rabbit holes, No-gos in order | Met | Export lines 7, 13, 19, 23, 32, 79. Criteria 1 to 8 at lines 85 to 156, each closed by Mark-as-done. Delivery line 160, Estimation 162, Rabbit holes 168, No-gos 174 |
| Requirements carry `Anyone with the link can view`, `Never`, `7 days`, `30 days`, `60 seconds`, `3 active links`, `Free`, `Plus`, `Team`, `noindex`, `Duplicate` | Met | Lines 44, 47 and 48, 50 and 51, 59 (``` `3` active links ```) and 63 (`3 active links` inside the limit string), 59 to 62, 74, 72 |
| `**Open:**` line carries `Do sub-pages inherit the link?` and names Lena | Unmet (string) / Met (Lena) | Line 36 `**Open:** whether a link on a page also opens its sub-pages is not decided` rewords the backticked question from `loomlist-view-only-links-design-notes.md` line 46. Lena named on line 36 |
| Rabbit holes repeat that question | Met in substance | Line 172 `Sub-page inheritance is not decided`, reworded |
| No acceptance criterion asserts how sub-pages behave | Met | Criteria at lines 85 to 156 never mention sub-pages |

**Blocking items hit**

- Pass clauses missed in Turn 1 and Turn 2 (drafted in Turn 1, no Story-lane clarification, no next number): root line 150, with `AGENTS.md` line 287.
- Side-effect ledger: a clarification turn may create only the `-clarification` export (root line 106). Turn 1 created the Story.
- Protected fact: `Do sub-pages inherit the link?` is a hard value the Pass clause lists verbatim and it was reworded (brief section 2, root line 188).

**Advisory items**

- Size band: 179 file lines (Read 180) against 90 to 170.
- Wrong `N` in Turn 1: printed 176 (`turn-1.md` line 4), Read #12 returned final line 177. Recorded only.
- Named additions, covered by `turn-1.md` lines 13 to 17.
- Borderline, not decisive: line 38 `until the open question is settled it opens that page only` and Rabbit holes line 172 `Build against a single page until then`. Fixture line 54 says the frames show a single page until then, so this may be source-backed, or it may be the Fail example "settles the sub-page question either way".

**Read-back table**

| Turn | Export path | `N` printed | Read after last write, lines returned | `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - Story-view-only-share-links.md` | 176 | Read #12 (offset 160), lines 160 to 177 of 177, after Write #10 | Not on disk in this state (edited in Turn 2) |
| 2 | `export/001 - Story-view-only-share-links.md` | 180 | Read #6, lines 1 to 180 of 180, after Edit #5 | 179 |

**Realism entries**

- `export/001 - Story-view-only-share-links.md`, Story. Required sections present: preamble, About, Problem, Solution, Expected outcomes, Requirements, Acceptance criteria, and Delivery, which the `**Open:**` line forces (`story-template.md` section 3, `story-mode.md` line 74). Company facts: H1 `Member - Sharing - View-only links` follows `loomlist-context.md` line 112. Problem `Pages are shared by invite only` matches line 179. Lena as PM of Sharing and Notifications, line 88. Plan names Free, Plus, Team, lines 35 to 37. No placeholder beyond the exempt `TBD...` Delivery slots. 179 lines against 90 to 170 (advisory). Gate passed.

**Open readings**

- Does rewording `Do sub-pages inherit the link?` in the `**Open:**` line miss the clause, when the backticked question is otherwise carried in substance? Graded Unmet.
- Is "build against a single page until then" (lines 38, 172) settling the sub-page question, given fixture line 54?
- Wrong `N` (176 against Read's 177), listed per the brief.

---

## PST-002 (Project) Story forced delivery

**Draft row**

```csv
PST-002,project,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 rendered the full Story with no Story question, saying Kofi's notes ""gave enough to draft it without asking you anything first"" (turn-1.md line 187), so every Turn 1 clause is missed. The **Open:** line also rewords `Do sub-pages inherit the link?` (turn-2.md line 34). Advisory: block body 180 lines against 90 to 170."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question | Unmet | `turn-1.md` line 187 `Kofi's notes gave enough to draft it without asking you anything first` |
| T1 renders it as its own block with its Story-lane `Export-equivalent path:` and HVR line | Unmet | The block at lines 1 to 181 is a full Story. Line 183 labels `export/NNN - Story-member-sharing-view-only-links.md`, not a `-clarification` name |
| T1 renders no draft | Unmet | Lines 1 to 181 |
| T2 renders one Story block with its `Export-equivalent path:` | Met | Fenced block lines 1 to 182, path line 184 |
| T2 names the Story kind | Met | Line 188 `I've updated the **Story**` |
| T2 `HVR self-scan:` line | Met | Line 186 |
| T2 claims no file | Met with a borderline line | Line 188 `It replaces the previous version under the same filename`. No save, write or read-back claim. See Open readings |
| Sections through a closing `## Delivery` with Estimation, Rabbit holes, No-gos in order | Met | Block lines 8, 12, 16, 20, 30, 71. Criteria 1 to 9 at lines 77 to 158, each closed by Mark-as-done. Delivery 162, Estimation 164, Rabbit holes 170, No-gos 176 |
| Eleven values verbatim in Requirements | Met | Lines 36, 39, 41 and 42, 49 and 54, 49 to 51, 66, 64 and 65 |
| `**Open:**` line carries `Do sub-pages inherit the link?` and names Lena | Unmet (string) / Met (Lena) | Line 34 `It is not decided whether a link on a page also opens its sub-pages`. Lena named on line 34 |
| Rabbit holes repeat that question | Met in substance | Line 174 `Sub-page inheritance is still open` |
| No criterion asserts sub-page behavior | Met | Criteria at lines 77 to 158 never mention sub-pages |

**Blocking items hit**

- Turn 1 Pass clauses missed (drafted before asking): root line 150, with `Custom Instructions.md` line 108.
- Protected fact: `Do sub-pages inherit the link?` reworded (brief section 2, root line 188).

**Advisory items**

- Size band: block body 180 lines against 90 to 170.
- Block form: fenced in both turns, no commentary before a block.
- Named additions, covered by `turn-1.md` lines 191 to 195: criteria 2 and 3, the Duplicate reading.

**Realism entries**

- Block `PST-002-turn1-block1.md`, Story (superseded in Turn 2). Same sections as below. 179 lines. Gate passed.
- Block `PST-002-turn2-block1.md`, Story. Required sections present, Delivery forced by the `**Open:**` line. Company facts: H1 follows `loomlist-context.md` line 112, Problem matches line 179 and line 167, Lena line 88, plans lines 35 to 37. Agencies on Plus from Turn 2. No placeholder beyond exempt `TBD...`. 180 lines against 90 to 170 (advisory). Gate passed.

**Open readings**

- Same rewording question as `SST-002`.
- Does `It replaces the previous version under the same filename` (line 188) count as a file claim under root line 189? Graded not a claim, since it says nothing was saved, written or read back.

---

## SST-003 (skill) Story refinement

**Draft row**

```csv
SST-003,skill,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 skipped the Story question and saved the refinement at once (turn-1.md line 1, events-turn-1 Write #12), so no Story-lane clarification exists. Turn 2 otherwise met the refinement name, shape and values under export/fernhouse-save-card-draft.md with the source untouched. facts_intact is no because the draft's stored brand became an **Open:** line (export line 42, see Open readings). Advisory: 151 lines against 70 to 130."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question | Unmet | `turn-1.md` line 1 `I've rebuilt Priya's draft as a house-format **Story**` |
| T1 saves only that question in the Story lane | Unmet | Turn 1 ledger creates `export/fernhouse-save-card-draft.md`. No `-clarification` file |
| T1 reads it back, replies with path, `Verified:`, HVR for the question | Unmet | Lines 3 to 5 report the refinement, not a question |
| T1 no draft | Unmet | `events-turn-1.jsonl` Write #12 of the refinement |
| T2 saves the refinement as `export/fernhouse-save-card-draft.md` | Met | Turn 2 ledger modifies that path, no number, no artifact word |
| T2 reads it back | Met | Last Edit #7, then Read #8 (offset 140), lines 140 to 152 of 152 |
| T2 names the Story kind | Met | `turn-2.md` line 1 `the **Story**` |
| T2 `HVR self-scan:` line | Met | `turn-2.md` line 5 |
| Leaves `context/fernhouse-save-card-draft.md` unchanged | Met | No Write, Edit or write-capable Bash touches `context/` in either stream (the only context commands are `cat`). Ledgers list no context change. Staged sha256 `c39e2440...` equals the fixture's |
| H1 with no `PRD -` prefix | Met | Export line 1 `# Customer - Checkout - Save card for next time` |
| No `**Checklist**` and no `- [ ]` build item in Requirements | Met | Requirements lines 26 to 67 hold none. The only `- [ ]` lines are Mark-as-done |
| Checklist content carried as bold-lead constraint groups | Met | Line 37 sixth card refused, line 44 stored fields, line 60 `Remove this card?`, line 64 the three events, line 30 platforms |
| `## Acceptance criteria` of numbered Given/When/Then each closed by Mark-as-done | Met | Line 69, criteria 1 to 6 at lines 75 to 128 |
| Every supplied value verbatim | Met | `Save this card for next time` 31, `unchecked by default` 32, `You can save up to 5 cards` 36, `Card ending 7031` and `Expires 08/28` 49, `CVC` and `€150` 51, `£130` 52, `Account > Payment methods` 58, `Remove this card?` 60, `guest checkout` 34 (as `Guest checkout`), Turn 2 copy 54, order-total rule 51 and 52 |

**Blocking items hit**

- Turn 1 Pass clauses missed: root line 150, with `AGENTS.md` line 287 (`$s` is the `$story` alias, `story-mode.md` line 59).
- Side-effect ledger: Turn 1 created the refinement where only a `-clarification` export is allowed (root line 106).

**Advisory items**

- Size band: 151 file lines (Read 152) against 70 to 130.
- Named additions, covered by `turn-1.md` lines 21 to 26 and `turn-2.md` line 14: all criteria, the `7031`/`08/28` format line, the NL, BE, DE and FR scope of `€150`, the tracking-plan rule, the named deciders, criterion 4.
- `turn-1.md` line 28 offers to push the Story "as a task". The kind named on line 1 is Story, so this reads as the ClickUp object and is not graded as a wrong artifact word.

**Read-back table**

| Turn | Export path | `N` printed | Read after last write, lines returned | `wc -l` |
|---|---|---|---|---|
| 1 | `export/fernhouse-save-card-draft.md` | 146 | Read #14 (offset 140), lines 140 to 146 of 146, after Write #12 | Not on disk in this state (edited in Turn 2) |
| 2 | `export/fernhouse-save-card-draft.md` | 152 | Read #8 (offset 140), lines 140 to 152 of 152, after Edit #7 (a `sed -i` Bash #5 also wrote it earlier) | 151 |

**Realism entries**

- `export/fernhouse-save-card-draft.md`, Story refinement. Required sections present: preamble, About, Problem, Solution, Expected outcomes, Requirements, Acceptance criteria, and Delivery forced by the brand `**Open:**` line. Figures 17%, 9%, 68% unaltered (line 13). Company facts: H1 follows `fernhouse-context.md` line 95. Card-data rule, line 153, raised as a conflict at line 42. Tracking-plan rule, line 164, at line 65. Web, iOS, Android from the draft, line 11. No placeholder beyond exempt `TBD...`. 151 lines against 70 to 130 (advisory). Gate passed.

**Open readings**

- The draft stores `token, brand, last four and expiry only` (draft line 48) and `fernhouse-context.md` line 153 allows only token, last four and expiry. The runtime kept the context rule in the requirement (line 44) and marked brand `**Open:**` (line 42). Is that correct handling of a conflict between two attachments, or a supplied draft value altered? The scenario's Expected signals expect brand stored. Not decisive here.
- Does `Guest checkout` at the start of a sentence (line 34) satisfy the verbatim `guest checkout`? Graded Met.

---

## PST-003 (Project) Story refinement

**Draft row**

```csv
PST-003,project,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 rendered the refined Story with no Story question (turn-1.md lines 1 to 162, line 168 ""I rebuilt Priya's draft""), so every Turn 1 clause is missed. Turn 2 carried every listed value and the order-total rule under Export-equivalent path export/fernhouse-save-card-draft.md (turn-2.md line 171). facts_intact is no for the same brand-storage handling as SST-003. Advisory: block body 167 lines against 70 to 130."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question | Unmet | `turn-1.md` line 168 `I rebuilt Priya's draft in the house format` |
| T1 renders it as its own block with a Story-lane `Export-equivalent path:` and HVR line | Unmet | Line 164 labels `export/fernhouse-save-card-draft.md`, the refinement, not a `-clarification` name |
| T1 renders no draft | Unmet | Block lines 1 to 162 is the full refinement |
| T2 renders one refined Story block with `Export-equivalent path: export/fernhouse-save-card-draft.md` | Met | Fenced (four backticks) block lines 1 to 169, path line 171 |
| T2 names the Story kind | Met | Line 175 `**Artifact kind:** Story` |
| T2 `HVR self-scan:` line | Met | Line 173 |
| T2 claims no file | Met | No save, write or read-back wording |
| H1 with no `PRD -` prefix | Met | Block line 2 |
| No `**Checklist**` and no `- [ ]` build item in Requirements | Met | Requirements lines 28 to 64 hold none |
| Checklist content as bold-lead constraint groups | Met | Lines 37, 57, 51, 61 and 62, 34 |
| `## Acceptance criteria` of numbered Given/When/Then each closed by Mark-as-done | Met | Line 66, criteria 1 to 8 at lines 72 to 145 |
| Every supplied value verbatim | Met | Lines 32, 33, 36, 43 (`Card ending 7031`, `Expires 08/28`), 44 (`CVC`, `€150`, `£130`, order-total rule), 50, 51, 35 (`Guest checkout`), 46 (Turn 2 copy) |

**Blocking items hit**

- Turn 1 Pass clauses missed: root line 150, with `Custom Instructions.md` line 108.

**Advisory items**

- Size band: block body 167 lines against 70 to 130.
- Block form: fenced with four backticks in both turns, no commentary before a block.
- Named additions, covered by `turn-1.md` lines 187 to 191 and `turn-2.md` line 182.

**Realism entries**

- Block `PST-003-turn1-block1.md`, Story refinement (superseded). Two `**Open:**` lines, Delivery forced. 160 lines. Gate passed.
- Block `PST-003-turn2-block1.md`, Story refinement. Required sections present, Delivery forced by the brand `**Open:**` line (line 55). Figures 17%, 9%, 68% unaltered (line 14). Company facts: H1 follows `fernhouse-context.md` line 95, card-data rule line 153 at line 55, tracking-plan rule line 164 at line 62, draft surfaces line 11. No placeholder beyond exempt `TBD...`. 167 lines against 70 to 130 (advisory). Gate passed.

**Open readings**

- Same brand-storage reading and `Guest checkout` reading as `SST-003`.

---

## SST-004 (skill) Story with nested tasks

**Draft row**

```csv
SST-004,skill,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 asked nothing and saved a seven-file bundle with six tasks, including 001.2 - task-packed-status.md and 001.6 - task-tracking-timeline-events.md (turn-1.md lines 1 to 22), so no Story-lane clarification exists. Turn 2 repaired the folder in place to the named four with correct Tasks and Story blocks. Advisory: Story 195 lines against 80 to 150."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question in the Story lane | Unmet | `turn-1.md` line 1 `Hamid's brief already names the task split ... so I wrote it without asking you anything first` |
| T1 saves only the question as `export/[###] - Story-[description]-clarification.md` at the top of `export/` | Unmet | Turn 1 ledger creates seven files in `export/001 - Story-order-tracking/`. No clarification |
| T1 reads it back, replies with path, `Verified:`, HVR | Unmet | Lines 3 to 24 report the bundle |
| T1 no draft and no folder | Unmet | Writes #15 to #21 in `events-turn-1.jsonl` |
| T2 saves one folder on the next number | Unmet | The folder `001 - Story-order-tracking/` was created in Turn 1. With no clarification there is no next number |
| Folder holds the Story and exactly four tasks `.1` to `.4` for FE iOS, FE Android, FE web, BE webhook in order | Met (final state) | `001.1 - task-ios-tracking-timeline.md`, `001.2 - task-android-tracking-timeline.md`, `001.3 - task-web-tracking-timeline.md`, `001.4 - task-tracking-webhook.md` |
| T2 reads every file back | Met | Reads #19 to #23, each after that file's last write (see table) |
| T2 replies with every path, Story first, each with its own `Verified:` line | Met | `turn-2.md` lines 3 to 16 |
| One `HVR self-scan:` line for the bundle | Met | `turn-2.md` line 18 |
| Names the Story kind | Met | `turn-2.md` line 26 `the Story has no Open lines left`, every path carries `Story-` |
| Leaves the clarification untouched outside the folder | Unmet | No clarification was ever saved |
| Story holds About, Problem, Solution, Expected outcomes, `#### **Tasks**` inside About with one bullet per task in order linking `(<[###].[n] - task-...md>)`, Requirements, numbered criteria with Mark-as-done | Met | Story lines 7, 11, 17, 21, 26 to 31 (four bullets in n order), 34, 104. Criteria 1 to 7 at lines 108 to 165 |
| Each task holds `### About`, a `**Story**` block linking `(<001 - Story-order-tracking.md>)`, no `**Parent task**`, `### Requirements` | Met | FE tasks lines 3, 9 to 13, 23. Webhook lines 3, 11 to 15, 25. `grep` finds no `Parent task` in the folder |
| Bundle carries the six statuses, five codes and every listed value verbatim | Met | Story line 38 (statuses), 41 to 44 (codes), 53 (`Arriving Thursday 1 October`, `Between 10:00 and 14:00`), 65 (`90 days`), 69 (`30 kg`, `120 cm`), 84, 85, 87, 90, 48, 54, 89 (`5 attempts`, `1 min, 5 min, 15 min, 1 h, 6 h`). Webhook task lines 7, 37 to 40 |

**Blocking items hit**

- Turn 1 Pass clauses missed: root line 150, with `AGENTS.md` line 287 and `story-mode.md` line 406 (no split in the request means the question asks for it).
- Fail example hit in Turn 1: `adds a Packed or DATA task` (scenario line 35). Turn 1 wrote `001.2 - task-packed-status.md` and `001.6 - task-tracking-timeline-events.md` (turn 1 ledger), deleted in Turn 2.
- Side-effect ledger: Turn 1 created a folder where only a `-clarification` export is allowed (root line 106).

**Advisory items**

- Size band: Story 195 file lines (Read 196) against 80 to 150. Tasks 72, 72, 72 and 84 lines, inside 35 to 90.
- Discipline codes present on all task titles (`FE - iOS - TRACK - ...`, `BE - TRACK - ...`), following `fernhouse-context.md` line 93.
- Delivery kept after both `**Open:**` lines were settled. The reply names it and asks (`turn-2.md` line 28). No-gos hold the brief's list plus the two Turn 2 exclusions, so it is not all placeholder.
- Named additions, covered by `turn-2.md` line 28 and `turn-1.md` lines 32 to 39: three Rabbit holes.
- Borderline, not decisive: FE tasks translate `Status and estimate text` (task line 72). The brief says `Status text is translated` (brief line 44), and PST-004 asked about the estimate lines instead.

**Read-back table**

| Turn | Export path | `N` printed | Read after last write, lines returned | `wc -l` |
|---|---|---|---|---|
| 1 | `001 - Story-order-tracking/001 - Story-order-tracking.md` | 205 | Read #26 (offset 195), 195 to 205 of 205, after Edit #24 | Superseded |
| 1 | `001.1 - task-tracking-webhook.md` | 86 | Read #27, 80 to 86 of 86 | Superseded (renamed) |
| 1 | `001.2 - task-packed-status.md` | 36 | Read #28, 30 to 36 of 36 | Deleted in Turn 2 |
| 1 | `001.3 - task-web-tracking-timeline.md` | 75 | Read #29, 70 to 75 of 75 | Superseded |
| 1 | `001.4 - task-ios-tracking-timeline.md` | 74 | Read #30, 70 to 74 of 74 | Superseded (renamed) |
| 1 | `001.5 - task-android-tracking-timeline.md` | 74 | Read #31, 70 to 74 of 74 | Superseded (renamed) |
| 1 | `001.6 - task-tracking-timeline-events.md` | 39 | Read #32, 34 to 39 of 39 | Deleted in Turn 2 |
| 2 | `001 - Story-order-tracking/001 - Story-order-tracking.md` | 196 | Read #19, 1 to 196 of 196, after Edit #10 | 195 |
| 2 | `001.1 - task-ios-tracking-timeline.md` | 73 | Read #20, 68 to 73 of 73, after Write #14 | 72 |
| 2 | `001.2 - task-android-tracking-timeline.md` | 73 | Read #21, 68 to 73 of 73, after Write #15 | 72 |
| 2 | `001.3 - task-web-tracking-timeline.md` | 73 | Read #22, 68 to 73 of 73, after Write #16 | 72 |
| 2 | `001.4 - task-tracking-webhook.md` | 85 | Read #23, 80 to 85 of 85, after Write #17 | 84 |

**Realism entries**

- `001 - Story-order-tracking.md`, Story. Required sections present. References omitted with no links. Tasks block placed after Expected outcomes, which the rule allows when References is absent. Company facts: H1 `Customer - Order page - Order tracking` follows `fernhouse-context.md` line 95. `Packed` via orders-service matches line 72. Pallet carrier sends no tracking events, line 74 and line 150. Six locales match lines 128 to 132. No placeholder beyond exempt `TBD...`. 195 lines against 80 to 150 (advisory). Gate passed.
- `001.1 - task-ios-tracking-timeline.md`, Task. `### About`, `**Story**`, `**Related tasks**`, `### Requirements` present, no `**Parent task**`. Facts: `TRACK` code, line 105. Title pattern, line 93. Frame name from Turn 2. 72 lines inside 35 to 90. Code `FE`. Gate passed.
- `001.2 - task-android-tracking-timeline.md`, Task. Same shape and facts as `001.1`, 72 lines, code `FE`. Gate passed.
- `001.3 - task-web-tracking-timeline.md`, Task. Same shape, web layout in the same frame per Turn 2 (line 7), 72 lines, code `FE`. Gate passed.
- `001.4 - task-tracking-webhook.md`, Task. `### About`, `**Story**`, `**Related tasks**`, `### Requirements`, no `**Parent task**`. Facts: shipping-service owns tracking intake, `fernhouse-context.md` line 65. `TRACK`, line 105. BE drops the surface segment, line 93. Every API value from `fernhouse-carrier-tracking-api-facts.md` lines 7, 43 to 46. 84 lines inside 35 to 90. Code `BE`. Gate passed.
- The two Turn 1 files deleted in Turn 2 (`001.2 - task-packed-status.md`, `001.6 - task-tracking-timeline-events.md`) are not on disk, so the gate could not run on them.

**Open readings**

- Does a task list inside an attached brief (`fernhouse-order-tracking-pm-brief.md` lines 54 to 61) count as "a split the request names" under `SKILL.md` line 252 and `story-mode.md` line 406? The scenario says the request names none. Graded by the scenario. The `$story` ask-first rule (`AGENTS.md` line 287) applies either way.

---

## PST-004 (Project) Story with nested tasks

**Draft row**

```csv
PST-004,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Confirmed from turn-1.md: Turn 1 rendered seven fenced blocks, a Story plus six tasks including BE - TRACK - Packed status from the warehouse system (line 28) and DATA - TRACK - Tracking timeline events (line 32), with no Story question. That misses the Turn 1 clauses and hits the Fail example of a Packed or DATA task. Turn 2 rendered the correct five-block bundle. Advisory: Story block 178 lines against 80 to 150."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question in the Story lane | Unmet | `turn-1.md` line 600 `I wrote a **Story** ... plus six tasks following the split in Hamid's brief`. No question anywhere in the reply |
| T1 renders it as its own block with its `Export-equivalent path:` outside any folder and the HVR line | Unmet | Seven artifact blocks, labels at lines 194, 277, 314, 394, 475, 556, 596, all inside `export/NNN - Story-order-tracking-timeline/` |
| T1 renders no draft | Unmet | Story block lines 1 to 193, then six task blocks. Tasks block lines 25 to 32 lists six tasks |
| T2 renders one Deliverable Block per file, Story first | Met | Fenced blocks at lines 1 to 180, 183 to 252, 255 to 324, 327 to 396, 399 to 478 |
| Exactly four task blocks for FE iOS, FE Android, FE web, BE webhook in that order | Met | Block H1s at lines 184, 256, 328, 400 |
| Each followed by its own `Export-equivalent path:` inside `export/[NNN] - Story-[description]/` | Met | Lines 181, 253, 325, 397, 479 |
| One `HVR self-scan:` line for the set | Met | Line 481 |
| Names the Story kind | Met | Line 483 `I updated the **Story**` |
| Claims no file | Met with a borderline line | Line 483 `this set replaces the earlier seven files`. No save, write or read-back claim. See Open readings |
| Story holds About, Problem, Solution, Expected outcomes, `#### **Tasks**` inside About with one bullet per task in order linking `(<[NNN].[n] - task-...md>)`, Requirements, criteria with Mark-as-done | Met | Block lines 8, 12, 16, 20, 25 to 30, 34, 89. Criteria 1 to 7 at lines 93 to 151 |
| Each task holds `### About`, a `**Story**` block linking `(<NNN - Story-order-tracking-timeline.md>)`, no `**Parent task**`, `### Requirements` | Met | FE iOS lines 186, 200 to 204, 214. FE Android 258, 272 to 276, 286. FE web 330, 344 to 348, 358. BE 402, 408 to 412, 422. No `Parent task` in the reply |
| Set carries the statuses, codes and every listed value verbatim | Met | Story lines 39, 42 and 43, 54, 55, 63, 64, 70, 72, 75, 57, 53, 74 |

**Blocking items hit**

- Turn 1 Pass clauses missed: root line 150, with `Custom Instructions.md` line 108 and Project `Product Owner - Templates - Story Mode - v0.402.md` line 382.
- Fail example hit in Turn 1: `adds a Packed or DATA task` (scenario line 35), at `turn-1.md` lines 28, 32, 280 and 559.

**Advisory items**

- Size band: Story block 178 lines against 80 to 150. Task blocks 68, 68, 68, 78 inside 35 to 90.
- Block form: fenced in both turns. Each block's `Export-equivalent path:` follows its closing fence with no blank line. No commentary before the first block.
- Discipline codes present on every task title.
- Delivery kept after both open questions were settled. Named, with a question to the user, at line 493.

**Realism entries**

| Block | Kind | Sections | Facts checked | Lines (band) | Code | Gate |
|---|---|---|---|---|---|---|
| `PST-004-turn1-block1.md` | Story (superseded) | All present, two `**Open:**` lines, Delivery forced | H1 line 95, `TRACK` line 105, locales lines 128 to 132 | 191 (80 to 150) | n/a | Passed |
| `PST-004-turn1-block2.md` | Task, BE webhook | About, Story, Related tasks, Requirements | shipping-service line 65, API facts lines 43 to 46 | 79 | BE | Passed |
| `PST-004-turn1-block3.md` | Task, BE Packed (the Fail example) | About, Story, Related tasks, Requirements | warehouse reports packed line 72 | 33 (under 35) | BE | Passed |
| `PST-004-turn1-block4.md` | Task, FE web | About, References, Story, Related tasks, Requirements | frame name brief line 30 | 76 | FE | Passed |
| `PST-004-turn1-block5.md` | Task, FE iOS | Same | Same | 77 | FE | Passed |
| `PST-004-turn1-block6.md` | Task, FE Android | Same | Same | 77 | FE | Passed |
| `PST-004-turn1-block7.md` | Task, DATA (the Fail example) | About, Story, Related tasks, Requirements | tracking-plan rule line 164, event properties line 162 | 36 | DATA | Passed |
| `PST-004-turn2-block1.md` | Story | All present, Tasks block after Expected outcomes (no References), Delivery kept | H1 `Customer - Order tracking - Order page timeline` line 95, `Packed` via orders-service line 72, pallet no tracking lines 74 and 150, locales lines 128 to 132 | 178 (80 to 150) | n/a | Passed |
| `PST-004-turn2-block2.md` | Task, FE iOS | About, References, Story, Related tasks, Requirements, no Parent task | `TRACK` line 105, title pattern line 93, frame from Turn 2 | 68 | FE | Passed |
| `PST-004-turn2-block3.md` | Task, FE Android | Same | Same | 68 | FE | Passed |
| `PST-004-turn2-block4.md` | Task, FE web | Same, web layout in the same frame (line 334) | Same | 68 | FE | Passed |
| `PST-004-turn2-block5.md` | Task, BE webhook | About, Story, Related tasks, Requirements, no Parent task | shipping-service line 65, BE drops surface line 93, API facts lines 7 and 43 to 46 | 78 | BE | Passed |

Placeholders: only the exempt `TBD...` and the Project `NNN` slot, which the links inside the blocks also use.

**Open readings**

- Do `They're one folder with seven files` (`turn-1.md` line 600) and `this set replaces the earlier seven files` (`turn-2.md` line 483) count as file claims under root line 189? Graded not claims, since neither says anything was saved, written or read back. Not decisive here.
- Same brief-named split reading as `SST-004`.

---

## Twin notes

| Pair | Verdicts | Agree or differ | Notes |
|---|---|---|---|
| `SST-001` / `PST-001` | PASS / PASS | Agree | Both asked one Story question for the promised Guest Support asks and waited, then delivered every hard value in Requirements. The promised-input rule is stated on both sides (`AGENTS.md` line 283, `Custom Instructions.md` line 108). |
| `SST-002` / `PST-002` | FAIL / FAIL | Agree | Both drafted in Turn 1 on `$story` without the Story question, and both reworded `Do sub-pages inherit the link?` in the `**Open:**` line. Small difference: the skill Story adds an interim single-page build rule (export lines 38 and 172), and the Project Story does not. |
| `SST-003` / `PST-003` | FAIL / FAIL | Agree | Both refined at once on `$s` without the Story question. Both then met the refinement name, shape and values, and both raised the brand-storage conflict with `fernhouse-context.md` line 153 as an `**Open:**` line. |
| `SST-004` / `PST-004` | FAIL / FAIL | Agree | Both treated the brief's six-task list as the named split and delivered six tasks, Packed and DATA included, in Turn 1. Both repaired to the named four in Turn 2 with correct Tasks and Story blocks. |

Cause shared by the three failing pairs. The twins agree, so no divergence needs classifying. The shared cause is a conflict each packaging carries identically, so it is neither a parity gap nor a split between runtimes:

- Ask first on an explicit command: `AGENTS.md` line 287 and `Custom Instructions.md` line 108 (`$story` still asks and waits).
- Ask only when unclear: `sk-product-owner/references/story-mode.md` line 64 and Project `Product Owner - Templates - Story Mode - v0.402.md` line 41 (`Ask one consolidated question only when role, value, requirement shape or artifact kind cannot be established safely`). `sk-product-owner/references/interactive-mode.md` line 172 and Project `Product Owner - System - Interactive Mode - v0.405.md` line 149 (`if_kind_and_scope_inferable: processing`).
- Both runtimes followed the Story Mode and Interactive gate reading in all three pairs, each saying the attachments supplied enough to draft (`SST-002` turn-1.md line 7, `PST-002` turn-1.md line 187, `SST-004` turn-1.md line 1, `PST-004` turn-1.md line 600).
- For the bundle pair, `story-mode.md` line 406 and Project Story Mode line 382 add a second ambiguity: whether a split listed in an attached brief counts as one the request names.

## Open readings for the operator (batch summary)

1. Which rule governs Turn 1 on `$story` or `$s` with complete attachments: the ask-first command rule (`AGENTS.md` line 287, kernel line 108) or Story Mode's ask-only-when-unclear rule (`story-mode.md` line 64, `interactive-mode.md` line 172 and their Project mirrors)? Six FAILs rest on the Pass clause text, which follows the first.
2. Does a task split listed in an attached brief count as one "the request names" (`SKILL.md` line 252, `story-mode.md` line 406)?
3. Must the `**Open:**` line carry `Do sub-pages inherit the link?` word for word, or is the question in substance enough (`SST-002`, `PST-002`)?
4. Is "build against a single page until then" (`SST-002` export lines 38 and 172) settling the sub-page question, given fixture line 54?
5. Save card: is keeping the context card-data rule and marking the draft's stored brand `**Open:**` correct conflict handling, or an altered draft value (`SST-003` line 42, `PST-003` line 55)? This set `facts_intact` to `no` on both.
6. Do `312 stays` with only the number backticked, and `Guest checkout` capitalized at the start of a sentence, count as verbatim?
7. Should a partial Read (for example lines 100 to 144 of 144) count as the read-back? Full-file Reads happened only in `SST-001` Turn 1, `SST-002` Turn 2 and the `SST-004` Turn 2 Story. Every other skill read-back in this batch returned only a tail range.
8. Wrong `N`: `SST-002` Turn 1 printed 176 where Read returned 177.
9. Project wording such as "replaces the previous version under the same filename" and "one folder with seven files": are these file claims under root line 189?
