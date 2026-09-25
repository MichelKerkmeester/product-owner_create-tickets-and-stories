I've written it up as one bug report, with the Android and iOS groups kept apart and the root cause left open.

Path: `export/002 - bug-reminders-late-after-clock-change.md`
Verified: read-back succeeded; 113 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `**1. Observed Behavior**` and `**2. Expected Behavior**`, the two fixed bug-report labels that are allowed to stay in title case.

**What's in the report:**
- **Group A, Android 5.2.3, one-off reminders, 64 tickets:** each group has its own reproduction steps, written from the tickets and marked as not yet reproduced by QA. This group also has Ruben's full log excerpt. It carries one hypothesis labelled unverified: the UTC time may be fixed using the offset in force on the day the reminder was set.
- **Group B, iOS 5.2.4, daily reminders, 53 tickets:** the report says plainly that there are no log lines for it yet.
- **Next clock change:** it's on 2026-10-25, and nobody has checked the 5.3 apps.

**Choices you should check:**
- **Title code:** you didn't pick one, so I used `FS - REM - …` with no platform part. That's the only code that covers two app platforms plus a service. If you want `BE` or a platform-specific `FE` instead, tell me.
- **Frequency:** set to `Not provided`, because the ticket counts don't say how often it happens. The counts are in Observed Behavior instead.
- **Browser fields:** set to "Not applicable". On Web and Desktop, reminders only show inside the app, and nobody reported a problem there.
- **Unknown details:** severity is High as you said. Device, OS version, recordings and how it behaved before are `Not provided`.
- **Left out:** Marta's fallback request for a help-center known-issue line and an agent macro. It's a Support deliverable, not part of this bug.

**Quality check:** the report follows the bug template, and every claim traces to one of the three source files or your answers. Neither the fixed QA checklist nor the steps say how to fix it.

If ClickUp tools are available here, I can create the ticket in the To-dos and Reminders list once you approve.