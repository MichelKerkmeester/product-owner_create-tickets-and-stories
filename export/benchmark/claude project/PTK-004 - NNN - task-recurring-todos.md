# FS - TODO - Recurring to-dos

## About

---

Repeating to-dos are the most requested to-do feature, with 212 feedback board requests since January. 38 Plus workspaces named it in the renewal survey as why they keep a second app for chores and routines. Today people copy a to-do by hand each week or keep moving a reminder.

This parent holds the shared behavior, rollout and tracking for the iOS, Android, Web and BE subtasks, and Desktop gets it through the web client.

**References**

---

Brief

- `Recurring to-dos, PM brief` (Ines, 2026-09-08, with planning answers from 2026-09-10)

Flows

- `Recurring to-dos / Repeat picker`
- `Recurring to-dos / Custom interval`
- `Recurring to-dos / Occurrence menu`

Anouk has these frames ready for review.

### Requirements

---

### **Subtasks**

---

1.  **iOS**

---

- `FE - iOS - TODO - Recurring to-dos`

2.  **Android**

---

- `FE - Android - TODO - Recurring to-dos`

3.  **Web**

---

- `FE - Web - TODO - Recurring to-dos`

4.  **BE**

---

- `BE - TODO - Recurring to-dos`

---

### **Shared behavior**

---

5.  **Setting a repeat**

---

Any to-do with a due date can repeat, from Repeat in its detail sheet. Without a due date, Repeat is greyed out with the hint `Add a due date to repeat`.

| Option | Next due date |
| --- | --- |
| Daily | The next day |
| Weekdays | The next weekday, Monday through Friday |
| Weekly | Same weekday next week |
| Monthly | Same day next month |
| Custom | Every N days, weeks or months, with N from 1 to 99 |

Monthly keeps the first due date's day, so a series from the 31st lands on the 30th in April and the 31st in May.

---

6.  **Ends**

---

Ends sits under Repeat:

- Never, the default
- On date, ending with the last occurrence on or before that date
- After, ending after 1 to 365 occurrences

---

7.  **Occurrences and Skip this one**

---

One occurrence exists at a time, and checking it off creates the next on the same page, keeping the assignee and the reminder's local time.

Skip this one, in the to-do's menu, moves it to the next due date without marking it done. A skip still counts toward an After limit, so an After 5 series ends after 5 either way.

---

8.  **Workspace limit**

---

A workspace can hold 500 unended repeating to-dos, not counting checked-off or ended series. At the limit, Repeat stays visible but opens the sheet `This workspace has 500 repeating to-dos. End one to add another.`

---

9.  **Time zones**

---

Next due dates use the to-do owner's time zone, like the Overdue chip and reminders, and the new owner's zone after a reassignment. Teammates in other zones see the owner's date and zone.

> The to-do owner is the assignee, or the creator when there is none, not the workspace Owner role.

---

10. **Plans**

---

Repeat is for Plus and Team. On Free it shows a Plus badge and opens the upgrade sheet.

---

### **Rollout and tracking**

---

11. **Flag and rollout**

---

Everything ships dark behind the workspace flag `recurring_todos`, and Data widens it from the first sample.

**Checklist**

- [] iOS, Android, Web and BE have all shipped with `recurring_todos` off
- [] Data turns `recurring_todos` on for a sample of Plus and Team workspaces only once iOS, Android and Web are out
- [] Success, 10% of weekly active Plus and Team workspaces holding a repeating to-do, is read 8 weeks after the flag is on for everyone

---

12. **Tracking**

---

| Event | Fires on | Event-specific property |
| --- | --- | --- |
| `todo_repeat_set` | Setting a repeat | `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom` |
| `todo_occurrence_skipped` | Skip this one | None |

Both carry the standard properties `workspace_id`, `user_id`, `platform`, `app_version` and `plan`.

**Checklist**

- [] Yara has reviewed the tracking plan with both events before iOS, Android or Web work starts
- [] `todo_repeat_set` sends `repeat` as one of `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [] `todo_occurrence_skipped` fires once for each Skip this one

---

### **Out of scope**

---

- Repeating a whole page or a database row
- Repeating from the check-off date, as in every 3 days after I finish
- A different time for each weekday
- Any Support console change

> Whether a series shows past occurrences in the to-do's activity is still open and not needed for the first release. Ines decides after the flag reaches everyone.
