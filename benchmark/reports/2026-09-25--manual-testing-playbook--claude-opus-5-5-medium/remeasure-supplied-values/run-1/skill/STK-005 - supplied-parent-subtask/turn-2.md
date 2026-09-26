I've written the Android subtask. It targets phones and tablets in the `5.4.0` release, and the app shows the next due date the recurrence engine returns without working it out on the device.

Path: `export/002 - task-android-recurring-todos.md`
Verified: read-back succeeded; 134 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the full stops inside the backticked limit-sheet message, because that is the parent's exact wording.

**Quality summary:** The subtask has six requirement groups: the repeat picker, the next due date, check-off and skip, the workspace limit, plans and the feature flag, and tracking. Every value in it comes from the parent task:
- the ranges `1` to `99` and `1` to `365`
- the `500` repeating to-do limit and its message
- the event names
- the `recurring_todos` flag

The ownership rule you gave me is in About and has its own requirement group.

Three parts are my own reading or additions, so please strike any that are wrong:
- **Flag off:** With `recurring_todos` off, Android shows no recurring to-do controls. That's how I read "ships dark".
- **Reminders:** The carried-over reminder is written as something the member sees, "fires on the next occurrence at the same local time". It doesn't say whether Android or the existing reminder flow does the scheduling.
- **Tracking:** A note asks Yara to confirm whether the app or the engine sends `todo_repeat_set` and `todo_occurrence_skipped`. The parent doesn't say.

**Not covered:** The flows and related tasks are plain text because no links were supplied. The subtask also doesn't say what happens when a member checks off a repeating to-do with no connection. You didn't answer that question, so I left it out.

I can push this to ClickUp if you'd like, but only once you say so.