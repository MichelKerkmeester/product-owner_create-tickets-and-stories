# FE - Web - TODO - Due today filter chip

### About

---

The To-dos view has three filter chips: All, Assigned to me and Overdue. Overdue shows to-dos that are already late. A member who wants to see what's due today has to scan the All list for them. A Due today chip shows those to-dos with one tap.

This task covers Web only. Desktop gets the chip through the web client the next time it loads, with no Desktop release. iOS and Android will follow in separate tasks.

### Requirements

---

1.  **Add the Due today chip**

---

The chip reuses the existing filter chip and follows the same rules as the other chips. The only new thing a member has to learn is which to-dos it shows.

"Today" means today in the to-do owner's time zone, which is the rule Overdue already uses. Because Overdue covers due dates before today and Due today covers today only, no to-do appears under both chips.

**Checklist**

- [ ] A chip labelled `Due today` sits directly after Overdue, so the order is All, Assigned to me, Overdue, Due today
- [ ] The chip reuses the existing filter chip with no visual changes
- [ ] Selecting Due today makes it the only active chip, and selecting any other chip turns it off
- [ ] All stays the default chip when the To-dos view opens
- [ ] With Due today active, the list shows only to-dos that are not checked off and whose due date is today in the to-do owner's time zone
- [ ] To-dos with no due date don't appear, and neither do to-dos due before or after today in the owner's time zone
- [ ] A to-do whose owner is in a different time zone from the viewer appears when its due date is today in the owner's time zone, even if the viewer's date is different
- [ ] The list sorts by due date, the same as the other chips

---

2.  **Track the chip selection**

---

Yara has already added `due_today` to the tracking plan, so the client can send it with no further Data review.

**Checklist**

- [ ] Selecting Due today sends `filter_selected` with `filter` set to `due_today`
- [ ] The event carries `workspace_id`, `user_id`, `platform`, `app_version` and `plan`, with `app_version` holding the web build number
- [ ] Selecting All, Assigned to me or Overdue still sends `all`, `assigned_to_me` or `overdue`
