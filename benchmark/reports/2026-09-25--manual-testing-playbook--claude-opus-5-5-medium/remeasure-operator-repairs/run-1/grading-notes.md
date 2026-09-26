# Grading notes, remeasure round `remeasure-operator-repairs/run-1`

Evidence behind every verdict in this folder's `results.csv`. The round reran 26 scenarios on Product Owner `39bcd29` and Barter `df2de5f0` (skill 1.11.0, kernel v1.15.0, playbook 2.1.0.0), after the operator's rulings of 2026-09-25 were repaired in the sources. Source and root lines cite that commit.

Three Opus 5.5 graders drafted the evidence, and the orchestrator reviewed it as for the main run. Sections 2 to 4 are the graders' drafts, each row showing the first reading with `after_failed_gate` unset, and `results.csv` holds the final row.

The round's exports left `export/benchmark/` on 2026-09-26, so export lines cited here refer to the files at Product Owner `3fdce37` and Barter `d214c160`.

---

## 1. Review

**Result.** Skill 7 PASS and 4 FAIL, Project 3 PASS and 12 FAIL. `PID-001` fails, so the other 14 Project rows carry `after_failed_gate` yes.

**The ask-first repair worked on both sides.** Every scenario with an explicit command now asks one question in its lane on Turn 1, drafts on Turn 2 on the next number, and on the skill side leaves the clarification file untouched.

`TK-002` and `TK-004` on both sides, `SBG-002`, `SST-003`, `SST-004`, `SEP-001` and `PIR-002` pass where the main run failed them, and `SDK-003` passes again.

**The file-promise repair did not hold on the Project side.** Eight Project rows still name a path or file for the next artifact, several nearly copying the example kernel line 101 quoted in this round.

They are `PID-001` Turn 1 ("Once you answer, the task will be `export/002 - task-due-today-filter-chip.md`"), `PBG-002`, `PTK-005` Turn 2 ("I'll update the same file"), `PTK-006` Turn 2, `PST-003`, `PST-004`, `PEP-001` and `PEP-002`.

The dividing line applied in every batch: a forward statement that attaches an `export/` path or the word file to the next artifact is a claim. One that names only the next number is not, as in `PIR-002` and `PDK-003`. The operator chose one more repair and a second round of these eight (`remeasure-file-forecast/run-1`).

**Backticked values are graded word for word, as in the main run.** One draft passed `PDK-003` on "Protocol v3 applies last-writer-wins at the block level" (block line 19), where the Pass clause lists `block-level last-writer-wins`.

The orchestrator regraded it FAIL, as `STK-005` ("below 1 or above 99" for `1 to 99`), `PDK-001` ("One code per order" for `one discount code per order`) and `SST-002`/`PST-002` (the reworded `Do sub-pages inherit the link?`) are graded the same way. `SDK-003` states the value verbatim at export line 18.

**Still failing on content:**

- `TK-003` on both sides leaves out `HMAC-SHA256`, `5 attempts` and the retry schedule
- `SDK-001` names its rules section `## Stacking rules` instead of `## Behavior rules`
- `PTK-006` still never marks `checkout_complete` as `deprecated`

**Readings kept as the drafts recorded them:**

- A Read of a line range after the last write counts as read-back, since `AGENTS.md` line 46 asks for non-empty content
- A clarification saying the two sources agree covers the authority field in `SDK-003` and `PDK-003`, as borderline
- The card brand held as `**Open:**` in `SST-003` and `PST-003` is a surfaced conflict, not a silent one
- `facts_intact` stays `no` for the draft's value, as in the main run

---

## 2. Tasks batch, grader draft

Batch `remeasure-tasks`, nine scenarios from the remeasure round `remeasure-operator-repairs/run-1`: `STK-002..STK-005` with their twins `PTK-002..PTK-005`, plus `PTK-006` alone. Model `claude-opus-5-5-medium`. Graded read-only against `scratch/grading-brief.md` and `scratch/grading-brief-remeasure.md`.

### Conventions used in this draft

- `<R1>` is `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/remeasure-operator-repairs/run-1/`. Skill evidence sits under `<R1>/skill/<ID> - <slug>/`, Project evidence under `<R1>/claude project/<ID> - <slug>/`. Every `replies/<ID>-turn<n>.txt` is byte-identical to its `turn-<n>.md` (checked with `cmp`, all 18 the same).
- Sources are cited at Product Owner `39bcd29`. `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing, so the working tree was read directly. Root lines come from `git show 39bcd29:sk-product-owner/manual-testing-playbook/manual-testing-playbook.md` (version 2.1.0.0): verdict line 150, rendering line 163, identity handover line 179, invented fact line 187, protected fact line 188, file claim line 189, Ticket realism lines 198 to 214.
- `run-status.json`: all nine scenarios `status ok`, `turns_run 2`, `turns_declared 2`.
- "call N" is the Nth tool call in that turn's `events-turn-<n>.jsonl`, counted in stream order.
- Skill export line numbers are the file in `exports/export/`. Project line numbers are `turn-<n>.md` reply lines. Block copies for the format gate sit in `scratch/grades/blocks/remeasure-tasks/<ID>-turn<n>-block1.md` and hold the text between the fence lines, so a block copy's line is the reply line minus 1.
- Format gate: `node validate-output-format.cjs --system product-owner "<file>"` from the `AI Systems/z*Sync Loop` folder the brief names. All 8 skill export files and all 10 Project block copies printed `Product Owner output format validation passed across 1 artifact file(s)`, exit 0.
- Every Project conversation had only `read`, `ls`, `grep`, `find` (meta.json), and every Project turn ledger is empty. Every skill ledger shows exactly one new `export/` file per turn and nothing modified or deleted, so no `context/` file changed and no clarification file was touched on Turn 2.
- The Read tool shows an empty last line after a trailing newline, so a full Read's final line number is `wc -l` plus 1 on every export here.

### Shared open readings

- **RO-1, verbatim versus the same value in other words** (carried over from the main run's OR-3, not among the seven rulings). The remeasure brief leaves it open, so every such case is graded by the text as Unmet. It alone decides `STK-005`: the Pass clause lists `1 to 99` "as the parent gives them" (parent line 67 "with N from 1 to 99"), and export line 56 writes "the member cannot save an N below 1 or above 99". It also touches `PTK-006`, where `date_changed` is "still a proposal" (turn-2.md line 10) and never `proposed`. Question: does a hard value or status restated with the same meaning in other words count as verbatim?
- **RO-2, what a Project promise has to say to be a file claim.** Ruling 3 (root line 189, kernel line 101) makes a promise to write or save a file a file claim, and the main-run regrade recorded `PBG-003` "the bug report will take the next number in the bug lane" as borderline because it names no file. Graded here as follows. File claim: `PTK-005` turn-2.md line 166 "Answer any of these and I'll update the same file." (decides `PTK-005`) and `PTK-006` turn-2.md line 96 "If you settle either point, I'll update the task under the same filename." (does not decide `PTK-006` alone). Borderline, recorded only: `PTK-003` turn-1.md line 45 "Once you answer, the task will be `export/002 - task-...`" (names a path but promises no write or save), and three sentences that name no file, `PTK-002` turn-1.md line 39, `PTK-005` turn-1.md line 34 and `PTK-006` turn-1.md line 39. Question: is "update the same file" or "update the task under the same filename" a promise to write a file, and is "the task will be `export/002 - ...`" one?
- **RO-3, a read-back that covers only part of the file.** `STK-002` Turn 2 and `STK-005` Turns 1 and 2 changed the export after their last full Read and then read back only a slice (lines 170-179, 5-17 and 120-129). `AGENTS.md` line 46 and `SKILL.md` line 211 require a Read that "returns non-empty content at that path", which a slice meets, so these are graded as proof. Question: must the read-back after the last change cover the whole file?
- **RO-4, which count is `N`** (the main run's OR-2). `AGENTS.md` line 46 sets `N` to "the final line number returned by Read". Most replies printed the full Read's final line (`wc -l` plus 1). `STK-002` Turn 2 printed 178, `wc -l`, where its last Read ended on line 179. No Pass clause here makes the count a condition, so nothing rests on it.
- **RO-5, a Turn 2 fact carried by structure or by the context's own name.** "No parent" (TK-002, TK-003) is carried by the absence of a `**Parent task**` block, as the main run read it. `STK-005` writes "The Mobile Platform team" where Turn 2 says "Oskar's team" (`loomlist-context.md` line 89 names Oskar as that team's lead). `PTK-006` does not name Nadia as the checker and never states that refinement left the event table unchanged, though it builds from `draft v0.3` as written. All graded Met or Met, borderline. Question: must such a fact be stated in words?
- **RO-6, where "it goes on the Fulfilment board" must live.** Both TK-003 runtimes keep the board out of the task and name it only in the reply (the same reading the main run applied to `PTK-003`). Graded Unmet in both, and it decides neither verdict alone.

---

### STK-002 | Design notes FE task (skill)

**Draft row**

```csv
STK-002,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 saved only export/001 - task-date-picker-stay-limits-clarification.md (call 7, read back by call 8) and drafted no task, and Turn 2 saved export/002 - task-date-picker-stay-limits.md on the next number with every limit, the five copy strings and every Turn 2 fact (export lines 9, 37-42, 54-56, 72-74, 87-88, 172). Advisory: 178 lines against the 70 to 150 band, and the last Read after the final rewrite covered lines 170-179 only (RO-3)."
```

**Against the main run:** fixed. The main run failed because Turn 1 drafted the task with no question and Turn 2 edited 001 in place.

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Met | one consolidated five-part question, clarification lines 1-13, shaped like the Task Format question (`assets/interactive-response-templates.md` line 90) |
| Saved under a `task` lane `-clarification` name | Met | T1 ledger creates only `export/001 - task-date-picker-stay-limits-clarification.md` |
| Reported with its path, `Verified:` and `HVR self-scan:` | Met | turn-1.md lines 3, 4, 5 |
| Turn 1 drafts no task | Met | T1 ledger, clarification holds questions only (a proposed title at line 5 is a question, not a draft) |
| Turn 2 saves one `task` export on the next number | Met | T2 ledger creates only `export/002 - task-date-picker-stay-limits.md` |
| Read back and reported the same way | Met | call 8 Read after the last change (lines 170-179, RO-3), turn-2.md lines 3, 4, 5 |
| H1, `### About`, `### Requirements` | Met | export lines 1, 3, 21 |
| Checklisted requirement groups | Met | nine numbered groups, each with `**Checklist**` (lines 35, 52, 70, 85, 115, 132, 145, 159, 174) |
| Stay limits as the notes give them | Met | `30 nights` line 38, `365 days` line 39, check-out past it line 41, `14 nights` line 42 (property page only), from config and never hard-coded lines 54-56 |
| Five copy strings exact | Met | `Select check-in date` line 72, `Select check-out date` line 73, `Show prices` line 74, `Stays can be up to 30 nights` line 87, `This property has a 3-night minimum` line 88 |
| Every Turn 2 fact | Met | line 9: one task for iOS, Android and web, Search squad, 8.13.0 train, search-service unchanged with its 30-night backstop; line 172 and 176-177: QA on all three platforms in `en-GB` and `en-US`; no parent block (RO-5) |
| No FAIL example hit | Met | no hard-coding (line 56), 365 on check-in only (line 41), no tracking, search-service change or flexible dates (line 11 excludes them), frame plain text with no link (line 19), no unfilled slot (the `{max}`, `{n}`, `{count}` in the key table lines 111-113 are quoted from notes lines 39-41) |

**Blocking items hit**

None.

**Advisory items**

- Size band: 178 lines against 70 to 150.
- Named additions at turn-2.md lines 16-18 (the "35 nights later" user story at lines 94-96, the final QA item at line 178). Borderline, not named: line 118 says `{max}` and `{n}` are filled from the limit values, which follows from notes lines 43 and 61.
- About line 7 narrows the notes' "lets a guest select any range" to "a range longer than 30 nights". The reply says why (turn-2.md line 12): the minimum-stay conflict between `roamstay-context.md` line 142 and the notes is left open, not resolved. No protected value changes.
- Asking for a fact an attachment states: none found. The questions (links, the minimum-stay conflict, whether the apps receive the values) are not answered by the notes.

**Read-back table**

| Turn | Export path | `N` printed | Read after the last change, lines returned | `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - task-date-picker-stay-limits-clarification.md` | 14 (turn-1.md line 4) | Write call 7, Read call 8, lines 1-14 | 13 |
| 2 | `export/002 - task-date-picker-stay-limits.md` | 178 (turn-2.md line 4) | Write call 2, Edit call 4, Bash python rewrites at calls 5 and 7 (call 3's heredoc failed and changed nothing). Full Read call 6 (lines 1-185) came before the call 7 rewrite. Last Read call 8 (offset 170), lines 170-179 | 178 |

**Realism entries**

- `export/001 - task-date-picker-stay-limits-clarification.md`, task-lane clarification (`SKILL.md` line 208). Question only. Facts: the picker applying the minimum on the property page (line 7) matches `roamstay-context.md` line 142; `PROP` against `SRCH` (line 7) matches context lines 91-92; the notes' date 2026-09-14 (line 13) matches notes line 4; the two-month desktop layout (line 5) matches notes line 56. Placeholders none. 13 lines, no band.
- `export/002 - task-date-picker-stay-limits.md`, Canonical Task (`assets/task-templates.md` line 38). Title, About, Requirements present. Facts: 23 chats in August (line 7) match notes line 11; Partner Hub minimum from 1 to 14 nights (line 42) matches notes line 19; Hana's sign-off on 2026-09-11 (line 104) matches notes line 5; the saved 45-night search (line 130) matches notes line 49; Monday week start except `en-US` (line 164) matches notes line 57 and context line 132. Placeholders: `{max}`, `{n}`, `{count}` quoted from notes lines 39-41 (exempt). 178 lines against 70 to 150. Code `FE`.

**Open readings**

- RO-3 (last Read covered lines 170-179), RO-4 (`N` 178 against the Read's final line 179), RO-5 (no parent).

---

### PTK-002 | Design notes FE task (Project)

**Draft row**

```csv
PTK-002,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 rendered one fenced question block labelled export/001 - task-date-picker-stay-limits-clarification.md with no task, and Turn 2 one fenced task block labelled export/002 - task-date-picker-stay-limits.md with every limit, the five copy strings and every Turn 2 fact (turn-2.md lines 12, 38-43, 49, 69-71, 82-83, 150-152) and no file claim. Advisory: 151 block lines against the 70 to 150 band. Borderline: turn-1.md line 39 says the task ""will be delivered under the next number in the task lane"", naming no file (RO-2)."
```

**Against the main run:** fixed. The main run failed because Turn 1 rendered the full task with no question.

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question rendered as its own block | Met | fenced block turn-1.md lines 1-22, one consolidated question in five labelled parts |
| Export-equivalent `task` lane `-clarification` label and `HVR self-scan:` | Met | line 24 `export/001 - task-date-picker-stay-limits-clarification.md`, line 26 |
| Turn 1 renders no task | Met | block holds questions only |
| Turn 2 renders one task block under an export-equivalent `task` label with `HVR self-scan:` | Met | fenced block turn-2.md lines 1-153, line 155 `export/002 - task-date-picker-stay-limits.md`, line 157 |
| No file claim, no `Path:`, `Saved:` or `Verified:` | Met | none on either turn. turn-1.md line 39 names no file (borderline, RO-2) |
| H1, `### About`, `### Requirements` | Met | lines 2, 4, 22 |
| Checklisted requirement groups | Met | eight numbered groups, each with `**Checklist**` |
| Stay limits as the notes give them | Met | `30 nights` line 39, `365 days` line 40, check-out past it line 41, config and no hard-coding line 43, `14 nights` line 49 (property page only), minimum from property details line 54 |
| Five copy strings exact | Met | lines 69, 70, 71, 82, 83 |
| Every Turn 2 fact | Met | line 12: one task for iOS, Android and web, Search squad, 8.13.0 train, search-service unchanged with its backstop; lines 150-152: QA in `en-GB` and `en-US` on all three, backstop still rejects; no parent section (RO-5) |
| No FAIL example hit | Met | no tracking, search-service change or flexible dates (line 12), frame as plain text (line 20), no unfilled slot (`{max}`, `{n}`, `{count}` lines 131-133 quoted from notes lines 39-41) |

**Blocking items hit**

None.

**Advisory items**

- Size band: 151 block lines against 70 to 150.
- Named addition: line 55 "The picker in the search form applies only the 1-night minimum", named at turn-2.md line 163.
- Block form: fenced on both turns, block first, no commentary before it.
- Borderline promise: turn-1.md line 39 "Once you answer, the task will be delivered under the next number in the task lane." Names no file, as `PBG-003` in the main-run regrade (RO-2).

**Realism entries**

- Block `PTK-002-turn1-block1.md` (reply lines 2-21), task-lane clarification (`Custom Instructions.md` line 228). Question only. Facts: "Guest app" with no platform means all three (line 5) matches `roamstay-context.md` line 17; `PROP` for the property page (line 6) matches context line 92; limits from search-service config (line 15) match notes line 61; seven locales (line 20) match context lines 124-130. Placeholders none. 20 lines, no band.
- Block `PTK-002-turn2-block1.md` (reply lines 2-152), Canonical Task (`Product Owner - Assets - Task Templates` line 19). Title, About, Requirements present. Facts: 23 chats in August (line 8) match notes line 11; 1 to 14 nights set in Partner Hub (line 49) match notes line 19; Hana's sign-off on 2026-09-11 (line 124) matches notes line 5; the saved 45-night search (line 102) matches notes line 49. Placeholders exempt as above. 151 lines against 70 to 150. Code `FE`.

**Open readings**

- RO-2 (turn-1.md line 39), RO-5 (no parent).

---

### STK-003 | Long BE integration task (skill)

**Draft row**

```csv
STK-003,skill,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 now asks and saves only the clarification, but the Turn 2 task export/002 - task-label-webhook-fix.md carries none of `HMAC-SHA256`, `5 attempts` or `1 min, 5 min, 15 min, 1 h, 6 h` (line 38 names only the header, lines 9 and 53 only the last retry) and drops the Turn 2 fact that it goes on the Fulfilment board, which appears only in the reply's ClickUp offer (turn-2.md line 22)."
```

**Against the main run:** still failing for the same cause, with the Turn 1 and read-back misses fixed. The main run restated `5 attempts` and the schedule. Here both are absent, `HMAC-SHA256` is newly missing, and the Fulfilment board is a new miss.

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Met | one seven-part question, clarification lines 1-17 |
| Saved under a `task` lane `-clarification` name with path, `Verified:` and `HVR self-scan:` | Met | T1 ledger `export/001 - task-label-webhook-fix-clarification.md`, turn-1.md lines 1, 2, 3 |
| Turn 1 drafts no task | Met | T1 ledger, question only |
| Turn 2 saves one `task` export on the next number, read back and reported the same way | Met | T2 ledger `export/002 - task-label-webhook-fix.md`, Read call 4 after the last change, turn-2.md lines 3-5 |
| H1, `### About`, `### Requirements` | Met | lines 1, 3, 22 |
| A checklisted group for each of the five points | Met | fast answer and queue line 30, `event_id` line 44, open-shipment guard line 59, 10-minute GET line 71, alerting line 88, each with `**Checklist**` |
| Carrier values verbatim | Unmet | `event_id` lines 48, 52-53, `X-Carrier-Signature` line 38, `5 seconds` lines 9, 30, 39. `HMAC-SHA256` absent (line 38 checks the header "against the raw request body" without naming it, API notes line 53). `5 attempts` and `1 min, 5 min, 15 min, 1 h, 6 h` absent (API notes line 58): line 9 has only "Their fifth and last retry comes 6 hours after the fourth" and line 53 "the carrier's last retry at 7 hours 21 minutes" |
| Thread values verbatim | Met | `7 days` line 53, `10 minutes` line 79, `30 minutes` and `#fulfilment-alerts` line 96, `more than 5` line 97 |
| Polling only kept out | Met | line 13, with the thread's rate-limit reason |
| Every Turn 2 fact | Unmet | present: no parent (no parent block), live before the November peak line 11, staging replay line 111, late `label.created` changes nothing lines 81 and 112, 8-second timeout kept and moved out lines 40-41. Absent: "it goes on the Fulfilment board", found only in turn-2.md line 22 "I can also create it on the Fulfilment board in ClickUp" (RO-6) |
| No FAIL example hit | Met | no carrier idempotency key or `reference` dedupe (line 63 states both absent), no changed retry, window or threshold, no polling, the `SERVICE_UNAVAILABLE` question left open (line 69), no unnamed queue, store or vendor, no slot (`{shipment_id}` lines 75 and 79 is the API path from notes line 14) |

**Blocking items hit**

- Pass clause missed, carrier values not verbatim, root line 150. Two of them are dropped outright, not restated, so this stands under either reading of RO-1.
- Pass clause missed, a Turn 2 fact dropped (the Fulfilment board), root line 150 (RO-6).

**Advisory items**

- Named additions at turn-2.md lines 10-15 (stored event survives a timeout line 42, `2xx` for a repeat line 52, wider guard and open states lines 67-68, copy into storage line 80, `429` back-off line 82, the carrier answer recorded before release line 69).
- Borderline: About line 9 "that afternoon the calls took 6 to 9 seconds" and line 111 "warehouse system calls taking 6 to 9 seconds" put on the warehouse calls the 6 to 9 seconds the thread gives the handler per event (thread line 21).
- Size band: 112 lines, inside 110 to 220.

**Read-back table**

| Turn | Export path | `N` printed | Read after the last change, lines returned | `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - task-label-webhook-fix-clarification.md` | 18 (turn-1.md line 2) | Write call 10, Read call 11, lines 1-18 | 17 |
| 2 | `export/002 - task-label-webhook-fix.md` | 113 (turn-2.md line 4) | Write call 2, Bash perl edit call 3, Read call 4, lines 1-113 | 112 |

**Realism entries**

- `export/001 - task-label-webhook-fix-clarification.md`, task-lane clarification. Question only. Facts: Noor's export "to attach to the label webhook ticket" (line 5) matches thread line 3; point 3 against the summary wording (line 7) matches thread lines 35 and 61; `label_pending` and `label_ready` (line 7) match API notes line 14; the shared 20 requests per second and `Retry-After` (line 11) match API notes line 68. Placeholders none. 17 lines, no band.
- `export/002 - task-label-webhook-fix.md`, Canonical Task. Title, About, Requirements present. Facts: `37 duplicate labels` between 14:10 and 15:50 (line 7) match thread line 9; `€0.42` (line 7) matches thread line 17; 12 orders, the 15:00 cut-off and the 18:00 collection (line 7) match thread line 13 and `fernhouse-context.md` lines 47-48; the 8-second timeout and the `500` (line 9) match thread line 27; POSTs at 14 a second (line 13) match thread line 45. Missing: `HMAC-SHA256` (API notes line 53), `5 attempts` and the schedule (API notes line 58). Placeholders none. 112 lines, inside 110 to 220. Code `BE - SHIP`, matching context lines 93 and 104.

**Open readings**

- RO-6 (Fulfilment board). RO-1 does not apply to the missing values, since they are absent rather than restated.

---

### PTK-003 | Long BE integration task (Project)

**Draft row**

```csv
PTK-003,project,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 now renders one question block, but the Turn 2 block carries none of `HMAC-SHA256`, `5 attempts` or `1 min, 5 min, 15 min, 1 h, 6 h` (turn-2.md line 33 names only the header, line 50 only the 7 hours 21 minutes) and leaves the Fulfilment board out of the task, naming it only in the next-step line 127. Borderline: turn-1.md line 45 says ""the task will be `export/002 - task-...`"" (RO-2)."
```

**Against the main run:** still failing for the same cause (`5 attempts`, the schedule and the Fulfilment board), with the Turn 1 draft fixed. `HMAC-SHA256`, present in the main run, is newly missing.

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question rendered as its own block | Met | fenced block turn-1.md lines 1-30 |
| Export-equivalent `task` lane `-clarification` label and `HVR self-scan:` | Met | line 32 `export/001 - task-carrier-label-webhook-fix-clarification.md`, line 34 |
| Turn 1 renders no task | Met | questions only |
| Turn 2 renders one task block under an export-equivalent `task` label with `HVR self-scan:` | Met | fenced block turn-2.md lines 1-106, line 108 `export/002 - task-carrier-label-webhook-fix.md`, line 110 |
| No file claim, no `Path:`, `Saved:` or `Verified:` | Met | no save, write or read-back claim. turn-1.md line 45 "the task will be `export/002 - task-...`" is recorded as borderline (RO-2). turn-2.md line 127 tells the human to save it to the board |
| H1, `### About`, `### Requirements` | Met | lines 2, 4, 21 |
| A checklisted group for each of the five points | Met | groups at lines 25, 41, 54, 69, 83, each with `**Checklist**` |
| Carrier values verbatim | Unmet | `event_id` lines 45, 49-50, `X-Carrier-Signature` line 33, `5 seconds` line 34. `HMAC-SHA256`, `5 attempts` and `1 min, 5 min, 15 min, 1 h, 6 h` absent (API notes lines 53 and 58). Line 50 has only "the carrier's last retry at 7 hours 21 minutes" |
| Thread values verbatim | Met | `7 days` line 50, `10 minutes` line 77, `30 minutes` and `#fulfilment-alerts` line 91, `more than 5` line 92 |
| Polling only kept out | Met | line 12 |
| Every Turn 2 fact | Unmet | present: no parent (no parent section), November peak line 10, staging replay line 104, late `label.created` line 105, 8-second timeout line 36. Absent from the block: the Fulfilment board, named only at turn-2.md line 127 (RO-6) |
| No FAIL example hit | Met | no carrier key or `reference` dedupe (line 58), the open carrier question left open (line 65), no polling, no unnamed product, no slot |

**Blocking items hit**

- Pass clause missed, carrier values not verbatim (absent), root line 150.
- Pass clause missed, a Turn 2 fact dropped (the Fulfilment board), root line 150 (RO-6).

**Advisory items**

- Named additions at turn-2.md lines 115-117 (queue retry line 37, `label_failed` not open line 63, rate limit on the GETs line 79). Borderline, not named: line 78 stores a GET label "as it would for a `label.created` event", which follows from API notes line 64 and thread line 36.
- Borderline: line 104 "the warehouse system taking 6 to 9 seconds per call", the same shift as `STK-003` line 111 (thread line 21).
- Size band: 104 block lines against 110 to 220.
- Borderline promise at turn-1.md line 45 (RO-2).

**Realism entries**

- Block `PTK-003-turn1-block1.md` (reply lines 2-29), task-lane clarification. Question only. Facts: the `BE - SHIP` title with no surface (line 7) matches `fernhouse-context.md` line 93; Noor's export "to attach to the label webhook ticket" (line 8) matches thread line 3; POSTs at up to 14 a second (line 16) match thread line 45; "usually within a minute" (line 25) matches context line 143. Placeholders none. 28 lines, no band.
- Block `PTK-003-turn2-block1.md` (reply lines 2-105), Canonical Task. Title, About, Requirements present. Facts: `€0.42` (line 8) matches thread line 17; `FH-2291834-1` (line 62) matches API notes line 16; 7 hours 21 minutes (line 50) matches API notes line 59; the 18:00 collection (line 8) matches thread line 13. Missing: `HMAC-SHA256`, `5 attempts`, the schedule. Placeholders: `{shipment_id}` (line 77) is the API path from notes line 14. 104 lines against 110 to 220. Code `BE - SHIP`.

**Open readings**

- RO-2 (turn-1.md line 45), RO-6.

---

### STK-004 | Parent task with subtasks (skill)

**Draft row**

```csv
STK-004,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 saved only the question file 001, and Turn 2 saved one parent task, export/002 - task-recurring-todos-parent.md, and no subtask files (T2 ledger), exactly as the Pass clause asks, with the four subtasks as backticked titles (lines 39, 47, 55, 63), every shared-rule value (lines 80-185) and every Turn 2 fact. Advisory: 195 lines against the 60 to 130 band."
```

**Against the main run:** fixed. The main run failed because Turn 1 saved a parent and four subtask files with no question and Turn 2 rewrote 001 in place.

**On the parent and its subtasks.** The export folder holds only `001 - task-recurring-todos-clarification.md` and `002 - task-recurring-todos-parent.md`. That is what the scenario asks: Turn 2 "saves one parent task ... and no subtask files" (scenario line 36), and the Fail clause names "Turn 2 saves subtask files as well" (line 39). The four subtasks are delivered as numbered entries named in plain text inside the parent, as the Parent Task template's Requirements list (`assets/task-templates.md` lines 188-208) and the named-but-unlinked rule (`references/task-mode.md` line 133) ask.

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Met | one seven-part question, clarification lines 1-17 |
| Saved under a `task` lane `-clarification` name with path, `Verified:` and `HVR self-scan:` | Met | T1 ledger `export/001 - task-recurring-todos-clarification.md`, turn-1.md lines 3, 4, 5 |
| Turn 1 drafts no task | Met | T1 ledger, questions only |
| Turn 2 saves one parent `task` export on the next number, read back and reported the same way | Met | T2 ledger creates only `export/002 - task-recurring-todos-parent.md`, Read call 6 after the last change, turn-2.md lines 3-5 |
| H1, `### About`, `### Requirements` | Met | lines 1, 3, 27 |
| One numbered entry each for iOS, Android, web and back end, in plain text | Met | `FE - iOS - TODO - Recurring to-dos` line 39, `FE - Android - TODO - Recurring to-dos` line 47, `FE - Web - TODO - Recurring to-dos` line 55, `BE - TODO - Recurring to-dos` line 63, no links |
| Shared-rule values as the brief gives them | Met | `Daily`, `Weekdays`, `Weekly`, `Monthly`, `Custom` lines 94-98, `1 to 99` lines 98 and 105, `Never`, `On date`, `After` line 116, `365` line 118, `Skip this one` lines 125 and 132-133, `500` lines 140 and 144, `recurring_todos` lines 177 and 183, `Plus` lines 75 and 81-82, the `owner's time zone` lines 152 and 156 |
| Every Turn 2 fact | Met | only the parent, leads write the subtasks, rules stated once (line 9); board-style titles (lines 39-63); iOS and Android on 5.4.0 (lines 41, 49); web and BE dark first (lines 57, 65, 184) |
| No FAIL example hit | Met | no subtask files, no Desktop or Support console subtask (Desktop gets none, line 57, Support console out of scope, line 194), no link or `(url)` slot, Repeat not on Free (line 82 upgrade sheet), limit and sheet copy exact (line 144), no check-off-date repeat or per-weekday time (lines 192-193 out of scope), activity history left open (line 195) |

**Blocking items hit**

None.

**Advisory items**

- Size band: 195 lines against 60 to 130.
- Named at turn-2.md lines 18-23: the open mobile upgrade-sheet decision (line 84), the frames as not yet signed off (line 21), the Desktop note from the context page (line 57), the Monthly short-month reason (line 100). Line 152's owner definition and line 170's event properties come from `loomlist-context.md` lines 55 and 187.
- The clarification's proposed title patterns carry `{title}` (line 5). It is a question describing a pattern, not an artifact body, so it is recorded only.

**Read-back table**

| Turn | Export path | `N` printed | Read after the last change, lines returned | `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - task-recurring-todos-clarification.md` | 18 (turn-1.md line 4) | Write call 8, Bash sed call 9, Read call 10, lines 1-18 | 17 |
| 2 | `export/002 - task-recurring-todos-parent.md` | 196 (turn-2.md line 4) | Write call 3, Bash sed calls 4 and 5, Read call 6, lines 1-196 | 195 |

**Realism entries**

- `export/001 - task-recurring-todos-clarification.md`, task-lane clarification. Question only. Facts: `TODO` against `REM` (line 5) matches `loomlist-context.md` lines 120-121; Yara's review of the two events (line 7) matches brief line 62; Web as the only billing surface (line 9) matches context line 13; the three frames (line 11) match brief line 58; 10% at 8 weeks (line 13) matches brief line 47. Placeholders: `{title}` in a proposed pattern (advisory). 17 lines, no band.
- `export/002 - task-recurring-todos-parent.md`, Parent Task (`assets/task-templates.md` line 165). Title, About, Requirements present. Facts: 212 requests and 38 Plus workspaces (line 7) match brief line 8; the to-do owner definition (line 152) matches context line 55; the five event properties (line 170) match context line 187; Desktop with no release (line 57) matches context line 18. Placeholders none. 195 lines against 60 to 130. Code `FS`.

**Open readings**

None that touch the verdict.

---

### PTK-004 | Parent task with subtasks (Project)

**Draft row**

```csv
PTK-004,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 rendered one question block labelled export/001 - task-recurring-todos-clarification.md, and Turn 2 one parent block and no subtask blocks, listing the four subtasks as plain-text bullets (turn-2.md lines 36, 46, 56, 66) with every shared-rule value and Turn 2 fact and no file claim. Advisory: 209 block lines against the 60 to 130 band."
```

**Against the main run:** fixed. The main run failed because Turn 1 rendered a parent and four subtask blocks with no question.

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question rendered as its own block | Met | fenced block turn-1.md lines 1-35 |
| Export-equivalent `task` lane `-clarification` label and `HVR self-scan:` | Met | line 37 `export/001 - task-recurring-todos-clarification.md`, line 39 |
| Turn 1 renders no task | Met | questions only |
| Turn 2 renders one parent block under an export-equivalent `task` label with `HVR self-scan:` | Met | one fenced block (four-backtick fence) turn-2.md lines 1-211, line 213 `export/002 - task-recurring-todos.md`, line 215 |
| No file claim, no `Path:`, `Saved:` or `Verified:`, and no subtask blocks | Met | one block only. turn-1.md line 51 promises blocks, not files |
| H1, `### About`, `### Requirements` | Met | lines 2, 4, 24 |
| One numbered entry each for iOS, Android, web and back end, in plain text | Met | lines 32/36, 42/46, 52/56, 62/66 |
| Shared-rule values as the brief gives them | Met | option names lines 84-88 and 94, `1 to 99` lines 88 and 95, `Never`, `On date`, `After` line 109, `365` line 111, `Skip this one` lines 126-127, `500` lines 139-141, `recurring_todos` lines 12 and 169, `Plus` lines 167-168, the `owner's time zone` lines 153-154 |
| Every Turn 2 fact | Met | only the parent, leads write their own subtasks, rules stated once (line 10); iOS and Android on 5.4.0, web and BE dark first (lines 12, 170-171) |
| No FAIL example hit | Met | no Desktop or Support console subtask (lines 58, 197), no link or slot, Repeat not on Free (line 168), limit and copy exact (line 140), exclusions kept (lines 194-197), activity history left open (line 203) |

**Blocking items hit**

None.

**Advisory items**

- Size band: 209 block lines against 60 to 130.
- Named at turn-2.md lines 222-225: seven of the eight open questions (lines 204-210), line 112's "No next occurrence appears once the series has ended" and the reason under rule 5. None enters a checklist.
- Block form: fenced on both turns, block first.

**Realism entries**

- Block `PTK-004-turn1-block1.md` (reply lines 2-34), task-lane clarification. Question only. Facts: the four subtask titles (line 7) follow `loomlist-context.md` line 104; `REM` (line 8) matches context line 121; tracking plans under `DATA` (line 17) match context line 101; Desktop through the web client (line 14) matches brief line 55. Placeholders none. 33 lines, no band.
- Block `PTK-004-turn2-block1.md` (reply lines 2-210), Parent Task (`Product Owner - Assets - Task Templates` line 146). Title, About, Requirements present. Facts: 212 requests and 38 Plus workspaces (line 8) match brief line 8; to-do owner, not the Owner role (line 149) matches context line 55; Yara's review before client work (lines 180, 184) matches brief line 62 and context line 191; no Desktop release (line 58) matches context line 18. Placeholders none. 209 lines against 60 to 130. Code `FS`.

**Open readings**

None that touch the verdict.

---

### STK-005 | Supplied parent subtask (skill)

**Draft row**

```csv
STK-005,skill,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Both turns now follow the chain, and the subtask names its parent at line 27, keeps Android-only scope and every Turn 2 fact, but the Pass clause value `1 to 99` is restated as ""the member cannot save an N below 1 or above 99"" (line 56). Graded by the text as Unmet under RO-1, which alone decides this verdict."
```

**Against the main run:** failing for a new cause. The main run failed because Turn 1 drafted the subtask and Turn 2 edited 001 in place. Both are fixed. The new miss is `1 to 99` not verbatim, which the main-run export had at line 67.

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Met | one eight-part question, clarification lines 1-17 |
| Saved under a `task` lane `-clarification` name with path, `Verified:` and `HVR self-scan:` | Met | T1 ledger `export/001 - task-android-recurring-todos-clarification.md`, turn-1.md lines 3, 4, 5 |
| Turn 1 drafts no task | Met | T1 ledger, questions only |
| Turn 2 saves one `task` export on the next number, read back and reported the same way | Met | T2 ledger `export/002 - task-android-recurring-todos.md`, Read call 7 after the last change (lines 120-129, RO-3), turn-2.md lines 3-5 |
| H1, `### About`, `### Requirements` | Met | lines 1, 3, 37 |
| Checklisted requirement groups | Met | five numbered groups under area headings, each with `**Checklist**` |
| Parent named as `FS - TODO - Recurring to-dos` | Met | `**Parent task**` block line 27, backticked, no link |
| Shared-rule values as the parent gives them | Unmet | present: option names line 55, `Never`, `On date`, `After` line 57, `365` line 58, `Skip this one` lines 92-93, `500` lines 67 and 73-74, `recurring_todos` lines 11 and 71, the `owner's time zone` lines 104 and 108. Not verbatim: `1 to 99`, line 56 reads "the member cannot save an N below 1 or above 99" against parent line 67 "with N from 1 to 99" (RO-1) |
| Android as the only client in scope | Met | every checklist item is Android. iOS, Web and Desktop appear only in line 9's reason and the related-task list lines 34-35 |
| Every Turn 2 fact | Met, borderline | the Android entry (title line 1), phones and tablets (lines 7, 53), Oskar's team written as "The Mobile Platform team" (line 7, RO-5), 5.4.0 (line 7), the next due date from BE and never on the device (lines 9, 59, 90-91, 93) |
| No FAIL example hit | Met | parent kept with no URL, no iOS, web, Desktop or engine work, no device date math, no changed option, range, limit, copy or plan rule, no unnamed widget or notification action, no slot |

**Blocking items hit**

- Pass clause missed, `1 to 99` not verbatim, root line 150, read under RO-1. The range itself is unchanged, so no protected fact is altered (root line 188) and `facts_intact` is `yes`.

**Advisory items**

- Named additions at turn-2.md lines 10-14 (flag off shows nothing line 71, no device-made date before the engine answers line 91, ended series line 96, the five standard properties with `user_id` hashed line 128).
- Borderline, not named: lines 55-56 and 92 tie each frame to a control ("matching `Recurring to-dos / Repeat picker`"), and line 67 says the Free and limit sheets tell members "why they cannot use it", where parent line 103 says only "opens the upgrade sheet". Neither decides anything.
- Size band: 128 lines, inside 60 to 130.

**Read-back table**

| Turn | Export path | `N` printed | Read after the last change, lines returned | `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - task-android-recurring-todos-clarification.md` | 17 (turn-1.md line 4) | Write call 8, Read call 9 (lines 1-18), Edit call 10, Read call 11 (offset 5, limit 13), lines 5-17 | 17 |
| 2 | `export/002 - task-android-recurring-todos.md` | 129 (turn-2.md line 4) | Write call 3, Read call 4 (lines 1-129), Bash perl edits calls 5 and 6, Read call 7 (offset 120), lines 120-129 | 128 |

**Realism entries**

- `export/001 - task-android-recurring-todos-clarification.md`, task-lane clarification. Question only. Facts: Web as the only billing surface (line 5) matches `loomlist-context.md` line 13; no offline mode and unsynced edits lost on close (line 7) match context lines 175-176; Android local notifications (line 9) match context line 77; Android 5.3.0 current (line 15) matches context line 133; `BE - TODO - Recurrence engine` (line 15) matches parent line 49. Placeholders none. 17 lines, no band.
- `export/002 - task-android-recurring-todos.md`, Subtask (`assets/task-templates.md` line 214). Title, About, Requirements, area headings present. Facts: Mobile Platform led by Oskar (line 7) matches context line 89; Yara's review on 2026-09-16 (line 122) matches parent line 109; the reminder as a local notification (line 95) matches context line 77; `user_id` hashed and no to-do text (line 128) match context lines 187-188. Placeholders none. 128 lines, inside 60 to 130. Code `FE - Android - TODO`.

**Open readings**

- RO-1 decides this verdict: under the other reading `STK-005` is `PASS`. RO-3 (both read-backs are slices), RO-5 (Oskar's team).

---

### PTK-005 | Supplied parent subtask (Project)

**Draft row**

```csv
PTK-005,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 rendered one question block and Turn 2 one subtask block with the parent, every shared-rule value and every Turn 2 fact, but turn-2.md line 166 closes ""Answer any of these and I'll update the same file."", a promise to write a file on the Project side (root line 189, kernel line 101, RO-2). Advisory: 143 block lines against the 60 to 130 band."
```

**Against the main run:** failing for a new cause. The main run failed because Turn 1 rendered the full subtask with no question, which is fixed. The new miss is the Turn 2 file promise.

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question rendered as its own block | Met | fenced block turn-1.md lines 1-19 |
| Export-equivalent `task` lane `-clarification` label and `HVR self-scan:` | Met | line 21 `export/001 - task-android-recurring-todos-clarification.md`, line 23 |
| Turn 1 renders no subtask | Met | questions only. line 34 names no file (borderline, RO-2) |
| Turn 2 renders one subtask block under an export-equivalent `task` label with `HVR self-scan:` | Met | fenced block turn-2.md lines 1-145, line 147 `export/002 - task-android-recurring-todos.md`, line 149 |
| No file claim | Unmet | line 166 "Answer any of these and I'll update the same file." |
| H1, `### About`, `### Requirements` with checklisted groups | Met | lines 2, 4, 34, seven groups each with `**Checklist**` |
| Parent named as `FS - TODO - Recurring to-dos` | Met | `**Parent task**` line 16, also About line 8 |
| Shared-rule values as the parent gives them | Met | option names line 52, `1 to 99` line 62, `Never`, `On date`, `After` line 64, `365` line 66, `Skip this one` lines 83-84, `500` lines 108 and 112, `recurring_todos` lines 10, 136, 140, the `owner's time zone` lines 120 and 124 |
| Android as the only client in scope | Met | every item is Android. iOS and Web appear only in line 136's flag note |
| Every Turn 2 fact | Met | phones and tablets (lines 8, 50), Oskar's team and 5.4.0 (line 10), engine returns the date and the device never works one out (lines 10, 81, 84, 86) |
| No FAIL example hit, apart from the file claim | Met | no URL, no iOS, web, Desktop or engine work, no changed value or copy, the one unstated Android behavior (line 98) is named at line 156, no slot |

**Blocking items hit**

- A file claim on the Project side, root line 189 and ruling 3 (kernel line 101): turn-2.md line 166.

**Advisory items**

- Size band: 143 block lines against 60 to 130.
- Named additions at turn-2.md lines 156-158 (lines 98, 140, 63 and 66).
- Borderline promise at turn-1.md line 34 "the subtask will take the next number in the task lane", naming no file (RO-2).

**Realism entries**

- Block `PTK-005-turn1-block1.md` (reply lines 2-18), task-lane clarification. Question only. Facts: `BE - TODO - Recurrence engine` (line 4) matches parent line 49; Android local notifications (line 8) match `loomlist-context.md` line 77; no offline mode and retry until the app closes (line 10) match context lines 175-176; Android 5.3.0 current (line 16) matches context line 133. Placeholders none. 17 lines, no band.
- Block `PTK-005-turn2-block1.md` (reply lines 2-144), Subtask (`Product Owner - Assets - Task Templates` line 195). Title, About, Requirements, area headings present. Facts: the UTC time reminders-service hands over (line 92) matches context line 77; `user_id` hashed before it leaves the device (line 143) matches context line 188; Yara's review on 2026-09-16 (line 144) matches parent line 109; the Monthly 31st case (line 76) matches parent line 69. Placeholders none. 143 lines against 60 to 130. Code `FE - Android - TODO`.

**Open readings**

- RO-2 decides this verdict: if "I'll update the same file" is not a promise to write a file, `PTK-005` is `PASS`.

---

### PTK-006 | Data tracking task (Project)

**Draft row**

```csv
PTK-006,project,claude-opus-5-5-medium,FAIL,2,2,pending,no,"The Turn 2 block never marks `checkout_complete` as `deprecated` (removal only, turn-2.md lines 10, 71, 75-76) and writes `date_changed` as ""still a proposal"" rather than `proposed` (line 10), and turn-2.md line 96 promises ""I'll update the task under the same filename"" (RO-2). Turn 1 routed to Task Mode and rendered one question block labelled export/001 - task-booking-funnel-events-clarification.md, naming no file."
```

**Against the main run:** still failing for the same cause, the missing `deprecated` label, which the main-run twin analysis read as a runtime fault. The Turn 1 promise to "save it as the next file" is fixed. New: `proposed` is missing, and the file promise moved to Turn 2.

**The two checks asked for.** `deprecated`: grep of `PTK-006-turn2-block1.md` finds no match. The block describes the status (line 71 "keeps firing next to `booking_confirmed` until 2026-11-01", lines 75-76 the collector drop) but never prints the plan's word (plan line 25 `deprecated, removal on 2026-11-01`). Promises: Turn 1 line 39 "the task will be the next deliverable in the task lane (`002`)" names no file (borderline). Turn 2 line 96 "I'll update the task under the same filename" is graded a file claim (RO-2).

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 routes to Task Mode | Met | "write a task" matches `Product Owner - System - Router Contract` line 356, task-lane label at turn-1.md line 30 |
| Asks one question rendered as its own block | Met | fenced block turn-1.md lines 1-28 |
| Export-equivalent `task` lane `-clarification` label and `HVR self-scan:` | Met | line 30 `export/001 - task-booking-funnel-events-clarification.md`, line 32 |
| Turn 1 renders no task | Met | questions only |
| Turn 2 renders one task block under an export-equivalent `task` label with `HVR self-scan:` | Met | fenced block turn-2.md lines 1-77, line 79 `export/002 - task-booking-funnel-event-checks.md`, line 81 |
| No file claim | Unmet | line 96 "If you settle either point, I'll update the task under the same filename." (RO-2) |
| H1, `### About`, `### Requirements` with checklisted groups | Met | lines 2, 4, 18. Groups 2 and 3 use `**Checklist**` (lines 57, 73). Group 1 puts its `- [ ]` items under `**All events**` and `**Per event**` (lines 28, 37), as the main run's block did |
| Six funnel events as the plan names them | Met | lines 30 and 59 |
| `booking_confirmed` from `booking-service` with `source` set to `server` | Met | line 43 `server`, line 55 fires when `booking-service` confirms |
| `total_amount_minor` in minor units | Met | line 35, with city tax and `currency` |
| `checkout_complete` marked `deprecated` with its removal on `2026-11-01` | Unmet | removal date lines 10, 63, 71, 75-76, the word `deprecated` absent |
| `date_changed` kept `proposed` and unbuilt | Unmet | unbuilt (line 10 "out of scope"), but the status reads "while it is still a proposal" and `proposed` is absent (RO-1) |
| Every Turn 2 fact | Met, borderline | `DATA` and `TRK` (line 2), the Data team's part, checks in `events-collector`, the dashboard move, the drop on the removal date, FE and BE in separate tasks (line 10, groups at lines 22, 51, 67). Nadia is not named as the checker, and the refinement leaving the table unchanged is not stated, only applied through `draft v0.3` (line 16) (RO-5) |
| No FAIL example hit | Met | no `date_changed` build, no early or late drop (lines 75-76), no booking count from `payment_submitted` or `checkout_complete` (lines 60-61), no client `booking_confirmed` (line 43), no decimals (line 35), no FE or BE build inside the task (line 10), no slot |

**Blocking items hit**

- Pass clause missed, `checkout_complete` not marked `deprecated`, root line 150. The main-run twin analysis read this as a runtime fault.
- Pass clause missed, `date_changed` not kept `proposed` in words, root line 150, read under RO-1.
- A file claim on the Project side, root line 189 and ruling 3: turn-2.md line 96 (RO-2).

**Advisory items**

- Named additions at turn-2.md lines 86-90 (expiry line 45, Trips reopen line 46, revenue per currency line 62, per-platform checks line 31, `date_changed` left out).
- Borderline promise at turn-1.md line 39, naming no file (RO-2).
- Group 1 has no `**Checklist**` label. `Product Owner - Templates - Task Mode` lines 84-89 make the label a "should" pattern and lines 54-58 require only Title, About and Requirements, so it is not a missing required section.
- Size band: 75 block lines, inside 60 to 140.

**Realism entries**

- Block `PTK-006-turn1-block1.md` (reply lines 2-27), task-lane clarification. Question only. Facts: the three owners (line 5) match plan lines 75-77; `draft v0.3` from 2026-09-15 and the refinement on 2026-09-24 (line 13) match plan lines 1, 4, 5; Android's late `room_selected` (line 19) matches plan lines 67-71; `booking-service` copying `session_id` and `app_version` (line 20) matches plan line 55. Placeholders none. 26 lines, no band.
- Block `PTK-006-turn2-block1.md` (reply lines 2-76), Canonical Task (`Product Owner - Assets - Task Templates` line 19). Title, About, Requirements present. Facts: `RS-2MF8QD` (line 47) matches plan line 48 and `roamstay-context.md` line 47; the 30-minute `payment_pending` expiry (line 45) matches context line 148; no currency conversion (line 62) matches context line 118; city tax inside `total_amount_minor` (line 35) matches plan line 45. Missing: the status words `deprecated` and `proposed` (plan lines 25-26). Placeholders none. 75 lines, inside 60 to 140. Code `DATA`.

**Open readings**

- RO-1 (`proposed`), RO-2 (turn-2.md line 96), RO-5 (Nadia, refinement). None decides the verdict alone, since `deprecated` fails it under the reading the main run applied.

---

### Twin notes

| Pair | Skill | Project | Agree or differ | Cause and rule lines |
|---|---|---|---|---|
| STK-002 / PTK-002 | PASS | PASS | Agree | Both asked one question on Turn 1 (`AGENTS.md` line 287, kernel line 108) and delivered on Turn 2 with every limit, copy string and Turn 2 fact. Differences are recorded only: the Project added a search-form minimum rule and named it (turn-2.md line 163), and the skill flagged the minimum-stay conflict between the context and the notes on both turns. |
| STK-003 / PTK-003 | FAIL | FAIL | Agree | Runtime fault in both. Both packagings tell the runtime to keep supplied values and numbers (skill `AGENTS.md` line 42 and `assets/task-templates.md` line 157, Project kernel line 90 and `Product Owner - Assets - Task Templates` line 138), and both dropped the same three carrier values (`HMAC-SHA256`, `5 attempts`, the retry schedule, API notes lines 53 and 58) and left the Fulfilment board out of the task. Both now ask on Turn 1. |
| STK-004 / PTK-004 | PASS | PASS | Agree | Both asked first, then delivered exactly one parent with four plain-text subtask entries and no subtask files or blocks, as the scenario asks. They differ on content choices only: the skill kept rollout and tracking checks, and the Project listed seven named open questions. |
| STK-005 / PTK-005 | FAIL | FAIL | Agree on the verdict, differ on the cause | `STK-005` fails only on RO-1 (`1 to 99` restated). Both packagings carry the same keep-the-value rules cited above, so if RO-1 is read strictly this is a runtime choice, and if it is read leniently `STK-005` passes. `PTK-005` fails on a Turn 2 file promise. That is a runtime fault: kernel line 101 and root line 189 forbid it, and the skill side has no counterpart rule because it really writes files. Under the lenient RO-1 reading the pair differs (PASS, FAIL) on that runtime fault. |
| PTK-006 | n/a | FAIL | No twin in this round | `STK-006` was not remeasured. In the main run both twins failed on the missing `deprecated` label, and `PTK-006` still does. |

---

## 3. Bugs, docs and identity batch, grader draft

Batch: SBG-002, PBG-002, SDK-001, PDK-001, SDK-003, PDK-003, PID-001, PIR-002. Model `claude-opus-5-5-medium`. Run folder `<RUN>/remeasure-operator-repairs/run-1/`, where `<RUN>` is `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`. Product Owner commit `39bcd29`, Barter commit `df2de5f0`, playbook 2.1.0.0. `git status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing, so every source was read from the working tree and every root and source line below is cited as it stands at `39bcd29` (root copy written with `git show 39bcd29:sk-product-owner/manual-testing-playbook/manual-testing-playbook.md`).

### Handover verdict first

- **PID-001 (Project handover): FAIL.** `claude project/PID-001 - identity-handover/turn-1.md` line 48 says "Once you answer, the task will be `export/002 - task-due-today-filter-chip.md`." The block itself says "I'll write the task from your answers" (line 4). Naming the future task as a concrete `export/` Markdown file is a promise of a file, which root lines 179 and 189 and `Custom Instructions.md` line 101 make a file claim. Every other PID-001 clause is met. The alternative reading is under PID-001 Open readings, and PID-001 flips to PASS only if the operator rejects this one.

Identity split greps at `39bcd29`, run from the workspace root:

| Grep | Expected | Observed |
|---|---|---|
| `grep -c "read-back succeeded" AGENTS.md` | `2`, exit `0` | `2`, exit `0` (lines 47 and 91) |
| `grep -c "read-back succeeded" "claude project/Custom Instructions.md"` | `0`, exit `1` | `0`, exit `1` |
| `grep -c "Canvas Artifact" AGENTS.md` | `0`, exit `1` | `0`, exit `1` |
| `grep -c "Canvas Artifact" "claude project/Custom Instructions.md"` | `4`, exit `0` | `4`, exit `0` (lines 76, 181, 221, 235) |

### Tally

| Runtime | PASS | FAIL | SKIP |
|---|---:|---:|---:|
| skill | 2 (SBG-002, SDK-003) | 1 (SDK-001) | 0 |
| project | 2 (PDK-003, PIR-002) | 3 (PBG-002, PDK-001, PID-001) | 0 |

### Method notes

- Format gate: `node validate-output-format.cjs --system product-owner <file>` from the Sync Loop folder on all five skill exports, on the ten Project block copies and on a reconstruction of the SDK-001 Turn 1 export. Everything passed with exit 0 except `skill/SDK-003 .../002 - doc-sync-conflict-options.md` lines 114 and 115 and block `PDK-003-turn2-block.md` lines 151 and 152, each `prose em dash (HVR bans it, use a comma, colon or full stop)`, all on Source basis bullets. No Pass clause in this batch names the em dash, so these are advisory evidence.
- Block copies sit in `scratch/grades/blocks/remeasure-bugs-docs-identity/` as `<ID>-turn<n>-block.md`: the text between the opening and closing fence, so block line `k` is reply line `k + 1`. Every Project block was fenced (```` ```markdown ```` or ```` ````markdown ```` at reply line 1), with nothing before it. Each copy is byte-identical to the collector's copy under `AI Systems/Product Owner/export/benchmark/claude project/remeasure-operator-repairs/run-1/`, and each skill export in the run folder is byte-identical to its copy under `export/benchmark/skill/remeasure-operator-repairs/run-1/`.
- SDK-001 Turn 2 edited `export/001 - doc-discount-stacking.md` in place, so the run folder only holds the Turn 2 state. The Turn 1 state is rebuilt from the file content returned by the Read at `events-turn-1.jsonl` line 105 and saved as `blocks/remeasure-bugs-docs-identity/SDK-001-turn1-export-reconstructed-from-read.md` (160 lines). Cited below as "T1 export".
- Every Project run's `meta.json` shows an empty ledger on both turns, and the Project sessions had only `Glob`, `Grep` and `Read`.
- In every Project realism entry and Pass table, line numbers are reply lines (`turn-<n>.md`) unless marked as block lines.
- Quotes that hold the definition or status-label delimiter are cut before it, so this draft carries no em dash. The block copies keep the runtime's own text byte for byte, delimiters included, because the gate and the collector comparison need them unchanged.

---

### SBG-002 (skill), Support ticket bug

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

### PBG-002 (project), Support ticket bug

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

### SDK-001 (skill), Behavior reference

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

### PDK-001 (project), Behavior reference

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

### SDK-003 (skill), Proposal with a decision owner

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

### PDK-003 (project), Proposal with a decision owner

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

### PID-001 (project), Project identity handover

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

### PIR-002 (project), Conflicting commands

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

### Twin notes

**SBG-002 and PBG-002: differ (PASS, FAIL). Runtime fault on the Project side.** Both runtimes asked first, and both built the same bug: the same amounts, the correct charge, Severity High, no device, the error-message line left out and Pay at property left open. The only difference is PBG-002's `turn-1.md` line 25 promise, "I'll write the report under the next number in the bug lane (`export/002 - bug-...`)". The skill may promise its own export (`references/bug-mode.md` line 63, `AGENTS.md` line 44). The Project kernel forbids that promise (`Custom Instructions.md` line 101), and the Project Bug Mode knowledge says only "The artifact takes the next number in the lane once the user answers" (line 46), which licenses no path. One small parity difference with no effect here: the skill states the error-message rule in Bug Mode itself (`bug-mode.md` lines 158 and 217), while the Project carries it only in the Assets template (`Product Owner - Assets - Bug Report Template - v0.101.md` line 85). Both runtimes complied.

**SDK-001 and PDK-001: agree (FAIL, FAIL), for different causes, each a runtime fault.** SDK-001 renamed the mandatory primary body to `## Stacking rules` and PDK-001 kept `## Behavior rules`. Both packagings carry the same rule: Overview and the primary body are mandatory, and only optional headings may be renamed (skill `assets/doc-templates.md` lines 115, 116 and 400; Project Doc Templates lines 94, 95 and 379). PDK-001 dropped the phrase `one discount code per order`, while SDK-001 kept it verbatim (line 53). Here the packagings agree too, and neither demands that a new document quote a source's rule phrase word for word. Their literal-copy rules cover refinements (skill `doc-mode.md` line 584, Project Doc Mode line 558), and "Preserve supplied technical identifiers" is qualified "when needed for fidelity" (skill `doc-templates.md` line 125, Project Doc Templates line 104). The verbatim demand comes from the scenario and root line 188, so the miss also points at a rule gap between the scenario and both packagings.

**SDK-003 and PDK-003: agree (PASS, PASS).** Both covered authority by stating the two files agree rather than asking which governs (skill clarification line 3, Project block line 2), so the same open reading holds for both. Both followed their Proposal scaffold's Source basis line into the format gate's em dash finding (skill `doc-templates.md` line 570, Project Doc Templates line 549). They differ only on the Doc summary. PDK-003 printed the five lines (`Custom Instructions.md` line 217) and SDK-003 printed none (`doc-mode.md` line 412). The rule is the same on both sides, so that is a skill runtime fault, recorded as advisory.

**PID-001 and PIR-002:** their twins (SID-001, SIR-002) are graded in other batches. On forward statements within this batch, the replies that attach an `export/` path to the next artifact failed (PID-001 line 48, PBG-002 line 25). The ones that name only the next number passed (PIR-002 line 64, PDK-003 line 32). Both kinds sit under the same kernel rule (`Custom Instructions.md` line 101) and the same Interactive Mode sentence (knowledge line 75).

---

## 4. Stories and Epics batch, grader draft

Run: `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/remeasure-operator-repairs/run-1/`. Model `claude-opus-5-5-medium`. Product Owner commit `39bcd29`, Barter commit `df2de5f0`, playbook 2.1.0.0. `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing, and the working-tree root is identical to `git show 39bcd29:sk-product-owner/manual-testing-playbook/manual-testing-playbook.md`, so every root, source and fixture line below is the line at `39bcd29`. `run-status.json` gives 2 of 2 turns for all nine scenarios.

Tally: skill 3 PASS, 1 FAIL. Project 0 PASS, 5 FAIL.

Reading notes that apply to every scenario below:

- **Read-back.** The skill runtime reads through the Read tool and through Bash (`cat -n`, `sed -n`). A Bash read of the exact export path that returns its lines, after the last write, is counted as the read-back. The Read tool counts the empty line after a trailing newline, so on every file read with that tool here its final line number is one above `wc -l`. `SST-002` read with Bash `cat -n`, which matches `wc -l`. Where a reply printed the `wc -l` figure instead, the `N` is recorded as off by one and not failed (brief section 2).
- **Project blocks.** Every Project block in this batch is fenced. The copies the format gate read are in `scratch/grades/blocks/remeasure-stories-epics/`, named `<ID>-turn<n>-block<k> - <label>.md`, body only, fences stripped.
- **Rulings applied.** Ruling 1 (an explicit command asks first), ruling 2 (an Epic omits References with no link) and ruling 3 (a promise to write or save a file is a Project file claim, root lines 179 and 189, kernel line 101).
- **Main-run verdicts** are from `<RUN>/results.csv`.

---

### SST-002, Story forced delivery (skill)

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

### PST-002, Story forced delivery (Project)

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

### SST-003, Story refinement (skill)

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

### PST-003, Story refinement (Project)

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

### SST-004, Story with nested tasks (skill)

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

### PST-004, Story with nested tasks (Project)

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

### SEP-001, Epic from strategy brief (skill)

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

### PEP-001, Epic from strategy brief (Project)

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

### PEP-002, Epic natural wording (Project)

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

### Twin notes

| Pair | Skill | Project | Agree or differ | Cause and rule lines |
|---|---|---|---|---|
| `ST-002` | FAIL | FAIL | Agree | Both reword `Do sub-pages inherit the link?`. It looks like a rule gap between the scenario and both packagings. The Pass clause backticks the question, while the marker template in both packagings asks only for "the part that is not decided" (`references/story-mode.md` line 332, knowledge `Product Owner - Templates - Story Mode - v0.403.md` line 308). Both Turn 1s are now correct. The Project also carries the borderline "the Story will be `export/002 - ...`" line (`turn-1.md` line 45) |
| `ST-003` | PASS | FAIL | Differ | Runtime fault on the Project side. The skill may promise its save (`turn-1.md` line 14 "I'll save the Story in `export/` under Priya's filename"), and the kernel forbids the same promise on the Project side (`Custom Instructions.md` line 101, root lines 179 and 189). The Project turn carried the skill's phrasing over. Both handle the brand conflict the same way |
| `ST-004` | PASS | FAIL | Differ | Runtime fault on the Project side, on two rules both packagings state alike. The split question is at `references/story-mode.md` line 406 and `SKILL.md` line 252 on the skill side, and knowledge Story Mode line 382 on the Project side. The skill asked it (clarification lines 5 to 12), and the Project announced the brief's six instead. The file promise breaks kernel line 101. Turn 2 is correct on both sides |
| `EP-001` | PASS | FAIL | Differ | Runtime fault on the Project side. Kernel line 101 forbids "I'll write the task as `export/002 - ...`", and `PEP-001` wrote "I'll write the epic as `export/002 - ...`". The Project knowledge frames the next artifact as "a new Deliverable Block taking the next number" (`Product Owner - System - Interactive Mode - v0.406.md` line 75), so no Project text invites the promise |
| `EP-002` | (not in this round, main run PASS) | FAIL | Differ against the main-run twin | Same runtime fault as `PEP-001`, kernel line 101 |

The Project file promise appears in four of the five Project scenarios here (`PST-003`, `PST-004`, `PEP-001`, `PEP-002`, plus the borderline `PST-002`), always in the closing line after the Turn 1 clarification block. Kernel line 101 is the only Project text that forbids it. Neither the Story Mode nor the Interactive Mode knowledge file restates it beside the clarification label rules, where the runtime writes that line.
