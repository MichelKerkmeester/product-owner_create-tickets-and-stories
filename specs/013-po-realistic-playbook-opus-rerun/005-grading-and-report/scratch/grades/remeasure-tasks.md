# Grades draft: remeasure-tasks batch

Batch `remeasure-tasks`, nine scenarios from the remeasure round `remeasure-operator-repairs/run-1`: `STK-002..STK-005` with their twins `PTK-002..PTK-005`, plus `PTK-006` alone. Model `claude-opus-5-5-medium`. Graded read-only against `scratch/grading-brief.md` and `scratch/grading-brief-remeasure.md`.

## Conventions used in this draft

- `<R1>` is `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/remeasure-operator-repairs/run-1/`. Skill evidence sits under `<R1>/skill/<ID> - <slug>/`, Project evidence under `<R1>/claude project/<ID> - <slug>/`. Every `replies/<ID>-turn<n>.txt` is byte-identical to its `turn-<n>.md` (checked with `cmp`, all 18 the same).
- Sources are cited at Product Owner `39bcd29`. `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing, so the working tree was read directly. Root lines come from `git show 39bcd29:sk-product-owner/manual-testing-playbook/manual-testing-playbook.md` (version 2.1.0.0): verdict line 150, rendering line 163, identity handover line 179, invented fact line 187, protected fact line 188, file claim line 189, Ticket realism lines 198 to 214.
- `run-status.json`: all nine scenarios `status ok`, `turns_run 2`, `turns_declared 2`.
- "call N" is the Nth tool call in that turn's `events-turn-<n>.jsonl`, counted in stream order.
- Skill export line numbers are the file in `exports/export/`. Project line numbers are `turn-<n>.md` reply lines. Block copies for the format gate sit in `scratch/grades/blocks/remeasure-tasks/<ID>-turn<n>-block1.md` and hold the text between the fence lines, so a block copy's line is the reply line minus 1.
- Format gate: `node validate-output-format.cjs --system product-owner "<file>"` from the `AI Systems/z*Sync Loop` folder the brief names. All 8 skill export files and all 10 Project block copies printed `Product Owner output format validation passed across 1 artifact file(s)`, exit 0.
- Every Project conversation had only `read`, `ls`, `grep`, `find` (meta.json), and every Project turn ledger is empty. Every skill ledger shows exactly one new `export/` file per turn and nothing modified or deleted, so no `context/` file changed and no clarification file was touched on Turn 2.
- The Read tool shows an empty last line after a trailing newline, so a full Read's final line number is `wc -l` plus 1 on every export here.

## Shared open readings

- **RO-1, verbatim versus the same value in other words** (carried over from the main run's OR-3, not among the seven rulings). The remeasure brief leaves it open, so every such case is graded by the text as Unmet. It alone decides `STK-005`: the Pass clause lists `1 to 99` "as the parent gives them" (parent line 67 "with N from 1 to 99"), and export line 56 writes "the member cannot save an N below 1 or above 99". It also touches `PTK-006`, where `date_changed` is "still a proposal" (turn-2.md line 10) and never `proposed`. Question: does a hard value or status restated with the same meaning in other words count as verbatim?
- **RO-2, what a Project promise has to say to be a file claim.** Ruling 3 (root line 189, kernel line 101) makes a promise to write or save a file a file claim, and the main-run regrade recorded `PBG-003` "the bug report will take the next number in the bug lane" as borderline because it names no file. Graded here as follows. File claim: `PTK-005` turn-2.md line 166 "Answer any of these and I'll update the same file." (decides `PTK-005`) and `PTK-006` turn-2.md line 96 "If you settle either point, I'll update the task under the same filename." (does not decide `PTK-006` alone). Borderline, recorded only: `PTK-003` turn-1.md line 45 "Once you answer, the task will be `export/002 - task-...`" (names a path but promises no write or save), and three sentences that name no file, `PTK-002` turn-1.md line 39, `PTK-005` turn-1.md line 34 and `PTK-006` turn-1.md line 39. Question: is "update the same file" or "update the task under the same filename" a promise to write a file, and is "the task will be `export/002 - ...`" one?
- **RO-3, a read-back that covers only part of the file.** `STK-002` Turn 2 and `STK-005` Turns 1 and 2 changed the export after their last full Read and then read back only a slice (lines 170-179, 5-17 and 120-129). `AGENTS.md` line 46 and `SKILL.md` line 211 require a Read that "returns non-empty content at that path", which a slice meets, so these are graded as proof. Question: must the read-back after the last change cover the whole file?
- **RO-4, which count is `N`** (the main run's OR-2). `AGENTS.md` line 46 sets `N` to "the final line number returned by Read". Most replies printed the full Read's final line (`wc -l` plus 1). `STK-002` Turn 2 printed 178, `wc -l`, where its last Read ended on line 179. No Pass clause here makes the count a condition, so nothing rests on it.
- **RO-5, a Turn 2 fact carried by structure or by the context's own name.** "No parent" (TK-002, TK-003) is carried by the absence of a `**Parent task**` block, as the main run read it. `STK-005` writes "The Mobile Platform team" where Turn 2 says "Oskar's team" (`loomlist-context.md` line 89 names Oskar as that team's lead). `PTK-006` does not name Nadia as the checker and never states that refinement left the event table unchanged, though it builds from `draft v0.3` as written. All graded Met or Met, borderline. Question: must such a fact be stated in words?
- **RO-6, where "it goes on the Fulfilment board" must live.** Both TK-003 runtimes keep the board out of the task and name it only in the reply (the same reading the main run applied to `PTK-003`). Graded Unmet in both, and it decides neither verdict alone.

---

## STK-002 | Design notes FE task (skill)

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

## PTK-002 | Design notes FE task (Project)

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

## STK-003 | Long BE integration task (skill)

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

## PTK-003 | Long BE integration task (Project)

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

## STK-004 | Parent task with subtasks (skill)

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

## PTK-004 | Parent task with subtasks (Project)

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

## STK-005 | Supplied parent subtask (skill)

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

## PTK-005 | Supplied parent subtask (Project)

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

## PTK-006 | Data tracking task (Project)

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

## Twin notes

| Pair | Skill | Project | Agree or differ | Cause and rule lines |
|---|---|---|---|---|
| STK-002 / PTK-002 | PASS | PASS | Agree | Both asked one question on Turn 1 (`AGENTS.md` line 287, kernel line 108) and delivered on Turn 2 with every limit, copy string and Turn 2 fact. Differences are recorded only: the Project added a search-form minimum rule and named it (turn-2.md line 163), and the skill flagged the minimum-stay conflict between the context and the notes on both turns. |
| STK-003 / PTK-003 | FAIL | FAIL | Agree | Runtime fault in both. Both packagings tell the runtime to keep supplied values and numbers (skill `AGENTS.md` line 42 and `assets/task-templates.md` line 157, Project kernel line 90 and `Product Owner - Assets - Task Templates` line 138), and both dropped the same three carrier values (`HMAC-SHA256`, `5 attempts`, the retry schedule, API notes lines 53 and 58) and left the Fulfilment board out of the task. Both now ask on Turn 1. |
| STK-004 / PTK-004 | PASS | PASS | Agree | Both asked first, then delivered exactly one parent with four plain-text subtask entries and no subtask files or blocks, as the scenario asks. They differ on content choices only: the skill kept rollout and tracking checks, and the Project listed seven named open questions. |
| STK-005 / PTK-005 | FAIL | FAIL | Agree on the verdict, differ on the cause | `STK-005` fails only on RO-1 (`1 to 99` restated). Both packagings carry the same keep-the-value rules cited above, so if RO-1 is read strictly this is a runtime choice, and if it is read leniently `STK-005` passes. `PTK-005` fails on a Turn 2 file promise. That is a runtime fault: kernel line 101 and root line 189 forbid it, and the skill side has no counterpart rule because it really writes files. Under the lenient RO-1 reading the pair differs (PASS, FAIL) on that runtime fault. |
| PTK-006 | n/a | FAIL | No twin in this round | `STK-006` was not remeasured. In the main run both twins failed on the missing `deprecated` label, and `PTK-006` still does. |
