# Late reminders after the March clock change: question before drafting

I'll write the bug report for To-dos and Reminders. One decision in the sources is yours to make, and two fields shape the title and the field table. Please answer all three in one reply.

**Scope, one bug or two:** Marta splits the 117 `reminder-late` tickets into two groups that "do not look alike", and Ruben expects the iOS daily tickets to look different from the Android one he logged.

- Group A: Android 5.2.3, one-off reminders, 64 tickets
- In Ruben's LL-20931 lines, a reminder created before the change carried `tz_offset=+01:00` and showed at 10:00 local, while one created after it showed at 09:00
- Group B: iOS 5.2.4, daily reminders, 53 tickets
- Group B reminders stay an hour late every day until the member opens the reminder and taps Save
- No log lines exist for Group B yet

Nothing in the sources says both groups share a cause, so a single report would suggest a link nobody has shown. Which do you want?

1. Two bugs, one per group, each carrying only its own evidence
2. One bug with both groups as separate observed cases and the root cause left open
3. One grouped Task for To-dos and Reminders that tracks both defects

**Discipline code and severity:** Titles follow `{Discipline} - {Platform} - REM - {Title}`, but Ruben has not read the scheduling code yet, so the sources don't say whether the fault sits in the apps (`FE - Android`, `FE - iOS`) or in reminders-service (`BE`, no platform segment). Which code should each report carry? No source sets a severity either, so give one or I'll write `Not provided`.

**Current app versions:** The reports cover Android 5.2.3 and iOS 5.2.4, while the current releases are Android 5.3.0 and iOS 5.3.2. Has anyone checked whether the current versions still carry the behavior? If not, I'll say so in the report, because the next clock change in these zones is on 2026-10-25.
