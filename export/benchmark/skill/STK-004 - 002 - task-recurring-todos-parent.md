# FS - TODO - Recurring to-dos

## About

---

Repeating to-dos are the most requested to-do feature. The feedback board holds 212 requests since January, and 38 Plus workspaces named it in the renewal survey as the reason they keep a second app for chores and routines. Today members copy a to-do by hand every week, or set a reminder far ahead and keep moving it.

A to-do with a due date can repeat. This parent states the rules every platform shares once, so the four platform subtasks point here instead of restating them. The feature is working when 10% of weekly active Plus and Team workspaces have at least one repeating to-do 8 weeks after the flag is on for everyone.

**References**

---

Flows

- `Recurring to-dos / Repeat picker`
- `Recurring to-dos / Custom interval`
- `Recurring to-dos / Occurrence menu`

Figma links are not supplied yet. Anouk has the frames ready for review.

### Requirements

---

1.  **Subtasks**

---

Each platform lead writes the subtask from this parent. Each subtask points to the shared rules in this parent rather than restating them.

- `FE - iOS - TODO - Recurring to-dos`
- `FE - Android - TODO - Recurring to-dos`
- `FE - Web - TODO - Recurring to-dos`
- `BE - TODO - Recurring to-dos`

---

2.  **Repeat options and next due date**

---

Repeat opens from the to-do's detail sheet. Each option sets the next due date as follows.

| Option | Next due date |
| --- | --- |
| Daily | The next day |
| Weekdays | The next weekday, Monday through Friday |
| Weekly | Same weekday next week |
| Monthly | Same day next month |
| Custom | Every N days, weeks or months, with N from 1 to 99 |

**Checklist**

- [] A to-do with no due date shows Repeat greyed out with the hint `Add a due date to repeat`
- [] Monthly keeps the day of the first due date, so a series starting on the 31st lands on the 30th in April and on the 31st again in May
- [] Custom accepts N from 1 to 99 for days, weeks or months

---

3.  **Ends and skip**

---

Ends sits under Repeat with three choices. Never is the default. On date stops the series after the last occurrence on or before that date. After stops it after a set number of occurrences.

**Checklist**

- [] Ends offers Never, On date and After, with Never as the default
- [] After accepts 1 to 365 occurrences
- [] Skip this one moves the to-do to its next due date without marking it done
- [] A skipped occurrence counts toward an After limit

---

4.  **Occurrences and reminders**

---

Only one occurrence exists at a time. Checking off a repeating to-do shows the next occurrence on the same page, with the assignee and the reminder carried over.

**Checklist**

- [] Checking off a repeating to-do creates the next occurrence with the next due date
- [] The next occurrence keeps the assignee and the reminder of the one checked off
- [] Reminders on iOS and Android schedule as local notifications
- [] Reminders on Web and Desktop show in the app only, as a banner and a badge on the To-dos view, and only while the app is open

> Open: the brief says a repeated reminder keeps the same local time. The Loomlist context says reminders-service stores the UTC time each reminder is due. Across a daylight saving change these two rules give different UTC times, so the rule is not settled. The reminder time after a daylight saving change stays out of the checklist until the decision owner settles it, and that owner is not yet named.

---

5.  **Limits, plans and time zones**

---

**Checklist**

- [] A workspace holds up to 500 repeating to-dos that have not ended, and checked-off or ended series do not count
- [] At 500, Repeat stays visible and opens a sheet that reads `This workspace has 500 repeating to-dos. End one to add another.`
- [] Repeat is for Plus and Team workspaces, and on Free it shows with a Plus badge and opens the upgrade sheet
- [] Next due dates use the owner's time zone, the same rule the Overdue chip and reminders follow
- [] A reassigned to-do's next occurrence uses the new owner's time zone
- [] A teammate in another time zone sees the owner's date with the zone shown

---

6.  **Rollout**

---

**Checklist**

- [] Everything ships behind the workspace flag `recurring_todos`
- [] Web and BE ship with the flag off before the iOS and Android 5.4.0 release
- [] iOS and Android target the 5.4.0 release
- [] Data turns the flag on for a sample of Plus and Team workspaces once iOS, Android and Web are all out, then widens it

---

7.  **Tracking**

---

Yara reviews the tracking plan before client work starts.

**Checklist**

- [] `todo_repeat_set` carries `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [] `todo_occurrence_skipped` fires on Skip this one
- [] Both events carry `workspace_id`, `user_id`, `platform`, `app_version` and `plan`

---

8.  **Out of scope**

---

- Repeating a whole page or a database row
- Repeating from the check-off date, such as every 3 days after the to-do is finished
- A different time for each weekday
- Any Support console change
- Past occurrences in the to-do's activity, not needed for the first release and decided by Ines after the flag reaches everyone
