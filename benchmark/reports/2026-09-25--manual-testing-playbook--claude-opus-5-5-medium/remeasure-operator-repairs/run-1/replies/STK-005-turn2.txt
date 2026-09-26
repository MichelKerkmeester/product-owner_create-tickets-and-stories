I've written the Android subtask, `FE - Android - TODO - Recurring to-dos`. Your answers left four points open, and I didn't settle them in the ticket.

Path: `export/002 - task-android-recurring-todos.md`
Verified: read-back succeeded; 129 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**What's in it:** It covers Android phones and tablets for the 5.4.0 release, with Oskar's Mobile Platform team named in About. The next due date always comes from the BE recurrence engine and is never worked out on the device. All values come from the parent: the five repeat options, N from 1 to 99, After from 1 to 365, the 500 limit and its message, the Plus badge and the two tracking events. Date calculation, including the Monthly 31st rule, is left to `BE - TODO - Recurrence engine`, which is listed as a related task.

**Things I added that you didn't state, so remove any you don't want:**
- The Figma flows, parent task and sibling tasks are plain names without links.
- Before the engine returns the next occurrence, Android shows no due date it worked out itself.
- With `recurring_todos` off, nothing from this subtask shows on Android.
- A series that has reached its end date or count shows no further occurrence.
- Both events carry the five standard properties from the board conventions, with `user_id` hashed.

**Still open, not written into the ticket:**
- **Upgrade sheet:** the parent says Repeat on Free "opens the upgrade sheet", but the board context says only Web can change billing. What that sheet lets an Android member do needs Oskar or Ines to decide.
- **Guests:** whether a guest with edit access can set Repeat.
- **Lost connection:** what a member sees if the connection drops right after checking off an occurrence.
- **Reminders on skip:** whether Android has to cancel the old reminder notification when a member skips.

If ClickUp tooling is available here, I can push the ticket to the To-dos and Reminders board once you approve.