---
title: "PST-004 -- Story with nested tasks"
description: "Validates that a Fernhouse order tracking Story asked for with its task breakdown renders in a Project as one Deliverable Block per file, labelled inside one bundle folder, in the split the PM names."
version: 1.0.0.1
---

# PST-004 -- Story with nested tasks

This scenario turns a Fernhouse PM brief and the parcel carrier's tracking facts into one order tracking Story with its four tasks, rendered as one linked set of Deliverable Blocks labelled inside one bundle folder.

---

## 1. OVERVIEW

The Post-purchase PM sends `$story` with Hamid's brief and Yusuf's carrier notes and asks for the work broken into tasks. A Story asked for with its task breakdown is one dependent deliverable, so the Project asks no question about which artifact to make. It still asks its one Story question, in the Story lane, and waits. The brief lists six tasks it expects. Turn 2 names four, in the order the Story lists them, and drops the other two with a reason. The Project renders one Deliverable Block per file, Story first, each labelled with its own export-equivalent path inside one folder on the next number, and claims no file was written.

### Why this matters

A Story and its tasks that arrive as loose blocks lose the thread the moment they are pasted into ClickUp one at a time. The `#### **Tasks**` block and each task's `**Story**` link are what keep the FE and BE work tied to the outcome they deliver. The split the PM names is the one the team staffs, so a bundle that follows the brief's older list of six instead builds work nobody planned.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a Story asked for with its task breakdown renders as one Deliverable Block per file, labelled inside one bundle folder, whose Story and four tasks link each other in the split the PM names, with every supplied value intact
- Real user request: `$story Order tracking on the order page, from Hamid's brief in context/fernhouse-order-tracking-pm-brief.md and Yusuf's carrier notes in context/fernhouse-carrier-tracking-api-facts.md. Please break it into tasks. Company background is in context/fernhouse-context.md.`
- Prompt: `$story Order tracking on the order page, from Hamid's brief in context/fernhouse-order-tracking-pm-brief.md and Yusuf's carrier notes in context/fernhouse-carrier-tracking-api-facts.md. Please break it into tasks. Company background is in context/fernhouse-context.md.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md), [fernhouse-order-tracking-pm-brief.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-order-tracking-pm-brief.md), [fernhouse-carrier-tracking-api-facts.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-carrier-tracking-api-facts.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and all three attachments sit at `context/<basename>` before the Canvas panel baseline is recorded
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the Story question block, submit Turn 2 in the same conversation and inspect the five rendered blocks
- Expected signals: Turn 1 routes to Story Mode on `$story` in the Story shape, reads all three attachments, asks no question about which artifact to make and asks its one consolidated Story question (`Custom Instructions.md` line 108), which asks for the task split because the request names none (`Product Owner - Templates - Story Mode` line 382). It renders that question as its own block, then `Export-equivalent path: export/[NNN] - Story-order-tracking-clarification.md`, outside any folder, and the `HVR self-scan:` line, and renders no draft. Turn 2 renders one Deliverable Block per file, Story first, then the tasks for FE iOS, FE Android, FE web and the BE tracking webhook in that order, each followed by its own `Export-equivalent path:` inside `export/[NNN] - Story-order-tracking/`: `[NNN] - Story-order-tracking.md`, then `[NNN].1` to `[NNN].4 - task-[description].md`. One `HVR self-scan:` line follows for the set, the reply names the Story kind and claims no file was written. The Story sits under a plain H1 such as `Customer - Orders - Order tracking` and holds the preamble, About, Problem, Solution, Expected outcomes, a `#### **Tasks**` block inside About after `#### **References**` where that block is present, Requirements and numbered Given/When/Then acceptance criteria. The Tasks block holds one `*   ` bullet per task in `n` order, each linking its sibling as `(<[NNN].[n] - task-[description].md>)`. Problem keeps the brief's figures (5,870 of 18,940 contacts tagged WISMO in August, 31%) and Expected outcomes the target (31% to under 20% within two months). Requirements carry `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` and `Delivery failed` in that order with their carrier codes `PU`, `IT`, `OD`, `DL` and `EX`, the estimate strings `Arriving Thursday 1 October` and `Between 10:00 and 14:00` shown only when the carrier sends a window, no estimate guessed from the dispatch date, one timeline per parcel, the pallet rule over `30 kg` or `120 cm` with its delivery slot line, events kept `90 days` after delivery, the status order read from `occurred_at`, and `Delivery failed` shown with no reason. Each task follows the Canonical Task template with `### About`, a `**Story**` block linking `(<[NNN] - Story-order-tracking.md>)`, no `**Parent task**` block and `### Requirements`. The BE tracking webhook task carries `tracking.updated`, `/webhooks/carrier/tracking`, `X-Carrier-Signature`, deduplication on `event_id`, ordering by `occurred_at`, the newest `eta_window` winning and `5 attempts` at `1 min, 5 min, 15 min, 1 h, 6 h`. No task covers `Packed` from the warehouse system or the DATA events
- Desired user-visible outcome: One Story question block in the Story lane, then five Deliverable Blocks, Story first, each labelled inside one bundle folder and linked both ways, with no file claimed
- Size band (advisory): Story 80 to 150 lines of body, each task 35 to 90 lines of body
- Pass/fail: PASS if Turn 1 asks one consolidated Story question in the Story lane, renders it as its own block with its `Export-equivalent path:` outside any folder and the `HVR self-scan:` line and renders no draft, and Turn 2 renders one Deliverable Block per file, Story first, then exactly four task blocks for FE iOS, FE Android, FE web and the BE tracking webhook in that order, each followed by its own `Export-equivalent path:` inside `export/[NNN] - Story-[description]/`, then one `HVR self-scan:` line for the set, names the Story kind and claims no file, where the Story holds About, Problem, Solution, Expected outcomes, a `#### **Tasks**` block inside About with one bullet per task in that order linking `(<[NNN].[n] - task-[description].md>)`, Requirements and numbered Given/When/Then acceptance criteria each closed by the Mark-as-done line, each task holds `### About`, a `**Story**` block linking `(<[NNN] - Story-[description].md>)`, no `**Parent task**` block and `### Requirements`, and the set carries the six statuses, the five carrier codes, `Arriving Thursday 1 October`, `Between 10:00 and 14:00`, `90 days`, `30 kg`, `120 cm`, `tracking.updated`, `/webhooks/carrier/tracking`, `event_id`, `X-Carrier-Signature`, `occurred_at`, `eta_window`, `5 attempts` and `1 min, 5 min, 15 min, 1 h, 6 h` verbatim. FAIL if it drafts in Turn 1, labels the question as `intake` or inside the folder, adds a `Packed` or DATA task, drops or reorders one of the four, renders the set as one merged block or labels the files flat or under two numbers, lists the tasks under `## Scope`, links a task to the Story through `**Parent task**`, names an epic nobody supplied, shows a reason for `Delivery failed`, guesses an estimate with no window, invents event names, polling, a tracking-history call or pallet tracking, rewrites a status, code or value, or claims a local save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$story Order tracking on the order page, from Hamid's brief in context/fernhouse-order-tracking-pm-brief.md and Yusuf's carrier notes in context/fernhouse-carrier-tracking-api-facts.md. Please break it into tasks. Company background is in context/fernhouse-context.md.` | Route to Story Mode on `$story` as one dependent deliverable, read all three attachments, ask one consolidated Story question that covers the task split, render it as a Story-lane clarification block outside any folder and wait. Create no draft | Story intent, the Story shape, order tracking and the pending task breakdown stay selected | Turn 1 reply, rendered clarification block, its label and the no-file-write statement |
| 2 | `Four tasks, in this order: FE iOS, FE Android, FE web and the BE tracking webhook. orders-service already gets "Packed" from the warehouse system, so no task for that, and the DATA events wait for a later story. "Delivery failed" shows no reason in this story, and the web layout is now done in the same "Order page / Tracking timeline" frame.` | Draft the Story and the four tasks in the named order, render one Deliverable Block per file, Story first, each with its own export-equivalent label inside the folder, then one self-scan line for the set, naming the Story kind and claiming no file | Five blocks labelled inside one folder on the next number, linked both ways | Turn 2 reply, all five rendered blocks, their labels, the Tasks block and each task's Story block |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$story Order tracking on the order page, from Hamid's brief in context/fernhouse-order-tracking-pm-brief.md and Yusuf's carrier notes in context/fernhouse-carrier-tracking-api-facts.md. Please break it into tasks. Company background is in context/fernhouse-context.md.`

### Commands

1. `sandbox: stage all three attachments at context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block and its label -> operator: confirm it holds only the question -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect all five rendered blocks and their labels -> operator: check the order, the labels, the links both ways, the house sections and every value against the brief, the carrier notes and Turn 2`

### Expected

Step 1 fixes the panel baseline with `context/` holding the three attachments. Step 2 returns one Story question as its own block, labelled in the Story lane outside any folder. Step 3 proves the wait state. Step 4 finds five blocks, Story first, then the FE iOS, FE Android, FE web and BE tracking webhook tasks, each with its own `Export-equivalent path:` inside one folder, a Story whose `#### **Tasks**` block links each task in that order, and tasks whose `**Story**` block links the Story, each with `### About` and `### Requirements` and none with a `**Parent task**` block.

### Evidence

Capture both replies, the clarification block and its label, all five rendered blocks and their labels, the self-scan line, the Tasks block, each task's Story block and the Requirements holding the statuses, codes, estimate strings and webhook facts.

### Pass / fail

- **Pass**: One Story-lane question block outside any folder, no early draft, then five blocks, Story first, each labelled inside one folder on the next number, the four named tasks in order, linked both ways, one self-scan line, every supplied value verbatim and no file claimed
- **Fail**: The runtime drafts early, labels the question `intake` or inside the folder, adds, drops or reorders a task, merges the set into one block or labels it flat, uses `## Scope` or `**Parent task**`, invents an epic, a failure reason, an estimate, event names, polling, a history call or pallet tracking, rewrites a status, code or value, or claims a local save

### Failure triage

1. Check the bundle rule and its reply shape in `Product Owner - Templates - Story Mode` and line 226 of `Custom Instructions.md`
2. Check the `**Story**` block and the Canonical Task template in `Product Owner - Assets - Task Templates`
3. Reconcile the task list against Turn 2 and every value in the brief and the carrier notes against the five blocks

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PST-004 | Story with nested tasks | Verify a Story asked for with its tasks renders as one linked set of blocks labelled inside one folder in the named split | `$story Order tracking on the order page, from Hamid's brief in context/fernhouse-order-tracking-pm-brief.md and Yusuf's carrier notes in context/fernhouse-carrier-tracking-api-facts.md. Please break it into tasks. Company background is in context/fernhouse-context.md.` | 1. Stage and canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the five blocks and labels | Step 1: baseline known. Step 2: one Story-lane question block. Step 3: split and decisions supplied. Step 4: five blocks, Story first, four tasks in order, labelled inside one folder, linked both ways, every value verbatim | Both replies, rendered blocks, labels, self-scan line, Tasks and Story blocks | PASS if the wait, the lane, the labels, the order, the links, the reply shape and every value all match. FAIL otherwise | 1. Check the bundle rule. 2. Check the task template. 3. Check the split and each value |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Line 85 the block without a Canvas panel, line 108 an explicit command still asks, line 226 the bundle folder, its links and one block per file, line 228 clarification label, line 233 no `Path:`, `Saved:` or `Verified:` |
| [`Product Owner - Templates - Story Mode - v0.403.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Story%20Mode%20-%20v0.403.md) | Line 341 the bundle exception to one artifact, lines 368 to 392 Story With Nested Tasks, line 382 a named split is authoritative, line 383 the clarification outside the folder, line 384 the Tasks block, line 385 the task template and the Story block, line 398 the bundle reply |
| [`Product Owner - Assets - Story Template - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Story%20Template%20-%20v0.100.md) | Lines 21 to 85 Story scaffold |
| [`Product Owner - Assets - Task Templates - v0.102.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Task%20Templates%20-%20v0.102.md) | Lines 19 to 133 Canonical Task template, lines 54 to 58 the `**Story**` block, line 141 the Story block in a bundle |
| [`Product Owner - System - Interactive Mode - v0.406.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.406.md) | Line 70 the Story lane for a bundle's clarification |
| [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Company context: surfaces, services, pallet limits, story and task title patterns |
| [fernhouse-order-tracking-pm-brief.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-order-tracking-pm-brief.md) | The PM brief: statuses, estimate strings, rules and the expected task list |
| [fernhouse-carrier-tracking-api-facts.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-carrier-tracking-api-facts.md) | The carrier tracking facts behind the BE tracking webhook |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project story modes
- Playbook ID: PST-004
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-story-modes/story-with-nested-tasks.md`
