# Grades draft: values-backlog batch

Batch `values-backlog`, six scenarios from the third round `remeasure-supplied-values/run-1`: both twins of `TK-003`, `TK-005` and `TK-006`, which are `STK-003`, `PTK-003`, `STK-005`, `PTK-005`, `STK-006` and `PTK-006`. Model `claude-opus-5-5-medium`. Graded read-only against `scratch/grading-brief.md`, `scratch/grading-brief-remeasure.md` and `scratch/grading-brief-values.md`.

Tally: skill 3 PASS, 0 FAIL. Project 3 PASS, 0 FAIL.

## Conventions used in this draft

- `<R3>` is `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/remeasure-supplied-values/run-1/`. Skill evidence sits under `<R3>/skill/<ID> - <slug>/`, Project evidence under `<R3>/claude project/<ID> - <slug>/`. Every `replies/<ID>-turn<n>.txt` is byte-identical to its `turn-<n>.md` (checked with `diff`, all 12 the same).
- Skill export line numbers are the files in `exports/export/`. Each is byte-identical (`cmp`) to its collected copy under `AI Systems/Product Owner/export/benchmark/skill/remeasure-supplied-values/run-1/<ID> - <file>`. Project line numbers are `turn-<n>.md` reply lines.
- Sources are cited at Product Owner `b50f0a0`. `git -C "AI Systems/Product Owner" rev-parse --short HEAD` prints `b50f0a0`, and `git status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing, so the working tree was read directly. Root is version 2.2.0.0: verdict and verbatim rule line 150, rendering line 163, identity rule line 179, invented fact line 187, protected fact line 188, file claim line 189, HVR line 190, response ordering line 195, Ticket realism lines 198 to 214.
- The rules under test: skill `sk-product-owner/references/task-mode.md` line 58 (value, name or status travels as the source writes it, in backticks) and line 273 (Content Validation), Project `claude project/knowledge/Product Owner - Templates - Task Mode - v0.306.md` lines 38 and 253, the same text. Every run in this batch opened its Task Mode file on Turn 1: `STK-003` call 3 (`cat`, content printed despite the sandbox's `/dev/null` error), `STK-005` call 6 (Read lines 1 to 355), `STK-006` call 5 (`cat`), `PTK-003` call 5, `PTK-005` call 4, `PTK-006` call 4.
- Scenario files at `b50f0a0`: the Pass/fail bullet is line 39 and Expected signals line 36 in all six files (`sk-product-owner/manual-testing-playbook/skill-backlog-modes/` and `project-backlog-modes/`, `long-be-integration-task.md`, `supplied-parent-subtask.md`, `data-tracking-task.md`).
- `run-status.json`: all six `status ok`, `attempts 1`, `turns_run 2`, `turns_declared 2`. Each twin pair received identical turn inputs and identical attachments (`meta.json`), the inputs match the scenario chain rows character for character, and every attachment's `sha256` matches the fixture on disk.
- Ledgers (`meta.json`): each skill turn created exactly one `export/` file and modified or deleted nothing, so no `context/` file changed and no clarification was touched on Turn 2. Every Project turn ledger is empty, and the Project tools were `read`, `ls`, `grep`, `find` only.
- "call N" is the Nth tool call in that turn's `events-turn-<n>.jsonl`, in stream order.
- Format gate: `node validate-output-format.cjs --system product-owner "<file>"` from the `AI Systems/z*Sync Loop` folder. All 6 skill export files and all 6 Project block copies printed `Product Owner output format validation passed across 1 artifact file(s)`, exit 0. Because this round's write authority is this one file, the Project block copies (the text between the fence lines, so a block line is the reply line minus 1) were written to the session scratchpad outside the repository, not to `scratch/grades/blocks/`.
- `after_failed_gate` is `no` in every row, per `grading-brief-values.md` line 40.

## Values under test, this round

| Scenario | Value | Kept | Where |
|---|---|---|---|
| `STK-003` | `event_id` | yes, verbatim in backticks | export `002` lines 48, 52, 53 |
| `STK-003` | `X-Carrier-Signature`, `HMAC-SHA256` | yes, verbatim in backticks | export `002` line 36 |
| `STK-003` | `5 seconds` | yes, verbatim in backticks | export `002` lines 7, 35 |
| `STK-003` | retry count or schedule | unchanged where stated: "the carrier's fifth retry landed after 21:00" (thread line 27) and "the carrier's last retry at 7 hours 21 minutes" (API notes line 59). `5 attempts` and the five steps are not written | export `002` lines 7, 53 |
| `STK-003` | Fulfilment board | yes, in the task | export `002` line 11 |
| `PTK-003` | `event_id` | yes | turn-2.md lines 47, 51, 55 |
| `PTK-003` | `X-Carrier-Signature`, `HMAC-SHA256` | yes | turn-2.md line 37 |
| `PTK-003` | `5 seconds` | yes | turn-2.md lines 8, 39 |
| `PTK-003` | retry count or schedule | count unchanged as "at most 5 times over 7 hours 21 minutes" (API notes lines 58 to 59), in About, not in the source's `5 attempts` wording and not in backticks. Steps not written | turn-2.md lines 10, 56 |
| `PTK-003` | Fulfilment board | yes, in the reply after the block | turn-2.md line 126 |
| `STK-005` | `99` | yes, "with N from `1` to `99`" | export `002` line 54 |
| `PTK-005` | `99` | yes, "with N from `1` to `99`" | turn-2.md line 53 |
| `STK-006` | `deprecated` | yes, with its meaning beside it | export `002` line 100 |
| `STK-006` | `proposed` | yes | export `002` line 108 |
| `STK-006` | `booking-service` | yes, no stand-in | export `002` lines 9, 69 |
| `PTK-006` | `deprecated` | yes, with its meaning beside it | turn-2.md line 88 |
| `PTK-006` | `proposed` | yes | turn-2.md line 68 |
| `PTK-006` | `booking-service` | yes, no stand-in | turn-2.md lines 57, 66 |

## Shared open readings

- **VB-1, a requirement group whose checklist items sit under per-event labels.** In both `006` twins group 1 carries its `- [ ]` items under bold labels (`**Every event**` and one per event) with no `**Checklist**` label, while groups 2 and 3 carry `**Checklist**` (`STK-006` export lines 31 to 74, `PTK-006` turn-2.md lines 22 to 62). The Pass clause says "checklisted requirement groups". Expected signals (line 36) read it as "numbered groups each with a `**Checklist**` of `- [ ]` items". Task Mode makes the label a "should" pattern (skill `references/task-mode.md` lines 104 to 109, Project Task Mode lines 84 to 89), and the required core sections are Title, `### About` and `### Requirements` only (skill lines 74 to 78, Project lines 54 to 58). Graded Met on the Pass clause's text, the reading round one applied to the same shape in `PTK-006` (`scratch/grades/remeasure-tasks.md`, PTK-006 advisory items). Question: does a numbered group with `- [ ]` items under per-event labels and no `**Checklist**` label count as a checklisted requirement group? Under the strict reading both `006` rows are FAIL.
- **VB-2, a skill-side forecast of the next export path.** `STK-003` turn-1.md line 17 "Once you answer, the task will be saved as `export/002 - task-label-webhook-fix.md`.", `STK-005` turn-1.md line 18 "the subtask will be saved as `002`", `STK-006` turn-1.md line 13 "the task will be saved as the next number". Root line 189 counts a forecast as a file claim on the Project side. On the skill side it blocks "a path claim with no readable file behind it", and in each case the file was written and read back on Turn 2. Graded not blocking. Question: does a skill-side forecast of the next path count as a path claim when the file does exist after the next turn?
- **VB-3, partial read-backs.** `STK-003` Turn 1 read back lines 13 to 14 after its last Edit, and `STK-005` Turn 2 read back lines 120 to 134 after a first Read at offset 150 returned no content. `AGENTS.md` line 46 asks for non-empty content at the path, which both meet, so both are graded as proof, as round one's RO-3 did. Question: must the read-back after the last change cover the whole file?
- **VB-4, an Expected signal the Pass clause does not list.** `STK-005` never frames the carried-over reminder as the local notification Android schedules from reminders-service's UTC time (scenario line 36, `loomlist-context.md` line 77). The Pass clause (line 39) does not list it, so it is recorded as advisory, as round two did for `PTK-005`. Question: are Expected-signal items outside the Pass bullet ever graded?
- **VB-5, a reported HVR count that misses a hard blocker.** An Oxford comma sits in `STK-006` clarification line 18 ("Should I leave it out, list it as out of scope, or include it") and in the `PTK-005` Turn 1 block (turn-1.md line 16, "a tablet layout, or a teammate's view"), and both replies report `0 hard blockers`. A count was taken, so root line 190 ("a count that was never taken") is read as not reached and both are advisory. Question: does a reported count that misses a hard blocker fail as a count never taken?
- **VB-6, "I'll draft the task once you answer" on the Project side.** `PTK-003` turn-1.md line 41, `PTK-005` turn-1.md line 41 and `PTK-006` turn-1.md lines 2 and 40 promise the artifact without naming a path or file, which is what kernel `Custom Instructions.md` line 228 asks a clarification reply to say. Kernel line 101 forbids "will write ... a file". Graded not a file claim, as round two read `PTK-005` turn-1.md line 40.
- **`N`.** Every skill reply printed the Read's final line number, which is `wc -l` plus 1 because Read shows the empty line after the trailing newline, as `AGENTS.md` line 46 asks. No wrong `N`.

---

## STK-003 | Long BE integration task (skill)

**Draft row**

```csv
STK-003,skill,claude-opus-5-5-medium,PASS,2,2,no,yes,"Turn 1 saved only export/001 - task-label-webhook-fix-clarification.md (read back by call 10), and Turn 2 saved export/002 - task-label-webhook-fix.md with `event_id`, `X-Carrier-Signature`, `HMAC-SHA256` and `5 seconds` verbatim (lines 35, 36, 48), every thread value (lines 53, 81, 98, 99), the retry facts unchanged (lines 7, 53) and every Turn 2 fact with the Fulfilment board in the task (line 11). Advisory: both replies open with a sentence before the path, and turn-1.md line 17 forecasts the 002 path (VB-2)."
```

**Against the latest earlier verdict (round one FAIL):** fixed. Round one missed `HMAC-SHA256`, `5 attempts` and the retry schedule and kept the board only in the reply's ClickUp offer. This round writes `HMAC-SHA256` at export line 36, the relaxed clause no longer asks for the count and steps verbatim and the task changes neither, and the board is in the task at line 11.

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Met | clarification `001` lines 1 to 13, one six-part question "in one response" (line 1) |
| Saves it under a `task` lane `-clarification` name | Met | T1 ledger creates only `export/001 - task-label-webhook-fix-clarification.md` |
| Reported with its path, the `Verified:` line and the `HVR self-scan:` line | Met | turn-1.md lines 3, 4, 5. Call 10 Read after the call 9 Edit returned lines 13 to 14 (VB-3) |
| Drafts no task | Met | T1 ledger, questions only. turn-1.md line 1 "I haven't written the task yet" |
| Turn 2 saves one `task` export on the next number | Met | T2 ledger creates only `export/002 - task-label-webhook-fix.md` |
| Read back and reported the same way | Met | call 4 Read lines 1 to 113 after the call 3 Write. turn-2.md lines 3, 4, 5 |
| H1, `### About`, `### Requirements` | Met | export lines 1, 3, 23 |
| A checklisted group for each of the five points | Met | groups 1 to 5 at lines 27, 44, 57, 73, 90, each with `**Checklist**` (lines 33, 50, 63, 79, 96) |
| `event_id`, `X-Carrier-Signature`, `HMAC-SHA256` and `5 seconds` verbatim | Met | `5 seconds` lines 7 and 35, `X-Carrier-Signature` and `HMAC-SHA256` line 36, `event_id` lines 48, 52, 53. API notes lines 29, 53 and 57 set each in backticks, so word for word applies (root line 150) |
| Any retry count or schedule the task states unchanged | Met | line 7 "the carrier's fifth retry landed after 21:00" (thread line 27), line 53 "the carrier's last retry at 7 hours 21 minutes" (API notes line 59). No count, step or window changed |
| `7 days`, `10 minutes`, `30 minutes`, `#fulfilment-alerts` and `more than 5` verbatim | Met | line 53, line 81, line 98 (both), line 99. Thread lines 34, 36, 37 |
| Polling only kept out | Met | line 13 "Polling only is out of scope. The thread rejected it because the account's `20 requests per second` limit is shared with the POSTs" (thread lines 45, 53) |
| Every Turn 2 fact, the board counting in the task or the reply | Met | line 11 "Owner: Joris. Board: Fulfilment. No parent task. It has to be live before the November peak."; the replay giving one shipment and one label per parcel line 111; a late `label.created` changing nothing lines 83 and 112; the 8-second warehouse timeout kept and moved to the queue worker lines 31 and 38 |
| No FAIL example hit | Met | no idempotency key claimed, and line 61 keeps "the carrier does not dedupe on `reference`"; no retry step, window or alert threshold changed; polling neither built nor offered; the open carrier question stays open at line 69 ("Their engineer thought not and promised to check", API notes line 72); no queue, store or vendor product beyond "a queue" (thread line 33) and "our own storage" (API notes line 64); About's cause matches thread lines 21 to 27; no slot or placeholder link, since `{shipment_id}` at lines 77 and 81 is the endpoint as API notes line 14 writes it |

**Blocking items hit**

None.

**Advisory items**

- Named additions at turn-2.md lines 9 to 17: open statuses (line 66), other failure codes unchanged (line 67), shared rate limit and `Retry-After` (line 84), a failed warehouse call leaving the event to process again (line 39), "changes nothing" spelled out (line 83), a GET label stored like a webhook label (line 82), the replay against the carrier's test environment (line 107), the title.
- Borderline, not named: line 65 keys the open-shipment check on the parcel's `reference`. API notes line 16 defines `reference` as the order number and parcel index, and line 61 keeps that the carrier does not dedupe on it, so it is not the Fail example.
- Line 86 sends the undecided GET `label_failed` path to Noor, and turn-2.md line 21 discloses it.
- Response ordering: both replies open with a sentence before `Path:` (turn-1.md line 1, turn-2.md line 1), where `AGENTS.md` line 108 says start with the path. Root line 195, advisory.
- turn-1.md line 17 forecasts the Turn 2 path (VB-2).
- The clarification asks nothing an attachment states outright.
- Size band: 112 lines, inside 110 to 220.

**Read-back table**

| Turn | Export path | `N` printed | Read after the last write, lines returned | `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - task-label-webhook-fix-clarification.md` | 14 (turn-1.md line 4) | Write call 7, Read call 8 (lines 1 to 14), Edit call 9, Read call 10 at offset 13, lines 13 to 14 of 14 | 13 |
| 2 | `export/002 - task-label-webhook-fix.md` | 113 (turn-2.md line 4) | Write call 3, Read call 4, lines 1 to 113 of 113 | 112 |

**Realism entries**

- `export/001 - task-label-webhook-fix-clarification.md`, task-lane clarification (`SKILL.md` line 208). Question only, no draft. Facts: `BE - SHIP` (line 3) matches `fernhouse-context.md` lines 93 and 104; the "label webhook ticket" (line 3) matches thread line 3; `label_pending` and `label_ready` (line 5) match API notes line 14; the open `SERVICE_UNAVAILABLE` question (line 7) matches API notes line 72; `20 requests per second` (line 9) matches API notes line 68; 6 to 9 seconds, `15:00` and 18:00 (line 13) match thread line 21 and context lines 47 to 48. Placeholders none. 13 lines, no band. Format gate passed.
- `export/002 - task-label-webhook-fix.md`, Canonical Task (`assets/task-templates.md` line 38). Title, `### About`, `### Requirements` present (lines 1, 3, 23). Facts: `37 duplicate labels` at `€0.42` (line 7) match thread lines 9 and 17; `12 orders`, `15:00` and 18:00 (line 7) match thread line 13; 14 POSTs a second (line 13) matches thread line 45; `FH-2291834-1` (line 65) matches API notes line 16; `label_url` expiring after `24 hours` (line 40) matches API notes line 64. Placeholders none. 112 lines, inside 110 to 220. Title code `BE`, feature `SHIP`, surface dropped as context line 93 asks. Format gate passed.

**Open readings**

- VB-2 (turn-1.md line 17), VB-3 (Turn 1 read-back is a slice). Neither decides the verdict.

---

## PTK-003 | Long BE integration task (Project)

**Draft row**

```csv
PTK-003,project,claude-opus-5-5-medium,PASS,2,2,no,yes,"Turn 1 rendered one fenced question block labelled export/001 - task-label-webhook-fix-clarification.md and Turn 2 one fenced task block with `event_id`, `X-Carrier-Signature`, `HMAC-SHA256` and `5 seconds` verbatim (turn-2.md lines 37, 39, 47), every thread value (lines 56, 87, 99, 100) and the retry count unchanged (line 10), the Fulfilment board named in the reply after the block (line 126) and no file claim in either turn. Borderline: the replay setup at line 112 and ""no carrier API call"" at line 40 are not named as additions."
```

**Against the latest earlier verdict (round one FAIL):** fixed. Round one missed `HMAC-SHA256`, `5 attempts` and the schedule and kept the board out of the task. This round writes `HMAC-SHA256` at turn-2.md line 37, states the count unchanged at line 10, and names the board at line 126, which the relaxed clause counts. Round one's borderline forecast "the task will be `export/002 - task-...`" is gone: Turn 1 closes "I'll draft the task as soon as you answer." (line 41). Not rerun in round two.

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question rendered as its own block | Met | fenced block turn-1.md lines 1 to 25, questions only |
| Under an export-equivalent `task` lane `-clarification` label | Met | line 27 `export/001 - task-label-webhook-fix-clarification.md` |
| With the `HVR self-scan:` line | Met | line 29 |
| Renders no task | Met | questions only, line 41 "I'll draft the task as soon as you answer." |
| Turn 2 renders one task block under an export-equivalent `task` label | Met | fenced block turn-2.md lines 1 to 118, line 120 `export/002 - task-label-webhook-fix.md` |
| With the `HVR self-scan:` line | Met | line 122 |
| No file claim, no `Path:`, `Saved:` or `Verified:` | Met | neither reply prints those labels or promises or forecasts a file (grep of both replies). turn-1.md line 41 names no file (VB-6) |
| H1, `### About`, `### Requirements` | Met | lines 2, 4, 21 |
| A checklisted group for each of the five points | Met | groups 1 to 5 at lines 29, 47, 64, 79, 93, each with `**Checklist**` (lines 35, 53, 70, 85, 97) |
| `event_id`, `X-Carrier-Signature`, `HMAC-SHA256` and `5 seconds` verbatim | Met | `5 seconds` lines 8 and 39, `X-Carrier-Signature` and `HMAC-SHA256` line 37, `event_id` lines 47, 51, 55 |
| Any retry count or schedule the task states unchanged | Met | line 10 "The carrier retries a failed delivery at most 5 times over 7 hours 21 minutes" against API notes lines 58 to 59 "up to `5 attempts` more" and "7 hours 21 minutes", line 56 "the carrier's last retry at 7 hours 21 minutes". No step stated |
| `7 days`, `10 minutes`, `30 minutes`, `#fulfilment-alerts` and `more than 5` verbatim | Met | line 56, line 87, line 99 (both), line 100 |
| Polling only kept out | Met | line 12 "Polling only is out of scope. The thread `rejected` it because of the rate limit" |
| Every Turn 2 fact, the board counting in the block or the reply after it | Met | no `**Parent task**` block and line 126 "I left out a parent task"; line 126 "Put it on the Fulfilment board when you add it."; the November peak line 10; the replay giving one shipment and one label per parcel line 116; a late `label.created` changing nothing line 117; the `8-second` warehouse timeout kept and moved to the queue lines 40 and 42 |
| No FAIL example hit | Met | line 10 keeps no idempotency key and no `reference` dedupe; no retry step, window or threshold changed; no polling; the open carrier question stays open at line 75; no product named; About's cause matches thread lines 21 to 27; no slot or placeholder link (`{shipment_id}` at lines 83 and 87 as API notes line 14 writes it) |

**Blocking items hit**

None.

**Advisory items**

- Named additions at turn-2.md lines 128 to 131: the references as plain names (lines 18 to 19), a GET label copied into our own storage (line 89), the open-question note (line 75).
- Borderline, not named: line 40 "No warehouse system call and no carrier API call happens inside the request" restates thread line 33 "Nothing slow inside the request", and line 112 describes the replay as recreating 2026-09-15 with the carrier retrying both event types "including `SERVICE_UNAVAILABLE` failures", drawn from About's incident facts. Neither adds a value.
- Lines 133 to 137 leave four points open in the reply and say so, rather than settling them in the block.
- Rendering: both blocks fenced at reply line 1 with no commentary before them (root line 163, kernel line 85).
- Size band: 116 block lines, inside 110 to 220.

**Realism entries**

- Block turn-1.md lines 2 to 24, task-lane clarification. Question only. Facts: `BE - SHIP` (line 5) matches `fernhouse-context.md` lines 93 and 104; €15.54 (line 23) matches thread line 17; `20 requests per second`, `429` and `Retry-After` (line 17) match API notes line 68; `ADDRESS_INVALID` waiting on a CS address fix (lines 10 to 11) matches API notes line 33. Placeholders none. 23 lines, no band. Format gate passed.
- Block turn-2.md lines 2 to 117, Canonical Task (`Product Owner - Assets - Task Templates` line 19). Title, `### About`, `### Requirements` present (lines 2, 4, 21). Facts: 14:05 to 15:50 and 6 to 9 seconds (line 8) match thread line 21; `€0.42` (line 8) matches thread line 17; 14 POSTs a second (line 12) matches thread line 45; the thread and notes dates (lines 18 to 19) match thread line 3 and API notes line 3. Placeholders none. 116 lines, inside 110 to 220. Title code `BE`, feature `SHIP`. Format gate passed.

**Open readings**

- VB-6 (turn-1.md line 41). It does not decide the verdict.

---

## STK-005 | Supplied parent subtask (skill)

**Draft row**

```csv
STK-005,skill,claude-opus-5-5-medium,PASS,2,2,no,yes,"Turn 1 saved only export/001 - task-android-recurring-todos-clarification.md and Turn 2 saved export/002 - task-android-recurring-todos.md naming `FS - TODO - Recurring to-dos` (line 25) with every shared-rule value, `99` at line 54, Android as the only client and every Turn 2 fact (lines 7, 9, 66). Advisory: 133 lines against the 60 to 130 band, and the carried-over reminder is never framed as an Android local notification (Expected signals only, VB-4)."
```

**Against the latest earlier verdict (round one FAIL):** fixed. Round one failed only on `1 to 99` restated as "cannot save an N below 1 or above 99". The clause now lists `99`, and export line 54 writes "with N from `1` to `99`".

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Met | clarification lines 3 to 23, six numbered parts, "please answer these in one reply" (line 3) |
| Saves it under a `task` lane `-clarification` name | Met | T1 ledger creates only `export/001 - task-android-recurring-todos-clarification.md` |
| Reported with its path, the `Verified:` line and the `HVR self-scan:` line | Met | turn-1.md lines 3, 4, 5. Call 13 Read lines 1 to 24 after the call 12 `sed -i` edit |
| Drafts no task | Met | T1 ledger, questions only |
| Turn 2 saves one `task` export on the next number | Met | T2 ledger creates only `export/002 - task-android-recurring-todos.md` |
| Read back and reported the same way | Met | call 5 Read at offset 120 returned lines 120 to 134 after the call 3 Write (call 4 at offset 150 returned no content, VB-3). turn-2.md lines 3, 4, 5 |
| H1, `### About`, `### Requirements` | Met | lines 1, 3, 35 |
| Checklisted requirement groups | Met | six numbered groups under four area headings (lines 39, 71, 91, 118), each with `**Checklist**` (lines 49, 64, 81, 101, 112, 128) |
| Parent named as `FS - TODO - Recurring to-dos` | Met | `**Parent task**` line 25, backticked, no link |
| `Daily`, `Weekdays`, `Weekly`, `Monthly`, `Custom` as the parent gives them | Met | line 53 (parent lines 63 to 67) |
| `99` | Met | line 54 "with N from `1` to `99`" (parent line 67) |
| `Never`, `On date`, `After` | Met | line 55 (parent lines 75 to 77) |
| `365` | Met | line 56 "from `1` to `365`" |
| `Skip this one` | Met | lines 86, 87 (parent line 85) |
| `500` | Met | lines 99 and 103, the sheet copy verbatim at line 103 (parent line 91) |
| `recurring_todos` | Met | lines 9, 110, 116 (parent line 11 sets it in backticks) |
| The `owner's time zone` | Met | line 62 "the owner's time zone" (parent line 97, plain text) |
| Android as the only client in scope | Met | every checklist item is Android. iOS and Web appear only in line 9's reason and as related tasks at lines 32 to 33 |
| Every Turn 2 fact | Met | the Android entry (title line 1 is parent line 37); phones and tablets lines 7, 51; Oskar's team as "The Mobile Platform team (Oskar)" line 7 (`loomlist-context.md` line 89); `5.4.0` line 7; the next due date from the engine and never on the device lines 9, 62, 66 |
| No FAIL example hit | Met | no URL; no iOS, web, Desktop or engine work; no device date math (line 66); no option, range, limit, sheet copy or plan rule changed; the one Android behavior no source states, flag off hides the controls (line 116), is named at turn-2.md line 16; no slot |

**Blocking items hit**

None.

**Advisory items**

- Named additions at turn-2.md lines 15 to 18: flag off (line 116), the reminder wording (line 85), the tracking-sender note to Yara (line 133).
- Expected signals line 36 ask for the carried-over reminder as the local notification Android schedules from reminders-service's UTC time (`loomlist-context.md` line 77). Line 85 keeps it as "fires on the next occurrence at the same local time", and turn-2.md line 17 says the subtask leaves the scheduler open. Not in the Pass bullet (VB-4).
- Asking for a fact an attachment states: clarification line 23 asks "whether Android covers tablets too", which `loomlist-context.md` line 15 states. Root line 211, recorded only.
- "offers" at line 55 describes a picker literally. HVR's copula list targets "offers" standing in for "is" or "has", so recorded only.
- Response ordering: both replies open with a sentence before `Path:` (root line 195).
- turn-1.md line 18 forecasts `002` (VB-2).
- Size band: 133 lines against 60 to 130.

**Read-back table**

| Turn | Export path | `N` printed | Read after the last write, lines returned | `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - task-android-recurring-todos-clarification.md` | 24 (turn-1.md line 4) | Write call 11, Bash `sed -i` call 12, Read call 13, lines 1 to 24 of 24 | 23 |
| 2 | `export/002 - task-android-recurring-todos.md` | 134 (turn-2.md line 4) | Write call 3, Read call 4 at offset 150 (no content, "file is shorter"), Read call 5 at offset 120, lines 120 to 134 of 134 | 133 |

**Realism entries**

- `export/001 - task-android-recurring-todos-clarification.md`, task-lane clarification. Question only. Facts: `BE - TODO - Recurrence engine` (line 5) matches parent line 49; Android local notifications from reminders-service's UTC time (line 11) match `loomlist-context.md` line 77; the three flow names (line 16) match parent lines 19 to 21; the open page kept and edits retried until close (line 21) match context lines 175 to 176. Placeholders none. 23 lines, no band. Format gate passed.
- `export/002 - task-android-recurring-todos.md`, Subtask (`assets/task-templates.md` line 214). Title, `### About`, `### Requirements` and area headings present (lines 1, 3, 35, 39). Facts: the Mobile Platform team under Oskar (line 7) matches context line 89; Yara's review on 2026-09-16 (line 126) matches parent line 109; the Monthly 31st example (line 67) matches parent line 69; the limit sheet copy (line 103) matches parent line 91. Placeholders none. 133 lines against 60 to 130. Title code `FE`, platform `Android`, feature `TODO`. Format gate passed.

**Open readings**

- VB-2, VB-3, VB-4. None decides the verdict.

---

## PTK-005 | Supplied parent subtask (Project)

**Draft row**

```csv
PTK-005,project,claude-opus-5-5-medium,PASS,2,2,no,yes,"Turn 1 rendered one fenced question block and Turn 2 one fenced subtask block naming `FS - TODO - Recurring to-dos` (turn-2.md line 28) with every shared-rule value, `99` at line 53, Android as the only client and every Turn 2 fact (lines 8, 10, 12), and neither reply claims or promises a file. Borderline: the flag-off check at line 106 and the frame checks at lines 56 and 70 are not named as additions."
```

**Against the latest earlier verdict (round one FAIL):** fixed. Round one failed on the Turn 2 promise "Answer any of these and I'll update the same file." This round has no file wording in either reply. Round two (`remeasure-file-forecast`) had already passed this scenario, so the result agrees with the most recent run too.

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question rendered as its own block | Met | fenced block turn-1.md lines 1 to 29, questions only |
| Under an export-equivalent `task` lane `-clarification` label | Met | line 31 `export/NNN - task-android-recurring-todos-clarification.md` |
| With the `HVR self-scan:` line | Met | line 33 |
| Renders no subtask | Met | line 41 "I'll draft the Android subtask once you answer." (VB-6) |
| Turn 2 renders one subtask block under an export-equivalent `task` label | Met | fenced block turn-2.md lines 1 to 110, line 112 `export/NNN - task-android-recurring-todos.md` |
| With the `HVR self-scan:` line | Met | line 114 |
| No file claim, no `Path:`, `Saved:` or `Verified:` | Met | none in either reply (grep of both) |
| H1, `### About`, `### Requirements` | Met | lines 2, 4, 38 |
| Checklisted requirement groups | Met | five numbered groups at lines 42, 58, 75, 86, 98, each with `**Checklist**` (lines 48, 64, 81, 92, 104) |
| Parent named as `FS - TODO - Recurring to-dos` | Met | `**Parent task**` line 28, backticked, no link, also line 8 |
| `Daily`, `Weekdays`, `Weekly`, `Monthly`, `Custom` as the parent gives them | Met | line 52, word for word in plain text as parent lines 63 to 67 write them |
| `99` | Met | line 53 "with N from `1` to `99`" |
| `Never`, `On date`, `After` | Met | line 54 |
| `365` | Met | line 55 |
| `Skip this one` | Met | lines 69, 106, 108 |
| `500` | Met | line 90, the sheet copy verbatim at line 95 |
| `recurring_todos` | Met | lines 12, 102, 106 |
| The `owner's time zone` | Met | line 10 "the owner's time zone", line 73 the teammate rule (parent line 97) |
| Android as the only client in scope | Met | every checklist item is Android. iOS and Web appear only as related tasks at lines 35 to 36 |
| Every Turn 2 fact | Met | the Android entry (title line 2); phones and tablets lines 8, 56, 70; "Oskar's team ships this in Android `5.4.0`" line 12; the engine returns the date and the device never works one out lines 10, 66, 71 |
| No FAIL example hit | Met | no URL; no iOS, web, Desktop or engine work; no device date math; no option, range, limit, copy or plan rule changed; the reminder group (lines 75 to 84), offline check-off (line 71) and tracking properties (line 109) are named at turn-2.md lines 119 to 122; no slot (`NNN` is the exempt Project path slot) |

**Blocking items hit**

None.

**Advisory items**

- Named additions at turn-2.md lines 118 to 122.
- Borderline, not named: line 106 "With `recurring_todos` off, Android shows neither Repeat nor Skip this one" restates the parent's "ships dark" (parent line 11), and the skill twin named the same item; lines 56 and 70 tie the frames to the picker and the menu; lines 107 to 108 have Android send both events where the parent (line 109) names no sender. None adds a value.
- Engine-side rules not restated: the new owner's zone on reassignment (parent line 97), a skip counting toward After (parent line 85) and the On date stop (parent line 76). Every Pass-clause value appears and Turn 2 gives these rules to the engine, so recorded only (root line 208).
- VB-5: the Turn 1 block's Oxford comma at turn-1.md line 16, against `0 hard blockers` at line 33.
- "offers" at lines 52 and 54 describes a picker literally. Recorded only.
- Option names are plain text, not backticked as Task Mode line 38 now asks. The parent writes them plain, so root line 150 meets the clause with the same words.
- Rendering: both blocks fenced at reply line 1 with no commentary before them.
- Size band: 108 block lines, inside 60 to 130.

**Realism entries**

- Block turn-1.md lines 2 to 28, task-lane clarification. Question only. Facts: billing only on Web (line 12) matches `loomlist-context.md` line 13; Android local notifications (line 9) match context line 77; the flow names (line 22) match parent lines 19 to 21; `BE - TODO - Recurrence engine` (line 5) matches parent line 49. Placeholders none. 27 lines, no band. Format gate passed.
- Block turn-2.md lines 2 to 109, Subtask (`Product Owner - Assets - Task Templates` line 195). Title, `### About`, `### Requirements` present (lines 2, 4, 38). Facts: Oskar's team (line 12) matches context line 89; `workspace_id`, `user_id`, `platform`, `app_version`, `plan` and `user_id` hashed (line 109) match context lines 187 to 188; Yara's review on 2026-09-16 (line 102) matches parent line 109; the limit sheet copy (line 95) matches parent line 91. Placeholders none. 108 lines, inside 60 to 130. Title code `FE`, platform `Android`, feature `TODO`. Format gate passed.

**Open readings**

- VB-5, VB-6. Neither decides the verdict.

---

## STK-006 | Data tracking task (skill)

**Draft row**

```csv
STK-006,skill,claude-opus-5-5-medium,PASS,2,2,no,yes,"Turn 1 saved only export/001 - task-booking-funnel-events-clarification.md and Turn 2 saved export/002 - task-booking-funnel-events.md with the six events (line 29), `booking_confirmed` from `booking-service` with `source` `server` (lines 34, 69), `total_amount_minor` in minor units (line 55), `checkout_complete` marked `deprecated` (line 100) with its 2026-11-01 removal, `date_changed` kept `proposed` (line 108) and every Turn 2 fact (lines 9, 11). Open reading: group 1 carries its checklist items under per-event labels with no `**Checklist**` label (lines 31 to 74), graded Met on the Pass clause text (VB-1)."
```

**Against the latest earlier verdict (main run FAIL, not rerun in round one or two):** fixed. The main run never printed `deprecated`. This round writes "`checkout_complete` is `deprecated`: it keeps firing until its removal date" at export line 100.

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 routes to Task Mode | Met | T1 call 5 reads `references/task-mode.md` and the clarification saves in the `task` lane; turn-1.md line 1 "I haven't written the task yet" |
| Asks one question | Met | clarification lines 3 to 26, parts 0 to 7 "all in one reply" (line 3) |
| Saves it under a `task` lane `-clarification` name | Met | T1 ledger creates only `export/001 - task-booking-funnel-events-clarification.md` |
| Reported with its path, the `Verified:` line and the `HVR self-scan:` line | Met | turn-1.md lines 3, 4, 5. Call 11 Read lines 1 to 27 after the call 10 Write |
| Drafts no task | Met | T1 ledger, questions only |
| Turn 2 saves one `task` export on the next number | Met | T2 ledger creates only `export/002 - task-booking-funnel-events.md` |
| Read back and reported the same way | Met | call 4 Read lines 1 to 109 after the call 2 Write (call 3 is a read-only `grep`). turn-2.md lines 3, 4, 5 |
| H1, `### About`, `### Requirements` | Met | lines 1, 3, 19 |
| Checklisted requirement groups | Met (VB-1) | groups 1 to 3 at lines 23, 78, 96. Groups 2 and 3 carry `**Checklist**` (lines 84, 102). Group 1 carries 28 `- [ ]` items under `**Every event**` (line 31) and six per-event labels (lines 39 to 67) with no `**Checklist**` label |
| The six funnel events as the plan names them | Met | line 29 and line 86, names as plan lines 19 to 24 |
| `booking_confirmed` from `booking-service` with `source` set to `server` | Met | line 9 "which `booking-service` sends", line 34 "`source` is `client` on the five client events and `server` on `booking_confirmed`", line 69 "Fires from `booking-service`" (plan line 55) |
| `total_amount_minor` in minor units | Met | line 55 "as an integer in minor units with city tax included, with `currency` beside it" (plan line 45) |
| `checkout_complete` marked `deprecated` with its removal on `2026-11-01` | Met | line 100 "`checkout_complete` is `deprecated`: it keeps firing until its removal date, then `events-collector` drops it"; 2026-11-01 at lines 9, 96, 104, 105. `deprecated` is a word from the plan's status key (plan line 28), so word for word applies, and it is met |
| `date_changed` kept `proposed` and unbuilt | Met | line 108 "`date_changed` is out of scope. It is `proposed`" |
| Every Turn 2 fact | Met | the Data team's own task under `TRK` (title line 1, line 9 "This task is the Data team's part"); Nadia checks each event in `events-collector` as a squad ships it (lines 9, 27); the dashboard move (line 9, group 2); the collector drop on the removal date (line 9, group 3); the client events and `booking_confirmed` in separate FE and BE tasks (line 9); the event table unchanged at refinement (line 11) |
| No FAIL example hit | Met | `date_changed` neither built nor validated (line 108); the drop neither early nor late (lines 104 to 105); no booking count from `payment_submitted` or `checkout_complete` (lines 87, 91); `booking_confirmed` from the server (line 69); no decimals and city tax included (lines 55 to 56); the FE and BE build kept out (line 9), group 1 checks what the squads ship; no slot |

**Blocking items hit**

None.

**Advisory items**

- Named additions at turn-2.md lines 11 to 21: the `Guest app` surface, the three `booking_confirmed` checks (lines 70 to 71), web amounts (line 56), revenue per currency (line 90), `payment_submitted` never a booking (line 91), the order of the last two jobs (line 106) and the `date_changed` note (line 108).
- Borderline: line 106 "The drop goes ahead only after the dashboard no longer reads `checkout_complete`" puts a gate on the drop. It is named at turn-2.md line 21, and lines 92 and 105 keep the move before 2026-11-01 and the drop on it (plan lines 56 and 77), so the task does not keep the event past its date on its own terms.
- turn-2.md line 23 says Turn 2's "yesterday" (2026-09-25) and the plan's 2026-09-24 disagree and keeps the date out of the task. Surfaced, not silently resolved.
- VB-5: clarification line 18 carries an Oxford comma, against `0 hard blockers` at turn-1.md line 5.
- Response ordering: both replies open with a sentence before `Path:` (root line 195).
- turn-1.md line 13 forecasts "the next number" with no path (VB-2).
- Size band: 108 lines, inside 60 to 140.

**Read-back table**

| Turn | Export path | `N` printed | Read after the last write, lines returned | `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - task-booking-funnel-events-clarification.md` | 27 (turn-1.md line 4) | Write call 10, Read call 11, lines 1 to 27 of 27 | 26 |
| 2 | `export/002 - task-booking-funnel-events.md` | 109 (turn-2.md line 4) | Write call 2, read-only `grep` call 3, Read call 4, lines 1 to 109 of 109 | 108 |

**Realism entries**

- `export/001 - task-booking-funnel-events-clarification.md`, task-lane clarification. Question only. Facts: `draft v0.3` (line 3) matches plan line 1; the refinement on 2026-09-24 (line 20) matches plan line 5; the title pattern (line 16) matches `roamstay-context.md` line 83; Android's late `room_selected` (line 22) matches plan lines 67 to 71; the 2026-11-01 drop (line 24) matches plan line 56. Placeholders: the title pattern `{Discipline} - {Surface} - {Feature code} - {Title}` at line 16 is quoted from context line 83 (exempt). 26 lines, no band. Format gate passed.
- `export/002 - task-booking-funnel-events.md`, Canonical Task (`assets/task-templates.md` line 38). Title, `### About`, `### Requirements` present (lines 1, 3, 19). Facts: `RS-2MF8QD` (line 73) matches plan line 48 and context line 47; the 30-minute `payment_pending` expiry (line 70) matches context line 148; no currency conversion (line 90) matches context line 118; the web built separately (line 27) matches context line 17; `DATA` and `TRK` match context lines 80 and 97. Placeholders none. 108 lines, inside 60 to 140. Title code `DATA`, surface `Guest app`. Format gate passed.

**Open readings**

- VB-1 touches the verdict: under the strict reading this row is FAIL. VB-2, VB-5.

---

## PTK-006 | Data tracking task (Project)

**Draft row**

```csv
PTK-006,project,claude-opus-5-5-medium,PASS,2,2,no,yes,"Turn 1 rendered one fenced question block and Turn 2 one fenced task block with the six events (turn-2.md line 78), `booking_confirmed` sent by `booking-service` with `source` set to `server` (line 57), `total_amount_minor` in minor units (line 32), `checkout_complete` marked `deprecated` (line 88), `date_changed` kept `proposed` (line 68) and every Turn 2 fact (line 10), with no file claim. Open reading: group 1 carries its checklist items under per-event labels with no `**Checklist**` label (lines 22 to 62), graded Met on the Pass clause text (VB-1)."
```

**Against the latest earlier verdict (round one FAIL):** fixed. Round one missed `deprecated`, wrote `date_changed` as "still a proposal" and promised to update a file. Round two (`remeasure-file-forecast`) still failed on `deprecated` and on a missing `booking-service`. This round prints `deprecated` (line 88), `proposed` (line 68) and `booking-service` (line 57) and names no file.

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 routes to Task Mode | Met | T1 call 4 reads `Product Owner - Templates - Task Mode - v0.306.md`; `task` lane label at turn-1.md line 36 |
| Asks one question rendered as its own block | Met | fenced block turn-1.md lines 1 to 34, parts 0 to 8 "in one reply" (line 2) |
| Under an export-equivalent `task` lane `-clarification` label | Met | line 36 `export/001 - task-booking-funnel-events-clarification.md` |
| With the `HVR self-scan:` line | Met | line 38 |
| Renders no task | Met | questions only. lines 2 and 40 "I'll write the task once you reply." name no file (VB-6) |
| Turn 2 renders one task block under an export-equivalent `task` label | Met | fenced block turn-2.md lines 1 to 95, line 97 `export/002 - task-booking-funnel-event-checks-and-dashboard-move.md` |
| With the `HVR self-scan:` line | Met | line 99 |
| No file claim, no `Path:`, `Saved:` or `Verified:` | Met | none in either reply (grep of both). line 123 tells the user to copy the task into ClickUp |
| H1, `### About`, `### Requirements` | Met | lines 2, 4, 12 |
| Checklisted requirement groups | Met (VB-1) | groups 1 to 3 at lines 16, 70, 84. Groups 2 and 3 carry `**Checklist**` (lines 76, 90). Group 1 carries its `- [ ]` items under seven bold labels (lines 22 to 55) with no `**Checklist**` label |
| The six funnel events as the plan names them | Met | line 78, and the labels at lines 35 to 55 |
| `booking_confirmed` from `booking-service` with `source` set to `server` | Met | line 57 "Sent by `booking-service` with `source` set to `server`" |
| `total_amount_minor` in minor units | Met | line 32 "as an integer in minor units with city tax included" |
| `checkout_complete` marked `deprecated` with its removal on `2026-11-01` | Met | line 88 "`checkout_complete` is `deprecated`, which means it keeps firing next to `booking_confirmed` until its removal date ... From 2026-11-01 `events-collector` drops it"; lines 84, 92, 93 |
| `date_changed` kept `proposed` and unbuilt | Met | line 68 "`date_changed` is `proposed`. ... This task doesn't check it until its row is agreed." |
| Every Turn 2 fact | Met | `DATA` and `TRK` (title line 2); line 10: the event table unchanged at the Booking squad refinement, the Data team's part, Nadia checks each event in `events-collector` as the squads ship it, the dashboard move, the drop on the removal date, the client events and `booking_confirmed` in their own `FE` or `BE` task |
| No FAIL example hit | Met | `date_changed` not checked (line 68); the drop neither early nor late (lines 92 to 93); no booking count from `payment_submitted` or `checkout_complete` (line 79); `booking_confirmed` from `booking-service` (line 57); no decimals and city tax included (lines 32 to 33); the FE and BE build out of scope (line 10); no slot |

**Blocking items hit**

None.

**Advisory items**

- Named additions at turn-2.md lines 110 to 116: the `Guest app` surface, per-platform checks (line 20), the nights check (line 27, the Monday to Thursday example from `roamstay-context.md` line 38), one event per `booking_id` and the `payment_pending` expiry (lines 61 to 62), the dashboard step order (line 78), revenue by currency (line 81).
- Line 66 raises the plan's own mismatch (common properties on every event, plan line 32, against `booking-service` copying only `session_id` and `app_version`, plan line 55) as an open point for the `BE` task, and turn-2.md line 120 says so. Surfaced, not silently resolved.
- Line 88 "Older app versions may keep sending it after that date." reads plan line 56's "whatever app version sends it". Recorded only.
- turn-2.md line 108 keeps the refinement date out of the task because Turn 2's "yesterday" and the plan's 2026-09-24 disagree. Surfaced.
- No `**References**` block, an optional section (Project Task Mode lines 60 to 64).
- Rendering: both blocks fenced at reply line 1 with no commentary before them.
- Size band: 93 block lines, inside 60 to 140.

**Realism entries**

- Block turn-1.md lines 2 to 33, task-lane clarification. Question only. Facts: `draft v0.3` and the 2026-09-24 refinement (line 18) match plan lines 1 and 5; the title pattern (line 15) matches `roamstay-context.md` line 83; `booking-service` copying `session_id` and `app_version` (line 27) matches plan line 55; Android's late `room_selected` (line 24) matches plan lines 67 to 71. Placeholders: the title pattern at line 15 is quoted from context line 83 (exempt). 32 lines, no band. Format gate passed.
- Block turn-2.md lines 2 to 94, Canonical Task (`Product Owner - Assets - Task Templates` line 19). Title, `### About`, `### Requirements` present (lines 2, 4, 12). Facts: €129.50 as `12950` (line 33) matches context line 183; `RS-2MF8QD` (line 59) matches plan line 48; no currency conversion (line 81) matches context line 118; the two-week app train and continuous web deploys (line 20) match context lines 108 and 110; the `payment_pending` expiry after `30 minutes` (line 62) matches context line 168. Placeholders none. 93 lines, inside 60 to 140. Title code `DATA`, surface `Guest app`. Format gate passed.

**Open readings**

- VB-1 touches the verdict: under the strict reading this row is FAIL. VB-6.

---

## Twin notes

| Pair | Skill | Project | Agree or differ | Cause and rule lines |
|---|---|---|---|---|
| STK-003 / PTK-003 | PASS | PASS | Agree | Both kept `HMAC-SHA256` this round under the new Task Mode rule (skill `references/task-mode.md` line 58, Project `Product Owner - Templates - Task Mode - v0.306.md` line 38), which both runs opened on Turn 1. They differ on where the board sits (task line 11 against reply line 126), and the relaxed clause (scenario line 39) accepts both. Neither writes `5 attempts` or the five steps. The skill states "fifth retry" and the 7 hours 21 minutes, the Project "at most 5 times over 7 hours 21 minutes", both unchanged, which is all the relaxed clause asks. |
| STK-005 / PTK-005 | PASS | PASS | Agree | Both keep `99` (export line 54, turn-2.md line 53) and every other shared-rule value. Content differs only: the Project writes the carried-over reminder as an Android local notification (group 3, `loomlist-context.md` line 77) and names it, while the skill leaves the scheduler open and says so. The skill names the flag-off item as an addition and the Project does not (borderline). |
| STK-006 / PTK-006 | PASS | PASS | Agree | Both now print `deprecated` and `proposed` and name `booking-service`, the three words the new Task Mode rule names (skill line 58, Project line 38). Both build group 1 the same way, `- [ ]` items under per-event labels with no `**Checklist**` label. If VB-1 is read strictly both fail together, and it would be a runtime choice in both, since both Task Mode files carry the label only as a "should" pattern (skill lines 104 to 109, Project lines 84 to 89). Only the Project raises the plan's common-property against copied-property mismatch for `booking_confirmed` (plan lines 32 and 55). |
