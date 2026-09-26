```markdown
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
```

Export-equivalent path: `export/NNN - task-android-recurring-todos.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** Passes all six checks. The checklist items are things a tester can see on the device. Every value, copy string, event and flow name comes from the parent or the Loomlist context page. The engine-owns-the-date rule, phones and tablets, and `5.4.0` come from your reply.

**What I added that you didn't ask for (strike any you don't want):**
- **Offline check-off:** after a check-off with no connection, the app still never shows a due date it worked out itself. This follows your engine rule plus the "no offline mode" note in the context page.
- **Monthly on the 31st:** a QA check that Android shows the engine's dates for a series starting on the 31st, using the parent's example.
- **Reminder group:** the parent says reminders carry over. Because Android fires reminders as local notifications on the device, I added the new reminder at the same local time and the old due date's reminder stopping. If REM work owns this, move the group there.
- **Tracking properties:** the five event properties and hashing `user_id` come from the context page's analytics conventions, not from the parent.

**Still open, written exactly as the parent has them:**
- **Upgrade sheet:** billing changes happen only on Web, so what the upgrade sheet does on Android still needs a decision.
- **Links:** the three flows, the parent and the sibling tasks appear as plain named text because no Figma or ClickUp links were supplied.
- **Translations:** the task doesn't say who supplies the non-English strings.