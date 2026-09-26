# FS - REM - Reminders arrive one hour late after the March clock change

## About

---

After clocks moved forward on 2026-03-29, members in affected time zones got reminders one hour late. Two unlike groups, one-off reminders on Android 5.2.3 (Group A) and daily reminders on iOS 5.2.4 (Group B), show no shared cause, so this report keeps them apart.

Nothing has shipped. Clocks go back one hour on 2026-10-25, and Support wants a fix or plan before then. Nobody has checked Android 5.3.0 or iOS 5.3.2, because clocks have not changed since March.

| Field           | Value                                                                 |
| --------------- | --------------------------------------------------------------------- |
| Frequency       | Not provided                                                          |
| Severity        | High                                                                  |
| Platform        | Android 5.2.3 (Group A), iOS 5.2.4 (Group B)                          |
| Device          | Not provided                                                          |
| OS Version      | Not provided                                                          |
| Browser         | Not applicable, Web and Desktop reminders show in-app only and none were reported |
| Browser Version | Not applicable                                                        |

**References:**

**Support**
- Marta's `reminder-late` report, 2026-04-07, re-shared with To-dos and Reminders on 2026-09-16
- LL-20931, Android 5.2.3, Europe/Amsterdam, Plus workspace (Group A)
- LL-20944, iOS 5.2.4, Europe/Berlin, Free workspace (Group B)
- LL-20958, iOS 5.2.4, Europe/Madrid, Team workspace (Group B)

**Logs**
- Ruben's reminders-service log excerpt for LL-20931, 2026-04-02, in the reminder-late investigation thread

**Flows and components:** Not provided

---

### Bug

---

**1. Observed Behavior**

---

From 2026-03-29 to 2026-04-05, Support tagged 117 tickets `reminder-late`, all from zones whose clocks moved forward on 2026-03-29. None report late iOS one-off or Android daily reminders, and QA has reproduced neither group.

Group A, Android 5.2.3, one-off reminders, 64 tickets
- A reminder set for 09:00 arrives at 10:00, as in LL-20931
- LL-20931 was set on Friday 2026-03-27 for Monday, and the member missed the call
- The member says their other reminders from that week were all an hour late
- One-off reminders set after the change arrived on time in the cases Support checked
- A one-off fires once, so there is nothing to repair

Group B, iOS 5.2.4, daily reminders, 53 tickets
- A daily 07:30 reminder arrives at 08:30 every day since the change
- Members changed nothing: LL-20944, a medication reminder, has come at 08:30 since Sunday 2026-03-29
- LL-20958: nine daily 07:30 stand-ups in one Team workspace arrive at 08:30
- Opening the reminder and tapping Save unchanged restores 07:30 from the next day
- On 2026-04-01 the LL-20944 member confirmed this, and the LL-20958 Admin fixed all nine that way
- Neither group shows an error message

Steps to Reproduce, Group A (from LL-20931, not yet reproduced by QA):
1. Before a forward clock change, on Android 5.2.3 with profile time zone Europe/Amsterdam, set a one-off to-do reminder for 09:00 local on a post-change date
2. Let the clock change pass
3. Wait for the reminder
4. Expected: it shows at 09:00 local, actual: 10:00 local
5. Control: a one-off reminder for 09:00 set after the change shows at 09:00

Steps to Reproduce, Group B (from LL-20944 and LL-20958, not yet reproduced by QA):
1. On iOS 5.2.4, with a profile time zone whose clocks move forward, set a daily 07:30 reminder before the change
2. Let the clock change pass
3. Wait for the next days' reminders
4. Expected: it shows at 07:30 local each day, actual: 08:30 local
5. Open the reminder and tap Save unchanged, and from the next day it shows at 07:30

Screen recording: Not provided, and no screenshots were supplied.

Log excerpt for LL-20931 (Group A only, UTC, IDs hashed as stored). Group B has no log lines yet.

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

Same member, phone, app version and zone: `rem_8f31c2`, created before the change with `tz_offset=+01:00`, showed at 10:00 local, and `rem_c41d07`, created after with `tz_offset=+02:00`, at 09:00.

Unverified hypothesis for Group A: the UTC due time may be fixed at creation with that day's offset. Ruben has not read the scheduling code, so it is not a confirmed root cause and says nothing about Group B.

---

**2. Expected Behavior**

---

A reminder arrives at the picked local date and time, in the to-do owner's profile time zone, whether set before or after a clock change
- Design spec: the member picks a local date and time in the owner's profile time zone (Loomlist product context)
- A daily reminder keeps its local time across a clock change without re-saving
- Previous working behavior: Not provided
- User expectation: reminders serve time-bound things (LL-20931 call, LL-20944 medication, LL-20958 stand-up), so an hour late is missed

Checklist
- [] Root cause identified
- [] Fix implemented
- [] Bug no longer reproducible
- [] No regressions introduced

---
