# FS - TODO - Recurring to-dos

### About

---

Members want to-dos that come back on a schedule. Repeating to-dos are the most requested to-do feature we have: 212 requests on the feedback board since January, and 38 Plus workspaces named it in the renewal survey as the reason they keep a second app for chores and routines. Today people copy a to-do by hand every week, or set a reminder far ahead and keep moving it.

This parent task holds the behavior every platform builds to, plus the rollout and the tracking. iOS, Android, Web and BE each deliver their part in a subtask. Desktop gets the feature through the web client, so it has no subtask of its own.

The work counts as a success when 10% of weekly active Plus and Team workspaces have at least one repeating to-do 8 weeks after the flag is on for everyone.

**References**

---

Brief

- `Recurring to-dos, PM brief` (Ines, 2026-09-08, with the answers from planning on 2026-09-10)

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

Any to-do with a due date can repeat. The member opens the to-do's detail sheet and taps Repeat. On a to-do without a due date, Repeat is greyed out with the hint `Add a due date to repeat`.

| Option | Next due date |
| --- | --- |
| Daily | The next day |
| Weekdays | The next weekday, Monday through Friday |
| Weekly | Same weekday next week |
| Monthly | Same day next month |
| Custom | Every N days, weeks or months, with N from 1 to 99 |

Monthly keeps to the day of the first due date. A series that starts on the 31st lands on the 30th in April and on the 31st again in May.

---

6.  **Ends**

---

Ends sits under Repeat and has three choices:

- Never, the default
- On date, which stops the series after the last occurrence on or before that date
- After, which stops the series after a set number of occurrences, from 1 to 365

---

7.  **Occurrences and Skip this one**

---

Only one occurrence exists at a time. When the member checks it off, the next one appears on the same page with the next due date. The assignee and the reminder carry over, and the reminder keeps the same local time.

Skip this one sits in the to-do's menu. It moves the to-do to its next due date without marking it done. A skipped occurrence still counts toward an After limit, so a series set to end after 5 occurrences ends after 5 whether each one was checked off or skipped.

---

8.  **Workspace limit**

---

A workspace can hold 500 repeating to-dos that have not ended. Checked-off and ended series do not count. When a workspace reaches the limit, Repeat stays visible but opens a sheet that says `This workspace has 500 repeating to-dos. End one to add another.`

---

9.  **Time zones**

---

Next due dates are worked out in the to-do owner's time zone. The Overdue chip and reminders follow the same rule, so all three agree for the owner. When the to-do is reassigned, the next occurrence uses the new owner's zone. A teammate in another zone sees the owner's date with the zone shown.

> The to-do owner is the assignee, or the creator when the to-do has no assignee. It is not the workspace Owner role.

---

10. **Plans**

---

Repeat is for Plus and Team workspaces. On Free it shows with a Plus badge and opens the upgrade sheet.

---

### **Rollout and tracking**

---

11. **Flag and rollout**

---

Everything ships behind the workspace flag `recurring_todos`, and iOS, Android, Web and BE all ship dark first. Data turns the flag on for a sample of Plus and Team workspaces once all three clients are out, then widens it from there.

**Checklist**

- [ ] iOS, Android, Web and BE have all shipped with `recurring_todos` off
- [ ] Data turns `recurring_todos` on for a sample of Plus and Team workspaces only after iOS, Android and Web are all out
- [ ] The 10% success target is read 8 weeks after the flag is on for everyone

---

12. **Tracking**

---

Data wants two events. Yara reviews the tracking plan before client work starts, so the plan is the first thing to close.

| Event | Fires on | Event-specific property |
| --- | --- | --- |
| `todo_repeat_set` | Setting a repeat | `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom` |
| `todo_occurrence_skipped` | Skip this one | None |

Both events carry the standard properties `workspace_id`, `user_id`, `platform`, `app_version` and `plan`.

**Checklist**

- [ ] Yara has reviewed the tracking plan with both events before iOS, Android or Web work starts
- [ ] `todo_repeat_set` sends `repeat` as one of `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [ ] `todo_occurrence_skipped` fires once for each Skip this one

---

### **Out of scope**

---

- Repeating a whole page or a database row
- Repeating from the date the to-do was checked off, as in every 3 days after I finish
- A different time for each weekday
- Any Support console change

> Whether a series shows its past occurrences in the to-do's activity is still open. It is not needed for the first release, and Ines decides after the flag reaches everyone.
