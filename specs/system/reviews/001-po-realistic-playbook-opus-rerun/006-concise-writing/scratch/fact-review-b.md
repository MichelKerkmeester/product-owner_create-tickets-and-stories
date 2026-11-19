claude project/PBG-003 - 001 - bug-reminders-late-after-march-clock-change-clarification.md | 6 | 6 | Changed | "a reminder set before 2026-03-29 for 09:00 on a date after it arrived at 10:00" (now "on a later date": the condition that the reminder date falls after the clock change is loosened to any later date; only the backticked `scheduled_utc=2026-03-30T08:00:00Z` on after line 7 still implies it. Borderline.)

Files read: 22 listed; 20 had a diff and every changed hunk was read; 2 had no diff.
Problems found: 1 (borderline).

## Per file

- PBG-001 bug-ios-cart-badge-stale-after-remove: no problems.
- PBG-002 bug-android-confirmation-total-missing-city-tax (turn 2): no problems.
- PBG-002 bug-android-confirmation-total-missing-city-tax: no problems.
- PBG-003 001 bug-reminders-late-after-march-clock-change-clarification: 1 problem, listed above.
- PBG-003 002 bug-reminders-late-after-march-clock-change: no problems. Step 2 was reworded the same way ("for a date after the change" became "for a later date", after line 62), but the condition is kept on after line 63 ("Wait for the reminder date after the change") and after line 100 ("for a date after it").
- PID-001 001 task-due-today-filter-chip-clarification: no problems.
- PID-001 002 task-due-today-filter-chip: no problems.
- PTK-001 task-free-shipping-banner-copy: no problems.
- PTK-002 task-date-picker-stay-limits (turn 2): no problems.
- PTK-002 task-date-picker-stay-limits: no problems. The dropped clause "where the picker also applies the property's minimum stay" is kept on after line 53 ("On the property page, a stay is also at least the property's minimum stay").
- PTK-003 task-label-webhook-duplicates-and-late-labels (turn 2): no problems. Every sentence of the split paragraphs is present.
- PTK-003 task-label-webhook-duplicates-and-late-labels: no problems.
- PTK-004 task-recurring-todos (turn 2): no problems. The dropped "Desktop gets the feature through the web client, so it has no subtask of its own" is kept on after line 59 ("Desktop gets it through the web client, with no Desktop release") and by the subtask list naming only iOS, Android, Web and BE.
- PTK-004 task-recurring-todos-android: no problems.
- PTK-004 task-recurring-todos-be: no diff.
- PTK-004 task-recurring-todos-ios: no diff.
- PTK-004 task-recurring-todos-web: no problems.
- PTK-004 task-recurring-todos: no problems.
- PTK-005 task-android-recurring-todos (turn 2): no problems.
- PTK-005 task-android-recurring-todos: no problems.
- PTK-006 001 task-booking-funnel-events-clarification: no problems.
- PTK-006 002 task-booking-funnel-event-checks: no problems. The dropped duty list ("check each event in `events-collector` as it ships, move the funnel dashboard to `booking_confirmed` and have the collector drop `checkout_complete` on its removal date, 2026-11-01") is kept as requirement headings on after lines 23, 59 and 74. The loosened "counted twice when reopened from Trips" is kept in full on after line 53 ("including when the guest reopens the confirmation from Trips").
