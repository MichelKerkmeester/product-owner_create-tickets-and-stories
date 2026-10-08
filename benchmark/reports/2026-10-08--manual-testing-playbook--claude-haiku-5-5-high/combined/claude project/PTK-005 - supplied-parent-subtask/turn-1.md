```markdown
# Android subtask for recurring to-dos: clarification

I'll create the Android subtask of `FS - TODO - Recurring to-dos`. Before drafting, I need the unresolved decisions below in one response.

**Scope:** The parent's shared rules apply to every client. Which of these does the Android subtask build: the Repeat picker, the Custom interval, the Occurrence menu, the limit sheet and the Free-plan upgrade sheet? Does it carry every shared rule, or a subset?

**Owner:** Should To-dos and Reminders (Ines) own the Android subtask, or Mobile Platform (Oskar), which leads Android releases?

**Title:** I'll use `FE - Android - TODO - Recurring to-dos`, the title the parent gives this requirement, unless you name a narrower one.

**Reminders:** Android schedules reminders as local notifications from the UTC time reminders-service hands over. When a check-off creates the next occurrence, should the Android app reschedule the reminder, or does reminders-service hand over the new time?

**Free plan:** Web is the only surface for billing changes. On Free, Repeat shows a Plus badge. Should the Android upgrade sheet link to the web upgrade flow, or show the badge with no purchase action?

**Offline:** Android has no offline mode. An edit made without a connection is retried until the app closes, then lost. Is that behavior acceptable for a check-off that creates the next occurrence?

**Tracking:** Should Android send `todo_repeat_set` and `todo_occurrence_skipped`, both named in the parent's tracking rule?

**Design and dependencies:** Which Figma frames cover the Android screens? Does the Android build wait on the recurrence engine contract in `BE - TODO - Recurrence engine`?

**Validation:** Do you expect any Android behavior to differ from iOS?
```

Export-equivalent path: `export/NNN - task-android-recurring-todos-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: bold lead labels, which the Task Format Question template fixes.

Quality status: clarification only, so no artifact is scored yet.

The parent splits work across four teams and leaves the Android scope, owner and offline behavior open, so I haven't drafted the subtask. Answer the questions above and I'll draft it in a new Deliverable Block.