**Path:** `export/002 - task-recurring-todos-android-subtask.md`
**Verified:** read-back succeeded; 140 lines
**HVR self-scan:** 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality summary:** The subtask covers the Android scope you described: the app shows the due date BE returns and never computes one on the device, on phones and tablets, shipping in 5.4.0. Its rules come from the parent, and the UI copy and values are carried verbatim in backticks. The clarification file 001 is unchanged.

The subtask is ready, but four points are open and I left them out rather than guess:

- **Reminders:** The parent doesn't say whether Android schedules the reminder for each next occurrence or whether the engine does, or whether the reminder keeps its local time.
- **Tracking:** `todo_repeat_set` and `todo_occurrence_skipped` are not in the draft because the parent doesn't name the client that sends them.
- **Limit trigger:** The draft says what the Repeat sheet shows at 500 repeating to-dos, but not how the app learns that the workspace is at the limit.
- **Flag reading:** I read "ships dark" as Repeat staying hidden while `recurring_todos` is off. Tell me if it should show greyed out instead.

Tell me the owner for each open point and I'll add it to the subtask.