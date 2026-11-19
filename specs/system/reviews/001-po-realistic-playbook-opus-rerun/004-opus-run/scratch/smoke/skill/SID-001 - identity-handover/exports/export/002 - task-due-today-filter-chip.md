# FE - Web - TODO - Due today filter chip

### About

---

Members can filter the To-dos view by All, Assigned to me and Overdue, but they have no quick way to see what is due today. This task adds a fourth chip, "Due today", so a member can see today's open work without scanning the full list or checking Overdue.

The chip ships on Web first. Desktop gets it through the web client the next time it loads, with no Desktop release. iOS and Android follow in later tasks.

### Requirements

---

1.  **Due today chip**

---

The chip reuses the existing filter chip component and follows the same selection rules as the other chips, so it looks and works like them. No new design is needed.

**Checklist**

- [ ] "Due today" sits directly after Overdue, making the order All, Assigned to me, Overdue, Due today
- [ ] The chip uses the existing filter chip component with no visual changes
- [ ] Only one chip is active at a time, so selecting Due today clears the chip that was active before
- [ ] All stays the default chip when the To-dos view opens

---

2.  **Due today list**

---

Due today shows the open to-dos a member still needs to finish today. "Today" is based on the to-do owner's time zone, which is also how Overdue works, so the two chips never show the same to-do.

**Checklist**

- [ ] The list shows only to-dos that are not checked off and whose due date is today in the to-do owner's time zone
- [ ] Overdue to-dos, checked-off to-dos and to-dos with no due date do not appear
- [ ] A to-do owned by someone in another time zone appears when its due date is today in the owner's time zone, even if the viewer's date is different
- [ ] The list shows only to-dos the member can open, the same as the rest of the To-dos view
- [ ] The list is sorted by due date, the same as the other chips

---

3.  **Tracking**

---

The `due_today` value is already in the tracking plan, so this item only sends the event from the client.

**Checklist**

- [ ] Selecting Due today sends `filter_selected` with `filter` set to `due_today`
- [ ] The event carries the standard properties: `workspace_id`, `user_id`, `platform`, `app_version` and `plan`
- [ ] `all`, `assigned_to_me` and `overdue` are still sent as before
