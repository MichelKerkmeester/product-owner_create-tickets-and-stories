```markdown
# FE - Web - TODO - Due today filter chip

## About

---

The To-dos view carries three chips today, All, Assigned to me and Overdue, and none of them answers what is left for today. A member who wants to see the day's to-dos has to scan the full list, or read Overdue and work out which items are still to come.

This task adds a fourth chip, `Due today`, directly after Overdue, so the day's work is one selection away. It reuses the existing chip and the rule and ordering the view already applies, and it reports the selection with a value the tracking plan carries.

### Requirements

---

1.  **Chip in the filter row**

---

The new chip sits fourth in the row, directly after Overdue, and reuses the existing chip so its height, padding and active state match the three chips beside it. Its label is `Due today`.

One chip is active at a time, and All stays the default when the view opens.

**Checklist**

- [] The filter row shows four chips in the order All, Assigned to me, Overdue, `Due today`
- [] The chip reuses the existing chip component with no new visual style
- [] Selecting `Due today` deactivates the chip that was active, and All is active when the view opens

---

2.  **What the chip shows**

---

`Due today` shows to-dos that are not checked off and whose due date is today in the owner's time zone. A to-do checked off earlier today drops out of the list.

The ordering stays the one the view uses now, sorted by due date, so the chip changes which to-dos appear and not their order.

**Checklist**

- [] A to-do that is not checked off and due today in the owner's time zone appears under `Due today`
- [] A to-do due today that is already checked off does not appear
- [] A to-do due yesterday or due tomorrow does not appear
- [] A to-do with no due date does not appear
- [] The filtered list stays sorted by due date
- [] A to-do owned by another member is dated in that owner's time zone, not the viewer's
- [] The list follows the owner's day as it turns over, so a to-do due today leaves the filter once tomorrow starts in the owner's time zone

---

3.  **Empty result**

---

When no to-do matches, the list area shows a short message naming the filter and the chip stays active, so the member can see the filter applied and return to All.

**Checklist**

- [] `Due today` with no matching to-do keeps the chip active and shows a message naming the filter
- [] Selecting All restores the full list

---

4.  **Selection event**

---

Picking the chip sends `filter_selected` with `filter` set to `due_today`, the value Yara added to the tracking plan, so no tracking plan review blocks the build.

**Checklist**

- [] Selecting `Due today` sends `filter_selected` with `filter` set to `due_today`
- [] The event carries the fields the view already sends with `filter_selected`
- [] All, Assigned to me and Overdue keep sending `all`, `assigned_to_me` and `overdue`

---
```

Export-equivalent path: `export/NNN - task-due-today-filter-chip.md`
HVR self-scan: 1 hard blocker. Fixed: Oxford comma in the chip list, rewritten as "All, Assigned to me and Overdue". Kept with reason: none.
Quality: every floor met | Kind: Task | Energy: Standard

The task adds `Due today` as the fourth chip after Overdue, reusing the existing chip, with the same not-checked-off and owner time zone rule Overdue applies. It carries the sort order, the one-active-chip rule and the `filter_selected` value `due_today`. Acceptance checks sit inside each requirement group for QA.

### Open items
1. **Empty result**
   - **Situation:** Your answer did not cover what the chip shows when nothing matches, so the task keeps the chip active and shows a short message naming the filter
   - **Open:** Send the copy if design or product has wording, or strike the requirement
2. **Filter runs on the loaded list**
   - **Situation:** You said front end and nothing depends on it, so the task assumes the filter works on the to-dos the view already holds with no `todos-service` query change
   - **Open:** Confirm that holds, or tell me and the ticket becomes FS with a service change beside it
3. **Day rollover**
   - **Situation:** Nothing named what happens at midnight in the owner's time zone, so the task requires the list to follow the day as it turns over
   - **Open:** Strike it if the chip may keep yesterday's results until the view reloads

Want me to change anything?