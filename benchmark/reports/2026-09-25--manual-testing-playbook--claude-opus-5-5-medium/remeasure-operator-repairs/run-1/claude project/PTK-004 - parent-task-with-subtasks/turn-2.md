````markdown
# FS - TODO - Recurring to-dos

### About

---

Repeating to-dos are the most requested to-do feature in Loomlist. The feedback board holds 212 requests since January. In the renewal survey, 38 Plus workspaces named it as the reason they keep a second app for chores and routines. Today members copy a to-do by hand every week, or set a reminder far ahead and keep moving it.

This parent task lets a to-do with a due date repeat on a schedule, with one open occurrence at a time. It is based on Ines's PM brief of 2026-09-08 and the planning session on 2026-09-10. The shared rules below are stated once so that each platform lead can write their own subtask from them and point back here.

iOS and Android target the 5.4.0 release. Web and BE ship dark before that, behind the workspace flag `recurring_todos`. We count the feature as working when 10% of weekly active Plus and Team workspaces have at least one repeating to-do 8 weeks after the flag is on for everyone.

**References**

---

Flows

- `Recurring to-dos / Repeat picker`
- `Recurring to-dos / Custom interval`
- `Recurring to-dos / Occurrence menu`

### Requirements

---

### **Subtasks**

---

1.  **iOS**

---

- `FE - iOS - TODO - Recurring to-dos`

Repeat and Ends pickers, Custom interval, Skip this one and the repeat icon on the to-do row.

---

2.  **Android**

---

- `FE - Android - TODO - Recurring to-dos`

Same scope as iOS.

---

3.  **Web**

---

- `FE - Web - TODO - Recurring to-dos`

Same scope as iOS. Desktop gets it through the web client, with no Desktop release.

---

4.  **BE**

---

- `BE - TODO - Recurring to-dos`

Next occurrence on check-off and skip, Ends, the 500 limit and handing the next reminder to reminders-service.

---

### **Shared rules**

---

5.  **Set a repeat**

---

A member opens the to-do's detail sheet and taps Repeat. Each next due date is worked out from the current one, so Repeat needs a due date.

| Option | Next due date |
|--------|---------------|
| Daily | The next day |
| Weekdays | The next weekday, Monday through Friday |
| Weekly | Same weekday next week |
| Monthly | Same day next month |
| Custom | Every N days, weeks or months, with N from 1 to 99 |

**Checklist**

- [ ] Repeat sits in the to-do's detail sheet
- [ ] A to-do without a due date shows Repeat greyed out with the hint `Add a due date to repeat`
- [ ] Repeat offers Daily, Weekdays, Weekly, Monthly and Custom, each giving the next due date in the table
- [ ] Custom takes every N days, weeks or months, with N from 1 to 99
- [ ] Monthly keeps to the day of the first due date: a series that starts on the 31st lands on the 30th in April and on the 31st again in May
- [ ] A repeating to-do shows the repeat icon on its row

---

6.  **Choose when the series ends**

---

Ends sits under Repeat and defaults to Never.

**Checklist**

- [ ] Ends offers Never, On date and After, with Never as the default
- [ ] On date stops the series after the last occurrence on or before the chosen date
- [ ] After stops the series after a set number of occurrences, from 1 to 365
- [ ] No next occurrence appears once the series has ended

---

7.  **Check off or skip an occurrence**

---

Only one occurrence of a series exists at a time, so the page holds one open to-do per series and never a stack of future copies.

**Checklist**

- [ ] Checking off an occurrence makes the next one appear on the same page with the next due date
- [ ] The next occurrence keeps the assignee and the reminder, with the reminder at the same local time
- [ ] The to-do's menu has Skip this one, which moves the to-do to its next due date without marking it done
- [ ] A skipped occurrence counts toward an After limit

---

8.  **Workspace limit**

---

The cap covers every repeating to-do in the workspace that has not ended.

**Checklist**

- [ ] A workspace can hold 500 repeating to-dos that have not ended
- [ ] At 500, Repeat stays visible and opens a sheet that says `This workspace has 500 repeating to-dos. End one to add another.`
- [ ] Checked-off and ended series do not count toward the 500

---

9.  **Time zones**

---

Next due dates follow the same rule as the Overdue chip and reminders, so a series stays on the dates its owner sees. Owner here means the to-do owner, not the workspace Owner role.

**Checklist**

- [ ] Next due dates are worked out in the to-do owner's time zone
- [ ] After a reassignment, the next occurrence uses the new owner's time zone
- [ ] A teammate in another time zone sees the owner's date with the zone shown

---

10. **Plans, flag and release**

---

Everything ships dark first. Data turns the flag on for a sample of Plus and Team workspaces and widens it from there.

**Checklist**

- [ ] Repeat works in Plus and Team workspaces
- [ ] On Free, Repeat shows with a Plus badge and opens the upgrade sheet
- [ ] All repeat behavior stays behind the workspace flag `recurring_todos`
- [ ] iOS and Android ship dark in 5.4.0
- [ ] Web and BE ship dark before iOS and Android 5.4.0
- [ ] Data turns the flag on only after iOS, Android and Web are all out

---

11. **Tracking**

---

Data wants two events. New events go through a tracking plan that Yara reviews.

**Checklist**

- [ ] Yara reviews the tracking plan before any client work starts
- [ ] `todo_repeat_set` carries `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [ ] `todo_occurrence_skipped` fires on Skip this one

---

### **Out of scope**

---

- Repeating a whole page or a database row
- Repeating from the date the to-do was checked off, as in every 3 days after I finish
- A different time for each weekday
- Any Support console change

### **Open questions**

---

- Whether a series shows its past occurrences in the to-do's activity. It isn't needed for the first release, and Ines decides after the flag reaches everyone
- Which side sends each event, the client or BE
- What happens when a Monthly series that starts on the 29th, 30th or 31st reaches February
- Whether Custom every N months follows the Monthly day-of-month rule
- What happens to the next occurrence when a member unchecks the one they checked off
- What happens when a member removes the due date from a repeating to-do
- What happens to active series when a Plus or Team workspace moves down to Free
- Whether a guest with edit access can set Repeat
````

Export-equivalent path: `export/002 - task-recurring-todos.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality: passes. All six checks meet their minimum, and every checklist item describes something a tester can see.

Here's the parent task on its own. It lists the four subtasks by board title with a one-line scope each, and states the shared rules once so the subtasks can point back to them. The release plan is in About and in rule 10. iOS and Android target 5.4.0, and Web and BE ship dark before that.

**Things I added or decided that you should check:**
- **Open questions:** only the first one (past occurrences) comes from the brief. The other seven are my additions. Six are gaps the brief leaves open, and one is which side sends each tracking event. None of them appear in the checklists. Delete any you don't want the leads to see.
- **Two small inferences:**
  - "No next occurrence appears once the series has ended" in rule 6 follows from the brief's wording that Ends "stops the series".
  - The one-line reason under rule 5 (Repeat needs a due date because each next date is worked out from it) is my explanation of the brief's greyed-out rule, not a quote.
- **BE feature code:** the BE subtask uses TODO because you didn't pick between TODO and REM.
- **Tracking:** stays as a shared rule in this parent, so there's no fifth DATA subtask.
- **Links:** the brief gave no ClickUp or Figma links, so the subtasks and design frames are listed as plain text. Swap in links when you have them.