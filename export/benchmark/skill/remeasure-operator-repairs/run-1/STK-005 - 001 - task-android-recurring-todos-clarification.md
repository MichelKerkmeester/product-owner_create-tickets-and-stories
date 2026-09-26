I'll create the Android subtask `FE - Android - TODO - Recurring to-dos` under the parent `FS - TODO - Recurring to-dos`. The parent already fixes the shared rules, the `recurring_todos` flag, the 500 limit and the two events. Before drafting, I need the open points below answered in one reply:

**Format & scope:** Should the subtask restate the shared rules as Android checklists, or link to the parent and carry only what Android has to get right? Is anything beyond the detail sheet, the occurrence menu and the limit and upgrade sheets in scope, such as a repeat marker on the to-do row or in the To-dos view?

**Upgrade sheet on Free:** The parent says Repeat on Free "opens the upgrade sheet", but the board context says Web is the only surface for billing changes. What should the Android upgrade sheet let a Free member do: send them to Web, tell them to ask the Owner or something else?

**Requirements:** When a member checks off an occurrence on Android, does the app wait for the recurrence engine to create the next one, or show it at once? If the connection drops before sync, what should the member see? There is no offline mode, and an edit that has not synced is lost when the app closes.

**Reminders:** Android schedules reminders as local notifications. Is there any Android-specific reminder work to capture, for example cancelling the old notification on Skip this one? Or does the existing reminders-service handover cover it with no change?

**Permissions:** Can a guest with edit access set or change Repeat, or is it for members only?

**Tracking:** Does Android fire `todo_repeat_set` and `todo_occurrence_skipped` from the client, or does the engine send them?

**Design & dependencies:** Do you have Figma links for `Recurring to-dos / Repeat picker`, `Recurring to-dos / Custom interval` and `Recurring to-dos / Occurrence menu`, or should they stay as named flows? Should the subtask name `BE - TODO - Recurrence engine` as a dependency? Is there a target app version, since Android 5.3.0 is current?

**Validation:** What am I likely to get wrong about Android here, such as how Android handles time zones or what older app versions show for a repeating to-do?
