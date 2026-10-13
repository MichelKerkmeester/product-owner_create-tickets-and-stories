# BE - TODO - Recurring to-dos

### About

---

This covers the recurring to-dos back end, with each rule defined in the parent task. Every next due date a member sees comes from here.

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

The owner's time zone keeps due dates in step with the Overdue chip and reminders.

**Checklist**

- [ ] Checking off an occurrence creates the next on the same page, dated by the parent task's option table
- [ ] Only one occurrence of a series exists at any time
- [ ] Weekdays moves a Friday occurrence to the following Monday
- [ ] A Monthly series from the 31st lands on the 30th in April and the 31st in May
- [ ] Custom moves the due date by N days, weeks or months, with N from 1 to 99
- [ ] The next due date uses the to-do owner's time zone, or the new owner's after a reassignment
- [ ] The next occurrence keeps the assignee and the reminder at the same local time
- [ ] On check-off and on skip, the next occurrence's reminder is handed to reminders-service

---

2.  **Skip this one**

---

**Checklist**

- [ ] Skip this one moves the to-do to its next due date without marking it done, and counts toward an After limit

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

**Checklist**

- [ ] A workspace holds at most 500 repeating to-dos that have not ended, and checked-off or ended series do not count
- [ ] A repeat that would take the workspace past 500 is refused, so the clients show the limit sheet

---

5.  **Flag**

---

**Checklist**

- [ ] With `recurring_todos` off for a workspace, the back end accepts no repeat on its to-dos
