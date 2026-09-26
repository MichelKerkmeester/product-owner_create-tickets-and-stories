# FE - Web - TODO - Due today filter chip

## About

---

Members scan the full To-dos list for today's work, because Overdue covers only earlier dates. This task adds a fourth chip, Due today, on Web only, which Desktop gets on its next web client load with no Desktop release, and iOS and Android follow in their own tasks.

"Today" is the date in the to-do owner's time zone, as for Overdue, so a to-do is never in both lists and moves to Overdue at the owner's midnight if unchecked.

### Requirements

---

1.  **Due today chip**

---

There is no Figma file for this change.

**Checklist**

- [] Chip order: All, Assigned to me, Overdue, Due today
- [] It uses the existing filter chip component unchanged
- [] It shows every unchecked to-do the member can open that is due today in the owner's time zone
- [] Checked-off, undated and other-day to-dos stay out
- [] Results sort by due date, as under the other chips
- [] One chip is active at a time, so picking any chip turns off the previous one
- [] All stays the default when the To-dos view opens
- [] With nothing due, the list stays empty without switching to All
- [] The label has a string in all six shipped locales, with en-US as fallback

> For a to-do owned in another time zone, Due today uses the owner's today, so its date can look like tomorrow or yesterday to the viewer. The date shows in the owner's zone, with the zone shown when it differs.

---

2.  **Analytics**

---

Yara has added `due_today` to the tracking plan, so client work needs no further Data review.

**Checklist**

- [] Picking Due today sends `filter_selected` with `filter` set to `due_today`
- [] It carries `workspace_id`, `user_id`, `platform`, `app_version` and `plan`, like other `filter_selected` events
- [] `all`, `assigned_to_me` and `overdue` keep sending as today
