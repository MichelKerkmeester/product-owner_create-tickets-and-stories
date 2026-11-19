# Remeasure grades: batch `remeasure-bugs-docs-identity`

Batch: SBG-002, PBG-002, SDK-001, PDK-001, SDK-003, PDK-003, PID-001, PIR-002. Model `claude-opus-5-5-medium`. Run folder `<RUN>/remeasure-operator-repairs/run-1/`, where `<RUN>` is `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`. Product Owner commit `39bcd29`, Barter commit `df2de5f0`, playbook 2.1.0.0. `git status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing, so every source was read from the working tree and every root and source line below is cited as it stands at `39bcd29` (root copy written with `git show 39bcd29:sk-product-owner/manual-testing-playbook/manual-testing-playbook.md`).

## Handover verdict first

- **PID-001 (Project handover): FAIL.** `claude project/PID-001 - identity-handover/turn-1.md` line 48 says "Once you answer, the task will be `export/002 - task-due-today-filter-chip.md`." The block itself says "I'll write the task from your answers" (line 4). Naming the future task as a concrete `export/` Markdown file is a promise of a file, which root lines 179 and 189 and `Custom Instructions.md` line 101 make a file claim. Every other PID-001 clause is met. The alternative reading is under PID-001 Open readings, and PID-001 flips to PASS only if the operator rejects this one.

Identity split greps at `39bcd29`, run from the workspace root:

| Grep | Expected | Observed |
|---|---|---|
| `grep -c "read-back succeeded" AGENTS.md` | `2`, exit `0` | `2`, exit `0` (lines 47 and 91) |
| `grep -c "read-back succeeded" "claude project/Custom Instructions.md"` | `0`, exit `1` | `0`, exit `1` |
| `grep -c "Canvas Artifact" AGENTS.md` | `0`, exit `1` | `0`, exit `1` |
| `grep -c "Canvas Artifact" "claude project/Custom Instructions.md"` | `4`, exit `0` | `4`, exit `0` (lines 76, 181, 221, 235) |

## Tally

| Runtime | PASS | FAIL | SKIP |
|---|---:|---:|---:|
| skill | 2 (SBG-002, SDK-003) | 1 (SDK-001) | 0 |
| project | 2 (PDK-003, PIR-002) | 3 (PBG-002, PDK-001, PID-001) | 0 |

## Method notes

- Format gate: `node validate-output-format.cjs --system product-owner <file>` from the Sync Loop folder on all five skill exports, on the ten Project block copies and on a reconstruction of the SDK-001 Turn 1 export. Everything passed with exit 0 except `skill/SDK-003 .../002 - doc-sync-conflict-options.md` lines 114 and 115 and block `PDK-003-turn2-block.md` lines 151 and 152, each `prose em dash (HVR bans it, use a comma, colon or full stop)`, all on Source basis bullets. No Pass clause in this batch names the em dash, so these are advisory evidence.
- Block copies sit in `scratch/grades/blocks/remeasure-bugs-docs-identity/` as `<ID>-turn<n>-block.md`: the text between the opening and closing fence, so block line `k` is reply line `k + 1`. Every Project block was fenced (```` ```markdown ```` or ```` ````markdown ```` at reply line 1), with nothing before it. Each copy is byte-identical to the collector's copy under `AI Systems/Product Owner/export/benchmark/claude project/remeasure-operator-repairs/run-1/`, and each skill export in the run folder is byte-identical to its copy under `export/benchmark/skill/remeasure-operator-repairs/run-1/`.
- SDK-001 Turn 2 edited `export/001 - doc-discount-stacking.md` in place, so the run folder only holds the Turn 2 state. The Turn 1 state is rebuilt from the file content returned by the Read at `events-turn-1.jsonl` line 105 and saved as `blocks/remeasure-bugs-docs-identity/SDK-001-turn1-export-reconstructed-from-read.md` (160 lines). Cited below as "T1 export".
- Every Project run's `meta.json` shows an empty ledger on both turns, and the Project sessions had only `Glob`, `Grep` and `Read`.
- In every Project realism entry and Pass table, line numbers are reply lines (`turn-<n>.md`) unless marked as block lines.
- Quotes that hold the definition or status-label delimiter are cut before it, so this draft carries no em dash. The block copies keep the runtime's own text byte for byte, delimiters included, because the gate and the collector comparison need them unchanged.

---

## SBG-002 (skill), Support ticket bug

**Draft row**

```csv
SBG-002,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 asked one question and saved the question-only export/001 - bug-android-confirmation-total-city-tax-clarification.md, read back (turn-1.md lines 3 to 5), and Turn 2 saved export/002 - bug-android-confirmation-total-city-tax.md with ticket 58213, RS-7Q4K2M, Android 8.12.1, Pay now, Total €387.00 against €405.00 and €18.00 city tax (export lines 22, 43, 44), the charge kept correct (line 7) and Device Not provided (line 14). The error-message line is left out of Observed Behavior (lines 41 to 50), as ruling 6 allows; advisory: the heading at turn-2.md line 11 carries an em dash."
```

**Against the main run:** fixed. The main run failed because Turn 1 asked nothing and saved the whole bug. This round Turn 1 asks and saves only the clarification.

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Met | Clarification lines 5 to 13: Scope, Environment, Evidence, Severity and title, Validation, in one message |
| Saves it question-only under the `bug` word | Met | `001 - bug-android-confirmation-total-city-tax-clarification.md`: an H1, one framing line (3) and five question paragraphs, no draft |
| With its path, `Verified:` and `HVR self-scan:` lines | Met | `turn-1.md` line 3 `Path:`, line 4 `Verified: read-back succeeded; 14 lines`, line 5 `HVR self-scan:` |
| Drafts nothing | Met | `meta.json` turn 1 ledger: only the clarification created. `turn-1.md` line 1 "I haven't written the bug report yet" |
| Turn 2 saves one bug under the `bug` word on the next number, read back | Met | `002 - bug-android-confirmation-total-city-tax.md`, turn 2 ledger creates only this file; read-back table |
| Every required template section | Met | Title (1), `### About` (3), field table (9 to 17), References (19 to 29), `### Bug` (33), `**1. Observed Behavior**` (37), `Steps to Reproduce:` (52), screen recording (61), `**2. Expected Behavior**` (65), Checklist (76 to 80), optional BDD (84) |
| Ticket `58213`, `RS-7Q4K2M`, Android `8.12.1`, `Pay now` | Met | Lines 22, 43, 13, 7 |
| "Total €387.00" against `€405.00` and the `€18.00` city tax | Met | Line 43 "showed Total €387.00 and the card was charged €405.00", line 44 "room €387.00 (3 nights at €129.00) plus city tax €18.00" |
| Severity `High` | Met | Line 12 |
| No device model | Met | Line 14 `Not provided`; line 15 OS names only "Android 14 on the Guest Support test phone" |
| Every other amount exact and adding up | Met | 2 nights €270.00 and €258.00 (45), 1 night €135.00 = €129.00 + €6.00 (46), iOS €405.00 (47); all against ticket lines 46 to 48 and 55 to 58 |
| Charge correct, Android confirmation total the defect | Met | Line 7 "The card is charged the correct amount with city tax"; line 41 |
| Scope held to Android `8.12.1` Pay now stays of 2 nights or more | Met | Title line 1, lines 7 and 41 |
| No claim that 1 night, iOS `8.12.0` or web is wrong | Met | Lines 46, 47 and 73 state all three correct |
| Fail: Pay at property stated either way | Not hit | Line 49 "have not been tested and no guest has reported one" |
| Fail: Frequency from the 14 chats | Not hit | Line 11 `Always` rests on "per Guest Support escalation", as the scenario allows; the 14 chats stay in Observed Behavior (48) |
| Fail: invented device, root cause or step | Not hit | No cause stated; checklist keeps "Root cause identified" open (77). Steps 1 to 6 follow the agent's 2-night test (ticket 53 and 55); step 7 "Cancel the test booking inside free cancellation" is ticket line 58 and is named at `turn-2.md` line 17 |
| Fail: unfilled template slot | Not hit | None |

Error-message line (ruling 6): left out. Observed Behavior (lines 41 to 50) has no error-message bullet, and the word "error" appears nowhere in the bug, so nothing asserts that no error message appears.

**Blocking items hit:** None.

**Advisory items**

- `turn-2.md` line 11, the chat heading "Choices I made that you didn't give me", carries an em dash. Commentary outside the export
- Asking for a fact an attachment states (root line 211), recorded only: clarification line 11 asks whether Severity should follow Maren's High, which the ticket's Priority field states (ticket line 10)
- Borderline, never decides alone: line 47 "checked on 2026-09-26" turns the Turn 2 "this morning" into a date taken from the session clock
- Size: 91 lines, inside 60 to 110. Discipline code: `FE`

**Read-back table**

| Turn | Export path | `N` printed | Read after the last write, lines returned | Real `wc -l` |
|---|---|---:|---|---:|
| 1 | `export/001 - bug-android-confirmation-total-city-tax-clarification.md` | 14 | Write at `events-turn-1.jsonl` line 39 (only write), Read at line 41, result line 42: lines 1 to 14, totalLines 14 | 13 |
| 2 | `export/002 - bug-android-confirmation-total-city-tax.md` | 92 | Write at `events-turn-2.jsonl` line 17, Bash `perl -0pi` at line 25 (last write), Read at line 27, result line 29: lines 1 to 92, totalLines 92 | 91 |

`N` equals the final line number the Read returned (`AGENTS.md` line 46); `wc -l` is one lower because of the trailing newline.

**Realism entries**

- `export/001 - bug-android-confirmation-total-city-tax-clarification.md`, bug-lane clarification. Required content is the question alone: present. Facts: Android 8.12.1 reproduction and iOS 8.12.0 comparison (line 3 vs ticket lines 53 and 58); Pay at property untested (line 5 vs ticket 61); ticket priority High (line 11 vs ticket 10); title pattern `{Discipline} - Guest app - BOOK - {Title}` (line 11 vs `roamstay-context.md` lines 83 and 93). Placeholder: `{Discipline}` and `{Title}` sit inside a quoted title pattern inside a question, the pattern from `roamstay-context.md` line 83, not toy content. 13 lines, no band. Format gate: passed.
- `export/002 - bug-android-confirmation-total-city-tax.md`, bug. Routed template `assets/bug-report-template.md` lines 63 to 140 and `references/bug-mode.md` lines 127 to 135: all required sections present (Pass table). Facts: booking RS-7Q4K2M, property 40217, €3.00 per adult per night (43 vs ticket 12 and 15); room 3 x €129.00 = €387.00 plus €18.00 = €405.00 (44 vs ticket 46 to 48); staged Android rollout reaching everyone on 2026-09-21 (48 vs ticket 66 and `roamstay-context.md` 112); City tax line in the price breakdown and part of the total (72 vs `roamstay-context.md` 44); title `FE - Guest app - BOOK - ...` (1 vs `roamstay-context.md` 83 and 93). Placeholder: none (`Not provided` is exempt). 91 lines against 60 to 110. Discipline code `FE`. Format gate: passed.

**Open readings**

- Does turning "this morning" into "2026-09-26" from the session clock (export line 47) count as a supplied value restated, or as a value the user never gave? Recorded as borderline, same question on PBG-002 and PIR-002.

---

## PBG-002 (project), Support ticket bug

**Draft row**

```csv
PBG-002,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"File claim under root line 189 and kernel line 101: turn-1.md line 25 says ""Once you answer, I'll write the report under the next number in the bug lane (`export/002 - bug-...`)"". Every other clause holds: a fenced question-only block under export/001 - bug-android-confirmation-total-city-tax-clarification.md (turn-1.md lines 2 to 16 and 19), then a fenced bug with every amount, the correct charge, Severity High, no device model, the error-message line left out and the Android 8.12.1 Pay now scope (turn-2.md lines 8 to 66)."
```

**Against the main run:** failing for a new cause. The main run failed because Turn 1 rendered the whole bug with no clarification. This round Turn 1 asks correctly, and the reply then promises the file.

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Met | `turn-1.md` lines 4 to 16, seven numbered points in one message |
| Renders it as its own question-only block | Met | Fenced, reply lines 1 to 17, block lines 2 to 16: one framing line (2) and the seven points. Form: fenced, nothing before it |
| `Export-equivalent path:` under the `bug` word with `-clarification` | Met | Line 19 `export/001 - bug-android-confirmation-total-city-tax-clarification.md` |
| `HVR self-scan:` line | Met | Line 21 |
| Drafts nothing | Met | Line 23 "I haven't drafted the bug report yet" |
| Turn 2 renders one bug as its own block | Met | `turn-2.md` lines 1 to 85, fenced, nothing before it |
| `Export-equivalent path:` under the `bug` word, `HVR self-scan:` | Met | Line 87 `export/002 - bug-android-confirmation-total-city-tax.md`, line 89 |
| Claims no file on either turn | **Unmet** | `turn-1.md` line 25 "Once you answer, I'll write the report under the next number in the bug lane (`export/002 - bug-...`)". Turn 2 has no file wording |
| Every required template section | Met | Title (2), `### About` (4), table (10 to 18), References (20 to 23), `### Bug` (27), Observed (31), Steps (44), Screen recording (52), Expected (58), Checklist (68 to 72), optional BDD (76). Flows and Components are left out because none were supplied (Project Bug Mode knowledge line 136 "Add flow and component references when provided") |
| Ticket `58213`, `RS-7Q4K2M`, Android `8.12.1`, `Pay now` | Met | Lines 23, 36, 8 and 14, 8 |
| "Total €387.00" against `€405.00` and the `€18.00` city tax | Met | Line 36 "showed Total €387.00. The card was charged €405.00, which is €387.00 for the room plus €18.00 city tax (€3.00 per adult per night)" |
| Severity `High` | Met | Line 13 |
| No device model | Met | Line 15 "Guest's phone: Not provided. Guest Support test phone: model Not provided" |
| Every other amount exact and adding up | Met | 2 nights €270.00 and €258.00 (38), 1 night €135.00 = €129.00 + €6.00 (39), iOS €405.00 (40), BDD €270.00 (82, 84) |
| Charge correct, Android confirmation total the defect | Met | Line 8 "The charge itself is correct. Only the confirmation screen shows less" |
| Scope held to Android `8.12.1` Pay now 2 nights or more | Met | Lines 2, 8, 35 |
| No claim that 1 night, iOS or web is wrong | Met | Lines 39, 40, 65 |
| Fail: Pay at property stated either way | Not hit | Line 54 lists it under "Not tested" |
| Fail: Frequency from the 14 chats | Not hit | Line 12 `Always` on "per Guest Support", with the scope in the cell |
| Fail: invented device, cause or step | Not hit | No cause; line 95 labels the `FE` title choice "only an inference because nobody has read the code yet". Steps follow the agent's 2-night test |
| Fail: unfilled slot | Not hit | None |

Error-message line (ruling 6): left out. Observed Behavior (lines 35 to 42) has no error-message bullet and no sentence asserting that none appears.

**Blocking items hit**

- File claim on the Project side: root line 189 ("any file claim at all on the Project side, where a promise to write or save a file counts as one"), `Custom Instructions.md` line 101. `turn-1.md` line 25 pairs "I'll write the report" with the path `export/002 - bug-...`, the shape of the ruling's own example

**Advisory items**

- Asking for a fact an attachment states (root line 211): line 8 asks whether Maren's High is the severity (ticket line 10)
- Borderline, never decides alone: step 1 (`turn-2.md` line 45) puts the test phone on "app language en-GB", which the ticket gives for the guest's app (ticket line 16), not for Maren's test phone
- Borderline: line 40 "checked on 2026-09-26" from the Turn 2 "this morning", as on SBG-002
- Named additions (line 99 and 100): the "Not tested" line and the BDD scenario. `Android 8.11.2` in the Not tested line is the previous train (`roamstay-context.md` line 110)
- Size: 83 block lines, inside 60 to 110. Discipline code `FE`

**Realism entries**

- Block `PBG-002-turn1-block.md` (reply lines 2 to 16), bug-lane clarification. Question alone: present. Facts: Maren's 1-night and 2-night tests and the iOS comparison (line 2 vs ticket 55 to 58); 14 related chats (2 vs ticket 61); Android 8.11.2 (14 vs `roamstay-context.md` 110); `booking-service` (16 vs `roamstay-context.md` 57). Placeholder: none. 15 lines, no band. Format gate: passed.
- Block `PBG-002-turn2-block.md` (reply lines 2 to 84), bug. Routed template Project `Product Owner - Assets - Bug Report Template - v0.101.md` and Bug Mode knowledge lines 110 to 118: every required section present. Facts: RS-7Q4K2M, property 40217, €3.00 per adult per night (36 vs ticket 12 and 15); Back office €405.00 and the email Total €405.00 (37 vs ticket 42 and 50); Android reaching all users on 2026-09-21 (42 vs ticket 66); per-stay city tax (54 vs `roamstay-context.md` 44); title `FE - Guest app - BOOK - ...` (2 vs `roamstay-context.md` 83 and 93). Placeholder: none. 83 lines against 60 to 110. Discipline code `FE`. Format gate: passed.

**Open readings**

- None beyond the shared date-conversion question under SBG-002. The file claim is the ruling's own example shape.

---

## SDK-001 (skill), Behavior reference

**Draft row**

```csv
SDK-001,skill,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Both turns name the mandatory primary body ## Stacking rules instead of ## Behavior rules (T1 export line 34, returned by the Read at events-turn-1.jsonl line 105; final export line 35), a missed Pass clause (root line 150) and a renamed mandatory section (doc-templates.md lines 115 and 116). Everything else holds: Turn 1 drafted at once with no question into export/001 - doc-discount-stacking.md, and Turn 2 revised it in place with the protected values, the retired label since 2026-05-01 (line 141) and no merchandiser Admin setup; advisory: the rule line writes half-up (line 86), with half up verbatim only in the example (line 124)."
```

**Against the main run:** still failing for the same cause. The main run named `## Stacking rules` at export line 59 as one of its causes, and it recurs on both turns. The main run's other two causes are gone: the rewritten scenario now expects a direct Turn 1 draft, which it got, and `one discount code per order` now appears verbatim (line 53).

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 routes to Doc Mode with no question and no clarification | Met | `turn-1.md` line 1 "I've written the stacking doc as a behavior reference"; turn 1 ledger creates only `export/001 - doc-discount-stacking.md` |
| Saves and reads back a Behavior reference in the doc lane on the first number | Met | `001 - doc-...`; read-back table |
| An Overview | Met | T1 export line 10, final line 11 |
| A `## Behavior rules` body | **Unmet** | T1 export line 34 and final export line 35 read `## Stacking rules`. No `## Behavior rules` heading on either turn |
| `* * *` directly under every content heading | Met | Every heading and bold rule label is followed by `* * *` on the next line (final lines 11/12 through 159/160); format gate passed |
| `*   ` bullets, no hyphen bullets, no `---` dividers | Met | Turn 1 self-check Grep (events line 106) found no `^- ` or `^---`; the only `---` are table separator rows |
| Sentence-case headings | Met | For example line 139 `### Retired: two codes on one order` |
| No empty spacer heading | Met | None on either turn |
| `one discount code per order` | Met | T1 line 52, final line 53 "A customer can use one discount code per order" |
| `automatic promotions first` | Met | Line 43 `**2. Automatic promotions first, then the code**` (capital at the start of the label) |
| `exclusive`, `STAFF-`, `compare_at`, `applies_to_sale` | Met | Lines 22, 25, 24, 23 |
| The `50%` cap | Met | Lines 80 and 82 |
| `0.01` `half up` rounding | Met (hyphen note) | Line 86 "rounded to 0.01 with half-up rounding"; `half up` verbatim at line 124 "rounds half up to €3.74" |
| Turn 2 asks no question and delivers the revised doc in the doc lane | Met | `turn-2.md` line 1 "I've made your changes"; turn 2 ledger modifies `001` in place (not graded) |
| Same layout checks on Turn 2 | Met | As above |
| Every value still verbatim on Turn 2 | Met (hyphen note) | As above |
| Two-codes rule in and labelled retired since `2026-05-01` | Met | Line 139 heading, line 141 "Status: Retired material" then the delimiter and "retained for orders placed before 2026-05-01", line 143 CS still explains and refunds |
| No account of merchandiser Admin setup | Met | Glossary line 20 dropped "set up by a merchandiser in Admin" (present at T1 line 19); line 147 mentions Admin only as where old orders show two codes |
| Nothing the two attachments do not state | Met (borderline noted) | Named addition at line 100 (an exclusive code can leave less discount), named in `turn-1.md` line 24 and `turn-2.md` line 24 |
| Fail: two-codes rule presented as current | Not hit | Lines 139 to 147 |
| Fail: supplied value altered | Not hit | Values above; worked-example amounts match rules lines 21 to 42 |

**Blocking items hit**

- Missed Pass clause, root line 150: `## Behavior rules` absent on both turns
- Ticket realism, a required section of the routed template missing (root line 205): the Overview and the shape's primary body are "the only mandatory sections" (`assets/doc-templates.md` line 115), the scaffold names it `## Behavior rules` (line 400), and only optional headings may be renamed (line 116). The rule content is present under `## Stacking rules`

**Advisory items**

- Doc summary names "Layout" rather than "ClickUp layout" (`turn-1.md` line 10, `turn-2.md` line 10). Expected signal only
- Borderline, never decides alone: line 26 glossary "One product in the cart with its quantity" (no attachment defines a line); line 45 illustrates rule 2 with "A 15% code on a line already at 20% off", the percentages of the note's own worked example
- Turn 2 also removed two context-sourced statements the user did not ask to remove ("never compute a discount themselves", the banner open question), reported at `turn-2.md` lines 18 to 20
- Size: T1 160 lines, final 162 lines, inside 80 to 180

**Read-back table**

| Turn | Export path | `N` printed | Read after the last write, lines returned | Real `wc -l` |
|---|---|---:|---|---:|
| 1 | `export/001 - doc-discount-stacking.md` | 161 | Write at `events-turn-1.jsonl` line 76, Edits at lines 93 to 101 (last write 101), Read at line 104, result line 105: lines 1 to 161, totalLines 161 | 160 (reconstructed from that Read; the file was later edited) |
| 2 | `export/001 - doc-discount-stacking.md` (in place) | 163 | Edits at `events-turn-2.jsonl` lines 16 to 30, Read at 33 (1 to 162), Edit at 39 (last write), Read at 41 offset 150, result line 42: lines 150 to 163, totalLines 163 | 162 |

**Realism entries**

- T1 export (`SDK-001-turn1-export-reconstructed-from-read.md`), Doc, Behavior reference. Routed template `assets/doc-templates.md` lines 355 to 450: Overview present (10), primary body renamed `## Stacking rules` (34). Optional: Glossary (17), Where the rules run (29), Combinations and precedence (92), Worked examples (108), retired rule (138), Boundaries and open questions (147), Related references (157). Facts: cart copy `Only one code per order. Your new code has replaced the old one.` (52 vs rules line 7); `STAFF-`, exclusive, 30% off, sale items (66 vs rules 10); free shipping at €50 or £45, shipping €4.95 or £3.95 (89 vs rules 13); banner `Free shipping on orders over €50` (154 vs `fernhouse-context.md` line 20); merchandisers alone change promotions (19 vs context 33). Placeholder: none. 160 lines against 80 to 180. Format gate: passed.
- Final export `export/001 - doc-discount-stacking.md`, Doc, Behavior reference, same template: Overview (11), primary body renamed (35), optional sections as above. Facts: 2026-05-01 retirement and 2026-05-04 code path removal (145 vs rules 50 and 52); worked-example subtotal €137.33 (122 vs rules 28); cap example €15.00 (128 vs rules 34); UK example £47.15 (132 vs rules 38); gift card example €57.00 (136 vs rules 42). Placeholder: none. 162 lines against 80 to 180. Format gate: passed.

**Open readings**

- Is "half-up" in the rule line (86), with "half up" kept verbatim in the worked example (124), verbatim for `half up`? Graded Met with a note, as the main run did. It does not decide this verdict.
- `N` 161 and 163 follow the Read's final line; `wc -l` gives 160 and 162.

---

## PDK-001 (project), Behavior reference

**Draft row**

```csv
PDK-001,project,claude-opus-5-5-medium,FAIL,2,2,pending,no,"The protected value one discount code per order never appears on either turn: the rule reads **3. One code per order** (turn-1.md and turn-2.md line 55) beside the cart copy, a missed verbatim Pass clause (root lines 150 and 188). Everything else holds: no question on Turn 1, a fenced Behavior reference with ## Behavior rules (line 32) under export/001 - doc-promotions-stacking.md, and a Turn 2 revision for CS agents and Checkout engineers with the retired label since 2026-05-01 (line 164), no merchandiser Admin setup and no file claim."
```

**Against the main run:** failing for a new cause. The main run failed on the missing Turn 1 clarification, which the rewritten scenario no longer expects, and it kept `one discount code per order` then. This round drops that phrase on both turns.

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 routes to Doc Mode, no question, no clarification block | Met | `turn-1.md` lines 1 to 180 hold the full reference; no `-clarification` label |
| Renders a Behavior reference with a doc-lane export-equivalent label | Met | Fenced (```` ````markdown ````), reply lines 1 to 180, nothing before it; line 182 `Export-equivalent path: export/001 - doc-promotions-stacking.md` |
| An Overview and a `## Behavior rules` body | Met | Line 11, line 32, both turns |
| `* * *` directly under every content heading | Met | Every heading and rule label, lines 2/4 through 171/172; format gate passed both blocks |
| `*   ` bullets, sentence-case headings | Met | No hyphen bullet or `---` divider inside the block |
| `one discount code per order` verbatim | **Unmet** | Absent from both replies (`grep -n -i "one discount code"` finds nothing). Line 55 `**3. One code per order**`, line 58 the cart copy "Only one code per order. ...", Turn 2 line 23 "An order carries one at most" |
| `automatic promotions first` | Met | Line 41 `**1. Automatic promotions first, then the code**` |
| `exclusive`, `STAFF-`, `compare_at`, `applies_to_sale` | Met | Lines 24, 27, 25, 26 |
| `50%` cap, `0.01` `half up` rounding | Met | Line 86 `50%`; line 94 "rounded to `0.01` with `half up` rounding" |
| Turn 2 asks no question, renders the revised reference with a doc-lane label | Met | `turn-2.md` lines 1 to 179 fenced; line 181 same label (not graded) |
| Every value still verbatim on Turn 2 | **Unmet** | Same miss as Turn 1 |
| Two-codes rule in and labelled retired since `2026-05-01` | Met | Line 162 heading, line 164 "Status: Retired material" then the delimiter and "retired on 2026-05-01", line 128 combinations row "Retired material", line 166 "It is here so CS can explain and refund orders" |
| No merchandiser Admin setup | Met | Line 22 no longer says "set up by a merchandiser in Admin"; line 17 dropped "Only merchandisers can create or change a promotion in Admin"; line 168 mentions Admin only for old orders |
| Nothing the two attachments do not state | Met | Open questions named as additions at `turn-2.md` line 202 |
| No file claim on either turn | Met | No `Path:`, `Saved:`, `Verified:`, no promise. `turn-1.md` line 189 "because this is a file export" uses Doc Mode's own layout term (Project Doc Mode line 73) and claims no save |

**Blocking items hit**

- Missed Pass clause, root line 150: `one discount code per order` verbatim, on both turns
- Protected fact altered, root line 188: the supplied rule phrase generalized to "One code per order"

**Advisory items**

- Block form: fenced both turns, no commentary before either block. Five-line Doc summary present both turns (`turn-1.md` lines 187 to 191, `turn-2.md` lines 186 to 190)
- Turn 1 line 34 "in all five markets" comes from `fernhouse-context.md` line 5; Turn 2 line 34 changed it to "the euro markets and the UK", the note's wording
- Size: 178 and 177 block lines, inside 80 to 180

**Realism entries**

- Block `PDK-001-turn1-block.md` (reply lines 2 to 179), Doc, Behavior reference. Routed template Project `Product Owner - Assets - Doc Templates - v0.107.md` lines 334 to 429: Overview (11) and `## Behavior rules` (32) present. Optional: Terms (20), Combinations and precedence (114), Worked examples (131), retired rule (162), Open questions (171). Facts: cart copy (58 vs rules 7); staff code 30% and sale items (73 vs rules 10); €50 and £45 thresholds with €4.95 and £3.95 (105, 106 vs rules 13); banner copy `Free shipping on orders over €50` (179 vs `fernhouse-context.md` 20); five markets (34 vs context 5). Placeholder: none. 178 lines against 80 to 180. Format gate: passed.
- Block `PDK-001-turn2-block.md` (reply lines 2 to 178), same template and sections. Facts: 2026-05-01 and 2026-05-04 (164 vs rules 50 and 52); subtotal €137.33 (142 vs rules 28); cap example €15.00 (149 vs rules 34); UK total £47.15 (154 vs rules 38); gift card €57.00 (159 vs rules 42). Placeholder: none. 177 lines against 80 to 180. Format gate: passed.

**Open readings**

- Does a rule heading "One code per order" plus the quoted cart copy "Only one code per order." satisfy the verbatim `one discount code per order`? Graded no, as the main run graded SDK-001's "one discount code at a time". If the operator accepts it, PDK-001 passes.

---

## SDK-003 (skill), Proposal with a decision owner

**Draft row**

```csv
SDK-003,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 saved the question-only export/001 - doc-sync-conflicts-lost-edits-clarification.md asking audience, shape, status, source set and scope (lines 5 to 19) with the no-conflict authority reading stated at line 3, read back, and Turn 2 saved export/002 - doc-sync-conflict-options.md with the Proposal notice under the title (lines 3 to 6), Options A to C as the thread gives them, support for B attributed (lines 81 to 83) and Joana, 2026-10-09, not decided (lines 4 to 5). Advisory: no five-line Doc summary in turn-2.md, and the format gate flags the em dash in the two Source basis bullets (lines 114 and 115), which follow the template's own Source basis line."
```

**Against the main run:** still passing (main run PASS). The main run's borderline "Approved direction" label on Joana's plan does not appear this round.

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one consolidated question covering source set, authority, status, shape and scope | Met (authority stated, see Open readings) | Clarification line 5 Purpose and audience, 7 Shape, 9 Status and recommendation, 11 Source set and recency, 13 to 19 Scope, 21 Technical depth. Authority: line 3 "I'll write a new document from `context/loomlist-sync-conflict-thread.md`, with `context/loomlist-context.md` as the company background. The two files agree ..., so I have no source conflict to settle" |
| Exports it in the doc lane | Met | `001 - doc-sync-conflicts-lost-edits-clarification.md`; turn 1 ledger creates only this file |
| Reads it back with no draft | Met | Read-back table; `turn-1.md` line 1 "I haven't written the document yet" |
| Proposal status notice directly below the title | Met | Lines 3 to 6: line 4 "**Status: Proposal" then the delimiter and "not decided**", line 5 "None of them is approved or built" |
| Overview and an options body | Met | Line 8, line 30 `## Options` |
| `* * *` directly under every content heading | Met | Lines 8/9 through 112/113 |
| `*   ` bullets, sentence-case headings, no empty spacer heading | Met | No hyphen bullet, no spacer |
| v3 `block-level last-writer-wins` as the current state | Met | Line 14 `### Current state`, 16 "Status: Current behavior", 18 "Protocol v3 is block-level last-writer-wins" |
| `Option A` as `field-level` last-writer-wins | Met | Line 34 |
| `Option B` as a `three-way merge` with `Conflicting edit from {device name}` verbatim | Met | Lines 44 and 48 |
| `Option C` as a `CRDT` | Met | Line 58 |
| Support for B attributed | Met | Lines 81 to 83: Selin, Marta's +1, Tomasz "only with Saskia's formatting fallback", Saskia chose no option |
| `Joana`, `2026-10-09`, `not decided` | Met | Lines 4 and 5, 101 |
| No option called chosen, agreed, approved or decided | Met | Lines 5, 36, 46, 60, 81 "Joana has said so without deciding" |
| Nothing the two attachments do not state | Met | Additions named at `turn-2.md` lines 12 to 14: release timing (28, 93, from `loomlist-context.md` 137), "Not stated in the thread" (74, 75), the note on Marta's figure (56) |
| Fail: figure or estimate changed | Not hit | 40 and 22 (12), 0.8% (24), 58% and 42% (25), about 3 weeks (40), roughly 6 to 8 weeks (50), two quarters (64), 33 of 40 (56) |
| Fail: `{device name}` filled | Not hit | Line 48 keeps the braces; "such as Work laptop" is thread line 32 |
| Fail: `---` dividers or hyphen bullets | Not hit | None |

**Blocking items hit:** None.

**Advisory items**

- `turn-2.md` gives no five-line Doc summary (Source safety, Shape fit, ClickUp layout, Readability, Voice). The Expected signals ask for it (`doc-mode.md` line 412); the Pass clause does not
- Format gate: export lines 114 and 115 `prose em dash`, on the two Source basis bullets. The Proposal scaffold writes its Source basis line with the same delimiter (`assets/doc-templates.md` line 570)
- Offline plans kept out (109), as Turn 2 asked
- Size: 115 lines, inside 70 to 160

**Read-back table**

| Turn | Export path | `N` printed | Read after the last write, lines returned | Real `wc -l` |
|---|---|---:|---|---:|
| 1 | `export/001 - doc-sync-conflicts-lost-edits-clarification.md` | 21 | Write at `events-turn-1.jsonl` line 42, Read at 44 (1 to 22), Bash `sed -i` at 50 (last write), Read at 53 offset 5 limit 17, result line 54: lines 5 to 21, totalLines 22 | 21 |
| 2 | `export/002 - doc-sync-conflict-options.md` | 115 | Write at `events-turn-2.jsonl` line 26, Read at 28, Edits 47 to 57, Read at 63 (8 to 115), Edits 69 and 71 (last write 71), Read at 73 offset 54, result line 74: lines 54 to 115, totalLines 116 | 115 |

**Realism entries**

- `export/001 - doc-sync-conflicts-lost-edits-clarification.md`, Doc clarification. Question alone: present. Facts: decision on 2026-10-09 (5 vs thread 60); thread export ends 2026-09-22 (11 vs thread 3); lean toward B by Tomasz, Selin and Marta (9 vs thread 32, 36, 44); Marta's 33 of 40 (16 vs thread 36); protocol v4 for Option C (21 vs thread 28). Placeholder: none. 21 lines, no band. Format gate: passed.
- `export/002 - doc-sync-conflict-options.md`, Doc, Proposal. Routed template `assets/doc-templates.md` section 6 (scaffold ending line 571): notice under the title (3 to 6), Overview (8) and options body (30) present. Optional: Current state (14), Options and trade-offs (68), Where the thread landed (77), What happens before the decision (87), Dependencies and risks (91), Open decisions (99), Out of scope (107), Source basis (112). Facts: 0.8% and the phone over-representation (24, 26 vs thread 18); 58% and 42% (25 vs thread 48); field list text, checked state, due date, assignee, reminder (38 vs thread 24); frame `Sync / Conflict copy` (48 vs thread 32); iOS and Android every two weeks over 7 days (28 vs `loomlist-context.md` 137). Placeholder: `{device name}` quoted from the thread, exempt under root line 207. 115 lines against 70 to 160. Format gate: 2 findings (above).

**Open readings**

- Does a clarification that states its authority reading ("from the thread, with the context doc as background", "no source conflict to settle", line 3) cover the authority field, or does `AGENTS.md` line 285 need authority asked as its own question? Graded covered on both twins. If the operator requires an explicit question, SDK-003 and PDK-003 both fail.
- Should the missing five-line Doc summary count against a scenario whose Expected signals name it but whose Pass clause does not? Graded advisory, as the main run graded SDK-003's four-line summary.
- Should the format gate's em dash on a Source basis bullet count against a Proposal that follows its own template's Source basis line (skill `doc-templates.md` line 570, Project Doc Templates line 549)?

---

## PDK-003 (project), Proposal with a decision owner

**Draft row**

```csv
PDK-003,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 under $d rendered a fenced question-only block covering audience, status per claim, the sources not supplied, scope and shape (turn-1.md lines 2 to 25) under export/001 - doc-sync-conflicts-status-clarification.md, and Turn 2 a fenced Proposal with the notice under the title (lines 4 to 7), Options A to C, positions attributed (lines 97 to 102), Joana and 2026-10-09 not decided, and no file claim. Borderline only: the spike and the A write-up are stated as in progress (lines 55, 69, 87, 88); advisory: the format gate flags the em dash in the Source basis bullets (lines 152 and 153)."
```

**Against the main run:** fixed. The main run failed because Turn 1 under `$d` drafted a status write-up. This round Turn 1 asks and waits.

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one consolidated question covering source set, authority, status, shape and scope | Met (authority stated, see SDK-003 Open readings) | Line 4 Purpose and audience, 6 to 10 Status per claim, 12 Sources not supplied, 14 to 18 Scope, 20 to 23 Shape, 25 Delivery. Authority: line 2 "I've read both files. They agree with each other" |
| Rendered as its own block with a doc-lane clarification label | Met | Fenced, reply lines 1 to 26, nothing before it; line 28 `export/001 - doc-sync-conflicts-status-clarification.md` |
| No draft | Met | Line 32 "I haven't drafted anything yet" |
| Turn 2 Proposal status notice directly below the title | Met | Lines 4 to 7: line 5 "**Status: Proposal" then the delimiter and "not decided, Joana decides on 2026-10-09**", line 6 "None of them is current behavior or approved direction" |
| Overview and an options body | Met | Line 9, line 43 `## Options` |
| `* * *` directly under every content heading | Met | Lines 9/10 through 149/150 |
| `*   ` bullets, sentence-case headings | Met | No hyphen bullet or `---` divider inside the block |
| v3 `block-level last-writer-wins` as the current state | Met (wording note) | Line 15 `### Current state`, 18 "Status: Current behavior", 20 "Protocol v3 applies last-writer-wins at the block level" |
| `Option A` as `field-level` | Met | Line 46 |
| `Option B` as a `three-way merge` with `Conflicting edit from {device name}` verbatim | Met | Lines 58 and 64 |
| `Option C` as a `CRDT` | Met | Line 72 |
| Support for B attributed | Met | Lines 97 to 100 Selin, Marta, Tomasz, Saskia; 102 Joana "Not deciding in the thread" |
| `Joana`, `2026-10-09`, `not decided` | Met | Lines 5, 6, 108 |
| No option called chosen, agreed, approved or decided | Met | Line 108 "No decision has been made and this document makes no recommendation". Line 114 "Status: Approved direction" sits on Joana's interim plan, a Doc Mode class under ruling 7 |
| Nothing the two attachments do not state | Met (borderline noted) | Additions named at `turn-2.md` lines 174 to 178: to-do fields under B (128, 138), what Support says after the decision (139), edits already lost (40), the release cadence (39, from `loomlist-context.md` 18 and 137), Desired outcome (29 to 32) |
| Claims no file | Met | No `Path:`, `Saved:`, `Verified:`. `turn-1.md` line 32 "I'll write the document and number it `002` in the doc series" names a number, no file or path (Open readings). Block line 25 asks "or only into the export file?", a question about destination. `turn-2.md` line 164 "pass for a file export" is Doc Mode's layout term |
| Fail: figure or estimate changed | Not hit (borderline noted) | 22 and 40 (12), 0.8% (24), 58% and 42% (24), about 3 weeks (54), roughly 6 to 8 weeks (67), 33 of the 40 (66). Line 78 "about two quarters" where the thread says "two quarters" (thread 28) |
| Fail: `{device name}` filled | Not hit | Line 64 |

**Blocking items hit:** None.

**Advisory items**

- Borderline, never decides alone: line 55 "Tomasz is writing up what A would take", line 69 "A two-week spike is running", table lines 87 and 88 "in progress" and "spike running". The thread gives the spike and the write-up as Joana's plan of 2026-09-22 (thread 58). Turn 1 line 12 asked whether to say the spike is running and Turn 2 did not answer. The same open reading as the main run
- Borderline: "about two quarters" (78, 89) hedges an estimate the thread states as "two quarters"
- Format gate: block lines 151 and 152 (reply lines 152 and 153) `prose em dash`, on the Source basis bullets, which follow Project Doc Templates line 549
- Five-line Doc summary present (`turn-2.md` lines 161 to 166)
- Size: 153 block lines, inside 70 to 160

**Realism entries**

- Block `PDK-003-turn1-block.md` (reply lines 2 to 25), Doc clarification. Question alone: present. Facts: 40 and 22 tickets, 0.8%, 58% and 42% (7 vs thread 10, 18, 48); the doc `Sync conflicts, options for v3 and after` and frame `Sync / Conflict copy` (12 vs thread 22 and 32); Joana on 2026-10-09 (2 vs thread 60); Oskar's offline point (15 vs thread 52). Placeholder: none. 24 lines, no band. Format gate: passed.
- Block `PDK-003-turn2-block.md` (reply lines 2 to 154), Doc, Proposal. Routed template Project Doc Templates section 6 (scaffold ending line 550): notice (4 to 7), Overview (9) and options body (43) present. Optional: Current state (15), Desired outcome (29), Principles and constraints (35), Options and trade-offs (82), positions (92), Recommendation or decision (105), Interim plan (111), Dependencies and risks (123), Open decisions (131), Out of scope (142), Source basis (149). Facts: Selin's visible-copy position (38 vs thread 32); Desktop picks up web changes with no Desktop release (39 vs `loomlist-context.md` 18); field list (51 vs thread 24); rich text failure cases (68 vs thread 40); context page updated 2026-09-22 (153 vs `loomlist-context.md` 3). Placeholder: `{device name}` exempt. 153 lines against 70 to 160. Format gate: 2 findings (above).

**Open readings**

- `block-level last-writer-wins` is written "last-writer-wins at the block level" (line 20). The Pass clause attaches "verbatim" only to `Conflicting edit from {device name}`, so this is graded Met. Should the backticked term be read as verbatim too? If yes, PDK-003 fails.
- `turn-1.md` line 32 "I'll write the document and number it `002` in the doc series": graded not a file claim, because it names a number and no file or path, like the main-run PIR-001 wording "the draft will be numbered 002" that stayed PASS. Its "I'll write" plus a number sits closer to the ruling's example than PIR-002's sentence does, so the operator may want to rule on it.
- Is "A two-week spike is running" an invented status under root line 187? Borderline, not decisive.

---

## PID-001 (project), Project identity handover

**Draft row**

```csv
PID-001,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Handover FAIL: turn-1.md line 48 says ""Once you answer, the task will be `export/002 - task-due-today-filter-chip.md`"", after the block's ""I'll write the task from your answers"" (line 4), a promise of a file under root lines 179 and 189 and kernel line 101. Everything else holds: both replies open with a fenced block, then Export-equivalent path: in the task lane (turn-1.md line 42 with the -clarification name, turn-2.md line 50) and the HVR self-scan line, with no Path:, Saved: or Verified: line, and the task keeps every Turn 2 fact."
```

**Against the main run:** still failing for the same cause. The main run's "When you reply, I'll write the task as `export/002 - task-due-today-filter-chip.md`" became "Once you answer, the task will be `export/002 - task-due-today-filter-chip.md`". The verb changed, and the forecast of a concrete export file for the task stayed.

**Pass clauses** (scenario line 35, read with root line 179)

| Clause | Result | Evidence |
|---|---|---|
| Both replies open with their rendered block | Met | `turn-1.md` line 1 and `turn-2.md` line 1 open ```` ```markdown ````; closing fences at 40 and 48. Form: fenced, nothing before either block |
| `Export-equivalent path:` with a `task` lane name | Met | `turn-1.md` line 42 `export/001 - task-due-today-filter-chip-clarification.md`; `turn-2.md` line 50 `export/002 - task-due-today-filter-chip.md` |
| `-clarification` name on Turn 1 | Met | `turn-1.md` line 42 |
| `HVR self-scan:` line | Met | `turn-1.md` line 44, `turn-2.md` line 52 |
| Neither reply claims a file was saved, written or read back, and neither promises to write or save one (root line 179) | **Unmet** | `turn-1.md` line 48 "Once you answer, the task will be `export/002 - task-due-today-filter-chip.md`", with the block's line 4 "Please answer them all in one reply and I'll write the task from your answers". No `Path:`, `Saved:` or `Verified:` in either reply; `turn-1.md` line 4 "I've read context/loomlist-context.md" is a read of the attachment, not a delivery claim |
| Turn 1 block holds only the question | Met | Block lines 2 to 39: a heading, one framing line (4) and seven question groups (6 to 39), no draft |
| Turn 2 task carries its H1, `### About`, `### Requirements` | Met | `turn-2.md` line 2 `# FE - Web - TODO - Due today filter chip`, line 4, line 12 |
| Turn 2 facts intact | Met | Web only, apps later (10); right after Overdue (26); not checked off, due today in the owner's time zone (30); sorted by due date (33); one chip active (28); `filter_selected` with `filter` set to `due_today` (45); Yara's tracking plan (41); existing chip reused (27) |
| No invented fact or unfilled slot | Met (borderline noted) | Additions named at `turn-2.md` line 56 (user-value line, time-zone item, All default, event properties); no slot (`TODO` is the feature code, `loomlist-context.md` line 120) |
| Fail: `Path:`, `Saved:`, `Verified: read-back succeeded` | Not hit | None in either reply |
| Fail: a block missing or after other text | Not hit | Both blocks at line 1 |
| Fail: Turn 1 renders the task | Not hit | `turn-1.md` line 48 "so I haven't written the task yet" |
| Fail: iOS or Android scoped, "Due today" renamed, owner's time zone dropped | Not hit | Line 10 puts iOS and Android in later tasks; `Due today` throughout; owner's time zone at 22, 30, 32 |

**Blocking items hit**

- Identity handover rule, root line 179: the reply "passes when it makes no claim ... and no promise to write or save one, such as "I'll write the task as `export/002 - ...`", which is a file claim too"
- File claim on the Project side, root line 189; `Custom Instructions.md` line 101 "never promise to write or save one ... because an export-equivalent path is a label rather than a file this Project writes"

**Advisory items**

- Delivery shape: no commentary before either block, so the PID-001 exception in root line 163 is not triggered
- Asking for a fact an attachment states (root line 211): `turn-1.md` line 23 asks whether the one-active-chip rule still applies, which `loomlist-context.md` line 163 states
- Borderline, never decides alone: `turn-2.md` line 41 "so the client can send it with no further Data review" extends "which Yara has already added to the tracking plan" against `loomlist-context.md` line 191, the same extension the main run recorded

**Realism entries**

- Block `PID-001-turn1-block.md` (reply lines 2 to 39), task-lane clarification. Question alone: present. Facts: chips All, Assigned to me and Overdue with one active (22, 23 vs `loomlist-context.md` 163); Web reaching Desktop with no Desktop release (8 vs 18); locales en-US, de-DE, fr-FR, es-ES, ja-JP, pt-BR (25 vs 155); todos-service owns the view queries (29 vs 69); Data review before client work (30 vs 191). Placeholder: none. 38 lines, no band. Format gate: passed.
- Block `PID-001-turn2-block.md` (reply lines 2 to 47), task. Routed template Project Task Mode knowledge lines 52 to 58 and `Product Owner - Assets - Task Templates - v0.102.md`: title, `### About`, `### Requirements` present. Facts: Desktop through the web client (10 vs `loomlist-context.md` 18); Overdue uses the owner's time zone (22 vs 157); event properties `workspace_id`, `user_id`, `platform`, `app_version`, `plan` (46 vs 187); web build number as `app_version` (46 vs 139); existing enum values (47 vs 189). Placeholder: none. 46 lines against 30 to 70. Discipline code `FE`. Format gate: passed.

**Open readings**

- Does "Once you answer, the task will be `export/002 - task-due-today-filter-chip.md`" (`turn-1.md` line 48), in a reply whose block says "I'll write the task from your answers" (line 4), promise to write a file under root lines 179 and 189 and kernel line 101? **Graded yes.** It names the task as a concrete `export/` Markdown file before it exists, without the export-equivalent label. That is the ruling's own example with a different verb. It also matches the main-run rulings that counted "will be a new file with the next number" (PIR-002) and "I'll write the epic as the next file in this numbering" (PEP-002) as file claims even though neither says "save". The other reading treats the sentence as a forecast of the next export-equivalent label, like PIR-001's "the draft will be numbered 002", which stayed PASS. Under that reading PID-001 passes, because every other clause is met. The operator should settle this before `after_failed_gate` is set.

---

## PIR-002 (project), Conflicting commands

**Draft row**

```csv
PIR-002,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 rendered one fenced question naming $bug and $story as the detected deliverables and asking for one (turn-1.md line 6) under export/001 - intake-wishlist-sync-clarification.md, and Turn 2 a fenced Story with every required section, `50 items` and the keep-the-50-most-recent rule (lines 51 and 52), the sign-in move and the unchanged no-account wishlist. Turn 1 line 64 ""the artifact will be numbered 002 in its own lane"" names no file or path; advisory: the Story body runs 126 lines against the 50 to 100 band."
```

**Against the main run:** fixed. The main run failed on "After you answer, the Bug, Story or Epic will be a new file with the next number". This round's forward line names only the number, as Interactive Mode knowledge line 75 and kernel line 228 do.

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question naming both detected deliverables and asking for one | Met | Line 6 "I detected two deliverables in the request: `$bug` and `$story`. Choose one primary deliverable"; lines 19 to 23 offer Bug, Story or Epic with the fields each needs |
| Renders it alone as its own block | Met | Fenced, reply lines 1 to 44, nothing before it; the block holds the question and a summary of what the two files say (8 to 12), no artifact |
| `Export-equivalent path:` under an `intake` `-clarification` name | Met | Line 46 `export/001 - intake-wishlist-sync-clarification.md` |
| Turn 2 renders a `Story` block with its label | Met | `turn-2.md` lines 1 to 128 fenced; line 130 `export/002 - Story-account-wishlist-in-apps.md`; line 134 names the kind Story |
| Preamble, About, Problem, Solution, Expected outcomes, Requirements, Acceptance criteria | Met | Lines 4 to 6, 8, 12, 23, 28, 36, 60. `#### **References**` left out with no link supplied (Story Template line 47). `## Delivery` (108) is forced by the `**Open:**` line at 45 (Story Mode knowledge lines 51 and 184) |
| Turn 2 values verbatim | Met | `50 items` (51); "When the device items and the account items together pass `50 items`, the account list keeps the `50` most recently added" (52); iOS and Android signed-in to the account (40); same list web shows (41); first sign-in move (47); no-account device wishlist as today (56) |
| Device and account facts as the attachments state them | Met | Line 14 "The apps save the wishlist on the device and web saves it to the account ... This has been the design since the wishlist first shipped in the apps, and nothing about it changed in 4.8.0 or 4.8.2" (wishlist feedback line 45, `fernhouse-context.md` 146) |
| No invented fact or unfilled slot | Met (borderline noted) | Additions named at `turn-2.md` lines 139 to 141; the Open line named at 136; `TBD...` in Estimation and No-gos is exempt (root line 207) |
| No file claim on either turn | Met | No `Path:`, `Saved:`, `Verified:`. `turn-1.md` line 64 "When you answer, the artifact will be numbered 002 in its own lane" names a number, no file or path |
| Fail: Turn 1 picks or renders an artifact | Not hit | No artifact in Turn 1; the Bug option explains what a bug would need (21) without choosing |
| Fail: second round on Turn 2 | Not hit | Turn 2 renders the Story; the three questions at 143 to 146 are left out of the Story, not asked before it |
| Fail: apps ever saved to the account, web changed, device-only wishlist called a defect | Not hit | Lines 14 and 25 |

**Blocking items hit:** None.

**Advisory items**

- Size: 126 block lines against 50 to 100, over the band
- Borderline, never decides alone: line 10 "Product signed off the change on 2026-09-25" converts the Turn 2 "Lotte signed this off yesterday" with the session clock; Lotte is Head of Product (`fernhouse-context.md` line 3)
- Turn 1 includes the energy choice (14 to 17), not graded

**Realism entries**

- Block `PIR-002-turn1-block.md` (reply lines 2 to 43), intake clarification. Question alone: present. Facts: Maud, 2026-09-21, 412 contacts from 2026-07-01 to 2026-09-20 (10 vs wishlist feedback 3 and 7); Teun, 2026-09-22, device vs account and nothing changed in 4.8.0 or 4.8.2 (11 vs feedback 43 and 45); Lotte not answered (12 vs feedback 51); both lists hold up to 50 items (33 vs `fernhouse-context.md` 146). Placeholder: none. 42 lines, no band. Format gate: passed.
- Block `PIR-002-turn2-block.md` (reply lines 2 to 127), Story. Routed template Project `Product Owner - Assets - Story Template - v0.100.md` lines 21 to 85 and section 3: every required section present. Facts: 171, 138, 64 and 39 contacts (15 to 18 vs feedback 11 to 14); monthly counts 118, 139, 155 (14 vs feedback 17); 23 complaint-tagged contacts (20 vs feedback 35); third biggest tag after WISMO and returns (14 vs feedback 7); next app release 4.9.0 in the reply (136 vs `fernhouse-context.md` 120). Placeholder: `TBD...` in two Delivery slots, exempt. 126 lines against 50 to 100. H1 carries no discipline code, as the Story H1 rule asks. Format gate: passed.

**Open readings**

- Is "When you answer, the artifact will be numbered 002 in its own lane" (`turn-1.md` line 64) free of a file claim? Graded yes, under the PIR-001 main-run precedent ("the draft will be numbered 002") and the Project's own wording (Interactive Mode knowledge line 75, `Custom Instructions.md` line 228). If the operator counts a number forecast as a promise, PIR-002 and PDK-003 both fail on it.

---

## Twin notes

**SBG-002 and PBG-002: differ (PASS, FAIL). Runtime fault on the Project side.** Both runtimes asked first, and both built the same bug: the same amounts, the correct charge, Severity High, no device, the error-message line left out and Pay at property left open. The only difference is PBG-002's `turn-1.md` line 25 promise, "I'll write the report under the next number in the bug lane (`export/002 - bug-...`)". The skill may promise its own export (`references/bug-mode.md` line 63, `AGENTS.md` line 44). The Project kernel forbids that promise (`Custom Instructions.md` line 101), and the Project Bug Mode knowledge says only "The artifact takes the next number in the lane once the user answers" (line 46), which licenses no path. One small parity difference with no effect here: the skill states the error-message rule in Bug Mode itself (`bug-mode.md` lines 158 and 217), while the Project carries it only in the Assets template (`Product Owner - Assets - Bug Report Template - v0.101.md` line 85). Both runtimes complied.

**SDK-001 and PDK-001: agree (FAIL, FAIL), for different causes, each a runtime fault.** SDK-001 renamed the mandatory primary body to `## Stacking rules` and PDK-001 kept `## Behavior rules`. Both packagings carry the same rule: Overview and the primary body are mandatory, and only optional headings may be renamed (skill `assets/doc-templates.md` lines 115, 116 and 400; Project Doc Templates lines 94, 95 and 379). PDK-001 dropped the phrase `one discount code per order`, while SDK-001 kept it verbatim (line 53). Here the packagings agree too, and neither demands that a new document quote a source's rule phrase word for word. Their literal-copy rules cover refinements (skill `doc-mode.md` line 584, Project Doc Mode line 558), and "Preserve supplied technical identifiers" is qualified "when needed for fidelity" (skill `doc-templates.md` line 125, Project Doc Templates line 104). The verbatim demand comes from the scenario and root line 188, so the miss also points at a rule gap between the scenario and both packagings.

**SDK-003 and PDK-003: agree (PASS, PASS).** Both covered authority by stating the two files agree rather than asking which governs (skill clarification line 3, Project block line 2), so the same open reading holds for both. Both followed their Proposal scaffold's Source basis line into the format gate's em dash finding (skill `doc-templates.md` line 570, Project Doc Templates line 549). They differ only on the Doc summary. PDK-003 printed the five lines (`Custom Instructions.md` line 217) and SDK-003 printed none (`doc-mode.md` line 412). The rule is the same on both sides, so that is a skill runtime fault, recorded as advisory.

**PID-001 and PIR-002:** their twins (SID-001, SIR-002) are graded in other batches. On forward statements within this batch, the replies that attach an `export/` path to the next artifact failed (PID-001 line 48, PBG-002 line 25). The ones that name only the next number passed (PIR-002 line 64, PDK-003 line 32). Both kinds sit under the same kernel rule (`Custom Instructions.md` line 101) and the same Interactive Mode sentence (knowledge line 75).
