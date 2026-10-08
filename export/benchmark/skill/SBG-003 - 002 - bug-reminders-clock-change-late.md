# BE - REM - Reminders fire one hour late after the March clock change

## About

---

Reminders saved before the clocks moved forward on 2026-03-29 fire one hour after the local time the member set, in time zones that changed that day, such as Europe/Amsterdam, Europe/Berlin and Europe/Madrid. Support has tagged 117 tickets `reminder-late` and needs a fix or a plan before the next clock change on 2026-10-25.

| Field           | Value                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------------- |
| Frequency       | Always (daily reminders stay late every day, per the support summary, not reproduced by QA)      |
| Severity        | High                                                                                              |
| Platform        | iOS 5.2.4 and Android 5.2.3, as reported                                                          |
| Device          | Not provided                                                                                      |
| OS Version      | Not provided                                                                                      |
| Browser         | Not applicable                                                                                    |
| Browser Version | Not applicable                                                                                    |

**References:**

**Flows**
- Get a reminder, from the Loomlist product context (link not provided)

---

### Bug

---

**1. Observed Behavior**

---

Reminders saved before 2026-03-29 fire one hour after the local time the member set. The reports describe two patterns, and their causes are not yet confirmed to be the same.

- Android one-off reminders: set for 09:00, shown at 10:00 local. Support counts 64 tickets on Android 5.2.3.
- iOS daily reminders: set for 07:30, shown at 08:30 every day. Support counts 53 tickets on iOS 5.2.4.
- The Android member in LL-20931 missed the call the reminder was for.
- The iOS member in LL-20944 has a daily reminder for medication.
- Editing and saving a daily reminder fixed it for the members in LL-20944 and LL-20958.
- Whether Android 5.3.0 or iOS 5.3.2 is affected is not confirmed, because no one has checked the current apps.
- Error message: Not provided

Ruben's reminders-service log excerpt covers the member in LL-20931 and their Android device, from 2026-03-27 to 2026-03-31. It holds two one-off reminders:

```text
2026-03-27T16:41:09.214Z INFO reminders-service reminder.created reminder_id=rem_8f31c2 member=m_5c07e1 todo=td_77a0b9 kind=one_off tz=Europe/Amsterdam local_date=2026-03-30 local_time=09:00 tz_offset=+01:00 scheduled_utc=2026-03-30T08:00:00Z platform=android app_version=5.2.3
2026-03-30T08:00:02.870Z INFO reminders-service reminder.shown reminder_id=rem_8f31c2 device=dv_3e19f0 platform=android app_version=5.2.3 device_local=2026-03-30T10:00:02+02:00
2026-03-30T08:07:52.563Z INFO reminders-service reminder.created reminder_id=rem_c41d07 member=m_5c07e1 todo=td_77a0c4 kind=one_off tz=Europe/Amsterdam local_date=2026-03-31 local_time=09:00 tz_offset=+02:00 scheduled_utc=2026-03-31T07:00:00Z platform=android app_version=5.2.3
2026-03-31T07:00:01.954Z INFO reminders-service reminder.shown reminder_id=rem_c41d07 device=dv_3e19f0 platform=android app_version=5.2.3 device_local=2026-03-31T09:00:01+02:00
```

- rem_8f31c2 was created before the change with tz_offset=+01:00 and scheduled_utc 08:00Z.
- On 2026-03-30 the zone is +02:00, where 09:00 local is 07:00Z, so the stored time is one hour late.
- rem_c41d07 was created after the change with tz_offset=+02:00 and scheduled_utc 07:00Z, and it shows at 09:00 local.

The root cause is not confirmed. The scheduling code has not been read, and the iOS log lines are not in the sources.

Steps to Reproduce:
1. On Android 5.2.3, set the to-do owner's time zone to Europe/Amsterdam.
2. Before 2026-03-29, set a one-off reminder for 09:00 on a Monday after the change.
3. Let the clock change pass on 2026-03-29.
4. At 09:00 local on the reminder's date, observe the reminder. Expected: it shows at 09:00 local. Actual: it shows at 10:00 local.

These steps follow the Android one-off report in LL-20931. QA has not reproduced the bug, and the sources have no steps for the iOS daily pattern.

Screen recording: Not provided

---

**2. Expected Behavior**

---

A reminder shows at the local time the member set, in the to-do owner's time zone, even across a clock change.

- Example: a one-off reminder set for Monday 09:00 in Europe/Amsterdam shows at 09:00 local, which is 07:00Z after the change.
- A daily reminder set for 07:30 shows at 07:30 local on each day after the change.
- Members do not need to edit or re-save a reminder to get the set time.
- Open: the sources do not say whether reminders saved before 2026-03-29 are corrected in place, or only new saves are fixed.

- Previous working behavior: reminders saved after the change show on time in the checked cases, including rem_c41d07 at 09:00 local.
- User expectations: members expect the set time with no change on their side (LL-20944: "I did not touch anything").
- Design specifications: Not provided

Checklist
- [] Root cause identified
- [] Fix implemented
- [] Bug no longer reproducible
- [] No regressions introduced
