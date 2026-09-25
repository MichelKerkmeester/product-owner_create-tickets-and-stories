# BE - TODO - Recurring to-dos

### About

---

This subtask covers the back end of recurring to-dos: the next occurrence on check-off and on skip, Ends, the workspace limit of 500 and handing the next reminder to reminders-service. The parent task defines each rule. The clients set the repeat and show the result, so every next due date a member sees comes from this subtask.

**Parent task**

---

- `FS - TODO - Recurring to-dos`

**Related tasks**

---

- `FE - iOS - TODO - Recurring to-dos`
- `FE - Android - TODO - Recurring to-dos`
- `FE - Web - TODO - Recurring to-dos`

### Requirements

---

1.  **Next occurrence**

---

Only one occurrence of a series exists at a time. The next due date is worked out in the to-do owner's time zone, the same rule the Overdue chip and reminders follow, so the date the owner sees matches their Overdue chip.

**Checklist**

- [ ] Checking off an occurrence creates the next one on the same page, with the next due date from the option table in the parent task
- [ ] Only one occurrence of a series exists at any time
- [ ] Weekdays moves a Friday occurrence to the following Monday
- [ ] A Monthly series that starts on the 31st lands on the 30th in April and on the 31st again in May
- [ ] Custom moves the due date by N days, weeks or months, with N from 1 to 99
- [ ] The next due date is worked out in the to-do owner's time zone
- [ ] After a reassignment, the next occurrence uses the new owner's time zone
- [ ] The next occurrence keeps the assignee and the reminder, and the reminder keeps the same local time
- [ ] On check-off and on skip, the next occurrence's reminder is handed to reminders-service

---

2.  **Skip this one**

---

A skip moves the series forward without counting as done, but it still uses up one occurrence of an After limit.

**Checklist**

- [ ] Skip this one moves the to-do to its next due date without marking it done
- [ ] A skipped occurrence counts toward an After limit

---

3.  **Ends**

---

**Checklist**

- [ ] Never keeps the series going with no end
- [ ] On date creates no occurrence after the last one on or before that date
- [ ] After creates no occurrence past the set count, from 1 to 365

---

4.  **Workspace limit**

---

The limit counts live series only, so ending a series frees room for a new one.

**Checklist**

- [ ] A workspace holds at most 500 repeating to-dos that have not ended
- [ ] Setting a repeat that would take the workspace past 500 is refused, so the clients can show the limit sheet
- [ ] Checked-off and ended series do not count toward the 500

---

5.  **Flag**

---

**Checklist**

- [ ] With `recurring_todos` off for a workspace, the back end accepts no repeat on its to-dos
