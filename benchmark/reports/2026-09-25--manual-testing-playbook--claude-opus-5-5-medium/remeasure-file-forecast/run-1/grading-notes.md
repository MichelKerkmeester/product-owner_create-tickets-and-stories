# Grading notes, second remeasure round `remeasure-file-forecast/run-1`

Evidence behind every verdict in this folder's `results.csv`. The round reran the eight Project scenarios that still named a file for an artifact still to come in the first round, on Product Owner `b591571` and Barter `e9eec279`: skill 1.12.0, kernel v1.16.0 and playbook 2.1.1.0. Source and root lines cite that commit. One Opus 5.5 grader drafted the evidence, and the orchestrator reviewed it. Section 2 is the draft. Its draft rows show `after_failed_gate` unset, and `results.csv` holds the final rows.

---

## 1. Review

**Result.** Project 5 PASS and 3 FAIL. `PID-001` passes, so no row in this round carries `after_failed_gate` yes.

**The forecast repair held.** None of the eight replies attaches an `export/` path to the next artifact. Turn 1 now says, for example, "I'll write it once you reply" (`PID-001` line 33) or "Once you answer, I'll write the bug report" (`PBG-002` line 44). `PID-001`, `PBG-002`, `PTK-005`, `PEP-001` and `PEP-002` pass where the first round failed them.

**One reading decides `PST-003`.** Turn 1 line 42 says "I'll keep the draft's original filename". The draft grades it a file claim, since it names the file of an artifact still to come by reference. The Project's own naming rules give a refinement the source's file name as its label (kernel line 229, `export/[original-source-filename].md`, and Story Mode knowledge line 363), so the sentence may only restate the label convention. Every other clause of `PST-003` is met. The operator ruled on 2026-09-26 that the sentence is a file claim, so `PST-003` stays FAIL.

**Still failing.** `PST-004` Turn 1 settles the six-task split from the brief instead of asking for it, which the Pass clause and Story Mode knowledge line 382 require, and Turn 2 then follows the four named tasks. `PTK-006` still never marks `checkout_complete` as `deprecated`, and its task no longer names `booking-service`.

---

## 2. Grader draft

Batch: `PID-001`, `PBG-002`, `PTK-005`, `PTK-006`, `PST-003`, `PST-004`, `PEP-001` and `PEP-002`, all Project side, in the order the forecast brief lists them. Model `claude-opus-5-5-medium`. Run folder `<R2>` is `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/remeasure-file-forecast/run-1/`. Product Owner commit `b591571`, Barter commit `e9eec279`, playbook 2.1.1.0, skill 1.12.0, kernel v1.16.0. Graded read-only against `grading-brief.md`, `grading-brief-remeasure.md` and `grading-brief-forecast.md`.

### Handover verdict first

**PID-001 (Project handover): PASS.** Both replies open with a fenced block at line 1, then `Export-equivalent path:` in the task lane and the `HVR self-scan:` line, with no `Path:`, `Saved:` or `Verified:` line. The first round failed on `turn-1.md` line 48, "Once you answer, the task will be `export/002 - task-due-today-filter-chip.md`". That forecast is gone. Turn 1 now closes "I haven't drafted the task yet because `$task` needs your answers first. I'll write it once you reply." (`turn-1.md` line 33), which names neither a path nor a file. The task keeps every Turn 2 fact. No Project handover failure needs stating at the top of the run report for this round.

Identity split greps at `b591571`, run from `AI Systems/Product Owner/`:

| Grep | Expected | Observed |
|---|---|---|
| `grep -c "read-back succeeded" AGENTS.md` | `2`, exit `0` | `2`, exit `0` (lines 47 and 91) |
| `grep -c "read-back succeeded" "claude project/Custom Instructions.md"` | `0`, exit `1` | `0`, exit `1` |
| `grep -c "Canvas Artifact" AGENTS.md` | `0`, exit `1` | `0`, exit `1` |
| `grep -c "Canvas Artifact" "claude project/Custom Instructions.md"` | `4`, exit `0` | `4`, exit `0` (lines 76, 181, 221, 235) |

### Tally

| Runtime | PASS | FAIL | SKIP |
|---|---:|---:|---:|
| project | 5 (`PID-001`, `PBG-002`, `PTK-005`, `PEP-001`, `PEP-002`) | 3 (`PTK-006`, `PST-003`, `PST-004`) | 0 |
| skill | not in this round | | |

Against the first round: five fixed. `PST-003` still fails for the same cause, a Turn 1 file mention, in a softer form. `PTK-006` still fails on the missing `deprecated`, plus one new miss. `PST-004` still fails for the second of its two first-round causes, and its file promise is gone.

### The rule under test, reply by reply

Every forward statement about the artifact still to come, across all 16 replies, graded against the dividing line in `grading-brief-forecast.md` line 23 (an `export/` path or the word file attached to the next artifact is a claim, the next number alone is not):

| Scenario | Reply line | Forward statement | Graded |
|---|---|---|---|
| `PID-001` | `turn-1.md` 33 | "I'll write it once you reply." | Not a claim: no path, no file |
| `PID-001` | `turn-2.md` 64 | "Send me an answer for either one and I'll add it." | Not a claim |
| `PBG-002` | `turn-1.md` 44 | "Once you answer, I'll write the bug report." | Not a claim |
| `PTK-005` | `turn-1.md` 40 | "I'll write the Android subtask once you've answered." | Not a claim |
| `PTK-006` | `turn-1.md` 42 | "I'll write the task once you answer." | Not a claim |
| `PST-003` | `turn-1.md` 42 | "I'll keep the draft's original filename, and I'll list anything I add ..." | **Claim** (see `PST-003`) |
| `PST-004` | `turn-1.md` 65 | "Once you answer, I'll write the Story and its six tasks as one set under the next number." | Not a claim: next number only |
| `PEP-001` | `turn-1.md` 44 | "The Epic comes next once you answer." | Not a claim: the kernel line 228 wording |
| `PEP-002` | `turn-1.md` 33 | "I'll write the epic once you reply." | Not a claim |

No Turn 2 reply in the batch says anything about a file for its own or a later artifact. A grep of all 16 replies for `Path:`, `Saved:`, `Verified:`, `read-back`, `saved`, `save`, `write`, `file`, `filename` and `export/` outside the `Export-equivalent path:` lines finds no `Path:`, `Saved:`, `Verified:` or `read-back` at all. Beyond the lines above it finds only the attachment ("the Loomlist context file", "the company context file"), the user's own "Figma files" and "design files" (`PEP-001` `turn-1.md` line 31, `PEP-002` `turn-1.md` line 23), "write" about content rather than a file (for example `PBG-002` `turn-1.md` lines 12 and 17 "I'll write Not provided") and card-saving product copy in `PST-003`.

"I'll write the task" and its siblings promise the artifact and name no file. The Project's own Task Format Question opens "I'll create your task." (`Product Owner - Assets - Interactive Response Templates - v0.103.md` line 70), so they are graded not a claim.

### Method notes

- `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing and HEAD is `b591571`, so every source was read from the working tree. Root lines come from `git show b591571:sk-product-owner/manual-testing-playbook/manual-testing-playbook.md` (1,074 lines): verdict 150, clarification turns 154 to 159, rendering 163, export names 167 and 171, identity handover 179, invented fact 187, protected fact 188, file claim 189, HVR 190, Ticket realism 198 to 214. Kernel `claude project/Custom Instructions.md`: 85, 90, 101, 103, 108, 226, 228, 229, 233. `Product Owner - System - Interactive Mode - v0.407.md` line 70.
- `<R2>/run-status.json`: all eight `status ok`, one attempt, `turns_run 2`, `turns_declared 2`.
- Every `replies/<ID>-turn<n>.txt` is byte-identical to its `turn-<n>.md` (`cmp`, 16 of 16).
- Every `meta.json` shows empty ledgers on both turns and empty `net_file_changes`. Every session's init event lists only `Glob`, `Grep` and `Read`, and every result event is `success`.
- Block copies sit in `scratch/grades/blocks/forecast/<ID>-turn<n>-block<k>.md`: the body only, fence lines stripped. Every block is fenced (three backticks, or four in `PBG-002` Turn 2 and both `PST-003` turns) and opens its reply at line 1, except `PST-004` Turn 2 blocks 2 to 5, which follow the previous block's label as the bundle shape requires (kernel line 226). For a block at reply line 1, block line `k` is reply line `k + 1`. Each copy is byte-identical to the collector's copy under `AI Systems/Product Owner/export/benchmark/claude project/remeasure-file-forecast/run-1/` (`cmp`, 20 of 20).
- Format gate, `node validate-output-format.cjs --system product-owner <file>` from the Sync Loop folder on all 20 copies: 18 passed with exit 0. `PID-001-turn1-block1.md` line 9 "effort reporting, the sentence narrates the work instead of the finding" and `PTK-005-turn1-block1.md` lines 9, 13, 16 and 17 "bullet item ends with a full stop", both exit 1. No Pass clause names either finding, so both are advisory evidence.
- Line numbers are reply lines (`turn-<n>.md`) unless marked as block lines. There are no read-back tables, because all eight scenarios are Project side.
- First-round verdicts come from `<RUN>/remeasure-operator-repairs/run-1/results.csv`. Open readings carried from the first round keep their labels there (`RO-1`, `RO-5` of `remeasure-tasks.md`).

---

### PID-001 (project), Project identity handover

**Draft row**

```csv
PID-001,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Handover PASS: both replies open with a fenced block at line 1, then Export-equivalent path: in the task lane (turn-1.md line 29 with the -clarification name, turn-2.md line 45) and the HVR self-scan line, with no Path:, Saved: or Verified: line, and Turn 1 now closes ""I'll write it once you reply."" (line 33), naming no path or file. The task keeps every Turn 2 fact; advisory: a format gate effort-reporting hit at Turn 1 block line 9, a false positive on ""checked off""."
```

**Against the first round:** fixed. The first round failed on `turn-1.md` line 48 "Once you answer, the task will be `export/002 - task-due-today-filter-chip.md`". No reply in this round forecasts a path or a file.

**Pass clauses** (scenario line 35, read with root line 179)

| Clause | Result | Evidence |
|---|---|---|
| Both replies open with their rendered block | Met | `turn-1.md` line 1 opens ```` ```markdown ````, closing fence line 27. `turn-2.md` line 1, closing fence line 43. Form: fenced, nothing before either |
| `Export-equivalent path:` with a `task` lane name | Met | `turn-1.md` line 29 `export/001 - task-due-today-filter-chip-clarification.md`. `turn-2.md` line 45 `export/002 - task-due-today-filter-chip.md` |
| `-clarification` name on Turn 1 | Met | `turn-1.md` line 29 |
| `HVR self-scan:` line | Met | `turn-1.md` line 31, `turn-2.md` line 47 |
| Neither reply claims a file saved, written or read back, promises one or forecasts one (root line 179) | Met | `turn-1.md` line 33 "I'll write it once you reply." names the task only. `turn-2.md` line 64 "I'll add it" names no file. "file" appears only for the attachment (`turn-1.md` line 35, `turn-2.md` lines 56 to 58 and 62). No `Path:`, `Saved:` or `Verified:` |
| Turn 1 block holds only the question | Met | Reply lines 2 to 26: the Task Format Question opener "I'll create your task." (Interactive Response Templates line 70) and five question groups. The two suggested defaults (lines 10 and 20) sit inside questions and are named as suggestions at line 35 |
| Turn 2 task carries its H1, `### About` and `### Requirements` | Met | `turn-2.md` lines 2, 4 and 12, two numbered groups each with `**Checklist**` (22, 39) |
| Turn 2 facts intact | Met | Web only, Desktop through the web client, apps later (10, 31). Right after Overdue (24). Not checked off and due today in the owner's time zone (27). Sorted by due date (29). One active chip (26). `filter_selected` with `filter` set to `due_today` (41). Already in the tracking plan (37). Existing chip reused (25). No Figma and no dependency, and none is listed |
| No invented fact | Met | "All stays the default" (26) is `loomlist-context.md` line 163, "every to-do the member can open" (27) is line 56. Additions named at lines 55 to 58: the time zone item (30), the Overdue boundary (20) and the event properties (42) |
| No unfilled slot | Met | None in the task |
| `Canvas Artifact` not required | Not graded | Not printed, as allowed |
| Fail: `Path:`, `Saved:`, `Verified: read-back succeeded` or a local save | Not hit | None in either reply |
| Fail: a block missing or after other text | Not hit | Both blocks at line 1 |
| Fail: Turn 1 renders the task | Not hit | Line 33 "I haven't drafted the task yet" |
| Fail: iOS or Android scoped, "Due today" renamed, owner's time zone dropped | Not hit | Line 10 puts iOS and Android in later tasks. `Due today` throughout. Owner's time zone at 20, 27 and 30 |

**Blocking items hit**

None.

**Advisory items**

- Delivery shape: no commentary before either block, so the `PID-001` exception at root line 163 is not triggered.
- Format gate, Turn 1 block line 9 (reply line 10), effort reporting. The sentence is "I'd start from the Overdue rule: not checked off, with a due date equal to today ...". The gate matched "checked" in "checked off", a to-do state. `Product Owner - Rules - Conciseness - v0.100.md` line 75 leaves alone a sentence whose subject is the process documented, so this reads as a false positive. No Pass clause names it.
- Asking for a fact an attachment states (root line 211): line 11 asks "Does the one-active-chip rule still apply?", which `loomlist-context.md` line 163 states.
- Routing evidence: Turn 1 read the Interactive Mode and Interactive Response Templates knowledge but not Task Mode (`events-turn-1.jsonl` lines 8 to 19). The task lane shows in the label and in the Task Format Question shape. No Pass clause asks for the read.

**Realism entries**

- Block `PID-001-turn1-block1.md` (reply lines 2 to 26), task-lane clarification. Question alone: present. Facts: the three chips and one active at a time (11 vs `loomlist-context.md` 163); Web reaching Desktop with no Desktop release (6 vs 18); the six locales (21 vs 155); Data review before client work (20 vs 191); todos-service (19 vs 69). Placeholder: `{Platform}` in the proposed title `FE - {Platform} - TODO - Due today filter chip` (line 5) is the title pattern's own slot from `loomlist-context.md` line 104, quoted from an attached source and so exempt under root line 207. The task fills it as `Web`. 25 lines, no band. Format gate: effort reporting at line 9.
- Block `PID-001-turn2-block1.md` (reply lines 2 to 42), task. Routed template: `Product Owner - Templates - Task Mode - v0.305.md` lines 52 to 58 and the Canonical Task in `Product Owner - Assets - Task Templates - v0.102.md` line 19. Title, About and Requirements present. Facts: Desktop through the web client (10, 31 vs 18); the owner's time zone (20, 27 vs 157); the event properties (42 vs 187); the existing `filter` enum (37 vs 189); All as the default (26 vs 163). Placeholder: none. 41 lines against 30 to 70. Discipline code `FE`. Format gate: passed.

**Open readings**

- None decides `PID-001`. For the record: "I'll write it once you reply." (`turn-1.md` line 33) and "I'll add it" (`turn-2.md` line 64) promise the task, not a file, and are graded not a claim under the forecast brief's dividing line. If the operator reads kernel line 101's "will write" as covering any promise to produce the artifact, every scenario in this batch fails on the same kind of sentence, the Project's own template opener included.

---

### PBG-002 (project), Support ticket bug

**Draft row**

```csv
PBG-002,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 renders one fenced question block under export/001 - bug-android-confirmation-total-missing-city-tax-clarification.md (turn-1.md lines 1 to 27 and 29) and closes ""Once you answer, I'll write the bug report."" (line 44), naming no path or file, and Turn 2 renders a fenced bug with every amount adding up, the charge correct, Severity High, no device model, Frequency Always on the escalation's every-guest claim and the Android 8.12.1 Pay now scope (turn-2.md lines 2 to 91). Borderline: ""checked on 2026-09-26"" (line 41) for Turn 2's ""this morning""."
```

**Against the first round:** fixed. The first round failed on `turn-1.md` line 25 "Once you answer, I'll write the report under the next number in the bug lane (`export/002 - bug-...`)". This round drops the path.

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Met | Reply lines 2 to 26, seven groups in one message |
| Renders it as its own question-only block | Met | Fenced, lines 1 to 27, nothing before it |
| `Export-equivalent path:` under `bug` with `-clarification` | Met | Line 29 `export/001 - bug-android-confirmation-total-missing-city-tax-clarification.md` |
| `HVR self-scan:` line | Met | Line 31 |
| Drafts nothing | Met | Line 44. Block line 22 proposes a title inside a question only |
| Turn 2 renders one bug as its own block | Met | ````` ````markdown ````` lines 1 to 92, nothing before it |
| `Export-equivalent path:` under `bug`, `HVR self-scan:` | Met | Line 94 `export/002 - bug-android-confirmation-total-missing-city-tax.md`, line 96 |
| Claims no file on either turn | Met | `turn-1.md` line 44 names no path or file. Lines 12 and 17 "I'll write Not provided" name a field value. Turn 2 has no file wording |
| Every required template section | Met | Title 2, `### About` 4, field table 10 to 18, References 20 to 23, `### Bug` 27, Observed 31, Steps 47 to 53, Screen recording 57, Expected 61, Checklist 71 to 75, optional BDD 79. The error-message line is left out, as ruling 6 and `Product Owner - Assets - Bug Report Template - v0.101.md` line 85 allow |
| Ticket `58213`, `RS-7Q4K2M`, Android `8.12.1`, `Pay now` | Met | 8, 23, 57; 23, 37, 38, 65; 8, 42, 48; 8, 12, 35 |
| "Total €387.00" against `€405.00` and the `€18.00` city tax | Met | Line 37 |
| Severity `High` | Met | Line 13 |
| No device model | Met | Line 15 "Guest's phone not provided, Guest Support Android test phone (model not provided)" |
| Every other amount exact and adding up | Met | Line 39: €270.00 at the payment step, Total €258.00, charge €270.00. Line 40: €135.00 = €129.00 + €6.00. Line 41: iOS €405.00. Line 52: €258.00 against €270.00, leaving out €12.00 (ticket line 55). Line 48: €3.00. BDD lines 84, 86 and 91 |
| Charge correct, Android confirmation total the defect | Met | Line 38 "The charge is correct, and only the confirmation screen is wrong" |
| Scope held to Android `8.12.1` Pay now, 2 nights or more | Met | Lines 8, 12 and 35 |
| No claim that 1 night, iOS `8.12.0` or web is wrong | Met | Lines 40, 41 and 68 |
| Fail: overcharged or charge wrong | Not hit | Line 8 "Guests read the difference as an overcharge" reports the guests' reading |
| Fail: Pay at property stated either way | Not hit | Line 43 "Pay at property bookings were not tested, and no guest has reported the problem on one yet" (ticket line 61) |
| Fail: Frequency from the 14 chats | Not hit | Line 12 `Always, for Pay now stays of 2 nights or more (per the Guest Support escalation)` rests on ticket line 66 "Every Pay now guest on Android with a stay of 2 nights or more". The chats stay in Observed (42), and line 101 gives the reasoning |
| Fail: invented device, cause or step | Not hit | No cause (line 98). Steps 48 to 53 follow Maren's 2-night test, test card included (ticket lines 53 and 55) |
| Fail: unfilled slot | Not hit | None |

**Blocking items hit**

None.

**Advisory items**

- Asking for a fact an attachment states (root line 211): `turn-1.md` line 13 asks whether the severity is High, and ticket line 10 gives Priority High.
- Borderline, never decides alone: line 41 "checked on 2026-09-26" turns Turn 2's "this morning" into a date, as the first round recorded.
- Borderline, never decides alone: line 43 "Tested only with EUR, the en-GB app language" and line 104. en-GB is the guest's app language (ticket line 16), and the test phone's language is not stated.
- Named additions at lines 100 to 109: the 1-night BDD scenario and the Guest Support handling note.
- Size: 90 block lines, inside 60 to 110. Discipline code `FE`.

**Realism entries**

- Block `PBG-002-turn1-block1.md` (reply lines 2 to 26), bug-lane clarification. Question alone: present. Facts: the confirmation screen shows reference, dates, guests and total (9 vs `roamstay-context.md` 154); 14 chats, all Android 8.12.1 Pay now stays of 2 nights or more (5, 14 vs ticket 61); Android 8.11.2 as the previous train (18 vs `roamstay-context.md` 110); the title pattern and `BOOK` (22 vs `roamstay-context.md` 83 and 93); city tax per adult per night, EUR, en-GB (26 vs ticket 15 and 16). Placeholder: none. 25 lines, no band. Format gate: passed.
- Block `PBG-002-turn2-block1.md` (reply lines 2 to 91), bug. Routed template: the Project Bug Report Template (lines 44 to 95) and `Product Owner - Templates - Bug Mode - v0.204.md` lines 110 to 118. Every required section present. Facts: property 40217 at €3.00 per adult per night (37, 48 vs ticket 15); the email Total €405.00 (38 vs ticket 50); the staged rollout reaching all users on 2026-09-21 (42 vs ticket 66, `roamstay-context.md` 112); test bookings cancelled inside free cancellation (55 vs ticket 58); the workaround (45 vs ticket 68); the guest's words (69 vs ticket 34). Placeholder: none (`Not provided` is exempt). 90 lines against 60 to 110. Discipline code `FE`. Format gate: passed.

**Open readings**

- None beyond the first round's date-conversion question ("this morning" written as a calendar date).

---

### PTK-005 (project), Supplied parent subtask

**Draft row**

```csv
PTK-005,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 renders one fenced question block under export/001 - task-android-recurring-todos-clarification.md and closes ""I'll write the Android subtask once you've answered."" (turn-1.md line 40), and Turn 2 renders one fenced subtask naming FS - TODO - Recurring to-dos (line 26) with every shared-rule value, Android only and every Turn 2 fact, with no file wording anywhere. Advisory: 158 block lines against 60 to 130, four bullet full stops in the Turn 1 block, and the reminder is never framed as an Android local notification (Expected signals only)."
```

**Against the first round:** fixed. The first round failed on `turn-2.md` line 166 "Answer any of these and I'll update the same file." This round's Turn 2 closes on the ClickUp connector line (181) and says nothing about a file.

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question rendered as its own block | Met | Fenced, lines 1 to 26 |
| Export-equivalent `task` lane `-clarification` label, `HVR self-scan:` | Met | Line 28 `export/001 - task-android-recurring-todos-clarification.md`, line 30 |
| Renders no subtask | Met | Questions only. Line 40 |
| Turn 2 renders one subtask block under a `task` label with `HVR self-scan:` | Met | Fenced, lines 1 to 160. Line 162 `export/002 - task-android-recurring-todos.md`, line 164 |
| No file claim | Met | `turn-1.md` line 40 and `turn-2.md` lines 166 to 181 name no path or file. "the board context page" (169) is the attachment |
| H1, `### About`, `### Requirements` with checklisted groups | Met | Lines 2, 4 and 36. Area headings 40, 73, 105 and 145. Groups 1 to 8, each with `**Checklist**` (50, 64, 83, 98, 115, 126, 137, 155) |
| Parent named as `FS - TODO - Recurring to-dos` | Met | `**Parent task**` block lines 22 to 26 as backticked plain text, and About line 8 |
| `Daily`, `Weekdays`, `Weekly`, `Monthly`, `Custom` | Met | Line 54 |
| `1 to 99` | Met | Line 55 "with N from 1 to 99" |
| `Never`, `On date`, `After` | Met | Line 66 |
| `365` | Met | Line 69 "from 1 to 365" |
| `Skip this one` | Met | Lines 88, 89, 139 and 158 |
| `500` | Met | Lines 113 and 118 |
| `recurring_todos` | Met | Lines 10, 135, 139 and 140 |
| `owner's time zone` | Met | Line 96 "the to-do owner's time zone" |
| As the parent gives them | Met | Sheet copy (118) matches parent line 91. Plus badge and upgrade sheet (129) match parent line 103. Reassignment (101) matches parent line 97 |
| Android the only client in scope | Met | iOS and Web appear only as Related tasks (32, 33) and in the flag note (10) |
| Every Turn 2 fact | Met | The Android entry (title, line 2), phones and tablets (8, 140), Oskar's team and 5.4.0 (10, 135), the engine built in parallel and the next due date from the back end, never worked out on the device (10, 56, 85, 90) |
| Fail: parent dropped or linked to an invented URL | Not hit | No URL |
| Fail: iOS, web, Desktop or engine work | Not hit | None scoped |
| Fail: the app works out the next due date | Not hit | Line 56 |
| Fail: an option, range, limit, sheet copy or plan rule changed | Not hit | All as the parent gives them |
| Fail: an unnamed Android requirement | Not hit | Android 9 (141), flag off (139), event properties (159) and the 31st check (90) are named at lines 168 to 172 |
| Fail: a template slot | Not hit | None |

**Blocking items hit**

None.

**Advisory items**

- Size: 158 block lines against 60 to 130.
- Format gate, Turn 1 block lines 9, 13, 16 and 17 (reply lines 10, 14, 17 and 18): bullet items end with a full stop. `Product Owner - Rules - Human Voice Core - v0.100.md` line 35 bans that shape, and the Turn 1 `HVR self-scan:` line reads "0 hard blockers" (line 30). Recorded the way the first round recorded `PEP-001`'s bullet full stops. See Open readings.
- Asking for a fact an attachment states (root line 211): `turn-1.md` line 5 asks whether to keep the title and parent as written (parent lines 1 and 37).
- Borderline, never decides alone: line 48 "because the engine counts every next due date from the current one" is an unrequested reason that sits uneasily beside parent line 69 "Monthly keeps to the day of the first due date".
- A parent detail left out, not changed: Skip this one "still counts toward an After limit" (parent line 85) is not carried.

**Realism entries**

- Block `PTK-005-turn1-block1.md` (reply lines 2 to 25), task-lane clarification. Question alone: present. Facts: `BE - TODO - Recurrence engine` (7 vs parent 49); reminders as local notifications (10 vs `loomlist-context.md` 77); no offline mode and retries until the app closes (12 vs 175 and 176); billing changes on Web only (11 vs 13); Ines last editing the parent on 2026-09-18 (25 vs parent 3). Placeholder: none. 24 lines, no band. Format gate: four bullet full stops.
- Block `PTK-005-turn2-block1.md` (reply lines 2 to 159), subtask. Routed template: the Subtask template, `Product Owner - Assets - Task Templates - v0.102.md` line 195. Title, About, References, area headings and numbered groups present. Facts: the 31st example (90 vs parent 69); reassignment to a new owner's zone (101 vs parent 97); Yara's review on 2026-09-16 (153 vs parent 109); Android 9 as the minimum OS (141 vs `loomlist-context.md` 133); `user_id` hashed before it leaves the device (159 vs 188); the three flows (18 to 20 vs parent 19 to 21). Placeholder: none. 158 lines against 60 to 130. Title code `FE - Android - TODO`. Format gate: passed.

**Open readings**

- The Expected signals (scenario line 36) and Test Execution Expected (line 66) have the carried-over reminder become a local notification that Android schedules from the UTC time reminders-service hands over (`loomlist-context.md` line 77). The block never says so. It carries only the parent's rule (86 and 87). The Pass/fail bullet (line 39) does not list it, so it is graded not decisive. Question: is that framing part of "the shared rules ... as the parent gives them"?
- Does an `HVR self-scan: 0 hard blockers` line on a clarification block with four bullet full stops count as "a count that was never taken" (root line 190, kernel line 103)? Graded no: the count was reported, and a gate finding decides only through a Pass clause (brief section 2). If yes, `PTK-005` fails.

---

### PTK-006 (project), Data tracking task

**Draft row**

```csv
PTK-006,project,claude-opus-5-5-medium,FAIL,2,2,pending,no,"The Turn 2 block still never marks `checkout_complete` as `deprecated` (removal only, turn-2.md lines 10, 75, 79 and 80) and now never names `booking-service` as the sender of `booking_confirmed` (source server only, line 33), two missed backticked Pass-clause values. Fixed since the first round: `date_changed` reads ""still proposed"" (line 12), and neither reply names a file (turn-1.md line 42 ""I'll write the task once you answer."")."
```

**Against the first round:** still failing for the same cause, the missing `deprecated`, plus a new miss, `booking-service`. Two first-round misses are fixed: `proposed` now appears (line 12), and the Turn 2 promise "I'll update the task under the same filename" is gone.

**The check asked for.** A case-insensitive grep for `deprecat` over both replies and both block copies finds nothing. The block describes the status without the plan's word: "keeps firing next to `booking_confirmed` until its removal date ... From 2026-11-01 `events-collector` drops it" (line 75), against plan line 25 `deprecated, removal on 2026-11-01` and the status key at plan line 28.

**Pass clauses** (scenario line 39)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 routes to Task Mode | Met | Turn 1 reads Task Mode, Task Templates and the Router Contract (`events-turn-1.jsonl` lines 13, 15, 17). Task-lane label at line 32. Line 36 "Your request clearly asks for a task" |
| Asks one question rendered as its own block | Met | Fenced, lines 1 to 30 |
| Export-equivalent `task` lane `-clarification` label, `HVR self-scan:` | Met | Line 32 `export/001 - task-booking-funnel-events-clarification.md`, line 34 |
| Renders no task | Met | Questions only |
| Turn 2 renders one task block under a `task` label with `HVR self-scan:` | Met | Fenced, lines 1 to 83. Line 85 `export/002 - task-booking-funnel-tracking-rollout.md`, line 87 |
| No file claim | Met | `turn-1.md` line 29 "I'll name the tracking plan in plain text" and line 42 name no file. `turn-2.md` lines 89 to 107 have no file wording |
| H1, `### About`, `### Requirements` with checklisted groups | Met | Lines 2, 4 and 20. Group 1 splits its `- [ ]` items under `**Every event**`, `**By step**` and `**booking_confirmed**` (30, 38, 49). Groups 2 and 3 use `**Checklist**` (64, 77) |
| The six funnel events as the plan names them | Met | Line 67 |
| `booking_confirmed` from `booking-service` with `source` set to `server` | **Unmet** | Line 33 "`source` is `client` on client events and `server` on `booking_confirmed`". Line 51 fires it when a booking leaves `payment_pending`. `booking-service` appears nowhere in the Turn 2 reply (it appears only in the Turn 1 question, line 11). Plan lines 24 and 55 |
| `total_amount_minor` in minor units | Met | Line 44 |
| `checkout_complete` marked `deprecated` with its removal on `2026-11-01` | **Unmet** | The removal date is at 10, 62, 69, 71, 75, 79 and 80. The word `deprecated` is absent |
| `date_changed` kept `proposed` and unbuilt | Met | Line 12 "`date_changed` is still proposed in the plan, so it stays out of this task" |
| Every Turn 2 fact | Met, borderline | `DATA` and `TRK` in the title (2). The Data team's part (10). Checks in `events-collector` as the squads ship (10, 28). The dashboard move (58 to 69). The drop on the removal date (71 to 82). FE and BE in separate tasks (12). The event table unchanged at refinement (10, "refinement closed with no change to its event table"). Nadia is not named as the checker (`RO-5`) |
| Fail: `date_changed` built or given properties | Not hit | Line 12 |
| Fail: `checkout_complete` kept past its date or dropped early | Not hit | Lines 79 and 80 |
| Fail: bookings counted from `payment_submitted` or `checkout_complete` | Not hit | Lines 47 and 66 |
| Fail: `booking_confirmed` sent from a client | Not hit | Line 33 |
| Fail: money as decimals or without city tax | Not hit | Line 44 |
| Fail: FE or BE build inside the task | Not hit | Line 12 |
| Fail: a template slot | Not hit | None |

**Blocking items hit**

- Pass clause missed (root line 150): `checkout_complete` is never marked `deprecated`. The plan's status reaches the task only as a description, a supplied value generalized (root line 188).
- Pass clause missed (root line 150): `booking-service` never appears as the sender of `booking_confirmed`.

**Advisory items**

- Named additions at `turn-2.md` lines 98 to 105.
- Group 1 has no `**Checklist**` label. `Product Owner - Templates - Task Mode - v0.305.md` lines 84 to 89 make the label a "should" pattern, and lines 54 to 58 require only Title, About and Requirements, so it is not a missing required section.
- Line 96 names the refinement-date conflict (Turn 2 "yesterday" against the plan's 2026-09-24) and leaves the date out rather than resolving it silently.
- Borderline, never decides alone: line 80 extends the drop to "from the web", where plan line 56 says "whatever app version sends it".
- Size: 81 block lines, inside 60 to 140.

**Realism entries**

- Block `PTK-006-turn1-block1.md` (reply lines 2 to 29), task-lane clarification. Question alone: present. Facts: the three owners (10 to 12 vs plan 75 to 77); draft v0.3 and the refinement on 2026-09-24 (16 vs plan 1 and 5); the `date_changed` open point (20 vs plan 65); the Android `room_selected` timing (24 vs plan 67 to 71); the drop on 2026-11-01 (28 vs plan 56). Placeholder: none. 28 lines, no band. Format gate: passed.
- Block `PTK-006-turn2-block1.md` (reply lines 2 to 82), task. Routed template: the Canonical Task, `Product Owner - Assets - Task Templates - v0.102.md` line 19. Title, About, References and Requirements present. Facts: the `RS-` reference format (54 vs `roamstay-context.md` 47); the 30-minute `payment_pending` expiry (52 vs 148); no currency conversion (68 vs 118); the two-week release train (28 vs 110); the Monday-to-Thursday nights example (35 vs 38); the plan's three problems (8 vs plan 11 to 13). Missing: `deprecated` (plan 25) and `booking-service` (plan 24 and 55). Placeholder: none. 81 lines against 60 to 140. Title code `DATA`. Format gate: passed.

**Open readings**

- `RO-1`, carried: does a status or a service given in other words count as verbatim? Line 75 describes `deprecated`, and line 33 implies the server sender without naming `booking-service`. Graded Unmet, as in the main run and the first round. Under the lenient reading `PTK-006` passes, because every other clause is met.
- `RO-5`, carried: Nadia is not named as the one who checks the events. Not decisive.

---

### PST-003 (project), Story refinement

**Draft row**

```csv
PST-003,project,claude-opus-5-5-medium,FAIL,2,2,pending,no,"File claim under root line 189 and kernel lines 101 and 228: turn-1.md line 42 promises ""I'll keep the draft's original filename"" for the Story still to come, which attaches the word file to the next artifact under the forecast brief's dividing line. Turn 2 otherwise meets every clause under Export-equivalent path export/fernhouse-save-card-draft.md (turn-2.md line 148); advisory: 144 block lines against 70 to 130."
```

**Against the first round:** still failing for the same cause, a Turn 1 file mention about the refinement, in a softer form. The first round's "It will save as `export/fernhouse-save-card-draft.md`" became "I'll keep the draft's original filename". The path and the word "save" are gone, but the file is still named.

**The line the orchestrator asked about.** `turn-1.md` line 42, after the clarification block and its label, reads: "Once you answer, I'll restructure the draft into the house Story format. I'll keep the draft's original filename, and I'll list anything I add that isn't in Priya's draft so you can remove it." Graded a claim, for these reasons:

1. The dividing line in `grading-brief-forecast.md` line 23 makes a forward statement a claim when it attaches "an `export/` path or the word file to the next artifact". This sentence is forward ("I'll keep"), and it attaches "filename", which carries the word file, to the refinement still to come.
2. "The draft's original filename" resolves to exactly one name, `fernhouse-save-card-draft.md`, the basename of `context/fernhouse-save-card-draft.md`. So it forecasts the next artifact's file name by reference, where the first round spelled it out.
3. Kernel line 101 bars "a path or file for an artifact still to come". Kernel line 228 and Interactive Mode line 70 let the reply say "the artifact comes next once the user answers, without naming the artifact's path or file". The first sentence of line 42 does exactly what those lines allow. The second adds the file.
4. It is not the label of the block rendered in that reply. That label is `export/NNN - Story-save-card-for-next-time-clarification.md` (line 33), which is never a claim.

The other reading is under Open readings. Under it, `PST-003` passes.

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one consolidated Story question | Met | Reply lines 2 to 30, six groups in one message |
| Its own block, a Story-lane `Export-equivalent path:`, `HVR self-scan:` | Met | Fenced (````` ````markdown `````), lines 1 to 31. Line 33 `export/NNN - Story-save-card-for-next-time-clarification.md`: `NNN` is the Project's placeholder slot (kernel line 233, root lines 167 and 207). Line 35 |
| Renders no draft | Met | Line 37 "I haven't drafted the Story yet" |
| Turn 2 renders one refined Story block with `Export-equivalent path: export/fernhouse-save-card-draft.md` | Met | Fenced, lines 1 to 146. Line 148 |
| Names the Story kind | Met | Line 152 "into a house **Story**" |
| `HVR self-scan:` line | Met | Line 150 |
| Claims no file | **Unmet** | Turn 2 has no file wording. Turn 1 line 42 "I'll keep the draft's original filename". Root line 189 covers any file claim on the Project side, on either turn |
| H1 with no `PRD -` prefix | Met | Line 2 `# Customer - Checkout - Save card for next time` |
| No `**Checklist**` and no `- [ ]` build item in Requirements | Met | Requirements, lines 28 to 58 |
| The checklist's content as bold-lead constraint groups | Met | The sixth card refused (35), the stored fields (37), `Remove this card?` (52), `**Tracking**` (54 to 57) |
| `## Acceptance criteria`, numbered Given/When/Then, each closed by Mark-as-done | Met | Criteria 1 to 6 at 67, 76, 87, 96, 105 and 115, Mark-as-done at 74, 83, 94, 103, 111 and 121. Saving (1), paying (3), removing (6), guest checkout (1, line 72), a declined saved card (5) |
| `Save this card for next time`, `unchecked by default` | Met | Line 32 |
| `You can save up to 5 cards` | Met | Line 34 |
| `Card ending 7031`, `Expires 08/28` | Met | Line 43 |
| `CVC`, `€150`, `£130` | Met | Lines 44 and 45 |
| `Account > Payment methods` | Met | Line 51 |
| `Remove this card?` | Met | Line 52 |
| `guest checkout` | Met | Line 33 "Saving is not available in guest checkout", and line 143 |
| The Turn 2 copy | Met | Line 47 `This card was declined. Choose another card or enter a new one.` |
| The order-total rule for the CVC limits | Met | Line 45 "The `€150` and `£130` limits apply to the order total including shipping" |
| Fail: a numbered `Story-` label | Not hit | Line 148 |
| Fail: the `PRD -` H1 or the build checklist kept | Not hit | Lines 2, 28 to 58 |
| Fail: a value dropped or rewritten | Not hit | All values verbatim |
| Fail: `TBD...` for the declined copy | Not hit | `TBD...` appears only in Estimation (131) |
| Fail: invented event names, card brands or a stored field | Not hit | Events left unnamed (56). The stored fields (37) are fewer than the draft's, not more (see Open readings) |
| Fail: ticket header fields or story points | Not hit | None |
| Fail: a local save claimed | Hit | Turn 1 line 42, on the reading above |

**Blocking items hit**

- File claim on the Project side (root line 189, kernel lines 101 and 228, Interactive Mode line 70): `turn-1.md` line 42 names the file of the artifact still to come.

**Advisory items**

- Size: 144 block lines against 70 to 130.
- Named changes at `turn-2.md` lines 154 to 164.
- `## Delivery` is forced by the `**Open:**` line (41), as `Product Owner - Templates - Story Mode - v0.403.md` line 132 allows. `TBD...` in Estimation is the exempt slot.

**Realism entries**

- Block `PST-003-turn1-block1.md` (reply lines 2 to 30), Story-lane clarification. Question alone: present. Facts: the card data rule (10 vs `fernhouse-context.md` 153); `object_action` names and the tracking plan row before FE work (15 vs 161 and 164); the Story title shape (5 vs 95); the draft's export line (6 vs draft line 1). Placeholder: `TBD...` at line 18 is quoted from draft line 56, exempt. 29 lines, no band. Format gate: passed.
- Block `PST-003-turn2-block1.md` (reply lines 2 to 145), Story refinement. Routed template: `Product Owner - Assets - Story Template - v0.100.md`. Preamble (5, 6), About (8), Problem (12), Solution (16), Expected outcomes (20), Requirements (28) and Acceptance criteria (61) present, with Delivery (125). Facts: the H1 shape (2 vs `fernhouse-context.md` 95); the stored fields (37 vs 153); the tracking plan row and DATA task (57 vs 164); 68% of app orders from returning customers (14 vs 18 and draft 15); 17% and 9% unaltered (14 vs draft 15). Placeholder: none beyond the exempt `TBD...`. 144 lines against 70 to 130. Format gate: passed.

**Open readings**

- **Decides the verdict.** Is "I'll keep the draft's original filename" (`turn-1.md` line 42) a file claim? Graded yes, for the four reasons above. The other reading takes "filename" as the name of the refinement's label convention rather than a file. The Project's own text phrases that convention with the same word: kernel line 229 `export/[original-source-filename].md`, and `Product Owner - Templates - Story Mode - v0.403.md` line 370 "a refined Story keeps its source filename". The sentence also promises no write or save and gives no `export/` path. Under that reading `PST-003` passes, because every other clause is met.
- `facts_intact` is `no` for the same unruled reading as the main run and the first round. The draft stores "token, brand, last four and expiry only" (draft line 48), and the Story stores "the payment provider's card token, the last four digits and the expiry date, and nothing else" (line 37). The Turn 1 question on the conflict (lines 8 to 11) went unanswered. The change is disclosed at line 155 and kept open at lines 41 and 137, so it is not a silent resolution (root line 188). Not decisive.

---

### PST-004 (project), Story with nested tasks

**Draft row**

```csv
PST-004,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 again settles the split instead of asking for it: ""I'll write the Story with its six tasks, split the way Hamid's brief lists them"" (turn-1.md line 4), and none of the eleven questions asks which tasks to make, so the one Story question misses the task split the request never named (knowledge Story Mode line 382). The file promise is gone (line 65 names only the next number), and Turn 2 renders the Story and exactly the four named tasks in order under export/002 - Story-order-tracking/."
```

**Against the first round:** still failing for the same cause, the second of the first round's two: the split is announced, not asked. The first cause is fixed. The first round's "The Story and task files will go under the next number, in `export/002 - Story-order-tracking/`" became "Once you answer, I'll write the Story and its six tasks as one set under the next number." (line 65), which names the next number only.

**The two points the orchestrator asked about.**

- Turn 1 still asks one consolidated Story question: one message, eleven numbered items, in the Story lane. It does not ask for the split. Block line 3 (reply line 4) fixes it as "the Story with its six tasks, split the way Hamid's brief lists them", and line 56 repeats "this is a **Story** with its six tasks under it". Item 6 (lines 28 to 31) asks only whether `FE - Web` goes in now or waits for the web design. Item 7 (line 36) speaks of "the DATA task" as settled. Both presuppose the brief's six and ask nothing about which tasks to make or in what order. The Expected signals (scenario line 32), the conversation chain (line 42) and `Product Owner - Templates - Story Mode - v0.403.md` line 382 have this question ask for the split when the request names none.
- Turn 2 follows the four named tasks exactly: FE iOS, FE Android, FE web, then the BE tracking webhook, with no `Packed` and no DATA task (reply line 481 "your four tasks in the order you gave").

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one consolidated Story question in the Story lane | **Unmet** | One message in the Story lane, but no item asks for the task split, and line 4 settles it as the brief's six. See the two points above |
| Its own block, `Export-equivalent path:` outside any folder, `HVR self-scan:` | Met | Fenced, lines 1 to 50. Line 52 `export/001 - Story-order-tracking-clarification.md`. Line 54 |
| Renders no draft | Met | No Story or task block on Turn 1 |
| Turn 2: one block per file, Story first, then exactly four task blocks in the named order | Met | Story 1 to 182, iOS 186 to 252, Android 256 to 322, web 326 to 392, BE 396 to 475 |
| Each followed by its own `Export-equivalent path:` inside `export/[NNN] - Story-[description]/` | Met | Lines 184, 254, 324, 394 and 477, all under `export/002 - Story-order-tracking/`, `002` then `002.1` to `002.4` |
| One `HVR self-scan:` line for the set | Met | Line 479 |
| Names the Story kind | Met | Line 481 "I've written the Story and your four tasks" |
| Claims no file | Met | `turn-1.md` line 65 names only the next number. `turn-2.md` lines 481 to 497 have no file wording. "the company context file" (488) is the attachment |
| Story holds About, Problem, Solution, Expected outcomes | Met | Lines 8, 12, 16 and 20 |
| `#### **Tasks**` inside About, one bullet per task in order, each linking `(<[NNN].[n] - task-[description].md>)` | Met | Lines 25 to 30, `(<002.1 - task-ios-order-tracking-timeline.md>)` to `(<002.4 - task-carrier-tracking-webhook.md>)` |
| Requirements | Met | Line 34 |
| Numbered Given/When/Then criteria, each closed by Mark-as-done | Met | Criteria 1 to 7 at 92, 101, 110, 119, 128, 138 and 147, Mark-as-done at 99, 108, 117, 126, 134, 145 and 153 |
| Each task holds `### About`, a `**Story**` block linking `(<[NNN] - Story-[description].md>)`, no `**Parent task**`, `### Requirements` | Met | iOS 189, 195 to 199, 209. Android 259, 265 to 269, 279. Web 329, 335 to 339, 349. BE 399, 405 to 409, 419 |
| The six statuses | Met | Lines 39 to 44, and each FE task (223, 293, 363) |
| The five carrier codes | Met | Lines 41 to 44, BE task 446 to 449 |
| `Arriving Thursday 1 October`, `Between 10:00 and 14:00` | Met | Line 54, and lines 237, 307 and 377 |
| `90 days` | Met | Lines 66 and 67, 251, 321, 391, 473 |
| `30 kg`, `120 cm` | Met | Line 61 |
| `tracking.updated`, `/webhooks/carrier/tracking` | Met | Lines 75 and 431 |
| `event_id` | Met | Lines 79 and 435 |
| `X-Carrier-Signature` | Met | Lines 76 and 432 |
| `occurred_at` | Met | Lines 56, 80, 81, 461 to 463 |
| `eta_window` | Met | Lines 51, 53, 55 and 56 |
| `5 attempts`, `1 min, 5 min, 15 min, 1 h, 6 h` | Met | Line 78 (the Pass clause asks the set) |
| Fail: drafts in Turn 1, `intake` label, label inside the folder | Not hit | Lines 52 and 65 |
| Fail: a `Packed` or DATA task, one of the four dropped or reordered | Not hit | Lines 27 to 30 |
| Fail: merged block, flat labels or two numbers | Not hit | Five blocks, one folder, one number |
| Fail: tasks under `## Scope`, `**Parent task**`, an epic nobody supplied | Not hit | None |
| Fail: a reason for `Delivery failed`, a guessed estimate | Not hit | Lines 44, 55 and 179 |
| Fail: invented event names, polling, a tracking-history call or pallet tracking | Not hit | Lines 170 and 427 state that `GET /v1/shipments/{shipment_id}` returns label fields only (carrier notes line 48). Line 61 keeps pallet items without tracking |
| Fail: a status, code or value rewritten | Not hit | All verbatim |

**Blocking items hit**

- Pass clause missed (root line 150): the Turn 1 Story question does not ask for the task split the request never named (scenario lines 32 and 42, `Product Owner - Templates - Story Mode - v0.403.md` line 382).

**Advisory items**

- Size: the Story block is 180 lines against 80 to 150. The task blocks are 65, 65, 65 and 78 lines, inside 35 to 90.
- The BE webhook task does not carry `5 attempts` or the retry schedule. The Story carries them (line 78) and the Pass clause asks the set, but the Expected signals (scenario line 32) place them in the BE task.
- Named additions at `turn-2.md` lines 485 to 489, and choices on unanswered questions at 490 to 495.
- Block form: fenced, all six blocks.

**Realism entries**

- Block `PST-004-turn1-block1.md` (reply lines 2 to 49), Story-lane clarification. Question alone: present. Facts: the four `exception_code` values (7 vs carrier notes 29); the parcel-point `DL` (16 vs 31); no tracking history (21 vs 48); the webhook on shipping-service and status in orders-service (25 vs carrier notes 7, `fernhouse-context.md` 64); the `eta_window` offsets (39 vs carrier notes 17); guests with no order history (46 vs `fernhouse-context.md` 35). Placeholder: none. 48 lines, no band. Format gate: passed.
- Block `PST-004-turn2-block1.md` (reply lines 2 to 181), Story. Routed template: `Product Owner - Assets - Story Template - v0.100.md` with the bundle rules at Story Mode knowledge lines 370 to 392. Required sections and the Tasks block present. Facts: 5,870 of 18,940, 31% (14 vs brief 7); 31% to under 20% within two months (22 vs brief 65); the six locales (47 vs `fernhouse-context.md` 128 to 132); about 43,000 events on a peak day (82 vs carrier notes 52); the signature (76 vs 43); `5 seconds` (77 vs 44). Placeholder: none beyond the exempt `TBD...`. 180 lines against 80 to 150. Format gate: passed.
- Blocks `PST-004-turn2-block2.md` to `block4.md` (reply lines 187 to 251, 257 to 321, 327 to 391), FE tasks. Routed template: the Canonical Task in `Product Owner - Assets - Task Templates - v0.102.md`, with About, Story, Related tasks and Requirements. Facts: `TRACK` (title vs `fernhouse-context.md` 105); the surface segment (title vs 93); the pallet line (250 vs brief 42); `90 days` (251 vs brief 41); the web layout in the same frame (333 vs Turn 2). 65 lines each, inside 35 to 90. Title codes `FE - iOS - TRACK`, `FE - Android - TRACK`, `FE - Web - TRACK`. Format gate: passed.
- Block `PST-004-turn2-block5.md` (reply lines 397 to 474), BE task. Facts: `event_id` the same on every retry (435 vs carrier notes 11); late `IT` after `OD` (457 vs 35); the guide version 2.4 and the 2026-09-19 call (403 vs 3); 5,400 parcels at 5 to 8 events (436 vs 52); `Packed` already in orders-service (403 vs Turn 2). 78 lines, inside 35 to 90. Title code `BE - TRACK`. Format gate: passed.

**Open readings**

- Is the brief's list of six expected tasks "a split the request names" under knowledge line 382? Graded no, as in the first round: the request is the user's prompt, which says only "Please break it into tasks". If the brief's list counts as named, it is authoritative, Turn 1 needs no split question, and `PST-004` passes on every other clause.

---

### PEP-001 (project), Epic from strategy brief

**Draft row**

```csv
PEP-001,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 renders one fenced Epic question under export/001 - Epic-partner-hub-self-onboarding-clarification.md and closes ""The Epic comes next once you answer."" (turn-1.md line 44), the kernel line 228 wording with no path or file, and Turn 2 renders a fenced Epic with the six stage names as plain-text child stories, the channel manager under Added Later, the five brief values verbatim and References omitted as no link was supplied. Advisory: 142 block lines inside 90 to 150, no format gate finding."
```

**Against the first round:** fixed. The first round failed on `turn-1.md` line 39 "Once you reply, I'll write the epic as `export/002 - Epic-partner-hub-self-onboarding.md`."

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one Epic question in the Epic lane and drafts nothing | Met | Fenced, lines 1 to 32. Line 34 `export/001 - Epic-partner-hub-self-onboarding-clarification.md`. `HVR self-scan:` line 36. Line 38 "I haven't drafted anything yet" |
| Turn 2 renders one Epic with a `# Epic - ` H1 and no story preamble | Met | Fenced, lines 1 to 144. Line 2 `# Epic - Partner Hub - Self-onboarding`, then `* * *` and `## About` (5). No preamble |
| `## About` holding `### Problem`, `### Goal`, `### Solution` | Met | Lines 10, 22 and 40 |
| `#### **References**` only when a link is supplied | Met | Omitted. Line 150 "no References section, because you haven't shared any links" |
| `## Scope` naming exactly six child stories as plain text, one per stage name verbatim | Met | Lines 54 to 58 and 62: Sign-up and verification, Property profile and photos, Rooms and rates setup, Policies and city tax, Payout details and identity checks, Go-live review queue (brief lines 27 to 32) |
| `#### Added Later` holding the channel manager connection | Met | Lines 64 to 69 |
| Release-level `## Acceptance criteria` in numbered `1\.` blocks, each closed by Mark-as-done | Met | Criteria 1 to 4 at 78, 87, 96 and 105, Mark-as-done at 85, 94, 103 and 111. The section closes on `* * *` (112) above `##   ` (113) |
| No `## Requirements`, header fields, story points or INVEST notes | Met | None |
| Consults only the Epic scaffold where the reads show | Met | Turn 1 reads Story Mode, Interactive Mode, the Interactive Response Templates and Human Voice Core. Turn 2 reads the Epic Template, the Epic example and Conciseness (`events-turn-2.jsonl` lines 3, 5, 7). No Story Template read |
| Names the kind | Met | Line 150 "This is an Epic" |
| `11 business days`, `38%` | Met | Lines 15 and 16 |
| `3 business days`, `1,500`, `2027-06-30` | Met | Lines 24 and 26 |
| Invents no link | Met | No URL |
| Claims no file | Met | `turn-1.md` line 44. Line 31 "Without links I'll leave out References" names a section. Turn 2 has no file wording |
| Fail: a brief value rounded or rewritten | Not hit | 813 of 2,140 (16), 4.5 hours (17), 640 (18), `8` photos and `20 MB` (55), `1 business day` (62), 18,000 (26, brief line 21) |
| Fail: a child story added, merged or dropped | Not hit | Six |
| Fail: chains, over 40 rooms or channel manager properties in first-release scope | Not hit | Lines 46, 107 and 141 |
| Fail: an estimate the brief never gave | Not hit | Estimation lines 121 to 123 are `TBD...` |
| Fail: an unfilled slot | Not hit | `TBD...` in the Delivery slots is exempt (root line 207). "Date: TBD..." (129) is the fixed line of `Product Owner - Templates - Story Mode - v0.403.md` line 330 |

**Blocking items hit**

None.

**Advisory items**

- Named additions at `turn-2.md` lines 152 to 159. Borderline, never decides alone: the business register dependency (129) is labelled an inference at line 156 but still states that "sign-up verification stays blocked in a country until it does".
- Asking for a fact an attachment states (root line 211): Turn 1 item 2 (line 11) asks "One child story per stage, six in all", which brief line 63 already asks for.
- Size: 142 block lines, inside 90 to 150.

**Realism entries**

- Block `PEP-001-turn1-block1.md` (reply lines 2 to 31), Epic-lane clarification. Question alone: present. Facts: payouts wait for the identity checks (5 vs brief 49); stage 6 in Back office by Ops Tools (11 vs brief 32 and 57); seven Partner Hub locales and five currencies (26 vs `roamstay-context.md` 132 and 118); Owner-only payout changes (28 vs 28); up to 40 rooms (8 vs brief 36). Placeholder: `TBD...` at line 23 is quoted as a named option, not a slot. 30 lines, no band. Format gate: passed.
- Block `PEP-001-turn2-block1.md` (reply lines 2 to 143), Epic. Routed template: `Product Owner - Assets - Epic Template - v0.101.md`, with the optional Delivery close (section 3) and External dependencies (Story Mode knowledge line 133). Required sections present. Facts: the H1 shape (2 vs `roamstay-context.md` 85); 813 of 2,140 (16 vs brief 11); 4.5 hours per property (17 vs brief 12); 640 in the queue (18 vs brief 13); `8` photos, `20 MB` (55 vs brief 28); the three squads (121 to 123 vs brief 56 to 58). Placeholder: none beyond the exempt `TBD...`. 142 lines against 90 to 150. Format gate: passed.

**Open readings**

- None decides `PEP-001`.

---

### PEP-002 (project), Epic natural wording

**Draft row**

```csv
PEP-002,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 resolves the Epic lane from wording alone and renders one fenced question under export/001 - Epic-offline-mode-clarification.md, closing ""I'll write the epic once you reply."" (turn-1.md line 33) with no path or file, and Turn 2 renders a fenced Epic with the four areas verbatim as plain-text child stories across iOS, Android and Desktop, 23% and 31%, Web out and the 2026-10-09 decision left open. Today's rule now reads block-level last-writer-wins word for word (turn-2.md line 17)."
```

**Against the first round:** fixed. The first round failed on `turn-1.md` line 31 "When you reply, I'll write the epic as `export/002 - Epic-offline-mode.md`." The first round's borderline paraphrase of `block-level last-writer-wins` is also gone.

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 resolves the Epic kind from wording alone | Met | No command token. Turn 1 reads Story Mode, the Epic Template and the Router Contract (`events-turn-1.jsonl` lines 12, 14, 16). Line 33 "This will be an Epic" |
| One Epic question in the Epic lane, drafts nothing | Met | Fenced, lines 1 to 25. Line 27 `export/001 - Epic-offline-mode-clarification.md`. `HVR self-scan:` line 29. Line 33 "I need your answer before drafting" |
| Turn 2 renders one Epic with a `# Epic - ` H1 and no story preamble | Met | Fenced, lines 1 to 103. Line 2 `# Epic - Platform - Offline mode` |
| `## About` holding `### Problem`, `### Goal`, `### Solution` | Met | Lines 5, 10, 20 and 34 |
| `#### **References**` only when a link is supplied | Met | Omitted. Line 122 |
| `## Scope` naming exactly the four areas verbatim as plain-text child stories, each covering iOS, Android and Desktop | Met | Lines 48, 49, 55 and 56: Offline reading, Offline indicator and storage settings, Offline editing and creation, Sync on reconnect. Line 44 "covers iOS, Android and Desktop together" |
| Release-level criteria in numbered `1\.` blocks, each closed by Mark-as-done | Met | Criteria 1 to 4 at 65, 74, 84 and 93, Mark-as-done at 72, 82, 91 and 100 |
| No `## Requirements`, header fields, story points or INVEST notes | Met | None |
| Consults only the Epic scaffold where the reads show | Met | Turn 2 reads the Epic example and Conciseness (`events-turn-2.jsonl` lines 7 and 9). No Story Template read |
| Names the kind | Met | Line 109 "I wrote this as an Epic" |
| `23%` and `31%` verbatim | Met | Line 12 |
| Web out of every child story and criterion | Met | Line 8 "Web is out of scope". No story or criterion names Web |
| Conflict handling named as a dependency on the `2026-10-09` decision | Met | Line 53 "These two stories can't be finalised until that decision is made", and Solution line 39 |
| Claims no file | Met | `turn-1.md` line 33. Turn 2 has no file wording |
| Fail: asks in the intake or Story lane, drafts in Turn 1 | Not hit | Lines 27 and 33 |
| Fail: a child story split per platform | Not hit | Four areas |
| Fail: Web or an out-of-scope item added | Not hit | Line 8 lists the brief's out-of-scope items as out (brief lines 43 to 48) |
| Fail: a conflict-handling approach stated as decided | Not hit | Line 17 describes today's rule. Line 39 "whichever conflict-handling option Joana chooses" |
| Fail: offline mode limited to a plan | Not hit | Lines 7 and 67 "Free included" |
| Fail: a brief value altered | Not hit | 500 pages and 1 GB (37), the halving within 8 weeks (30), Q1 2027 (7), `block-level last-writer-wins` on protocol v3 (17) |
| Fail: an invented link or a local save | Not hit | None |

**Blocking items hit**

None.

**Advisory items**

- Named additions at `turn-2.md` lines 115 to 119, among them criterion 2's "closing the app before the connection returns loses none of those changes" (79) and the page-history clause (17, from `loomlist-context.md` line 180).
- Size: 101 block lines, inside 80 to 140.

**Realism entries**

- Block `PEP-002-turn1-block1.md` (reply lines 2 to 24), Epic-lane clarification. Question alone: present. Facts: Desktop wrapping the web client (8 vs `loomlist-context.md` 12 and 18); the two-week train with a 7-day rollout (8 vs 137); Joana's decision on 2026-10-09 (7, 16 vs brief 32); a protocol change needing every client (17 vs 177); the `lost-edit` tickets (20 vs brief 10). Placeholder: none. 23 lines, no band. Format gate: passed.
- Block `PEP-002-turn2-block1.md` (reply lines 2 to 102), Epic. Routed template: `Product Owner - Assets - Epic Template - v0.101.md`, required sections present, no Delivery. Facts: the H1 shape (2 vs `loomlist-context.md` 112); 500 pages and 1 GB (37 vs brief 22); Joana as Engineering Manager, Sync (53 vs 87 and brief 32); Q1 2027 (7 vs brief 36); the out-of-scope list (8 vs brief 45 to 48); `block-level last-writer-wins` on protocol v3 (17 vs brief 26, `loomlist-context.md` 70). Placeholder: none. 101 lines against 80 to 140. Format gate: passed.

**Open readings**

- None.

---

### Twin notes

No skill twin ran in this round. Each Project row is compared with its twin's latest verdict: the first round where that twin was remeasured, the main run otherwise.

| Pair | Skill (latest) | Project (this round) | Agree or differ | Cause and rule lines |
|---|---|---|---|---|
| `SID-001` / `PID-001` | PASS (main run) | PASS | Agree | Each proves its own runtime. The skill does it with `Path:` and `Verified: read-back succeeded` (`AGENTS.md` line 47), the Project with a fenced block and `Export-equivalent path:` with no file wording (kernel lines 85, 101 and 228). The greps above keep the two proof strings apart |
| `SBG-002` / `PBG-002` | PASS (first round) | PASS | Agree | Same bug facts on both sides. The Project's first-round path promise is gone |
| `STK-005` / `PTK-005` | FAIL (first round) | PASS | Differ | Runtime fault on the skill side under `RO-1` read strictly. Both packagings keep supplied source content (skill `assets/task-templates.md` line 157, Project Task Templates line 138) and never cut a number (skill `SKILL.md` line 276, kernel line 90). `STK-005` restated `1 to 99` as "below 1 or above 99", and `PTK-005` writes "with N from 1 to 99" (line 55). Under the lenient `RO-1` reading they agree |
| `STK-006` / `PTK-006` | FAIL (main run) | FAIL | Agree | Both miss `deprecated`, a runtime fault on both sides under the same keep-the-source rule (skill `assets/task-templates.md` line 157, Project Task Templates line 138). `PTK-006` adds a Project-only miss, `booking-service`. `STK-006` was not rerun on the repaired sources |
| `SST-003` / `PST-003` | PASS (first round) | FAIL | Differ | Looks like a rule gap inside the Project packaging more than a plain runtime fault. The skill may announce its save under the source filename (`AGENTS.md` line 45 "save an exported copy with the exact original source filename"). The Project bars naming a file for an artifact still to come (kernel lines 101 and 228, Interactive Mode line 70), yet its own refinement rules use the same word for the label: kernel line 229 `export/[original-source-filename].md`, Story Mode knowledge line 370 "a refined Story keeps its source filename". `PST-003` line 42 echoes that vocabulary. If the operator rules that "filename" names a file, the kernel already forbids it and this is a runtime fault. Either way, the shared wording is the likely trigger |
| `SST-004` / `PST-004` | PASS (first round) | FAIL | Differ | Runtime fault on the Project side. Both packagings state the same rule: skill `references/story-mode.md` line 406 and `SKILL.md` line 252, Project `Product Owner - Templates - Story Mode - v0.403.md` line 382. The skill asked for the split, and the Project announced the brief's six twice (`turn-1.md` lines 4 and 56). Turn 2 is correct on both sides |
| `SEP-001` / `PEP-001` | PASS (first round) | PASS | Agree | Both omit References with no link, and neither side names a file for the Epic to come |
| `SEP-002` / `PEP-002` | PASS (main run) | PASS | Agree | Same four areas, Web out and the 2026-10-09 dependency open on both sides |

On the rule under test: all eight first-round rows carried file wording for the artifact still to come. In this round seven carry none: no reply attaches an `export/` path to the next artifact, and `PST-004`'s folder promise is gone too. The one left is `PST-003`'s "filename", which borrows the Project's own refinement wording. `PTK-006` and `PST-004` fail for causes unrelated to the rule.
