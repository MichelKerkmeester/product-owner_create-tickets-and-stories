# Miss causes: TK-003, long BE integration task at Fernhouse

Read-only investigation under `miss-cause-brief.md`. Paths are relative to `AI Systems/Product Owner/` unless they start with `specs/`. Short names used below:

| Short name | Path |
|---|---|
| MAIN | `benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium` |
| R1 | `MAIN/remeasure-operator-repairs/run-1` |
| main STK export | `export/benchmark/skill/STK-003 - 001 - task-label-webhook-fix.md` (byte-identical to `MAIN/skill/STK-003 - long-be-integration-task/exports/export/001 - task-label-webhook-fix.md`) |
| R1 STK export | `export/benchmark/skill/remeasure-operator-repairs/run-1/STK-003 - 002 - task-label-webhook-fix.md` (byte-identical to the copy under `R1/skill/`) |
| SK scenario | `sk-product-owner/manual-testing-playbook/skill-backlog-modes/long-be-integration-task.md` |
| PJ scenario | `sk-product-owner/manual-testing-playbook/project-backlog-modes/long-be-integration-task.md` |
| root | `sk-product-owner/manual-testing-playbook/manual-testing-playbook.md` |
| API notes | `benchmark/fixtures/companies/fernhouse/fernhouse-carrier-label-api-notes.md` |
| thread | `benchmark/fixtures/companies/fernhouse/fernhouse-carrier-label-thread.md` |
| CI | `claude project/Custom Instructions.md` (the kernel) |
| PK Task Mode | `claude project/knowledge/Product Owner - Templates - Task Mode - v0.305.md` |
| PK Task Templates | `claude project/knowledge/Product Owner - Assets - Task Templates - v0.102.md` |
| PK Quality Scoring | `claude project/knowledge/Product Owner - Rules - Quality Scoring - v0.100.md` |
| PK Conciseness | `claude project/knowledge/Product Owner - Rules - Conciseness - v0.100.md` |

Runs: the main run on `3023c5e`, where both runtimes drafted on Turn 1 and revised on Turn 2, and round one on `39bcd29`. Round two on `b591571` did not rerun TK-003: `MAIN/remeasure-file-forecast/run-1/results.csv` holds no TK-003 row. Every source line cited below reads the same at all three commits. `git diff 3023c5e b591571` touches none of `task-mode.md`, `task-templates.md`, `conciseness.md`, `quality-scoring.md` or their Project mirrors, and its edits to `AGENTS.md` (line 287), `SKILL.md` (lines 5 and 252) and CI (lines 1, 101, 108, 140 and 228) replace lines in place. The fixture hashes in both runs' `meta.json` match the fixtures today, and both scenario files differ from `3023c5e` only in the Project twin's version and a knowledge-file link.

## Table

| Row | Value | Kept in | Dropped in | Class | Change in one line |
|---|---|---|---|---|---|
| STK-003, PTK-003 | `HMAC-SHA256` | main STK (export line 38), main PTK (turn-2 line 40) | round one STK (export line 38), round one PTK (turn-2 line 33) | rule gap | Add a Task Mode rule that a supplied hard value a requirement builds or checks travels verbatim and is not HOW, and say so at CI line 19 |
| STK-003, PTK-003 | `5 attempts` | No run verbatim. Main STK (export line 34) and main PTK (turn-2 line 36) keep the value as "up to 5 more times" | round one STK and round one PTK, which keep only the fifth retry and the 7 hours 21 minutes total | scenario defect | Take `5 attempts` out of the Pass clause's verbatim list and fail only a retry count that is changed |
| STK-003, PTK-003 | `1 min, 5 min, 15 min, 1 h, 6 h` | No run verbatim. Main STK (export line 34) keeps every step as "after 1 min, 5 min, 15 min, 1 h and 6 h" | main PTK, round one STK, round one PTK (last step and total only) | scenario defect | The same Pass clause edit as `5 attempts`: fail only a changed step |
| STK-003, PTK-003 | Turn 2 "it goes on the Fulfilment board" | main STK (export line 13) | main PTK (reply line 139), round one STK (reply line 22), round one PTK (reply line 127): each names it in the reply, not the task | scenario defect | Let the Pass clause accept the board in the task or in the reply's delivery or ClickUp line |

## Task Mode answer, for the whole group

There is none. Neither `sk-product-owner/references/task-mode.md`, `sk-product-owner/assets/task-templates.md`, PK Task Mode nor PK Task Templates holds a rule that supplied technical values such as algorithms, counts or schedules travel into a task unchanged. The nearest lines, and why none of them is that rule:

- `task-templates.md:157` (PK Task Templates:138): "If the user provides source content, preserve it and only normalize what the user asked to normalize". The same asset scopes preservation to a sync at `task-templates.md:34`, "preserve source structure when the user asks for sync or refinement" (PK Task Templates:15), and Task Mode pairs source preservation with a sync at `task-mode.md:58` "When syncing or refining an existing task, preserve the source section names, section order and reference labels", `task-mode.md:256` "Source material preserved when task is a sync or refinement?" and `task-mode.md:284` "converted to proper checklists only when the user asked to normalize them". The line names no kind of value and says nothing about which parts of an attachment a new task must carry.
- `task-mode.md:354` (PK Task Mode:334): "In a Story, Requirements holds hard constraints only, carries every hard value the source supplied with its value, units and notation intact". It is the pointer copy of `SKILL.md:268`, scoped to a Story by its own words. Its only sentence for tasks is "Keep the Task QA checklist inside a Task's Requirements."
- `task-mode.md:109` (PK Task Mode:89) "`- [ ]` checklist items for literal, actionable requirements" and `task-mode.md:274` (PK Task Mode:254) "Requirement wording is concrete and testable?". Both ask for concrete wording, not for a supplied value.

Every verbatim-value rule in either package is Story-scoped: `sk-product-owner/references/story-mode.md:75` and `:80`, `sk-product-owner/assets/story-template.md:111`, `SKILL.md:268` ("In a Story"), `AGENTS.md:270` ("For Story intent"), `sk-product-owner/references/quality-scoring.md:155` ("A PRD") and CI:140 (the Story shape).

## Against the earlier reading

The round-one comparison called both rows a runtime fault (`R1/grading-notes.md:519`, "Both packagings tell the runtime to keep supplied values and numbers (skill `AGENTS.md` line 42 and `assets/task-templates.md` line 157, Project kernel line 90 and `Product Owner - Assets - Task Templates` line 138)"), as the main run did (`MAIN/grading-notes.md:1044`). This file does not follow it, for three reasons:

- `AGENTS.md:42` and CI:90 are cut rules for the pre-export pass (`conciseness.md:155` "Run this after the voice pass and before the export"). Round one STK never drafted the three carrier values, so no cut removed them: the Turn 2 events (`R1/skill/STK-003 - long-be-integration-task/events-turn-2.jsonl`) contain no `HMAC-SHA256`, no `5 attempts` and no `5 more`, the first Write (`transcript-turn-2.md:45`) builds the export without them and the only later edit (`transcript-turn-2.md:53`) rewrites two other sentences. The Project has no draft history to check, so for PTK the same is inference.
- `HMAC-SHA256` is an algorithm name, not a number, so no keep rule names it.
- `task-templates.md:157` and PK Task Templates:138 read as the sync rule, as shown above.

The evidence is thin in one place: the thinking blocks in both round-one `events-turn-2.jsonl` files are empty strings, so no run records why a value was left out.

## Rule catalogue

Quoted once here and named by id in each miss.

Rules that reach a task and lean toward keeping a value:

- K1 `AGENTS.md:42`: "Cut only what a reader could rebuild from what remains, and keep the semantic connectives, scope qualifiers, caveats, numbers and examples the layer names."
- K2 `SKILL.md:276`: "Apply `references/conciseness.md` to every artifact after the voice pass. Cut only what a reader could rebuild from what remains, and never cut a semantic connective, a scope qualifier, a caveat, a number or the one example that makes a rule usable." Project: CI:90, the same text.
- K3 `sk-product-owner/references/conciseness.md:89` "**The specific number.** 33 fixtures, not several fixtures" and `conciseness.md:35` "After a cut, could a reader who does not already know the answer recover what was removed from what remains?" Project: PK Conciseness:89 and :35.
- K4 `task-templates.md:157` (PK Task Templates:138), quoted above, sync-scoped.
- K5 `SKILL.md:266`: "Use user-provided context as the main source of truth." The Project carries this only in its Story Mode and Doc Mode knowledge files, not for tasks.

Rules that reach a task and push the other way:

- P1 `task-mode.md:33` "Task Mode creates or refines Product Owner tasks that define WHAT and WHY", `task-mode.md:273` "Requirements describe WHAT and WHY, not HOW?" and `task-mode.md:332` "Stay in WHAT and WHY, not HOW". Project: PK Task Mode:13, :253 and :312.
- P2 `task-mode.md:107` "One or more short paragraphs that explain the outcome and context" and `task-templates.md:109` "{1-2 short paragraphs describing the expected outcome and why it matters.}". Project: PK Task Mode:87 and PK Task Templates:90.
- P3 `SKILL.md:263` "Keep backlog artifacts outcome-focused.", `SKILL.md:268` "Write acceptance criteria as outcomes the user can rely on, few in number and open on the mechanism", `SKILL.md:306` "Outcome before mechanism for backlog artifacts", `AGENTS.md:11` "Backlog artifacts define WHAT needs doing, WHY it matters and how success will be verified" and `AGENTS.md:266` "Keep backlog work outcome-focused". Project: PK Task Mode:326 and :334.
- P4 CI:15 "Backlog artifacts communicate WHAT matters and WHY it matters." and CI:19 "For Doc intent, this boundary overrides the generic backlog-only instructions to omit HOW or implementation detail. Those instructions continue to govern Task and Bug artifacts." The skill has no sentence this explicit.
- P5 `quality-scoring.md:94`: "Mechanism Depth is satisfied by a user-value line rather than by implementation reasoning, since a task that explains HOW has drifted out of Product Owner scope and loses Relevance for it." Project: PK Quality Scoring:71.
- P6, the board only. No slot holds it: the Canonical Task context blocks are `**References**`, `**Epic**`, `**Story**`, `**Parent task**`, `**Related tasks**` and `**Related tickets**` (`task-templates.md:51` to `:95`, PK Task Templates:32 to :76), and `task-mode.md:82` limits optional context to "Use only when they add value or already exist in the source task". `SKILL.md:236` (CI:195) "Push shape: the artifact's H1 becomes the ClickUp task name and is dropped from the body." leaves the ClickUp location to the push.
- P7, the board only and weak. `conciseness.md:53` (PK Conciseness:53): "**Restated constraint.** Repeating back a fact the user supplied".

Grading lines: root:150 "A turn that misses any Pass clause fails the scenario even when no Fail example describes the miss", root:188 "A protected fact altered: a supplied value generalized, a conflict silently resolved or a proposal promoted to current behavior", root:208 "Omitting a context fact the request does not need is not a defect".

## 1. `HMAC-SHA256`

**1. The source.** API notes:53: "Each request carries `X-Carrier-Signature`: the hex `HMAC-SHA256` of the raw request body, keyed with our webhook secret. Check it against the raw bytes before parsing the JSON, and answer `401` when it does not match." The agreed scope names the check at thread:33: "Check the signature, store the raw event, return 200 and do the work from a queue".

**2. The demand.** SK scenario:39 and PJ scenario:39: "the carrier values `event_id`, `X-Carrier-Signature`, `HMAC-SHA256`, `5 seconds`, `5 attempts` and `1 min, 5 min, 15 min, 1 h, 6 h` verbatim". Both files at :36: "the carrier's contract verbatim (`fernhouse-carrier-label-api-notes.md` lines 13 to 68)". Root:150 makes the one missed clause a FAIL.

**3. What was written.**

| Run | Where | Text | Result |
|---|---|---|---|
| main STK | main STK export:38 | "`X-Carrier-Signature` is checked as the hex `HMAC-SHA256` of the raw request body before the JSON is parsed, and a mismatch is answered with `401`" | kept |
| main PTK | `MAIN/replies/PTK-003-turn2.txt:40` | "`/webhooks/carrier/labels` checks `X-Carrier-Signature`, the hex `HMAC-SHA256` of the raw body keyed with the webhook secret, against the raw bytes before parsing the JSON, and answers `401` on a mismatch" | kept |
| round one STK | R1 STK export:38 | "`X-Carrier-Signature` is checked against the raw request body before the JSON is parsed, and a mismatch gets `401`" | dropped, never drafted (see Against the earlier reading) |
| round one PTK | `R1/replies/PTK-003-turn2.txt:33` | "The handler checks `X-Carrier-Signature` against the raw request body and answers `401` when it does not match" | dropped |

The notes reached both round-one sessions: `HMAC-SHA256` occurs in `R1/skill/STK-003 - long-be-integration-task/events-turn-1.jsonl` and in `R1/claude project/PTK-003 - long-be-integration-task/events-turn-1.jsonl`.

**4. The rules.** Keep side: none reaches this value in a task. K1 to K3 protect numbers, and `HMAC-SHA256` is an algorithm name. K4 is sync-scoped. K5 names no wording. Push side: P1, P3, P4 and P5 read a signature algorithm as implementation detail. No rule for a task protects this value.

**5. The cause class: rule gap.** The deciding evidence is the absence above together with the run history: both runtimes kept the value in the main run and dropped it in round one under task rules that are identical at both commits, so the rules allow either outcome. It is not a runtime fault, because no clear rule required the value and the keep rules that do reach a task never met it in round one STK, which never wrote it. It is not a rule conflict on this evidence, because the same checklist items kept equal implementation detail (`X-Carrier-Signature`, the raw body, `401`) and the WHAT/WHY rules did not remove the value in the main run. It moves to rule conflict if a run shows the runtime dropping the value on the WHAT/WHY-not-HOW rule. The only hint today is `R1/replies/PTK-003-turn1.txt:45` "It will describe the outcome and the reason for each point, not the implementation.", which is inference, not proof.

**6. The smallest change.**

- Skill, `sk-product-owner/references/task-mode.md`, a new paragraph after line 112, whose current text is "Number requirement groups only when the task carries two or more. A single group keeps its bold title without a number. The moment a second group appears, number them `1.`, `2.` in order." Proposed paragraph: "A hard value the supplied sources or the user's answers give for something a requirement builds or checks, such as an algorithm, a header, an endpoint, a status code, a count, a timeout, a schedule or a threshold, travels into that requirement verbatim, in the source's own units and notation, inside backticks. A supplied value is a constraint rather than HOW, so staying in WHAT and WHY never removes it, and neither a paraphrase nor a total worked out from it stands in for it."
- Skill, `task-mode.md:273`, current "- [ ] Requirements describe WHAT and WHY, not HOW?", proposed "- [ ] Requirements describe WHAT and WHY, not HOW, and carry every supplied hard value a requirement builds or checks verbatim?"
- Project, PK Task Mode: the same paragraph after line 92 (the same current text) and the same checklist edit at line 253.
- Project, CI:19, current "Those instructions continue to govern Task and Bug artifacts.", proposed "Those instructions continue to govern Task and Bug artifacts, where a supplied hard value a requirement builds or checks is a constraint rather than HOW and travels verbatim."
- The knowledge file's version bump and the `SYNC.md` note follow the system's manual parity method.

## 2. `5 attempts`

**1. The source.** API notes:58: "After a failed delivery it makes up to `5 attempts` more, waiting `1 min, 5 min, 15 min, 1 h, 6 h` before each one". API notes:59: "That is 7 hours 21 minutes from the first try to the last. After the fifth failed retry the event is dropped and never sent again". The thread uses only the consequence, at thread:34: "Keep processed ids for `7 days`, well past the carrier's last retry".

**2. The demand.** SK scenario:39 and PJ scenario:39, quoted under miss 1. The Fail clause at :39 and :75 ("changes a retry, window or threshold") targets alteration only.

**3. What was written.**

| Run | Where | Text | Result |
|---|---|---|---|
| main STK | main STK export:34 | "retries up to 5 more times, after 1 min, 5 min, 15 min, 1 h and 6 h" | value intact, wording changed, graded Unmet under the open reading OR-3 (`MAIN/grading-notes.md:459`, `:580`) |
| main PTK | `MAIN/replies/PTK-003-turn2.txt:36` and `:59` | "It then retries up to 5 more times over 7 hours 21 minutes and drops the event after the last retry fails" and "delivered 6 times (the first try plus 5 retries)" | value intact, wording changed. The main-run row calls it dropped (`MAIN/grading-notes.md:877`) |
| round one STK | R1 STK export:9 and :53 | "Their fifth and last retry comes 6 hours after the fourth" and "well past the carrier's last retry at 7 hours 21 minutes" | count not stated, only implied by "fifth and last", never drafted |
| round one PTK | `R1/replies/PTK-003-turn2.txt:50` and `:73` | "well past the carrier's last retry at 7 hours 21 minutes after the first try" and "The carrier drops an event after its fifth failed retry" | count not stated, only implied by "fifth" |

No run kept `5 attempts` verbatim.

**4. The rules.** Keep side: nothing requires it verbatim. K1 to K3 reach it as a number, but they govern cuts in the pre-export pass, and round one STK never drafted it. K3's "the specific number" is met by "fifth" and by "7 hours 21 minutes". K4 is sync-scoped. Push side: P1, P2 and P5. No rule for a task protects the value verbatim.

**5. The cause class: scenario defect.** The deciding evidence: no task rule requires the value, and the source does not make it binding on this task. Turn 1 sets the scope as "the five points from the thread" (SK scenario:31). None of those points (thread:33 to :37, summary :59 to :63) acts on the carrier's retry count, and point 2 uses only its consequence, which all four runs carry. The scenario itself treats contract values the five points do not act on as optional: its overview at :17 lists `24 hours` and `20 requests per second` among the contract values, the Pass list at :39 leaves them out, and no run carries `24 hours` or `422` (API notes:64 and :16) with no grading consequence. Root:208 excuses "a context fact the request does not need", and root:188 protects against alteration, which no run did. It moves to rule gap if the operator rules that a task built on a supplied contract carries every hard value the contract states, whether or not a requirement acts on it. The miss 1 paragraph then drops "for something a requirement builds or checks" and covers this value too.

**6. The smallest change.** SK scenario:39, current "the carrier values `event_id`, `X-Carrier-Signature`, `HMAC-SHA256`, `5 seconds`, `5 attempts` and `1 min, 5 min, 15 min, 1 h, 6 h` verbatim", proposed "the carrier values `event_id`, `X-Carrier-Signature`, `HMAC-SHA256` and `5 seconds` verbatim, with any retry count or schedule the task states unchanged". The matching expected-signal wording is SK scenario:36, current "the carrier's contract verbatim (`fernhouse-carrier-label-api-notes.md` lines 13 to 68)", proposed "every carrier value a requirement builds or checks verbatim (`fernhouse-carrier-label-api-notes.md` lines 13 to 68)", and SK scenario:66, current "the carrier contract values verbatim", proposed "the carrier values its requirements build or check verbatim". The Fail wording at :39 ("changes a retry step, window or alert threshold") and :75 stays and still catches a changed count. Counterpart: PJ scenario:39, :36 and :66, with the same text.

## 3. `1 min, 5 min, 15 min, 1 h, 6 h`

**1. The source.** API notes:58, quoted under miss 2, and the total at API notes:59. The thread uses the last step at thread:27: "The fifth retry comes 6 h after the fourth, so those labels only landed after 21:00."

**2. The demand.** SK scenario:39 and PJ scenario:39, quoted under miss 1.

**3. What was written.**

| Run | Where | Text | Result |
|---|---|---|---|
| main STK | main STK export:34 | "after 1 min, 5 min, 15 min, 1 h and 6 h" | every step intact, list joined with "and" and set without backticks (OR-3) |
| main PTK | `MAIN/replies/PTK-003-turn2.txt:36` and `:10` | "over 7 hours 21 minutes" and "the fifth retry, 6 h after the fourth" | last step and total only |
| round one STK | R1 STK export:9 and :53 | "Their fifth and last retry comes 6 hours after the fourth" and "7 hours 21 minutes" | last step and total only, never drafted |
| round one PTK | `R1/replies/PTK-003-turn2.txt:50` | "7 hours 21 minutes after the first try" | total only |

No run kept the schedule verbatim.

**4. The rules.** As for miss 2. K1 to K3 reach the numbers, and K3's reconstruction test would fail a cut from five steps to their total, but it governs a cut, and round one STK never drafted the steps. Push side: P1, P2 and P5. No rule for a task protects the schedule verbatim.

**5. The cause class: scenario defect.** The deciding evidence is as for miss 2: no task rule requires the schedule, and no agreed point acts on its steps. The runtimes carried the two consequences the thread uses, the 6 h last step (thread:27) and the total behind "well past the carrier's last retry" (thread:34). It moves to rule gap on the same operator ruling as miss 2.

**6. The smallest change.** The miss 2 edit covers it: "with any retry count or schedule the task states unchanged".

## 4. Turn 2 "it goes on the Fulfilment board"

**1. The source.** SK scenario:47 and PJ scenario:47, Turn 2: "`No parent, it goes on the Fulfilment board and has to be live before the November peak. ...`".

**2. The demand.** SK scenario:39: "Turn 2 saves one `task` export on the next number, read back and reported the same way, carrying its H1, `### About` and `### Requirements` ... and every Turn 2 fact". SK scenario:36: "Every Turn 2 fact survives: no parent, the Fulfilment board, live before the November peak, ...". PJ scenario:39 has "Turn 2 renders one task block ... carrying ... every Turn 2 fact", with the same list at :36.

**3. What was written.**

| Run | Where | Text | Result |
|---|---|---|---|
| main STK | main STK export:13 | "It sits on the Fulfilment board with no parent task, and it has to be live before the November peak." | in the task |
| main PTK | `MAIN/replies/PTK-003-turn2.txt:139` | "The Fulfilment board and Joris as assignee are ClickUp fields rather than ticket text, so set both when you create the task." | reply only |
| round one STK | `R1/replies/STK-003-turn2.txt:22` | "I can also create it on the Fulfilment board in ClickUp, with no parent, if you'd like." | reply only |
| round one PTK | `R1/replies/PTK-003-turn2.txt:127` | "**Next step:** save the task to the Fulfilment board with Joris as the assignee." | reply only |

Every run kept the fact. Three of the four put it with delivery rather than in the body.

**4. The rules.** Keep side: no rule says a placement fact from an answer goes into the task body. Interactive Mode hands the answer back to Task Mode at `sk-product-owner/references/interactive-mode.md:28` ("the resolved mode reference with its paired scaffold once the user answers") and says nothing about where each answer lands. K5 is met by every run. Push side: P6 (no slot, and the push shape leaves the ClickUp location to the push) and P7 (weak). No rule for a task places the board in the body.

**5. The cause class: scenario defect.** The deciding evidence: no rule and no template slot put a board in a task body, and every run honoured the placement where a board is set, in the ClickUp offer or the reply's next step. The scenario's own picture of a realistic task (SK scenario:19, PJ scenario:19) lists the title, About, references, requirement groups, acceptance and the polling note, with no board line. The round-one grader reads the parallel Turn 2 fact "no parent" as carried by structure, not words (`R1/grading-notes.md:44`, RO-5), and left the board reading open (`R1/grading-notes.md:45`, RO-6). It moves to rule gap if the operator rules RO-6 as "the board belongs in the task body".

**6. The smallest change.**

- SK scenario:39, current "polling only kept out, and every Turn 2 fact. FAIL if", proposed "polling only kept out, and every Turn 2 fact, the Fulfilment board counting when either the task or the reply's delivery or ClickUp line names it. FAIL if".
- SK scenario:36, current "Every Turn 2 fact survives: no parent, the Fulfilment board, live before the November peak,", proposed "Every Turn 2 fact survives: no parent, the Fulfilment board (in the task or in the reply's delivery or ClickUp line), live before the November peak,".
- Counterpart: PJ scenario:39 and :36, reading "the block or the reply after it" in place of "the task or the reply's delivery or ClickUp line".
- If the operator rules RO-6 the other way, this becomes a rule gap and the smallest rule is `task-templates.md:49`, current "{1-3 short paragraphs describing the task, why it matters and what outcome it should create.}", proposed "{1-3 short paragraphs describing the task, why it matters and what outcome it should create, plus any board, deadline or owner the user names for it.}", mirrored at PK Task Templates:30.
