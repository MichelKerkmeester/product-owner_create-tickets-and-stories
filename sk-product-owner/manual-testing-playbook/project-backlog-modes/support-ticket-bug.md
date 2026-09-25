---
title: "PBG-002 -- Support ticket bug"
description: "Validates that a bug command handing over a Roamstay support ticket renders one evidence question as a clarification block, waits, then renders a bug block that keeps the ticket's amounts, scope and the fact that the charge is right while the Android total is wrong."
version: 1.0.0.0
---

# PBG-002 -- Support ticket bug

This scenario validates the explicit `$bug` path from an escalated support ticket to a rendered Bug Deliverable Block, through one evidence question.

---

## 1. OVERVIEW

The Roamstay Booking squad receives Guest Support ticket 58213: on Android the confirmation screen leaves city tax out of the total on stays of 2 nights or more. The ticket carries the chat, the Back office breakdown, the Tier 2 agent's tests on 1, 2 and 3 nights and on iOS, and a count of matching chats. An explicit `$bug` still asks its context question and waits, whatever the attachment holds. Turn 2 adds a severity, the test phone's Android version, the evidence situation, a web check and the fact that nobody has looked at the code. The bug block must keep the ticket's arithmetic and its central fact: the charge is right and the Android confirmation total is wrong. The Project claims no file at any point.

### Why this matters

The guest read the gap as an overcharge, and a bug that repeats that reading sends Payments after a charge that was correct while the Android screen stays wrong. A support ticket is also where amounts drift, so every total in the bug has to add up the way the ticket's does.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the single evidence question, the wait state and a bug block that keeps the ticket's values, scope and charge-versus-display fact
- Real user request: `Guest Support escalated a ticket about the Android confirmation total missing city tax, can you turn it into a bug for Booking?`
- Prompt: `$bug Guest Support escalated ticket 58213 to Booking. On Android the confirmation screen leaves city tax out of the total on stays of 2 nights or more, so the guest saw "Total €387.00" and was charged €405.00. The ticket with Maren's tests is in context/roamstay-support-ticket-58213.md and our product context is in context/roamstay-context.md`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-support-ticket-58213.md](../../../benchmark/fixtures/companies/roamstay/roamstay-support-ticket-58213.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments sit at `context/` beside the Project
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the clarification block, answer in Turn 2 and inspect the rendered bug block
- Expected signals: Turn 1 asks one bug context question and drafts nothing, because an explicit `$bug` still asks its mode's question and waits (`Custom Instructions.md` line 108, `Product Owner - Templates - Bug Mode` line 44). It renders the question alone as its own block (`Product Owner - Templates - Bug Mode` line 46), then `Export-equivalent path: export/[NNN] - bug-[description]-clarification.md` (`Custom Instructions.md` line 228) and the `HVR self-scan:` line (root section 5, Clarification turns), and claims no file. A question field the ticket already answers is recorded, not failed (root section 5, Ticket realism). Turn 2 renders one bug as its own block, a Canvas Artifact or, with no panel, one fenced block (`Custom Instructions.md` line 85), followed by `Export-equivalent path: export/[NNN] - bug-[description].md` (`Custom Instructions.md` lines 224 and 233) and the `HVR self-scan:` line, with no save or read-back claimed (`Custom Instructions.md` line 101). The bug follows the fixed order (`Product Owner - Templates - Bug Mode` lines 110 to 118) and carries ticket `58213`, booking `RS-7Q4K2M`, Android `8.12.1`, `Pay now`, `3 nights` and `2 adults`, the confirmation screen's "Total €387.00" against the `€405.00` charge, which is `€387.00` plus `€18.00` city tax at `€3.00` per adult per night. It keeps the 2-night test, where the payment step showed the City tax line and `€270.00` and the confirmation showed Total `€258.00` for a `€270.00` charge, and the correct 1-night total, iOS `8.12.0` total and confirmation email. Severity reads `High` from Turn 2. Device reads `Not provided`, and any OS value names only the test phone's Android 14 (`Product Owner - Templates - Bug Mode` line 236). Frequency carries only what the ticket states, `Always` for Android `8.12.1` Pay now stays of 2 nights or more on the escalation's every-guest claim, or `Not provided`, never a label read off the `14 chats` (`Product Owner - Templates - Bug Mode` line 240). Steps use only what the ticket shows, the guest's booking or the agent's 2-night test (`Product Owner - Templates - Bug Mode` line 216). Expected Behavior has the Android confirmation total match the charge, city tax included, as the payment step, the email and iOS already do. Whether Pay at property bookings are affected stays unknown, as the ticket says. A title with no discipline code is recorded only (root section 5, Ticket realism)
- Desired user-visible outcome: One evidence question rendered as a clarification block, then one bug block for the Booking squad under an export-equivalent label, with no file claimed
- Size band (advisory): 60 to 110 lines of artifact body
- Pass/fail: PASS if Turn 1 asks one question, renders it as its own question-only block with `Export-equivalent path:` under the `bug` word and the `-clarification` suffix and the `HVR self-scan:` line and drafts nothing, and Turn 2 renders one bug as its own block with `Export-equivalent path:` under the `bug` word and the `HVR self-scan:` line, claims no file on either turn, and the bug carries every required template section, ticket `58213`, `RS-7Q4K2M`, Android `8.12.1`, `Pay now`, "Total €387.00" shown against `€405.00` charged and the `€18.00` city tax that makes the difference, Severity `High`, no device model, every other amount exactly as the ticket gives it and adding up, the charge described as correct and the Android confirmation total as the defect, and the scope held to Android `8.12.1` Pay now stays of 2 nights or more, with no claim that the 1-night total, iOS `8.12.0` or web shows a wrong total. FAIL if Turn 1 drafts, either turn claims a saved or verified file, the bug calls the guest overcharged or the charge wrong, alters or miscomputes an amount, claims iOS or web is affected, states whether Pay at property is affected, derives Frequency from the 14 chats, invents a device model, a root cause or a reproduction step, or leaves a template slot unfilled
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$bug Guest Support escalated ticket 58213 to Booking. On Android the confirmation screen leaves city tax out of the total on stays of 2 nights or more, so the guest saw "Total €387.00" and was charged €405.00. The ticket with Maren's tests is in context/roamstay-support-ticket-58213.md and our product context is in context/roamstay-context.md` | Read both attachments, ask one bug context question, render it as a question-only clarification block with its export-equivalent label and the `HVR self-scan:` line, and claim no file. Create no bug draft | Bug Mode at Standard energy, ticket 58213 and the Android confirmation total held as the subject | Turn 1 reply, rendered clarification block, its label and the no-file-write statement |
| 2 | `Severity High. We do not know the guest's phone model, and Maren's test phone runs Android 14. No screen recording, and the guest's screenshot stays in the support desk tool. I checked web this morning with a 3-night Pay now booking and its confirmation total was right. No related bug is open, and nobody on Booking has looked at the code yet.` | Build the bug from the ticket and the answer, keep every amount and scope limit as the ticket states it, write `Not provided` where nothing was supplied, render it as one bug block and report its export-equivalent label and the `HVR self-scan:` line with no file claim | The charge stays correct and the display stays the defect, the 1-night total, iOS and web stay right, Pay at property stays unknown and no cause appears | Turn 2 reply, rendered bug block, its label and the field table, observed, steps and expected text |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$bug Guest Support escalated ticket 58213 to Booking. On Android the confirmation screen leaves city tax out of the total on stays of 2 nights or more, so the guest saw "Total €387.00" and was charged €405.00. The ticket with Maren's tests is in context/roamstay-support-ticket-58213.md and our product context is in context/roamstay-context.md`

### Commands

1. `sandbox: stage context/roamstay-context.md and context/roamstay-support-ticket-58213.md -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered bug block -> operator: grade the field table, the amounts, the scope, the steps, the checklist and the label against the ticket and Turn 2`

### Expected

Step 1 fixes the panel baseline with both attachments staged. Step 2 returns one evidence question as its own clarification block under its label. Step 3 proves the wait state. Step 4 finds `### About` with the field table reading Severity `High`, `**1. Observed Behavior**` with "Total €387.00" against the `€405.00` charge on booking `RS-7Q4K2M`, numbered steps from the ticket, `**2. Expected Behavior**` with the confirmation total matching the charge, city tax included, and the four Checklist items.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the field table values, every amount the bug states, the scope statements for 1 night, iOS, web and Pay at property, the steps and the checklist.

### Pass / fail

- **Pass**: One evidence question rendered as its own block under its label, no early draft, and one rendered bug block under an export-equivalent label with the `bug` word, every required section, the ticket's amounts intact and adding up, the charge kept correct, the Android confirmation total kept as the defect, the scope held to Android `8.12.1` Pay now stays of 2 nights or more and no file claim
- **Fail**: The runtime drafts before Turn 2, claims a local file, calls the charge wrong or the guest overcharged, changes or miscomputes an amount, widens or narrows the scope the ticket sets, derives a frequency from the chat count, or invents a device, a cause or a step

### Failure triage

1. Check the explicit-command wait in `Custom Instructions.md` and the clarification block rule in `Product Owner - Templates - Bug Mode`
2. Recompute every amount in the bug against the Back office breakdown and the agent's tests in `roamstay-support-ticket-58213.md`
3. Compare the field table with the Frequency and `Not provided` rules in `Product Owner - Assets - Bug Report Template` and strike any cause or step the ticket never gave

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PBG-002 | Support ticket bug | Verify one evidence question, then a bug block that keeps the support ticket's amounts, scope and charge-versus-display fact | `$bug Guest Support escalated ticket 58213 to Booking. On Android the confirmation screen leaves city tax out of the total on stays of 2 nights or more, so the guest saw "Total €387.00" and was charged €405.00. The ticket with Maren's tests is in context/roamstay-support-ticket-58213.md and our product context is in context/roamstay-context.md` | 1. Stage and panel baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the bug block | Step 1: baseline known. Step 2: one evidence question block. Step 3: wait state. Step 4: fixed structure, ticket amounts adding up, charge right and display wrong, label present | Both replies, rendered blocks, labels and artifact excerpts | PASS if the question, the wait and a bug block keeping every ticket value, the arithmetic and the scope all hold with no invented fact and no file claim. FAIL otherwise | 1. Check the command wait. 2. Recompute the amounts. 3. Check the field table and strike any cause |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Clarification turns, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, the explicit-command wait, the Deliverable Block and the export-equivalent contract |
| [`Product Owner - Templates - Bug Mode - v0.203.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Bug%20Mode%20-%20v0.203.md) | Project bug workflow, evidence rules, Frequency recovery and fixed structure |
| [`Product Owner - Assets - Bug Report Template - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Bug%20Report%20Template%20-%20v0.100.md) | Field table, Frequency rules and Checklist |
| [`Product Owner - System - Interactive Mode - v0.405.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.405.md) | Clarification delivery contract |
| [`roamstay-context.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Attachment: surfaces, app versions, city tax and Pay now |
| [`roamstay-support-ticket-58213.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-support-ticket-58213.md) | Attachment: the chat, the Back office breakdown, the agent's tests and the escalation |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PBG-002
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/support-ticket-bug.md`
