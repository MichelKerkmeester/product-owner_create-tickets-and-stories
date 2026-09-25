# FS - TODO - Recurring to-dos

### About

---

Members who want a to-do to come back every week copy it by hand, or set a reminder far ahead and keep moving it. Repeating to-dos are the most requested to-do feature: the feedback board holds 212 requests since January, and 38 Plus workspaces named it in the renewal survey as the reason they keep a second app for chores and routines.

This parent task holds the shared rules for every surface, numbered 1 to 5 below so each subtask can point at them instead of restating them. The platform leads write their own subtasks from it. Desktop gets the feature through the web client, with no Desktop release. The source is Ines's PM brief from 2026-09-08, with the answers from the 2026-09-10 planning session folded in. Anouk has the three design frames ready for review.

The feature counts as working when 10% of weekly active Plus and Team workspaces have at least one repeating to-do 8 weeks after the `recurring_todos` flag is on for everyone.

Out of scope: repeating a whole page or a database row, repeating from the date a to-do was checked off (as in every 3 days after I finish), a different time for each weekday and any Support console change.

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

A to-do can repeat only when it has a due date, because every Repeat option counts forward from that date. Repeat sits in the to-do's detail sheet and Ends sits under it, as `Recurring to-dos / Repeat picker` and `Recurring to-dos / Custom interval` show.

| Option | Next due date |
| --- | --- |
| Daily | The next day |
| Weekdays | The next weekday, Monday through Friday |
| Weekly | Same weekday next week |
| Monthly | Same day next month |
| Custom | Every N days, weeks or months, with N from 1 to 99 |

**Checklist**

- [ ] A to-do without a due date shows Repeat greyed out with the hint `Add a due date to repeat`
- [ ] Each Repeat option sets the next due date the table gives
- [ ] Monthly keeps to the day of the first due date, so a series that starts on the 31st lands on the 30th in April and on the 31st again in May
- [ ] Ends has Never, On date and After, and Never is the default
- [ ] On date stops the series after the last occurrence on or before that date
- [ ] After stops the series after a set number of occurrences, from 1 to 365

2.  **Occurrences, Skip this one and the repeat icon**

---

Only one occurrence of a series exists at a time, so a page never fills up with future copies of the same to-do. Skip this one sits in the to-do's menu, as `Recurring to-dos / Occurrence menu` shows.

**Checklist**

- [ ] Checking off an occurrence makes the next one appear on the same page with the next due date
- [ ] The next occurrence keeps the assignee and the reminder
- [ ] Skip this one moves the to-do to its next due date without marking it done
- [ ] A skipped occurrence counts toward an After limit
- [ ] A repeating to-do shows the repeat icon on its row

3.  **Reminders and time zones**

---

Next due dates follow the rule the Overdue chip and reminders already follow, so a repeating to-do never disagrees with them about which day it is due. Each surface delivers the next occurrence's reminder the way it delivers any reminder today.

**Checklist**

- [ ] Next due dates are worked out in the to-do owner's time zone
- [ ] After a reassign, the next occurrence uses the new to-do owner's time zone
- [ ] A teammate in another time zone sees the to-do owner's date with the zone shown
- [ ] The next occurrence's reminder keeps the same local time and reaches reminders-service, which hands it to every device of the to-do owner
- [ ] On iOS and Android the next occurrence's reminder arrives as a local notification
- [ ] On Web and Desktop it shows in the app only, while the app is open, as every reminder there does

4.  **Plans and the workspace limit**

---

Repeat is for Plus and Team workspaces. The limit caps any one workspace at 500 series that are still running.

**Checklist**

- [ ] Repeat works on Plus and Team workspaces
- [ ] On Free, Repeat shows with a Plus badge and opens the upgrade sheet
- [ ] A workspace holds up to 500 repeating to-dos that have not ended, and checked-off and ended series do not count toward the 500
- [ ] At 500, Repeat stays visible and opens a sheet that says `This workspace has 500 repeating to-dos. End one to add another.`

5.  **Flag, release order and tracking**

---

Everything ships dark behind the workspace flag `recurring_todos`. Web and BE ship dark first, and iOS and Android aim for the 5.4.0 release. Once all three clients are out, Data turns the flag on for a sample of Plus and Team workspaces and widens it from there.

**Checklist**

- [ ] No part of the feature shows in a workspace where `recurring_todos` is off
- [ ] Web and BE are live behind the flag before iOS and Android 5.4.0
- [ ] Yara has reviewed the tracking plan before any client subtask starts
- [ ] `todo_repeat_set` carries `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [ ] `todo_occurrence_skipped` fires on Skip this one
- [ ] Both events carry `workspace_id`, `user_id`, `platform`, `app_version` and `plan`, as every Loomlist event does

> The brief does not say which surface sends each event. The tracking plan settles that before the client subtasks start.

> Whether a series shows its past occurrences in the to-do's activity is not part of the first release. Ines decides after the flag reaches everyone.

### **Subtasks**

---

6.  **iOS**

---

`FE - iOS - TODO - Recurring to-dos`

The Repeat and Ends pickers, the Custom interval, Skip this one and the repeat icon on the to-do row, built against shared rules 1 to 5. Aims for 5.4.0.

7.  **Android**

---

`FE - Android - TODO - Recurring to-dos`

Same scope as iOS, built against shared rules 1 to 5. Aims for 5.4.0.

8.  **Web**

---

`FE - Web - TODO - Recurring to-dos`

Same scope as iOS, built against shared rules 1 to 5. Ships dark before 5.4.0, and Desktop members get it through the web client, so every check also passes in the Desktop app.

9.  **BE**

---

`BE - TODO - Recurring to-dos`

The next occurrence on check-off and on Skip this one, Ends, the 500 limit and handing the next reminder to reminders-service, built against shared rules 1 to 5. Ships dark before 5.4.0.
