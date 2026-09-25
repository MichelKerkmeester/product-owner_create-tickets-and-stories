---
title: "PBG-003 -- Two-platform log bug"
description: "Validates that a bug command handing over a Loomlist log excerpt and support reports renders one evidence question as a clarification block, waits, then renders one bug block that keeps two platform issues as two observed and expected pairs, invents no root cause and claims no file."
version: 1.0.0.0
---

# PBG-003 -- Two-platform log bug

This scenario validates the `$b` path from a log excerpt and a set of user reports to one rendered Bug Deliverable Block that keeps two issues apart, through one evidence question.

---

## 1. OVERVIEW

The Loomlist support lead asks for one bug for the To-dos and Reminders team about reminders arriving an hour late after the March clock change. The two attachments describe two issues that do not look alike: on Android `5.2.3` one-off reminders set for 09:00 arrive at 10:00, and on iOS `5.2.4` daily reminders set for 07:30 arrive at 08:30 every day until the member edits the reminder and saves it. The log excerpt covers the Android case only and shows evidence, never a cause. An explicit `$b` still asks its context question and waits. Turn 2 gives a severity and says what nobody knows yet: device models, a QA reproduction and the state of the current 5.3 apps. The one bug block must keep two observed and expected pairs, carry the log lines as evidence and name no cause, and the Project claims no file at any point.

### Why this matters

Folding the two groups into "reminders are an hour late after the clock change" loses the reminder kind, the version and the edit-and-save workaround QA needs to reproduce each one. A guessed cause, or one cause given to both, points the team at a single fix for what the reports call two different problems, with the next clock change coming.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the single evidence question, the wait state and one bug block that keeps two platform issues as two observed and expected pairs with no invented cause
- Real user request: `Reminders came an hour late for a lot of people after the March clock change, on Android and on iOS. Can you write it up for the reminders team?`
- Prompt: `$b Reminders arrived an hour late after the March clock change, one-off reminders on Android and daily ones on iOS. Please write it up as one bug for the To-dos and Reminders team from Ruben's log lines in context/loomlist-reminders-dst-log-excerpt.md and Marta's support reports in context/loomlist-reminders-dst-user-reports.md, with our product context in context/loomlist-context.md`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-reminders-dst-log-excerpt.md](../../../benchmark/fixtures/companies/loomlist/loomlist-reminders-dst-log-excerpt.md), [loomlist-reminders-dst-user-reports.md](../../../benchmark/fixtures/companies/loomlist/loomlist-reminders-dst-user-reports.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and all three attachments sit at `context/` beside the Project
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the clarification block, answer in Turn 2 and inspect the rendered bug block
- Expected signals: Turn 1 asks one bug context question and drafts nothing, because an explicit `$b` still asks its mode's question and waits (`Custom Instructions.md` line 108, `Product Owner - Templates - Bug Mode` line 44). It renders the question alone as its own block (`Product Owner - Templates - Bug Mode` line 46), then `Export-equivalent path: export/[NNN] - bug-[description]-clarification.md` (`Custom Instructions.md` line 228) and the `HVR self-scan:` line (root section 5, Clarification turns), and claims no file. A question field the attachments already answer is recorded, not failed (root section 5, Ticket realism). Turn 2 renders one bug as its own block, a Canvas Artifact or, with no panel, one fenced block (`Custom Instructions.md` line 85), since Turn 1 asked for one report covering both (`Product Owner - Templates - Bug Mode` line 48), followed by `Export-equivalent path: export/[NNN] - bug-[description].md` (`Custom Instructions.md` lines 224 and 233) and the `HVR self-scan:` line, with no save or read-back claimed (`Custom Instructions.md` line 101). The bug follows the fixed order (`Product Owner - Templates - Bug Mode` lines 110 to 118) and keeps two issues, each with its own observed and expected statement, as labelled parts of the two fixed sections or as one pair per issue. The Android issue: Android `5.2.3`, one-off reminders set for `09:00` arrive at `10:00`, `64` tickets. Its evidence is the log for `rem_8f31c2` in `Europe/Amsterdam`, set before the change for 09:00 on the Monday after it with `tz_offset=+01:00` and `scheduled_utc=2026-03-30T08:00:00Z` and shown at 10:00 local, beside `rem_c41d07`, set after the change with `tz_offset=+02:00` and shown at 09:00. Expected: a one-off reminder arrives at the local time it was set for, whenever it was set. The iOS issue: iOS `5.2.4`, daily reminders set for `07:30` arrive at `08:30` every day, `53` tickets, until the member opens the reminder and saves it, after which it arrives at 07:30 from the next day. Expected: a daily reminder keeps arriving at its local time across the change with no edit. Both rest on `117` tickets tagged `reminder-late` between 2026-03-29 and 2026-04-05, all from zones whose clocks moved forward on 2026-03-29, sample tickets `LL-20931`, `LL-20944` and `LL-20958`, no reports of late iOS one-off or Android daily reminders, web and desktop reporting nothing because reminders there show in the app only, and the next change on 2026-10-25. Severity reads `High` from Turn 2. Device and OS Version read `Not provided` (`Product Owner - Templates - Bug Mode` line 236). Frequency carries only what the reports state and never a label read off the 117, 64 or 53 counts (`Product Owner - Templates - Bug Mode` line 240). Steps use only what the reports and the log show, with nothing presented as a QA reproduction (`Product Owner - Templates - Bug Mode` line 216). No cause is given for either issue and none for both, since the log's own notes call its lines the log lines and nothing more (`Custom Instructions.md` line 104), and `Root cause identified` stays open. Nothing is said about the current 5.3 apps or about what the October change will do. A title with no discipline code is recorded only (root section 5, Ticket realism)
- Desired user-visible outcome: One evidence question rendered as a clarification block, then one bug block for the To-dos and Reminders team under an export-equivalent label that keeps the Android and iOS issues apart and reads the log as evidence, with no file claimed
- Size band (advisory): 80 to 150 lines of artifact body
- Pass/fail: PASS if Turn 1 asks one question, renders it as its own question-only block with `Export-equivalent path:` under the `bug` word and the `-clarification` suffix and the `HVR self-scan:` line and drafts nothing, and Turn 2 renders one bug as its own block with `Export-equivalent path:` under the `bug` word and the `HVR self-scan:` line, claims no file on either turn, and the bug carries every required template section, Android `5.2.3` one-off reminders set for `09:00` arriving at `10:00` and iOS `5.2.4` daily reminders set for `07:30` arriving at `08:30` kept as two separate observed and expected pairs, the log evidence for the Android issue with `rem_8f31c2` and `Europe/Amsterdam`, the edit-and-save workaround for the iOS issue, every ticket ID, count, offset, UTC time and date it states exactly as the attachments give it, Severity `High`, no device model or OS version, and no root cause for either issue. FAIL if Turn 1 drafts, either turn claims a saved or verified file, the reply renders two bug blocks where Turn 1 asked for one, merges the two issues into one symptom or swaps a platform, version or reminder kind, states why either issue happens or gives both one cause, for example that reminders-service converts the time with the offset in force when the reminder was set, derives Frequency from the 117, 64 or 53 counts, says the 5.3 apps are affected or fixed, predicts what the October change will do, presents a step as a QA reproduction, attributes the log lines to iOS, or leaves a template slot unfilled
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$b Reminders arrived an hour late after the March clock change, one-off reminders on Android and daily ones on iOS. Please write it up as one bug for the To-dos and Reminders team from Ruben's log lines in context/loomlist-reminders-dst-log-excerpt.md and Marta's support reports in context/loomlist-reminders-dst-user-reports.md, with our product context in context/loomlist-context.md` | Read all three attachments, ask one bug context question, render it as a question-only clarification block with its export-equivalent label and the `HVR self-scan:` line, and claim no file. Create no bug draft | Bug Mode at Standard energy, one report requested, the Android and iOS issues held apart | Turn 1 reply, rendered clarification block, its label and the no-file-write statement |
| 2 | `Severity High for both. Support never collected device models or OS versions, so we have none. QA has not reproduced either one yet, and nobody has checked the current 5.3 apps because the clocks have not changed since March. No screenshots or recordings, and no other bug is open for it. Keep it as one report.` | Build one bug from the attachments and the answer, keep each issue's platform, version, reminder kind, set time and arrival time apart, carry the log lines as evidence, write `Not provided` where nothing was supplied, render it as one bug block and report its export-equivalent label and the `HVR self-scan:` line with no file claim | Two observed and expected pairs, no cause, nothing claimed about the 5.3 apps or the October change | Turn 2 reply, rendered bug block, its label and the field table, both observed and expected pairs, the log evidence and the steps |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$b Reminders arrived an hour late after the March clock change, one-off reminders on Android and daily ones on iOS. Please write it up as one bug for the To-dos and Reminders team from Ruben's log lines in context/loomlist-reminders-dst-log-excerpt.md and Marta's support reports in context/loomlist-reminders-dst-user-reports.md, with our product context in context/loomlist-context.md`

### Commands

1. `sandbox: stage context/loomlist-context.md, context/loomlist-reminders-dst-log-excerpt.md and context/loomlist-reminders-dst-user-reports.md -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered bug block -> operator: grade the two observed and expected pairs, the log evidence, the field table, the steps, the checklist and the label against the attachments and Turn 2`

### Expected

Step 1 fixes the panel baseline with the three attachments staged. Step 2 returns one evidence question as its own clarification block under its label. Step 3 proves the wait state. Step 4 finds one bug block with `### About`, the field table reading Severity `High` and `Not provided` for Device and OS Version, `**1. Observed Behavior**` and `**2. Expected Behavior**` covering the Android `5.2.3` one-off issue and the iOS `5.2.4` daily issue apart, the `rem_8f31c2` log lines as evidence and the four Checklist items with `Root cause identified` open.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the field table values, each issue's observed and expected text, every ticket ID, count, offset, UTC time and date the bug states, the steps and the checklist.

### Pass / fail

- **Pass**: One evidence question rendered as its own block under its label, no early draft, and one rendered bug block under an export-equivalent label with the `bug` word, every required section, the two issues kept as two observed and expected pairs with their own platform, version, reminder kind and times, the log lines carried as evidence, no cause stated and no file claim
- **Fail**: The runtime drafts before Turn 2, claims a local file, splits the report or merges the issues, swaps a platform, version or reminder kind, states a cause, derives a frequency from a count, claims anything about the 5.3 apps or the October change, or presents a step as a QA reproduction

### Failure triage

1. Check the explicit-command wait in `Custom Instructions.md` and the grouped-bug rule in `Product Owner - Templates - Bug Mode`
2. Compare each issue's platform, version, reminder kind and times with the two groups in `loomlist-reminders-dst-user-reports.md`, and each log value with `loomlist-reminders-dst-log-excerpt.md`
3. Strike any cause, prediction or reproduction claim the attachments and Turn 2 never gave, and check the field table against the Frequency and `Not provided` rules in `Product Owner - Assets - Bug Report Template`

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PBG-003 | Two-platform log bug | Verify one evidence question, then one bug block keeping two platform issues apart with the log as evidence and no invented cause | `$b Reminders arrived an hour late after the March clock change, one-off reminders on Android and daily ones on iOS. Please write it up as one bug for the To-dos and Reminders team from Ruben's log lines in context/loomlist-reminders-dst-log-excerpt.md and Marta's support reports in context/loomlist-reminders-dst-user-reports.md, with our product context in context/loomlist-context.md` | 1. Stage and panel baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the bug block | Step 1: baseline known. Step 2: one evidence question block. Step 3: wait state. Step 4: one bug block, two observed and expected pairs, log as evidence, no cause, label present | Both replies, rendered blocks, labels and artifact excerpts | PASS if the question, the wait and one bug block keeping both issues apart with every attachment value intact, no invented cause and no file claim all hold. FAIL otherwise | 1. Check the command wait. 2. Check each issue against its group and the log. 3. Strike any cause or prediction |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Clarification turns, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, the explicit-command wait, the root cause rule, the Deliverable Block and the export-equivalent contract |
| [`Product Owner - Templates - Bug Mode - v0.203.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Bug%20Mode%20-%20v0.203.md) | Project bug workflow, the grouped-bug rule, evidence placement, Frequency recovery and fixed structure |
| [`Product Owner - Assets - Bug Report Template - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Bug%20Report%20Template%20-%20v0.100.md) | Field table, Frequency rules and Checklist |
| [`Product Owner - System - Interactive Mode - v0.405.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode%20-%20v0.405.md) | Clarification delivery contract |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Attachment: platforms, app versions, how reminders reach each platform and the owning team |
| [`loomlist-reminders-dst-log-excerpt.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-reminders-dst-log-excerpt.md) | Attachment: the Android log lines for two reminders either side of the change |
| [`loomlist-reminders-dst-user-reports.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-reminders-dst-user-reports.md) | Attachment: the two report groups, sample tickets, the workaround and the next change |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PBG-003
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/two-platform-log-bug.md`
