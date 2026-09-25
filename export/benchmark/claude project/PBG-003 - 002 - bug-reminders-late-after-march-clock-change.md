# FS - REM - Reminders arrive one hour late after the March clock change

### About

---

Since the clocks moved forward on 2026-03-29, reminders have arrived one hour late for members in the affected time zones. The late reminders are one-off reminders on Android 5.2.3 and daily reminders on iOS 5.2.4. The clocks in these zones go back one hour on 2026-10-25, and Support has asked for a fix or a plan before then.

| Field           | Value                                     |
| --------------- | ----------------------------------------- |
| Frequency       | Not provided                              |
| Severity        | High                                      |
| Platform        | Android (app 5.2.3), iOS (app 5.2.4)      |
| Device          | Not provided                              |
| OS Version      | Not provided                              |
| Browser         | Not applicable                            |
| Browser Version | Not applicable                            |

**References:**

**Support tickets**
- LL-20931, Android 5.2.3, Europe/Amsterdam, Plus workspace, one-off reminder
- LL-20944, iOS 5.2.4, Europe/Berlin, Free workspace, daily reminder
- LL-20958, iOS 5.2.4, Europe/Madrid, Team workspace, nine daily reminders

**Investigation**
- reminders-service log excerpt for LL-20931, pulled by Ruben (Backend Engineer, Reminders) on 2026-04-02
- Late reminder reports after the March clock change, compiled by Marta (Support Lead) on 2026-04-07 and re-shared on 2026-09-16

---

### Bug

---

**1. Observed Behavior**

---

Between 2026-03-29 and 2026-04-05, Support tagged 117 tickets `reminder-late`. All of them came from members in time zones where the clocks moved forward on 2026-03-29. The tickets fall into two groups:

- Group A, 64 tickets, Android 5.2.3: a one-off reminder set for 09:00 arrives at 10:00. It fires once, so nothing can be corrected after it arrives
- Group B, 53 tickets, iOS 5.2.4: a daily reminder set for 07:30 arrives at 08:30 every day. It stays late until the member opens the reminder and taps Save without changing anything. From the next day it arrives at 07:30 again
- No late one-off reminders were reported on iOS, and no late daily reminders were reported on Android
- No reports came from Web or Desktop. On those surfaces reminders appear only inside the app
- No error message was reported
- Impact shown in the tickets: a member missed the call the reminder was for (LL-20931), a medication reminder arrived an hour late (LL-20944), and nine members of one team got their stand-up reminder late until the Admin re-saved each reminder by hand (LL-20958)
- Log lines for LL-20931 show that the reminder set before the change was stored with `tz_offset=+01:00` and `scheduled_utc=2026-03-30T08:00:00Z`. It was shown at 10:00 local time. A reminder the same member set after the change was stored with `tz_offset=+02:00` and was shown at 09:00 local time
- There are no log lines for Group B yet

QA has not reproduced either group yet. Nobody has checked Android 5.3.0 or iOS 5.3.2, because the clocks have not changed since March. The steps below come from the support tickets and the log lines.

Steps to Reproduce:

Group A, one-off reminder on Android
1. On Android app 5.2.3, sign in as a member whose profile time zone moves its clocks forward, such as Europe/Amsterdam
2. Before the clock change, add a one-off reminder at 09:00 to a to-do, for a date after the change. In LL-20931 the reminder was set on 2026-03-27 for 2026-03-30
3. Wait for the reminder date after the change
4. Observe the notification. Expected: 09:00 local time. Actual: 10:00 local time
5. After the change, add another one-off reminder at 09:00. It arrives at 09:00

Group B, daily reminder on iOS
1. On iOS app 5.2.4, sign in as a member whose profile time zone moves its clocks forward, such as Europe/Berlin or Europe/Madrid
2. Before the clock change, add a daily reminder at 07:30 to a to-do
3. After the change, observe the notification on each following day. Expected: 07:30 local time. Actual: 08:30 local time, every day
4. Open the reminder and tap Save without changing anything
5. Observe the next day's notification. It arrives at 07:30

reminders-service log excerpt for LL-20931 (server time in UTC, IDs hashed):

```text
2026-03-27T16:41:09.214Z INFO reminders-service reminder.created reminder_id=rem_8f31c2 member=m_5c07e1 todo=td_77a0b9 kind=one_off tz=Europe/Amsterdam local_date=2026-03-30 local_time=09:00 tz_offset=+01:00 scheduled_utc=2026-03-30T08:00:00Z platform=android app_version=5.2.3
2026-03-27T16:41:09.388Z INFO reminders-service reminder.handoff reminder_id=rem_8f31c2 device=dv_3e19f0 platform=android app_version=5.2.3 scheduled_utc=2026-03-30T08:00:00Z result=accepted
2026-03-28T07:15:44.901Z INFO reminders-service device.pull device=dv_3e19f0 platform=android app_version=5.2.3 reminders=1
2026-03-29T09:02:31.117Z INFO reminders-service device.pull device=dv_3e19f0 platform=android app_version=5.2.3 reminders=1
2026-03-30T06:48:12.540Z INFO reminders-service device.pull device=dv_3e19f0 platform=android app_version=5.2.3 reminders=1
2026-03-30T08:00:00.431Z INFO reminders-service reminder.due reminder_id=rem_8f31c2 scheduled_utc=2026-03-30T08:00:00Z
2026-03-30T08:00:02.870Z INFO reminders-service reminder.shown reminder_id=rem_8f31c2 device=dv_3e19f0 platform=android app_version=5.2.3 device_local=2026-03-30T10:00:02+02:00
2026-03-30T08:07:52.563Z INFO reminders-service reminder.created reminder_id=rem_c41d07 member=m_5c07e1 todo=td_77a0c4 kind=one_off tz=Europe/Amsterdam local_date=2026-03-31 local_time=09:00 tz_offset=+02:00 scheduled_utc=2026-03-31T07:00:00Z platform=android app_version=5.2.3
2026-03-30T08:07:52.702Z INFO reminders-service reminder.handoff reminder_id=rem_c41d07 device=dv_3e19f0 platform=android app_version=5.2.3 scheduled_utc=2026-03-31T07:00:00Z result=accepted
2026-03-31T07:00:00.318Z INFO reminders-service reminder.due reminder_id=rem_c41d07 scheduled_utc=2026-03-31T07:00:00Z
2026-03-31T07:00:01.954Z INFO reminders-service reminder.shown reminder_id=rem_c41d07 device=dv_3e19f0 platform=android app_version=5.2.3 device_local=2026-03-31T09:00:01+02:00
```

Screen recording: Not provided

---

**2. Expected Behavior**

---

A reminder arrives at the local time the member picked, in the to-do owner's time zone. This holds whether the reminder was set before or after a clock change.

- A one-off reminder set for 09:00 before a clock change, for a date after it, arrives at 09:00
- A daily reminder set for 07:30 arrives at 07:30 on every day before and after a clock change, with no edit or re-save by the member
- Previous working behavior: one-off reminders set on Android after the change arrived on time (rem_c41d07). Daily reminders on iOS arrive on time again from the day after the member re-saves them
- User expectation: members rely on reminders for calls, medication and team routines, so a reminder that arrives an hour late causes them to miss the thing it was set for

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** One-off reminder set before a clock change
- **Given** a member in Europe/Amsterdam sets a one-off reminder for 09:00 on a date after the clocks move forward
- **When** that date arrives after the change
- **Then** the reminder arrives at 09:00 local time

**Scenario:** Daily reminder that spans a clock change
- **Given** a member in Europe/Berlin has a daily reminder at 07:30 that was set before the clocks moved forward
- **When** each day after the change arrives
- **Then** the reminder arrives at 07:30 local time without the member editing or re-saving it
