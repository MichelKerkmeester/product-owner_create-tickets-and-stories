---
title: "Product Owner: Manual Testing Playbook"
description: "Operator-facing directory, execution policy and release-readiness guide for the two-runtime Product Owner manual validation package."
version: 2.0.0.0
---

# Product Owner: Manual Testing Playbook

This package turns the Product Owner contract into 46 reproducible conversations across two runtimes, each one a realistic request at one of three fictional companies. The skill set (`S`-prefixed IDs) runs the system from `AGENTS.md` with `sk-product-owner/` loaded. The Project set (`P`-prefixed IDs) runs the same system from `claude project/Custom Instructions.md` with that system's knowledge documents attached. The root owns shared policy and indexing. Each linked scenario file owns one synchronized Turn 1 prompt, its attachment list, a conversation chain, one nine-field execution table and current source anchors.

---

### Result persistence

<!-- MANUAL_PLAYBOOK_RESULT_PERSISTENCE_CONTRACT -->
A scenario run is complete only after its `PASS`, `FAIL` or `SKIP` outcome and reason are persisted into `benchmark/reports/<dated-run-label>/`. Generated report Markdown is renderer-owned and never hand-authored.

---

## 1. OVERVIEW

The playbook covers 46 scenarios in two mirrored sets of 23, grouped under ten category folders and set at Roamstay, Loomlist and Fernhouse. No alternate or supplemental scenario files are part of the package.

Each set ends in 7 tasks, 3 bugs, 5 Stories, 4 Epics and 4 docs. The interactive pair supplies one of those Epics and one of those Stories. Its Turn 1 asks one intake question, and Turn 2 picks an Epic at Deeper energy in `SIR-001` and `PIR-001` and a Story at Quick energy in `SIR-002` and `PIR-002`. One Story is a refinement of a supplied draft, and one is a bundle holding 4 nested tasks. Three scenarios per set run one turn and the other 20 run two, 86 turns in all.

### Coverage map

| Category | IDs | Count | Primary surface |
|---|---|---:|---|
| Skill identity | `SID-001` | 1 | Skill delivery contract handover on a Loomlist task |
| Skill backlog modes | `STK-001..STK-006`, `SBG-001..SBG-003` | 9 | Quick, FE, BE and DATA tasks, a parent and subtask pair and three bug depths, filesystem delivery |
| Skill document modes | `SDK-001..SDK-004` | 4 | Behavior reference, runbook, proposal and the catalog conflict gate |
| Skill story modes | `SST-001..SST-004`, `SEP-001..SEP-003` | 7 | Stories with hard values and forced Delivery, a refinement, the Story bundle and three Epics |
| Skill interactive routing | `SIR-001`, `SIR-002` | 2 | Vague intake ending in an Epic and conflicting commands ending in a Story, intake clarification export |
| Project identity | `PID-001` | 1 | Project Deliverable Block handover on a Loomlist task |
| Project backlog modes | `PTK-001..PTK-006`, `PBG-001..PBG-003` | 9 | The same tasks and bugs as Deliverable Blocks |
| Project document modes | `PDK-001..PDK-004` | 4 | The same docs and the conflict stop in a Project |
| Project story modes | `PST-001..PST-004`, `PEP-001..PEP-003` | 7 | The same Stories, bundle and Epics as Deliverable Blocks |
| Project interactive routing | `PIR-001`, `PIR-002` | 2 | Vague intake ending in an Epic and conflicting commands ending in a Story, clarification block |

### Two runtimes, one system

Both sets test the same Product Owner contract against the surface that actually runs it, never one system tested twice. A skill-side reply is only genuine when it names a real readable path under `export/` and prints the read-back verification line. A Project-side reply is only genuine when it renders the Deliverable Block as a Canvas Artifact, or as its own block where the runtime has no Canvas panel (section 5), reports `Export-equivalent path:` and makes no claim that a file was saved, written or read back. A reply that could have come from either runtime fails the scenario that produced it. The handover files `SID-001` and `PID-001` carry the four greps that prove the vocabulary split, and every other scenario names its runtime's handover as a precondition.

### Realistic test model

1. Prepare a disposable copy of `Product Owner/` for skill-side runs, or a fresh Claude Project holding the kernel and knowledge documents for Project-side runs, and stage the scenario's attachments (section 2, Company context and attachments)
2. Start a fresh session unless the scenario explicitly continues the same conversation
3. Submit every turn exactly as written
4. Capture the assistant response, retained state and filesystem changes after every turn
5. Record `PASS`, `FAIL` or a specifically justified `SKIP`

Run every scenario against the real runtime. Do not mock responses.

### No-feature-catalog exception

This skill has no canonical feature catalog. Scenario files link directly to current skill, reference, asset and Project sources, and to the company fixtures they attach. Section 18 is the source cross-reference.

### Natural Turn 1 coverage

At least two scenarios per set open with a Turn 1 that carries no command token, no leading slash and no dollar-prefixed flag: `STK-006`, `SDK-001`, `SST-001`, `SEP-002` and `SIR-001` on the skill side, `PTK-006`, `PDK-001`, `PST-001`, `PEP-002` and `PIR-001` on the Project side. The reason is measured rather than stylistic: the 2026-09-16 comparison run on Barter Deal Templates gave two readers the same six prompts, one restricted to that system's Project package and one to its skill, and found that, on that system, a user naming an energy in plain words is covered by no rule in either packaging.

---

## 2. GLOBAL PRECONDITIONS

1. Work only in a disposable project copy for skill-side runs, never inside the authoritative `sk-product-owner/` tree
2. Confirm `AGENTS.md`, `sk-product-owner/` and a writable `export/` directory exist before skill-side runs
3. Attach `claude project/Custom Instructions.md` plus the full `claude project/knowledge/` set before Project-side runs
4. Stage the scenario's attachments into `context/` on both runtimes, exactly as its `- Attachments:` bullet lists them (Company context and attachments, below)
5. Run the runtime's handover scenario first: `SID-001` leads the `S` set and `PID-001` the `P` set. A failed handover is flagged, never a stop (section 5, Handovers in an automated run)
6. Record the `export/` baseline before each skill-side scenario, and each staged attachment's checksum before Turn 1 on both runtimes
7. Use a fresh session per ID and keep follow-up turns inside that same ID and session
8. Do not use production credentials, private partner data or live ClickUp access, and never let a ClickUp push become part of a verdict
9. Remove only scenario-created files after evidence capture, and never edit a fixture under `benchmark/fixtures/companies/`

No scenario in this package is destructive. Skill-side runs only add new `export/` files inside the disposable copy and Project-side runs write nothing, so precondition 9 is the only cleanup path needed.

### Company context and attachments

Every scenario is set at one of three fictional companies and attaches that company's context document. The fixtures live under [`benchmark/fixtures/companies/`](../../benchmark/fixtures/companies/), one folder per company.

| Company | What it is | Surfaces | Folder |
|---|---|---|---|
| Roamstay | A hotel booking marketplace | Guest app on iOS, Android and web, Partner Hub for hotels, Back office | [`roamstay/`](../../benchmark/fixtures/companies/roamstay/) |
| Loomlist | A workspace of pages, databases and to-dos | Desktop, Web, iOS and Android, kept in step by a sync service | [`loomlist/`](../../benchmark/fixtures/companies/loomlist/) |
| Fernhouse | A home and kitchen store selling direct to consumers | Web storefront, iOS and Android app, Admin, warehouse and carrier integrations | [`fernhouse/`](../../benchmark/fixtures/companies/fernhouse/) |

Each folder holds `<company>-context.md`, with the company's surfaces, teams, discipline codes, platforms, versions and conventions. It also holds the source attachments its scenarios cite: support tickets, a log excerpt, team threads, PM briefs, design notes, API notes and two drafts.

The staging rule is the same on both runtimes:

- A scenario's `- Attachments:` bullet is its one list. It links each file under `benchmark/fixtures/companies/<company>/`, the company's context file first, then the sources in the order Turn 1 names them
- Before the baseline, the runner copies each listed file to `context/<basename>` in the skill sandbox and in the Project sandbox alike. Turn 1 names each one by that path
- An attachment is never modified. The runtime reads it and never rewrites, renames or deletes it. A refinement saves its copy under `export/` instead (section 5, Export names)
- Nothing else sits in `context/`. The runner stops before any scenario runs when a link does not resolve or two attachments share a basename, and its isolation proof fails a run whose `context/` holds an extra, a missing or an altered file

The skill sandbox copy leaves out `benchmark/`, so staging is the only way a fixture reaches either runtime. In a claude.ai Project run by hand, attach the same files to the conversation under their basenames, beside the kernel and the knowledge set. An `S` scenario and its `P` twin always attach the same files.

### Side-effect ledger

| Turn | Files before | Files after | Created | Modified | Deleted | Allowed? |
|---|---|---|---|---|---|---|
| 1 | Operator capture | Operator capture | Exact paths | Exact paths | Exact paths | Yes/No with reason |

Clarification turns may create only the expected `-clarification` export on the skill side. A Story with its tasks creates one bundle folder holding the Story and its task files, and a refinement creates one export under its source's file name. No turn may create, modify or delete anything under `context/`. Project-side runs create no files at all.

---

## 3. GLOBAL EVIDENCE REQUIREMENTS

- Runtime identifier and profile (skill CLI run or Claude Project)
- The staged attachment list, each file with its checksum before Turn 1 and after the last turn
- Exact prompts and the full response after every turn
- Per-turn state-retention notes
- Per-turn side-effect ledger on the skill side
- Resource or knowledge-routing notes when observable
- Export read-back proof on the skill side, or Deliverable Block capture on the Project side
- The `HVR self-scan:` line from every delivery response
- Final `PASS`, `FAIL` or justified `SKIP` with rationale

---

## 4. DETERMINISTIC COMMAND NOTATION

- `sandbox:` prepares or inspects the disposable project copy and stages the scenario's attachments into `context/`
- `session:` starts or continues a conversation in the runtime under test
- `user:` submits the exact text shown for a turn
- `filesystem:` records and reads allowed artifacts, skill side only
- `canvas:` inspects the rendered Deliverable Block, Project side only, and reads the reply text where the runtime has no Canvas panel
- `operator:` compares observed behavior with the contract
- `->` separates sequential steps

### Prompt synchronization gate

For every ID, the scenario-contract `Prompt`, the execution-table `Exact Prompt` and the root summary `Prompt` text must match character for character. The `Real user request` line is natural human voice and is not part of this gate. An `S` scenario and its `P` twin carry every turn input word for word and the same `- Attachments:` list. The validator never compares two files, so the operator and the run's selftest check twins.

---

## 5. REVIEW PROTOCOL AND RELEASE READINESS

### Scenario acceptance rules

A scenario passes only when the exact sequence ran, every turn matched expected behavior, prior facts remained intact, the ledger contains only allowed changes and any returned path matches the delivery evidence for that runtime.

- `PASS`: every required check is true
- `FAIL`: any critical signal, state, artifact or boundary is wrong
- `SKIP`: a named sandbox or runtime blocker prevents execution and no safe deterministic fallback exists

Each scenario's Fail bullet names the likely failures and is not a complete list. A turn that misses any Pass clause fails the scenario even when no Fail example describes the miss, so there is no verdict between `PASS` and `FAIL`.

### Clarification turns

A clarification is a delivery on both runtimes. `references/interactive-mode.md` line 85 exports it like any other deliverable and line 93 reports its path exactly as an artifact delivery does. The `Product Owner - System - Interactive Mode` knowledge file says the same for the Project at lines 62 and 70. The `HVR self-scan:` line belongs to every delivery response (`SKILL.md` line 217, `Custom Instructions.md` line 89). Every turn-1 clarification check in this package therefore includes these:

- Skill side: the question-only file saved under its lane's `-clarification` name and read back, and a reply carrying its path, the `Verified: read-back succeeded; N lines` line and the `HVR self-scan:` line. Whether the reply also prints the question is not graded either way. `references/interactive-mode.md` asks the user the question, while `AGENTS.md` Section 2 keeps a full artifact out of chat and the file is that artifact. The tension is logged as a follow-up finding
- Project side: the question rendered as its own block, then `Export-equivalent path:` with the `-clarification` name and the `HVR self-scan:` line

The lane is the routed artifact's word, one of `{task|bug|doc|Story|Epic}`, or `intake` when no artifact was resolved (`SKILL.md` line 208, `Custom Instructions.md` line 228). A Story asked for with its tasks asks in the Story lane at the top of `export/`, outside the bundle folder, and the folder takes the next number (`references/interactive-mode.md` line 93, line 70 of the knowledge file).

### Rendering without a Canvas panel

The kernel delivers every artifact as a Canvas Artifact in the side Canvas panel and renders the Deliverable Block before any commentary (`Custom Instructions.md` lines 76 and 85). A terminal run, the playbook runner included, gives the Project runtime no Canvas panel. There the block counts as rendered when the artifact or the clarification question sits in the reply as one delimited block, either fenced or opened by its own heading and closed where the `Export-equivalent path:` line begins. Commentary before the block is a response-ordering defect. Record it, and let it fail a scenario only when the scenario tests delivery shape, as Defect severity says. `PID-001` is such a scenario. `canvas:` steps read the reply text, and the panel baseline is empty. The kernel asks for the rendering and the `Export-equivalent path:` label, not for the words, so no reply is graded on printing `Canvas Artifact` or `Deliverable Block`. Record which form the block took.

### Export names

The `[description]` part of every path a scenario names is illustrative, because the rules fix the pattern and not the slug (`SKILL.md` lines 207 and 208, `Custom Instructions.md` lines 223 to 228). Grade the artifact word (`task`, `bug`, `doc`, `Story`, `Epic` or `intake`) and the `-clarification` suffix on both runtimes. On the skill side grade the order too, with the clarification first and the artifact on the next number. On the Project side `[NNN]` is a placeholder the human reconciles (`Custom Instructions.md` line 233), so number order is not graded there.

A new Story asked for with its tasks saves as one bundle folder, `export/[###] - Story-[description]/`, holding `[###] - Story-[description].md` and one `[###].[n] - task-[description].md` per task (`AGENTS.md` lines 84 to 91, `references/story-mode.md` lines 392 to 409, `Custom Instructions.md` line 226). Grade the folder, the artifact word on every file in it and `n` counting from 1 in the Story's task order, on both runtimes. The `n` suffix is not a number the human reconciles. On the Project side each file gets its own Deliverable Block, Story first, each with its own `Export-equivalent path:` inside the folder.

A refinement keeps its source file name, with no number and no artifact word (`AGENTS.md` lines 70 to 73, `SKILL.md` line 209, `Custom Instructions.md` lines 229 to 231). The refinement of `context/fernhouse-save-card-draft.md` therefore exports `export/fernhouse-save-card-draft.md` on the skill side and reports that same name as its `Export-equivalent path:` on the Project side. Grade that exact name on both runtimes. It carries no number, so there is no number order to grade for it. The source in `context/` stays unchanged.

### Handovers in an automated run

Every scenario runs in its own fresh sandbox or conversation, so a handover hands nothing on to the scenarios after it. The playbook runner runs `SID-001` and `PID-001` first but does not hold the rest of a set on their verdict. Grade every scenario in both sets, whatever the handovers return. When a handover fails, state that failure at the top of the run report, before any other result, and name the runtime whose other verdicts it puts in question. A scenario whose precondition says its handover passed reads, in an automated run, as the handover having run first in its own session. Its verdict gates nothing.

### Identity handover rule

`SID-001` and `PID-001` prove the runtime, not only the artifact. A reply that could have come from either runtime is a `FAIL`. Both handovers are the same two-turn `$task` chain for a Loomlist task. `$task` still asks its context question before drafting (`AGENTS.md` line 287), so Turn 1 delivers the task-lane clarification and Turn 2, the answer, delivers the task on the next number. Turn 2 answers the question rather than asking about the delivery, so each turn is a delivery and the proof is graded on both. The skill side must name a real readable `export/` path and print the read-back confirmation fixture `Verified: read-back succeeded` with its line count. The Project side must render the Deliverable Block, or the clarification question as its own block, in the form Rendering without a Canvas panel describes when there is no panel, and report `Export-equivalent path:`. Its reply passes when it makes no claim that any file was saved, written or read back. It does not have to say out loud that no file was written. The skill proof string is `read-back succeeded` and the Project proof string is `Canvas Artifact`. Each handover file carries the four greps that show a proof string appears only in its own identity file. The Project string proves the packaging through those greps and is not required in a reply.

### Defect severity

Record both the verdict and the severity that drove it.

Blocking, any one of which is a `FAIL`:

- An invented fact: a requirement, value, status, approval or behavior the user never supplied. The one exception is a disclosed addition: an edge case, assumption or other addition the reply names as an addition in its chat response is not an invented fact and does not fail the scenario (`SKILL.md` line 283, `Custom Instructions.md` line 104). A reply that names a criterion or other whole item as an addition has named every clause inside it. An addition the reply does not name stays blocking, and naming never excuses an invented status, approval, evidence, root cause or platform detail, or any other item in this list. A root cause the artifact labels as an unverified hypothesis, the way the skill's own bug examples do (`assets/examples/bug/bug-example-mobile-crash.md` line 68, the Project's Mobile Crash example line 67), is not an invented root cause. A cause stated as fact, or one cause given to two separate issues, still is
- A protected fact altered: a supplied value generalized, a conflict silently resolved or a proposal promoted to current behavior
- A path claim with no readable file behind it on the skill side, or any file claim at all on the Project side
- A missing `HVR self-scan:` line or a count that was never taken
- Process material inside a delivered artifact body: scores, self-scan lines, mode or energy headers outside a line-1 HTML comment

Advisory, recorded without failing unless the scenario tests delivery shape:

- Response ordering and commentary length
- Progress-note verbosity

### Ticket realism

Ticket realism grades whether a delivered artifact reads like work a team at the scenario's company would pick up. It adds five Blocking and four Advisory items beside Defect severity and changes none of that list's items. A Blocking item here is a `FAIL` exactly as a Defect severity one is. Record the item name beside the verdict.

| Severity | Item | Boundary |
|---|---|---|
| Blocking | Wrong artifact word | The export word or the kind the reply names differs from the routed kind, a Story saved under the old `PRD` export word included. This is the Export names check already graded, stated once |
| Blocking | A required section of the routed template missing | Required for the shape and energy the reply resolved, read from that runtime's own template: the skill asset or the Project knowledge mirror. A section the template marks optional or opt-in, such as Story `## Requirements` with no hard value or `## Delivery` nobody forced, is never required |
| Blocking | An invented fact | Exactly the Defect severity definition, the disclosed-addition exception, the whole-item naming sentence and the labelled-hypothesis reading included. The rubric adds no stricter reading |
| Blocking | Placeholder or toy content | An unfilled slot (`{...}`, `{LINK}`, `TODO`, lorem ipsum) or a stand-in name or value where the turns or an attachment supply the real one. Exempt: the Project `[NNN]` path slot, the bug template's `Not provided`, Story Mode's `TBD...` in the three Delivery slots, every fixed template line and a placeholder quoted verbatim from an attached source, such as `Conflicting edit from {device name}` in the Loomlist sync thread, braces included |
| Blocking | Context facts ignored or altered | The artifact states a name, surface, service, number, code, platform or version the attachments or turns contradict, or puts a generic stand-in where they name the real thing the request is about. Omitting a context fact the request does not need is not a defect |
| Advisory | Size band | The artifact body's line count against the band the scenario records. Never a failure, whatever the scenario tests |
| Advisory | Commentary | Unchanged from Defect severity, its delivery-shape exception for `PID-001` included |
| Advisory | Asking for a fact an attachment already states | Recorded as it is today, never a failure |
| Advisory | A Task or Bug title with no discipline code | No routed template asks for one, so it is recorded only. Story and Epic H1s follow the skill's H1 rule, which bans `BO`, `BE` and `FE` short codes and a `PRD -` prefix, so neither the rubric nor any Pass clause expects a code there |

These existing readings stay exactly as they are, and no rubric item turns one into a failure: response ordering and commentary length, progress-note verbosity, commentary before a Project block, the skill reply printing the clarification question, Project number order and the illustrative `[description]` slug.

### Release readiness rule

The system is ready only when every scenario has evidence, no scenario is `FAIL`, every handover is `PASS`, every `SKIP` names a real blocker and no blocking triage item remains. Documentation validation alone does not prove runtime readiness.

---

## 6. ORCHESTRATION AND WAVE PLANNING

| Wave | Scenarios | Isolation |
|---|---|---|
| 1 | `SID-001`, `PID-001` | One fresh session per runtime, handovers run first |
| 2 | `STK-001..STK-006`, `PTK-001..PTK-006` | Separate task baselines per runtime, the parent and subtask pair included |
| 3 | `SBG-001..SBG-003`, `PBG-001..PBG-003` | Separate bug baselines per runtime |
| 4 | `SDK-001..SDK-004`, `PDK-001..PDK-004` | Separate doc baselines, clarification exports allowed |
| 5 | `SST-001..SST-004`, `SEP-001..SEP-003`, `PST-001..PST-004`, `PEP-001..PEP-003` | Story and Epic baselines, one bundle folder and one refinement export allowed |
| 6 | `SIR-001..SIR-002`, `PIR-001..PIR-002` | Intake clarification baselines |

Every wave stages each scenario's attachments into its own sandbox before the baseline. One coordinator owns exact prompts, attachment staging, sandbox isolation, ledgers and final verdicts. Workers may execute independent IDs in separate sandboxes or Projects.

---

## 7. SKILL IDENTITY (`SID-001`)

### SID-001 | Skill identity handover

#### Description

Verify skill identity through two filesystem deliveries, a task-lane clarification and then the task, each with a real readable export path and the read-back confirmation.

#### Scenario contract

Prompt: `$task Small front end task for a "Due today" filter chip on the To-dos view, the chips we have today are described in context/loomlist-context.md`

Desired user-visible outcome: A saved task-lane question, then a saved task for the "Due today" chip, each reported path first with the skill-only delivery lines.

#### Test execution

> **Feature file:** [SID-001](skill-identity/identity-handover.md)

---

## 8. SKILL BACKLOG MODES (`STK-001..STK-006`, `SBG-001..SBG-003`)

### STK-001 | Quick copy task

#### Description

Verify that Quick energy on a fully specified copy change skips intake and saves a faithful Fernhouse quick task.

#### Scenario contract

Prompt: `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.`

Desired user-visible outcome: One quick task export for the banner copy change, delivered with its path and no question asked.

#### Test execution

> **Feature file:** [STK-001](skill-backlog-modes/quick-copy-task.md)

### STK-002 | Design notes FE task

#### Description

Verify task routing, the single context question and a front end task that keeps every value from the design notes and every fact from the answer.

#### Scenario contract

Prompt: `$task FE task for the stay limits in the Guest app date picker. Ines's handover notes are in context/roamstay-date-picker-design-notes.md and our ticket conventions in context/roamstay-context.md.`

Desired user-visible outcome: One saved task-lane question, then a saved front end task for the date picker stay limits built from the notes and the answer.

#### Test execution

> **Feature file:** [STK-002](skill-backlog-modes/design-notes-fe-task.md)

### STK-003 | Long BE integration task

#### Description

Verify the `$t` shortcut, the single context question and a long back end task that keeps every carrier value and thread decision and adds nothing the sources do not state.

#### Scenario contract

Prompt: `$t BE task for the label webhook fix, Joris is taking it. The carrier API facts are in context/fernhouse-carrier-label-api-notes.md, the fix Noor summarised is at the end of context/fernhouse-carrier-label-thread.md and our ticket conventions are in context/fernhouse-context.md. Scope is the five points from the thread: answer inside the carrier's timeout and work from a queue, dedupe on event_id, guard against a second open shipment for a parcel, the 10-minute GET for stragglers and the alerting. Polling only stays out, the thread rejected it.`

Desired user-visible outcome: One saved task-lane question, then a saved back end task for label webhook idempotency and retries that a Fulfilment engineer can build and test from.

#### Test execution

> **Feature file:** [STK-003](skill-backlog-modes/long-be-integration-task.md)

### STK-004 | Parent task with subtasks

#### Description

Verify task routing, the single context question and one parent task that lists four subtasks by title and states the brief's shared rules once.

#### Scenario contract

Prompt: `$task Parent task for recurring to-dos from Ines's brief in context/loomlist-recurring-todos-pm-brief.md, with subtasks for iOS, Android, web and BE. Board conventions are in context/loomlist-context.md.`

Desired user-visible outcome: One saved task-lane question, then one saved parent task that lists four subtasks by title and states the recurring to-do rules once.

#### Test execution

> **Feature file:** [STK-004](skill-backlog-modes/parent-task-with-subtasks.md)

### STK-005 | Supplied parent subtask

#### Description

Verify subtask routing, the single context question and an Android subtask that names its supplied parent, keeps the parent's shared rules and holds only Android client work.

#### Scenario contract

Prompt: `$task --subtask Android subtask of the recurring to-dos parent in context/loomlist-recurring-todos-parent-task.md. Board conventions are in context/loomlist-context.md.`

Desired user-visible outcome: One saved task-lane question, then a saved Android subtask under its named parent that an Android engineer can build and test from.

#### Test execution

> **Feature file:** [STK-005](skill-backlog-modes/supplied-parent-subtask.md)

### STK-006 | Data tracking task

#### Description

Verify natural-wording task routing, the single scope question and a DATA task that keeps every status and value from the tracking plan and every scope fact from the answer.

#### Scenario contract

Prompt: `Can you write a task for the booking funnel events in Nadia's tracking plan, context/roamstay-booking-funnel-tracking-plan.md? Our conventions are in context/roamstay-context.md.`

Desired user-visible outcome: One saved task-lane question, then a saved DATA task for the booking funnel events that the Data team can work and check from.

#### Test execution

> **Feature file:** [STK-006](skill-backlog-modes/data-tracking-task.md)

### SBG-001 | Quick bug

#### Description

Verify that Quick energy on a complete one-line bug skips intake and saves a faithful Fernhouse bug report.

#### Scenario contract

Prompt: `$quick $bug iOS 4.8.0, the cart badge keeps the old count after an item is removed. Put 2 of one product and 1 of another in the cart so the tab bar badge reads "3", open the cart and tap "Remove" on the single item. The cart then holds 2 units but the badge stays on "3" until the app is restarted. Happens every time on both our iOS test phones, while Android 4.8.2 and web update the badge straight away. Severity Medium, product context is in context/fernhouse-context.md`

Desired user-visible outcome: One compact bug export for the iOS cart badge, delivered with its path and no question asked.

#### Test execution

> **Feature file:** [SBG-001](skill-backlog-modes/quick-bug.md)

### SBG-002 | Support ticket bug

#### Description

Verify the single evidence question, the wait state and a bug that keeps the ticket's values, scope and charge-versus-display fact.

#### Scenario contract

Prompt: `$bug Guest Support escalated ticket 58213 to Booking. On Android the confirmation screen leaves city tax out of the total on stays of 2 nights or more, so the guest saw "Total €387.00" and was charged €405.00. The ticket with Maren's tests is in context/roamstay-support-ticket-58213.md and our product context is in context/roamstay-context.md`

Desired user-visible outcome: One evidence question saved as a clarification, then one bug export for the Booking squad that a developer can reproduce from without reopening the ticket.

#### Test execution

> **Feature file:** [SBG-002](skill-backlog-modes/support-ticket-bug.md)

### SBG-003 | Two-platform log bug

#### Description

Verify the single evidence question, the wait state and one bug that keeps two platform issues as two observed and expected pairs with no invented cause.

#### Scenario contract

Prompt: `$b Reminders arrived an hour late after the March clock change, one-off reminders on Android and daily ones on iOS. Please write it up as one bug for the To-dos and Reminders team from Ruben's log lines in context/loomlist-reminders-dst-log-excerpt.md and Marta's support reports in context/loomlist-reminders-dst-user-reports.md, with our product context in context/loomlist-context.md`

Desired user-visible outcome: One evidence question saved as a clarification, then one bug export for the To-dos and Reminders team that keeps the Android and iOS issues apart and reads the log as evidence.

#### Test execution

> **Feature file:** [SBG-003](skill-backlog-modes/two-platform-log-bug.md)

---

## 9. SKILL DOCUMENT MODES (`SDK-001..SDK-004`)

### SDK-001 | Behavior reference

#### Description

Verify no-command Doc routing, the five-field Doc intake question and a ClickUp behavior reference that keeps Fernhouse's current and retired promotion rules apart.

#### Scenario contract

Prompt: `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.`

Desired user-visible outcome: One question that settles the doc before any drafting, then a behavior reference CS agents and the Checkout engineers can use to predict the discount on any cart.

#### Test execution

> **Feature file:** [SDK-001](skill-document-modes/behavior-reference.md)

### SDK-002 | Incident runbook

#### Description

Verify the Doc intake question under `$doc` and a ClickUp runbook that follows the incident notes' procedure and keeps the proposed dual-secret window proposed.

#### Scenario contract

Prompt: `$doc We need a doc on handling payment webhook failures, like the INC-0412 outage. Start with context/roamstay-payment-webhook-incident-notes.md, and context/roamstay-context.md has the company background.`

Desired user-visible outcome: One question that settles the doc before any drafting, then a runbook the Payments on-call engineer can follow from the alert to the cleanup.

#### Test execution

> **Feature file:** [SDK-002](skill-document-modes/incident-runbook.md)

### SDK-003 | Proposal with a decision owner

#### Description

Verify the Doc intake question under `$d` and a ClickUp proposal that lays out the three sync conflict options, attributes support and leaves the decision with its owner.

#### Scenario contract

Prompt: `$d Can you write up where we are on sync conflicts and the lost edits? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.`

Desired user-visible outcome: One question that settles the doc before any drafting, then a proposal the Sync and Mobile engineers and the Support lead can read before the decision without mistaking any option for the chosen one.

#### Test execution

> **Feature file:** [SDK-003](skill-document-modes/proposal-decision-owner.md)

### SDK-004 | Catalog conflict gate

#### Description

Verify the conflict stop on the digest send time, the consolidated clarification export and a ClickUp catalog that follows the user's authority decision.

#### Scenario contract

Prompt: `$doc Can you pull the six activity emails into one reference page? So far I have context/loomlist-notification-spec.md and context/loomlist-email-template-inventory.md, plus context/loomlist-context.md for background.`

Desired user-visible outcome: A clarification export that names the conflict, then one catalog of the six activity emails after the user says which source governs.

#### Test execution

> **Feature file:** [SDK-004](skill-document-modes/catalog-conflict-gate.md)

---

## 10. SKILL STORY MODES (`SST-001..SST-004`, `SEP-001..SEP-003`)

### SST-001 | Story hard values

#### Description

Verify that a no-command Story request waits for the promised input, then exports one house-format Story that keeps every hard value from the PM notes verbatim.

#### Scenario contract

Prompt: `Can you write up the free cancellation filter as a story for the Search squad? Tomas's notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md. Guest Support sent me two asks for it as well, I'll pass them on.`

Desired user-visible outcome: One Story question that collects the Guest Support asks, then one house-format Story export that names its kind and keeps every value as the notes wrote it.

#### Test execution

> **Feature file:** [SST-001](skill-story-modes/story-hard-values.md)

### SST-002 | Story forced delivery

#### Description

Verify that an open question in the source stays open as an `**Open:**` line and forces the `## Delivery` close in the exported Story.

#### Scenario contract

Prompt: `$story View-only share links for the Sharing team, from Kofi's design notes in context/loomlist-view-only-links-design-notes.md. Workspace background is in context/loomlist-context.md.`

Desired user-visible outcome: One Story question, then one house-format Story export that names its kind, marks the sub-page question as open and closes on the Delivery section that open question forces.

#### Test execution

> **Feature file:** [SST-002](skill-story-modes/story-forced-delivery.md)

### SST-003 | Story refinement

#### Description

Verify an authorized restructure of a rough Story draft into the house shape under the source file name, with every supplied value intact.

#### Scenario contract

Prompt: `$s Priya's rough save card draft is in context/fernhouse-save-card-draft.md, can you bring it into our house Story format before the Checkout team picks it up? Restructure whatever it needs. Company background is in context/fernhouse-context.md.`

Desired user-visible outcome: One Story question, then one refined Story saved under the draft's own file name, in the house shape, with every value the draft and the turns supplied.

#### Test execution

> **Feature file:** [SST-003](skill-story-modes/story-refinement.md)

### SST-004 | Story with nested tasks

#### Description

Verify that a Story asked for with its task breakdown saves as one bundle folder whose Story and four tasks link each other, in the split the PM names, with every supplied value intact.

#### Scenario contract

Prompt: `$story Order tracking on the order page, from Hamid's brief in context/fernhouse-order-tracking-pm-brief.md and Yusuf's carrier notes in context/fernhouse-carrier-tracking-api-facts.md. Please break it into tasks. Company background is in context/fernhouse-context.md.`

Desired user-visible outcome: One Story question in the Story lane, then one bundle folder holding the order tracking Story and its four tasks, linked both ways, with every path read back.

#### Test execution

> **Feature file:** [SST-004](skill-story-modes/story-with-nested-tasks.md)

### SEP-001 | Epic from strategy brief

#### Description

Verify that `$epic` on a strategy brief asks one Epic question, then saves a house-format Epic whose child stories, numbers and boundaries come from the brief.

#### Scenario contract

Prompt: `$epic Partner Hub self-onboarding from Freya's strategy brief in context/roamstay-partner-self-onboarding-brief.md, company context is in context/roamstay-context.md. We haven't agreed the first release cut yet.`

Desired user-visible outcome: One Epic question, then one Roamstay Epic the Partner, Ops Tools and Payments squads can plan from, with the brief's numbers intact.

#### Test execution

> **Feature file:** [SEP-001](skill-story-modes/epic-from-strategy-brief.md)

### SEP-002 | Epic natural wording

#### Description

Verify that a no-command request to write an epic resolves the Epic shape and lane, asks one Epic question, then saves an Epic that keeps the brief's scope, numbers and open dependency.

#### Scenario contract

Prompt: `Can you write an epic for offline mode from Oskar's brief in context/loomlist-offline-mode-brief.md? Our product context is in context/loomlist-context.md. I'm not sure yet whether the child stories should follow his four areas or be split per platform.`

Desired user-visible outcome: One Epic question, then one Loomlist Epic the Sync and Mobile Platform teams can plan from, with Web out and the conflict decision still open.

#### Test execution

> **Feature file:** [SEP-002](skill-story-modes/epic-natural-wording.md)

### SEP-003 | Epic quick energy

#### Description

Verify that `$quick $e` with the Goal and child stories in the prompt passes the Story gate and saves one lean house-format Epic in one turn, with its scope decisions intact.

#### Scenario contract

Prompt: `$quick $e self-serve returns, company context in context/fernhouse-context.md. Goal: signed-in customers on web, iOS and Android start a return themselves inside the 30-day window, so CS stops creating returns by hand in Admin, and by the end of Q1 2027 at least 60% of returns start without a CS contact. Child stories: start a return from order history with the items and a reason, return label by email, return status on the order page, refund after the warehouse check. Guest returns go under Added Later, and pallet items stay with CS.`

Desired user-visible outcome: One lean Fernhouse Epic in the first reply, ready for the Post-purchase team to cut child stories from.

#### Test execution

> **Feature file:** [SEP-003](skill-story-modes/epic-quick-energy.md)

---

## 11. SKILL INTERACTIVE ROUTING (`SIR-001..SIR-002`)

### SIR-001 | Vague intake, kind and energy

#### Description

Verify the energy-first comprehensive question, its intake-lane export and the Epic Turn 2 selects.

#### Scenario contract

Prompt: `Leadership keeps asking whether guests could earn loyalty points on their stays and I am not sure what we should put in the backlog for it, background is in context/roamstay-context.md`

Desired user-visible outcome: One energy-first question saved in the intake lane, then an Epic for guest loyalty points that keeps Roamstay's facts and the answer's numbers.

#### Test execution

> **Feature file:** [SIR-001](skill-interactive-routing/vague-intake-kind-and-energy.md)

### SIR-002 | Conflicting commands

#### Description

Verify one consolidated question for two explicit artifact commands, its intake-lane export and the Story Turn 2 selects.

#### Scenario contract

Prompt: `$bug $story Not sure if this is a bug or a story, customers lose their app wishlist when they change phones and cannot see it on web, CS has 412 contacts on it, see context/fernhouse-context.md and context/fernhouse-wishlist-feedback.md`

Desired user-visible outcome: One question that resolves the command conflict, saved in the intake lane, then a Story that moves the app wishlist to the account with every supplied value intact.

#### Test execution

> **Feature file:** [SIR-002](skill-interactive-routing/conflicting-commands.md)

---

## 12. PROJECT IDENTITY (`PID-001`)

### PID-001 | Project identity handover

#### Description

Verify Project identity through two rendered Deliverable Blocks, a task-lane clarification and then the task, each with an export-equivalent label and no file claim.

#### Scenario contract

Prompt: `$task Small front end task for a "Due today" filter chip on the To-dos view, the chips we have today are described in context/loomlist-context.md`

Desired user-visible outcome: A rendered task-lane question, then a rendered task for the "Due today" chip, each with its export-equivalent label and no file claim.

#### Test execution

> **Feature file:** [PID-001](project-identity/identity-handover.md)

---

## 13. PROJECT BACKLOG MODES (`PTK-001..PTK-006`, `PBG-001..PBG-003`)

### PTK-001 | Quick copy task

#### Description

Verify that Quick energy on a fully specified copy change skips intake and renders a faithful Fernhouse quick task block.

#### Scenario contract

Prompt: `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.`

Desired user-visible outcome: One quick task block for the banner copy change, labelled export-equivalent, with no question asked and no file claim.

#### Test execution

> **Feature file:** [PTK-001](project-backlog-modes/quick-copy-task.md)

### PTK-002 | Design notes FE task

#### Description

Verify task routing, the single context question and a front end task block that keeps every value from the design notes and every fact from the answer.

#### Scenario contract

Prompt: `$task FE task for the stay limits in the Guest app date picker. Ines's handover notes are in context/roamstay-date-picker-design-notes.md and our ticket conventions in context/roamstay-context.md.`

Desired user-visible outcome: One task-lane question block, then a front end task block for the date picker stay limits built from the notes and the answer, each labelled export-equivalent with no file claim.

#### Test execution

> **Feature file:** [PTK-002](project-backlog-modes/design-notes-fe-task.md)

### PTK-003 | Long BE integration task

#### Description

Verify the `$t` shortcut, the single context question and a long back end task block that keeps every carrier value and thread decision and adds nothing the sources do not state.

#### Scenario contract

Prompt: `$t BE task for the label webhook fix, Joris is taking it. The carrier API facts are in context/fernhouse-carrier-label-api-notes.md, the fix Noor summarised is at the end of context/fernhouse-carrier-label-thread.md and our ticket conventions are in context/fernhouse-context.md. Scope is the five points from the thread: answer inside the carrier's timeout and work from a queue, dedupe on event_id, guard against a second open shipment for a parcel, the 10-minute GET for stragglers and the alerting. Polling only stays out, the thread rejected it.`

Desired user-visible outcome: One task-lane question block, then a back end task block for label webhook idempotency and retries that a Fulfilment engineer can build and test from, each labelled export-equivalent with no file claim.

#### Test execution

> **Feature file:** [PTK-003](project-backlog-modes/long-be-integration-task.md)

### PTK-004 | Parent task with subtasks

#### Description

Verify task routing, the single context question and one parent task block that lists four subtasks by title and states the brief's shared rules once.

#### Scenario contract

Prompt: `$task Parent task for recurring to-dos from Ines's brief in context/loomlist-recurring-todos-pm-brief.md, with subtasks for iOS, Android, web and BE. Board conventions are in context/loomlist-context.md.`

Desired user-visible outcome: One task-lane question block, then one parent task block that lists four subtasks by title and states the recurring to-do rules once, each labelled export-equivalent with no file claim.

#### Test execution

> **Feature file:** [PTK-004](project-backlog-modes/parent-task-with-subtasks.md)

### PTK-005 | Supplied parent subtask

#### Description

Verify subtask routing, the single context question and an Android subtask block that names its supplied parent, keeps the parent's shared rules and holds only Android client work.

#### Scenario contract

Prompt: `$task --subtask Android subtask of the recurring to-dos parent in context/loomlist-recurring-todos-parent-task.md. Board conventions are in context/loomlist-context.md.`

Desired user-visible outcome: One task-lane question block, then an Android subtask block under its named parent that an Android engineer can build and test from, each labelled export-equivalent with no file claim.

#### Test execution

> **Feature file:** [PTK-005](project-backlog-modes/supplied-parent-subtask.md)

### PTK-006 | Data tracking task

#### Description

Verify natural-wording task routing, the single scope question and a DATA task block that keeps every status and value from the tracking plan and every scope fact from the answer.

#### Scenario contract

Prompt: `Can you write a task for the booking funnel events in Nadia's tracking plan, context/roamstay-booking-funnel-tracking-plan.md? Our conventions are in context/roamstay-context.md.`

Desired user-visible outcome: One task-lane question block, then a DATA task block for the booking funnel events that the Data team can work and check from, each labelled export-equivalent with no file claim.

#### Test execution

> **Feature file:** [PTK-006](project-backlog-modes/data-tracking-task.md)

### PBG-001 | Quick bug

#### Description

Verify that Quick energy on a complete one-line bug skips intake and renders a faithful Fernhouse bug block.

#### Scenario contract

Prompt: `$quick $bug iOS 4.8.0, the cart badge keeps the old count after an item is removed. Put 2 of one product and 1 of another in the cart so the tab bar badge reads "3", open the cart and tap "Remove" on the single item. The cart then holds 2 units but the badge stays on "3" until the app is restarted. Happens every time on both our iOS test phones, while Android 4.8.2 and web update the badge straight away. Severity Medium, product context is in context/fernhouse-context.md`

Desired user-visible outcome: One compact bug block for the iOS cart badge under an export-equivalent label, with no question asked and no file claimed.

#### Test execution

> **Feature file:** [PBG-001](project-backlog-modes/quick-bug.md)

### PBG-002 | Support ticket bug

#### Description

Verify the single evidence question, the wait state and a bug block that keeps the ticket's values, scope and charge-versus-display fact.

#### Scenario contract

Prompt: `$bug Guest Support escalated ticket 58213 to Booking. On Android the confirmation screen leaves city tax out of the total on stays of 2 nights or more, so the guest saw "Total €387.00" and was charged €405.00. The ticket with Maren's tests is in context/roamstay-support-ticket-58213.md and our product context is in context/roamstay-context.md`

Desired user-visible outcome: One evidence question rendered as a clarification block, then one bug block for the Booking squad under an export-equivalent label, with no file claimed.

#### Test execution

> **Feature file:** [PBG-002](project-backlog-modes/support-ticket-bug.md)

### PBG-003 | Two-platform log bug

#### Description

Verify the single evidence question, the wait state and one bug block that keeps two platform issues as two observed and expected pairs with no invented cause.

#### Scenario contract

Prompt: `$b Reminders arrived an hour late after the March clock change, one-off reminders on Android and daily ones on iOS. Please write it up as one bug for the To-dos and Reminders team from Ruben's log lines in context/loomlist-reminders-dst-log-excerpt.md and Marta's support reports in context/loomlist-reminders-dst-user-reports.md, with our product context in context/loomlist-context.md`

Desired user-visible outcome: One evidence question rendered as a clarification block, then one bug block for the To-dos and Reminders team under an export-equivalent label that keeps the Android and iOS issues apart and reads the log as evidence, with no file claimed.

#### Test execution

> **Feature file:** [PBG-003](project-backlog-modes/two-platform-log-bug.md)

---

## 14. PROJECT DOCUMENT MODES (`PDK-001..PDK-004`)

### PDK-001 | Behavior reference

#### Description

Verify no-command Doc routing, the five-field Doc intake question and a ClickUp behavior reference that keeps Fernhouse's current and retired promotion rules apart.

#### Scenario contract

Prompt: `Can you document how discount codes and automatic promotions stack? Start with context/fernhouse-promotions-rules.md, and context/fernhouse-context.md has the company background.`

Desired user-visible outcome: One question that settles the doc before any drafting, then a behavior reference block CS agents and the Checkout engineers can use to predict the discount on any cart.

#### Test execution

> **Feature file:** [PDK-001](project-document-modes/behavior-reference.md)

### PDK-002 | Incident runbook

#### Description

Verify the Doc intake question under `$doc` and a ClickUp runbook that follows the incident notes' procedure and keeps the proposed dual-secret window proposed.

#### Scenario contract

Prompt: `$doc We need a doc on handling payment webhook failures, like the INC-0412 outage. Start with context/roamstay-payment-webhook-incident-notes.md, and context/roamstay-context.md has the company background.`

Desired user-visible outcome: One question that settles the doc before any drafting, then a runbook block the Payments on-call engineer can follow from the alert to the cleanup.

#### Test execution

> **Feature file:** [PDK-002](project-document-modes/incident-runbook.md)

### PDK-003 | Proposal with a decision owner

#### Description

Verify the Doc intake question under `$d` and a ClickUp proposal that lays out the three sync conflict options, attributes support and leaves the decision with its owner.

#### Scenario contract

Prompt: `$d Can you write up where we are on sync conflicts and the lost edits? Start with context/loomlist-sync-conflict-thread.md, and context/loomlist-context.md has the company background.`

Desired user-visible outcome: One question that settles the doc before any drafting, then a proposal block the Sync and Mobile engineers and the Support lead can read before the decision without mistaking any option for the chosen one.

#### Test execution

> **Feature file:** [PDK-003](project-document-modes/proposal-decision-owner.md)

### PDK-004 | Catalog conflict gate

#### Description

Verify the conflict stop on the digest send time, the consolidated clarification block and a ClickUp catalog that follows the user's authority decision.

#### Scenario contract

Prompt: `$doc Can you pull the six activity emails into one reference page? So far I have context/loomlist-notification-spec.md and context/loomlist-email-template-inventory.md, plus context/loomlist-context.md for background.`

Desired user-visible outcome: A clarification block that names the conflict, then one catalog block of the six activity emails after the user says which source governs.

#### Test execution

> **Feature file:** [PDK-004](project-document-modes/catalog-conflict-gate.md)

---

## 15. PROJECT STORY MODES (`PST-001..PST-004`, `PEP-001..PEP-003`)

### PST-001 | Story hard values

#### Description

Verify that a no-command Story request waits for the promised input, then renders one house-format Story that keeps every hard value from the PM notes verbatim.

#### Scenario contract

Prompt: `Can you write up the free cancellation filter as a story for the Search squad? Tomas's notes are in context/roamstay-free-cancellation-pm-notes.md and our company background is in context/roamstay-context.md. Guest Support sent me two asks for it as well, I'll pass them on.`

Desired user-visible outcome: One Story question block that collects the Guest Support asks, then one house-format Story block that names its kind and keeps every value as the notes wrote it.

#### Test execution

> **Feature file:** [PST-001](project-story-modes/story-hard-values.md)

### PST-002 | Story forced delivery

#### Description

Verify that an open question in the source stays open as an `**Open:**` line and forces the `## Delivery` close in the rendered Story.

#### Scenario contract

Prompt: `$story View-only share links for the Sharing team, from Kofi's design notes in context/loomlist-view-only-links-design-notes.md. Workspace background is in context/loomlist-context.md.`

Desired user-visible outcome: One Story question block, then one house-format Story block that names its kind, marks the sub-page question as open and closes on the Delivery section that open question forces.

#### Test execution

> **Feature file:** [PST-002](project-story-modes/story-forced-delivery.md)

### PST-003 | Story refinement

#### Description

Verify an authorized restructure of a rough Story draft into the house shape under the source file name label, with every supplied value intact.

#### Scenario contract

Prompt: `$s Priya's rough save card draft is in context/fernhouse-save-card-draft.md, can you bring it into our house Story format before the Checkout team picks it up? Restructure whatever it needs. Company background is in context/fernhouse-context.md.`

Desired user-visible outcome: One Story question block, then one refined Story block labelled with the draft's own file name, in the house shape, with every value the draft and the turns supplied.

#### Test execution

> **Feature file:** [PST-003](project-story-modes/story-refinement.md)

### PST-004 | Story with nested tasks

#### Description

Verify that a Story asked for with its task breakdown renders as one Deliverable Block per file, labelled inside one bundle folder, whose Story and four tasks link each other in the split the PM names, with every supplied value intact.

#### Scenario contract

Prompt: `$story Order tracking on the order page, from Hamid's brief in context/fernhouse-order-tracking-pm-brief.md and Yusuf's carrier notes in context/fernhouse-carrier-tracking-api-facts.md. Please break it into tasks. Company background is in context/fernhouse-context.md.`

Desired user-visible outcome: One Story question block in the Story lane, then five Deliverable Blocks, Story first, each labelled inside one bundle folder and linked both ways, with no file claimed.

#### Test execution

> **Feature file:** [PST-004](project-story-modes/story-with-nested-tasks.md)

### PEP-001 | Epic from strategy brief

#### Description

Verify that `$epic` on a strategy brief asks one Epic question, then renders a house-format Epic whose child stories, numbers and boundaries come from the brief.

#### Scenario contract

Prompt: `$epic Partner Hub self-onboarding from Freya's strategy brief in context/roamstay-partner-self-onboarding-brief.md, company context is in context/roamstay-context.md. We haven't agreed the first release cut yet.`

Desired user-visible outcome: One Epic question block, then one Roamstay Epic block the Partner, Ops Tools and Payments squads can plan from, with the brief's numbers intact.

#### Test execution

> **Feature file:** [PEP-001](project-story-modes/epic-from-strategy-brief.md)

### PEP-002 | Epic natural wording

#### Description

Verify that a no-command request to write an epic resolves the Epic shape and lane, asks one Epic question, then renders an Epic that keeps the brief's scope, numbers and open dependency.

#### Scenario contract

Prompt: `Can you write an epic for offline mode from Oskar's brief in context/loomlist-offline-mode-brief.md? Our product context is in context/loomlist-context.md. I'm not sure yet whether the child stories should follow his four areas or be split per platform.`

Desired user-visible outcome: One Epic question block, then one Loomlist Epic block the Sync and Mobile Platform teams can plan from, with Web out and the conflict decision still open.

#### Test execution

> **Feature file:** [PEP-002](project-story-modes/epic-natural-wording.md)

### PEP-003 | Epic quick energy

#### Description

Verify that `$quick $e` with the Goal and child stories in the prompt passes the Story gate and renders one lean house-format Epic in one turn, with its scope decisions intact.

#### Scenario contract

Prompt: `$quick $e self-serve returns, company context in context/fernhouse-context.md. Goal: signed-in customers on web, iOS and Android start a return themselves inside the 30-day window, so CS stops creating returns by hand in Admin, and by the end of Q1 2027 at least 60% of returns start without a CS contact. Child stories: start a return from order history with the items and a reason, return label by email, return status on the order page, refund after the warehouse check. Guest returns go under Added Later, and pallet items stay with CS.`

Desired user-visible outcome: One lean Fernhouse Epic block in the first reply, ready for the Post-purchase team to cut child stories from.

#### Test execution

> **Feature file:** [PEP-003](project-story-modes/epic-quick-energy.md)

---

## 16. PROJECT INTERACTIVE ROUTING (`PIR-001..PIR-002`)

### PIR-001 | Vague intake, kind and energy

#### Description

Verify the energy-first comprehensive question, its intake-lane clarification block and the Epic Turn 2 selects.

#### Scenario contract

Prompt: `Leadership keeps asking whether guests could earn loyalty points on their stays and I am not sure what we should put in the backlog for it, background is in context/roamstay-context.md`

Desired user-visible outcome: One energy-first question rendered as an intake clarification, then an Epic block for guest loyalty points that keeps Roamstay's facts and the answer's numbers, with no file claim.

#### Test execution

> **Feature file:** [PIR-001](project-interactive-routing/vague-intake-kind-and-energy.md)

### PIR-002 | Conflicting commands

#### Description

Verify one consolidated question for two explicit artifact commands, its intake-lane clarification block and the Story Turn 2 selects.

#### Scenario contract

Prompt: `$bug $story Not sure if this is a bug or a story, customers lose their app wishlist when they change phones and cannot see it on web, CS has 412 contacts on it, see context/fernhouse-context.md and context/fernhouse-wishlist-feedback.md`

Desired user-visible outcome: One question that resolves the command conflict, rendered as an intake clarification, then a Story block that moves the app wishlist to the account with every supplied value intact and no file claim.

#### Test execution

> **Feature file:** [PIR-002](project-interactive-routing/conflicting-commands.md)

---

## 17. AUTOMATED VALIDATION CROSS-REFERENCE

| Check | Coverage | Playbook overlap |
|---|---|---|
| [`../../benchmark/router/run_fixtures.sh`](../../benchmark/router/run_fixtures.sh) | Router differential against `route_contract.py` | Turn 1 routing of every ID, most directly `STK-003`, `STK-005`, `STK-006`, `SBG-003`, `SDK-003`, `SST-003`, `SEP-001..SEP-003`, `SIR-001`, `SIR-002` and their Project mirrors |
| [`../../benchmark/format/run_fixtures.sh`](../../benchmark/format/run_fixtures.sh) | Output-format gate on this system's instruction surface | All delivered artifact shapes |
| [`../../benchmark/parity/`](../../benchmark/parity/) scripts | Kernel-to-skill parity and residency checks | `PID-001`, `SID-001` |
| Playbook package validator | Paths, IDs, sections, prompts, tables, links | This package |
| Real manual execution | Runtime behavior and side effects | All 46 IDs, `SID-001` to `PIR-002` |

---

## 18. SOURCE CROSS-REFERENCE INDEX

| Feature ID | Feature name | Category | Feature file | Primary source |
|---|---|---|---|---|
| SID-001 | Skill identity handover | Skill identity | [SID-001](skill-identity/identity-handover.md) | [`AGENTS.md`](../../AGENTS.md) |
| STK-001 | Quick copy task | Skill backlog modes | [STK-001](skill-backlog-modes/quick-copy-task.md) | [`task-mode.md`](../references/task-mode.md) |
| STK-002 | Design notes FE task | Skill backlog modes | [STK-002](skill-backlog-modes/design-notes-fe-task.md) | [`task-mode.md`](../references/task-mode.md) |
| STK-003 | Long BE integration task | Skill backlog modes | [STK-003](skill-backlog-modes/long-be-integration-task.md) | [`task-mode.md`](../references/task-mode.md) |
| STK-004 | Parent task with subtasks | Skill backlog modes | [STK-004](skill-backlog-modes/parent-task-with-subtasks.md) | [`task-mode.md`](../references/task-mode.md) |
| STK-005 | Supplied parent subtask | Skill backlog modes | [STK-005](skill-backlog-modes/supplied-parent-subtask.md) | [`task-mode.md`](../references/task-mode.md) |
| STK-006 | Data tracking task | Skill backlog modes | [STK-006](skill-backlog-modes/data-tracking-task.md) | [`task-mode.md`](../references/task-mode.md) |
| SBG-001 | Quick bug | Skill backlog modes | [SBG-001](skill-backlog-modes/quick-bug.md) | [`bug-mode.md`](../references/bug-mode.md) |
| SBG-002 | Support ticket bug | Skill backlog modes | [SBG-002](skill-backlog-modes/support-ticket-bug.md) | [`bug-mode.md`](../references/bug-mode.md) |
| SBG-003 | Two-platform log bug | Skill backlog modes | [SBG-003](skill-backlog-modes/two-platform-log-bug.md) | [`bug-mode.md`](../references/bug-mode.md) |
| SDK-001 | Behavior reference | Skill document modes | [SDK-001](skill-document-modes/behavior-reference.md) | [`doc-mode.md`](../references/doc-mode.md) |
| SDK-002 | Incident runbook | Skill document modes | [SDK-002](skill-document-modes/incident-runbook.md) | [`doc-mode.md`](../references/doc-mode.md) |
| SDK-003 | Proposal with a decision owner | Skill document modes | [SDK-003](skill-document-modes/proposal-decision-owner.md) | [`doc-mode.md`](../references/doc-mode.md) |
| SDK-004 | Catalog conflict gate | Skill document modes | [SDK-004](skill-document-modes/catalog-conflict-gate.md) | [`doc-mode.md`](../references/doc-mode.md) |
| SST-001 | Story hard values | Skill story modes | [SST-001](skill-story-modes/story-hard-values.md) | [`story-mode.md`](../references/story-mode.md) |
| SST-002 | Story forced delivery | Skill story modes | [SST-002](skill-story-modes/story-forced-delivery.md) | [`story-mode.md`](../references/story-mode.md) |
| SST-003 | Story refinement | Skill story modes | [SST-003](skill-story-modes/story-refinement.md) | [`story-mode.md`](../references/story-mode.md) |
| SST-004 | Story with nested tasks | Skill story modes | [SST-004](skill-story-modes/story-with-nested-tasks.md) | [`story-mode.md`](../references/story-mode.md) |
| SEP-001 | Epic from strategy brief | Skill story modes | [SEP-001](skill-story-modes/epic-from-strategy-brief.md) | [`story-mode.md`](../references/story-mode.md) |
| SEP-002 | Epic natural wording | Skill story modes | [SEP-002](skill-story-modes/epic-natural-wording.md) | [`story-mode.md`](../references/story-mode.md) |
| SEP-003 | Epic quick energy | Skill story modes | [SEP-003](skill-story-modes/epic-quick-energy.md) | [`story-mode.md`](../references/story-mode.md) |
| SIR-001 | Vague intake, kind and energy | Skill interactive routing | [SIR-001](skill-interactive-routing/vague-intake-kind-and-energy.md) | [`interactive-mode.md`](../references/interactive-mode.md) |
| SIR-002 | Conflicting commands | Skill interactive routing | [SIR-002](skill-interactive-routing/conflicting-commands.md) | [`interactive-mode.md`](../references/interactive-mode.md) |
| PID-001 | Project identity handover | Project identity | [PID-001](project-identity/identity-handover.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PTK-001 | Quick copy task | Project backlog modes | [PTK-001](project-backlog-modes/quick-copy-task.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PTK-002 | Design notes FE task | Project backlog modes | [PTK-002](project-backlog-modes/design-notes-fe-task.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PTK-003 | Long BE integration task | Project backlog modes | [PTK-003](project-backlog-modes/long-be-integration-task.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PTK-004 | Parent task with subtasks | Project backlog modes | [PTK-004](project-backlog-modes/parent-task-with-subtasks.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PTK-005 | Supplied parent subtask | Project backlog modes | [PTK-005](project-backlog-modes/supplied-parent-subtask.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PTK-006 | Data tracking task | Project backlog modes | [PTK-006](project-backlog-modes/data-tracking-task.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PBG-001 | Quick bug | Project backlog modes | [PBG-001](project-backlog-modes/quick-bug.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PBG-002 | Support ticket bug | Project backlog modes | [PBG-002](project-backlog-modes/support-ticket-bug.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PBG-003 | Two-platform log bug | Project backlog modes | [PBG-003](project-backlog-modes/two-platform-log-bug.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PDK-001 | Behavior reference | Project document modes | [PDK-001](project-document-modes/behavior-reference.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PDK-002 | Incident runbook | Project document modes | [PDK-002](project-document-modes/incident-runbook.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PDK-003 | Proposal with a decision owner | Project document modes | [PDK-003](project-document-modes/proposal-decision-owner.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PDK-004 | Catalog conflict gate | Project document modes | [PDK-004](project-document-modes/catalog-conflict-gate.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PST-001 | Story hard values | Project story modes | [PST-001](project-story-modes/story-hard-values.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PST-002 | Story forced delivery | Project story modes | [PST-002](project-story-modes/story-forced-delivery.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PST-003 | Story refinement | Project story modes | [PST-003](project-story-modes/story-refinement.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PST-004 | Story with nested tasks | Project story modes | [PST-004](project-story-modes/story-with-nested-tasks.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PEP-001 | Epic from strategy brief | Project story modes | [PEP-001](project-story-modes/epic-from-strategy-brief.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PEP-002 | Epic natural wording | Project story modes | [PEP-002](project-story-modes/epic-natural-wording.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PEP-003 | Epic quick energy | Project story modes | [PEP-003](project-story-modes/epic-quick-energy.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PIR-001 | Vague intake, kind and energy | Project interactive routing | [PIR-001](project-interactive-routing/vague-intake-kind-and-energy.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PIR-002 | Conflicting commands | Project interactive routing | [PIR-002](project-interactive-routing/conflicting-commands.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
