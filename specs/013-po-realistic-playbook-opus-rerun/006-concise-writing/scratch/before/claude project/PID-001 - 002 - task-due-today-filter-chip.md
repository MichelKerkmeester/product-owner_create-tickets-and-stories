# FE - Web - TODO - Due today filter chip

### About

---

The To-dos view has three filter chips: All, Assigned to me and Overdue. Members can see which to-dos are already late, but no chip shows the to-dos due today. To find those, they have to look through the full list.

Add a Due today chip on Web. It shows the to-dos that are not checked off and are due today in the owner's time zone. Desktop gets the chip through the web client. iOS and Android will follow in later tasks and are out of scope here.

### Requirements

---

1.  **Add the Due today chip**

---

The new chip reuses the existing filter chip, so it looks and behaves like the three chips already on the To-dos view.

**Checklist**

- [ ] Show a chip labelled `Due today` directly after Overdue, so the chips read All, Assigned to me, Overdue, Due today
- [ ] Use the existing filter chip with no new styling
- [ ] Keep one chip active at a time, so selecting Due today deactivates the previously active chip
- [ ] Keep All as the default chip when the To-dos view opens
- [ ] Show the chip label in every shipped locale, with en-US as the fallback for a missing string
- [ ] Confirm Desktop shows the chip the next time it loads, with no Desktop release

---

2.  **Show only the to-dos due today**

---

"Today" follows the same rule as Overdue. It is read in the to-do owner's time zone, not the viewer's. A to-do shows under Due today when its owner's date is today, even if the member viewing the list is already on a different date.

**Checklist**

- [ ] With Due today active, list every to-do the member can open that is not checked off and whose due date is today in the owner's time zone
- [ ] Leave out checked-off to-dos, to-dos due before or after today and to-dos with no due date
- [ ] Sort the list by due date, the same as the other chips
- [ ] When no to-do is due today, keep the chip active and show no to-dos rather than falling back to another chip's list

---

3.  **Send filter_selected when the chip is picked**

---

The `due_today` value is already in the tracking plan, so the client work does not wait on a Data review.

**Checklist**

- [ ] Send `filter_selected` with `filter` set to `due_today` when the member selects Due today
- [ ] Send the same properties the other `filter_selected` events carry: `workspace_id`, hashed `user_id`, `platform`, `app_version` set to the web build number and `plan`
- [ ] Keep sending `all`, `assigned_to_me` and `overdue` for the existing chips, unchanged
