# Remeasure batch `remeasure-stories-epics`, grader draft

Run: `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/remeasure-operator-repairs/run-1/`. Model `claude-opus-5-5-medium`. Product Owner commit `39bcd29`, Barter commit `df2de5f0`, playbook 2.1.0.0. `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing, and the working-tree root is identical to `git show 39bcd29:sk-product-owner/manual-testing-playbook/manual-testing-playbook.md`, so every root, source and fixture line below is the line at `39bcd29`. `run-status.json` gives 2 of 2 turns for all nine scenarios.

Tally: skill 3 PASS, 1 FAIL. Project 0 PASS, 5 FAIL.

Reading notes that apply to every scenario below:

- **Read-back.** The skill runtime reads through the Read tool and through Bash (`cat -n`, `sed -n`). A Bash read of the exact export path that returns its lines, after the last write, is counted as the read-back. The Read tool counts the empty line after a trailing newline, so on every file read with that tool here its final line number is one above `wc -l`. `SST-002` read with Bash `cat -n`, which matches `wc -l`. Where a reply printed the `wc -l` figure instead, the `N` is recorded as off by one and not failed (brief section 2).
- **Project blocks.** Every Project block in this batch is fenced. The copies the format gate read are in `scratch/grades/blocks/remeasure-stories-epics/`, named `<ID>-turn<n>-block<k> - <label>.md`, body only, fences stripped.
- **Rulings applied.** Ruling 1 (an explicit command asks first), ruling 2 (an Epic omits References with no link) and ruling 3 (a promise to write or save a file is a Project file claim, root lines 179 and 189, kernel line 101).
- **Main-run verdicts** are from `<RUN>/results.csv`.

---

## SST-002, Story forced delivery (skill)

**Draft row**

```csv
SST-002,skill,claude-opus-5-5-medium,FAIL,2,2,pending,no,"The **Open:** line rewords the backticked question `Do sub-pages inherit the link?` (export/002 - Story-view-only-share-links.md line 53, ""whether a link on a page also opens its sub-pages"", against design notes line 46), so that Pass clause is unmet. Turn 1 now asks one Story question and saves only it (turn-1.md lines 3 to 5), and every other clause holds. Advisory: 175 lines against 90 to 170."
```

**Against the main run:** still failing, for a narrower cause. The main run's Turn 1 drafting cause is fixed. The reworded `**Open:**` question, which the main run also recorded, remains and now decides the verdict alone.

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one consolidated Story question | Met | `export/001 - Story-view-only-share-links-clarification.md` lines 1 to 17, one question in six fields. It asks Story or Epic, which the Story context question template carries in its Requirements field (`assets/interactive-response-templates.md` line 123) |
| Saves only that question in the Story lane | Met | File name carries `Story-` and `-clarification`. Ledger turn 1 creates only that file (`meta.json`) |
| Reads it back | Met | `events-turn-1.jsonl` L62, `sed -i` then `cat -n` of the exact path in the same command. L63 returns lines 1 to 17 |
| Replies with path, `Verified:` line and `HVR self-scan:` | Met | `turn-1.md` lines 3, 4 (`17 lines`) and 5 |
| No draft | Met | `turn-1.md` line 1 "I haven't drafted the PRD yet". No Story file in the turn 1 ledger |
| Turn 2 saves one Story on the next number | Met | `export/002 - Story-view-only-share-links.md`, ledger turn 2 |
| Reads it back | Met (partial range) | L57 `sed -i` then `cat -n ... \| sed -n 88,98p; wc -l; tail -1` on the exact path. L58 returns lines 88 to 98, `175` and the last line `* * *` |
| Names the Story kind | Met | `turn-2.md` line 1 "I've written the view-only share links PRD as a Story" |
| `HVR self-scan:` line | Met | `turn-2.md` line 5 |
| About, Problem, Solution, Expected outcomes, Requirements | Met | Export lines 7, 11, 15, 19, 26 |
| Numbered Given/When/Then criteria, each closed by Mark-as-done | Met | Criteria 1 to 8, Mark-as-done at lines 79, 88, 96, 107, 116, 128, 137, 146 |
| Closing `## Delivery` with Estimation, Rabbit holes, No-gos in order | Met | Lines 150, 152, 164, 170, with the allowed `#### External dependencies` at 158. `## Delivery` is the last section |
| Requirements carry the eleven values verbatim | Met | `Anyone with the link can view` line 30, `Never`, `7 days`, `30 days` line 33, `60 seconds` lines 35 and 36, `3 active links` line 47 (inside the copy `Your workspace has 3 active links. ...`), `Free` 43, `Plus` 44, `Team` 45, `Duplicate` 59, `noindex` 61 |
| `**Open:**` line carries `Do sub-pages inherit the link?` and names Lena | Unmet (string) / Met (Lena) | Line 53 `**Open:** whether a link on a page also opens its sub-pages, and so what `Duplicate` copies. Lena decides with the security reviewer ...`. The notes' question is `Do sub-pages inherit the link?` (`loomlist-view-only-links-design-notes.md` line 46) |
| Rabbit holes repeat that question | Met in substance | Line 168 "Sub-page inheritance is open and will not be settled before the build starts", with both views from notes lines 50 and 52 |
| No criterion asserts sub-page behavior | Met | Criteria at lines 72 to 146 never mention sub-pages. Criterion 7 copies "the page" only |

**Blocking items hit**

- Protected fact: the Pass clause lists `Do sub-pages inherit the link?` verbatim and the `**Open:**` line rewords it (root line 188, brief section 2).

**Advisory items**

- Size band: 175 lines against 90 to 170 (root line 209).
- Borderline, not decisive: Problem line 13 "In the design research sessions, readers who hit a sign-in wall stopped reading" generalizes Kofi's argument for sub-page inheritance, which is about readers "who followed a link inside a shared page" (notes line 50).
- Disclosed addition: criterion 3 on view-only members, named at `turn-2.md` line 14.
- The Turn 1 reply also prints the questions (root line 156, not graded).

**Read-back table**

| Turn | Export path | N printed | Read after last write, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - Story-view-only-share-links-clarification.md` | 17 | Bash `cat -n` at L62, lines 1 to 17 | 17 |
| 2 | `export/002 - Story-view-only-share-links.md` | 175 | Bash `cat -n \| sed -n 88,98p` plus `tail -1` at L57, lines 88 to 98 and the last line | 175 |

**Realism entries**

- `export/001 - Story-view-only-share-links-clarification.md`, Story-lane clarification, question only. Facts: plans and the Team Admin control (notes lines 22 to 30), Lena undecided with no date (notes line 54), Data team tracking plan review (`loomlist-context.md` line 191). No placeholder. 17 lines. Gate passed.
- `export/002 - Story-view-only-share-links.md`, Story. Required sections present (skill `assets/story-template.md` lines 40 to 103): preamble, About, Problem, Solution, Expected outcomes, Requirements, Acceptance criteria, plus Delivery forced by the `**Open:**` line (template line 124). References omitted with no link supplied (template line 66). Facts: H1 `Member - Sharing - View-only share links` follows `loomlist-context.md` line 112. Problem "Today a page can only be shared by inviting a member or a guest" matches context line 179 and notes line 8. Lena as the Sharing PM, context line 88. Plans Free, Plus and Team, context lines 35 to 37. No placeholder beyond the exempt `TBD...` slots. 175 lines against 90 to 170 (advisory). No discipline code expected. Gate passed.

**Open readings**

- Must the `**Open:**` line carry `Do sub-pages inherit the link?` word for word, when the skill's own marker template asks for "the part that is not decided" (`references/story-mode.md` line 332)? Graded Unmet, as in the main run, where the same question went to the operator unanswered. It now decides `SST-002` alone.
- Does a read-back that returns only lines 88 to 98 and the last line count as reading the file back? Graded Met.

---

## PST-002, Story forced delivery (Project)

**Draft row**

```csv
PST-002,project,claude-opus-5-5-medium,FAIL,2,2,pending,no,"The **Open:** line rewords `Do sub-pages inherit the link?` (turn-2.md line 56, ""Whether a link on a page also opens its sub-pages""), so that Pass clause is unmet. Turn 1 now asks one Story question as a fenced block with its label (turn-1.md lines 1 to 37). Borderline, not decisive: turn-1.md line 45 ""the Story will be `export/002 - Story-view-only-share-links.md`"" may be a file promise under ruling 3."
```

**Against the main run:** still failing, for a narrower cause. Turn 1 now asks and renders no draft, so the main run's Turn 1 cause is fixed. The reworded `**Open:**` question remains.

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one consolidated Story question | Met | `turn-1.md` lines 2 to 32, seven fields in one block |
| Renders it as its own block with a Story-lane `Export-equivalent path:` | Met | Fenced block lines 1 to 33, `Export-equivalent path: export/001 - Story-view-only-share-links-clarification.md` line 35 |
| `HVR self-scan:` line, no draft | Met | Line 37. Line 39 "I haven't written the Story yet" |
| Turn 2 renders one Story block with its `Export-equivalent path:` | Met | Fenced block lines 1 to 161, path line 163 |
| Names the Story kind | Met | Line 167 "I wrote this as a **Story**" |
| `HVR self-scan:` line | Met | Line 165 |
| Claims no file | Met in Turn 2 | No save, write or read-back claim in `turn-2.md`. Turn 1 line 45 is recorded under Open readings |
| About, Problem, Solution, Expected outcomes, Requirements | Met | Reply lines 8, 12, 16, 20, 27 |
| Numbered criteria, each closed by Mark-as-done | Met | Criteria 1 to 6, Mark-as-done at 82, 91, 101, 110, 122, 131 |
| Closing `## Delivery` with Estimation, Rabbit holes, No-gos in order | Met | Lines 135, 137, 149, 155, External dependencies at 143 |
| The eleven values verbatim | Met | `Anyone with the link can view` 31, `Never`, `7 days`, `30 days` 34, `60 seconds` 37 and 38, `Free` 46, `Plus` 47, `Team` 48, `3 active links` 50 (inside the copy), `Duplicate` 62, `noindex` 64 |
| `**Open:**` line carries `Do sub-pages inherit the link?` and names Lena | Unmet (string) / Met (Lena) | Line 56 `**Open:** Whether a link on a page also opens its sub-pages. ... Lena settles it with the security reviewer, and no date is set.` |
| Rabbit holes repeat that question | Met in substance | Line 153 "Whether a link on a page also opens its sub-pages ..." |
| No criterion asserts sub-page behavior | Met | Criteria lines 75 to 131 never mention sub-pages |

**Blocking items hit**

- Protected fact: `Do sub-pages inherit the link?` reworded (root line 188).

**Advisory items**

- Borderline file promise, not decisive: `turn-1.md` line 45 "Once you reply, the Story will be `export/002 - Story-view-only-share-links.md`."
- Commentary after the blocks only. Block form: fenced (four backticks) in both turns.
- Size band: block body 159 lines, inside 90 to 170.

**Realism entries**

- Block `PST-002-turn1-block1 - Story-view-only-share-links-clarification.md`, Story-lane clarification, question only. Facts: the three frame names (notes line 4), the Free limit of 3 (notes line 24), the review date 2026-09-15 (notes line 3). No placeholder. 31 lines. Gate passed.
- Block `PST-002-turn2-block1 - Story-view-only-share-links.md`, Story. Required sections present per the Project mirror (`Product Owner - Assets - Story Template - v0.100.md` lines 21 to 84), Delivery forced (lines 103 to 128), References omitted with no link (line 47). Facts: H1 `Member - Sharing - View-only links` follows `loomlist-context.md` line 112. Problem matches context line 179. Lena, context line 88. Plans, context lines 35 to 37. Agencies on Plus from Turn 2. No placeholder beyond exempt `TBD...`. 159 lines against 90 to 170. Gate passed.

**Open readings**

- The same `**Open:**` wording question as `SST-002` (knowledge Story Mode line 308 carries the same marker template).
- Is "the Story will be `export/002 - ...md`" a promise to write or save a file under ruling 3? It sits between `PIR-002` "will be a new file with the next number" (ruled a file claim) and `PBG-003` "will take the next number in the bug lane" (borderline, names no file). Not decisive here.

---

## SST-003, Story refinement (skill)

**Draft row**

```csv
SST-003,skill,claude-opus-5-5-medium,PASS,2,2,pending,no,"Turn 1 saves only the Story question as export/001 - Story-save-card-for-next-time-clarification.md and Turn 2 saves the refinement as export/fernhouse-save-card-draft.md with every listed value, the order-total rule and no checklist, context/ untouched. facts_intact is no for the same unruled reading as the main run: the draft's stored brand becomes an **Open:** line (export line 43) after the Turn 1 question on it went unanswered. Advisory: 147 lines against 70 to 130, gate connective finding on the clarification."
```

**Against the main run:** fixed. The main run failed on Turn 1 refining without the Story question. The brand reading behind `facts_intact` is unchanged.

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one consolidated Story question | Met | Clarification lines 1 to 18, five numbered fields |
| Saves only that question in the Story lane | Met | `export/001 - Story-save-card-for-next-time-clarification.md`. Ledger turn 1 creates only it |
| Reads it back | Met | `events-turn-1.jsonl` Read at L55, L56 returns lines 1 to 19 of 19 |
| Path, `Verified:`, `HVR self-scan:`, no draft | Met | `turn-1.md` lines 3, 4, 5. Line 1 "I haven't drafted the Story yet" |
| Turn 2 saves the refinement as `export/fernhouse-save-card-draft.md` | Met | Ledger turn 2, `turn-2.md` line 3 |
| Reads it back | Met (partial range) | Write L33, Read L35 at offset 150 returns nothing, Read L38 at offset 140 returns lines 140 to 148 of 148 |
| Names the Story kind, `HVR self-scan:` | Met | `turn-2.md` line 1 "as a Story", line 5 |
| `context/fernhouse-save-card-draft.md` unchanged | Met | Both turn ledgers list no modified file (`meta.json`). No Write, Edit, `sed -i`, redirect, `mv`, `cp`, `rm` or `tee` against `context/` in either event stream |
| H1 with no `PRD -` prefix | Met | Line 1 `# Customer - Checkout - Save card for next time` |
| No `**Checklist**`, no `- [ ]` build item in Requirements | Met | Requirements lines 26 to 63 hold none |
| Checklist content carried as bold-lead constraint groups | Met | Sixth card refused line 34, `**Stored card data**` 37 to 39, `Remove this card?` 55, `**Tracking**` 57 to 61. The brand is held open, see Open readings |
| `## Acceptance criteria`, numbered, each closed by Mark-as-done | Met | Line 65, criteria 1 to 6, Mark-as-done at 78, 87, 95, 103, 111, 122 |
| Every listed value verbatim | Met | `Save this card for next time` and `unchecked by default` 30, `You can save up to 5 cards` 33, `Card ending 7031` and `Expires 08/28` 45, `CVC`, `€150`, `£130` 46, `Account > Payment methods` 54, `Remove this card?` 55, `guest checkout` 32, `This card was declined. Choose another card or enter a new one.` 48 |
| Order-total rule for the CVC limits | Met | Line 46 "An order whose total including shipping is over `€150`, or over `£130` in the UK" |

**Blocking items hit**

None. No Fail example applies: the event names are left to the Data team (lines 59 to 61), no brand or stored field is invented, no `TBD...` remains for the declined copy.

**Advisory items**

- Size band: 147 lines against 70 to 130.
- Format gate on the clarification: "prose connectives 4.3 per 1000 across 231 prose words". No Pass clause covers it.
- Disclosed additions: criterion 4 "no order is placed" and criterion 6 removed card on every platform (`turn-2.md` lines 22 to 24). The Checkout product owner of the expired-card question is named as an addition at line 9.

**Read-back table**

| Turn | Export path | N printed | Read after last write, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - Story-save-card-for-next-time-clarification.md` | 19 | Read L55, lines 1 to 19 of 19 | 18 |
| 2 | `export/fernhouse-save-card-draft.md` | 148 | Read L38 at offset 140, lines 140 to 148 of 148 | 147 |

**Realism entries**

- `export/001 - Story-save-card-for-next-time-clarification.md`, Story-lane clarification, question only. Facts: the card-data rule (`fernhouse-context.md` line 153), the draft's stored fields (draft line 48), the tracking plan rule (context line 164). No placeholder. 18 lines. Gate: connective finding.
- `export/fernhouse-save-card-draft.md`, Story refinement. Required sections present: preamble, About, Problem, Solution, Expected outcomes, Requirements, Acceptance criteria, and Delivery forced by the two `**Open:**` lines. References omitted with no link. Figures 17%, 9% and 68% unaltered (line 13, draft line 15). Facts: H1 follows context line 95. Stored card data line 39 matches context line 153. Lotte owns the context (context line 3), line 43. Tracking plan and DATA task rule, context line 164, line 61. Web, iOS and Android from draft line 11. No placeholder beyond exempt `TBD...`. 147 lines against 70 to 130 (advisory). Gate passed.

**Open readings**

- The draft stores the brand (draft lines 39 and 48), and `fernhouse-context.md` line 153 allows only token, last four and expiry. The runtime asked in Turn 1 (clarification line 5), got no answer, kept the context rule and held the brand logo as `**Open:**` for Lotte, saying so in the reply (`turn-2.md` line 8). The main run left this reading to the operator unruled. Is `facts_intact` `no` right for a conflict between two attachments that is raised rather than silently resolved, and does root line 144 "prior facts remained intact" reach it? Graded PASS with `facts_intact` `no`, for consistency with the main-run row.
- Does a read-back of lines 140 to 148 count? Graded Met.

---

## PST-003, Story refinement (Project)

**Draft row**

```csv
PST-003,project,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 promises a save: turn-1.md line 30 ""I'll write the Story. It will save as `export/fernhouse-save-card-draft.md`"", and block line 4 ""I'll keep a copy under its original basename"", a file claim under root line 189 and kernel line 101. Turn 2 otherwise meets every clause under Export-equivalent path export/fernhouse-save-card-draft.md (turn-2.md line 147). Advisory: block body 143 lines against 70 to 130."
```

**Against the main run:** failing for a new cause. The main run failed on Turn 1 rendering the refinement without asking. Turn 1 now asks and renders no draft, but promises a save.

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one consolidated Story question | Met | Block lines 2 to 23, eight fields |
| Own block with Story-lane `Export-equivalent path:` and `HVR self-scan:` | Met | Fenced lines 1 to 24, path line 26, HVR line 28 |
| No draft | Met | Line 30 "I haven't drafted anything yet" |
| Turn 2 renders one refined Story block with `Export-equivalent path: export/fernhouse-save-card-draft.md` | Met | Fenced lines 1 to 145, path line 147 |
| Names the Story kind, `HVR self-scan:` | Met | Line 151 "into the house Story format", line 149 |
| Claims no file | Unmet | Turn 1 line 30 "It will save as `export/fernhouse-save-card-draft.md`", block line 4 "I'll keep a copy under its original basename". Turn 2 makes no such claim |
| H1 with no `PRD -` prefix | Met | Line 2 |
| No `**Checklist**`, no build item | Met | Requirements lines 27 to 58 |
| Checklist content as bold-lead constraint groups | Met | Sixth card 37, stored fields 38, `Remove this card?` 52, `**Analytics**` 54 to 56 |
| Acceptance criteria numbered, each closed by Mark-as-done | Met | Criteria 1 to 6, Mark-as-done at 73, 82, 93, 102, 111, 121 |
| Every listed value verbatim | Met | `Save this card for next time` 34, "unchecked by default" 34, `You can save up to 5 cards` 36, `Card ending 7031` and `Expires 08/28` 44, `CVC`, `€150`, `£130` 45, `Account > Payment methods` 51, `Remove this card?` 52, declined copy 47, guest checkout 35 ("Guest checkout has no saving", sentence case) |
| Order-total rule | Met | Line 45 "Orders whose total including shipping is over `€150`, or over `£130` in the UK" |

**Blocking items hit**

- Project file claim: a promise to save a file (root line 189, ruling 3, kernel line 101 "never promise to write or save one").

**Advisory items**

- Size band: block body 143 lines against 70 to 130.
- Turn 2 finished on `end_turn` at 8192 output tokens, 5272 of them thinking (`events-turn-2.jsonl` last line), so the reply is complete, not cut off.
- Disclosed additions at `turn-2.md` lines 165 to 168: the Analytics group, criterion 5 "no order exists until a payment is authorised" (context line 141), criterion 2's reason line.
- Block form: fenced, both turns.

**Realism entries**

- Block `PST-003-turn1-block1 - Story-save-card-for-next-time-clarification.md`, Story-lane clarification. Facts: card-data rule (context line 153), glossary subtotal question, `object_action` naming (context line 161). No placeholder. 22 lines. Gate passed.
- Block `PST-003-turn2-block1 - fernhouse-save-card-draft.md`, Story refinement. Required sections present per the Project mirror, Delivery forced by the brand `**Open:**` line (line 31). Figures 17%, 9% and 68% unaltered (line 14). Facts: H1 follows context line 95, stored fields line 38 match context line 153, Lotte line 31 matches context line 3, tracking plan line 56 matches context line 164. No placeholder beyond exempt `TBD...`. 143 lines against 70 to 130 (advisory). Gate passed.

**Open readings**

- The brand handling is the same as `SST-003`, here as `**Open:**` at line 31 with the logo kept pending at line 44. `facts_intact` set `no` for the same reason.

---

## SST-004, Story with nested tasks (skill)

**Draft row**

```csv
SST-004,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 saves only a Story-lane question that asks for the task split (export/001 - Story-order-tracking-clarification.md lines 5 to 12), and Turn 2 saves folder 002 with the Story and exactly 002.1 to 002.4 for FE iOS, FE Android, FE web and the BE webhook, the Tasks block and each **Story** block linked both ways, every file read back and every value verbatim. Advisory: Story 180 lines against 80 to 150, tasks 121 to 122 against 35 to 90, and Turn 2 N printed as wc -l, one under each Read's final line."
```

**Against the main run:** fixed. The main run asked nothing and saved a seven-file bundle with six tasks on Turn 1.

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one consolidated Story question in the Story lane | Met | Clarification lines 1 to 26. Field 1 asks for the split (lines 5 to 12), since the request names none (`references/story-mode.md` line 406, `SKILL.md` line 252) |
| Saves only that question as `export/[###] - Story-[description]-clarification.md` at the top of `export/` | Met | `export/001 - Story-order-tracking-clarification.md`, ledger turn 1 |
| Reads it back | Met | Read L61, L62 returns lines 1 to 27 of 27 |
| Path, `Verified:`, `HVR self-scan:`, no draft, no folder | Met | `turn-1.md` lines 3, 4, 5. Ledger turn 1 holds no folder |
| Turn 2 saves one folder on the next number | Met | `export/002 - Story-order-tracking/`, ledger turn 2 |
| Story plus exactly four tasks `002.1` to `002.4` for FE iOS, FE Android, FE web and BE webhook in that order | Met | `002.1 - task-fe-ios-...`, `002.2 - task-fe-android-...`, `002.3 - task-fe-web-...`, `002.4 - task-be-tracking-webhook.md` |
| Reads every file back | Met | Reads L121, L123, L125, L127, L129 after the last Write at L111, each returning the whole file |
| Every path, Story first, each with its own `Verified:`, then one `HVR self-scan:` | Met | `turn-2.md` lines 5 to 18, HVR line 20 |
| Names the Story kind | Met | Line 3 "**Artifact kind:** Story, with its tasks in one folder" |
| Clarification untouched outside the folder | Met | Ledger turn 2 modifies nothing |
| Story: About, Problem, Solution, Expected outcomes | Met | Story lines 7, 13, 19, 23 |
| `#### **Tasks**` inside About, one bullet per task in order, linking `(<[###].[n] - task-...md>)` | Met | Lines 28 to 33, before the About spacer at 34 |
| Requirements and numbered criteria, each closed by Mark-as-done | Met | Requirements 36, criteria 1 to 8 with Mark-as-done at 117, 126, 135, 143, 151, 159, 170, 178 |
| Each task: `### About`, `**Story**` linking `(<002 - Story-order-tracking.md>)`, no `**Parent task**`, `### Requirements` | Met | 002.1 lines 3, 21 to 25, 35. 002.2 and 002.3 differ from 002.1 only in platform lines (diff). 002.4 lines 3, 13 to 17, 27. No `**Parent task**` in any |
| Bundle values verbatim | Met | Six statuses Story line 40, `PU` `IT` 43, `OD` 44, `DL` 45, `EX` 46, `Arriving Thursday 1 October` and `Between 10:00 and 14:00` 54, `90 days` 65, `30 kg` and `120 cm` 70, `tracking.updated` and `/webhooks/carrier/tracking` 84, `X-Carrier-Signature` 86, `5 attempts` and `1 min, 5 min, 15 min, 1 h, 6 h` 88, `event_id` 89, `occurred_at` 94, `eta_window` 54 to 57. The BE task repeats them at lines 43 to 48, 62, 98 to 101 |

**Blocking items hit**

None. No Packed or DATA task, no `## Scope`, no `**Parent task**`, no epic, `Delivery failed` shows no reason (Story line 46), no estimate without a window (line 55), no polling or history call (line 90 states `GET /v1/shipments/{shipment_id}` returns label fields only, carrier notes line 48).

**Advisory items**

- Size band: Story 180 lines against 80 to 150. Tasks 121, 121, 122 and 122 lines against 35 to 90.
- Wrong `N` on Turn 2: every printed figure equals `wc -l` and sits one under the Read's final line (see the table).
- Disclosed additions: estimate lines translated for all six locales, and an unsigned event not stored (`turn-2.md` lines 27 and 28).
- Borderline, not decisive: "Carrier codes are mapped to statuses in the tracking webhook task, never in the clients" (Story line 49) and "maps no carrier codes itself" (FE tasks line 11) infer a boundary from the brief's BE task line (brief line 56).

**Read-back table**

| Turn | Export path | N printed | Read after last write, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - Story-order-tracking-clarification.md` | 27 | Read L61, 1 to 27 of 27 | 26 |
| 2 | `export/002 - Story-order-tracking/002 - Story-order-tracking.md` | 180 | Read L121, 1 to 181 of 181 | 180 |
| 2 | `.../002.1 - task-fe-ios-order-tracking-timeline.md` | 121 | Read L123, 1 to 122 of 122 | 121 |
| 2 | `.../002.2 - task-fe-android-order-tracking-timeline.md` | 121 | Read L125, 1 to 122 of 122 | 121 |
| 2 | `.../002.3 - task-fe-web-order-tracking-timeline.md` | 122 | Read L127, 1 to 123 of 123 | 122 |
| 2 | `.../002.4 - task-be-tracking-webhook.md` | 122 | Read L129, 1 to 123 of 123 | 122 |

The Bash call at L103, which tried to build 002.2 and 002.3 from 002.1, failed on a here-document and wrote nothing. Both files were then written by Write at L107 and L109.

**Realism entries**

- `export/001 - Story-order-tracking-clarification.md`, Story-lane clarification, question only. Facts: the brief's six expected tasks (brief lines 56 to 61), `parcel_point` after a second `NOT_HOME` (carrier line 31), the DATA-before-FE rule (context line 164). No placeholder. 26 lines. Gate passed.
- `002 - Story-order-tracking.md`, Story. Required sections present: preamble, About, Problem, Solution, Expected outcomes, Tasks, Requirements, Acceptance criteria. No Delivery, none forced. Facts: H1 `Customer - Order page - Order tracking` follows context line 95. WISMO 5,870 of 18,940 and 31% match brief line 7. Six locales match context lines 128 to 132. Volume matches carrier line 52. No placeholder. 180 lines against 80 to 150 (advisory). Gate passed.
- `002.1 - task-fe-ios-order-tracking-timeline.md`, task. Required sections present (`assets/task-templates.md` lines 42 to 151): About, References as a backticked frame name, Story, Related tasks, Requirements. Facts: `TRACK` code (context line 105), title pattern (context line 93), pallet limits (context line 150). 121 lines against 35 to 90 (advisory). Title code `FE - iOS - TRACK`. Gate passed.
- `002.2 - task-fe-android-order-tracking-timeline.md`, task. Same sections and facts as 002.1. 121 lines (advisory). Title code `FE - Android - TRACK`. Gate passed.
- `002.3 - task-fe-web-order-tracking-timeline.md`, task. Same sections. Adds the one responsive build (context line 13) and the web layout in the same frame from Turn 2. 122 lines (advisory). Title code `FE - Web - TRACK`. Gate passed.
- `002.4 - task-be-tracking-webhook.md`, task. Sections About, Story, Related tasks, Requirements. Facts: shipping-service receives the webhook (carrier line 7), signature and retries (carrier lines 43 to 46), `occurred_at` ordering (carrier line 35). 122 lines (advisory). Title code `BE - TRACK`, surface dropped per context line 93. Gate passed.

**Open readings**

- Does the Read tool's extra final line decide `N`? `AGENTS.md` line 46 names the Read's final line number, and the reply printed `wc -l` on Turn 2. Recorded, not failed.

---

## PST-004, Story with nested tasks (Project)

**Draft row**

```csv
PST-004,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 promises files: turn-1.md line 25 ""The Story and task files will go under the next number, in `export/002 - Story-order-tracking/`"", a file claim under root line 189 and kernel line 101. Its question also pre-empts the split instead of asking for it, block line 2 ""I'll write the Story and its six tasks, split the way Hamid's brief lists them"" (knowledge Story Mode line 382). Turn 2 renders the correct five blocks in the named order."
```

**Against the main run:** failing for a new cause. The main run rendered seven blocks with a Packed and a DATA task on Turn 1. Turn 1 now renders only a question, but it promises files and does not ask for the split.

On the two points the orchestrator raised: "I'll write the Story and its six tasks" (block line 2) is drafting language about artifacts, not by itself a file promise, but it announces the brief's six-task split as settled rather than asking for one. The file promise is line 25, which calls them files and places them in an `export/` folder. Turn 2 follows the four named tasks exactly.

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one consolidated Story question in the Story lane | Unmet | Block lines 2 to 18 ask eight questions, none about the split. Line 2 settles it as "the Story and its six tasks, split the way Hamid's brief lists them (BE webhook, BE `Packed`, FE Web, FE iOS, FE Android, DATA)". Expected signals and knowledge Story Mode line 382 have the question ask for the split when the request names none. Lines 27 to 30 list title, codes and order as assumptions "unless you correct them", not the split |
| Own block, `Export-equivalent path:` outside any folder, `HVR self-scan:` | Met | Fenced lines 1 to 19, path `export/001 - Story-order-tracking-clarification.md` line 21, HVR line 23 |
| No draft | Met | No Story or task block in Turn 1 |
| Turn 2: one block per file, Story first, then exactly four task blocks in the named order | Met | Story lines 1 to 148, iOS 152 to 219, Android 223 to 290, Web 294 to 361, BE 365 to 448 |
| Each followed by its own `Export-equivalent path:` inside `export/[NNN] - Story-[description]/` | Met | Lines 150, 221, 292, 363, 450 |
| One `HVR self-scan:` line for the set | Met | Line 452 |
| Names the Story kind | Met | Line 454 "This is a **Story** with four tasks in the order you gave" |
| Claims no file | Unmet | Turn 1 line 25. Turn 2 line 476 "I'll update the files ... the files are ready to save or paste" is recorded as borderline |
| Story sections, `#### **Tasks**` inside About in order with sibling links | Met | About 8, Problem 14, Solution 18, Expected outcomes 22, Tasks 27 to 32 linking `(<002.1 - task-ios-tracking-timeline.md>)` to `(<002.4 - task-tracking-webhook.md>)` |
| Requirements and numbered criteria, each closed by Mark-as-done | Met | Requirements 36, criteria 1 to 7 with Mark-as-done at 94, 103, 112, 121, 129, 137, 145 |
| Each task: `### About`, `**Story**` link, no `**Parent task**`, `### Requirements` | Met | iOS block lines 4, 12 to 16, 26 (reply 155, 163 to 167, 177). Android and Web differ only in platform lines (diff). BE reply lines 368, 376 to 380, 390 |
| Set values verbatim | Met | Statuses 40, codes 43 to 46, estimate strings 55, `90 days` 75, `30 kg` and `120 cm` 74, `tracking.updated` and `/webhooks/carrier/tracking` 61, `X-Carrier-Signature` 62, `5 attempts` and `1 min, 5 min, 15 min, 1 h, 6 h` 64, `event_id` 65, `occurred_at` 56 and 66, `eta_window` 54 to 57 |

**Blocking items hit**

- Project file claim: a promise that files will be placed in an `export/` folder (root line 189, ruling 3, kernel line 101).

**Advisory items**

- Borderline, not decisive: `turn-2.md` line 476 "I'll update the files. ... the files are ready to save or paste."
- Format gate on the Turn 1 block: "importance assertion" at block line 15 ("This matters for the UK").
- Size band: Story block 146 lines inside 80 to 150, task blocks 66, 66, 66 and 82 inside 35 to 90.
- Disclosed additions at `turn-2.md` lines 460 to 463.
- Block form: fenced, all six blocks.

**Realism entries**

- Block `PST-004-turn1-block1 - Story-order-tracking-clarification.md`, Story-lane clarification. Facts: Maud's split (brief line 69), `delivered_to: parcel_point` (carrier line 31), `eta_window` offsets (carrier line 17). No placeholder. 17 lines. Gate: importance assertion.
- Block `PST-004-turn2-block1 - Story-order-tracking.md`, Story. Required sections present per the Project mirror, Tasks block present. Facts: H1 follows context line 95, WISMO figures brief line 7, locales context lines 128 to 132, peak `43,000` carrier line 52. No placeholder. 146 lines. Gate passed.
- Blocks `PST-004-turn2-block2` to `block4` (iOS, Android, Web tasks). Sections per `Product Owner - Assets - Task Templates - v0.102.md`: About, Story, Related tasks, Requirements. No category heading under Requirements, which the gate did not flag and no Pass clause asks for. Facts: `TRACK` context line 105, pallet limits context line 150, slot line brief line 42. 66 lines each. Title codes `FE - iOS - TRACK`, `FE - Android - TRACK`, `FE - Web - TRACK`. Gate passed.
- Block `PST-004-turn2-block5 - task-tracking-webhook.md`, task. Facts: carrier lines 7, 43 to 46, 48, 52. 82 lines. Title `BE - TRACK`. Gate passed.

**Open readings**

- Is the brief's list of six expected tasks "a split the request names"? The scenario and knowledge line 382 read "the request" as the user's prompt, which names none. Graded Unmet.
- Is `turn-2.md` line 476 a promise to write files? Not decisive.

---

## SEP-001, Epic from strategy brief (skill)

**Draft row**

```csv
SEP-001,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 saves only the Epic question as export/001 - Epic-partner-hub-self-onboarding-clarification.md, and Turn 2 saves export/002 - Epic-partner-hub-self-onboarding.md with the six stage names as plain-text child stories, the channel manager under Added Later, the five brief values verbatim, no Requirements and no References, since no link was supplied. Advisory: none decisive, 142 lines inside 90 to 150."
```

**Against the main run:** fixed. The main run drafted and saved the Epic on Turn 1.

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one Epic question in the Epic lane and drafts nothing | Met | `export/001 - Epic-partner-hub-self-onboarding-clarification.md` lines 1 to 21, `turn-1.md` lines 1 to 5 |
| Turn 2 saves one Epic | Met | `export/002 - Epic-partner-hub-self-onboarding.md`, ledger turn 2, `turn-2.md` lines 3 to 5 |
| `# Epic - ` H1, no story preamble | Met | Line 1. Line 3 is the divider and line 4 `## About` |
| About with Problem, Goal, Solution | Met | Lines 9, 20, 32 |
| References only when a link is supplied | Met | Omitted, no link supplied. `turn-2.md` line 19 says so |
| Scope names exactly six child stories, plain text, one per stage name verbatim | Met | Lines 49 to 57: `Sign-up and verification`, `Property profile and photos`, `Rooms and rates setup`, `Policies and city tax`, `Payout details and identity checks`, `Go-live review queue` |
| `#### Added Later` holds the channel manager connection | Met | Lines 59 to 64 |
| Release-level criteria in numbered `1\.` blocks, each closed by Mark-as-done | Met | Criteria 1 to 5, Mark-as-done at 80, 89, 98, 106, 115 |
| No `## Requirements`, ticket header fields, story points or INVEST notes | Met | None present |
| Names the kind | Met | `turn-2.md` line 1 "(artifact kind: Epic)" |
| `11 business days`, `38%`, `3 business days`, `1,500`, `2027-06-30` verbatim | Met | Lines 14, 15, 22, 24, 24 |
| Invents no link | Met | No URL in the file |

**Blocking items hit**

None. Chains, properties over 40 rooms and channel manager properties stay out of the first release (Solution line 41, criterion 4, No-gos line 141). Estimation is `TBD...` plus the brief's squad ownership (brief lines 52, 56 to 58). The runtime read `assets/epic-template.md` (turn 1 L33) and the Epic example (turn 2 L14), never the Story scaffold.

**Advisory items**

- Disclosed additions: criterion 4, two Rabbit holes, per-stage tracking and the squad sizing split (`turn-2.md` lines 9 to 15).

**Read-back table**

| Turn | Export path | N printed | Read after last write, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - Epic-partner-hub-self-onboarding-clarification.md` | 22 | Read L60 after Edit L58, 1 to 22 of 22 | 21 |
| 2 | `export/002 - Epic-partner-hub-self-onboarding.md` | 143 | Read L68 after Edit L63, 1 to 143 of 143 | 142 |

**Realism entries**

- `export/001 - Epic-partner-hub-self-onboarding-clarification.md`, Epic-lane clarification, question only. Facts: up to 40 rooms and no channel manager (brief lines 36 to 38), per-country business register (brief line 27), queue capacity sized by Ops Tools (brief line 52). No placeholder. 21 lines. Gate passed.
- `export/002 - Epic-partner-hub-self-onboarding.md`, Epic. Required sections present (`assets/epic-template.md` lines 40 to 112): About, Problem, Goal, Solution, Scope with Added Later, Acceptance criteria, plus the optional Delivery close. Facts: H1 follows `roamstay-context.md` line 85. Problem figures 813 of 2,140, 4.5 hours and 640 match brief lines 10 to 13. Bram as Ops Lead, brief line 59. `partner-service` owned by Partner, brief line 56. No placeholder beyond exempt `TBD...`. 142 lines inside 90 to 150. Gate passed.

**Open readings**

None.

---

## PEP-001, Epic from strategy brief (Project)

**Draft row**

```csv
PEP-001,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"File claim under ruling 3: turn-1.md line 39 ""Once you reply, I'll write the epic as `export/002 - Epic-partner-hub-self-onboarding.md`"", the kernel line 101 example almost word for word. Every other clause holds, with References omitted as no link was supplied. Advisory: block body 151 lines against 90 to 150, gate bullet full stops in the Turn 1 block."
```

**Against the main run:** still failing for the same cause, a Turn 1 promise to write the Epic as a numbered file (main run `turn-1.md` line 37).

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one Epic question in the Epic lane and drafts nothing | Met | Fenced block lines 1 to 31, `Export-equivalent path: export/001 - Epic-partner-hub-self-onboarding-clarification.md` line 33, HVR line 35, line 37 "I haven't drafted the epic yet" |
| Turn 2 renders one Epic, `# Epic - ` H1, no preamble | Met | Fenced block lines 1 to 153, H1 line 2, `## About` line 5 |
| About with Problem, Goal, Solution | Met | Lines 10, 21, 38 |
| References only when a link is supplied | Met | Omitted, line 159 says no links were supplied |
| Scope names exactly six child stories verbatim as plain text | Met | Lines 53, 57, 58, 59, 63, 67, each opening with the stage name after the `Partner Hub - Self-onboarding - ` or `Back office - Self-onboarding - ` path |
| `#### Added Later` holds the channel manager connection | Met | Lines 69 to 74 |
| Numbered criteria, each closed by Mark-as-done | Met | Criteria 1 to 5, Mark-as-done at 90, 99, 108, 117, 126 |
| No `## Requirements`, header fields, points or INVEST | Met | None |
| Consults only the Epic scaffold where reads show | Met | Turn 1 reads `Product Owner - Assets - Epic Template` (L21), turn 2 the Epic example (L13). No Story Template read |
| Names the kind, `HVR self-scan:` | Met | Line 159 "I wrote this as an **Epic**", line 157 |
| Five values verbatim | Met | `11 business days` 15, `38%` 16, `3 business days`, `1,500`, `2027-06-30` 23 |
| Invents no link | Met | No URL |
| Claims no file | Unmet | `turn-1.md` line 39 "Once you reply, I'll write the epic as `export/002 - Epic-partner-hub-self-onboarding.md`." |

**Blocking items hit**

- Project file claim: a promise to write a file (root line 189, ruling 3, kernel line 101).

**Advisory items**

- Format gate on the Turn 1 block: bullet items ending with a full stop at block lines 9 and 25.
- Size band: Epic block body 151 lines against 90 to 150.
- Disclosed additions at `turn-2.md` lines 163 to 167, including the Owner payout Rabbit hole, which comes from `roamstay-context.md` line 28.
- Block form: fenced, both turns.

**Realism entries**

- Block `PEP-001-turn1-block1 - Epic-partner-hub-self-onboarding-clarification.md`, Epic-lane clarification. Facts: payouts wait for identity checks (brief line 31), stage 6 in Back office by Ops Tools (brief line 57), Owner-only payout changes (context line 28). No placeholder. 29 lines. Gate: two bullet full stops.
- Block `PEP-001-turn2-block1 - Epic-partner-hub-self-onboarding.md`, Epic. Required sections present per `Product Owner - Assets - Epic Template - v0.101.md`, plus the optional Delivery. Facts: H1 follows context line 85, squads Partner, Ops Tools and Payments (brief lines 56 to 58), stage values `8 photos` and `20 MB` (brief line 28), `1 business day` (brief line 32). No placeholder beyond exempt `TBD...`. 151 lines against 90 to 150 (advisory). Gate passed.

**Open readings**

None beyond ruling 3, which decides the row.

---

## PEP-002, Epic natural wording (Project)

**Draft row**

```csv
PEP-002,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"File claim under ruling 3: turn-1.md line 31 ""When you reply, I'll write the epic as `export/002 - Epic-offline-mode.md`"". Every other clause holds: Epic lane from wording alone, four areas verbatim, Web out, the 2026-10-09 dependency open, References omitted with no link supplied."
```

**Against the main run:** still failing for the same cause, a Turn 1 promise to write the Epic as the next file (main run `turn-1.md` line 31).

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 resolves the Epic kind from wording alone, one Epic question in the Epic lane, no draft | Met | Fenced block lines 1 to 23, `Export-equivalent path: export/001 - Epic-offline-mode-clarification.md` line 25, HVR line 27, line 29 "I haven't drafted the epic yet" |
| Turn 2 renders one Epic, `# Epic - ` H1, no preamble | Met | Block lines 1 to 103, H1 `# Epic - Member - Offline mode` line 2 |
| About with Problem, Goal, Solution | Met | Lines 5, 9, 19, 33 |
| References only when a link is supplied | Met | Omitted, line 115 |
| Scope names exactly the four areas verbatim, plain text, each across iOS, Android and Desktop | Met | Lines 51, 52, 58, 59. Line 45 "for iOS, Android and Desktop", About line 7 "Each story covers iOS, Android and Desktop together" |
| Numbered criteria, each closed by Mark-as-done | Met | Criteria 1 to 4, Mark-as-done at 74, 83, 91, 100 |
| No `## Requirements`, header fields, points or INVEST | Met | None |
| Consults only the Epic scaffold where reads show | Met | Turn 1 reads the Epic Template (L17), turn 2 the Epic example (L8). No Story Template read |
| Names the kind | Met | Line 109 "I wrote this as an **Epic**" |
| `23%` and `31%` verbatim | Met | Line 11 |
| Web out of every child story and criterion | Met | Line 41 "This epic does not cover Web". No story or criterion names Web |
| Conflict handling named as a dependency on the `2026-10-09` decision | Met | Line 56 "Joana ... decides on 2026-10-09 ... Neither story below can be finalised before that decision", Solution line 38 |
| Claims no file | Unmet | `turn-1.md` line 31 "When you reply, I'll write the epic as `export/002 - Epic-offline-mode.md`." |

**Blocking items hit**

- Project file claim: a promise to write a file (root line 189, ruling 3, kernel line 101).

**Advisory items**

- Borderline, not decisive: line 56 renders today's behavior as "keeps the version that reaches it last, per block, on protocol v3", where the brief and context say `block-level last-writer-wins` (brief line 26, `loomlist-context.md` line 70). Same meaning, not the source's wording.
- Disclosed addition: criterion 2's "no change made offline is lost" line (`turn-2.md` line 118).
- Size band: block body 101 lines inside 80 to 140.
- Block form: fenced, both turns.

**Realism entries**

- Block `PEP-002-turn1-block1 - Epic-offline-mode-clarification.md`, Epic-lane clarification. Facts: Desktop wraps the web client (context lines 12 and 18), protocol change needs every client (context line 177), Joana's date (brief line 32). No placeholder. 21 lines. Gate passed.
- Block `PEP-002-turn2-block1 - Epic-offline-mode.md`, Epic. Required sections present per the Project Epic Template mirror. Facts: H1 follows context line 112, `500` pages and `1 GB` (brief line 22), Joana as Sync Engineering Manager (context line 87, brief line 32), Q1 2027 (brief line 36), out-of-scope list (brief lines 45 to 48). No placeholder. 101 lines. Gate passed.

**Open readings**

- Is "keeps the version that reaches it last, per block" an altered brief value, when the Expected signals allow today's behavior only as `block-level last-writer-wins`? Not decisive here.

---

## Twin notes

| Pair | Skill | Project | Agree or differ | Cause and rule lines |
|---|---|---|---|---|
| `ST-002` | FAIL | FAIL | Agree | Both reword `Do sub-pages inherit the link?`. It looks like a rule gap between the scenario and both packagings. The Pass clause backticks the question, while the marker template in both packagings asks only for "the part that is not decided" (`references/story-mode.md` line 332, knowledge `Product Owner - Templates - Story Mode - v0.403.md` line 308). Both Turn 1s are now correct. The Project also carries the borderline "the Story will be `export/002 - ...`" line (`turn-1.md` line 45) |
| `ST-003` | PASS | FAIL | Differ | Runtime fault on the Project side. The skill may promise its save (`turn-1.md` line 14 "I'll save the Story in `export/` under Priya's filename"), and the kernel forbids the same promise on the Project side (`Custom Instructions.md` line 101, root lines 179 and 189). The Project turn carried the skill's phrasing over. Both handle the brand conflict the same way |
| `ST-004` | PASS | FAIL | Differ | Runtime fault on the Project side, on two rules both packagings state alike. The split question is at `references/story-mode.md` line 406 and `SKILL.md` line 252 on the skill side, and knowledge Story Mode line 382 on the Project side. The skill asked it (clarification lines 5 to 12), and the Project announced the brief's six instead. The file promise breaks kernel line 101. Turn 2 is correct on both sides |
| `EP-001` | PASS | FAIL | Differ | Runtime fault on the Project side. Kernel line 101 forbids "I'll write the task as `export/002 - ...`", and `PEP-001` wrote "I'll write the epic as `export/002 - ...`". The Project knowledge frames the next artifact as "a new Deliverable Block taking the next number" (`Product Owner - System - Interactive Mode - v0.406.md` line 75), so no Project text invites the promise |
| `EP-002` | (not in this round, main run PASS) | FAIL | Differ against the main-run twin | Same runtime fault as `PEP-001`, kernel line 101 |

The Project file promise appears in four of the five Project scenarios here (`PST-003`, `PST-004`, `PEP-001`, `PEP-002`, plus the borderline `PST-002`), always in the closing line after the Turn 1 clarification block. Kernel line 101 is the only Project text that forbids it. Neither the Story Mode nor the Interactive Mode knowledge file restates it beside the clarification label rules, where the runtime writes that line.
