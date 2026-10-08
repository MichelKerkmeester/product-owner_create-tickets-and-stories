# FE - Web - TODO - Due today filter chip

## About

The Web To-dos view has three filter chips today: All, Assigned to me and Overdue. A member who wants the to-dos due today has to scan the full list by date. This task adds a Due today chip so a member can narrow the list to today's open to-dos in one selection.

Desktop shows the same chip through the web client, with no Desktop release. The iOS and Android apps follow in a later task.

---

### Requirements

---

1.  **Chip placement**

---

The Due today chip sits directly after the Overdue chip and reuses the existing chip style.

**Checklist**

- [] The Due today chip appears directly after the Overdue chip
- [] The Due today chip uses the existing chip style
- [] The chip row reads All, Assigned to me, Overdue, Due today

2.  **Filter result**

---

Selecting the chip narrows the list to to-dos that are open and due today. The list sorts by due date, as the other chips do.

**Checklist**

- [] Selecting Due today lists only to-dos that are not checked off
- [] Selecting Due today lists only to-dos whose due date is today in the to-do owner's time zone
- [] A to-do due today that is already checked off does not appear in the list
- [] The list sorts by due date, the same as the other chips
- [] When a member views another member's to-do, its due date is judged in the owner's time zone

3.  **Chip selection**

---

Only one chip is active at a time, and All stays the default.

**Checklist**

- [] Selecting Due today makes it the only active chip
- [] Selecting All, Assigned to me or Overdue clears the Due today selection
- [] All is the active chip when the To-dos view opens

4.  **Analytics**

---

Selecting the chip sends one event that the Data team's tracking plan already covers.

**Checklist**

- [] Selecting Due today sends `filter_selected` with `filter` set to `due_today`

5.  **Platform scope**

---

The chip ships on Web in this task. Desktop receives it through the web client.

**Checklist**

- [] The chip appears in the Web To-dos view
- [] The chip appears in Desktop through the web client without a Desktop release
- [] The chip does not appear in the iOS or Android apps in this task
