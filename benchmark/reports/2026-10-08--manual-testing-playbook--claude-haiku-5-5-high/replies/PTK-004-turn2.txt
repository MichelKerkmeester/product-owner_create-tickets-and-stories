```markdown
# FS - TODO - Recurring to-dos

## About

---

Repeating to-dos are the most requested to-do feature. The feedback board holds 212 requests since January, and 38 Plus workspaces named the feature in the renewal survey as the reason they keep a second app for chores and routines. Today people copy a to-do by hand every week, or set a reminder far ahead and keep moving it.

This task holds the shared rules once, and each subtask points here. iOS and Android aim for release 5.4.0, and Web and BE ship dark before that. We call it working when 10% of weekly active Plus and Team workspaces have at least one repeating to-do 8 weeks after the flag is on for everyone.

**Subtasks**

---

- `FE - iOS - TODO - Recurring to-dos`
- `FE - Android - TODO - Recurring to-dos`
- `FE - Web - TODO - Recurring to-dos`
- `BE - TODO - Recurring to-dos`

**References**

---

Design frames, held by Anouk for review

- `Recurring to-dos / Repeat picker`
- `Recurring to-dos / Custom interval`
- `Recurring to-dos / Occurrence menu`

### Requirements

---

1.  **Repeat setting**

---

A to-do with a due date can repeat. The member opens the to-do's detail sheet and taps Repeat.

**Checklist**

- [] Repeat opens from the to-do's detail sheet
- [] A to-do without a due date shows Repeat greyed out with the hint `Add a due date to repeat`

---

2.  **Repeat options**

---

The next due date depends on the option the member picks.

| Option   | Next due date                                  |
| -------- | ---------------------------------------------- |
| Daily    | The next day                                   |
| Weekdays | The next weekday, Monday through Friday        |
| Weekly   | Same weekday next week                         |
| Monthly  | Same day next month                            |
| Custom   | Every N days, weeks or months, with N from 1 to 99 |

**Checklist**

- [] Monthly keeps the day of the first due date
- [] A series that starts on the 31st lands on the 30th in April and on the 31st again in May
- [] Custom accepts N from 1 to 99

---

3.  **Ends**

---

Ends sits under Repeat and sets when the series stops.

**Checklist**

- [] Ends offers Never, On date and After
- [] Never is the default
- [] On date stops the series after the last occurrence on or before that date
- [] After stops the series after a set number of occurrences, from 1 to 365
- [] A skipped occurrence counts toward an After limit

---

4.  **One occurrence at a time**

---

A series never holds two open occurrences.

**Checklist**

- [] Only one occurrence exists at a time
- [] Checking off an occurrence creates the next one on the same page, with the next due date
- [] The next occurrence keeps the assignee and the reminder
- [] The reminder keeps the same local time

---

5.  **Skip this one**

---

The member can move a repeating to-do forward without finishing it.

**Checklist**

- [] The to-do's menu offers Skip this one
- [] Skip this one moves the to-do to its next due date without marking it done

---

6.  **Limit**

---

The limit applies per workspace.

**Checklist**

- [] A workspace holds 500 repeating to-dos that have not ended
- [] At 500, Repeat stays visible and opens a sheet reading `This workspace has 500 repeating to-dos. End one to add another.`
- [] Checked-off and ended series do not count toward the 500

---

7.  **Time zones**

---

Dates follow the owner, as the Overdue chip and reminders already do.

**Checklist**

- [] Next due dates use the owner's time zone
- [] A reassigned to-do's next occurrence uses the new owner's time zone
- [] A teammate in another time zone sees the owner's date with the zone shown

---

8.  **Plans**

---

Repeat is a paid feature with a visible upgrade path on Free.

**Checklist**

- [] Repeat is for Plus and Team workspaces
- [] On Free, Repeat shows with a Plus badge and opens the upgrade sheet

---

9.  **Platform split**

---

Each platform subtask carries the scope in its row.

| Area    | Scope |
| ------- | ----- |
| iOS     | Repeat and Ends pickers, Custom interval, Skip this one, repeat icon on the to-do row |
| Android | As iOS |
| Web     | As iOS, with Desktop included through the web client |
| BE      | Next occurrence on check-off and skip, Ends, the 500 limit, handing the next reminder to reminders-service |

---

10.  **Rollout**

---

Everything ships dark behind one flag, and Data widens it once the clients are out.

**Checklist**

- [] Everything ships behind the workspace flag `recurring_todos`
- [] iOS and Android aim for release 5.4.0
- [] Web and BE ship with the flag off for everyone before 5.4.0
- [] Once iOS, Android and Web are out, Data turns the flag on for a sample of Plus and Team workspaces and widens it from there
- [] Desktop gets the feature through the web client, with no Desktop release

---

11.  **Tracking**

---

Data reviews the events before any client work starts.

**Checklist**

- [] Yara reviews the tracking plan before client work starts
- [] `todo_repeat_set` carries `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [] `todo_occurrence_skipped` fires on Skip this one

**Out of scope**

---

- Repeating a whole page or a database row
- Repeating from the date the to-do was checked off, for example every 3 days after it is finished
- A different time for each weekday
- Any Support console change

**Still open**

---

> Whether a series shows its past occurrences in the to-do's activity is open. It is not needed for the first release, and Ines decides after the flag reaches everyone.
```

Export-equivalent path: `export/NNN - task-recurring-todos.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality status: structure and source checks pass. I did not score the parent.

The parent carries the shared rules once. The four subtask titles use the board convention, and I wrote no subtask content. Three points from my last message are still unanswered, so the parent keeps the brief's wording for them:

- **iOS and Android upgrade sheet:** the brief says Free opens the upgrade sheet, and I did not specify what it does on mobile.
- **Event owner:** the parent lists both events without naming the subtask that fires them.
- **Reminder hand-off:** the BE row names the handoff to reminders-service, with no contract details.

The Still open note on past occurrences is an addition from the brief's own open item. Strike it if you want it left out.