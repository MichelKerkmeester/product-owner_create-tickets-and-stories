I haven't written the Android subtask yet. A `$task` command still needs one intake question answered first, so I saved that question instead.

Path: `export/001 - task-android-recurring-todos-clarification.md`
Verified: read-back succeeded; 17 lines
HVR self-scan: 1 hard blocker. Fixed: Oxford comma in "tell them to ask the Owner, or something else". Kept with reason: none.

The file holds only the question. The parent already settles the shared rules, the `recurring_todos` flag, the 500 limit, plans and tracking, so I only asked about the open points for Android:

- **Scope:** should the subtask restate the shared rules or link to the parent, and is a repeat marker on the to-do row or in the To-dos view in scope?
- **Upgrade sheet on Free:** the parent says Repeat on Free "opens the upgrade sheet", but the board context says only Web can change billing. What should that sheet let a member do on Android?
- **Check-off timing:** does the app wait for the recurrence engine before showing the next occurrence, or show it at once? What should the member see if the connection drops first?
- **Reminders:** is there Android-specific work, such as cancelling the old notification on Skip this one?
- **Guests:** can a guest with edit access set Repeat?
- **Tracking:** does Android fire `todo_repeat_set` and `todo_occurrence_skipped`, or does the engine send them?
- **Links and dependencies:** Figma links for the three named flows, whether to list the engine subtask as a dependency, and a target app version.

Once you answer, the subtask will be saved as `export/002 - task-android-recurring-todos.md` under `FE - Android - TODO - Recurring to-dos`. If you'd like me to go ahead now on defaults, say `$quick`. Anything I fill in myself will be listed in my reply so you can remove it.