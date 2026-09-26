# FE - Android - TODO - Recurring to-dos

## About

---

Like iOS, the Android app gets the member-facing half of recurring to-dos, BE owns the next occurrence, Ends, the 500 limit and reminder handover, and the parent holds the shared rules.

It starts after Yara reviews the tracking plan and ships dark behind `recurring_todos`, which Data turns on only once iOS, Android and Web are out.

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

**Checklist**

- [] Repeat in the detail sheet offers Daily, Weekdays, Weekly, Monthly and Custom, matching `Recurring to-dos / Repeat picker`
- [] Without a due date, Repeat is greyed out with the hint `Add a due date to repeat`
- [] Custom sets every N days, weeks or months, N from 1 to 99, matching `Recurring to-dos / Custom interval`
- [] Ends, under Repeat, offers Never, the default, On date and After
- [] After accepts 1 to 365 occurrences

---

2.  **Skip this one and the repeat icon**

---

**Checklist**

- [] The to-do's menu has Skip this one, matching `Recurring to-dos / Occurrence menu`
- [] Skip this one moves the to-do to its next due date, unchecked
- [] Repeating to-dos show the repeat icon on their row
- [] Checking one off shows the next on the same page with the next due date, assignee and reminder

---

3.  **Plans, the workspace limit and the flag**

---

**Checklist**

- [] On Free, Repeat shows a Plus badge and opens the upgrade sheet
- [] At the limit, Repeat stays visible and opens a sheet saying `This workspace has 500 repeating to-dos. End one to add another.`
- [] With `recurring_todos` off, Repeat, Ends, Skip this one and the repeat icon are hidden

---

4.  **Reminders and time zones**

---

Android schedules every reminder as a local notification from the UTC time reminders-service hands over.

**Checklist**

- [] The next reminder arrives as a local notification at the previous one's local time
- [] Teammates in other zones see the owner's date with the zone shown

---

5.  **Tracking**

---

**Checklist**

- [] The app sends whichever of `todo_repeat_set` and `todo_occurrence_skipped` the reviewed tracking plan gives clients, with `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
