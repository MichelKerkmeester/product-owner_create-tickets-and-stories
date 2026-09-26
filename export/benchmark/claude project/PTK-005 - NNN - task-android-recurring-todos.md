# FE - Android - TODO - Recurring to-dos

## About

---

The Android app gets recurring to-dos per the parent's shared rules: members make dated to-dos repeat, check off or skip occurrences and see the next.

Android matches iOS and Web due dates, so switching devices shows one schedule. It ships dark behind the workspace flag `recurring_todos`.

**References**

---

Flows

- `Recurring to-dos / Repeat picker`
- `Recurring to-dos / Custom interval`
- `Recurring to-dos / Occurrence menu`

**Parent task**

---

- `FS - TODO - Recurring to-dos`

**Related tasks**

---

- `FE - iOS - TODO - Recurring to-dos`
- `FE - Web - TODO - Recurring to-dos`
- `BE - TODO - Recurrence engine`

### Requirements

---

### **Repeat picker**

---

1.  **Set a repeat schedule**

---

Next due dates follow the parent task's Repeat options table.

**Checklist**

- [] Show Repeat on the detail sheet: Daily, Weekdays, Weekly, Monthly, Custom
- [] With no due date, grey out Repeat with the hint `Add a due date to repeat`
- [] Custom repeats every N days, weeks or months, N from 1 to 99 only
- [] Weekdays means Monday to Friday, whatever the locale's first weekday
- [] Monthly from the 31st lands on the 30th in April and the 31st in May
- [] Dates follow the member's locale, and new copy ships in en-US, de-DE, fr-FR, es-ES, ja-JP and pt-BR, with en-US fallback

---

2.  **Choose when the series ends**

---

**Checklist**

- [] Default Ends to Never
- [] On date stops after the last occurrence on or before that date
- [] After stops after 1 to 365 occurrences, rejecting other values

---

### **Occurrences**

---

3.  **Check off an occurrence**

---

One occurrence at a time keeps the list free of future copies.

**Checklist**

- [] Show one open occurrence per series at a time
- [] Checking one off creates the next on the same page with the next due date
- [] Carry the assignee to the next occurrence
- [] Carry the reminder at the same local time, as a local notification on the owner's Android devices
- [] Create no next occurrence once On date or After ends the series

---

4.  **Skip this one**

---

**Checklist**

- [] Only repeating to-dos' menu shows Skip this one
- [] Skip moves the to-do to its next due date without marking it done
- [] A skip counts toward an After limit, so skipping the last allowed occurrence ends the series

---

### **Time zone**

---

5.  **Use the owner's time zone**

---

The owner is the assignee, or else the creator.

**Checklist**

- [] Work out next due dates in the owner's zone, not the device's
- [] After reassignment, use the new owner's zone
- [] A teammate in another zone sees the owner's date with the zone shown

---

### **Limit, plans and flag**

---

6.  **Workspace limit**

---

A workspace holds at most 500 unended repeating to-dos.

**Checklist**

- [] At the limit, keep Repeat visible and open a sheet saying `This workspace has 500 repeating to-dos. End one to add another.`
- [] Leave checked-off and ended series out of the count

---

7.  **Plans and flag**

---

Repeat is for Plus and Team, hidden until Data turns on `recurring_todos` once all three clients are out.

**Checklist**

- [] On Plus and Team, Repeat opens the picker
- [] On Free, show Repeat with a Plus badge, opening the upgrade sheet on tap
- [] With `recurring_todos` off, show no Repeat or Skip this one

---

### **Tracking**

---

8.  **Send the tracking events**

---

Both events are in the tracking plan Yara reviewed on 2026-09-16.

**Checklist**

- [] Send `todo_repeat_set` with `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [] Send `todo_occurrence_skipped` on Skip this one
- [] Both carry `workspace_id`, a hashed `user_id`, `platform`, `app_version` and `plan`
