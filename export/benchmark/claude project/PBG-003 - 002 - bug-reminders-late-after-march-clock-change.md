# FS - REM - Reminders arrive one hour late after the March clock change

### About

---

Since the clocks moved forward on 2026-03-29, one-off reminders on Android 5.2.3 and daily reminders on iOS 5.2.4 arrive one hour late. Clocks go back one hour on 2026-10-25, and Support wants a fix or plan before then.

| Field           | Value                                     |
| --------------- | ----------------------------------------- |
| Frequency       | Not provided                              |
| Severity        | High                                      |
| Platform        | Android 5.2.3, iOS 5.2.4                  |
| Device          | Not provided                              |
| OS Version      | Not provided                              |
| Browser         | Not applicable                            |
| Browser Version | Not applicable                            |

**References:**

**Support tickets**
- LL-20931, Android 5.2.3, Europe/Amsterdam, Plus, one-off
- LL-20944, iOS 5.2.4, Europe/Berlin, Free, daily
- LL-20958, iOS 5.2.4, Europe/Madrid, Team, nine daily reminders

**Investigation**
- reminders-service log excerpt for LL-20931, pulled by Ruben (Backend Engineer, Reminders) on 2026-04-02
- Late reminder reports, compiled by Marta (Support Lead) on 2026-04-07 and re-shared on 2026-09-16

---

### Bug

---

**1. Observed Behavior**

---

Between 2026-03-29 and 2026-04-05, Support tagged 117 tickets `reminder-late`, all from zones where clocks moved forward on 2026-03-29:

- Group A, 64 tickets, Android 5.2.3: a one-off 09:00 reminder arrives at 10:00, and fires only once
- Group B, 53 tickets, iOS 5.2.4: a daily 07:30 reminder arrives at 08:30 until the member re-saves it unchanged
- No late one-off reminders on iOS, daily ones on Android, or reports from Web or Desktop, where reminders show only in-app
- No error message was reported
- Impact: a missed call (LL-20931), a medication reminder an hour late (LL-20944), nine teammates' stand-up reminders late until the Admin re-saved each (LL-20958)
- LL-20931 logs: a reminder set before the change stored `tz_offset=+01:00` and `scheduled_utc=2026-03-30T08:00:00Z` and showed at 10:00, one set after stored `tz_offset=+02:00` and showed at 09:00
- No Group B log lines exist yet

QA has reproduced neither group, and nobody has checked Android 5.3.0 or iOS 5.3.2, as the clocks have not changed since March. Steps come from the tickets and logs.

Steps to Reproduce:

Group A, one-off reminder on Android
1. On Android 5.2.3, sign in as a member whose profile time zone moves clocks forward, such as Europe/Amsterdam
2. Before the change, add a one-off 09:00 reminder for a later date, as LL-20931 did on 2026-03-27 for 2026-03-30
3. On that date: expected 09:00 local time, actual 10:00
4. After the change, a new one-off 09:00 reminder arrives at 09:00

Group B, daily reminder on iOS
1. On iOS 5.2.4, sign in as a member whose profile time zone moves clocks forward, such as Europe/Berlin or Europe/Madrid
2. Before the change, add a daily 07:30 reminder
3. After the change, each day: expected 07:30 local time, actual 08:30
4. Tap Save on the reminder unchanged, and the next day it arrives at 07:30

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

A reminder arrives at the local time picked, in the to-do owner's time zone, whether set before or after a clock change.

- A one-off 09:00 reminder set before a clock change, for a date after it, arrives at 09:00
- A daily 07:30 reminder arrives at 07:30 every day across a clock change, with no edit or re-save
- Previous working behavior: Android one-off reminders set after the change (rem_c41d07) and re-saved iOS daily reminders arrive on time
- User expectation: reminders for calls, medication and team routines arrive on time

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** One-off reminder set before a clock change
- **Given** a member in Europe/Amsterdam sets a one-off 09:00 reminder for a date after clocks move forward
- **When** that date arrives
- **Then** it arrives at 09:00 local time

**Scenario:** Daily reminder that spans a clock change
- **Given** a member in Europe/Berlin has a daily 07:30 reminder set before clocks moved forward
- **When** each later day arrives
- **Then** it arrives at 07:30 local time with no edit or re-save
