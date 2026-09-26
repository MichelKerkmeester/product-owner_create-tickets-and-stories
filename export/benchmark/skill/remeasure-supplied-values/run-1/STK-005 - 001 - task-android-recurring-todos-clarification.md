# FE - Android - TODO - Recurring to-dos: clarification

I'll write this as the Android subtask of `FS - TODO - Recurring to-dos`, under the title the parent already names. Before drafting, please answer these in one reply:

**1. Client versus engine split:** The parent says each subtask builds the shared rules "in one client or in the engine" but doesn't say which side owns what. For Android, which of these does the app own, and which does it only show from `BE - TODO - Recurrence engine`?
- Working out the next due date, including the Monthly day-of-month rule and the owner's time zone
- Creating the next occurrence on check-off and on Skip this one
- Enforcing the 500-series limit and the After count (1 to 365)
- Showing Repeat with a Plus badge on Free and opening the upgrade sheet

**2. Reminders on the next occurrence:** On Android, reminders fire as local notifications scheduled from the UTC time reminders-service hands over. Should this subtask cover scheduling the carried-over reminder for the new occurrence, or does the existing reminder flow already handle it once reminders-service sends the new time?

**3. Tracking:** Does Android send `todo_repeat_set` and `todo_occurrence_skipped` itself, or does the engine send them server-side?

**4. Screens and links:**
- Figma or ClickUp links for the three flows (`Recurring to-dos / Repeat picker`, `Recurring to-dos / Custom interval`, `Recurring to-dos / Occurrence menu`) and for the parent task, or should I name them as plain text?
- Does Android already have an upgrade sheet that Repeat can open on Free, and a sheet pattern for the limit message, or are these new?

**5. Release and dependencies:**
- Which Android release does this target, and is there a minimum engine version or date it has to wait for?
- No connection: the app keeps the open page but retries edits until it closes. Should the subtask state what the member sees when they check off a repeating to-do offline, or leave that to the engine subtask?

**6. What am I likely to get wrong?** For example, whether Android covers tablets too, or any rule in the parent that doesn't apply to Android.
