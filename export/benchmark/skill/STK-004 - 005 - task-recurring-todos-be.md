# BE - TODO - Recurring to-do occurrences, Ends and workspace limit

## About

---

BE owns what follows Repeat: the next occurrence on check-off and Skip this one, Ends, the 500 limit on running series and reminder handover to reminders-service. It must hold whichever of the three clients the member uses, and the parent holds the shared rules.

BE ships dark behind the workspace flag `recurring_todos`, like the clients.

**Parent task**

---

- [FS - TODO - Recurring to-dos](<001 - task-recurring-todos-parent.md>)

**Related tasks**

---

- [FE - iOS - TODO - Recurring to-dos](<002 - task-recurring-todos-ios.md>)
- [FE - Android - TODO - Recurring to-dos](<003 - task-recurring-todos-android.md>)
- [FE - Web - TODO - Recurring to-dos](<004 - task-recurring-todos-web.md>)

### Requirements

---

1.  **Next occurrence on check-off**

---

**Checklist**

- [] Checking off an occurrence creates the next on the same page, with the next due date from the parent's Repeat table
- [] Monthly keeps the first due date's day, so a 31st series lands on the 30th in April and the 31st in May
- [] Custom counts every N days, weeks or months, N from 1 to 99
- [] The next occurrence keeps the assignee and reminder
- [] A series never holds more than one open occurrence
- [] Checking off one occurrence on two devices before sync still yields one next occurrence
- [] A check-off from an app version without Repeat still gets a next occurrence

---

2.  **Skip this one**

---

**Checklist**

- [] Skip this one moves the to-do to its next due date without marking it done
- [] A skip counts toward an After limit

---

3.  **Ends**

---

**Checklist**

- [] Never, the default, keeps the series going
- [] On date stops it after the last occurrence on or before that date
- [] After stops it after the set 1 to 365 occurrences, skips included

---

4.  **Time zones**

---

Due dates follow the Overdue chip and reminders' rule, so all three agree.

**Checklist**

- [] Next due dates use the to-do owner's time zone
- [] After a reassign, the new owner's zone applies

---

5.  **Workspace limit**

---

**Checklist**

- [] A workspace holds up to 500 unended repeating to-dos
- [] Checked-off and ended series do not count toward the 500
- [] Setting Repeat in a workspace at 500 is refused, so clients can open the sheet saying `This workspace has 500 repeating to-dos. End one to add another.`

---

6.  **Reminder handover**

---

reminders-service holds each reminder's UTC due time and sends it to all the owner's devices, so the next reminder reaches members only once BE passes it on.

**Checklist**

- [] The next reminder goes to reminders-service at the previous one's local time, in the owner's zone

---

7.  **Flag and tracking**

---

**Checklist**

- [] With `recurring_todos` off, no repeat behavior runs
- [] BE sends whichever of `todo_repeat_set` and `todo_occurrence_skipped` the reviewed tracking plan assigns it
