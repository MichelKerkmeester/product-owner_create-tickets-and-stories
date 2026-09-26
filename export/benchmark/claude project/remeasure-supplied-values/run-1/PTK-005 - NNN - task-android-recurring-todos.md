# FE - Android - TODO - Recurring to-dos

### About

---

A member can set a to-do with a due date to repeat. When they check off or skip one occurrence, the next one appears. This subtask builds the Android side of `FS - TODO - Recurring to-dos` for phones and tablets. The shared rules live in the parent. This task covers what the Android app shows and what it sends.

`BE - TODO - Recurrence engine` works out every next due date and is being built in parallel. The Android app shows the date the engine returns and never works one out on the device. That way Android shows the same date as the engine for Monthly edge days, Weekdays and the owner's time zone.

Oskar's team ships this in Android `5.4.0`. It stays dark behind `recurring_todos` until Data turns the flag on once the three clients are out.

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

1.  **Repeat on the detail sheet**

---

A member sets how often a to-do repeats and when the series ends. Repeat needs a due date because every later occurrence counts from it.

**Checklist**

- [ ] Repeat sits on the to-do's detail sheet
- [ ] A to-do without a due date shows Repeat greyed out with the hint `Add a due date to repeat`
- [ ] Repeat offers Daily, Weekdays, Weekly, Monthly and Custom
- [ ] Custom sets every N days, weeks or months, with N from `1` to `99`
- [ ] Ends offers Never as the default, On date and After
- [ ] After accepts from `1` to `365` occurrences
- [ ] The picker matches `Recurring to-dos / Repeat picker` and Custom matches `Recurring to-dos / Custom interval` on phones and tablets

2.  **Occurrences**

---

Only one occurrence of a series exists at a time. The date the member sees always comes from the engine, so Android and the engine never disagree about when the next occurrence is due.

**Checklist**

- [ ] Checking off an occurrence shows the next one on the same page, with the next due date `BE - TODO - Recurrence engine` returns
- [ ] Assignee and reminder carry over to the next occurrence
- [ ] The page shows one occurrence of a series at a time
- [ ] Skip this one sits in the to-do's menu and moves the to-do to its next due date without marking it done
- [ ] The occurrence menu matches `Recurring to-dos / Occurrence menu` on phones and tablets
- [ ] Android never shows a next due date the engine did not return, including after a check-off made without a connection
- [ ] A Monthly series that starts on the 31st shows the 30th in April and the 31st again in May, as the engine returns them
- [ ] A teammate in another time zone sees the owner's date with the zone shown

3.  **Reminder on the device**

---

Android delivers reminders as local notifications on the device. When a reminder carries over, it has to fire for the new occurrence and stop firing for the old one.

**Checklist**

- [ ] The next occurrence's reminder notifies the to-do owner on their Android devices at the same local time as the previous reminder
- [ ] After a check-off or a skip, the reminder no longer fires for the old due date

4.  **Plans and the 500 limit**

---

Repeat is for Plus and Team workspaces. A workspace holds at most 500 repeating to-dos that have not ended. Checked-off and ended series do not count.

**Checklist**

- [ ] On Plus and Team below the limit, Repeat opens the picker
- [ ] At the limit, Repeat stays visible and opens a sheet that says `This workspace has 500 repeating to-dos. End one to add another.`
- [ ] On Free, Repeat shows with a Plus badge and opens the upgrade sheet

5.  **Flag and tracking**

---

Nothing of this feature is visible on Android until `recurring_todos` is on. Data counts use through the two events in the tracking plan Yara reviewed on 2026-09-16.

**Checklist**

- [ ] With `recurring_todos` off, Android shows neither Repeat nor Skip this one
- [ ] Setting a repeat sends `todo_repeat_set` with `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [ ] Skip this one sends `todo_occurrence_skipped`
- [ ] Both events carry `workspace_id`, `user_id`, `platform`, `app_version` and `plan`, with `user_id` hashed before it leaves the device
