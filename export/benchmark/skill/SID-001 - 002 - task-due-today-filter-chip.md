# FE - Web - TODO - Due today filter chip

### About

---

The To-dos view has three filter chips today: All, Assigned to me and Overdue. A member who wants to see what needs doing today has to scan the full list, because Overdue only covers dates before today. This task adds a fourth chip, Due today, after Overdue. It shows the to-dos due today that are not checked off yet.

This task covers Web only. Desktop gets the chip through the web client the next time it loads, with no Desktop release. iOS and Android will follow in their own tasks later and are out of scope here.

"Today" follows the same rule as Overdue: the date in the to-do owner's time zone. Because both chips use the same zone, a to-do is never in both lists at once. At midnight in the owner's time zone, an unchecked to-do moves from Due today to Overdue.

### Requirements

---

1.  **Due today chip**

---

The chip reuses the existing filter chip component, so it looks and behaves like the other three. There is no Figma file for this change.

**Checklist**

- [ ] A chip labelled "Due today" sits directly after Overdue, so the order is All, Assigned to me, Overdue, Due today
- [ ] The chip uses the existing filter chip component with no visual changes
- [ ] Picking Due today shows every to-do the member can open that is not checked off and has a due date of today in the to-do owner's time zone
- [ ] To-dos that are checked off, have no due date or are due on any other day do not appear under Due today
- [ ] Results are sorted by due date, the same as under the other chips
- [ ] Only one chip is active at a time. Picking Due today turns off the chip that was active, and picking another chip turns off Due today
- [ ] All stays the default chip when the To-dos view opens
- [ ] When nothing is due today, the Due today list is empty and the view does not switch back to All
- [ ] The "Due today" label has a string in each of the six shipped locales, and en-US is the fallback when a string is missing

> A member can see to-dos owned by someone in a different time zone. For those to-dos, Due today uses the owner's today rather than the viewer's, so the list can include a to-do whose date looks like tomorrow or yesterday to the viewer. The date shows in the owner's time zone, and the zone is shown whenever it differs from the viewer's.

---

2.  **Analytics**

---

Yara has already added `due_today` to the tracking plan, so client work can start without another Data review.

**Checklist**

- [ ] Picking Due today sends `filter_selected` with `filter` set to `due_today`
- [ ] The event carries `workspace_id`, `user_id`, `platform`, `app_version` and `plan`, the same as the other `filter_selected` events
- [ ] The `all`, `assigned_to_me` and `overdue` values keep sending as they do today
