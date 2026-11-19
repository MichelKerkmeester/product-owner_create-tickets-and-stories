# FE - Android - TODO - Recurring to-dos

### About

---

This subtask builds recurring to-dos in the Android app, following the shared rules in the parent task. A member on Android can make a to-do with a due date repeat, check off or skip one occurrence and see the next one appear with the next due date.

Android must show the same series and the same due dates as iOS and Web, so a member who switches devices sees one schedule, not two. Everything ships dark behind the workspace flag `recurring_todos`.

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

Repeat sits on the to-do's detail sheet and only works once the to-do has a due date. The next due date for each option follows the Repeat options table in the parent task.

**Checklist**

- [ ] Show Repeat on the to-do's detail sheet with the options Daily, Weekdays, Weekly, Monthly and Custom
- [ ] On a to-do with no due date, show Repeat greyed out with the hint `Add a due date to repeat`
- [ ] Custom repeats every N days, weeks or months, with N from 1 to 99, and accepts no value outside that range
- [ ] Weekdays lands on Monday through Friday only, whatever day the member's locale starts the week on
- [ ] A Monthly series that starts on the 31st lands on the 30th in April and on the 31st again in May
- [ ] Show dates in the member's locale and the new copy in en-US, de-DE, fr-FR, es-ES, ja-JP and pt-BR, with en-US as the fallback for a missing string

---

2.  **Choose when the series ends**

---

Ends controls when a series stops. It offers Never, On date and After, and Never is the default.

**Checklist**

- [ ] Default Ends to Never
- [ ] On date stops the series after the last occurrence on or before the chosen date
- [ ] After stops the series after a set number of occurrences, from 1 to 365, and accepts no value outside that range

---

### **Occurrences**

---

3.  **Check off an occurrence**

---

Only one occurrence exists at a time, so the member's list never fills with future copies of the same to-do.

**Checklist**

- [ ] Show only one open occurrence of a series at a time
- [ ] Checking off an occurrence creates the next one on the same page with the next due date
- [ ] Carry the assignee over to the next occurrence
- [ ] Carry the reminder over at the same local time, and schedule it as a local notification for the next occurrence on the to-do owner's Android devices
- [ ] Create no next occurrence once the series has ended through On date or After

---

4.  **Skip this one**

---

Skip this one lets a member pass on an occurrence without marking it done.

**Checklist**

- [ ] Show Skip this one in the to-do's menu for repeating to-dos only
- [ ] Skip this one moves the to-do to its next due date without marking it done
- [ ] A skipped occurrence counts toward an After limit, so skipping the last allowed occurrence ends the series

---

### **Time zone**

---

5.  **Use the owner's time zone**

---

Next due dates follow the to-do owner's time zone. The to-do owner is the assignee, or the creator when the to-do has no assignee.

**Checklist**

- [ ] Work out next due dates in the owner's time zone, not the viewer's device zone
- [ ] After a reassignment, the next occurrence uses the new owner's time zone
- [ ] A teammate in another zone sees the owner's date with the zone shown

---

### **Limit, plans and flag**

---

6.  **Workspace limit**

---

A workspace holds at most 500 repeating to-dos that have not ended. Checked-off and ended series do not count toward the limit.

**Checklist**

- [ ] At the limit, keep Repeat visible and open a sheet that says `This workspace has 500 repeating to-dos. End one to add another.`
- [ ] Leave checked-off and ended series out of the count

---

7.  **Plans and flag**

---

Repeat is for Plus and Team workspaces. The whole feature stays hidden until Data turns on `recurring_todos`, which happens once the three clients are out.

**Checklist**

- [ ] On Plus and Team workspaces, Repeat opens the picker
- [ ] On Free workspaces, show Repeat with a Plus badge and open the upgrade sheet on tap
- [ ] With `recurring_todos` off, show no Repeat on the detail sheet and no Skip this one in the menu

---

### **Tracking**

---

8.  **Send the tracking events**

---

Both events are in the tracking plan Yara reviewed on 2026-09-16.

**Checklist**

- [ ] Send `todo_repeat_set` with `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [ ] Send `todo_occurrence_skipped` when the member uses Skip this one
- [ ] Both events carry `workspace_id`, a hashed `user_id`, `platform`, `app_version` and `plan`
