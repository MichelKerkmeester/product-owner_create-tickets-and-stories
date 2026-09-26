# FS - REM - Reminders arrive one hour late after the March clock change

### About

---

After the clocks moved forward on 2026-03-29, members in affected time zones got reminders one hour after the local time they picked. Support sees two groups that do not look alike: one-off reminders on Android 5.2.3 and daily reminders on iOS 5.2.4. Nothing shows a shared cause, so this report keeps them apart as Group A and Group B.

Nothing has shipped for this yet. The next clock change in these zones is on 2026-10-25, when the clocks go back one hour, and Support has asked for a fix or a plan before then. Nobody has checked the current Android 5.3.0 and iOS 5.3.2 apps, because the clocks have not changed since March.

| Field           | Value                                                                 |
| --------------- | --------------------------------------------------------------------- |
| Frequency       | Not provided                                                          |
| Severity        | High                                                                  |
| Platform        | Android 5.2.3 (Group A), iOS 5.2.4 (Group B)                          |
| Device          | Not provided                                                          |
| OS Version      | Not provided                                                          |
| Browser         | Not applicable, reminders on Web and Desktop show in the app only and none were reported |
| Browser Version | Not applicable                                                        |

**References:**

**Support**
- Marta's `reminder-late` report, compiled 2026-04-07 and re-shared with To-dos and Reminders on 2026-09-16
- LL-20931, Android 5.2.3, Europe/Amsterdam, Plus workspace (Group A)
- LL-20944, iOS 5.2.4, Europe/Berlin, Free workspace (Group B)
- LL-20958, iOS 5.2.4, Europe/Madrid, Team workspace (Group B)

**Logs**
- Ruben's reminders-service log excerpt for LL-20931, pulled 2026-04-02 and posted in the reminder-late investigation thread

**Flows and components:** Not provided

---

### Bug

---

**1. Observed Behavior**

---

Between 2026-03-29 and 2026-04-05, Support tagged 117 tickets `reminder-late`, all from members in time zones whose clocks moved forward on 2026-03-29. There are no reports of late one-off reminders on iOS or late daily reminders on Android. QA has not reproduced either group yet.

Group A, Android 5.2.3, one-off reminders, 64 tickets
- A reminder set for 09:00 arrives at 10:00
- LL-20931: a reminder set on Friday 2026-03-27 for Monday 09:00 arrived at 10:00, and the member missed the call it was for
- The LL-20931 member says the other reminders they set that week were all an hour late
- A one-off reminder set after the change arrived on time in the cases Support checked
- A one-off reminder fires once, so there is nothing for the member to repair after the fact

Group B, iOS 5.2.4, daily reminders, 53 tickets
- A daily reminder set for 07:30 arrives at 08:30, every day from the change onward
- Members changed nothing: LL-20944 is a daily medication reminder that has come at 08:30 since Sunday 2026-03-29
- LL-20958: nine daily 07:30 stand-up reminders in one Team workspace all arrive at 08:30
- The delay continues until the member opens the reminder and taps Save with no change, and from the next day it arrives at 07:30 again
- On 2026-04-01 the LL-20944 member confirmed that re-saving works, and the LL-20958 Admin fixed all nine reminders that way
- No error message is shown in either group

Steps to Reproduce, Group A (from LL-20931, not yet reproduced by QA):
1. Before a forward clock change, on Android 5.2.3 with profile time zone Europe/Amsterdam, set a one-off to-do reminder for 09:00 local on a post-change date
2. Let the clock change pass
3. Wait for the reminder on the chosen date
4. Expected: the reminder shows at 09:00 local, actual: it shows at 10:00 local
5. Control: set a second one-off reminder for 09:00 after the change, and it shows at 09:00

Steps to Reproduce, Group B (from LL-20944 and LL-20958, not yet reproduced by QA):
1. On iOS 5.2.4, with a profile time zone whose clocks move forward, have a daily reminder set for 07:30 before the change
2. Let the clock change pass
3. Wait for the reminder on the following days
4. Expected: the reminder shows at 07:30 local each day, actual: it shows at 08:30 local every day
5. Open the reminder and tap Save without changing anything, and from the next day it shows at 07:30

Screen recording: Not provided. No screenshots were supplied.

Log excerpt for LL-20931 (Group A only, server time in UTC, IDs hashed as stored). No log lines exist yet for Group B.

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

Both reminders belong to the same member, phone, app version and time zone. `rem_8f31c2` was created before the change with `tz_offset=+01:00` and showed at 10:00 local. `rem_c41d07` was created after the change with `tz_offset=+02:00` and showed at 09:00 local.

Hypothesis for Group A, unverified: the UTC due time may be fixed when the reminder is created, using the offset in force that day. Ruben has not read the scheduling code, so this is not a confirmed root cause, and it says nothing about Group B.

---

**2. Expected Behavior**

---

A reminder arrives at the local date and time the member picked, in the to-do owner's profile time zone, whether it was set before or after a clock change
- Design spec: reminders use the to-do owner's profile time zone, and the member picks a local date and time (Loomlist product context)
- A daily reminder keeps its local time across a clock change without the member opening it and saving it again
- Previous working behavior: Not provided
- User expectation: members rely on reminders for time-bound things (the LL-20931 call, LL-20944 medication, LL-20958 stand-up), so an hour late is a missed reminder

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---
