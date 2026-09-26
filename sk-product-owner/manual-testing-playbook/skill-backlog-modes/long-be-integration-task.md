---
title: "STK-003 -- Long BE integration task"
description: "Validates that a task shortcut carrying a full scope asks one context question, then saves a long Fernhouse back end task for label webhook idempotency and retries that keeps every carrier value, every agreed fix and the rejected polling option out."
version: 1.1.0.0
---

# STK-003 -- Long BE integration task

This scenario validates the `$t` shortcut from a long, context-heavy request to a saved back end integration task, through one clarification turn.

---

## 1. OVERVIEW

A Fernhouse engineering lead asks for the back end task behind the label webhook fix. Turn 1 carries the most context of any task scenario: the owner, the three attachments and the five agreed points, with polling only ruled out. `$t` is the `$task` shortcut, so Task Mode still asks its context question before drafting and Turn 1 saves a task-lane clarification. Turn 2 answers with what the sources do not hold: no parent, the Fulfilment board, live before the November peak, a staging replay as the done condition, a late `label.created` that must change nothing, and the 8-second warehouse timeout kept but moved out of the request.

The attachments carry two kinds of fact. The carrier API notes give the contract: `POST /v1/shipments` with no idempotency key, `GET /v1/shipments/{shipment_id}`, `label.created` and `label.failed` on `/webhooks/carrier/labels`, `event_id` as the dedupe key, the hex `HMAC-SHA256` in `X-Carrier-Signature` with `401` on a mismatch, a `5 seconds` wait, `5 attempts` at `1 min, 5 min, 15 min, 1 h, 6 h`, a `label_url` that expires after `24 hours` and `20 requests per second` for the whole account. The `#fulfilment-eng` thread gives the incident and the fix: `37 duplicate labels` at `€0.42` each, `12 orders` paid before the `15:00` cut-off that shipped a day late, the cause the logs showed, processed ids kept `7 days`, a GET after `10 minutes`, an alert in `#fulfilment-alerts` after `30 minutes`, a page when `more than 5` are stuck, and `polling only` marked `rejected` because of the rate limit. Three carrier questions are still open and stay open.

A task that reads like the team's own carries a title in the `{Discipline} - {Feature code} - {Title}` form the context gives for back end work, here `BE` and `SHIP`, an About with the incident and its cause, the two sources and the thread channel as plain-text references, and one numbered requirement group per agreed point, each with a `**Checklist**`, plus the acceptance from Turn 2 and an out-of-scope note for polling. The corpus closes such tasks with a Resolution Checklist and a QA sign-off. No routed template names that list or the title code, so both are recorded, never graded (root section 5, Ticket realism).

### Why this matters

Integration tasks are where invented facts cost the most. A task that promises the carrier's idempotency header, settles an open carrier question or quietly brings polling back sends the engineer to build against behavior nobody has.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the `$t` shortcut, the single context question and a long back end task that keeps every carrier value and thread decision and adds nothing the sources do not state
- Real user request: `Joris needs the ticket for the label webhook fix we agreed in the fulfilment thread.`
- Prompt: `$t BE task for the label webhook fix, Joris is taking it. The carrier API facts are in context/fernhouse-carrier-label-api-notes.md, the fix Noor summarised is at the end of context/fernhouse-carrier-label-thread.md and our ticket conventions are in context/fernhouse-context.md. Scope is the five points from the thread: answer inside the carrier's timeout and work from a queue, dedupe on event_id, guard against a second open shipment for a parcel, the 10-minute GET for stragglers and the alerting. Polling only stays out, the thread rejected it.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md), [fernhouse-carrier-label-api-notes.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-carrier-label-api-notes.md), [fernhouse-carrier-label-thread.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-carrier-label-thread.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and all three attachments sit in `context/` in the sandbox
- Expected execution process: Start fresh, submit Turn 1, inspect the clarification export, answer in Turn 2 in the same session and inspect the task export
- Expected signals: `$t` is the `$task` shortcut (`AGENTS.md` line 190) and an explicit command still asks its context question once and waits (`AGENTS.md` line 287, `references/task-mode.md` line 50, `references/interactive-mode.md` line 124). The question is saved as `export/[###] - task-[description]-clarification.md`, holding the question and nothing else, read back, and the reply carries its path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (`AGENTS.md` line 82, root section 5, Clarification turns). Re-asking for the scope Turn 1 already gave is recorded only (root section 5, Ticket realism). Turn 2 saves `export/[###] - task-[description].md` on the next number, reads it back and replies path first with the `Verified:` line and the `HVR self-scan:` line (`AGENTS.md` lines 46 and 47). The task follows the Canonical Task template (`assets/task-templates.md` line 38): H1, `## About` and `### Requirements` (`references/task-mode.md` lines 72 to 78) and numbered groups each with a `**Checklist**` of `- []` items (lines 102 to 112). About carries the incident and the cause as the thread states them (`fernhouse-carrier-label-thread.md` lines 9 to 27). Requirements cover the five points with the thread's values (lines 33 to 37 and 59 to 63) and every carrier value a requirement builds or checks verbatim (`fernhouse-carrier-label-api-notes.md` lines 13 to 68), keep `polling only` out as `rejected` (thread line 53), state that the carrier has no idempotency key so the open-shipment guard is Fernhouse's own (API notes line 18, thread line 35), and leave the three open carrier questions open (API notes lines 72 to 74). Every Turn 2 fact survives: no parent, the Fulfilment board (in the task or the reply's delivery or ClickUp line), live before the November peak, the staging replay giving one shipment and one label per parcel, a late `label.created` changing nothing, and the 8-second warehouse timeout kept outside the request. Joris may appear as the owner
- Desired user-visible outcome: One saved task-lane question, then a saved back end task for label webhook idempotency and retries that a Fulfilment engineer can build and test from
- Size band (advisory): 110 to 220 lines of artifact body
- Pass/fail: PASS if Turn 1 asks one question, saves it under a `task` lane `-clarification` name reported with its path, the `Verified:` line and the `HVR self-scan:` line and drafts no task, and Turn 2 saves one `task` export on the next number, read back and reported the same way, carrying its H1, `## About` and `### Requirements` with a checklisted group for each of the five points, the carrier values `event_id`, `X-Carrier-Signature`, `HMAC-SHA256` and `5 seconds` verbatim, with any retry count or schedule the task states unchanged, the thread values `7 days`, `10 minutes`, `30 minutes`, `#fulfilment-alerts` and `more than 5` verbatim, polling only kept out, and every Turn 2 fact, the Fulfilment board counting when either the task or the reply's delivery or ClickUp line names it. FAIL if Turn 1 drafts the task, the task claims the carrier offers an idempotency key or dedupes on `reference`, changes a retry step, window or alert threshold, builds or offers polling only, answers an open carrier question, names a queue, store or vendor product no attachment names, invents a cause beyond the thread's, drops a Turn 2 fact, or leaves a template slot or a placeholder link in the body
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$t BE task for the label webhook fix, Joris is taking it. The carrier API facts are in context/fernhouse-carrier-label-api-notes.md, the fix Noor summarised is at the end of context/fernhouse-carrier-label-thread.md and our ticket conventions are in context/fernhouse-context.md. Scope is the five points from the thread: answer inside the carrier's timeout and work from a queue, dedupe on event_id, guard against a second open shipment for a parcel, the 10-minute GET for stragglers and the alerting. Polling only stays out, the thread rejected it.` | Read all three attachments, ask the task context question once on what the sources leave open, save it as a task-lane clarification, read it back and reply with its path, the `Verified:` line and the `HVR self-scan:` line. Draft no task | Task Mode, the five points and the polling exclusion stay selected, one new `-clarification` file, `context/` unchanged | Turn 1 reply, clarification file, read-back result and side-effect ledger |
| 2 | `No parent, it goes on the Fulfilment board and has to be live before the November peak. Done means replaying a slow afternoon in staging gives one shipment and one label per parcel, and a label.created that lands after the 10-minute GET already took the label changes nothing. Keep our 8-second timeout on the warehouse system, only move that call out of the request.` | Build the task from the three sources and the answer, save it on the next number, read it back and reply path first with the `Verified:` line and the `HVR self-scan:` line | The five points, the carrier values, the thread values, the polling exclusion and every Turn 2 fact survive, the clarification file stays untouched | Turn 2 reply, task export, read-back result and side-effect ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$t BE task for the label webhook fix, Joris is taking it. The carrier API facts are in context/fernhouse-carrier-label-api-notes.md, the fix Noor summarised is at the end of context/fernhouse-carrier-label-thread.md and our ticket conventions are in context/fernhouse-context.md. Scope is the five points from the thread: answer inside the carrier's timeout and work from a queue, dedupe on event_id, guard against a second open shipment for a parcel, the 10-minute GET for stragglers and the alerting. Polling only stays out, the thread rejected it.`

### Commands

1. `sandbox: stage context/fernhouse-context.md, context/fernhouse-carrier-label-api-notes.md and context/fernhouse-carrier-label-thread.md -> record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the new task export -> operator: grade the sections, the five requirement groups, every carrier and thread value, the polling exclusion, the open questions and the Turn 2 facts`

### Expected

Step 1 fixes the baseline with all three attachments staged. Step 2 returns one context question and one clarification file. Step 3 proves the wait state and the question-only file. Step 4 finds an H1, `## About` with the incident and its cause, `### Requirements` with a numbered, checklisted group for the fast answer and queue, the `event_id` dedupe for `7 days`, the open-shipment guard, the GET after `10 minutes` and the alerting after `30 minutes` in `#fulfilment-alerts` with a page past `more than 5`, the carrier values its requirements build or check verbatim, polling only kept out, the open carrier questions left open and the Turn 2 acceptance, deadline and timeout, and the board in the task or the reply.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back lines, the self-scan lines and task excerpts showing each requirement group, the carrier and thread values, the polling exclusion and every Turn 2 fact.

### Pass / fail

- **Pass**: One context question saved as a task-lane clarification, no early draft, then one readable task export with the required sections, a checklisted group per agreed point, every carrier and thread value intact, polling only excluded, open questions left open and every Turn 2 fact
- **Fail**: The runtime drafts before Turn 2, invents a carrier idempotency key or a `reference` dedupe, changes a retry, window or threshold, revives polling, settles an open carrier question, names an unsupplied product or cause, drops a Turn 2 fact or leaves a template slot

### Failure triage

1. Check the `$t` shortcut at `AGENTS.md` line 190 and the explicit-command question rule at line 287, then the clarification export at line 82
2. Compare the task with the Canonical Task template at `assets/task-templates.md` line 38 and the requirement grammar at `references/task-mode.md` lines 102 to 112
3. Diff every carrier value against `fernhouse-carrier-label-api-notes.md` lines 13 to 74, every thread value against `fernhouse-carrier-label-thread.md` lines 9 to 63 and every scope fact against Turn 2

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| STK-003 | Long BE integration task | Verify a context-heavy shortcut request and one answer become a faithful back end task | `$t BE task for the label webhook fix, Joris is taking it. The carrier API facts are in context/fernhouse-carrier-label-api-notes.md, the fix Noor summarised is at the end of context/fernhouse-carrier-label-thread.md and our ticket conventions are in context/fernhouse-context.md. Scope is the five points from the thread: answer inside the carrier's timeout and work from a queue, dedupe on event_id, guard against a second open shipment for a parcel, the 10-minute GET for stragglers and the alerting. Polling only stays out, the thread rejected it.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the task export | Step 1: baseline known. Step 2: one question and one clarification. Step 3: state retained. Step 4: required sections, five checklisted groups, carrier and thread values, polling excluded, Turn 2 facts intact | Both replies, ledger, clarification and task export paths, read-back lines and artifact excerpts | PASS if routing, the context gate and a faithful back end task all match. FAIL otherwise | 1. Check the `$t` shortcut. 2. Check the task template. 3. Diff carrier, thread and Turn 2 facts |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Command registry with the `$t` shortcut, the explicit-command question rule, the clarification export and the read-back reply |
| [`SKILL.md`](../../SKILL.md) | Export names, the HVR self-scan line and the named-addition rule |
| [`task-mode.md`](../../references/task-mode.md) | Task workflow, required sections and requirement grammar |
| [`task-templates.md`](../../assets/task-templates.md) | Canonical Task scaffold |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Direct `$task` row and the clarification export |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Attachment: services, the `SHIP` code, the cut-off, the label cost rule and the title convention |
| [`fernhouse-carrier-label-api-notes.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-carrier-label-api-notes.md) | Attachment: the carrier label contract, retries, signature, rate limit and open questions |
| [`fernhouse-carrier-label-thread.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-carrier-label-thread.md) | Attachment: the incident, its cause, the five agreed points and the rejected polling option |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: STK-003
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/long-be-integration-task.md`
