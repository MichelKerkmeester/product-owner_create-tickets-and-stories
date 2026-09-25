# reminders-service log excerpt, late reminder on Android

Pulled by Ruben, Backend Engineer, Reminders, from the reminders-service log search on 2026-04-02.
Posted in the reminder-late investigation thread so Support and the Android team work from the same lines.

Filtered to the one member behind support ticket LL-20931 and the reminders on their Android phone. Member, to-do and device IDs are hashed the way the logs store them. The first column is server time in UTC.

From the ticket: the member lives in Europe/Amsterdam, where the clocks moved forward one hour on 2026-03-29. On Friday 2026-03-27 they set a one-off reminder for Monday at 09:00.

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

## Ruben's notes

rem_8f31c2 was created before the clock change and carries tz_offset=+01:00. It was shown on the phone at 10:00 local on 2026-03-30.

rem_c41d07 was created after the change, carries tz_offset=+02:00 and was shown at 09:00 local on 2026-03-31.

Both reminders were set by the same member on the same phone, same app version, same time zone.

I have not read the scheduling code yet, so these are the log lines and nothing more. Next I am pulling the same window for two of the iOS daily reminder tickets, which look different from this one.
