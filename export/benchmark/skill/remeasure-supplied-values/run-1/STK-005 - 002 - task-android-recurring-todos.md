# FE - Android - TODO - Recurring to-dos

### About

---

Members on Android can set a to-do with a due date to repeat, then check off or skip each occurrence and get the next one with its next due date. This subtask brings the parent's shared rules to the Android app on phones and tablets. The Mobile Platform team (Oskar) takes it into the `5.4.0` release.

BE builds the recurrence engine in parallel. The app shows the next due date the engine returns and never works it out on the device, so a date on Android always matches the date iOS and Web show for the same to-do. Everything ships dark behind the workspace flag `recurring_todos`.

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

### **Setting a repeat**

---

1.  **Repeat picker**

---

Repeat sits on the to-do's detail sheet. The member picks how often the to-do repeats and when the series ends, so the picker has to offer exactly the options and ranges the engine accepts.

**Checklist**

- [ ] Repeat shows on the to-do's detail sheet on phones and tablets
- [ ] A to-do without a due date shows Repeat greyed out with the hint `Add a due date to repeat`
- [ ] Options are `Daily`, `Weekdays`, `Weekly`, `Monthly` and `Custom`
- [ ] Custom sets every N days, weeks or months, with N from `1` to `99`
- [ ] Ends offers `Never` as the default, `On date` and `After`
- [ ] After accepts a number of occurrences from `1` to `365`

2.  **Next due date**

---

The engine decides every next due date, including the Monthly rule that keeps to the day of the first due date and the owner's time zone. Android displays what the engine returns, because a second calculation on the device could disagree with the other clients.

**Checklist**

- [ ] Every next due date shown on Android is the date returned by `BE - TODO - Recurrence engine`, with no calculation on the device
- [ ] A Monthly series that starts on the 31st shows the 30th in April and the 31st in May, as the engine returns them
- [ ] A teammate in another time zone sees the owner's date with the owner's zone shown
- [ ] After the to-do is reassigned, the next occurrence shows the date the engine returns for the new owner's zone

### **Occurrences**

---

3.  **Check off and skip**

---

Only one occurrence exists at a time. Checking it off or skipping it moves the member straight to the next occurrence, so nothing about the to-do is lost between occurrences.

**Checklist**

- [ ] Checking off an occurrence shows the next one on the same page with its next due date
- [ ] Assignee carries over to the next occurrence
- [ ] The reminder carries over and fires on the next occurrence at the same local time
- [ ] `Skip this one` sits in the to-do's menu
- [ ] Skip this one moves the to-do to its next due date without marking it done
- [ ] A skipped occurrence counts toward an After limit, so the series ends after the set number of occurrences
- [ ] A series with `On date` stops after the last occurrence on or before that date

### **Access and limits**

---

4.  **Workspace limit**

---

A workspace holds at most `500` repeating to-dos that have not ended. Checked-off and ended series do not count.

**Checklist**

- [ ] At the limit, Repeat stays visible and opens a sheet with `This workspace has 500 repeating to-dos. End one to add another.`
- [ ] Below the limit, Repeat opens the picker as normal

5.  **Plans and flag**

---

Repeat is for Plus and Team workspaces. The whole feature stays dark behind `recurring_todos`, and Data turns the flag on once the three clients are out.

**Checklist**

- [ ] On Plus and Team, Repeat opens the picker
- [ ] On Free, Repeat shows with a Plus badge and opens the upgrade sheet
- [ ] With `recurring_todos` off, Android shows no recurring to-do controls

### **Tracking**

---

6.  **Events**

---

Both events are in the tracking plan Yara reviewed on 2026-09-16.

**Checklist**

- [ ] `todo_repeat_set` records the repeat set on Android, with `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [ ] `todo_occurrence_skipped` records each Skip this one on Android

> The parent does not say whether the app or the engine sends these events. Confirm the sender with Yara before build so each event is recorded once.
