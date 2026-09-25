```markdown
# Clarification: late reminders after the March clock change

I'll write the bug report for the To-dos and Reminders team. The sources describe two groups of reports that Marta says "do not look alike" and Ruben says "look different". Before drafting, please answer the points below in one reply:

**Evidence so far:**
- Group A, Android 5.2.3, one-off reminders, 64 tickets: a reminder set before 2026-03-29 for 09:00 on a date after it arrived at 10:00. Ruben's log lines for LL-20931 show that reminder stored with `tz_offset=+01:00` and `scheduled_utc=2026-03-30T08:00:00Z`. A reminder set after the change was on time
- Group B, iOS 5.2.4, daily reminders, 53 tickets: 07:30 arrives at 08:30 every day until the member opens the reminder and taps Save. No log lines for this group yet
- No late one-off reminders reported on iOS and no late daily reminders reported on Android

**1. One bug or two:**
- Do you want both groups in one report, or one report per group? One report would carry two reproduction paths, two platforms and possibly two separate root causes under one "Bug no longer reproducible" check
- The title convention needs one platform segment or none. Should it be `FE - Android - REM`, `FE - iOS - REM`, `BE - REM` or something else? The logs don't say whether the fault sits in reminders-service or in the apps

**2. iOS evidence:**
- Ruben planned to pull log lines for two iOS daily reminder tickets. Did he, and can you share them? Without them, Group B rests on tickets LL-20944 and LL-20958 only

**3. Severity:**
- None of the sources set one. Which value should the report carry?

**4. Current versions:**
- Every report is from Android 5.2.3 or iOS 5.2.4. Has anyone checked Android 5.3.0 or iOS 5.3.2? If not, I'll mark current-version status as Not provided

**5. October clock change:**
- Marta asks for a fix or a plan before 2026-10-25, when these zones go back one hour. Should Expected Behavior also cover reminders across that change? The sources don't say what will happen then, so I'd write it only as expected behavior, never as observed
```

Export-equivalent path: `export/001 - bug-reminders-late-after-march-clock-change-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality status: this is an intake question, not the bug report, so no artifact score applies. The question covers the scope conflict, the title and discipline, the missing iOS evidence, severity, current versions and the October question.

**Why I stopped to ask:** The logs and Marta's reports give enough detail for a bug report. The problem is that both sources say these are two different patterns: one-off reminders on Android arrive late once, while daily reminders on iOS stay late until someone re-saves them. Putting them in one bug report could hide a second root cause. I'd rather you make that call than me. Once you answer, the bug report will take the next number in the bug lane.