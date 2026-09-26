```markdown
I'll create the Android subtask `FE - Android - TODO - Recurring to-dos` under `FS - TODO - Recurring to-dos`. The parent already sets the shared rules, so I only need the Android decisions below. Please answer them together in one reply.

**Scope split with the engine:**
- Which rules does the Android app apply itself, and which does it only show from `BE - TODO - Recurrence engine`? For example the next due date, the After count, the 500 limit check and the owner's time zone
- After a check-off, should Android show the next occurrence right away, or only once the engine returns it?

**Reminders on the device:**
- Android schedules reminders as local notifications. When a member checks off or skips an occurrence, does this subtask cover cancelling the old notification and scheduling the next one at the same local time? Or does that belong to REM work?

**Free plan upgrade sheet:**
- Billing changes happen only on Web. What should the upgrade sheet do on Android? It could explain Plus and send the member to Web, or it could open an existing Android upgrade sheet. If one exists, please name it

**Requirements and acceptance:**
- Should the checklist restate each shared rule as an Android check, or point to the parent and list only Android behavior?
- Should it cover any Android-only states? For example a failed save when the connection drops, a tablet layout, or a teammate's view that shows the owner's zone

**Copy and locales:**
- Will localisation supply translations for the new strings, such as `Add a due date to repeat`, the 500-limit sheet and the option labels? Or should the task name only the en-US strings?

**Design and links:**
- Do you have Figma links for `Recurring to-dos / Repeat picker`, `Recurring to-dos / Custom interval` and `Recurring to-dos / Occurrence menu`, and a ClickUp link for the parent? Without links I'll name each one as backticked text

**Release:**
- Is there a target Android release, or does the task only say it ships behind `recurring_todos`?

**Validation:**
- What in the parent am I likely to misread, and which constraint should I question?
```

Export-equivalent path: `export/NNN - task-android-recurring-todos-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I read the parent task and the Loomlist context. The subtask title and discipline code come straight from the parent. The questions cover the things neither file settles:

- **Engine vs Android:** which rules the engine owns and which the Android app handles.
- **Reminders on Android:** Android schedules reminders as local notifications on the device, so each new occurrence may need its own.
- **Upgrade sheet vs billing:** the parent wants an upgrade sheet on Free, but billing changes happen only on Web. That clash needs a decision before I write the requirement.

I'll draft the Android subtask once you answer.