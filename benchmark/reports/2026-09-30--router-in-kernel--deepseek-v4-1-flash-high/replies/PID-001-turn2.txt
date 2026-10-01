```
# FE - Web - TODO - Due today filter chip on the To-dos view

## About

---

Three chips sit above the To-dos view list today: All, Assigned to me and Overdue. None of them isolates the current day, so a member who wants to know what is due today reads the whole list instead.

This task adds a fourth chip, Due today, to the existing row on the Web client. Once it ships, a member sees the day's due to-dos in one place. Desktop picks the chip up with the next web build it loads, and the mobile apps follow later.

### Requirements

---

### **Add the chip to the To-dos view**

---

1.  **Place Due today after Overdue in the existing chip row**

---

One chip is active at a time in the row above the list. Add Due today as the last chip, directly after Overdue, and leave the rest of the row as it is.

**Checklist**

- [] Add a `Due today` chip to the row, directly after `Overdue`
- [] Reuse the existing chip component with no new variant, matching the current chips in size, spacing, label style and active state
- [] Keep one chip active at a time, with `All` still active on first load
- [] Clear the active chip when another one is picked, so picking `Due today` leaves no other chip active
- [] Localize the `Due today` label for the six shipped languages, with en-US as the fallback
- [] Add no Figma frame and no new chip component for this change

---

### **Due today filter behavior**

---

2.  **Match to-dos that are not checked off and due today**

---

`Due today` follows the same rule as `Overdue`, with today in place of a date before today. Each to-do's due date is read in the to-do owner's time zone.

**Checklist**

- [] Show only to-dos that are not checked off and whose due date is today in the owner's time zone
- [] Leave a to-do whose due date is before today to the `Overdue` chip
- [] Leave out a to-do whose due date is after today, and leave out any to-do with no due date
- [] Read the due date in the to-do owner's time zone, so a to-do owned by a member in another zone matches on that owner's date
- [] Sort the filtered list by due date, in the order the other chips use
- [] Return the same to-dos the member can already open, with no change to page or workspace access

**User Story**

- **Given:** I am a member on the To-dos view with to-dos due today
- **When:** I pick `Due today`
- **Then:** I see the to-dos I can open that are not checked off and due today, ordered by due date

---

3.  **Keep the chip filtering when nothing is due today**

---

On a day with no due to-dos, the chip stays a filter rather than falling back to the full list.

**Checklist**

- [] Keep `Due today` active and the list empty when no to-do is due today
- [] Keep the list on `Due today` instead of switching back to `All` on an empty result
- [] Change no existing empty-state copy in this task

---

### **Tracking and platform reach**

---

4.  **Send filter_selected with the due_today value**

---

A chip pick is tracked with `filter_selected` and a `filter` value of `all`, `assigned_to_me` or `overdue`. `due_today` is already in the tracking plan, so this task carries no tracking-plan work.

**Checklist**

- [] Send `filter_selected` with `filter` set to `due_today` when a member picks `Due today`
- [] Carry the fields the other `filter_selected` values carry, including `workspace_id`, `user_id`, `platform`, `app_version` and `plan`
- [] Add no event or plan change beyond the chip pick, since `due_today` is already added

---

5.  **Reach Web first, then Desktop, then the apps**

---

Web deploys continuously and Desktop wraps the web client in a native shell.

**Checklist**

- [] Ship the chip on the Web client, with no store release
- [] Confirm Desktop shows the chip once it loads the next web build, with no Desktop shell change
- [] Leave iOS and Android out of this task, since the apps follow later
```

Export-equivalent path: `export/NNN - task-due-today-filter-chip.md`

Quality: scope is Web-only and chip-sized, every checklist line is testable, the filter boundary against Overdue and undated to-dos is explicit, and the tracking value arrives already planned.

HVR self-scan: 0 hard blockers. Fixed: the chip list repeated in the Requirements intro, rewritten as the row above the list. Kept with reason: the three supplied chip names as content, and the identifiers `filter_selected`, `due_today`, `assigned_to_me` and `overdue` as the platform names them.

Additions to strike if you disagree: the opening problem line in About is my framing of why the chip is worth building, the empty-result behavior (chip stays active, list empty, no new copy) is a boundary I added, and the six-locale label line assumes the `Due today` string is new copy rather than an existing string. The chip carries no count in this version, since the reused component has none and you did not ask for one.

The task is ready to send back once you confirm those three, and the human reconciles the file number when saving it outside the Project.