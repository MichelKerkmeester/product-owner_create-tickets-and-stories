claude project/PDK-002 - 002 - doc-payment-webhook-failures-runbook.md | 70 (and 18) | 68 (and 18) | Dropped | "The payment provider's retries alone would leave most bookings waiting hours for the next attempt." and "so bookings don't have to wait for the next retry" (the only reason given for running psp-replay; cut line 16 keeps "so guests can wait hours" under retries, but nothing ties that wait to the replay step any more. Borderline: a reader can still infer it)
claude project/PST-004 - NNN - Story-order-tracking-timeline/NNN - Story-order-tracking-timeline.md | 163 | 161 | Changed | "**Given** an order delivered longer ago than the tracking retention period" (cut reads "delivered before the tracking retention period", which no longer says the delivery is older than the 90 days; requirement line 68 still states the 90-day rule)
claude project/PST-004 - NNN - Story-order-tracking-timeline/NNN - Story-order-tracking-timeline (turn 2).md | 150 | 148 | Changed | "**Given** an order delivered longer ago than the tracking retention period" (same rewrite as the turn 1 copy, "delivered before the tracking retention period")
skill/SBG-003 - 002 - bug-reminders-late-after-clock-change.md | 62 | 62 | Changed | "on Android 5.2.3 with profile time zone Europe/Amsterdam" (cut says "in Europe/Amsterdam", which a tester can read as device location or device clock rather than the profile time zone setting the reminder uses)
skill/SBG-003 - 002 - bug-reminders-late-after-clock-change.md | 69 | 69 | Changed | "with a profile time zone whose clocks move forward" (cut says "in a zone whose clocks move forward", same loss of the profile setting as the repro condition)
skill/SID-001 - 002 - task-due-today-filter-chip.md | 19 | 19 | Added | "There is no Figma file for this change." (cut adds a cause the snapshot never gave: "There is no Figma file, because the chip reuses the existing component.")
skill/STK-005 - 001 - task-android-recurring-todos-subtask.md | 87 | 83 | Changed | "Checking it off brings the next one onto the same page, so the member never has to recreate the to-do." (cut gives the reason as "Only one occurrence exists at a time, so nobody recreates the to-do", which swaps the reason for a non-sequitur; checklist line 87 still carries the check-off behavior)

Files read: 17 (each snapshot and its cut copy). Problems found: 7, in 5 files.

Files with no problems: PST-004 NNN.1 task-ios-tracking-timeline, NNN.1 task-tracking-webhook, NNN.2 task-android-tracking-timeline, NNN.2 task-packed-status, NNN.3 task-web-tracking-timeline, NNN.3 task-web-tracking-timeline (turn 2), NNN.4 task-ios-tracking-timeline, NNN.4 task-tracking-webhook, NNN.5 task-android-tracking-timeline, NNN.6 task-tracking-timeline-events, SBG-001.

## Verdicts on the cuts the writer flagged

- PDK-002, closing "This document is written for the runbook follow-up, which stays Open until it's linked from the Payments / Webhooks dashboard.": Fine. The table row "Webhook failures runbook, linked from the Payments / Webhooks dashboard | Karim | Open" still carries the action, its owner, its Open status and the link as its done condition, and the title names this document as that runbook.
- PDK-002, three-gap Review follow-ups list cut to the unalerted 19 minutes: Fine. The other two gaps still stand as facts in the cut: the rotation order in step 3 line 55 and Boundaries line 100, and the hand-paused expiry job in step 2 line 41. Only the attribution of those two to the review is gone, and the agreed actions table is intact.
- PDK-002, "nothing watched that rate before it was added": Fine. "added on 2026-09-10" (line 22) and "nothing alerted until Guest Support noticed 19 minutes in" (line 104) carry it.
- PDK-002, "instead of waiting for retries" (snapshot lines 18 and 70): Dropped, entered above as borderline. Line 16 keeps the hours-long wait, but the replay step no longer says why it runs.
- PST-004 Story, Solution dropped "The tracking number stays in the shipping email for customers who still prefer the carrier's page": Fine. Order page rules line 70 (turn 2: line 64) keeps "The shipping email keeps the tracking number"; the "who still prefer" clause is color.
- PST-004 NNN.1 and NNN.4 tracking webhook, dropped "Five failed attempts mean the event is gone for good" / "After five failed retries, the event is gone for good": Fine. About line 7 keeps "The carrier drops an event for good after its last retry", and the parent Story keeps the `5 attempts` and schedule.
- STK-005, merged "At the limit" items: Fine. Both conditions (Repeat stays visible, opens the sheet with the exact text) survive in line 116.
- STK-005, Custom interval intro cut: Fine, the checklist carries days, weeks or months and N.
- STK-005, Skip intro cut: Fine, the checklist carries no-done, next BE due date and the After-limit count with "never a free extra".
- STK-005, Ends intro cut: Fine, "Never is the default, so a series runs until the member ends it" carries it.
- STK-005, Owner's time zone intro cut: Fine, "from its next occurrence" is carried by checklist line 143.
- SBG-003, 09:00 moved between the LL-20931 bullets: Fine. Line 47 ties "set for 09:00 arrives at 10:00" to LL-20931 and line 48 keeps Friday 2026-03-27 for Monday and the missed call.
- SBG-003, reworded Design spec time zone bullet: Fine. "the member picks a local date and time in the owner's profile time zone" plus the main Expected line 103 keep that reminders run in the to-do owner's profile time zone.
- SID-001, chip order now implies "right after Overdue": Fine. "All, Assigned to me, Overdue, Due today" puts Due today directly after Overdue.
- SBG-001, dropped Observed bullet "Android 4.8.2 and web show the new count on the badge as soon as the item is removed": Fine. About line 7 keeps "Android 4.8.2 and web update at once" and Expected line 56 names both again.

## Turn copies

- PST-004 Story and Story (turn 2): the cut copies differ in exactly the places the snapshots differ (Tasks list, web layout open question versus shared frame, Packed source, Delivery failed reason, Analytics, AC4 "with no reason", Rabbit holes, No-gos). Every sentence the snapshots shared is worded identically in both cut copies, including the AC7 rewrite flagged above.
- PST-004 NNN.3 web task and NNN.3 (turn 2): the cut copies differ only where the snapshots differ (About second sentence, Related tasks, the `Delivery failed` no-reason item, Analytics). All shared checklist lines are worded identically.
