---
title: "STK-006 -- Data tracking task"
description: "Validates that a plain-language request with no command routes to Task Mode, asks one scope question, then saves a Roamstay DATA task for the booking funnel events that keeps every event status from the tracking plan, the deprecated event's removal date included, and leaves the proposed event unbuilt."
version: 1.0.0.0
---

# STK-006 -- Data tracking task

This scenario validates a natural-wording task request with no command token, from a tracking plan to a saved DATA task, through one clarification turn.

---

## 1. OVERVIEW

A Roamstay PM types a plain request for a task covering the booking funnel events in Nadia's tracking plan. There is no command, so the router takes the route from the "write a task" framing. The plan splits the build three ways, the client events to the apps and web, `booking_confirmed` to the Booking squad in `booking-service` and the funnel dashboard to the Data team, and the request names none of them, so the scope is missing and Task Mode asks once. Turn 2 settles it: the Data team's own task under `TRK`, where Nadia checks every event in `events-collector` as the squads ship them, moves the funnel dashboard to `booking_confirmed` and has the collector drop `checkout_complete` on its removal date, while the client events and `booking_confirmed` itself get separate FE and BE tasks later. Refinement closed with no change to the event table, so every status in it stands.

The plan carries two status traps a faithful task keeps as written. `checkout_complete` is `deprecated`: it keeps firing beside `booking_confirmed` until `2026-11-01`, then `events-collector` drops it whatever app version sends it. `date_changed` is `proposed`, raised in comments with no properties agreed, and is not an event anyone builds yet. The plan also fixes the values the Data team checks: `search_submitted` and `property_viewed` changed, `room_selected`, `checkout_started`, `payment_submitted` and `booking_confirmed` new, `booking_confirmed` sent by `booking-service` with `source` set to `server`, dates as `check_in` and `check_out` in `YYYY-MM-DD`, `nights`, `guests`, `property_id`, and money as `total_amount_minor` in minor units with city tax included beside `currency`.

A task that reads like the team's own carries a title in the `{Discipline} - {Surface} - {Feature code} - {Title}` pattern with `DATA` and `TRK`, an About with the three problems the plan opens on, the plan as a plain-text reference, and numbered requirement groups for event validation, the dashboard move and the `checkout_complete` removal, each with a `**Checklist**`, with the FE and BE build named as dependencies rather than scoped in. No routed template asks for a title code, so a title without one is recorded, never graded (root section 5, Ticket realism).

### Why this matters

Tracking tasks are where a proposal most easily turns into a build item and a deprecated event quietly keeps a dashboard alive. A DATA task that validates `date_changed`, counts bookings from `payment_submitted` or forgets the removal date gives the funnel numbers nobody agreed on.

---

## 2. SCENARIO CONTRACT

- Objective: Verify natural-wording task routing, the single scope question and a DATA task that keeps every status and value from the tracking plan and every scope fact from the answer
- Real user request: `Nadia's funnel events need a ticket before the squads start building.`
- Prompt: `Can you write a task for the booking funnel events in Nadia's tracking plan, context/roamstay-booking-funnel-tracking-plan.md? Our conventions are in context/roamstay-context.md.`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-booking-funnel-tracking-plan.md](../../../benchmark/fixtures/companies/roamstay/roamstay-booking-funnel-tracking-plan.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit in `context/` in the sandbox
- Expected execution process: Start fresh, submit Turn 1, inspect the clarification export, answer in Turn 2 in the same session and inspect the task export
- Expected signals: With no command, the "write a task" framing routes to Task Mode (`SKILL.md` line 82, `references/router-contract.md` line 356) and a clear natural-language task goes to the task context gate (`references/interactive-mode.md` line 123). The plan assigns the build to three teams and the request names none, so the scope is missing and Task Mode asks one question and waits (`AGENTS.md` line 283, `references/task-mode.md` line 55). The question is saved as `export/[###] - task-[description]-clarification.md`, holding the question and nothing else, read back, and the reply carries its path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (`AGENTS.md` line 82, root section 5, Clarification turns). A question that asks for a fact the plan already states is recorded only (root section 5, Ticket realism). Turn 2 saves `export/[###] - task-[description].md` on the next number, reads it back and replies path first with the `Verified:` line and the `HVR self-scan:` line (`AGENTS.md` lines 46 and 47). The task follows the Canonical Task template (`assets/task-templates.md` line 38): H1, `### About` and `### Requirements` (`references/task-mode.md` lines 72 to 78) and numbered groups each with a `**Checklist**` of `- [ ]` items (lines 102 to 112). It carries the plan's event names, statuses and properties verbatim (`roamstay-booking-funnel-tracking-plan.md` lines 17 to 57), keeps `booking_confirmed` as the server event from `booking-service` that every booking count uses (line 55), keeps `checkout_complete` firing until its removal date and dropped by `events-collector` from then on (line 56), leaves `date_changed` out as `proposed` (lines 26 and 57) and keeps the Android `room_selected` timing Nadia agreed (lines 67 to 71). Every Turn 2 fact survives: the Data team's own task under `TRK`, Nadia's checks in `events-collector`, the dashboard move, the collector drop on the removal date, the FE and BE build left to separate tasks, and the event table unchanged at refinement
- Desired user-visible outcome: One saved task-lane question, then a saved DATA task for the booking funnel events that the Data team can work and check from
- Size band (advisory): 60 to 140 lines of artifact body
- Pass/fail: PASS if Turn 1 routes to Task Mode, asks one question, saves it under a `task` lane `-clarification` name reported with its path, the `Verified:` line and the `HVR self-scan:` line and drafts no task, and Turn 2 saves one `task` export on the next number, read back and reported the same way, carrying its H1, `### About` and `### Requirements` with checklisted requirement groups, the six funnel events as the plan names them, `booking_confirmed` from `booking-service` with `source` set to `server`, `total_amount_minor` in minor units, `checkout_complete` marked `deprecated` with its removal on `2026-11-01`, `date_changed` kept `proposed` and unbuilt, and every Turn 2 fact. FAIL if Turn 1 drafts a task or routes to another mode, the task builds or validates `date_changed` as an agreed event or invents properties for it, keeps `checkout_complete` past its removal date or drops it early, counts bookings from `payment_submitted` or `checkout_complete`, sends `booking_confirmed` from a client, sends money as decimals or without city tax, puts the FE or BE build inside the DATA task's own requirements, drops a Turn 2 fact or leaves a template slot in the body
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Can you write a task for the booking funnel events in Nadia's tracking plan, context/roamstay-booking-funnel-tracking-plan.md? Our conventions are in context/roamstay-context.md.` | Route to Task Mode on the task framing, read both attachments, ask one question that covers the missing scope, save it as a task-lane clarification, read it back and reply with its path, the `Verified:` line and the `HVR self-scan:` line. Draft no task | Task Mode and the booking funnel events stay selected, one new `-clarification` file, `context/` unchanged | Turn 1 reply, clarification file, read-back result and side-effect ledger |
| 2 | `It is the Data team's own task under TRK. Nadia checks every event in events-collector as the squads ship them, moves the funnel dashboard over to booking_confirmed and has the collector drop checkout_complete on its removal date. The client events and booking_confirmed itself get separate FE and BE tasks later. Refinement closed yesterday with no change to the event table.` | Build the DATA task from the plan and the answer, save it on the next number, read it back and reply path first with the `Verified:` line and the `HVR self-scan:` line | The plan's events, statuses and properties and every Turn 2 fact survive, the clarification file stays untouched | Turn 2 reply, task export, read-back result and side-effect ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Can you write a task for the booking funnel events in Nadia's tracking plan, context/roamstay-booking-funnel-tracking-plan.md? Our conventions are in context/roamstay-context.md.`

### Commands

1. `sandbox: stage context/roamstay-context.md and context/roamstay-booking-funnel-tracking-plan.md -> record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the new task export -> operator: grade the sections, requirement groups, event names, statuses, properties, the removal date, the proposed event and the Turn 2 facts against the plan and the answer`

### Expected

Step 1 fixes the baseline with both attachments staged. Step 2 returns one scope question and one clarification file, with Task Mode selected from plain wording. Step 3 proves the wait state and the question-only file. Step 4 finds an H1, `### About`, `### Requirements` and numbered groups with `**Checklist**` items for checking each event in `events-collector`, moving the funnel dashboard to `booking_confirmed` and dropping `checkout_complete` on `2026-11-01`, the six events and their properties as the plan gives them, `date_changed` left out as proposed and the FE and BE build named as dependencies.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back lines, the self-scan lines and task excerpts showing each requirement group, the event statuses, the server event, the money property, the removal date and every Turn 2 fact.

### Pass / fail

- **Pass**: Task Mode from plain wording, one scope question saved as a task-lane clarification, no early draft, then one readable DATA task with the required sections, every event, status and property from the plan, the deprecated event's removal date, the proposed event unbuilt and every Turn 2 fact
- **Fail**: The runtime drafts before Turn 2 or routes elsewhere, promotes `date_changed`, mishandles the `checkout_complete` removal, counts bookings from the wrong event, sends the server event from a client, changes the money format, scopes the FE or BE build into the DATA task, drops a Turn 2 fact or leaves a template slot

### Failure triage

1. Check the task framing route at `SKILL.md` line 82 and `references/interactive-mode.md` line 123, then the missing-scope question rule at `AGENTS.md` line 283 and the clarification export at line 82
2. Compare the task with the Canonical Task template at `assets/task-templates.md` line 38 and the requirement grammar at `references/task-mode.md` lines 102 to 112
3. Diff every event, status and property against `roamstay-booking-funnel-tracking-plan.md` lines 17 to 77 and every scope fact against Turn 2

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| STK-006 | Data tracking task | Verify a plain request and one answer become a faithful DATA task | `Can you write a task for the booking funnel events in Nadia's tracking plan, context/roamstay-booking-funnel-tracking-plan.md? Our conventions are in context/roamstay-context.md.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the task export | Step 1: baseline known. Step 2: Task Mode from plain wording, one question and one clarification. Step 3: state retained. Step 4: required sections, events and statuses intact, removal date kept, proposed event unbuilt, Turn 2 facts intact | Both replies, ledger, clarification and task export paths, read-back lines and artifact excerpts | PASS if routing, the scope question and a faithful DATA task all match. FAIL otherwise | 1. Check the framing route and scope rule. 2. Check the task template. 3. Diff events, statuses and Turn 2 facts |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | The missing-scope question rule, the clarification export and the read-back reply |
| [`SKILL.md`](../../SKILL.md) | Framing detection with no command, export names and the HVR self-scan line |
| [`router-contract.md`](../../references/router-contract.md) | The task framing pattern the plain request matches |
| [`task-mode.md`](../../references/task-mode.md) | Task workflow, the ask-first rule, required sections and requirement grammar |
| [`task-templates.md`](../../assets/task-templates.md) | Canonical Task scaffold |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Clear natural-language task row and the clarification export |
| [`roamstay-context.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Attachment: services, squads, the `DATA` discipline, the `TRK` code and the analytics conventions |
| [`roamstay-booking-funnel-tracking-plan.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-booking-funnel-tracking-plan.md) | Attachment: the funnel events, statuses, properties, per-event notes, comments and the build split |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: STK-006
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/data-tracking-task.md`
