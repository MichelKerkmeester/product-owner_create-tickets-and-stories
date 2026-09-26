# FE - Web - TODO - Due today filter chip

### About

---

The To-dos view has three filter chips: All, Assigned to me and Overdue. None of them shows only what needs doing today. Overdue shows only to-dos that are already late, and All also includes future to-dos and to-dos with no due date. This task adds a Due today chip on Web so members can see today's open to-dos in one click.

Due today uses the same day boundary as Overdue. An open to-do due before today appears under Overdue, and one due today appears under Due today, never under both. Desktop gets the chip through the web client with no Desktop release. iOS and Android follow in later tasks.

### Requirements

---

1.  **Add the Due today chip**

---

Due today picks up where Overdue stops. Both chips measure "today" in the to-do owner's time zone, so the two lists never overlap and no open to-do falls between them.

**Checklist**

- [ ] A Due today chip appears directly after Overdue, so the chips read All, Assigned to me, Overdue, Due today
- [ ] The chip reuses the existing filter chip with no new visual design
- [ ] Only one chip is active at a time, so selecting Due today deactivates the active chip, and All stays the default
- [ ] With Due today active, the list shows every to-do the member can open that is not checked off and whose due date is today in the to-do owner's time zone
- [ ] To-dos that are checked off, have no due date or are due on another day do not appear under Due today
- [ ] The list sorts by due date, the same way as the other chips
- [ ] A to-do owned by a member in another time zone appears when it is due today in its owner's time zone, even when that date differs from the viewer's today
- [ ] Desktop shows the chip once it loads a web build that contains it

2.  **Track Due today selections**

---

`filter_selected` already records which chip a member picks. `due_today` is already in the tracking plan.

**Checklist**

- [ ] Selecting Due today sends `filter_selected` with `filter` set to `due_today`
- [ ] The event carries the same properties as the other chip selections: `workspace_id`, `user_id`, `platform`, `app_version` and `plan`
