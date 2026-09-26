# FE - Android - TODO - Recurring to-dos

## About

---

The Android app gets recurring to-dos for phones and tablets per the parent's shared rules: members make dated to-dos repeat, check off or skip occurrences and see the next. Oskar's Mobile Platform team ships it in Android 5.4.0.

Android shows the due dates from BE's recurrence engine, built in parallel, so Android, iOS and Web show one schedule. It ships dark behind the workspace flag `recurring_todos`.

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

- `BE - TODO - Recurrence engine`
- `FE - iOS - TODO - Recurring to-dos`
- `FE - Web - TODO - Recurring to-dos`

### Requirements

---

### **Repeat picker**

---

1.  **Set a repeat schedule**

---

The member picks the schedule, and the recurrence engine decides the due dates.

**Checklist**

- [] Show Repeat on the detail sheet: Daily, Weekdays, Weekly, Monthly, Custom
- [] With no due date, grey out Repeat with the hint `Add a due date to repeat`
- [] Custom repeats every N days, weeks or months, N from 1 to 99 only
- [] Show the engine's next due date for each option, never one computed on device
- [] Dates follow the member's locale, and new copy ships in en-US, de-DE, fr-FR, es-ES, ja-JP and pt-BR, with en-US fallback
- [] The Repeat picker, Custom interval and occurrence menu work on phones and tablets

---

2.  **Choose when the series ends**

---

**Checklist**

- [] Default Ends to Never
- [] On date takes a date, stopping after the last occurrence on or before it
- [] After takes 1 to 365 occurrences, rejecting other values
- [] Once the engine ends a series via On date or After, show no next occurrence

---

### **Occurrences**

---

3.  **Check off an occurrence**

---

One occurrence at a time keeps the list free of future copies.

**Checklist**

- [] Show one open occurrence per series at a time
- [] Checking one off shows the next on the same page, with the engine's due date
- [] Carry the assignee to the next occurrence
- [] Carry the reminder at the same local time, as a local notification on the owner's Android devices

---

4.  **Skip this one**

---

**Checklist**

- [] Only repeating to-dos' menu shows Skip this one
- [] Skip moves the to-do to the engine's next due date without marking it done
- [] A skip counts toward an After limit, so skipping the last allowed occurrence ends the series

---

### **Time zone**

---

5.  **Show dates in the owner's time zone**

---

The engine uses the owner's time zone, the owner being the assignee, or else the creator.

**Checklist**

- [] Show the owner's due date as the engine returns it, unconverted to the device zone
- [] After reassignment, show the date the engine returns for the new owner
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
