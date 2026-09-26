```markdown
# FE - Android - TODO - Recurring to-dos

### About

---

This subtask builds recurring to-dos in the Android app on phones and tablets, as part of `FS - TODO - Recurring to-dos`. A member sets a to-do with a due date to repeat. When they check off or skip one occurrence, the next one appears with its next due date.

The parent task states the shared rules. The Android app gives the member the controls and shows the results. `BE - TODO - Recurrence engine` works out every next due date and is being built at the same time. The app shows the date the engine returns and never works one out on the device. Oskar's team ships this in Android 5.4.0 behind the workspace flag `recurring_todos`.

**Parent task**

---

- `FS - TODO - Recurring to-dos`

**Related tasks**

---

- `BE - TODO - Recurrence engine`

**References**

---

Flows

- `Recurring to-dos / Repeat picker`
- `Recurring to-dos / Custom interval`
- `Recurring to-dos / Occurrence menu`

### Requirements

---

### **Repeat setup**

---

1.  **Repeat on the detail sheet**

---

Repeat sits on the to-do's detail sheet, next to the due date the member already sets there. A to-do needs a due date before it can repeat, because the engine works out each next date from it.

**Checklist**

- [ ] Show Repeat on the detail sheet of every to-do, on phones and tablets
- [ ] Grey out Repeat on a to-do without a due date and show the hint `Add a due date to repeat`
- [ ] Offer Daily, Weekdays, Weekly, Monthly and Custom as repeat options

2.  **Custom interval and ends**

---

Custom covers any interval the preset options miss. Ends sets when the series stops.

**Checklist**

- [ ] Let the member set Custom to every N days, weeks or months, with N from 1 to 99
- [ ] Accept no Custom value below 1 or above 99
- [ ] Offer Never, On date and After under Ends, with Never selected by default
- [ ] Let the member pick the end date for On date
- [ ] Let the member set After to a number of occurrences from 1 to 365, and accept no number outside that range

### **Occurrences**

---

3.  **Check off and Skip this one**

---

Only one occurrence of a series exists at a time, so the member sees one to-do for the series and never a list of future ones. Every next due date comes from the engine, including the Monthly case where a series that starts on the 31st lands on the 30th in April.

**Checklist**

- [ ] Show one occurrence of a series at a time
- [ ] After check off, show the next occurrence on the same page with the next due date the engine returns
- [ ] Carry the assignee and the reminder over to the next occurrence
- [ ] Show Skip this one in the menu of a repeating to-do
- [ ] On Skip this one, move the to-do to the next due date the engine returns without marking it done
- [ ] Show no next occurrence when the engine reports that the series has ended
- [ ] Never work out a next due date on the device

4.  **Reminder on the next occurrence**

---

Android schedules reminders as local notifications on the device, from the UTC time reminders-service hands over. The reminder keeps the same local time on each occurrence.

**Checklist**

- [ ] Schedule the next occurrence's reminder as a local notification from the time reminders-service hands over
- [ ] Keep the reminder at the same local time as on the previous occurrence
- [ ] Do not fire the reminder of an occurrence that was checked off or skipped

### **Limit, plans and time zone**

---

5.  **Workspace limit and plan**

---

A workspace holds at most 500 repeating to-dos that have not ended. Repeat is for Plus and Team workspaces.

**Checklist**

- [ ] When the workspace is at the limit, keep Repeat visible and open a sheet that says `This workspace has 500 repeating to-dos. End one to add another.`
- [ ] Let Plus and Team workspaces use Repeat
- [ ] On Free, show Repeat with a Plus badge and open the upgrade sheet when the member taps it

6.  **Time zone**

---

Next due dates are worked out in the to-do owner's time zone, so a teammate in another zone sees the owner's date.

**Checklist**

- [ ] Show each occurrence's due date in the owner's time zone
- [ ] Show the zone beside the date when the viewer's zone differs from the owner's
- [ ] After the to-do is reassigned, show the date the engine returns in the new owner's zone

### **Release and tracking**

---

7.  **Flag, release and tracking**

---

All four subtasks ship dark. Data turns `recurring_todos` on once iOS, Android and Web are out.

**Checklist**

- [ ] Ship in Android 5.4.0 behind `recurring_todos`, with Repeat hidden while the flag is off
- [ ] Send `todo_repeat_set` with `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [ ] Send `todo_occurrence_skipped` on Skip this one
- [ ] Send both events with `workspace_id`, `user_id`, `platform`, `app_version` and `plan`, with `user_id` hashed before it leaves the device
- [ ] Match both events to the tracking plan Yara reviewed on 2026-09-16
```

Export-equivalent path: `export/002 - task-android-recurring-todos.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality: meets every floor. Completeness 8, Clarity 9, Actionability 9, Accuracy 9, Relevance 9, Mechanism Depth 8. Completeness sits at the floor because of the open points below.

This is the Android subtask for 5.4.0, covering phones and tablets. It follows your split: the app shows the next due date the engine returns and never works one out on the device. I wrote the shared rules as Android checks with the parent's values and copy, so QA can test the subtask without opening the parent.

**Items I added that you didn't state (remove any you don't want):**
- The reminder of a to-do that was checked off or skipped does not fire
- Repeat stays hidden while `recurring_todos` is off
- The app refuses Custom and After values outside the parent's ranges

**Still open from my first question, so the subtask doesn't cover them:**
- What a member sees after checking off a repeating to-do with no connection. The app can't show a date from the engine while offline
- Whether a guest with edit access, or a member who isn't the to-do owner, can set Repeat
- Figma links for the three flows. They're named as plain text for now
- Links for the parent and the engine task. These are also plain text

Answer any of these and I'll update the same file.