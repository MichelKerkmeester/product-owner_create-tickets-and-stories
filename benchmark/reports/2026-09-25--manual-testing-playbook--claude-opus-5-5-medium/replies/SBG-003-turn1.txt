I haven't written the bug yet. I saved one question first, because your sources describe two problems that don't look like one bug.

Path: `export/001 - bug-reminders-late-after-clock-change-clarification.md`
Verified: read-back succeeded; 19 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Why I stopped:** Marta's reports split the 117 tickets into two groups that "do not look alike":
- **Android one-off reminders (5.2.3):** Ruben's logs show a reminder set before the clock change keeping the old offset and arriving an hour late. One set after the change arrived on time.
- **iOS daily reminders (5.2.4):** these stay an hour late every day until the member opens the reminder and taps Save. There are no log lines for this group yet.

Ruben expects the iOS tickets to look different too, and nothing in the sources links the two to one cause. Writing a single bug would suggest a shared cause nobody has shown.

**What the question asks:**
- **How to split it:** two bugs, one combined bug with the root cause left open, or one grouped task.
- **Title code:** the title needs a discipline code, and nobody has read the scheduling code yet. So the sources can't tell me whether the fault is in the apps (FE) or in reminders-service (BE).
- **Severity:** none is set in the sources.
- **Current versions:** has anyone checked whether today's Android 5.3.0 and iOS 5.3.2 still do this? That matters because the next clock change is on 2026-10-25.

Once you answer, the bug report (or reports) will be saved under the next number, and this question file stays as it is.