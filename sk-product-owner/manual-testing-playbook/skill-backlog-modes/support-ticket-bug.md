---
title: "SBG-002 -- Support ticket bug"
description: "Validates that a bug command handing over a Roamstay support ticket asks one evidence question, waits, then saves a bug that keeps the ticket's amounts, scope and the fact that the charge is right while the Android total is wrong."
version: 1.0.0.0
---

# SBG-002 -- Support ticket bug

This scenario validates the explicit `$bug` path from an escalated support ticket to a saved bug report, through one evidence question.

---

## 1. OVERVIEW

The Roamstay Booking squad receives Guest Support ticket 58213: on Android the confirmation screen leaves city tax out of the total on stays of 2 nights or more. The ticket carries the chat, the Back office breakdown, the Tier 2 agent's tests on 1, 2 and 3 nights and on iOS, and a count of matching chats. An explicit `$bug` still asks its context question and waits, whatever the attachment holds. Turn 2 adds a severity, the test phone's Android version, the evidence situation, a web check and the fact that nobody has looked at the code. The bug must keep the ticket's arithmetic and its central fact: the charge is right and the Android confirmation total is wrong.

### Why this matters

The guest read the gap as an overcharge, and a bug that repeats that reading sends Payments after a charge that was correct while the Android screen stays wrong. A support ticket is also where amounts drift, so every total in the bug has to add up the way the ticket's does.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the single evidence question, the wait state and a bug that keeps the ticket's values, scope and charge-versus-display fact
- Real user request: `Guest Support escalated a ticket about the Android confirmation total missing city tax, can you turn it into a bug for Booking?`
- Prompt: `$bug Guest Support escalated ticket 58213 to Booking. On Android the confirmation screen leaves city tax out of the total on stays of 2 nights or more, so the guest saw "Total €387.00" and was charged €405.00. The ticket with Maren's tests is in context/roamstay-support-ticket-58213.md and our product context is in context/roamstay-context.md`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-support-ticket-58213.md](../../../benchmark/fixtures/companies/roamstay/roamstay-support-ticket-58213.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit at `context/` in the sandbox
- Expected execution process: Start fresh, submit Turn 1, capture the evidence question and its clarification export, answer in Turn 2 and inspect the next bug export
- Expected signals: Turn 1 asks one bug context question and drafts nothing, because an explicit `$bug` still asks its mode's question and waits (`AGENTS.md` line 287, `references/bug-mode.md` line 61). It saves the question alone as `export/[###] - bug-[description]-clarification.md` (`SKILL.md` line 208, `references/bug-mode.md` line 63), reads it back and replies with its path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (root section 5, Clarification turns). A question field the ticket already answers is recorded, not failed (root section 5, Ticket realism). Turn 2 saves one bug on the next number as `export/[###] - bug-[description].md` (`SKILL.md` line 207), reads it back and replies with its path and both lines. The bug follows the fixed order (`references/bug-mode.md` lines 127 to 135) and carries ticket `58213`, booking `RS-7Q4K2M`, Android `8.12.1`, `Pay now`, `3 nights` and `2 adults`, the confirmation screen's "Total €387.00" against the `€405.00` charge, which is `€387.00` plus `€18.00` city tax at `€3.00` per adult per night. It keeps the 2-night test, where the payment step showed the City tax line and `€270.00` and the confirmation showed Total `€258.00` for a `€270.00` charge, and the correct 1-night total, iOS `8.12.0` total and confirmation email. Severity reads `High` from Turn 2. Device reads `Not provided`, and any OS value names only the test phone's Android 14 (`references/bug-mode.md` line 253). Frequency carries only what the ticket states, `Always` for Android `8.12.1` Pay now stays of 2 nights or more on the escalation's every-guest claim, or `Not provided`, never a label read off the `14 chats` (`references/bug-mode.md` line 257). Steps use only what the ticket shows, the guest's booking or the agent's 2-night test (`references/bug-mode.md` line 233). Expected Behavior has the Android confirmation total match the charge, city tax included, as the payment step, the email and iOS already do. Whether Pay at property bookings are affected stays unknown, as the ticket says. A title with no discipline code is recorded only (root section 5, Ticket realism)
- Desired user-visible outcome: One evidence question saved as a clarification, then one bug export for the Booking squad that a developer can reproduce from without reopening the ticket
- Size band (advisory): 60 to 110 lines of artifact body
- Pass/fail: PASS if Turn 1 asks one question, saves it as a question-only clarification under the `bug` word with its path, `Verified:` and `HVR self-scan:` lines and drafts nothing, and Turn 2 saves one bug under the `bug` word on the next number, read back, with every required template section, ticket `58213`, `RS-7Q4K2M`, Android `8.12.1`, `Pay now`, "Total €387.00" shown against `€405.00` charged and the `€18.00` city tax that makes the difference, Severity `High`, no device model, every other amount exactly as the ticket gives it and adding up, the charge described as correct and the Android confirmation total as the defect, and the scope held to Android `8.12.1` Pay now stays of 2 nights or more, with no claim that the 1-night total, iOS `8.12.0` or web shows a wrong total. FAIL if Turn 1 drafts, the bug calls the guest overcharged or the charge wrong, alters or miscomputes an amount, claims iOS or web is affected, states whether Pay at property is affected, derives Frequency from the 14 chats, invents a device model, a root cause or a reproduction step, or leaves a template slot unfilled
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$bug Guest Support escalated ticket 58213 to Booking. On Android the confirmation screen leaves city tax out of the total on stays of 2 nights or more, so the guest saw "Total €387.00" and was charged €405.00. The ticket with Maren's tests is in context/roamstay-support-ticket-58213.md and our product context is in context/roamstay-context.md` | Read both attachments, ask one bug context question, save it as a question-only clarification, read it back and reply with its path, the `Verified:` line and the `HVR self-scan:` line. Create no bug draft | Bug Mode at Standard energy, ticket 58213 and the Android confirmation total held as the subject | Turn 1 reply, clarification export, read-back result and a ledger holding no draft |
| 2 | `Severity High. We do not know the guest's phone model, and Maren's test phone runs Android 14. No screen recording, and the guest's screenshot stays in the support desk tool. I checked web this morning with a 3-night Pay now booking and its confirmation total was right. No related bug is open, and nobody on Booking has looked at the code yet.` | Build the bug from the ticket and the answer, keep every amount and scope limit as the ticket states it, write `Not provided` where nothing was supplied, save it on the next number, read it back and reply with its path and both lines | The charge stays correct and the display stays the defect, the 1-night total, iOS and web stay right, Pay at property stays unknown and no cause appears | Turn 2 reply, bug export, read-back result and the field table, observed, steps and expected text |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$bug Guest Support escalated ticket 58213 to Booking. On Android the confirmation screen leaves city tax out of the total on stays of 2 nights or more, so the guest saw "Total €387.00" and was charged €405.00. The ticket with Maren's tests is in context/roamstay-support-ticket-58213.md and our product context is in context/roamstay-context.md`

### Commands

1. `sandbox: stage context/roamstay-context.md and context/roamstay-support-ticket-58213.md -> record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the new bug export -> operator: grade the field table, the amounts, the scope, the steps and the checklist against the ticket and Turn 2`

### Expected

Step 1 fixes the baseline with both attachments staged. Step 2 returns one evidence question and one clarification file. Step 3 proves the wait state and the question-only file. Step 4 finds `## About` with the field table reading Severity `High`, `**1. Observed Behavior**` with "Total €387.00" against the `€405.00` charge on booking `RS-7Q4K2M`, numbered steps from the 2-night test, `**2. Expected Behavior**` with the confirmation total matching the charge, city tax included, and the four Checklist items.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back lines, the field table values, every amount the bug states, the scope statements for 1 night, iOS, web and Pay at property, the steps and the checklist.

### Pass / fail

- **Pass**: One evidence question, no early draft, and one readable bug export under the `bug` word with every required section, the ticket's amounts intact and adding up, the charge kept correct, the Android confirmation total kept as the defect and the scope held to Android `8.12.1` Pay now stays of 2 nights or more
- **Fail**: The runtime drafts before Turn 2, calls the charge wrong or the guest overcharged, changes or miscomputes an amount, widens or narrows the scope the ticket sets, derives a frequency from the chat count, or invents a device, a cause or a step

### Failure triage

1. Check the explicit-command wait in `AGENTS.md` and the clarification export rules in `bug-mode.md`
2. Recompute every amount in the bug against the Back office breakdown and the agent's tests in `roamstay-support-ticket-58213.md`
3. Compare the field table with the Frequency and `Not provided` rules in `bug-report-template.md` and strike any cause or step the ticket never gave

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SBG-002 | Support ticket bug | Verify one evidence question, then a bug that keeps the support ticket's amounts, scope and charge-versus-display fact | `$bug Guest Support escalated ticket 58213 to Booking. On Android the confirmation screen leaves city tax out of the total on stays of 2 nights or more, so the guest saw "Total €387.00" and was charged €405.00. The ticket with Maren's tests is in context/roamstay-support-ticket-58213.md and our product context is in context/roamstay-context.md` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the bug export | Step 1: baseline known. Step 2: one evidence question. Step 3: question-only file and wait. Step 4: fixed structure, ticket amounts adding up, charge right and display wrong | Both replies, ledger, clarification and bug export paths, read-back lines and artifact excerpts | PASS if the question, the wait and a bug keeping every ticket value, the arithmetic and the scope all hold with no invented fact. FAIL otherwise | 1. Check the command wait. 2. Recompute the amounts. 3. Check the field table and strike any cause |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Clarification turns, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Explicit-command wait, the clarification deliverable and the read-back reply |
| [`SKILL.md`](../../SKILL.md) | Bug routing, export names and the clarification lane |
| [`bug-mode.md`](../../references/bug-mode.md) | Bug workflow, evidence rules, Frequency recovery and fixed structure |
| [`bug-report-template.md`](../../assets/bug-report-template.md) | Field table, Frequency rules and Checklist |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Clarification export contract |
| [`roamstay-context.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Attachment: surfaces, app versions, city tax and Pay now |
| [`roamstay-support-ticket-58213.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-support-ticket-58213.md) | Attachment: the chat, the Back office breakdown, the agent's tests and the escalation |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: SBG-002
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/support-ticket-bug.md`
