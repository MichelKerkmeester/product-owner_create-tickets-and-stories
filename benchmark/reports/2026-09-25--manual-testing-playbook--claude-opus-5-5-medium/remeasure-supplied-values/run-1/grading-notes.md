# Grading notes, third remeasure round `remeasure-supplied-values/run-1`

Evidence behind every verdict in this folder's `results.csv`. The round reran both twins of `TK-003`, `TK-005`, `TK-006`, `DK-001`, `DK-003` and `ST-002` on Product Owner `b50f0a0` and Barter `7396d79e` (skill 1.13.0, kernel v1.16.0, playbook 2.2.0.0). Source and root lines cite that commit.

Two Opus 5.5 graders drafted the evidence, one for the three task pairs and one for the doc and Story pairs, and the orchestrator reviewed it. Sections 2 and 3 are the drafts, and `results.csv` holds the final rows.

The round's exports left `export/benchmark/` on 2026-09-26, so export lines cited here refer to the files at Product Owner `3fdce37` and Barter `d214c160`.

---

## 1. Review

**Result.** Skill 6 PASS, Project 6 PASS. No handover scenario ran in this round, and the last one graded, round two's `PID-001`, passed, so every row carries `after_failed_gate` no.

**The repair held on both sides.** Every value the first round dropped or reworded is present in this round:

| Pair | Value | Skill | Project |
| --- | --- | --- | --- |
| `TK-003` | `HMAC-SHA256` | task line 36 | turn 2 line 37 |
| `TK-005` | `99` | task line 54 | turn 2 line 53 |
| `TK-006` | `checkout_complete` marked `deprecated` | task line 100 | turn 2 line 88 |
| `TK-006` | `date_changed` kept `proposed` | task line 108 | turn 2 line 68 |
| `TK-006` | `booking-service` | task lines 9 and 69 | turn 2 line 57 |
| `DK-001` | `## Behavior rules` | export line 29 | turn 1 line 37, turn 2 line 39 |
| `DK-001` | `one discount code per order` | export line 42 | turn 2 line 45 |
| `DK-003` | block-level last-writer-wins | export line 19 | turn 2 line 20 |
| `ST-002` | `Do sub-pages inherit the link?` in the `**Open:**` line | export line 66 | turn 2 line 56 |

An independent count of each value across this round's exports and replies agreed with the drafts before they were read.

**One reading, ruled by the operator.** `PDK-003` never prints `not decided`, but its notice calls the block a proposal that is not current product behavior. It then says "none of them is approved" and "Nothing here is decided" (turn 2 lines 5, 6 and 12).

The thread's pinned `Status: not decided` (thread line 66) is neither backticked nor a status-key word, so under root line 150 other words meet the clause. The operator ruled so on 2026-09-26, and the row stays PASS.

**Readings the orchestrator checked and kept.**

- `PDK-001` says "I left out spacer headings because this is a file export" (turn 1 line 169), a rule term Doc Mode knowledge uses at lines 73 and 432, not a file claim
- The skill side forecasts the next export path on Turn 1 (`STK-003` turn 1 line 17), which the kernel's Project-only forecast rule does not govern
- Each forecast file was written and read back on Turn 2, so no path claim lacks a readable file
- Group 1 of both `TK-006` tasks lists checklist items under per-event labels without a `**Checklist**` label, which still meets the Pass clause's checklisted groups
- Partial read-backs after the last change count, as in every earlier round (`AGENTS.md` line 46)

---

## 2. Grader draft, task pairs

Batch `values-backlog`, six scenarios from the third round `remeasure-supplied-values/run-1`: both twins of `TK-003`, `TK-005` and `TK-006`, which are `STK-003`, `PTK-003`, `STK-005`, `PTK-005`, `STK-006` and `PTK-006`. Model `claude-opus-5-5-medium`. Graded read-only against `scratch/grading-brief.md`, `scratch/grading-brief-remeasure.md` and `scratch/grading-brief-values.md`.

Tally: skill 3 PASS, 0 FAIL. Project 3 PASS, 0 FAIL.

### Conventions used in this draft

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

### Values under test, this round

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

### Shared open readings

- **VB-1, a requirement group whose checklist items sit under per-event labels.** In both `006` twins group 1 carries its `- [ ]` items under bold labels (`**Every event**` and one per event) with no `**Checklist**` label, while groups 2 and 3 carry `**Checklist**` (`STK-006` export lines 31 to 74, `PTK-006` turn-2.md lines 22 to 62). The Pass clause says "checklisted requirement groups". Expected signals (line 36) read it as "numbered groups each with a `**Checklist**` of `- [ ]` items". Task Mode makes the label a "should" pattern (skill `references/task-mode.md` lines 104 to 109, Project Task Mode lines 84 to 89), and the required core sections are Title, `### About` and `### Requirements` only (skill lines 74 to 78, Project lines 54 to 58). Graded Met on the Pass clause's text, the reading round one applied to the same shape in `PTK-006` (`scratch/grades/remeasure-tasks.md`, PTK-006 advisory items). Question: does a numbered group with `- [ ]` items under per-event labels and no `**Checklist**` label count as a checklisted requirement group? Under the strict reading both `006` rows are FAIL.
- **VB-2, a skill-side forecast of the next export path.** `STK-003` turn-1.md line 17 "Once you answer, the task will be saved as `export/002 - task-label-webhook-fix.md`.", `STK-005` turn-1.md line 18 "the subtask will be saved as `002`", `STK-006` turn-1.md line 13 "the task will be saved as the next number". Root line 189 counts a forecast as a file claim on the Project side. On the skill side it blocks "a path claim with no readable file behind it", and in each case the file was written and read back on Turn 2. Graded not blocking. Question: does a skill-side forecast of the next path count as a path claim when the file does exist after the next turn?
- **VB-3, partial read-backs.** `STK-003` Turn 1 read back lines 13 to 14 after its last Edit, and `STK-005` Turn 2 read back lines 120 to 134 after a first Read at offset 150 returned no content. `AGENTS.md` line 46 asks for non-empty content at the path, which both meet, so both are graded as proof, as round one's RO-3 did. Question: must the read-back after the last change cover the whole file?
- **VB-4, an Expected signal the Pass clause does not list.** `STK-005` never frames the carried-over reminder as the local notification Android schedules from reminders-service's UTC time (scenario line 36, `loomlist-context.md` line 77). The Pass clause (line 39) does not list it, so it is recorded as advisory, as round two did for `PTK-005`. Question: are Expected-signal items outside the Pass bullet ever graded?
- **VB-5, a reported HVR count that misses a hard blocker.** An Oxford comma sits in `STK-006` clarification line 18 ("Should I leave it out, list it as out of scope, or include it") and in the `PTK-005` Turn 1 block (turn-1.md line 16, "a tablet layout, or a teammate's view"), and both replies report `0 hard blockers`. A count was taken, so root line 190 ("a count that was never taken") is read as not reached and both are advisory. Question: does a reported count that misses a hard blocker fail as a count never taken?
- **VB-6, "I'll draft the task once you answer" on the Project side.** `PTK-003` turn-1.md line 41, `PTK-005` turn-1.md line 41 and `PTK-006` turn-1.md lines 2 and 40 promise the artifact without naming a path or file, which is what kernel `Custom Instructions.md` line 228 asks a clarification reply to say. Kernel line 101 forbids "will write ... a file". Graded not a file claim, as round two read `PTK-005` turn-1.md line 40.
- **`N`.** Every skill reply printed the Read's final line number, which is `wc -l` plus 1 because Read shows the empty line after the trailing newline, as `AGENTS.md` line 46 asks. No wrong `N`.

---

### STK-003 | Long BE integration task (skill)

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

### PTK-003 | Long BE integration task (Project)

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

### STK-005 | Supplied parent subtask (skill)

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

### PTK-005 | Supplied parent subtask (Project)

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

### STK-006 | Data tracking task (skill)

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

### PTK-006 | Data tracking task (Project)

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

### Twin notes

| Pair | Skill | Project | Agree or differ | Cause and rule lines |
|---|---|---|---|---|
| STK-003 / PTK-003 | PASS | PASS | Agree | Both kept `HMAC-SHA256` this round under the new Task Mode rule (skill `references/task-mode.md` line 58, Project `Product Owner - Templates - Task Mode - v0.306.md` line 38), which both runs opened on Turn 1. They differ on where the board sits (task line 11 against reply line 126), and the relaxed clause (scenario line 39) accepts both. Neither writes `5 attempts` or the five steps. The skill states "fifth retry" and the 7 hours 21 minutes, the Project "at most 5 times over 7 hours 21 minutes", both unchanged, which is all the relaxed clause asks. |
| STK-005 / PTK-005 | PASS | PASS | Agree | Both keep `99` (export line 54, turn-2.md line 53) and every other shared-rule value. Content differs only: the Project writes the carried-over reminder as an Android local notification (group 3, `loomlist-context.md` line 77) and names it, while the skill leaves the scheduler open and says so. The skill names the flag-off item as an addition and the Project does not (borderline). |
| STK-006 / PTK-006 | PASS | PASS | Agree | Both now print `deprecated` and `proposed` and name `booking-service`, the three words the new Task Mode rule names (skill line 58, Project line 38). Both build group 1 the same way, `- [ ]` items under per-event labels with no `**Checklist**` label. If VB-1 is read strictly both fail together, and it would be a runtime choice in both, since both Task Mode files carry the label only as a "should" pattern (skill lines 104 to 109, Project lines 84 to 89). Only the Project raises the plan's common-property against copied-property mismatch for `booking_confirmed` (plan lines 32 and 55). |

---

## 3. Grader draft, doc and Story pairs

Batch: SDK-001, PDK-001, SDK-003, PDK-003, SST-002, PST-002. Model `claude-opus-5-5-medium`. Run folder `<RUN>/remeasure-supplied-values/run-1/`, where `<RUN>` is `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`. Product Owner commit `b50f0a0`, Barter commit `7396d79e`, playbook root 2.2.0.0, skill 1.13.0, kernel v1.16.0. `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing and `git log` shows HEAD at `b50f0a0`, so every source, scenario file and fixture was read from the working tree and every line below is cited as it stands at `b50f0a0`.

### Tally

| Runtime | PASS | FAIL | SKIP |
|---|---:|---:|---:|
| skill | 3 (SDK-001, SDK-003, SST-002) | 0 | 0 |
| project | 3 (PDK-001, PDK-003, PST-002) | 0 | 0 |

One verdict rests on an open reading: PDK-003 passes only because the thread's pinned `Status: not decided` is read as neither backticked nor a status-key word under root line 150. Open readings under PDK-003 set out the reading that fails it.

### Method notes

- Scenario files read at `b50f0a0`: `skill-document-modes/behavior-reference.md` and `project-document-modes/behavior-reference.md` (Pass/fail line 39), `skill-document-modes/proposal-decision-owner.md` and `project-document-modes/proposal-decision-owner.md` (line 39), `skill-story-modes/story-forced-delivery.md` and `project-story-modes/story-forced-delivery.md` (line 35). Root rules cited from `sk-product-owner/manual-testing-playbook/manual-testing-playbook.md` at `b50f0a0`, where lines 150, 179, 187 to 190 and 198 to 214 hold the text the briefs name.
- Root line 150 as it now stands is applied to every backticked value: word for word where the source sets it in backticks, gives it as a defined label such as a word from a status key, or the clause says verbatim for it; elsewhere the same value in other words meets the clause.
- Write authority for this round is this one file, so the Project block copies and the SDK-001 Turn 1 reconstruction sit in the session scratchpad, not under `scratch/grades/blocks/`. Each block copy is the text between the opening and closing fence, so block line `k` is reply line `k + 1`, and each is byte-identical (`cmp`) to the collector's copy under `AI Systems/Product Owner/export/benchmark/claude project/remeasure-supplied-values/run-1/`. Every skill export in the run folder is byte-identical to its copy under `export/benchmark/skill/remeasure-supplied-values/run-1/`.
- Format gate: `node validate-output-format.cjs --system product-owner <file>` from the Sync Loop folder, on all five skill exports, on the reconstructed SDK-001 Turn 1 export and on the six Project block copies. All twelve printed `Product Owner output format validation passed across 1 artifact file(s)` with exit 0.
- SDK-001 Turn 2 edited `export/001 - doc-promotion-stacking.md` in place (turn 2 ledger `modified`), so the run folder holds only the Turn 2 state. The Turn 1 state is rebuilt from the full Read result at `events-turn-1.jsonl` line 118 with the one later Edit (line 123, "four cases" to "five cases") applied. It has 164 lines. Cited below as "T1 export".
- Every Project run's `meta.json` shows an empty ledger on both turns and the tools `read`, `ls`, `grep`, `find` only. Every Project block was fenced (```` ```markdown ```` at reply line 1) with nothing before it.
- In Project tables, line numbers are reply lines (`turn-<n>.md`) unless marked as block lines.
- `after_failed_gate` is `no` on every row, per `grading-brief-values.md` line 40.

---

### SDK-001 (skill), Behavior reference

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

### PDK-001 (project), Behavior reference

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

### SDK-003 (skill), Proposal with a decision owner

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

### PDK-003 (project), Proposal with a decision owner

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

### SST-002 (skill), Story forced delivery

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

### PST-002 (project), Story forced delivery

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

### Rules under test: values kept this round

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

### Twin notes

**SDK-001 and PDK-001: agree (PASS, PASS).** Both kept `## Behavior rules`, which the new sentence in skill `assets/doc-templates.md` line 116 and Project `Product Owner - Assets - Doc Templates - v0.108.md` line 95 now states in the same words, and both kept every backticked rule phrase under skill line 73 and Project line 52. One difference with no verdict effect: SDK-001 carries `automatic promotions first` in a follow-on sentence that quotes the rule's wording (export line 35), where PDK-001 puts it in the stating sentence (`turn-2.md` line 50). Both packagings say the phrase belongs "in the sentence that states that rule", so this is a small runtime drift under one shared rule, not a gap. Each revised its own Turn 1 doc its own way, skill in place and Project under the same label, and both are allowed.

**SDK-003 and PDK-003: agree (PASS, PASS), and they differ on one status value.** SDK-003 prints `not decided` in its notice (line 4); PDK-003 states the same status in other words (`turn-2.md` lines 6 and 12). Both packagings carry the same rules: "Explicit status markers travel with the claims they qualify" (skill `doc-mode.md` line 153, Project Doc Mode line 129) and the Proposal notice `> **Status: {Proposal or approved direction}**` (skill `doc-templates.md` line 486, Project Doc Templates line 465). If the operator reads the pinned status as a defined label, the split is a runtime fault on the Project side. They also differ on the Doc summary: PDK-003 prints the five lines (`turn-2.md` lines 128 to 132) and SDK-003 prints none, under the same rule on both sides (skill `doc-mode.md` line 412, kernel `Custom Instructions.md` line 217). That is a skill runtime fault, advisory. Both state today's v3 rule in the thread's words, so the relaxed clause at line 39 decides nothing this round.

**SST-002 and PST-002: agree (PASS, PASS).** Both Open lines now quote `Do sub-pages inherit the link?` and then name Lena, the exact shape the amended sentence asks for (skill `references/story-mode.md` line 80, Project `Product Owner - Templates - Story Mode - v0.404.md` line 57, same text), and both repeat it in Rabbit holes (skill line 341, Project line 317). They differ only in placement: the skill opens a fourth `**Sub-pages**` group (line 64), and the Project puts the Open line under `**What a viewer sees**` (line 54). The slot at skill line 327 and Project line 303 lets either stand, so neither is a gap. Both carry every Requirements value and wrap only the numeral in the Free limit bullet ("`3` active links"), with the whole phrase in the quoted copy.
