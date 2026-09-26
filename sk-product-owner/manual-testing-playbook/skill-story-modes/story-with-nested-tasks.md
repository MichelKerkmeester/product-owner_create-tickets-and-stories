---
title: "SST-004 -- Story with nested tasks"
description: "Validates that a Fernhouse order tracking Story asked for with its task breakdown saves as one bundle folder holding the Story and four linked tasks in the split the PM names."
version: 1.0.0.0
---

# SST-004 -- Story with nested tasks

This scenario turns a Fernhouse PM brief and the parcel carrier's tracking facts into one order tracking Story with its four tasks, saved together as one linked bundle.

---

## 1. OVERVIEW

The Post-purchase PM sends `$story` with Hamid's brief and Yusuf's carrier notes and asks for the work broken into tasks. A Story asked for with its task breakdown is one dependent deliverable, so the runtime asks no question about which artifact to make (`AGENTS.md` line 208). It still asks its one Story question, in the Story lane, and waits. The brief lists six tasks it expects. Turn 2 names four, in the order the Story lists them, and drops the other two with a reason. The runtime saves one folder on the next number holding the Story and the four tasks, each file linking the others, and reads every file back.

### Why this matters

A Story and its tasks that ship as loose files lose the thread the moment they are pasted into ClickUp one at a time. The `#### **Tasks**` block and each task's `**Story**` link are what keep the FE and BE work tied to the outcome they deliver. The split the PM names is the one the team staffs, so a bundle that follows the brief's older list of six instead builds work nobody planned.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a Story asked for with its task breakdown saves as one bundle folder whose Story and four tasks link each other, in the split the PM names, with every supplied value intact
- Real user request: `$story Order tracking on the order page, from Hamid's brief in context/fernhouse-order-tracking-pm-brief.md and Yusuf's carrier notes in context/fernhouse-carrier-tracking-api-facts.md. Please break it into tasks. Company background is in context/fernhouse-context.md.`
- Prompt: `$story Order tracking on the order page, from Hamid's brief in context/fernhouse-order-tracking-pm-brief.md and Yusuf's carrier notes in context/fernhouse-carrier-tracking-api-facts.md. Please break it into tasks. Company background is in context/fernhouse-context.md.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md), [fernhouse-order-tracking-pm-brief.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-order-tracking-pm-brief.md), [fernhouse-carrier-tracking-api-facts.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-carrier-tracking-api-facts.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and all three attachments sit at `context/<basename>` before the export baseline is recorded
- Expected execution process: Start fresh, submit Turn 1, capture the Story question and its clarification export, submit Turn 2 in the same session and inspect the bundle folder on the next number
- Expected signals: Turn 1 routes to Story Mode on `$story` in the Story shape, reads all three attachments, asks no question about which artifact to make and asks its one consolidated Story question (`AGENTS.md` line 287), which asks for the task split because the request names none (`SKILL.md` line 252, `story-mode.md` line 406). It saves only that question as `export/[###] - Story-order-tracking-clarification.md` at the top of `export/`, outside any folder, reads it back, replies with its path, its `Verified:` read-back line and the `HVR self-scan:` line, and writes no draft and no folder. Turn 2 saves one folder on the next number, `export/[###] - Story-order-tracking/`, holding `[###] - Story-order-tracking.md` and `[###].1` to `[###].4 - task-[description].md` for FE iOS, FE Android, FE web and the BE tracking webhook, in that order. It reads every file back and replies with every path, Story first, each with its own `Verified:` read-back line and line count, then one `HVR self-scan:` line counted across the bundle, and names the Story kind. The clarification file stays untouched outside the folder. The Story sits under a plain H1 such as `Customer - Orders - Order tracking` and holds the preamble, About, Problem, Solution, Expected outcomes, a `#### **Tasks**` block inside About after `#### **References**` where that block is present, Requirements and numbered Given/When/Then acceptance criteria. The Tasks block holds one `*   ` bullet per task in `n` order, each linking its sibling as `(<[###].[n] - task-[description].md>)`. Problem keeps the brief's figures (5,870 of 18,940 contacts tagged WISMO in August, 31%) and Expected outcomes the target (31% to under 20% within two months). Requirements carry `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` and `Delivery failed` in that order with their carrier codes `PU`, `IT`, `OD`, `DL` and `EX`, the estimate strings `Arriving Thursday 1 October` and `Between 10:00 and 14:00` shown only when the carrier sends a window, no estimate guessed from the dispatch date, one timeline per parcel, the pallet rule over `30 kg` or `120 cm` with its delivery slot line, events kept `90 days` after delivery, the status order read from `occurred_at`, and `Delivery failed` shown with no reason. Each task follows the Canonical Task template with `## About`, a `**Story**` block linking `(<[###] - Story-order-tracking.md>)`, no `**Parent task**` block and `### Requirements`. The BE tracking webhook task carries `tracking.updated`, `/webhooks/carrier/tracking`, `X-Carrier-Signature`, deduplication on `event_id`, ordering by `occurred_at`, the newest `eta_window` winning and `5 attempts` at `1 min, 5 min, 15 min, 1 h, 6 h`. No task covers `Packed` from the warehouse system or the DATA events
- Desired user-visible outcome: One Story question in the Story lane, then one bundle folder holding the order tracking Story and its four tasks, linked both ways, with every path read back
- Size band (advisory): Story 80 to 150 lines of body, each task 35 to 90 lines of body
- Pass/fail: PASS if Turn 1 asks one consolidated Story question in the Story lane, saves only that question as `export/[###] - Story-[description]-clarification.md` at the top of `export/`, reads it back and replies with its path, its `Verified:` line and the `HVR self-scan:` line, with no draft and no folder, and Turn 2 saves one folder on the next number, `export/[###] - Story-[description]/`, holding the Story and exactly four task files `[###].1` to `[###].4 - task-[description].md` for FE iOS, FE Android, FE web and the BE tracking webhook in that order, reads every file back, replies with every path, Story first, each with its own `Verified:` line, then one `HVR self-scan:` line for the bundle, names the Story kind and leaves the clarification untouched outside the folder, where the Story holds About, Problem, Solution, Expected outcomes, a `#### **Tasks**` block inside About with one bullet per task in that order linking `(<[###].[n] - task-[description].md>)`, Requirements and numbered Given/When/Then acceptance criteria each closed by the Mark-as-done line, each task holds `## About`, a `**Story**` block linking `(<[###] - Story-[description].md>)`, no `**Parent task**` block and `### Requirements`, and the bundle carries the six statuses, the five carrier codes, `Arriving Thursday 1 October`, `Between 10:00 and 14:00`, `90 days`, `30 kg`, `120 cm`, `tracking.updated`, `/webhooks/carrier/tracking`, `event_id`, `X-Carrier-Signature`, `occurred_at`, `eta_window`, `5 attempts` and `1 min, 5 min, 15 min, 1 h, 6 h` verbatim. FAIL if it drafts in Turn 1, saves the question as `intake` or inside the folder, adds a `Packed` or DATA task, drops or reorders one of the four, writes the Story and tasks as flat files or under two numbers, lists the tasks under `## Scope`, links a task to the Story through `**Parent task**`, names an epic nobody supplied, shows a reason for `Delivery failed`, guesses an estimate with no window, invents event names, polling, a tracking-history call or pallet tracking, or rewrites a status, code or value
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$story Order tracking on the order page, from Hamid's brief in context/fernhouse-order-tracking-pm-brief.md and Yusuf's carrier notes in context/fernhouse-carrier-tracking-api-facts.md. Please break it into tasks. Company background is in context/fernhouse-context.md.` | Route to Story Mode on `$story` as one dependent deliverable, read all three attachments, ask one consolidated Story question that covers the task split, export it as a Story-lane clarification at the top of `export/`, read it back and wait. Create no draft and no folder | Story intent, the Story shape, order tracking and the pending task breakdown stay selected | Turn 1 reply, clarification export, read-back line and a ledger holding only the clarification |
| 2 | `Four tasks, in this order: FE iOS, FE Android, FE web and the BE tracking webhook. orders-service already gets "Packed" from the warehouse system, so no task for that, and the DATA events wait for a later story. "Delivery failed" shows no reason in this story, and the web layout is now done in the same "Order page / Tracking timeline" frame.` | Draft the Story and the four tasks in the named order, save them as one folder on the next number, read every file back and reply with every path, Story first, each with its read-back line, then one self-scan line for the bundle, naming the Story kind | Five files in one folder on the next number, linked both ways, and the clarification file unchanged outside it | Turn 2 reply, the folder listing, every export and read-back line, the Tasks block and each task's Story block |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$story Order tracking on the order page, from Hamid's brief in context/fernhouse-order-tracking-pm-brief.md and Yusuf's carrier notes in context/fernhouse-carrier-tracking-api-facts.md. Please break it into tasks. Company background is in context/fernhouse-context.md.`

### Commands

1. `sandbox: stage all three attachments at context/ -> filesystem: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export and confirm no folder exists -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: list the new folder and open all five files -> operator: check the names, the order, the links both ways, the house sections and every value against the brief, the carrier notes and Turn 2`

### Expected

Step 1 fixes the baseline with `context/` holding the three attachments. Step 2 returns one Story question and one clarification file at the top of `export/`. Step 3 proves the wait state. Step 4 finds one folder on the next number holding the Story and `[###].1` to `[###].4` task files in the order FE iOS, FE Android, FE web, BE tracking webhook, a Story whose `#### **Tasks**` block links each task in that order, and tasks whose `**Story**` block links the Story, each with `## About` and `### Requirements` and none with a `**Parent task**` block.

### Evidence

Capture both replies, the side-effect ledger, the clarification path, the folder listing, all five files and their read-back lines, the Tasks block, each task's Story block and the Requirements holding the statuses, codes, estimate strings and webhook facts.

### Pass / fail

- **Pass**: One Story-lane question outside any folder, no early draft, then one folder on the next number holding the Story and the four named tasks in order, linked both ways, every file read back with its own line, one self-scan line, and every supplied value verbatim
- **Fail**: The runtime drafts early, asks in the `intake` lane or inside the folder, adds, drops or reorders a task, writes flat files, uses `## Scope` or `**Parent task**`, invents an epic, a failure reason, an estimate, event names, polling, a history call or pallet tracking, or rewrites a status, code or value

### Failure triage

1. Check the bundle rule and its reply shape in `story-mode.md` and the `AGENTS.md` bundle naming block
2. Check the `**Story**` block and the Canonical Task template in `task-templates.md`
3. Reconcile the task list against Turn 2 and every value in the brief and the carrier notes against the bundle

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SST-004 | Story with nested tasks | Verify a Story asked for with its tasks saves as one linked bundle in the named split | `$story Order tracking on the order page, from Hamid's brief in context/fernhouse-order-tracking-pm-brief.md and Yusuf's carrier notes in context/fernhouse-carrier-tracking-api-facts.md. Please break it into tasks. Company background is in context/fernhouse-context.md.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the folder and its five files | Step 1: baseline known. Step 2: one Story-lane question. Step 3: split and decisions supplied. Step 4: one folder, Story plus four tasks in order, linked both ways, every value verbatim | Both replies, ledger, clarification path, folder listing, five files, read-back lines, Tasks and Story blocks | PASS if the wait, the lane, the folder, the order, the links, the reply shape and every value all match. FAIL otherwise | 1. Check the bundle rule. 2. Check the task template. 3. Check the split and each value |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Lines 84 to 91 the bundle naming block and its reply, line 208 the Routing Compatibility exception, line 287 an explicit command still asks |
| [`SKILL.md`](../../SKILL.md) | Line 207 the bundle folder and its reply, line 208 clarification export name, line 252 the task split in the Story question |
| [`story-mode.md`](../../references/story-mode.md) | Line 365 the bundle exception to one artifact, lines 392 to 416 Story With Nested Tasks, line 406 a named split is authoritative, line 407 the clarification outside the folder, line 408 the Tasks block, line 409 the task template and the Story block, line 422 the bundle reply |
| [`story-template.md`](../../assets/story-template.md) | Lines 40 to 104 Story scaffold |
| [`task-templates.md`](../../assets/task-templates.md) | Lines 38 to 152 Canonical Task template, lines 73 to 77 the `**Story**` block, line 160 the Story block in a bundle |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Line 93 the Story lane for a bundle's clarification |
| [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Company context: surfaces, services, pallet limits, story and task title patterns |
| [fernhouse-order-tracking-pm-brief.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-order-tracking-pm-brief.md) | The PM brief: statuses, estimate strings, rules and the expected task list |
| [fernhouse-carrier-tracking-api-facts.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-carrier-tracking-api-facts.md) | The carrier tracking facts behind the BE tracking webhook |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill story modes
- Playbook ID: SST-004
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-story-modes/story-with-nested-tasks.md`
