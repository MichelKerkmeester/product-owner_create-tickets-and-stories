# FS - TODO - Recurring to-dos

### About

---

Members can't set a to-do to repeat. It is our most requested to-do feature, with 212 requests on the feedback board since January. 38 Plus workspaces named it in the renewal survey as the reason they keep a second app for chores and routines. Today people copy a to-do by hand every week, or they set a reminder far ahead and keep moving it.

This parent task makes a to-do with a due date repeat on a schedule the member picks, one occurrence at a time. iOS, Android, Web and BE each deliver their part in a subtask that the platform lead writes. The shared rules below are stated once so every subtask can point here instead of restating them.

**References**

---

Flows

- `Recurring to-dos / Repeat picker`
- `Recurring to-dos / Custom interval`
- `Recurring to-dos / Occurrence menu`

Anouk has these frames ready for review. They have not been signed off yet.

Page

- `Recurring to-dos, PM brief` by Ines, posted 2026-09-08, with answers from the 2026-09-10 planning session

### Requirements

---

### **Subtasks**

---

1.  **iOS**

---

`FE - iOS - TODO - Recurring to-dos`

Covers the Repeat and Ends pickers, the Custom interval, Skip this one and the repeat icon on the to-do row. Target release is iOS 5.4.0.

2.  **Android**

---

`FE - Android - TODO - Recurring to-dos`

Same scope as iOS. Target release is Android 5.4.0.

3.  **Web**

---

`FE - Web - TODO - Recurring to-dos`

Same scope as iOS. Desktop gets it through the web client, so there is no Desktop subtask and no Desktop release. Web ships dark before iOS and Android 5.4.0.

4.  **BE**

---

`BE - TODO - Recurring to-dos`

Covers the next occurrence on check-off and on skip, Ends, the 500 limit and handing the next reminder to reminders-service. BE ships dark before iOS and Android 5.4.0.

### **Shared rules**

---

5.  **When Repeat is available**

---

Only a to-do with a due date can repeat, because every repeat option works out the next due date from the current one. Repeat sits on the to-do's detail sheet and belongs to Plus and Team workspaces.

**Checklist**

- [ ] Repeat opens from the to-do's detail sheet
- [ ] A to-do without a due date shows Repeat greyed out with the hint `Add a due date to repeat`
- [ ] Plus and Team workspaces can set Repeat
- [ ] On Free, Repeat shows with a Plus badge and opens the upgrade sheet

> Open for iOS and Android: the context page says Web is the only surface for billing changes. Ines still has to decide what the upgrade sheet does on the mobile apps.

6.  **Repeat options**

---

Each option sets how the next due date is worked out from the current one.

| Option | Next due date |
| --- | --- |
| Daily | The next day |
| Weekdays | The next weekday, Monday through Friday |
| Weekly | Same weekday next week |
| Monthly | Same day next month |
| Custom | Every N days, weeks or months, with N from 1 to 99 |

Monthly keeps the day of the first due date rather than the day of the latest occurrence. Otherwise one short month would shift the series for good.

**Checklist**

- [ ] Each option gives the next due date shown in the table
- [ ] Custom accepts N from 1 to 99 and nothing outside that range
- [ ] A Monthly series that starts on the 31st lands on the 30th in April and on the 31st again in May

7.  **Ends**

---

Ends sits under Repeat and decides when a series stops.

**Checklist**

- [ ] Ends has three choices, Never, On date and After, with Never as the default
- [ ] On date stops the series after the last occurrence on or before that date
- [ ] After stops the series after a set number of occurrences, from 1 to 365
- [ ] A skipped occurrence counts toward an After limit

8.  **Occurrences, check-off and skip**

---

Only one occurrence of a series exists at a time. Checking off an occurrence makes the next one. Skip this one moves the schedule on without recording the to-do as done.

**Checklist**

- [ ] Checking off an occurrence makes the next one appear on the same page with the next due date
- [ ] The next occurrence keeps the assignee and the reminder
- [ ] The carried-over reminder keeps the same local time
- [ ] The to-do's menu has Skip this one
- [ ] Skip this one moves the to-do to its next due date without marking it done
- [ ] A repeating to-do shows the repeat icon on its row

9.  **Workspace limit**

---

A workspace can hold 500 repeating to-dos that have not ended. Checked-off and ended series do not count toward the limit.

**Checklist**

- [ ] At 500, Repeat stays visible but opens a sheet that says `This workspace has 500 repeating to-dos. End one to add another.`
- [ ] Ending a series frees a place under the limit
- [ ] Checked-off and ended series are left out of the count

10.  **Time zones**

---

Next due dates follow the owner's time zone, which is the same rule the Overdue chip and reminders already follow. The owner is the to-do owner, meaning the assignee, or the creator when there is no assignee.

**Checklist**

- [ ] The next due date is worked out in the owner's time zone
- [ ] After a reassignment, the next occurrence uses the new owner's time zone
- [ ] A teammate in another zone sees the owner's date with the zone shown

11.  **Tracking**

---

Data needs two events to measure adoption. Yara reviews the tracking plan before client work starts, so no client subtask starts before that review.

**Checklist**

- [ ] `todo_repeat_set` fires when a member sets Repeat, with `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [ ] `todo_occurrence_skipped` fires on Skip this one
- [ ] Both events carry `workspace_id`, `user_id`, `platform`, `app_version` and `plan`
- [ ] Yara has reviewed the tracking plan before client work starts

12.  **Rollout**

---

Everything ships behind the workspace flag `recurring_todos`, so each part can ship dark before members see anything. Once all three clients are out, Data turns the flag on for a sample of Plus and Team workspaces and widens it from there.

We call it working when 10% of weekly active Plus and Team workspaces have at least one repeating to-do 8 weeks after the flag is on for everyone.

**Checklist**

- [ ] iOS, Android, Web and BE all ship behind `recurring_todos`, off by default
- [ ] Web and BE ship dark before iOS and Android 5.4.0
- [ ] The flag stays off until iOS 5.4.0, Android 5.4.0 and the Web release are all out

### **Out of scope**

---

- Repeating a whole page or a database row
- Repeating from the date the to-do was checked off, as in every 3 days after I finish
- A different time for each weekday
- Any Support console change
- Showing past occurrences of a series in the to-do's activity. It is not needed for the first release, and Ines will decide after the flag reaches everyone
