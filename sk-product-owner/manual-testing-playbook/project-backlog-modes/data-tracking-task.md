---
title: "PTK-006 -- Data tracking task"
description: "Validates that a plain-language request with no command routes to Task Mode in a Claude Project, renders one scope question block, then a Roamstay DATA task block for the booking funnel events that keeps every event status from the tracking plan, the deprecated event's removal date included, and leaves the proposed event unbuilt."
version: 1.0.0.3
---

# PTK-006 -- Data tracking task

This scenario validates a natural-wording task request with no command token, from a tracking plan to a rendered DATA task block, through one clarification turn.

---

## 1. OVERVIEW

A Roamstay PM types a plain request for a task covering the booking funnel events in Nadia's tracking plan. There is no command, so the router takes the route from the "write a task" framing. The plan splits the build three ways, the client events to the apps and web, `booking_confirmed` to the Booking squad in `booking-service` and the funnel dashboard to the Data team, and the request names none of them, so the scope is missing and Task Mode asks once. Turn 2 settles it: the Data team's own task under `TRK`, where Nadia checks every event in `events-collector` as the squads ship them, moves the funnel dashboard to `booking_confirmed` and has the collector drop `checkout_complete` on its removal date, while the client events and `booking_confirmed` itself get separate FE and BE tasks later. Refinement closed with no change to the event table, so every status in it stands.

The plan carries two status traps a faithful task keeps as written. `checkout_complete` is `deprecated`: it keeps firing beside `booking_confirmed` until `2026-11-01`, then `events-collector` drops it whatever app version sends it. `date_changed` is `proposed`, raised in comments with no properties agreed, and is not an event anyone builds yet. The plan also fixes the values the Data team checks: `search_submitted` and `property_viewed` changed, `room_selected`, `checkout_started`, `payment_submitted` and `booking_confirmed` new, `booking_confirmed` sent by `booking-service` with `source` set to `server`, dates as `check_in` and `check_out` in `YYYY-MM-DD`, `nights`, `guests`, `property_id`, and money as `total_amount_minor` in minor units with city tax included beside `currency`.

A task that reads like the team's own carries a title in the `{Discipline} - {Surface} - {Feature code} - {Title}` pattern with `DATA` and `TRK`, an About with the three problems the plan opens on, the plan as a plain-text reference, and numbered requirement groups for event validation, the dashboard move and the `checkout_complete` removal, each with a `**Checklist**`, with the FE and BE build named as dependencies rather than scoped in. No routed template asks for a title code, so a title without one is recorded, never graded (root section 5, Ticket realism).

### Why this matters

Tracking tasks are where a proposal most easily turns into a build item and a deprecated event quietly keeps a dashboard alive. A DATA task block that validates `date_changed`, counts bookings from `payment_submitted` or forgets the removal date gives the funnel numbers nobody agreed on.

---

## 2. SCENARIO CONTRACT

- Objective: Verify natural-wording task routing, the single scope question and a DATA task block that keeps every status and value from the tracking plan and every scope fact from the answer
- Real user request: `Nadia's funnel events need a ticket before the squads start building.`
- Prompt: `Can you write a task for the booking funnel events in Nadia's tracking plan, context/roamstay-booking-funnel-tracking-plan.md? Our conventions are in context/roamstay-context.md.`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-booking-funnel-tracking-plan.md](../../../benchmark/fixtures/companies/roamstay/roamstay-booking-funnel-tracking-plan.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments sit in `context/` in the sandbox
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the clarification block, answer in Turn 2 in the same conversation and inspect the rendered task block
- Expected signals: With no command, the "write a task" framing routes to Task Mode (`Product Owner - System - Router Contract` line 356) and a clear natural-language task goes to the task context gate (`Product Owner - System - Interactive Mode` line 100). The plan assigns the build to three teams and the request names none, so the scope is missing and Task Mode asks one question and waits (`Custom Instructions.md` line 108, `Product Owner - Templates - Task Mode` line 35). The question renders as its own block, then `Export-equivalent path: export/[NNN] - task-[description]-clarification.md` (`Custom Instructions.md` line 228) and the `HVR self-scan:` line, with no file claim and no task (`Product Owner - System - Interactive Mode` lines 62 and 70, root section 5, Clarification turns). A question that asks for a fact the plan already states is recorded only (root section 5, Ticket realism). Turn 2 renders the task as the Deliverable Block before any commentary, fenced where there is no Canvas panel (`Custom Instructions.md` line 85), then `Export-equivalent path: export/[NNN] - task-[description].md` (line 223) and the `HVR self-scan:` line (line 89), with no claim that a file was written (line 101). The block follows the Canonical Task template (`Product Owner - Assets - Task Templates` line 19): H1, `### About` and `### Requirements` (`Product Owner - Templates - Task Mode` lines 52 to 58) and numbered groups each with a `**Checklist**` of `- [ ]` items (lines 82 to 92). It carries the plan's event names, statuses and properties verbatim (`roamstay-booking-funnel-tracking-plan.md` lines 17 to 57), keeps `booking_confirmed` as the server event from `booking-service` that every booking count uses (line 55), keeps `checkout_complete` firing until its removal date and dropped by `events-collector` from then on (line 56), leaves `date_changed` out as `proposed` (lines 26 and 57) and keeps the Android `room_selected` timing Nadia agreed (lines 67 to 71). Every Turn 2 fact survives: the Data team's own task under `TRK`, Nadia's checks in `events-collector`, the dashboard move, the collector drop on the removal date, the FE and BE build left to separate tasks, and the event table unchanged at refinement
- Desired user-visible outcome: One task-lane question block, then a DATA task block for the booking funnel events that the Data team can work and check from, each labelled export-equivalent with no file claim
- Size band (advisory): 60 to 140 lines of artifact body
- Pass/fail: PASS if Turn 1 routes to Task Mode, asks one question rendered as its own block under an export-equivalent `task` lane `-clarification` label with the `HVR self-scan:` line and renders no task, and Turn 2 renders one task block under an export-equivalent `task` label with the `HVR self-scan:` line and no file claim, carrying its H1, `### About` and `### Requirements` with checklisted requirement groups, the six funnel events as the plan names them, `booking_confirmed` from `booking-service` with `source` set to `server`, `total_amount_minor` in minor units, `checkout_complete` marked `deprecated` with its removal on `2026-11-01`, `date_changed` kept `proposed` and unbuilt, and every Turn 2 fact. FAIL if Turn 1 renders a task or routes to another mode, a reply prints `Path:`, `Saved:` or `Verified:` or claims a file, the task builds or validates `date_changed` as an agreed event or invents properties for it, keeps `checkout_complete` past its removal date or drops it early, counts bookings from `payment_submitted` or `checkout_complete`, sends `booking_confirmed` from a client, sends money as decimals or without city tax, puts the FE or BE build inside the DATA task's own requirements, drops a Turn 2 fact or leaves a template slot in the block
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Can you write a task for the booking funnel events in Nadia's tracking plan, context/roamstay-booking-funnel-tracking-plan.md? Our conventions are in context/roamstay-context.md.` | Route to Task Mode on the task framing, read both attachments, ask one question that covers the missing scope, render it as a clarification block with an export-equivalent label and the `HVR self-scan:` line and wait. Claim no file and render no task | Task Mode and the booking funnel events stay selected, no task block exists | Turn 1 reply, rendered clarification block, its label and the no-file statement |
| 2 | `It is the Data team's own task under TRK. Nadia checks every event in events-collector as the squads ship them, moves the funnel dashboard over to booking_confirmed and has the collector drop checkout_complete on its removal date. The client events and booking_confirmed itself get separate FE and BE tasks later. Refinement closed yesterday with no change to the event table.` | Render the DATA task block from the plan and the answer, then its export-equivalent label and the `HVR self-scan:` line, with no file claim | The plan's events, statuses and properties and every Turn 2 fact survive | Turn 2 reply, rendered task block, its label and the no-file statement |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Can you write a task for the booking funnel events in Nadia's tracking plan, context/roamstay-booking-funnel-tracking-plan.md? Our conventions are in context/roamstay-context.md.`

### Commands

1. `sandbox: stage context/roamstay-context.md and context/roamstay-booking-funnel-tracking-plan.md -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `operator: confirm one scope question block and no task block -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered task block -> operator: grade the sections, requirement groups, event names, statuses, properties, the removal date, the proposed event, the Turn 2 facts, the label and the no-file boundary`

### Expected

Step 1 fixes the panel baseline with both attachments staged. Step 2 returns one scope question as its own block with a `-clarification` label, with Task Mode selected from plain wording. Step 3 proves the wait state and state retention. Step 4 finds an H1, `### About`, `### Requirements` and numbered groups with `**Checklist**` items for checking each event in `events-collector`, moving the funnel dashboard to `booking_confirmed` and dropping `checkout_complete` on `2026-11-01`, the six events and their properties as the plan gives them, `date_changed` left out as proposed and the FE and BE build named as dependencies, under an export-equivalent label.

### Evidence

Capture both replies, both rendered blocks and which form each took, the two export-equivalent labels, the self-scan lines, the no-file statements and block excerpts showing each requirement group, the event statuses, the server event, the money property, the removal date and every Turn 2 fact.

### Pass / fail

- **Pass**: Task Mode from plain wording, one scope question block under a task-lane clarification label, no early task block, then one DATA task block with the required sections, every event, status and property from the plan, the deprecated event's removal date, the proposed event unbuilt, every Turn 2 fact and no file claim
- **Fail**: The runtime renders a task before Turn 2 or routes elsewhere, prints `Path:` or `Saved:`, claims a file, promotes `date_changed`, mishandles the `checkout_complete` removal, counts bookings from the wrong event, sends the server event from a client, changes the money format, scopes the FE or BE build into the DATA task, drops a Turn 2 fact or leaves a template slot

### Failure triage

1. Check the task framing route at `Product Owner - System - Router Contract` line 356 and `Product Owner - System - Interactive Mode` line 100, then the missing-scope question rule at `Custom Instructions.md` line 108 and the clarification label at line 228
2. Compare the block with the Canonical Task template at `Product Owner - Assets - Task Templates` line 19 and the requirement grammar at `Product Owner - Templates - Task Mode` lines 82 to 92
3. Diff every event, status and property against `roamstay-booking-funnel-tracking-plan.md` lines 17 to 77 and every scope fact against Turn 2

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PTK-006 | Data tracking task | Verify a plain request and one answer become a faithful DATA task block | `Can you write a task for the booking funnel events in Nadia's tracking plan, context/roamstay-booking-funnel-tracking-plan.md? Our conventions are in context/roamstay-context.md.` | 1. Stage and panel baseline -> 2. Submit Turn 1 fresh -> 3. Confirm wait and submit Turn 2 -> 4. Inspect the task block | Step 1: baseline known. Step 2: Task Mode from plain wording, one question block with a clarification label. Step 3: state retained. Step 4: required sections, events and statuses intact, removal date kept, proposed event unbuilt, Turn 2 facts intact | Both replies, rendered blocks, labels, no-file statements and artifact excerpts | PASS if routing, the scope question and a faithful DATA task block all match with no file claim. FAIL otherwise | 1. Check the framing route and scope rule. 2. Check the task template. 3. Diff events, statuses and Turn 2 facts |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, the missing-scope question rule, Deliverable Block and export-equivalent contract |
| [`Product Owner - System - Router Contract - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Router%20Contract%20-%20v0.100.md) | The task framing pattern the plain request matches |
| [`Product Owner - Templates - Task Mode - v0.306.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Task%20Mode%20-%20v0.306.md) | Project task workflow, the ask-first rule, required sections and requirement grammar |
| [`Product Owner - Assets - Task Templates - v0.102.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Task%20Templates%20-%20v0.102.md) | Project Canonical Task scaffold |
| [`Product Owner - System - Interactive Mode - v0.407.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.407.md) | Clear natural-language task row and clarification delivery |
| [`roamstay-context.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Attachment: services, squads, the `DATA` discipline, the `TRK` code and the analytics conventions |
| [`roamstay-booking-funnel-tracking-plan.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-booking-funnel-tracking-plan.md) | Attachment: the funnel events, statuses, properties, per-event notes, comments and the build split |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PTK-006
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/data-tracking-task.md`
