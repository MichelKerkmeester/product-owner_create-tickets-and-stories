# FE - Android - TODO - Recurring to-dos

### About

---

The Android app gets the same member-facing half of recurring to-dos as iOS: the Repeat and Ends pickers, the Custom interval, Skip this one and the repeat icon on the to-do row. The next occurrence, Ends, the 500 limit and the reminder handover belong to the BE subtask, and the shared rules with every value sit in the parent task.

Work starts after Yara has reviewed the tracking plan. The app ships dark behind `recurring_todos`, and Data turns the flag on only once iOS, Android and Web are all out.

**References**

---

Components

- `Recurring to-dos / Repeat picker`
- `Recurring to-dos / Custom interval`
- `Recurring to-dos / Occurrence menu`

**Parent task**

---

- [FS - TODO - Recurring to-dos](<001 - task-recurring-todos-parent.md>)

**Related tasks**

---

- [FE - iOS - TODO - Recurring to-dos](<002 - task-recurring-todos-ios.md>)
- [BE - TODO - Recurring to-do occurrences, Ends and workspace limit](<005 - task-recurring-todos-be.md>)

### Requirements

---

1.  **Repeat and Ends pickers**

---

Members set a repeat from the to-do's detail sheet, where the due date, assignee and reminder already live.

**Checklist**

- [ ] Repeat sits in the to-do's detail sheet and has Daily, Weekdays, Weekly, Monthly and Custom, matching `Recurring to-dos / Repeat picker`
- [ ] A to-do without a due date shows Repeat greyed out with the hint `Add a due date to repeat`
- [ ] Custom sets every N days, weeks or months, with N from 1 to 99, matching `Recurring to-dos / Custom interval`
- [ ] Ends sits under Repeat with Never, On date and After, and Never is the default
- [ ] After accepts from 1 to 365 occurrences

---

2.  **Skip this one and the repeat icon**

---

A member can see at a glance which to-dos repeat, and can move one on without pretending it was done.

**Checklist**

- [ ] The to-do's menu has Skip this one, matching `Recurring to-dos / Occurrence menu`
- [ ] Skip this one moves the to-do to its next due date and leaves it unchecked
- [ ] A repeating to-do shows the repeat icon on its row
- [ ] Checking off an occurrence shows the next one on the same page with the next due date, the same assignee and the same reminder

---

3.  **Plans, the workspace limit and the flag**

---

**Checklist**

- [ ] On a Free workspace, Repeat shows with a Plus badge and opens the upgrade sheet
- [ ] At the workspace limit, Repeat stays visible and opens a sheet that says `This workspace has 500 repeating to-dos. End one to add another.`
- [ ] With `recurring_todos` off for the workspace, Repeat, Ends, Skip this one and the repeat icon do not show

---

4.  **Reminders and time zones**

---

Android schedules reminders as local notifications from the UTC time reminders-service hands over, so the next occurrence's reminder has to arrive the same way as any other.

**Checklist**

- [ ] The next occurrence's reminder arrives as a local notification at the same local time as the one before
- [ ] A teammate in another time zone sees the to-do owner's date with the zone shown

---

5.  **Tracking**

---

**Checklist**

- [ ] The app sends whichever of `todo_repeat_set` and `todo_occurrence_skipped` the reviewed tracking plan assigns to clients, with `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
