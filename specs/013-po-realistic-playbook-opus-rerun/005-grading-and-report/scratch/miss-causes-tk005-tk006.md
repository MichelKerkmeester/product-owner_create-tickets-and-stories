# Miss causes: TK-005 and TK-006

| Row | Value | Kept in | Dropped in | Class | Change in one line |
| --- | --- | --- | --- | --- | --- |
| `STK-005` | `1 to 99` | `STK-005` main run (export line 67). Contrast: `PTK-005` main, round one and round two all keep it | `STK-005` round one (export line 56, "cannot save an N below 1 or above 99") | scenario defect | List the value as `99` in both twins' Pass clause (line 39), the way the same clause already lists `365` |
| `STK-006`, `PTK-006` | `deprecated` | none | `STK-006` main; `PTK-006` main, round one and round two | rule gap | Add one Task Mode Core Rule that a supplied name or status word travels as the source writes it (skill `task-mode.md` after line 59, Project Task Mode after line 39) |
| `PTK-006` | `proposed` | `STK-006` main; `PTK-006` main and round two | `PTK-006` round one ("still a proposal") | rule gap | The same Core Rule bullet, which names `proposed` |
| `PTK-006` | `booking-service` | `STK-006` main; `PTK-006` main and round one | `PTK-006` round two | rule gap | The same Core Rule bullet, which names service names and bans a generic stand-in |

Paths are relative to `AI Systems/Product Owner/`. Short forms used below:

- `PB` = `sk-product-owner/manual-testing-playbook`
- `R` = `benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium` (main run, `3023c5e`)
- `R1` = `R/remeasure-operator-repairs/run-1` (round one, `39bcd29`)
- `R2` = `R/remeasure-file-forecast/run-1` (round two, `b591571`, Project rows only)
- `EX` = `export/benchmark/skill`
- `K/<name>` = `claude project/knowledge/Product Owner - <name> - v0.xxx.md` (Task Mode v0.305, Task Templates v0.102, Quality Scoring v0.100, Conciseness v0.100, Human Voice Core v0.100, Interactive Mode v0.407)
- `plan` = `benchmark/fixtures/companies/roamstay/roamstay-booking-funnel-tracking-plan.md`
- `parent` = `benchmark/fixtures/companies/loomlist/loomlist-recurring-todos-parent-task.md`

Diff check: `git diff 3023c5e b591571` touches none of `task-mode.md`, `task-templates.md`, `quality-scoring.md`, `conciseness.md`, `hvr-core.md`, `K/Task Mode`, `K/Task Templates`, `K/Quality Scoring`, the four scenario Pass clauses or the fixtures. `AGENTS.md` (line 287), `SKILL.md` (lines 5, 252) and the kernel (lines 1, 101, 108, 140, 228) changed by one-line replacements, so every line cited below holds for all three runs. Which files each run opened comes from the `file_path` and `command` fields of each run's `events-turn-<n>.jsonl`. Thinking text is redacted in every run checked (0 characters in every thinking block), so no claim below rests on what a runtime intended.

---

## 1. `STK-005`, `1 to 99`

### 1. The source

`parent:67`: "| Custom | Every N days, weeks or months, with N from 1 to 99 |". The parent writes the range as plain prose in a table cell. The strings it means as literal it backticks: `parent:59` `Add a due date to repeat`, `parent:91` `This workspace has 500 repeating to-dos. End one to add another.`, `parent:103` `recurring_todos`, `parent:109` `todo_repeat_set`. `parent:11` makes the rules binding, not their phrasing: "This parent states the shared rules once. Each subtask builds them in one client or in the engine".

### 2. The demand

`PB/skill-backlog-modes/supplied-parent-subtask.md:39`, Pass: "the shared rules with `Daily`, `Weekdays`, `Weekly`, `Monthly`, `Custom`, `1 to 99`, `Never`, `On date`, `After`, `365`, `Skip this one`, `500`, `recurring_todos` and the `owner's time zone` as the parent gives them". The same line's Fail clause: "changes an option, range, limit, sheet copy or plan rule". Expected signals, `:36`: "carries the parent's shared rules verbatim for the Android client (lines 59 to 109)". The Project twin `PB/project-backlog-modes/supplied-parent-subtask.md:39` lists the same values.

### 3. What was written

- `STK-005` main run: `EX/STK-005 - 001 - task-android-recurring-todos-subtask.md:67` "- [ ] N accepts 1 to 99 and nothing outside that range". Kept
- `STK-005` round one: `EX/remeasure-operator-repairs/run-1/STK-005 - 002 - task-android-recurring-todos.md:56` "- [ ] Custom takes every N days, weeks or months, and the member cannot save an N below 1 or above 99, matching `Recurring to-dos / Custom interval`". Dropped as a phrase, value unchanged. The same export at `:58` restates the After range in the same shape, "the member cannot save a number below 1 or above 365", and that was graded Met because the Pass clause lists the bare `365` (`R1/grading-notes.md:379`). The chat reply says the value came across whole: `R1/replies/STK-005-turn2.txt:7` "All values come from the parent: the five repeat options, N from 1 to 99, After from 1 to 365", with `:5` "HVR self-scan: 0 hard blockers. Fixed: none."
- `PTK-005`, as contrast: main run `R/replies/PTK-005-turn2.txt:54` "Custom repeats every N days, weeks or months, with N from 1 to 99, and accepts no value outside that range". Round one `R1/replies/PTK-005-turn2.txt:62` "with N from 1 to 99", and `:63` "Accept no Custom value below 1 or above 99", so it wrote both forms. Round two `R2/replies/PTK-005-turn2.txt:55` "with N from 1 to 99". Kept in all three

Both round-one runtimes read the same task scaffold before drafting: `STK-005` Turn 2 ran `sed -n 38,260p assets/task-templates.md` (`R1/skill/STK-005 - supplied-parent-subtask/events-turn-2.jsonl`), which covers line 157, and `PTK-005` Turn 2 opened `K/Task Templates` (`R1/claude project/PTK-005 - supplied-parent-subtask/events-turn-2.jsonl`). One kept the phrase and one did not.

### 4. The rules

Rules that could require it, for the task kind:

- `sk-product-owner/assets/task-templates.md:157` "If the user provides source content, preserve it and only normalize what the user asked to normalize" (Project `K/Task Templates:138`, same text). It is a Notes For Use bullet under the Canonical Task template (`:154`). The Subtask template (`:214` to `:256`, Project `:195`) has no notes. Its neighbours scope preservation to a sync: `task-templates.md:34` "preserve source structure when the user asks for sync or refinement" (Project `:15`), `task-mode.md:58` "When syncing or refining an existing task, preserve the source section names, section order and reference labels", `task-mode.md:256` "Source material preserved when task is a sync or refinement?". It names no value, range or notation. The round-two grading notes read it as a keep-the-source rule (`R2/grading-notes.md:582`); read in its own section it is the sync rule
- `SKILL.md:276` "never cut a semantic connective, a scope qualifier, a caveat, a number or the one example that makes a rule usable" (kernel `Custom Instructions.md:90`). Both numbers survive at export `:56`, so this is met
- Notation-intact rules exist only for Stories: `story-mode.md:75` "Supplied hard values travel into Requirements verbatim. ... in the source's own units and notation, inside backticks", `SKILL.md:268` "In a Story, Requirements holds hard constraints only, carries every hard value the source supplied with its value, units and notation intact" (`task-mode.md:354`, Project `K/Task Mode:334`), `AGENTS.md:270` "For Story intent, list every hard value the supplied source states, in its own grouping and notation", `quality-scoring.md:155` "A PRD ... carries every supplied hard value verbatim"
- Grading side only: root `PB/manual-testing-playbook.md:188` "A protected fact altered: a supplied value generalized". The range was not generalized

Rules that push the other way:

- `hvr-core.md:106` "**False ranges.** "From X to Y" where the endpoints share no scale" (Project `K/Human Voice Core:106`). By its own scope it does not reach 1 to 99, and the full rules say so: `human-voice-rules.md:311` "Genuine ranges with meaningful endpoints are acceptable". The self-scan reports no fix, so there is no evidence it fired
- `task-mode.md:109` "`- [ ]` checklist items for literal, actionable requirements" and `quality-scoring.md:94` "**Task.** Actionability decides it. Requirements are QA-checkable outcomes". A boundary a tester can try, "cannot save below 1 or above 99", fits both. This permits the restatement and does not require it
- The scenario's size band (`:38`) is grader-side and never reaches the runtime

No rule for the task kind protects the notation of a supplied range.

### 5. The cause class

`scenario defect`. No task rule requires the phrase, so it is not a runtime fault. The source does not make the phrase binding: the parent backticks what it means as literal and leaves "1 to 99" as prose (`parent:67` against `parent:59` and `:91`). The value is unchanged, and a changed value is what the scenario's own Fail clause (`:39` "changes an option, range, limit") and root `:188` name as the failure. The same export restates the After range in the same shape at `:58` and passed, because the Pass clause spells that value `365`, so the verdict turned on the Pass clause's spelling and not on what the runtime did.

What would move it: an operator ruling on RO-1 (`R1/grading-notes.md:40`) that a hard value restated in other words fails in a task too would make the demand legitimate and this a `rule gap`.

### 6. The smallest change

`PB/skill-backlog-modes/supplied-parent-subtask.md:39`, current: "`Monthly`, `Custom`, `1 to 99`, `Never`". Proposed: "`Monthly`, `Custom`, `99`, `Never`", the shape the same clause gives `365`. Counterpart: `PB/project-backlog-modes/supplied-parent-subtask.md:39`, the same edit. If the operator rules RO-1 strictly instead, the rule-side change is to add "a number, range or limit" to the Core Rule bullet proposed in section 2 below, in skill `task-mode.md` after `:59` and Project `K/Task Mode` after `:39`.

---

## 2. `STK-006` and `PTK-006`, `deprecated`

### 1. The source

- `plan:25` "| `checkout_complete` | The confirmation screen renders | Client | deprecated, removal on 2026-11-01 |"
- `plan:28` "Status key: new, changed (a live event whose properties change), deprecated (fires until its removal date), proposed (raised in comments)."
- `plan:56` "`checkout_complete` keeps firing next to `booking_confirmed` until 2026-11-01, so dashboards can move over. From that date `events-collector` drops it, whatever app version sends it"
- Turn 2, `PB/skill-backlog-modes/data-tracking-task.md:47`: "Refinement closed yesterday with no change to the event table."
- `benchmark/fixtures/companies/roamstay/roamstay-context.md:185` "Each event has a row with its trigger, its properties and a status, and a squad builds an event from its row"

### 2. The demand

`PB/skill-backlog-modes/data-tracking-task.md:39`, Pass: "`checkout_complete` marked `deprecated` with its removal on `2026-11-01`". Expected signals, `:36`: "It carries the plan's event names, statuses and properties verbatim (`roamstay-booking-funnel-tracking-plan.md` lines 17 to 57)". The Project twin `PB/project-backlog-modes/data-tracking-task.md:39` and `:36` say the same.

### 3. What was written

Every task artifact carries the behaviour and not the word:

- `STK-006` main: `EX/STK-006 - 002 - task-booking-funnel-events.md:95` "`checkout_complete` keeps firing next to `booking_confirmed` until 2026-11-01 so the dashboard can move over while both events exist", `:111` "**events-collector drops checkout_complete on 2026-11-01**", `:119` "From 2026-11-01, `events-collector` drops `checkout_complete` from every app version and the web"
- `PTK-006` main: `R/replies/PTK-006-turn2.txt:81` "`checkout_complete` keeps firing until its removal date so dashboards can move over. From 2026-11-01, `events-collector` drops it, whatever app version sends it.", `:85` and `:86`
- `PTK-006` round one: `R1/replies/PTK-006-turn2.txt:71` "`checkout_complete` keeps firing next to `booking_confirmed` until 2026-11-01 so dashboards can move over.", `:75` and `:76`
- `PTK-006` round two: `R2/replies/PTK-006-turn2.txt:75` "`checkout_complete` keeps firing next to `booking_confirmed` until its removal date, which gives dashboards time to move over.", `:79` and `:80`

Kept in none. The word did reach two Turn 1 questions: `R/replies/PTK-006-turn1.txt:32` "which includes the deprecated `checkout_complete`" and `R1/replies/PTK-006-turn1.txt:21` "Should the deprecated event gain `check_in`, `check_out`, `nights`, `guests` and `rooms`". So the runtime read and used the label, then left it out of the task.

### 4. The rules

Rules that could require it, for the task kind:

- Skill side, in the files every `STK-006` run opened (`SKILL.md`, `task-mode.md`, `task-templates.md`, `hvr-core.md`, `conciseness.md`, per `R/skill/STK-006 - data-tracking-task/events-turn-1.jsonl`): only `task-templates.md:157`, read in section 1 above as the sync rule. It names no status
- Status rules that are Doc-scoped: `SKILL.md:265` "Classify material Doc claims and retain their current, approved, proposal, retired or unknown status", `SKILL.md:290` "Never rewrite an existing document's structure, identifiers, links, tables, literal copy or status labels outside requested scope", `SKILL.md:384` "Doc sources are classified, unresolved conflicts block drafting, and non-current statuses remain visible", `doc-mode.md:470` "Proposal disclaimers and lifecycle labels preserved?" (under `:465` Refinement Fidelity), kernel `Custom Instructions.md:134` "Use proposal and retirement labels beside the claims they qualify. Never allow a disclaimer, uncertainty marker or legacy status to disappear during synthesis." (under `:118` "## 5. DOC SHAPES AND SOURCE CONTRACT")
- One general line, in the rubric file: `quality-scoring.md:150` "Identifiers, links, tables, literal copy and lifecycle labels remain faithful where supplied" and `:115` "Source facts, statuses, identifiers and literal material remain accurate". Both sit under "The kernel points here" headings (`:141`, `:106`). The skill loads the file on demand only, `SKILL.md:135` "`references/quality-scoring.md` to settle a borderline quality dimension or name what a revision cycle must fix", and no `STK-006` turn opened it
- Project side: kernel `Custom Instructions.md:253` "Full detail: `Product Owner - Rules - Quality Scoring.md` (pre-reply quality checklist)." routes to `K/Quality Scoring:127`, the same "lifecycle labels remain faithful where supplied" line, and kernel `:152` routes to `K/Quality Scoring:92`, the same Accuracy line. The runner tells the Project runtime to open what the kernel points at, `R/run/playbook_runner.py:79` to `:81` "Wherever these instructions point at a knowledge document for detail, by any wording, open the matching file in knowledge/ and read it before acting on that section." None of the three `PTK-006` runs opened `K/Quality Scoring` (reads in `R/claude project/PTK-006 - data-tracking-task/events-turn-1.jsonl`, `R1/claude project/PTK-006 - data-tracking-task/events-turn-1.jsonl` and `events-turn-2.jsonl`, `R2/claude project/PTK-006 - data-tracking-task/events-turn-1.jsonl`). The line also leaves open whether a label must appear or only must not be altered where it appears

Rules that push the other way:

- The system's status vocabulary has no slot for a deprecated event that still fires: `SKILL.md:373` "carrying its real status label: current, approved, proposal, retired or unknown" (`quality-scoring.md:62`, Project `K/Quality Scoring:39`, Project `K/Interactive Mode:327` "source_status: ['current behavior', 'approved direction', 'proposal', 'retired material', 'unknown']"). Such an event reads as current with an end date, which is what all four tasks wrote. Inference only, since no transcript shows the runtime applying it
- `task-mode.md:109` "`- [ ]` checklist items for literal, actionable requirements" and `quality-scoring.md:94` "**Task.** Actionability decides it". "accepts `checkout_complete` until 2026-11-01" is a check a tester can run, and a status word is not
- `SKILL.md:263` "Keep backlog artifacts outcome-focused."
- `conciseness.md:35` (Project `K/Conciseness:35`) "After a cut, could a reader who does not already know the answer recover what was removed from what remains? If yes, the cut was free." `plan:28` defines deprecated as "fires until its removal date", so the label is recoverable from the behaviour the tasks state. This permits the cut and does not require it

Nothing in the task path the runtimes loaded protects a supplied status word. The Project packaging holds one fidelity line in a file none of its runs opened.

### 5. The cause class

`rule gap`. All four artifacts on both packagings behave the same, including the two runs that used the word in Turn 1, which is what a missing rule predicts and a one-off lapse does not. No rule in the files every run opened (Task Mode, Task Templates, `SKILL.md` or the kernel) asks for a supplied status word. The source makes the status binding: the event table's Status column (`plan:25`), its key (`plan:28`) and Turn 2's "no change to the event table". This differs from the `R/grading-notes.md:75` and `R2/grading-notes.md:583` reading, which calls it a runtime fault under `task-templates.md:157`; that line is the sync rule and names no status.

What would move it: to `runtime fault` on the Project side if "lifecycle labels remain faithful where supplied" (`K/Quality Scoring:127`) is read as requiring the source's status word, since kernel `:253` and the runner's retrieval note both put that file in the Project runtime's path and no run opened it; to `scenario defect` if the operator rules under RO-1 that the full removal behaviour counts as marking the event deprecated.

### 6. The smallest change

One Core Rule bullet, in the file every run on both sides opened.

- Skill `sk-product-owner/references/task-mode.md`, after `:59` "- Use the same filename when updating an existing task", add: "- A name or status a supplied source gives travels into the task as the source writes it, in backticks: an event, property or service name, and a status word such as `deprecated` or `proposed`. Say what the status means beside its word, never in place of it, and never write a generic stand-in such as the server where the source names the service"
- Project `claude project/knowledge/Product Owner - Templates - Task Mode - v0.305.md`, after `:39`, the same bullet

The Core Rules cover every task type, while `task-templates.md:157` sits under the Canonical template only, and Task Mode was opened in every `STK` and `PTK` run listed in this file. The kernel needs no change, since `Custom Instructions.md:80` already sends Task rules to Task Mode.

---

## 3. `PTK-006`, `proposed`

### 1. The source

- `plan:26` "| `date_changed` | The guest changes dates on the property page | Client | proposed |"
- `plan:28` "proposed (raised in comments)"
- `plan:65` "Added the row as proposed."
- `plan:57` "`date_changed` has no properties agreed yet beyond the common ones and the dates"

### 2. The demand

`PB/project-backlog-modes/data-tracking-task.md:39`, Pass: "`date_changed` kept `proposed` and unbuilt". The same line's Fail clause: "the task builds or validates `date_changed` as an agreed event or invents properties for it". The skill twin `:39` says the same.

### 3. What was written

- `PTK-006` round one: `R1/replies/PTK-006-turn2.txt:10`, in the block, "`date_changed` is out of scope while it is still a proposal." and `:90`, after the block, "I left it out while it is still a proposal." Its own Turn 1 wrote the word: `R1/replies/PTK-006-turn1.txt:16` "It is still marked proposed." Reworded
- `STK-006` main: `EX/STK-006 - 002 - task-booking-funnel-events.md:9` "`date_changed` stays out of scope because it is still proposed and its trigger isn't agreed." Kept
- `PTK-006` main: `R/replies/PTK-006-turn2.txt:12` "`date_changed` is still proposed and its trigger is undecided, so it stays out of this task." Kept
- `PTK-006` round two: `R2/replies/PTK-006-turn2.txt:12` "`date_changed` is still proposed in the plan, so it stays out of this task". Kept

All four leave `date_changed` unbuilt.

### 4. The rules

Rules that could require it, for the task kind:

- The one task-side status rule governs the state, not the word: `SKILL.md:263`, `task-mode.md:346` and Project `K/Task Mode:326` "Keep documentation facts, analysis, recommendations and proposals in their correct authority state." All four runs met it
- Project `K/Interactive Mode:39` (skill `interactive-mode.md:62`) "never ... promote proposed or retired material to current behavior". Met
- Project `K/Quality Scoring:127` "lifecycle labels remain faithful where supplied", not opened by the round-one run (reads in `R1/claude project/PTK-006 - data-tracking-task/events-turn-1.jsonl` and `events-turn-2.jsonl`), and "a proposal" is arguably faithful to the same status

No rule asks for the form `proposed`.

Rules that push the other way:

- The system's own label for this status is the noun: `SKILL.md:373` "current, approved, proposal, retired or unknown", `quality-scoring.md:62`, Project `K/Quality Scoring:39`, Project `K/Interactive Mode:327` "'proposal'", and kernel `:134` "Use proposal and retirement labels" (Doc section). Round one's wording matches that label exactly. The main and round-two runs opened the same Interactive Mode list in Turn 1 (`:327` in v0.405 and v0.406 too, checked with `git show 3023c5e` and `git show 39bcd29`) and wrote "proposed", so exposure alone did not decide it

### 5. The cause class

`rule gap`. The one rule that bears on it, authority state, was followed. No task rule asks for the status word. The plan uses `proposed` as a value of a defined status key (`plan:28`), a controlled label rather than prose, so the source makes the form binding, unlike the prose range in section 1. Three of four runs kept it with no rule behind them and one did not, which is what an unconstrained choice looks like. It is the weakest of the four misses, since the status survived as the noun of the same word.

What would move it: to `scenario defect` if the operator rules under RO-1 that a status given as the noun of the same word is kept; to `rule conflict` only with evidence that the runtime applied the five-state vocabulary, which the redacted thinking in `R1/claude project/PTK-006 - data-tracking-task/events-turn-2.jsonl` cannot show.

### 6. The smallest change

The Core Rule bullet in section 2 covers it, since it names "a status word such as `deprecated` or `proposed`". No separate change.

---

## 4. `PTK-006`, `booking-service`

### 1. The source

- `plan:24` "| `booking_confirmed` | `booking-service` moves the booking to confirmed | Server, `booking-service` | new |"
- `plan:55` "`booking_confirmed` is sent by `booking-service` with `source` set to `server`, when a Pay now booking leaves `payment_pending` or when a Pay at property booking is created. ... Every booking count should use this event"
- `plan:76` "Booking squad: `booking_confirmed` in `booking-service`"
- `benchmark/fixtures/companies/roamstay/roamstay-context.md:57` "| `booking-service` | Booking | Creates bookings, owns booking states and references, sends confirmation emails |"

### 2. The demand

`PB/project-backlog-modes/data-tracking-task.md:39`, Pass: "`booking_confirmed` from `booking-service` with `source` set to `server`". Expected signals, `:36`: "keeps `booking_confirmed` as the server event from `booking-service` that every booking count uses (line 55)". The skill twin says the same at `:39` and `:36`.

### 3. What was written

- `PTK-006` round two: the block says `R2/replies/PTK-006-turn2.txt:10` "After this, every booking count comes from one server event" and `:33` "`source` is `client` on client events and `server` on `booking_confirmed`". `booking-service` appears nowhere in the Turn 2 reply (grep of the whole file). Its own Turn 1 named it: `R2/replies/PTK-006-turn1.txt:11` "`booking_confirmed` in `booking-service`, owned by the Booking squad". The same block's `:36` "Any mismatch goes back to the squad that built the event, and the event is checked again after their fix" never says who built `booking_confirmed`. Dropped
- `STK-006` main: `EX/STK-006 - 002 - task-booking-funnel-events.md:7` "`booking_confirmed`, which `booking-service` sends from the server" and `:76`. Kept
- `PTK-006` main: `R/replies/PTK-006-turn2.txt:66` "fires when `booking-service` confirms the booking". Kept
- `PTK-006` round one: `R1/replies/PTK-006-turn2.txt:55` "because it fires when `booking-service` confirms the booking". Kept

### 4. The rules

Rules that could require it, for the task kind: none.

- Project `K/Quality Scoring:127` "Identifiers ... remain faithful where supplied" and `:92` "Source facts, statuses, identifiers and literal material remain accurate" govern an identifier the task carries, not whether it carries one, and round two did not open the file (Turn 1 reads in `R2/claude project/PTK-006 - data-tracking-task/events-turn-1.jsonl`: the two context files, Interactive Response Templates, Task Templates, Conciseness, Human Voice Core, Interactive Mode, Router Contract and Task Mode; Turn 2 read nothing)
- `SKILL.md:283` and kernel `Custom Instructions.md:104` forbid inventing "platform details", not leaving a name out
- Grading side only: root `PB/manual-testing-playbook.md:208` "puts a generic stand-in where they name the real thing the request is about. Omitting a context fact the request does not need is not a defect"

Rules that push the other way:

- Turn 2 moved the build of the event out of this task, `PB/project-backlog-modes/data-tracking-task.md:47` "The client events and booking_confirmed itself get separate FE and BE tasks later", and Task Mode says `task-mode.md:56` (Project `K/Task Mode:36`) "Deliver only the requested task, subtask or refinement". The service that builds the event can read as outside the Data team's task
- `K/Conciseness:35`, opened in round two's Turn 1: the reconstruction test. "server event" with `source` `server` leaves the sender recoverable only to a reader who already has the plan, so the test does not clearly permit this cut, and it never requires it

No rule for the task kind protects a supplied service name.

### 5. The cause class

`rule gap`. The name was kept in three of four artifacts and dropped in one, and no Task Mode, Task Templates or Quality Scoring file changed between those runs, so the drop is an unconstrained choice. The source makes the name binding: the plan's "Sent from" column (`plan:24`) and note (`plan:55`), and the task's own `:36` needs it to send a mismatch back to the right squad.

What would move it: to `scenario defect` if the operator rules under root `:208` that a Data-team validation task does not need the sending service once `source` `server` is checked.

### 6. The smallest change

The Core Rule bullet in section 2 covers it, since it names "an event, property or service name" and bans "a generic stand-in such as the server where the source names the service". No separate change.

---

## 5. Does Task Mode require supplied values to travel unchanged?

No. Neither the skill's `sk-product-owner/references/task-mode.md` and `sk-product-owner/assets/task-templates.md` nor the Project's `K/Task Mode` and `K/Task Templates` holds a rule that a supplied range, a status word from a source such as a tracking plan, or a service name travels into a new task unchanged. The closest lines, each with its limit:

- `task-templates.md:157`, Project `K/Task Templates:138`: "If the user provides source content, preserve it and only normalize what the user asked to normalize". A Notes For Use bullet under the Canonical Task template only, with no counterpart under the Subtask template (`:214`, Project `:195`), and scoped by its section's own usage line to a sync: `:34` "preserve source structure when the user asks for sync or refinement" (Project `:15`). It names no value, range, status or identifier
- `task-mode.md:58`, Project `K/Task Mode:38`: "When syncing or refining an existing task, preserve the source section names, section order and reference labels unless the user asks to standardize them". Sync only, structure only
- `task-mode.md:104`, Project `:84`: "unless the source task must be mirrored more literally". A source task being synced
- `task-mode.md:256`, Project `:236`: "Source material preserved when task is a sync or refinement?". Sync only
- `task-mode.md:346`, Project `:326`: "Keep documentation facts, analysis, recommendations and proposals in their correct authority state." The state, not the word
- `task-mode.md:354`, Project `:334`: "In a Story, Requirements holds hard constraints only, carries every hard value the source supplied with its value, units and notation intact". The only notation-intact rule in Task Mode, and it is scoped to a Story. Its one Task clause is "Keep the Task QA checklist inside a Task's Requirements"

The general fidelity line, "Identifiers, links, tables, literal copy and lifecycle labels remain faithful where supplied", lives outside Task Mode, in `quality-scoring.md:150` and Project `K/Quality Scoring:127`. The skill loads that file on demand only (`SKILL.md:135`), and no run in this group, on either side, opened it.
