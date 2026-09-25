# FS - TODO - Recurring to-dos

_Parent task from the To-dos and Reminders board, written by Ines, Product Manager, To-dos and Reminders. Last edited 2026-09-18._

### About

---

A to-do with a due date can repeat on a schedule the member picks. When the member checks off or skips one occurrence, the next one appears with the next due date.

This parent states the shared rules once. Each subtask builds them in one client or in the engine, and everything ships dark behind the workspace flag `recurring_todos`. Desktop gets the feature through the web client, so it has no subtask of its own.

**References**

---

Flows

- `Recurring to-dos / Repeat picker`
- `Recurring to-dos / Custom interval`
- `Recurring to-dos / Occurrence menu`

### Requirements

---

1.  **iOS app**

---

`FE - iOS - TODO - Recurring to-dos`

2.  **Android app**

---

`FE - Android - TODO - Recurring to-dos`

3.  **Web client**

---

`FE - Web - TODO - Recurring to-dos`

4.  **Recurrence engine**

---

`BE - TODO - Recurrence engine`

### **Shared rules**

---

1.  **Repeat options**

---

Repeat sits on the to-do's detail sheet. A to-do without a due date shows it greyed out with the hint `Add a due date to repeat`.

| Option | Next due date |
|--------|---------------|
| Daily | The next day |
| Weekdays | The next weekday, Monday through Friday |
| Weekly | Same weekday next week |
| Monthly | Same day next month |
| Custom | Every N days, weeks or months, with N from 1 to 99 |

Monthly keeps to the day of the first due date. A series that starts on the 31st lands on the 30th in April and on the 31st again in May.

2.  **Ends**

---

- Never, the default
- On date, which stops the series after the last occurrence on or before that date
- After, which stops the series after a set number of occurrences, from 1 to 365

3.  **Occurrences**

---

Only one occurrence exists at a time. Checking it off creates the next one on the same page with the next due date. Assignee and reminder carry over, and the reminder keeps the same local time.

Skip this one sits in the to-do's menu. It moves the to-do to its next due date without marking it done, and it still counts toward an After limit.

4.  **Limit**

---

A workspace holds at most 500 repeating to-dos that have not ended. At the limit Repeat stays visible and opens a sheet that says `This workspace has 500 repeating to-dos. End one to add another.` Checked-off and ended series do not count.

5.  **Time zone**

---

Next due dates are worked out in the owner's time zone. When the to-do is reassigned, the next occurrence uses the new owner's zone. A teammate in another zone sees the owner's date with the zone shown.

6.  **Plans and flag**

---

Repeat is for Plus and Team workspaces. On Free it shows with a Plus badge and opens the upgrade sheet. All four subtasks ship behind `recurring_todos`, and Data turns it on once the three clients are out.

7.  **Tracking**

---

`todo_repeat_set` carries `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`. `todo_occurrence_skipped` fires on Skip this one. Both are in the tracking plan Yara reviewed on 2026-09-16.
