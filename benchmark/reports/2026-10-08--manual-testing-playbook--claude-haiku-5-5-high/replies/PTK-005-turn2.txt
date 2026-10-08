```markdown
# Android subtask for recurring to-dos: clarification (round two)

I still need these decisions before drafting the Android subtask of `FS - TODO - Recurring to-dos`. Please answer them in one response.

**Scope:** Which of these does the 5.4.0 build include: the Repeat picker, the Custom interval, the Occurrence menu, the limit sheet and the Free-plan upgrade sheet? Does it carry every shared rule, or a subset?

**Reminders:** When a check-off creates the next occurrence, should the app reschedule its local reminder to the time BE returns for that occurrence?

**Free plan:** Should the Android upgrade sheet link to the web upgrade flow, or show the Plus badge with no purchase action?

**Offline:** Is it acceptable that a check-off made without a connection is retried until the app closes, then lost?

**Tracking:** Should Android send `todo_repeat_set` and `todo_occurrence_skipped`?

**Engine contract:** Which contract or identifier should the subtask cite for the next-occurrence response, and is it fixed before the Android build starts?

**Design:** Which Figma frames cover the Android screens?
```

Export-equivalent path: `export/NNN - task-android-recurring-todos-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: bold lead labels, which the Task Format Question template fixes.

Quality status: clarification only, so no artifact is scored yet.

Your answers settle three things: the owner is Mobile Platform (Oskar's team), the release is 5.4.0, and the title is `FE - Android - TODO - Recurring to-dos` from the parent's list. The app shows the next due date that BE returns and computes nothing on the device. The first clarification stays as delivered, and the subtask takes the next number once these questions are answered.