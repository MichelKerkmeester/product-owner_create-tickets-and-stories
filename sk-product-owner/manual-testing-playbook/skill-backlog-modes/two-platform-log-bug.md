---
title: "SBG-003 -- Two-platform log bug"
description: "Validates that a bug command handing over a Loomlist log excerpt and support reports asks one evidence question, waits, then saves one bug that keeps two platform issues as two observed and expected pairs and invents no root cause."
version: 1.1.0.0
---

# SBG-003 -- Two-platform log bug

This scenario validates the `$b` path from a log excerpt and a set of user reports to one saved bug report that keeps two issues apart, through one evidence question.

---

## 1. OVERVIEW

The Loomlist support lead asks for one bug for the To-dos and Reminders team about reminders arriving an hour late after the March clock change. The two attachments describe two issues that do not look alike: on Android `5.2.3` one-off reminders set for 09:00 arrive at 10:00, and on iOS `5.2.4` daily reminders set for 07:30 arrive at 08:30 every day until the member edits the reminder and saves it. The log excerpt covers the Android case only and shows evidence, never a cause. An explicit `$b` still asks its context question and waits. Turn 2 gives a severity and says what nobody knows yet: device models, a QA reproduction and the state of the current 5.3 apps. The one bug must keep two observed and expected pairs, carry the log lines as evidence and name no cause.

### Why this matters

Folding the two groups into "reminders are an hour late after the clock change" loses the reminder kind, the version and the edit-and-save workaround QA needs to reproduce each one. A guessed cause, or one cause given to both, points the team at a single fix for what the reports call two different problems, with the next clock change coming.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the single evidence question, the wait state and one bug that keeps two platform issues as two observed and expected pairs with no invented cause
- Real user request: `Reminders came an hour late for a lot of people after the March clock change, on Android and on iOS. Can you write it up for the reminders team?`
- Prompt: `$b Reminders arrived an hour late after the March clock change, one-off reminders on Android and daily ones on iOS. Please write it up as one bug for the To-dos and Reminders team from Ruben's log lines in context/loomlist-reminders-dst-log-excerpt.md and Marta's support reports in context/loomlist-reminders-dst-user-reports.md, with our product context in context/loomlist-context.md`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-reminders-dst-log-excerpt.md](../../../benchmark/fixtures/companies/loomlist/loomlist-reminders-dst-log-excerpt.md), [loomlist-reminders-dst-user-reports.md](../../../benchmark/fixtures/companies/loomlist/loomlist-reminders-dst-user-reports.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and all three attachments sit at `context/` in the sandbox
- Expected execution process: Start fresh, submit Turn 1, capture the evidence question and its clarification export, answer in Turn 2 and inspect the next bug export
- Expected signals: Turn 1 asks one bug context question and drafts nothing, because an explicit `$b` still asks its mode's question and waits (`AGENTS.md` line 287, `references/bug-mode.md` line 61). It saves the question alone as `export/[###] - bug-[description]-clarification.md` (`SKILL.md` line 208, `references/bug-mode.md` line 63), reads it back and replies with its path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (root section 5, Clarification turns). A question field the attachments already answer is recorded, not failed (root section 5, Ticket realism). Turn 2 saves one bug on the next number as `export/[###] - bug-[description].md` (`SKILL.md` line 207), since Turn 1 asked for one report covering both (`references/bug-mode.md` line 65), reads it back and replies with its path and both lines. The bug follows the fixed order (`references/bug-mode.md` lines 127 to 135) and keeps two issues, each with its own observed and expected statement, as labelled parts of the two fixed sections or as one pair per issue. The Android issue: Android `5.2.3`, one-off reminders set for `09:00` arrive at `10:00`, `64` tickets. Its evidence is the log for `rem_8f31c2` in `Europe/Amsterdam`, set before the change for 09:00 on the Monday after it with `tz_offset=+01:00` and `scheduled_utc=2026-03-30T08:00:00Z` and shown at 10:00 local, beside `rem_c41d07`, set after the change with `tz_offset=+02:00` and shown at 09:00. Expected: a one-off reminder arrives at the local time it was set for, whenever it was set. The iOS issue: iOS `5.2.4`, daily reminders set for `07:30` arrive at `08:30` every day, `53` tickets, until the member opens the reminder and saves it, after which it arrives at 07:30 from the next day. Expected: a daily reminder keeps arriving at its local time across the change with no edit. Both rest on `117` tickets tagged `reminder-late` between 2026-03-29 and 2026-04-05, all from zones whose clocks moved forward on 2026-03-29, sample tickets `LL-20931`, `LL-20944` and `LL-20958`, no reports of late iOS one-off or Android daily reminders, web and desktop reporting nothing because reminders there show in the app only, and the next change on 2026-10-25. Severity reads `High` from Turn 2. Device and OS Version read `Not provided` (`references/bug-mode.md` line 253). Frequency carries only what the reports state and never a label read off the 117, 64 or 53 counts (`references/bug-mode.md` line 257). Steps use only what the reports and the log show, with nothing presented as a QA reproduction (`references/bug-mode.md` line 233). No cause is stated as fact for either issue and no one cause is given to both, since the log's own notes call its lines the log lines and nothing more (`SKILL.md` line 283, `AGENTS.md` line 16), and `Root cause identified` stays open. A cause the artifact labels as an unverified hypothesis is allowed (root section 5, Defect severity). Nothing is said about the current 5.3 apps or about what the October change will do. A title with no discipline code is recorded only (root section 5, Ticket realism)
- Desired user-visible outcome: One evidence question saved as a clarification, then one bug export for the To-dos and Reminders team that keeps the Android and iOS issues apart and reads the log as evidence
- Size band (advisory): 80 to 150 lines of artifact body
- Pass/fail: PASS if Turn 1 asks one question, saves it as a question-only clarification under the `bug` word with its path, `Verified:` and `HVR self-scan:` lines and drafts nothing, and Turn 2 saves one bug under the `bug` word on the next number, read back, with every required template section, Android `5.2.3` one-off reminders set for `09:00` arriving at `10:00` and iOS `5.2.4` daily reminders set for `07:30` arriving at `08:30` kept as two separate observed and expected pairs, the log evidence for the Android issue with `rem_8f31c2` and `Europe/Amsterdam`, the edit-and-save workaround for the iOS issue, every ticket ID, count, offset, UTC time and date it states exactly as the attachments give it, Severity `High`, no device model or OS version, and no root cause stated as fact for either issue, where a cause the artifact labels as an unverified hypothesis is allowed (root section 5, Defect severity). FAIL if Turn 1 drafts, the bug saves two files where Turn 1 asked for one, merges the two issues into one symptom or swaps a platform, version or reminder kind, states as fact why either issue happens or gives both one cause, for example that reminders-service converts the time with the offset in force when the reminder was set, derives Frequency from the 117, 64 or 53 counts, says the 5.3 apps are affected or fixed, predicts what the October change will do, presents a step as a QA reproduction, attributes the log lines to iOS, or leaves a template slot unfilled
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$b Reminders arrived an hour late after the March clock change, one-off reminders on Android and daily ones on iOS. Please write it up as one bug for the To-dos and Reminders team from Ruben's log lines in context/loomlist-reminders-dst-log-excerpt.md and Marta's support reports in context/loomlist-reminders-dst-user-reports.md, with our product context in context/loomlist-context.md` | Read all three attachments, ask one bug context question, save it as a question-only clarification, read it back and reply with its path, the `Verified:` line and the `HVR self-scan:` line. Create no bug draft | Bug Mode at Standard energy, one report requested, the Android and iOS issues held apart | Turn 1 reply, clarification export, read-back result and a ledger holding no draft |
| 2 | `Severity High for both. Support never collected device models or OS versions, so we have none. QA has not reproduced either one yet, and nobody has checked the current 5.3 apps because the clocks have not changed since March. No screenshots or recordings, and no other bug is open for it. Keep it as one report.` | Build one bug from the attachments and the answer, keep each issue's platform, version, reminder kind, set time and arrival time apart, carry the log lines as evidence, write `Not provided` where nothing was supplied, save it on the next number, read it back and reply with its path and both lines | Two observed and expected pairs, no cause, nothing claimed about the 5.3 apps or the October change | Turn 2 reply, bug export, read-back result and the field table, both observed and expected pairs, the log evidence and the steps |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$b Reminders arrived an hour late after the March clock change, one-off reminders on Android and daily ones on iOS. Please write it up as one bug for the To-dos and Reminders team from Ruben's log lines in context/loomlist-reminders-dst-log-excerpt.md and Marta's support reports in context/loomlist-reminders-dst-user-reports.md, with our product context in context/loomlist-context.md`

### Commands

1. `sandbox: stage context/loomlist-context.md, context/loomlist-reminders-dst-log-excerpt.md and context/loomlist-reminders-dst-user-reports.md -> record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the new bug export -> operator: grade the two observed and expected pairs, the log evidence, the field table, the steps and the checklist against the attachments and Turn 2`

### Expected

Step 1 fixes the baseline with the three attachments staged. Step 2 returns one evidence question and one clarification file. Step 3 proves the wait state and the question-only file. Step 4 finds one bug with `## About`, the field table reading Severity `High` and `Not provided` for Device and OS Version, `**1. Observed Behavior**` and `**2. Expected Behavior**` covering the Android `5.2.3` one-off issue and the iOS `5.2.4` daily issue apart, the `rem_8f31c2` log lines as evidence and the four Checklist items with `Root cause identified` open.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back lines, the field table values, each issue's observed and expected text, every ticket ID, count, offset, UTC time and date the bug states, the steps and the checklist.

### Pass / fail

- **Pass**: One evidence question, no early draft, and one readable bug export under the `bug` word with every required section, the two issues kept as two observed and expected pairs with their own platform, version, reminder kind and times, the log lines carried as evidence and no cause stated as fact
- **Fail**: The runtime drafts before Turn 2, splits the report or merges the issues, swaps a platform, version or reminder kind, states a cause as fact, derives a frequency from a count, claims anything about the 5.3 apps or the October change, or presents a step as a QA reproduction

### Failure triage

1. Check the explicit-command wait in `AGENTS.md` and the grouped-bug rule in `bug-mode.md`
2. Compare each issue's platform, version, reminder kind and times with the two groups in `loomlist-reminders-dst-user-reports.md`, and each log value with `loomlist-reminders-dst-log-excerpt.md`
3. Strike any cause, prediction or reproduction claim the attachments and Turn 2 never gave, and check the field table against the Frequency and `Not provided` rules in `bug-report-template.md`

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SBG-003 | Two-platform log bug | Verify one evidence question, then one bug keeping two platform issues apart with the log as evidence and no invented cause | `$b Reminders arrived an hour late after the March clock change, one-off reminders on Android and daily ones on iOS. Please write it up as one bug for the To-dos and Reminders team from Ruben's log lines in context/loomlist-reminders-dst-log-excerpt.md and Marta's support reports in context/loomlist-reminders-dst-user-reports.md, with our product context in context/loomlist-context.md` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the bug export | Step 1: baseline known. Step 2: one evidence question. Step 3: question-only file and wait. Step 4: one bug, two observed and expected pairs, log as evidence, no cause stated as fact | Both replies, ledger, clarification and bug export paths, read-back lines and artifact excerpts | PASS if the question, the wait and one bug keeping both issues apart with every attachment value intact and no invented cause all hold. FAIL otherwise | 1. Check the command wait. 2. Check each issue against its group and the log. 3. Strike any cause stated as fact and any prediction |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Clarification turns, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Explicit-command wait, the ban on fabricated root causes and the read-back reply |
| [`SKILL.md`](../../SKILL.md) | Bug routing, export names, the clarification lane and the root cause rule |
| [`bug-mode.md`](../../references/bug-mode.md) | Bug workflow, the grouped-bug rule, evidence placement, Frequency recovery and fixed structure |
| [`bug-report-template.md`](../../assets/bug-report-template.md) | Field table, Frequency rules and Checklist |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Clarification export contract |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Attachment: platforms, app versions, how reminders reach each platform and the owning team |
| [`loomlist-reminders-dst-log-excerpt.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-reminders-dst-log-excerpt.md) | Attachment: the Android log lines for two reminders either side of the change |
| [`loomlist-reminders-dst-user-reports.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-reminders-dst-user-reports.md) | Attachment: the two report groups, sample tickets, the workaround and the next change |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: SBG-003
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/two-platform-log-bug.md`
