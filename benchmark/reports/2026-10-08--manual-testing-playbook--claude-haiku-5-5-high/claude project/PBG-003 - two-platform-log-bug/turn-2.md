````markdown
# BE - REM - Reminders fire an hour late after a clock change

## About

Reminders on Android and iOS fire one hour after the local time the member set, when they were set before the clocks moved forward on 2026-03-29. Support tagged 117 tickets between 2026-03-29 and 2026-04-05, all from time zones that moved forward that day.

| Field | Value |
| --- | --- |
| Frequency | Not provided |
| Severity | High |
| Platform | Android and iOS |
| Device | Not provided |
| OS Version | Not provided |

---

### Bug

---

**1. Observed Behavior**

---

Reminders fire an hour late when they were set before the clock change. Two patterns are reported:
- Android one-off reminder, app 5.2.3: set for 09:00 on Monday 2026-03-30 in Europe/Amsterdam, it appears at 10:00 local.
- iOS daily reminder, app 5.2.4: set for 07:30, it appears at 08:30 every day from Sunday 2026-03-29 until the member edits and saves the reminder.
- Support tagged 64 Android one-off tickets and 53 iOS daily tickets, including LL-20931, LL-20944 and LL-20958.
- Error message: Not provided.
- Unconfirmed: the log lines fit a scheduled UTC time fixed when the reminder was created, under the offset in force then.

Log lines from LL-20931, with member and device IDs removed. The first reminder was created before the change and the second after it:

```text
2026-03-27T16:41:09.214Z INFO reminders-service reminder.created reminder_id=rem_8f31c2 kind=one_off tz=Europe/Amsterdam local_date=2026-03-30 local_time=09:00 tz_offset=+01:00 scheduled_utc=2026-03-30T08:00:00Z platform=android app_version=5.2.3
2026-03-30T08:00:02.870Z INFO reminders-service reminder.shown reminder_id=rem_8f31c2 platform=android app_version=5.2.3 device_local=2026-03-30T10:00:02+02:00
2026-03-30T08:07:52.563Z INFO reminders-service reminder.created reminder_id=rem_c41d07 kind=one_off tz=Europe/Amsterdam local_date=2026-03-31 local_time=09:00 tz_offset=+02:00 scheduled_utc=2026-03-31T07:00:00Z platform=android app_version=5.2.3
2026-03-31T07:00:01.954Z INFO reminders-service reminder.shown reminder_id=rem_c41d07 platform=android app_version=5.2.3 device_local=2026-03-31T09:00:01+02:00
```

No iOS log lines are attached.

- Current builds are not checked. Android 5.3.0 and iOS 5.3.2 have not been tested, because the clocks have not changed since March.
- QA has not reproduced either pattern.
- Screen recording: Not provided. No screenshots are attached.

Steps to Reproduce:

QA has not reproduced this yet. The steps come from LL-20931 and LL-20944.

1. On Android 5.2.3 with the time zone Europe/Amsterdam, create a one-off reminder for 09:00 before a clock change, for a time after it.
2. Let the clocks move forward one hour.
3. Wait for the reminder's date. Expected: the reminder appears at 09:00 local. Actual: it appears at 10:00 local.
4. On iOS 5.2.4 in a time zone that moved forward, create a daily reminder for 07:30 before the clock change.
5. Let the clocks move forward one hour, then wait for the next morning. Expected: the reminder appears at 07:30 local. Actual: it appears at 08:30 local.

---

**2. Expected Behavior**

---

Each reminder appears at the local time the member set, on the day set, after the clocks move forward.
- Android one-off reminder appears at 09:00 local on the set day.
- iOS daily reminder appears at 07:30 local every day.
- Previous working behavior: reminders set after the change arrived on time in the cases support checked.
- Members expect the reminder at the time they set. One member missed a call because the reminder arrived an hour late.

Checklist
- [] Root cause identified
- [] Fix implemented
- [] Bug no longer reproducible
- [] No regressions introduced
````

Export-equivalent path: export/NNN - bug-reminders-late-after-clock-change.md

Quality status: the Bug structure and the Bug-specific checks are met. Attention points: QA has not reproduced either pattern, Device and OS are Not provided, and Frequency stays Not provided because no source gives an every-time claim for the whole bug.

Additions for you to strike or confirm:
- The discipline code BE and the title built on it. You did not answer that question, so I applied my proposal.
- The iOS steps come from the ticket descriptions and have not been reproduced.
- The root-cause line is marked unconfirmed, based on Ruben's reading of the log lines.
- Member and device IDs are removed from the log lines, and the Browser rows are left out because the bug is not on web.
- Your answer did not say whether Ruben's iOS log pull is coming, so no iOS log lines are attached.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the bold labels "1. Observed Behavior" and "2. Expected Behavior", which the Human Voice card fixes for Bug Mode.