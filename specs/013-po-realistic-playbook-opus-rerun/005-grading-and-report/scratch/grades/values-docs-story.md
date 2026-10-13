# Values round grades: batch `values-docs-story`

Batch: SDK-001, PDK-001, SDK-003, PDK-003, SST-002, PST-002. Model `claude-opus-5-5-medium`. Run folder `<RUN>/remeasure-supplied-values/run-1/`, where `<RUN>` is `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`. Product Owner commit `b50f0a0`, Barter commit `7396d79e`, playbook root 2.2.0.0, skill 1.13.0, kernel v1.16.0. `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing and `git log` shows HEAD at `b50f0a0`, so every source, scenario file and fixture was read from the working tree and every line below is cited as it stands at `b50f0a0`.

## Tally

| Runtime | PASS | FAIL | SKIP |
|---|---:|---:|---:|
| skill | 3 (SDK-001, SDK-003, SST-002) | 0 | 0 |
| project | 3 (PDK-001, PDK-003, PST-002) | 0 | 0 |

One verdict rests on an open reading: PDK-003 passes only because the thread's pinned `Status: not decided` is read as neither backticked nor a status-key word under root line 150. Open readings under PDK-003 set out the reading that fails it.

## Method notes

- Scenario files read at `b50f0a0`: `skill-document-modes/behavior-reference.md` and `project-document-modes/behavior-reference.md` (Pass/fail line 39), `skill-document-modes/proposal-decision-owner.md` and `project-document-modes/proposal-decision-owner.md` (line 39), `skill-story-modes/story-forced-delivery.md` and `project-story-modes/story-forced-delivery.md` (line 35). Root rules cited from `sk-product-owner/manual-testing-playbook/manual-testing-playbook.md` at `b50f0a0`, where lines 150, 179, 187 to 190 and 198 to 214 hold the text the briefs name.
- Root line 150 as it now stands is applied to every backticked value: word for word where the source sets it in backticks, gives it as a defined label such as a word from a status key, or the clause says verbatim for it; elsewhere the same value in other words meets the clause.
- Write authority for this round is this one file, so the Project block copies and the SDK-001 Turn 1 reconstruction sit in the session scratchpad, not under `scratch/grades/blocks/`. Each block copy is the text between the opening and closing fence, so block line `k` is reply line `k + 1`, and each is byte-identical (`cmp`) to the collector's copy under `AI Systems/Product Owner/export/benchmark/claude project/remeasure-supplied-values/run-1/`. Every skill export in the run folder is byte-identical to its copy under `export/benchmark/skill/remeasure-supplied-values/run-1/`.
- Format gate: `node validate-output-format.cjs --system product-owner <file>` from the Sync Loop folder, on all five skill exports, on the reconstructed SDK-001 Turn 1 export and on the six Project block copies. All twelve printed `Product Owner output format validation passed across 1 artifact file(s)` with exit 0.
- SDK-001 Turn 2 edited `export/001 - doc-promotion-stacking.md` in place (turn 2 ledger `modified`), so the run folder holds only the Turn 2 state. The Turn 1 state is rebuilt from the full Read result at `events-turn-1.jsonl` line 118 with the one later Edit (line 123, "four cases" to "five cases") applied. It has 164 lines. Cited below as "T1 export".
- Every Project run's `meta.json` shows an empty ledger on both turns and the tools `read`, `ls`, `grep`, `find` only. Every Project block was fenced (```` ```markdown ```` at reply line 1) with nothing before it.
- In Project tables, line numbers are reply lines (`turn-<n>.md`) unless marked as block lines.
- `after_failed_gate` is `no` on every row, per `grading-brief-values.md` line 40.

---

## SDK-001 (skill), Behavior reference

**Draft row**

```csv
SDK-001,skill,claude-opus-5-5-medium,PASS,2,2,no,yes,"Turn 1 drafted at once with no question into export/001 - doc-promotion-stacking.md, and both states keep ## Behavior rules (line 29 in each) and every protected value verbatim: one discount code per order (line 42), automatic promotions first (35), exclusive, STAFF-, compare_at, applies_to_sale, the 50% cap (67) and 0.01 half up (74). Turn 2 revised in place with the two-codes rule labelled retired on 2026-05-01 (143) and its refund split (145), and no merchandiser Admin setup; advisory: a four-line Doc summary, and the Turn 1 Read after the last Edit returned lines 1 to 8 of 165."
```

**Against the latest earlier verdict (round one FAIL):** fixed. Round one failed because both turns named the primary body `## Stacking rules`. Both states now carry `## Behavior rules` at line 29.

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| T1 routes to Doc Mode | Met | Export word `doc`; `doc-mode.md` printed by the Bash calls at `events-turn-1.jsonl` lines 17, 19 and 39 (results 18, 20 and 40 carry the file's text beneath the sandbox's `/dev/null` noise) and `doc-templates.md` Read at line 45; `turn-1.md` line 1 "I've written a behavior reference" |
| T1 asks no question and writes no clarification | Met | `turn-1.md` lines 1 to 26 hold no question (line 26 is an offer). Turn 1 ledger creates only `export/001 - doc-promotion-stacking.md` |
| T1 saves in the doc lane on the first number | Met | `export/001 - doc-promotion-stacking.md` (`turn-1.md` line 3) |
| T1 reads it back | Met | Write at event line 82, last Edit at 123, Read at 125 returned lines 1 to 8 of 165 (partial, see Read-back table and Open readings) |
| A Behavior reference with an Overview and a `## Behavior rules` body | Met | T1 export line 10 `## Overview`, line 29 `## Behavior rules`; `turn-1.md` line 16 names the shape |
| `* * *` directly under every content heading | Met | Every heading from line 10 to 161 is followed by `* * *` on the next line (checked by script); the H1 takes one blank line first, as `doc-mode.md` line 90 requires |
| `*   ` bullets, no hyphen bullets, no `---` | Met | Lines 19 to 26, 49 to 50, 154 to 158; no `- ` bullet or `---` line; format gate passed |
| Sentence-case headings | Met | All 22 headings, for example line 45 `### Exclusive promotions and codes`, line 141 `### Retired rule: two codes on one order` |
| No empty spacer heading | Met | No `##   ` or `###   ` line in the file |
| `one discount code per order` verbatim | Met | T1 export line 42 "A customer can use `one discount code per order`." |
| `automatic promotions first` verbatim | Met | Line 35 "The rule's own wording is `automatic promotions first`." |
| `exclusive` | Met | Line 47 |
| `STAFF-` | Met | Line 57 |
| `compare_at` | Met | Line 62 |
| `applies_to_sale` | Met | Line 62 |
| The `50%` cap | Met | Line 67 |
| `0.01` `half up` rounding | Met | Line 74 "rounded to `0.01` with `half up` rounding" |
| T2 asks no question | Met | `turn-2.md` lines 1 to 18, no question; line 18 "Tell me if you'd rather drop them" is an offer |
| T2 delivers the revised doc in the doc lane | Met | Same path, Turn 2 ledger `modified`; `turn-2.md` line 3; where it saved is not graded |
| T2 same layout checks | Met | Final export: every heading from line 10 to 160 followed by `* * *`, `*   ` bullets, sentence case, no spacer heading; format gate passed |
| T2 every value still verbatim | Met | Lines 42, 35, 47, 57, 62, 62, 67, 74, exactly as in T1 |
| Two-codes rule in and labelled retired since `2026-05-01` | Met | Line 141 heading; line 143 "Status: Retired material" then "retired on 2026-05-01, kept so CS can explain and refund orders placed before that date. Do not build on it"; line 147 keeps it apart from current behavior |
| No account of how merchandisers set promotions up in Admin | Met | `grep -i "merchandis\|admin\|set up\|configur"` hits only line 147 "Orders placed before `2026-05-01` can still show two codes in Admin" (rules note line 50) and line 162 "Merchandising space". The T1 lines 12, 14 and 19 on merchandisers and Admin are gone |
| Nothing the two attachments do not state | Met | Every rule traces to `fernhouse-promotions-rules.md` lines 3 to 52; the 12% derivation (line 35) and the threshold consequence (line 81) are named as additions at `turn-1.md` lines 20 to 22 and `turn-2.md` line 18. Borderlines below |
| Fail: two-codes rule presented as current | Not hit | Lines 141 to 147 in both states |
| Fail: a supplied value altered, a rule, number or example invented | Not hit | Staff 30% (57), €4.95 and £3.95 (81), all four worked examples copied (112 to 138) against rules lines 10, 13, 19 to 42 |

**Blocking items hit:** None.

**Advisory items**

- Doc summary (`doc-mode.md` line 412 asks five lines): `turn-1.md` lines 14 to 18 and `turn-2.md` lines 12 to 16 print four, "Shape" for Shape fit and "Readability and voice" as one line. An Expected signal, not a Pass clause
- Size band 80 to 180: T1 export 164 lines, final export 163 lines. Inside the band
- Borderline, never decisive alone: line 57 "They are also the one kind of code that always applies to sale items" (rules line 10 says staff codes "also apply to sale items"; rules line 11 lets any promotion with `applies_to_sale` switched on apply too); line 110 calls HOME15, HOME25 and WELCOME10 "sample codes"; line 31 "all markets"; T1 line 12 "Merchandisers use it when setting up a promotion" against rules line 3 "check when a discount looks wrong"

**Read-back table**

| Turn | Export path | `N` printed | Read after the last write, lines returned | Real `wc -l` |
|---|---|---:|---|---:|
| 1 | `export/001 - doc-promotion-stacking.md` | 165 | Write line 82, Edits 98 to 111, full Read line 117 (1 to 165), last Edit line 123, Read line 125 (offset 1, limit 8), result line 126: lines 1 to 8, totalLines 165 | 164 (reconstruction; the Turn 1 state no longer exists on disk) |
| 2 | `export/001 - doc-promotion-stacking.md` | 163 | Edits lines 13 to 29 (last at 29), Read line 37, result line 38: lines 1 to 164, totalLines 164 | 163 |

The Bash at Turn 1 line 94 failed on the sandbox's here-document ban and wrote nothing (result line 95 prints the pre-edit text), so the Edits from line 98 are the writes.

**Realism entries**

- T1 export (reconstructed), Behavior reference. Routed template `assets/doc-templates.md` lines 355 to 450: Overview (10) and `## Behavior rules` (29) present, optional Glossary, Combinations and precedence, Examples, Related references each earning its Include-when row (lines 461 to 468). Facts: Colette, Promotions lead, last edited 2026-09-02 (line 5 vs rules line 3); staff codes 30% off (57 vs rules 10); standard shipping €4.95 or £3.95 (81 vs rules 13); code path removed 2026-05-04 (145 vs rules 52); banner copy `Free shipping on orders over €50` (158 vs `fernhouse-context.md` line 20). Placeholder: none. 164 lines, inside 80 to 180. Discipline code: not applicable. Format gate: passed
- Final export, Behavior reference, same template, same sections present. Facts: Colette owns the governing note (162 vs rules 3); Lotte in the Product space (163 vs context 3); refund splits the discount across both codes (145 vs rules 50); catalog-service holds `compare_at` (62 vs rules 11). Placeholder: none. 163 lines, inside the band. Format gate: passed

**Open readings**

- The Turn 1 read-back after the last Edit was a partial Read, lines 1 to 8 of 165 (`events-turn-1.jsonl` line 125); the full Read (line 117) came before that Edit. `AGENTS.md` step 6 asks for a Read that returns non-empty content, which this did. Does a partial Read after the last write count as the read-back? Graded yes, as earlier rounds did (`scratch/grades/stories.md` line 64)
- `N`: Turn 1 printed 165, the Read's totalLines, against 164 lines on disk; Turn 2 printed 163, the `wc -l` count, against the Read's final line 164. Recorded only, no Pass clause makes the count a condition

---

## PDK-001 (project), Behavior reference

**Draft row**

```csv
PDK-001,project,claude-opus-5-5-medium,PASS,2,2,no,yes,"Both fenced Behavior reference blocks carry ## Behavior rules (turn-1.md line 37, turn-2.md line 39) and every protected value verbatim, with one discount code per order in the sentence stating the rule (turn-2.md line 45) and automatic promotions first at line 50, under export/001 - doc-promotion-stacking-rules.md and with no question on Turn 1. Turn 2 names CS agents and Checkout engineers, keeps the two-codes rule labelled retired on 2026-05-01 (line 148), leaves the Admin setup out (line 16) and claims no file; borderline only: ""this is a file export"" (turn-1.md line 169, turn-2.md line 172)."
```

**Against the latest earlier verdict (round one FAIL):** fixed. Round one dropped `one discount code per order` behind the label "**3. One code per order**". Both turns now state it in the rule's own sentence (`turn-1.md` line 43, `turn-2.md` line 45).

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| T1 routes to Doc Mode | Met | Reads Doc Mode knowledge (`events-turn-1.jsonl` line 17) and Doc Templates (34); doc-lane label |
| T1 no question, no clarification block | Met | `turn-1.md` lines 1 to 182: one artifact block, no question; line 182 is a next-step suggestion |
| Behavior reference with a doc-lane export-equivalent label | Met | Line 162 `export/001 - doc-promotion-stacking-rules.md`; line 168 names the shape |
| Overview and `## Behavior rules` body | Met | Lines 12 and 37 |
| `* * *` under every content heading, `*   ` bullets, sentence case | Met | Block copy: every heading after the H1 followed by `* * *`; no hyphen bullet or `---` inside the block (the chat report after it uses `- `, outside the artifact); headings such as line 64 `### Sale items and staff codes`; format gate passed. Spacer headings not graded (scenario line 67) |
| `one discount code per order` | Met | Line 43 "A customer can use `one discount code per order`." |
| `automatic promotions first` | Met | Line 48 "promotions-service applies `automatic promotions first`, then the discount code on the price that is left" |
| `exclusive`, `STAFF-`, `compare_at`, `applies_to_sale` | Met | Lines 58, 68, 66, 66 |
| `50%` cap, `0.01` `half up` | Met | Lines 73 and 88 |
| T2 no question | Met | `turn-2.md` lines 1 to 187, no question |
| T2 revised reference with a doc-lane label | Met | Line 165 `export/001 - doc-promotion-stacking-rules.md`; which label is not graded |
| T2 same layout checks | Met | Block copy passes the same script checks and the format gate |
| T2 every value still verbatim | Met | Lines 45, 50, 60, 70, 68, 68, 75, 90 |
| Two-codes rule labelled retired since `2026-05-01` | Met | Line 146 heading; line 148 "Status: Retired material" then "retired on 2026-05-01"; line 150 "Do not build on this rule, and do not use it to predict a new cart"; line 110 its own table row marked Retired material; refund split line 152 |
| No merchandiser Admin setup | Met | Line 16 "How a promotion is set up in Admin is outside this reference." states the exclusion; glossary line 21 drops "set up by a merchandiser in Admin" (T1 line 21); the only other Admin mention is line 152, the note's own line 50 |
| Nothing the two attachments do not state | Met | Additions named at `turn-2.md` lines 180 to 186 (four conclusions and the retired-section line); Boundaries lines 157 to 161 state gaps as gaps |
| No file claim on either turn | Met | No `Path:`, `Saved:`, `Verified:`, and no promise to write or save. `turn-1.md` line 169 "because this is a file export" and `turn-2.md` line 172 "no spacer headings in the file export" use Project Doc Mode line 73's layout term and name no save (Open readings) |
| Fail: two-codes rule as current, value altered, rule, number or example invented | Not hit | Worked examples lines 117 to 143 against rules lines 19 to 42; staff 30% line 70 vs rules 10 |

**Blocking items hit:** None.

**Advisory items**

- Size band 80 to 180: T1 block 158 lines, T2 block 161 lines. Inside the band
- Commentary: none before either block
- Borderline, never decisive alone: "The rules hold in all five markets" (`turn-1.md` line 16 with "on web, iOS and Android", `turn-2.md` line 16), inferred from rules line 13's euro markets and UK; Checkout engineers "whose services carry the prices promotions-service returns" (`turn-2.md` line 16), against `fernhouse-context.md` line 61

**Realism entries**

- T1 block (reply lines 2 to 159), Behavior reference. Routed template `Product Owner - Assets - Doc Templates - v0.108.md` Behavior reference scaffold (Project line 334 onward, mirroring skill 355 to 450): Overview and `## Behavior rules` present. Facts: Colette, Promotions lead, Merchandising, 2026-09-02 (line 6 vs rules line 3); Lotte, Head of Product, 2026-09-18 (7 vs context 3); cart-service holds line prices after automatic promotions (34 vs context 61); only merchandisers change a promotion, in Admin (34 vs context 33). Placeholder: none. 158 lines. Format gate: passed
- T2 block (reply lines 2 to 162), Behavior reference, same sections. Facts: cart-service, which Checkout owns (36 vs context 61); standard shipping €4.95 or £3.95 (83 vs rules 13); code path removed 2026-05-04 (148 vs rules 52); banner copy `Free shipping on orders over €50` (157 vs context 20). Placeholder: none. 161 lines. Format gate: passed

**Open readings**

- Is "this is a file export" (`turn-1.md` line 169, `turn-2.md` line 172) a file claim under root line 189 and kernel line 101? It names none of the kernel's verbs (saved, verified, read back, pushed, will write, will save, will update), though kernel line 221 says the deliverable is "never a file". Graded no, as every earlier round did (`scratch/grades/docs.md` lines 141 and 263, `scratch/grades/remeasure-bugs-docs-identity.md` line 256)

---

## SDK-003 (skill), Proposal with a decision owner

**Draft row**

```csv
SDK-003,skill,claude-opus-5-5-medium,PASS,2,2,no,yes,"Turn 1 saved the question-only export/001 - doc-sync-conflicts-lost-edits-clarification.md covering source set, authority, status, shape and scope (lines 7 to 19), read back, and Turn 2 saved export/002 - doc-sync-conflict-options.md with the Proposal notice under the title reading not decided (line 4), block-level last-writer-wins as today's state (19), Options A to C with Conflicting edit from {device name} verbatim (59), support for B attributed (93 to 96) and Joana deciding on 2026-10-09 (103). Advisory: no five-line Doc summary in turn-2.md; borderline: ""spike in progress"" (line 57)."
```

**Against the latest earlier verdict (round one PASS):** still passing, for the same reasons. Round one's format gate finding on the Source basis bullets is gone: the gate passes this export.

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated question | Met | Clarification lines 3 to 19, one message; `turn-1.md` lines 7 to 13 summarize it |
| Covers source set | Met | Clarification line 7 "**Source set:**", naming `Sync conflicts, options for v3 and after` as not supplied |
| Covers authority | Met | Line 9 "**Authority:**" "Can the thread govern the options, numbers and next steps, with the context page governing product facts" |
| Covers status | Met | Line 11 "**Status:**" current v3, Options as proposals, neutral or recommending |
| Covers shape | Met | Line 13 "**Shape:**" narrative status overview or decision brief |
| Covers scope | Met | Lines 15 to 19 "**Scope:**" four in-or-out items |
| Exported in the doc lane, read back | Met | `export/001 - doc-sync-conflicts-lost-edits-clarification.md`; Read at `events-turn-1.jsonl` line 57 after the last Edit at 55, lines 1 to 20 of 20 |
| No draft | Met | Turn 1 ledger creates only the clarification; `turn-1.md` line 1 "I haven't written the document yet" |
| T2 Proposal with the status notice directly below the title | Met | `002` lines 3 to 6: line 4 opens "Status: Proposal" and, after the status delimiter, reads "not decided, not current product behavior"; line 5 "Joana, Engineering Manager, Sync, decides on 2026-10-09" |
| Overview and a proposed-design or options body | Met | Line 8 `## Overview`, line 40 `## Options` |
| `* * *` under every content heading, `*   ` bullets, sentence case, no spacer | Met | Script check and format gate passed; headings such as line 42 `### Option A, field-level last-writer-wins` |
| Today's v3 block-level last-writer-wins as the current state | Met | Line 17 "Status: Current behavior", line 19 "Protocol v3 resolves conflicts with block-level last-writer-wins." (thread line 14) |
| `Option A` as `field-level` last-writer-wins | Met | Lines 42 and 46 |
| `Option B` as a `three-way merge` with `Conflicting edit from {device name}` verbatim | Met | Line 55 `### Option B, three-way merge on block text`; line 59 "labelled `Conflicting edit from {device name}`" and line 61 |
| `Option C` as a `CRDT` | Met | Lines 70 and 74 |
| Support for B attributed to the people who gave it | Met | Lines 93 to 96: Selin, Marta ("her estimate"), Saskia's condition, Tomasz "leans B, but only with Saskia's fallback" |
| `Joana` decision owner, `2026-10-09`, status `not decided` | Met | Line 103 "Joana owns the decision and will make it on 2026-10-09."; line 4 "not decided" (thread line 66) |
| No option called chosen, agreed, approved or decided | Met | `grep -i "chosen\|agreed\|approv\|decided"` hits only line 4 "not decided" |
| Nothing the two attachments do not state | Met | Current state lines 19 and 21 trace to `loomlist-context.md` lines 59, 60, 70, 169, 177, 180; options to thread lines 22 to 28; the two judgements are named at `turn-2.md` lines 19 to 21 |
| Fail: figure or estimate changed | Not hit | `0.8%` (28), `40` `lost-edit` and 22 (12), 58% and 42% (30), about 3 weeks (50), 6 to 8 weeks (63), two quarters (74), against thread lines 10, 18, 24, 26, 28, 48 |
| Fail: `{device name}` filled | Not hit | Lines 59 and 61 keep the braces; "such as Work laptop" is Selin's example (thread line 32) |

**Blocking items hit:** None.

**Advisory items**

- Doc summary: `turn-2.md` prints no Source safety, Shape fit, ClickUp layout, Readability and Voice lines (`doc-mode.md` line 412). An Expected signal, not a Pass clause
- Size band 70 to 160: 126 lines. Inside the band
- Borderline, never decisive alone: line 57 "Status: Proposal" then "described by Tomasz, spike in progress", where the thread says "Tomasz runs a two-week spike" (line 58) with no start date

**Read-back table**

| Turn | Export path | `N` printed | Read after the last write, lines returned | Real `wc -l` |
|---|---|---:|---|---:|
| 1 | `export/001 - doc-sync-conflicts-lost-edits-clarification.md` | 19 | Write line 46, Read 49, last Edit line 55, Read line 57, result line 58: lines 1 to 20, totalLines 20 | 19 |
| 2 | `export/002 - doc-sync-conflict-options.md` | 126 | Write line 33, Edits 48, 50, 58, full Read 60 (1 to 128), last Edit line 68, Read line 70 (offset 110), result line 71: lines 110 to 127, totalLines 127 | 126 |

The Bash at Turn 2 line 45 failed on the here-document ban (result line 46) and wrote nothing.

**Realism entries**

- `001 - doc-sync-conflicts-lost-edits-clarification.md`, doc-lane clarification. Question alone: present. Facts: Tomasz's doc `Sync conflicts, options for v3 and after` (line 7 vs thread 22); Joana decides 2026-10-09 (11 vs thread 67 and 68); estimates about 3 weeks, 6 to 8 weeks, two quarters (11 vs thread 24, 26, 28); Marta's 33 of the 40 (11 vs thread 36). Placeholder: none. 19 lines, no band. Format gate: passed
- `002 - doc-sync-conflict-options.md`, Proposal. Routed template `assets/doc-templates.md` Proposal scaffold (skill lines 476 to 571): status notice, Overview and options body present; optional Current state, Open decisions, Out of scope, Source basis present. Facts: 40 `lost-edit` tickets up from 22 (12 vs thread 10); frame `Sync / Conflict copy` (61 vs thread 32); context page updated 2026-09-22 (125 vs context 3); thread exported by Joana on 2026-09-22 (124 vs thread 3). Placeholder: `Conflicting edit from {device name}` is exempt, quoted verbatim from thread line 26 (root line 207). 126 lines, inside 70 to 160. Format gate: passed

**Open readings**

- The Turn 2 read-back after the last Edit was a partial Read, lines 110 to 127 of 127 (`events-turn-2.jsonl` line 70). Graded Met, as for SDK-001
- `N` 19 and 126 match `wc -l`; the Reads' final lines were 20 and 127. Recorded only

---

## PDK-003 (project), Proposal with a decision owner

**Draft row**

```csv
PDK-003,project,claude-opus-5-5-medium,PASS,2,2,no,yes,"Turn 1 under $d rendered a fenced question-only block covering source set, authority, status, shape and scope (turn-1.md lines 12 to 34) under export/001 - doc-sync-conflicts-lost-edits-status-clarification.md, and Turn 2 a fenced Proposal with the notice under the title (lines 5 to 6), block-level last-writer-wins verbatim (20), Options A to C, support for B attributed (89 to 92), Joana on 2026-10-09 and no file claim. The block never prints not decided and gives it in other words (""Nothing here is decided"", line 12), which meets the clause under root line 150 because the thread's pinned Status line is neither backticked nor a status-key word; that reading is open and turns the row to FAIL if the operator rules otherwise."
```

**Against the latest earlier verdict (round one FAIL):** fixed. Round one failed on "Protocol v3 applies last-writer-wins at the block level" under the old word-for-word convention. The clause is now relaxed, and this run writes "block-level last-writer-wins" in the thread's words anyway (`turn-2.md` line 20). A new open reading replaces it: the status `not decided` appears only in other words, where round one and the main run printed it (`remeasure-operator-repairs/run-1/replies/PDK-003-turn2.txt` line 5, `replies/PDK-003-turn2.txt` line 5).

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated question | Met | Block `turn-1.md` lines 2 to 36, one message with eight labelled parts |
| Covers source set | Met | Line 12 "**Source set:** Should I use only these two files?" with the two unsupplied items at 13 and 14 |
| Covers authority | Met | Line 18 "**Authority & figures:** Please confirm how I should handle these" |
| Covers status | Met | Line 23 "**Document status:**" v3 current, A to C proposals, no approved direction |
| Covers shape | Met | Lines 31 to 34 "**Shape:**" Narrative overview, Proposal or Guide |
| Covers scope | Met | Lines 25 to 29 "**Scope:**" |
| Rendered as its own block with a doc-lane clarification label | Met | Fenced, reply lines 1 to 37, nothing before it; line 39 `export/001 - doc-sync-conflicts-lost-edits-status-clarification.md`; HVR line 41 |
| No draft | Met | Line 45 "I haven't written the document yet" |
| T2 Proposal with the status notice directly below the title | Met | `turn-2.md` lines 4 to 7: line 5 opens "Status: Proposal" and, after the status delimiter, reads "not current product behavior"; line 6 "none of them is approved" |
| Overview and an options body | Met | Lines 9 and 34 |
| `* * *` under every content heading, `*   ` bullets, sentence case | Met | Script check on the block copy and format gate passed; spacer headings not graded (scenario line 67) |
| Today's v3 block-level last-writer-wins as current state | Met | Line 20 "Protocol v3 settles conflicts with block-level last-writer-wins." |
| `Option A` `field-level`, `Option B` `three-way merge` with `Conflicting edit from {device name}` verbatim, `Option C` `CRDT` | Met | Lines 37, 50, 53, 65 |
| Support for B attributed | Met | Lines 89 to 92: Selin, Marta, Tomasz with Saskia's fallback, Saskia's condition |
| `Joana` decision owner, `2026-10-09` decision date | Met | Line 6 "Joana, Engineering Manager, Sync, decides on 2026-10-09"; line 100 |
| Status `not decided` | Met, on an open reading | The literal "not decided" appears nowhere in either reply. The block says line 6 "none of them is approved", line 12 "Nothing here is decided.", line 87 "There's no recommendation or decision on record.", line 94 "Didn't decide in the thread." Thread line 66 gives "Status: not decided" as plain text, not in backticks; the only status key in the fixtures is `roamstay-booking-funnel-tracking-plan.md` line 28; the clause attaches "verbatim" only to `Conflicting edit from {device name}`. So root line 150's "Elsewhere the same value stated in other words meets the clause" applies |
| No option called chosen, agreed, approved or decided | Met | Line 92 "If Option B is chosen" reports Saskia's condition (thread line 40 "If we go with B"); line 6 "none of them is approved" |
| Nothing the two attachments do not state | Met | Line 20 traces to context lines 169, 177, 180; line 118 to context line 3; the Out of scope additions are named at line 137. Borderlines below |
| Claims no file | Met | No `Path:`, `Saved:`, `Verified:`. `turn-1.md` line 51 "Once you answer, I'll write the document." names no file or path; `turn-2.md` line 130 "It's formatted as a file export" is Doc Mode's layout term (Open readings) |
| Fail: figure or estimate changed | Not hit | 22 and 40 (24), 0.8% (25), 58% and 42% (26), 3 weeks (44), 6 to 8 weeks (56), 33 of the 40 (57), two quarters (70) |

**Blocking items hit:** None, on the text reading of `not decided`. On the other reading, a protected fact generalized (root line 188) and a missed Pass clause (root line 150).

**Advisory items**

- Size band 70 to 160: Turn 2 block 119 lines. Inside the band
- Commentary: none before either block
- Borderline, never decisive alone: line 47 "Tomasz is writing down what Option A would take", line 62 "Tomasz is running a two-week spike", line 80 "Proposed, in spike", present progressive where the thread's "Tomasz runs a two-week spike ... and writes down" (line 58) gives no start. Line 6 "decides on 2026-10-09 once Tomasz's spike on Option B is done" matches the scenario's own framing, "with Tomasz's two-week spike on B as the step before it" (scenario line 67)

**Realism entries**

- T1 block (reply lines 2 to 36), doc-lane clarification. Question alone: present. Facts: thread exported on 2026-09-22 (23 vs thread 3); `Sync / Conflict copy` and the options doc not supplied (13 and 14 vs thread 22 and 32); an edit made without a connection retried until the app closes, then lost (27 vs context 176); Yara's 58% counts checkbox, due date or assignee sessions (20 vs thread 48). Placeholder: none. 35 lines. Format gate: passed
- T2 block (reply lines 2 to 120), Proposal. Routed template `Product Owner - Assets - Doc Templates - v0.108.md` lines 461 to 550: status notice, Overview and options body present; Open decisions, Out of scope, Source basis present. Facts: Elif, Product Operations, updated 2026-09-22 (118 vs context 3); v3 has no merge and no conflict copy (20 vs context 177); the phone on the train, laptop at the office pattern (22 vs thread 10); Selin, Product Designer, Sync (89 vs thread 30). Placeholder: `Conflicting edit from {device name}` exempt (root line 207). 119 lines. Format gate: passed

**Open readings**

- Root line 150: does the thread's pinned "Status: not decided" (line 66, beside "Decision owner:" and "Decision date:") give `not decided` "as a defined label such as a word from a status key"? Graded no here, because the line is plain text and defines nothing, and the only status key in the fixtures is Roamstay's legend. If the operator reads a pinned `Status:` field as a defined label, the clause is Unmet and PDK-003 is FAIL. Doc Mode's own rule points toward carrying it: "Explicit status markers travel with the claims they qualify" (Project `Product Owner - Templates - Doc Mode - v0.111.md` line 129, skill `doc-mode.md` line 153)
- Is "Once you answer, I'll write the document." (`turn-1.md` line 51) a promise to write a file under kernel line 101 and root line 189? It names neither a file nor a path. Graded no, as round one graded "I'll write the document and number it `002`" (`scratch/grades/remeasure-bugs-docs-identity.md` line 371)
- Is "It's formatted as a file export" (`turn-2.md` line 130) a file claim? Graded no, as under PDK-001

---

## SST-002 (skill), Story forced delivery

**Draft row**

```csv
SST-002,skill,claude-opus-5-5-medium,PASS,2,2,no,yes,"Turn 1 saved only the Story question as export/001 - Story-view-only-share-links-clarification.md and read it back, and Turn 2 saved export/002 - Story-view-only-share-links.md, whose **Open:** line now quotes Do sub-pages inherit the link? word for word and names Lena (line 66), repeated in Rabbit holes (159), with every Requirements value verbatim (lines 32 to 61), no sub-page criterion and a Delivery close with TBD... in Estimation and No-gos. Advisory only: 166 lines inside 90 to 170, and N 167 printed against 166 on disk."
```

**Against the latest earlier verdict (round one FAIL):** fixed. Round one's Open line read "whether a link on a page also opens its sub-pages". This round's reads "**Open:** `Do sub-pages inherit the link?`" (line 66).

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question | Met | Clarification lines 3 to 22, one message; `turn-1.md` lines 7 to 13 |
| Saves only that question in the Story lane | Met | `export/001 - Story-view-only-share-links-clarification.md`; Turn 1 ledger creates only it; the file holds framing and questions, no draft |
| Reads it back | Met | Write `events-turn-1.jsonl` line 42, Read line 47, result line 48: lines 1 to 23, totalLines 23 |
| Replies with its path, `Verified:` and `HVR self-scan:` | Met | `turn-1.md` lines 3, 4, 5 |
| No draft | Met | Line 1 "I haven't written the Story yet" |
| T2 saves one Story on the next number, read back | Met | `export/002 - Story-view-only-share-links.md`; Turn 2 ledger creates only it; read-back table |
| Names the Story kind, `HVR self-scan:` | Met | `turn-2.md` line 1 "as a Story"; line 5 |
| About, Problem, Solution, Expected outcomes, Requirements | Met | Lines 7, 13, 17, 21, 28 |
| Numbered Given/When/Then criteria, each closed by the Mark-as-done line | Met | Criteria 1 to 7 at lines 78, 88, 99, 108, 119, 128, 137; Mark-as-done at 86, 95, 105, 115, 126, 135, 143 |
| Closing `## Delivery` with Estimation, Rabbit holes, No-gos in order | Met | Line 147; lines 149, 155, 161; closed by a bare `* * *` at line 166 |
| `Anyone with the link can view` | Met | Line 32 |
| `Never`, `7 days`, `30 days` | Met | Line 35, with `Never` the default; line 46 `Never` only on Free |
| `60 seconds` | Met | Lines 37, 38, 51 |
| `3 active links` | Met | Line 49 carries it word for word inside the quoted copy "`Your workspace has 3 active links. ...`"; the Plans bullet at line 46 reads "up to `3` active links per workspace" |
| `Free`, `Plus`, `Team` | Met | Lines 46, 47, 48 |
| `noindex` | Met | Line 61 |
| `Duplicate` | Met | Lines 59 and 60 |
| `**Open:**` line carries `Do sub-pages inherit the link?` | Met | Line 66 "**Open:** `Do sub-pages inherit the link?`", word for word from notes line 46 (backticked there) |
| Names Lena as the one who settles it | Met | Line 66 "Lena, Product Manager, Sharing and Notifications, decides after talking it through with the security reviewer" |
| Rabbit holes repeat the question | Met | Line 159 "`Do sub-pages inherit the link?` is open until Lena decides with the security reviewer" |
| No criterion asserts how sub-pages behave | Met | Criteria 1 to 7 (lines 78 to 143) never mention sub-pages; criterion 6 (132) repeats notes line 37 "copies the page", not what else is copied |
| Fail: settles the sub-page question | Not hit | The Sub-pages group's one bullet, line 68 "The link opens the page it was turned on for, as the frames show", holds under either answer (notes line 54) |
| Fail: Estimation, a No-go or a date the sources never supply | Not hit | Lines 153 and 165 `TBD...`; no date in Delivery |
| Fail: plan limit, expiry option or delay changed; Guests can switch; ticket fields or story points | Not hit | Lines 35 to 51 against notes lines 12 to 30; line 41 "Guests never see the switch"; no header fields or points |

**Blocking items hit:** None.

**Advisory items**

- Size band 90 to 170: 166 lines. Inside the band
- Requirements adds a fourth group, `**Sub-pages**` (line 64), for the notes' `## Open question` section (notes line 44). The scenario's Expected signals ask for the Open line "under the requirement group it affects"; not a Pass clause
- Borderline, never decisive alone: line 39 adds "or has expired" to the trigger for `This link no longer works`, drawn from notes line 14 "An expired link counts as off". Criterion 5's "in a browser" (line 122) is named as an addition at `turn-2.md` line 19

**Read-back table**

| Turn | Export path | `N` printed | Read after the last write, lines returned | Real `wc -l` |
|---|---|---:|---|---:|
| 1 | `export/001 - Story-view-only-share-links-clarification.md` | 23 | Write line 42 (only write), Read line 47, result line 48: lines 1 to 23, totalLines 23 | 22 |
| 2 | `export/002 - Story-view-only-share-links.md` | 167 | Write line 38, Bash `sed -i` line 45, full Read line 50 (1 to 167), Bash `sed -i` line 55 (last write), Read line 57 (offset 160), result line 58: lines 160 to 167, totalLines 167 | 166 |

**Realism entries**

- `001 - Story-view-only-share-links-clarification.md`, Story-lane clarification. Question alone: present. Facts: Kofi's notes of 2026-09-15 (line 3 vs notes 3); "Pages are shared by invite only. There is no public link to a page" (7 vs `loomlist-context.md` 179); design yes, Caio no, Lena with the security reviewer, no date (9 vs notes 50 to 54); Dana, Theo, Mireille (15 vs context 40 to 42); de-DE, fr-FR, es-ES, ja-JP, pt-BR (19 vs context 155). Placeholder: none. 22 lines. Format gate: passed
- `002 - Story-view-only-share-links.md`, Story. Routed template `assets/story-template.md` lines 41 to 101 and Delivery close 127 to 145: preamble (4 and 5), About, Problem, Solution, Expected outcomes, Requirements, criteria and Delivery present; `#### **References**` rightly omitted, since no link was supplied (template line 66). Facts: H1 `Member - Sharing - View-only share links` follows the title pattern (1 vs context 112); frames `Share / View-only link`, `Share / Link settings`, `Shared page / Viewer` (11 vs notes 4); Lena, Product Manager, Sharing and Notifications (66 vs notes 54 and context 88); Caio, Backend Engineer, Sharing (159 vs notes 52); Free limit copy (49 vs notes 28). Placeholder: `TBD...` in Estimation and No-gos, exempt (root line 207). 166 lines, inside 90 to 170. Discipline code: not applicable to a Story (root line 212). Format gate: passed

**Open readings**

- The Turn 2 read-back after the last write was a partial Read, lines 160 to 167 of 167 (`events-turn-2.jsonl` line 57). Graded Met, as for SDK-001
- `N` 23 and 167 are the Reads' final line numbers; `wc -l` gives 22 and 166. Recorded only
- `3 active links`: the Plans bullet at line 46 backticks only the numeral, "`3` active links", and the unbroken phrase sits in the quoted copy at line 49. Graded Met because the words appear in Requirements in that order. Does the clause need the phrase in the limit bullet itself?

---

## PST-002 (project), Story forced delivery

**Draft row**

```csv
PST-002,project,claude-opus-5-5-medium,PASS,2,2,no,yes,"Turn 1 rendered one fenced Story question with its Story-lane clarification label and said only that the Story comes next (turn-1.md lines 1 to 25), and Turn 2 a fenced Story whose **Open:** line quotes Do sub-pages inherit the link? word for word and names Lena (line 56), repeated in Rabbit holes (148), with every Requirements value verbatim, no sub-page criterion, TBD... in Estimation and No-gos and no file claim. Borderline only: criterion 6 ""in the workspace they choose"" (line 129) against the notes' ""a workspace of theirs""."
```

**Against the latest earlier verdict (round one FAIL):** fixed. Round one's Open line read "Whether a link on a page also opens its sub-pages". This round's reads "**Open:** `Do sub-pages inherit the link?`" (line 56). Round one's borderline Turn 1 forecast of the Story's path is also gone: line 25 says only "The Story comes next, once you answer."

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question | Met | Block `turn-1.md` lines 2 to 16, one message |
| Rendered as its own block | Met | Fenced, reply lines 1 to 17, nothing before it |
| `Export-equivalent path:` in the Story lane | Met | Line 19 `export/NNN - Story-view-only-share-links-clarification.md` |
| `HVR self-scan:` | Met | Line 21 |
| No draft | Met | Line 25 "The Story comes next, once you answer." |
| T2 renders one Story block with its `Export-equivalent path:` | Met | Fenced, reply lines 1 to 159; line 161 `export/NNN - Story-view-only-share-links.md` |
| Names the Story kind, `HVR self-scan:` | Met | Line 165 "This is a Story."; line 163 |
| Claims no file | Met | No `Path:`, `Saved:`, `Verified:` and no promise or forecast of a file on either turn; `turn-1.md` line 12 "I'll add them under References" is about content |
| About, Problem, Solution, Expected outcomes, Requirements | Met | Lines 8, 12, 16, 20, 28 |
| Numbered Given/When/Then criteria, each closed by Mark-as-done | Met | Criteria 1 to 6 at lines 75, 84, 95, 104, 115, 125; Mark-as-done at 82, 91, 102, 111, 123, 132 |
| Closing `## Delivery` with Estimation, Rabbit holes, No-gos in order | Met | Line 136; 138, 144, 153; bare `* * *` at 158 |
| `Anyone with the link can view` | Met | Line 32 |
| `Never`, `7 days`, `30 days` | Met | Line 35, `Never` the default; line 45 `Never` only on Free |
| `60 seconds` | Met | Lines 37, 38, 51 |
| `3 active links` | Met | Line 49 inside the quoted copy; line 45 "up to `3` active links per workspace" |
| `Free`, `Plus`, `Team` | Met | Lines 45, 46, 47 |
| `noindex` | Met | Line 64 |
| `Duplicate` | Met | Lines 62 and 63 |
| `**Open:**` line carries `Do sub-pages inherit the link?` | Met | Line 56 "**Open:** `Do sub-pages inherit the link?`" |
| Names Lena as the one who settles it | Met | Line 56 "Lena, Product Manager, Sharing and Notifications, decides after talking it through with the security reviewer" |
| Rabbit holes repeat the question | Met | Line 148 "`Do sub-pages inherit the link?` is still undecided and will not be settled before the build starts" |
| No criterion asserts how sub-pages behave | Met | Criteria at lines 75 to 132 never mention sub-pages; criterion 6 line 129 says "a copy of the page", not what else it copies |
| Fail: settles the sub-page question, Estimation, No-go or date filled | Not hit | Lines 142 and 157 `TBD...`; line 56 "No date is set" (notes line 54) |
| Fail: plan limit, expiry or delay changed; Guests switch; header fields | Not hit | Lines 32 to 52 against notes 12 to 30; line 41 "Guests never see the switch" |

**Blocking items hit:** None.

**Advisory items**

- Size band 90 to 170: block 157 lines. Inside the band
- Commentary: none before either block
- Borderline, never decisive alone: criterion 6 "a signed-in viewer gets a copy of the page in the workspace they choose" (line 129) against notes line 37 "copies the page into a workspace of theirs", which adds a choice the notes do not state and the reply does not name; Rabbit holes line 149 "readers who hit a sign-in wall on a linked sub-page" against notes line 50 "followed a link inside a shared page". Criterion 3's "no new link goes live" and plan-matched expiry choices are named at line 181 and 182

**Realism entries**

- T1 block (reply lines 2 to 16), Story-lane clarification. Question alone: present. Facts: frames by name (12 vs notes 4); review on 2026-09-15 (16 vs notes 3); Lena with the security reviewer, no date (6 vs notes 54); plans Free, Plus and Team (4 vs notes 22 to 26). Placeholder: none. 15 lines. Format gate: passed
- T2 block (reply lines 2 to 158), Story. Routed template `Product Owner - Assets - Story Template - v0.100.md` Story scaffold and Delivery close: all present; References rightly omitted (template line 47). Facts: H1 `Member - Sharing - View-only links` (2 vs context 112); Lena's role (56 vs notes 54); Caio's view (150 vs notes 52); Team Admin note `Turned off by your workspace admin` (52 vs notes 30); invite-only today and agencies on Plus inviting guests (14 vs context 179 and Turn 2). Placeholder: `TBD...` exempt. 157 lines, inside 90 to 170. Format gate: passed

**Open readings**

- `3 active links`, same question as SST-002

---

## Rules under test: values kept this round

| Rule (values brief) | Value | Skill | Project |
|---|---|---|---|
| 2, Doc Templates primary body | `## Behavior rules` | Kept: SDK-001 T1 export line 29, final export line 29 | Kept: PDK-001 `turn-1.md` line 37, `turn-2.md` line 39 |
| 2, backticked phrase in the sentence that states its rule | `one discount code per order` | Kept, in the rule's sentence: export line 42 | Kept, in the rule's sentence: `turn-1.md` line 43, `turn-2.md` line 45 |
| 2 | `automatic promotions first` | Kept word for word, but in a sentence that quotes it, "The rule's own wording is `automatic promotions first`." (line 35), after the sentence that states the rule | Kept in the rule's sentence: `turn-1.md` line 48, `turn-2.md` line 50 |
| 2 | `exclusive`, `STAFF-`, `compare_at`, `applies_to_sale`, `50%` | Kept: lines 47, 57, 62, 62, 67 | Kept: `turn-2.md` lines 60, 70, 68, 68, 75 |
| 2 | `€50`, `£45`, `gift card` | Kept: lines 81, 81, 86 | Kept: `turn-2.md` lines 83, 83, 85 |
| 2 | `0.01`, `half up` | Kept: line 74 | Kept: `turn-2.md` line 90 |
| 2 | `2026-05-01` and the `retired` label | Kept: lines 143, 147 ("retired on 2026-05-01", not backticked) | Kept: `turn-2.md` lines 148, 150, 152 |
| 5, relaxed clause | today's v3 block-level last-writer-wins | Kept in the thread's words: SDK-003 `002` line 19 | Kept in the thread's words: PDK-003 `turn-2.md` line 20 |
| 4, root line 150 | `Conflicting edit from {device name}` (clause says verbatim) | Kept: `002` lines 59, 61 | Kept: `turn-2.md` line 53 |
| 4, root line 150 | `not decided` (thread line 66, plain text) | Kept word for word: `002` line 4 | Restated, not word for word: `turn-2.md` lines 6, 12, 87, 94. Met on the text reading, open reading under PDK-003 |
| 4, root line 150 | `lost-edit`, `0.8%`, `40`, `Joana`, `2026-10-09` | Kept: lines 12, 28, 12, 103, 103 | Kept: `turn-2.md` lines 14, 25, 14, 6, 6 |
| 3, Story Mode Open line | `Do sub-pages inherit the link?` quoted, then who settles it | Kept: SST-002 `002` line 66, Rabbit holes line 159 | Kept: PST-002 `turn-2.md` line 56, Rabbit holes line 148 |
| 4, root line 150 (clause says verbatim) | `Anyone with the link can view`, `Never`, `7 days`, `30 days`, `60 seconds`, `3 active links`, `Free`, `Plus`, `Team`, `noindex`, `Duplicate` | Kept: lines 32, 35, 35, 35, 37, 49 (46 as "`3` active links"), 46, 47, 48, 61, 59 | Kept: `turn-2.md` lines 32, 35, 35, 35, 37, 49 (45 as "`3` active links"), 45, 46, 47, 64, 62 |

Rule 1 (Task Mode) has no scenario in this batch.

---

## Twin notes

**SDK-001 and PDK-001: agree (PASS, PASS).** Both kept `## Behavior rules`, which the new sentence in skill `assets/doc-templates.md` line 116 and Project `Product Owner - Assets - Doc Templates - v0.108.md` line 95 now states in the same words, and both kept every backticked rule phrase under skill line 73 and Project line 52. One difference with no verdict effect: SDK-001 carries `automatic promotions first` in a follow-on sentence that quotes the rule's wording (export line 35), where PDK-001 puts it in the stating sentence (`turn-2.md` line 50). Both packagings say the phrase belongs "in the sentence that states that rule", so this is a small runtime drift under one shared rule, not a gap. Each revised its own Turn 1 doc its own way, skill in place and Project under the same label, and both are allowed.

**SDK-003 and PDK-003: agree (PASS, PASS), and they differ on one status value.** SDK-003 prints `not decided` in its notice (line 4); PDK-003 states the same status in other words (`turn-2.md` lines 6 and 12). Both packagings carry the same rules: "Explicit status markers travel with the claims they qualify" (skill `doc-mode.md` line 153, Project Doc Mode line 129) and the Proposal notice `> **Status: {Proposal or approved direction}**` (skill `doc-templates.md` line 486, Project Doc Templates line 465). If the operator reads the pinned status as a defined label, the split is a runtime fault on the Project side. They also differ on the Doc summary: PDK-003 prints the five lines (`turn-2.md` lines 128 to 132) and SDK-003 prints none, under the same rule on both sides (skill `doc-mode.md` line 412, kernel `Custom Instructions.md` line 217). That is a skill runtime fault, advisory. Both state today's v3 rule in the thread's words, so the relaxed clause at line 39 decides nothing this round.

**SST-002 and PST-002: agree (PASS, PASS).** Both Open lines now quote `Do sub-pages inherit the link?` and then name Lena, the exact shape the amended sentence asks for (skill `references/story-mode.md` line 80, Project `Product Owner - Templates - Story Mode - v0.404.md` line 57, same text), and both repeat it in Rabbit holes (skill line 341, Project line 317). They differ only in placement: the skill opens a fourth `**Sub-pages**` group (line 64), and the Project puts the Open line under `**What a viewer sees**` (line 54). The slot at skill line 327 and Project line 303 lets either stand, so neither is a gap. Both carry every Requirements value and wrap only the numeral in the Free limit bullet ("`3` active links"), with the whole phrase in the quoted copy.
