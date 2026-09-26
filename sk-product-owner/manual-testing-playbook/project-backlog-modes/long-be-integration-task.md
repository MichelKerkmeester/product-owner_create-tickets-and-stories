---
title: "PTK-003 -- Long BE integration task"
description: "Validates that a task shortcut carrying a full scope renders one context question block, then a long Fernhouse back end task block in a Claude Project for label webhook idempotency and retries that keeps every carrier value, every agreed fix and the rejected polling option out."
version: 1.0.0.2
---

# PTK-003 -- Long BE integration task

This scenario validates the `$t` shortcut from a long, context-heavy request to a rendered back end integration task block, through one clarification turn.

---

## 1. OVERVIEW

A Fernhouse engineering lead asks for the back end task behind the label webhook fix. Turn 1 carries the most context of any task scenario: the owner, the three attachments and the five agreed points, with polling only ruled out. `$t` is the `$task` shortcut, so Task Mode still asks its context question before drafting and Turn 1 renders a task-lane clarification block. Turn 2 answers with what the sources do not hold: no parent, the Fulfilment board, live before the November peak, a staging replay as the done condition, a late `label.created` that must change nothing, and the 8-second warehouse timeout kept but moved out of the request.

The attachments carry two kinds of fact. The carrier API notes give the contract: `POST /v1/shipments` with no idempotency key, `GET /v1/shipments/{shipment_id}`, `label.created` and `label.failed` on `/webhooks/carrier/labels`, `event_id` as the dedupe key, the hex `HMAC-SHA256` in `X-Carrier-Signature` with `401` on a mismatch, a `5 seconds` wait, `5 attempts` at `1 min, 5 min, 15 min, 1 h, 6 h`, a `label_url` that expires after `24 hours` and `20 requests per second` for the whole account. The `#fulfilment-eng` thread gives the incident and the fix: `37 duplicate labels` at `€0.42` each, `12 orders` paid before the `15:00` cut-off that shipped a day late, the cause the logs showed, processed ids kept `7 days`, a GET after `10 minutes`, an alert in `#fulfilment-alerts` after `30 minutes`, a page when `more than 5` are stuck, and `polling only` marked `rejected` because of the rate limit. Three carrier questions are still open and stay open.

A task that reads like the team's own carries a title in the `{Discipline} - {Feature code} - {Title}` form the context gives for back end work, here `BE` and `SHIP`, an About with the incident and its cause, the two sources and the thread channel as plain-text references, and one numbered requirement group per agreed point, each with a `**Checklist**`, plus the acceptance from Turn 2 and an out-of-scope note for polling. The corpus closes such tasks with a Resolution Checklist and a QA sign-off. No routed template names that list or the title code, so both are recorded, never graded (root section 5, Ticket realism).

### Why this matters

Integration tasks are where invented facts cost the most, and the Project's block is what reaches the board. A block that promises the carrier's idempotency header, settles an open carrier question or quietly brings polling back sends the engineer to build against behavior nobody has.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the `$t` shortcut, the single context question and a long back end task block that keeps every carrier value and thread decision and adds nothing the sources do not state
- Real user request: `Joris needs the ticket for the label webhook fix we agreed in the fulfilment thread.`
- Prompt: `$t BE task for the label webhook fix, Joris is taking it. The carrier API facts are in context/fernhouse-carrier-label-api-notes.md, the fix Noor summarised is at the end of context/fernhouse-carrier-label-thread.md and our ticket conventions are in context/fernhouse-context.md. Scope is the five points from the thread: answer inside the carrier's timeout and work from a queue, dedupe on event_id, guard against a second open shipment for a parcel, the 10-minute GET for stragglers and the alerting. Polling only stays out, the thread rejected it.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md), [fernhouse-carrier-label-api-notes.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-carrier-label-api-notes.md), [fernhouse-carrier-label-thread.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-carrier-label-thread.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and all three attachments sit in `context/` in the sandbox
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the clarification block, answer in Turn 2 in the same conversation and inspect the rendered task block
- Expected signals: `$t` routes as `$task` and an explicit command still asks its context question once and waits (`Custom Instructions.md` line 108, `Product Owner - Templates - Task Mode` line 30, `Product Owner - System - Interactive Mode` line 101). The question renders as its own block, then `Export-equivalent path: export/[NNN] - task-[description]-clarification.md` (`Custom Instructions.md` line 228) and the `HVR self-scan:` line, with no file claim and no task (`Product Owner - System - Interactive Mode` lines 62 and 70, root section 5, Clarification turns). Re-asking for the scope Turn 1 already gave is recorded only (root section 5, Ticket realism). Turn 2 renders the task as the Deliverable Block before any commentary, fenced where there is no Canvas panel (`Custom Instructions.md` line 85), then `Export-equivalent path: export/[NNN] - task-[description].md` (line 223) and the `HVR self-scan:` line (line 89), with no claim that a file was written (line 101). The block follows the Canonical Task template (`Product Owner - Assets - Task Templates` line 19): H1, `### About` and `### Requirements` (`Product Owner - Templates - Task Mode` lines 52 to 58) and numbered groups each with a `**Checklist**` of `- [ ]` items (lines 82 to 92). About carries the incident and the cause as the thread states them (`fernhouse-carrier-label-thread.md` lines 9 to 27). Requirements cover the five points with the thread's values (lines 33 to 37 and 59 to 63) and the carrier's contract verbatim (`fernhouse-carrier-label-api-notes.md` lines 13 to 68), keep `polling only` out as `rejected` (thread line 53), state that the carrier has no idempotency key so the open-shipment guard is Fernhouse's own (API notes line 18, thread line 35), and leave the three open carrier questions open (API notes lines 72 to 74). Every Turn 2 fact survives: no parent, the Fulfilment board, live before the November peak, the staging replay giving one shipment and one label per parcel, a late `label.created` changing nothing, and the 8-second warehouse timeout kept outside the request. Joris may appear as the owner
- Desired user-visible outcome: One task-lane question block, then a back end task block for label webhook idempotency and retries that a Fulfilment engineer can build and test from, each labelled export-equivalent with no file claim
- Size band (advisory): 110 to 220 lines of artifact body
- Pass/fail: PASS if Turn 1 asks one question rendered as its own block under an export-equivalent `task` lane `-clarification` label with the `HVR self-scan:` line and renders no task, and Turn 2 renders one task block under an export-equivalent `task` label with the `HVR self-scan:` line and no file claim, carrying its H1, `### About` and `### Requirements` with a checklisted group for each of the five points, the carrier values `event_id`, `X-Carrier-Signature`, `HMAC-SHA256`, `5 seconds`, `5 attempts` and `1 min, 5 min, 15 min, 1 h, 6 h` verbatim, the thread values `7 days`, `10 minutes`, `30 minutes`, `#fulfilment-alerts` and `more than 5` verbatim, polling only kept out, and every Turn 2 fact. FAIL if Turn 1 renders the task, a reply prints `Path:`, `Saved:` or `Verified:` or claims a file, the task claims the carrier offers an idempotency key or dedupes on `reference`, changes a retry step, window or alert threshold, builds or offers polling only, answers an open carrier question, names a queue, store or vendor product no attachment names, invents a cause beyond the thread's, drops a Turn 2 fact, or leaves a template slot or a placeholder link in the block
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$t BE task for the label webhook fix, Joris is taking it. The carrier API facts are in context/fernhouse-carrier-label-api-notes.md, the fix Noor summarised is at the end of context/fernhouse-carrier-label-thread.md and our ticket conventions are in context/fernhouse-context.md. Scope is the five points from the thread: answer inside the carrier's timeout and work from a queue, dedupe on event_id, guard against a second open shipment for a parcel, the 10-minute GET for stragglers and the alerting. Polling only stays out, the thread rejected it.` | Read all three attachments, ask the task context question once on what the sources leave open, render it as a clarification block with an export-equivalent label and the `HVR self-scan:` line and wait. Claim no file and render no task | Task Mode, the five points and the polling exclusion stay selected, no task block exists | Turn 1 reply, rendered clarification block, its label and the no-file statement |
| 2 | `No parent, it goes on the Fulfilment board and has to be live before the November peak. Done means replaying a slow afternoon in staging gives one shipment and one label per parcel, and a label.created that lands after the 10-minute GET already took the label changes nothing. Keep our 8-second timeout on the warehouse system, only move that call out of the request.` | Render the task block from the three sources and the answer, then its export-equivalent label and the `HVR self-scan:` line, with no file claim | The five points, the carrier values, the thread values, the polling exclusion and every Turn 2 fact survive | Turn 2 reply, rendered task block, its label and the no-file statement |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$t BE task for the label webhook fix, Joris is taking it. The carrier API facts are in context/fernhouse-carrier-label-api-notes.md, the fix Noor summarised is at the end of context/fernhouse-carrier-label-thread.md and our ticket conventions are in context/fernhouse-context.md. Scope is the five points from the thread: answer inside the carrier's timeout and work from a queue, dedupe on event_id, guard against a second open shipment for a parcel, the 10-minute GET for stragglers and the alerting. Polling only stays out, the thread rejected it.`

### Commands

1. `sandbox: stage context/fernhouse-context.md, context/fernhouse-carrier-label-api-notes.md and context/fernhouse-carrier-label-thread.md -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `operator: confirm one context question block and no task block -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered task block -> operator: grade the sections, the five requirement groups, every carrier and thread value, the polling exclusion, the open questions, the Turn 2 facts, the labels and the no-file boundary`

### Expected

Step 1 fixes the panel baseline with all three attachments staged. Step 2 returns one context question as its own block with a `-clarification` label. Step 3 proves the wait state and state retention. Step 4 finds an H1, `### About` with the incident and its cause, `### Requirements` with a numbered, checklisted group for the fast answer and queue, the `event_id` dedupe for `7 days`, the open-shipment guard, the GET after `10 minutes` and the alerting after `30 minutes` in `#fulfilment-alerts` with a page past `more than 5`, the carrier contract values verbatim, polling only kept out, the open carrier questions left open and the Turn 2 acceptance, deadline, board and timeout, under an export-equivalent label.

### Evidence

Capture both replies, both rendered blocks and which form each took, the two export-equivalent labels, the self-scan lines, the no-file statements and block excerpts showing each requirement group, the carrier and thread values, the polling exclusion and every Turn 2 fact.

### Pass / fail

- **Pass**: One context question block under a task-lane clarification label, no early task block, then one task block with the required sections, a checklisted group per agreed point, every carrier and thread value intact, polling only excluded, open questions left open, every Turn 2 fact and no file claim
- **Fail**: The runtime renders the task before Turn 2, prints `Path:` or `Saved:`, claims a file, invents a carrier idempotency key or a `reference` dedupe, changes a retry, window or threshold, revives polling, settles an open carrier question, names an unsupplied product or cause, drops a Turn 2 fact or leaves a template slot

### Failure triage

1. Check the explicit-command question rule at `Custom Instructions.md` line 108 and `Product Owner - System - Interactive Mode` line 101, then the clarification label at `Custom Instructions.md` line 228
2. Compare the block with the Canonical Task template at `Product Owner - Assets - Task Templates` line 19 and the requirement grammar at `Product Owner - Templates - Task Mode` lines 82 to 92
3. Diff every carrier value against `fernhouse-carrier-label-api-notes.md` lines 13 to 74, every thread value against `fernhouse-carrier-label-thread.md` lines 9 to 63 and every scope fact against Turn 2

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PTK-003 | Long BE integration task | Verify a context-heavy shortcut request and one answer become a faithful back end task block | `$t BE task for the label webhook fix, Joris is taking it. The carrier API facts are in context/fernhouse-carrier-label-api-notes.md, the fix Noor summarised is at the end of context/fernhouse-carrier-label-thread.md and our ticket conventions are in context/fernhouse-context.md. Scope is the five points from the thread: answer inside the carrier's timeout and work from a queue, dedupe on event_id, guard against a second open shipment for a parcel, the 10-minute GET for stragglers and the alerting. Polling only stays out, the thread rejected it.` | 1. Stage and panel baseline -> 2. Submit Turn 1 fresh -> 3. Confirm wait and submit Turn 2 -> 4. Inspect the task block | Step 1: baseline known. Step 2: one question block with a clarification label. Step 3: state retained. Step 4: required sections, five checklisted groups, carrier and thread values, polling excluded, Turn 2 facts intact | Both replies, rendered blocks, labels, no-file statements and artifact excerpts | PASS if routing, the context gate and a faithful back end task block all match with no file claim. FAIL otherwise | 1. Check the `$t` route and question rule. 2. Check the task template. 3. Diff carrier, thread and Turn 2 facts |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, the explicit-command question rule, the named-addition rule, Deliverable Block and export-equivalent contract |
| [`Product Owner - Templates - Task Mode - v0.305.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Task%20Mode%20-%20v0.305.md) | Project task workflow, required sections and requirement grammar |
| [`Product Owner - Assets - Task Templates - v0.102.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Task%20Templates%20-%20v0.102.md) | Project Canonical Task scaffold |
| [`Product Owner - System - Interactive Mode - v0.407.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.407.md) | Direct `$task` row and clarification delivery |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Attachment: services, the `SHIP` code, the cut-off, the label cost rule and the title convention |
| [`fernhouse-carrier-label-api-notes.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-carrier-label-api-notes.md) | Attachment: the carrier label contract, retries, signature, rate limit and open questions |
| [`fernhouse-carrier-label-thread.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-carrier-label-thread.md) | Attachment: the incident, its cause, the five agreed points and the rejected polling option |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PTK-003
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/long-be-integration-task.md`
