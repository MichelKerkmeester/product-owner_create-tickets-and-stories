# BE - TODO - Recurring to-do occurrences, Ends and workspace limit

### About

---

BE owns what happens after a member sets Repeat: the next occurrence on check-off and Skip this one, Ends, the 500 limit on series still running and the reminder handover to reminders-service. The three client subtasks show this behavior, so it has to hold whichever surface the member acts from. The parent task holds the shared rules with every value.

BE ships dark behind the workspace flag `recurring_todos`, the same as the clients.

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

Only one occurrence of a series exists at a time. Checking it off is what brings the next one into being, on the same page.

**Checklist**

- [ ] Checking off an occurrence creates the next one on the same page, with the next due date the parent task's Repeat table gives
- [ ] Monthly keeps the first due date's day, so a series starting on the 31st lands on the 30th in April and the 31st in May
- [ ] Custom counts every N days, weeks or months, with N from 1 to 99
- [ ] The next occurrence keeps the assignee and the reminder
- [ ] A series never holds more than one open occurrence
- [ ] Checking off the same occurrence on two devices before they sync still produces one next occurrence
- [ ] An occurrence checked off from an app version without Repeat still gets its next occurrence

---

2.  **Skip this one**

---

**Checklist**

- [ ] Skip this one moves the to-do to its next due date without marking it done
- [ ] A skipped occurrence counts toward an After limit

---

3.  **Ends**

---

**Checklist**

- [ ] With Ends set to Never, the default, the series keeps going
- [ ] With On date, the series stops after the last occurrence on or before that date
- [ ] With After, the series stops after the set number of occurrences, from 1 to 365, skipped occurrences included

---

4.  **Time zones**

---

Next due dates follow the rule the Overdue chip and reminders already follow, so all three agree on which day a to-do is due.

**Checklist**

- [ ] Next due dates are worked out in the to-do owner's time zone
- [ ] After a reassign, the next occurrence uses the new to-do owner's time zone

---

5.  **Workspace limit**

---

**Checklist**

- [ ] A workspace holds up to 500 repeating to-dos that have not ended
- [ ] Checked-off and ended series do not count toward the 500
- [ ] Setting Repeat on another to-do in a workspace at 500 is refused, so the clients can open the sheet that says `This workspace has 500 repeating to-dos. End one to add another.`

---

6.  **Reminder handover**

---

reminders-service holds each reminder's UTC due time and hands it to every device of the to-do owner, so the next occurrence's reminder reaches members only once BE passes it on.

**Checklist**

- [ ] The next occurrence's reminder goes to reminders-service at the same local time as the one before, in the to-do owner's time zone

---

7.  **Flag and tracking**

---

**Checklist**

- [ ] With `recurring_todos` off for a workspace, no repeat behavior runs there
- [ ] BE sends whichever of `todo_repeat_set` and `todo_occurrence_skipped` the reviewed tracking plan assigns to it
