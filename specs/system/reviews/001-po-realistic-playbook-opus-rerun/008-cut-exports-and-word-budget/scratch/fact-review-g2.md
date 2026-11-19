claude project/PTK-002 - 001 - task-date-picker-stay-limits.md | 8 | 8 | Dropped | "Guest Support logged 23 chats about it in August, mostly about long stays for work."
claude project/PTK-002 - 001 - task-date-picker-stay-limits.md | 10 | 10 | Dropped | "date selection isn't tracked today"
claude project/PTK-002 - 001 - task-date-picker-stay-limits.md | 10 | 10 | Dropped | "raise any mismatch with Ines in the Search squad channel before working around it"
claude project/PTK-002 - 001 - task-date-picker-stay-limits (turn 2).md | 8 | 8 | Dropped | "Guest Support logged 23 chats about it in August, mostly about long stays for work."
claude project/PTK-002 - 001 - task-date-picker-stay-limits (turn 2).md | 12 | 10 | Dropped | "`search-service` doesn't change"
claude project/PTK-002 - 001 - task-date-picker-stay-limits (turn 2).md | 12 | 10 | Dropped | "Date selection isn't tracked today, and this work adds no events."
claude project/PTK-002 - 001 - task-date-picker-stay-limits (turn 2).md | 14 | 10 | Dropped | "If the build doesn't match the file, raise it with Ines in the Search squad channel before working around it."
skill/STK-002 - 001 - task-date-picker-stay-limits.md | 7 | 7 | Dropped | "Guest Support logged 23 chats about it in August, mostly from guests booking long work stays."
skill/STK-002 - 001 - task-date-picker-stay-limits.md | 11 | 9 | Dropped | "Date selection isn't tracked today and this task adds no events."
skill/STK-002 - 001 - task-date-picker-stay-limits.md | 11 | 7 | Dropped | "search-service stays as it is, because its own 30-night check remains the backstop behind the picker."
skill/STK-002 - 001 - task-date-picker-stay-limits.md | 9 | 9 | Dropped | "If the build can't match the frame, raise it with Ines in the Search squad channel before working around it."
claude project/PTK-004 - NNN - task-recurring-todos.md | 7 | 7 | Dropped | "Today people copy a to-do by hand every week, or set a reminder far ahead and keep moving it."
claude project/PTK-004 - NNN - task-recurring-todos.md | 7 | 7 | Dropped | "38 Plus workspaces named it in the renewal survey as the reason they keep a second app for chores and routines"
claude project/PTK-004 - NNN - task-recurring-todos (turn 2).md | 7 | 7 | Dropped | "Today people copy a to-do by hand every week, or set a reminder far ahead and keep moving it."
claude project/PTK-004 - NNN - task-recurring-todos (turn 2).md | 7 | 7 | Dropped | "38 Plus workspaces named it in the renewal survey as the reason they keep a second app for chores and routines"
claude project/PTK-004 - NNN - task-recurring-todos (turn 2).md | 9 | 9 | Dropped | "The iOS, Android, Web and BE leads each write their own subtask from it and point at the numbered rules below instead of restating them."
claude project/PTK-004 - NNN - task-recurring-todos (turn 2).md | 11 | 157 | Dropped | "Web and BE ship dark before that, so both are in place when the apps land."
claude project/PTK-004 - NNN - task-recurring-todos-ios.md | 73 | after 67 | Dropped | "Today they get the same result by moving a reminder forward by hand."
claude project/PTK-004 - NNN - task-recurring-todos-android.md | 74 | after 68 | Dropped | "Today they get the same result by moving a reminder forward by hand."
claude project/PTK-004 - NNN - task-recurring-todos-web.md | 75 | after 69 | Dropped | "Today they get the same result by moving a reminder forward by hand."
skill/SDK-002 - 002 - doc-payment-webhook-failures-runbook.md | 110 | 108 | Changed | "this runbook refunds charged guests through psp-reconcile but does not restore an expired booking" (cut: "nothing restores the booking", a limit of this runbook became a claim that no route exists)

Files read: 13. Problems found: 21, in 9 files.

Files with no problems: `claude project/PTK-001 - NNN - task-free-shipping-banner-copy.md`, `claude project/PTK-004 - NNN - task-recurring-todos-be.md`, `claude project/PTK-006 - 002 - task-booking-funnel-event-checks.md`, `skill/SIR-002 - 002 - Story-wishlist-saved-to-account-in-apps.md`.

## Source check for the PTK-002 and STK-002 drops

The fixture `Product Owner/benchmark/fixtures/companies/roamstay/roamstay-date-picker-design-notes.md` supplies three of the dropped facts: line 11 "mostly long stays for work", line 68 "Date selection isn't tracked today" and line 7 "tell me in the Search squad channel before you work around it". "`search-service` doesn't change" is not in the fixture. The model inferred it, but it is still the only statement in scope that the backend is untouched. "keeps its 30-night backstop" says one check stays. It does not say the service is unchanged.

## Verdicts on the cuts the writer flagged

- PTK-002 (both turns) and STK-002, "mostly about long stays for work": Dropped. It says who hits the limit, it was supplied in the design notes and nothing else in the cut files says it.
- PTK-002 (both turns) and STK-002, "date selection isn't tracked today": Dropped. It is today's state and was supplied. "no events added" keeps the scope decision but loses the state.
- PTK-002 and STK-002, "because only check-in is limited": Fine. The rule stays in the adjacent lines ("Days more than 365 days ahead show but are disabled as check-in" / "Check-out may land more than 365 days ahead", PTK cut lines 47 and 48; STK cut lines 41 and 42). "Only check-in is limited" restates those two lines. It does not add a separate reason.
- PTK-004 turn 2, Web and BE subtask lines losing "Ships dark before iOS and Android 5.4.0": Fine. The same file keeps it at cut line 157: "Web and BE ship with `recurring_todos` off before iOS 5.4.0 and Android 5.4.0, which also ship with it off". The separate reason from snapshot line 11 ("so both are in place when the apps land") did go, and it is listed above.
- SDK-002 Overview losing the `payment_pending` consequence: Fine. Cut line 17 keeps it: "a rejection keeps it in `payment_pending`, even when charged. After 30 minutes booking-service expires it and resells the room".
- PTK-006, "The move finishes while `checkout_complete` still fires beside `booking_confirmed`": Fine. The ordering survives at cut lines 69, 79 and 81 ("The move is live before 2026-11-01", "`events-collector` accepts `checkout_complete` until 2026-11-01", "The drop goes live only after the funnel dashboard reads `booking_confirmed`"). Line 81 also carries the reason from snapshot line 78, "so dashboards can move over".
- PTK-006, "so no clean funnel can be drawn": Fine. It sums up the three defects that cut line 7 still lists (lost, doubled, mixed amount units and date formats). It gives no reason of its own.
- PTK-001, "Only the copy changes": Fine. Cut line 27 keeps it: "Keep the €50 and £45 thresholds and the banner's position and styling unchanged".
- SIR-002 criterion 3, "without an account" to "as a guest": Fine. The cut file defines guests at line 30 ("Guests keep the device wishlist, so it works without signing in"). The snapshot already used "Guests" in the same sense (snapshot line 32). The criterion's customer has an account at sign-in, so "as a guest" is if anything more exact.

## PTK-004 turn 1 and turn 2 shared wording

All sentences worded the same in both snapshots are also worded the same in both cut files, with one exception. Snapshot line 139 (turn 1) and line 155 (turn 2) both end "Data turns the flag on for a sample of Plus and Team workspaces once all three clients are out, then widens it from there." The cut has "Data widens it from the first sample." (turn 1, line 139) and "Data widens the flag after the first sample." (turn 2, line 153). This is a wording difference, not a fact difference. The sample condition stays in both rollout checklists, and those lines match (turn 1 line 144, turn 2 line 158). The Yara sentence was different in the two snapshots (lines 153 and 170) and is removed from both cut files. Both cut files keep the matching checklist line "Yara has reviewed the tracking plan with both events before iOS, Android or Web work starts".

## Judgment calls left as fine

- PTK-006 snapshot line 27, "Client events ship on iOS, Android and web together": "together" is gone at cut line 27. The checks on all three platforms remain, so I judged this fine. If simultaneous shipping matters to Nadia's timing, restore it.
- STK-002 snapshot line 37, "These limits apply everywhere the date picker opens": this is implied by cut line 53 ("on top of group 1, on the property page only"). I judged it fine.
- PTK-004 BE snapshot line 7, "The clients set the repeat and show the result": the BE file no longer states where its boundary sits. The client subtasks still do, and cut line 75 keeps "so the clients show the limit sheet".
