# FS - TODO - Recurring to-dos

### About

---

Members copy a weekly to-do by hand, or set a far-off reminder and keep moving it. Repeating to-dos are the most requested to-do feature: 212 feedback board requests since January, and 38 Plus workspaces named it in the renewal survey as why they keep a second app for chores and routines.

Success is 10% of weekly active Plus and Team workspaces with at least one repeating to-do 8 weeks after `recurring_todos` is on for everyone. Platform leads write their subtasks from shared rules 1 to 5, and Desktop gets it through the web client with no Desktop release.

Sources: Ines's 2026-09-08 PM brief and 2026-09-10 planning answers, and Anouk's three design frames await review. Out of scope: repeating a page or database row, repeating from check-off (every 3 days after I finish), per-weekday times and Support console changes.

**References**

---

Components

- `Recurring to-dos / Repeat picker`
- `Recurring to-dos / Custom interval`
- `Recurring to-dos / Occurrence menu`

### Requirements

---

### **Shared rules**

---

1.  **Repeat and Ends**

---

Every option counts forward from the due date. Repeat sits in the detail sheet with Ends below, as `Recurring to-dos / Repeat picker` and `Recurring to-dos / Custom interval` show.

| Option | Next due date |
| --- | --- |
| Daily | Next day |
| Weekdays | Next weekday, Monday to Friday |
| Weekly | Same weekday next week |
| Monthly | Same day next month |
| Custom | Every N days, weeks or months, N from 1 to 99 |

**Checklist**

- [ ] Without a due date, Repeat is greyed out with the hint `Add a due date to repeat`
- [ ] Each option sets the table's next due date
- [ ] Monthly keeps the first due date's day, so a 31st series lands on the 30th in April and the 31st in May
- [ ] Ends offers Never, the default, On date and After
- [ ] On date stops after the last occurrence on or before that date
- [ ] After stops after 1 to 365 occurrences

2.  **Occurrences, Skip this one and the repeat icon**

---

One occurrence at a time keeps pages free of future copies. Skip this one is in the to-do's menu, as `Recurring to-dos / Occurrence menu` shows.

**Checklist**

- [ ] Checking one off shows the next on the same page with the next due date
- [ ] The next keeps the assignee and reminder
- [ ] Skip this one moves the to-do to its next due date without marking it done
- [ ] A skip counts toward an After limit
- [ ] Repeating to-dos show the repeat icon on their row

3.  **Reminders and time zones**

---

Due dates follow the Overdue chip and reminders' rule, so they never disagree.

**Checklist**

- [ ] Next due dates use the to-do owner's time zone
- [ ] After a reassign, the new owner's zone applies
- [ ] Teammates in other zones see the owner's date with the zone shown
- [ ] The next reminder keeps its local time and goes to reminders-service, which sends it to all the owner's devices
- [ ] On iOS and Android it arrives as a local notification
- [ ] On Web and Desktop it shows only in the open app, like every reminder there

4.  **Plans and the workspace limit**

---

**Checklist**

- [ ] Repeat works on Plus and Team
- [ ] On Free, Repeat shows a Plus badge and opens the upgrade sheet
- [ ] A workspace holds up to 500 unended repeating to-dos, not counting checked-off and ended series
- [ ] At 500, Repeat stays visible and opens a sheet saying `This workspace has 500 repeating to-dos. End one to add another.`

5.  **Flag, release order and tracking**

---

Everything ships dark behind the workspace flag `recurring_todos`, and once all three clients are out, Data turns it on for a sample of Plus and Team workspaces, then widens it.

**Checklist**

- [ ] Nothing shows where `recurring_todos` is off
- [ ] Web and BE are live behind the flag before iOS and Android 5.4.0
- [ ] Yara reviews the tracking plan before any client subtask starts
- [ ] `todo_repeat_set` carries `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [ ] `todo_occurrence_skipped` fires on Skip this one
- [ ] Both carry `workspace_id`, `user_id`, `platform`, `app_version` and `plan`, as every Loomlist event does

> The brief does not say which surface sends each event, and the tracking plan settles it before client subtasks start.

> Whether past occurrences show in the to-do's activity is outside the first release, and Ines decides after the flag reaches everyone.

### **Subtasks**

---

6.  **iOS**

---

`FE - iOS - TODO - Recurring to-dos`

Repeat and Ends pickers, Custom interval, Skip this one and the row's repeat icon, per rules 1 to 5. Aims for 5.4.0.

7.  **Android**

---

`FE - Android - TODO - Recurring to-dos`

Same scope as iOS, per rules 1 to 5. Aims for 5.4.0.

8.  **Web**

---

`FE - Web - TODO - Recurring to-dos`

Same scope as iOS, per rules 1 to 5. Ships dark before 5.4.0, and every check also passes in the Desktop app.

9.  **BE**

---

`BE - TODO - Recurring to-dos`

Next occurrence on check-off and Skip this one, Ends, the 500 limit and the reminder handoff to reminders-service, per rules 1 to 5. Ships dark before 5.4.0.
