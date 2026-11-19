I'll write `FE - Android - TODO - Recurring to-dos` as a subtask of `FS - TODO - Recurring to-dos`. Please answer the points below in one reply.

**Format & scope:** Is this Android front end work only? The parent gives next due dates, occurrence creation, the 500 limit count and the time zone rule to `BE - TODO - Recurrence engine`. Does the Android app work out any of these on the device?

**Requirements:** Should the subtask restate each shared rule as an Android checklist item? That would cover Repeat on the detail sheet, Custom interval, Ends, check off, Skip this one, the 500 limit sheet, the Free upgrade sheet, the zone shown to teammates and the two events. Or should it cover only what differs on Android and point to the parent for the rest? Which Android-only behavior should it carry, if any, such as tablet layout or the back gesture on the picker?

**Reminders:** Android schedules reminders as local notifications. When a check off or a skip creates the next occurrence, should the subtask require the app to replace the old notification with one for the new due date at the same local time? Or does reminders-service handing over the new time already cover it?

**Connection:** There is no offline mode, and an edit made without a connection is retried until the app closes. What should a member see after checking off a repeating to-do with no connection? Does the next occurrence appear right away, or only once the engine answers?

**Design & platform:** Are there Figma links for `Recurring to-dos / Repeat picker`, `Recurring to-dos / Custom interval` and `Recurring to-dos / Occurrence menu`? The parent names them without links. Does Android have its own frames, or does it follow the shared flows?

**Access:** Can a guest with edit access, or a member who is not the to-do owner, set or change Repeat? The parent doesn't say.

**Dependencies & release:** Are there links for the parent and the three sibling tasks, or should I name them as plain text? Which Android release is the target, given 5.3.0 is current and the flag stays off until all three clients ship?

**Validation:** Is `FE - Android - TODO - Recurring to-dos` the title to use, and what am I likely to get wrong about this subtask?
