# FE - Android - TODO - Recurring to-dos

### About

---

Members on Android phones and tablets can set a to-do with a due date to repeat, check off or skip one occurrence and see the next one appear with its next due date. This subtask builds the parent's shared rules in the Android app. The Mobile Platform team takes it into the Android 5.4.0 release.

The recurrence engine is built by BE in parallel and owns every date calculation. The app sends the member's repeat choice and shows the next due date the engine returns. It never works out a due date on the device, so Android can never disagree with iOS, Web or Desktop about when a to-do is next due. The shared rules for date calculation, including how Monthly handles the 31st, live in the parent and belong to `BE - TODO - Recurrence engine`.

Everything ships dark behind the workspace flag `recurring_todos`. Data turns the flag on once the iOS, Android and Web clients are out.

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

1.  **Repeat on the detail sheet**

---

Repeat sits on the to-do's detail sheet. A repeat needs a due date to count from, so the option stays visible but cannot be used until the to-do has one.

**Checklist**

- [ ] Repeat appears on the to-do's detail sheet on Android phones and tablets
- [ ] A to-do without a due date shows Repeat greyed out with the hint `Add a due date to repeat`
- [ ] The picker offers Daily, Weekdays, Weekly, Monthly and Custom, matching `Recurring to-dos / Repeat picker`
- [ ] Custom takes every N days, weeks or months, and the member cannot save an N below 1 or above 99, matching `Recurring to-dos / Custom interval`
- [ ] Ends offers Never, On date and After, with Never selected by default
- [ ] After takes a number of occurrences, and the member cannot save a number below 1 or above 365
- [ ] Android sends the choice to the recurrence engine and does not work out any due date from it

---

2.  **Plans, limit and flag**

---

Repeat is for Plus and Team workspaces, and a workspace holds at most 500 repeating to-dos that have not ended. Members on Free or at the limit still see Repeat, and it opens a sheet that tells them why they cannot use it.

**Checklist**

- [ ] With `recurring_todos` off for the workspace, nothing from this subtask shows on Android
- [ ] On a Free workspace, Repeat shows with a Plus badge and opens the upgrade sheet
- [ ] On a workspace with 500 repeating to-dos that have not ended, Repeat stays visible and opens a sheet that says `This workspace has 500 repeating to-dos. End one to add another.`
- [ ] Checked-off and ended series do not count toward the 500, so a workspace under the limit after one ends can add a repeat again

---

### **Occurrences**

---

3.  **Check off and skip**

---

Only one occurrence of a series exists at a time. Checking it off or skipping it replaces it with the next occurrence on the same page, and the next due date is always the one the engine returns.

**Checklist**

- [ ] Checking off an occurrence shows the next occurrence on the same page with the next due date the engine returns
- [ ] Until the engine returns the next occurrence, Android shows no due date for it that the device worked out on its own
- [ ] Skip this one sits in the to-do's menu, matching `Recurring to-dos / Occurrence menu`
- [ ] Skip this one moves the to-do to the next due date the engine returns without marking it done
- [ ] The next occurrence keeps the assignee of the one before it
- [ ] The next occurrence keeps its reminder at the same local time, scheduled as a local notification on the device like any other Android reminder
- [ ] A series that has reached its On date or its After count shows no further occurrence once the last one is checked off or skipped

---

4.  **Due dates and time zones**

---

Due dates follow the to-do owner's time zone, and the engine applies that zone when it works out the next date. Android shows the result so that a teammate elsewhere sees the same date the owner does.

**Checklist**

- [ ] Every occurrence shows its due date in the owner's time zone
- [ ] A member in a different time zone from the owner sees the owner's date with the zone shown
- [ ] After the to-do is reassigned, the next occurrence shows the due date the engine returns for the new owner's zone

---

### **Tracking**

---

5.  **Repeat events**

---

Both events are in the tracking plan Yara reviewed on 2026-09-16, and Android records them with the names and values that plan uses.

**Checklist**

- [ ] `todo_repeat_set` is recorded when a member saves a repeat on Android, with `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [ ] `todo_occurrence_skipped` is recorded when a member taps Skip this one on Android
- [ ] Both events carry `workspace_id`, `user_id`, `platform`, `app_version` and `plan`, with `user_id` hashed and no to-do text in the event
