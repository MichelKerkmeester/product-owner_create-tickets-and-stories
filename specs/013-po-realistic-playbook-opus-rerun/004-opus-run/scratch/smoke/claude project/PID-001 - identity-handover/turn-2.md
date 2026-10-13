```markdown
# FE - Web - TODO - Due today filter chip

### About

---

The To-dos view has three filter chips: All, Assigned to me and Overdue. Overdue only shows to-dos due before today. To see what has to be finished today, a member has to scan All, where today's to-dos sit between older and later ones.

Add a Due today chip that lists the to-dos not checked off whose due date is today in the to-do owner's time zone. It uses the same day boundary as Overdue, so a to-do never appears under both chips. Together, the two chips cover everything not checked off that is due up to the end of today.

This task covers Web only. Desktop gets the chip through the web client the next time it loads, with no Desktop release. iOS and Android follow in later tasks.

### Requirements

---

1.  **Add the chip after Overdue**

---

Due today uses the existing filter chip, so it looks and behaves like the other three chips.

**Checklist**

- [ ] Show a chip labelled "Due today" directly after Overdue, so the row reads All, Assigned to me, Overdue, Due today
- [ ] Use the existing filter chip component with no new styles or states
- [ ] Keep one chip active at a time, so selecting Due today deactivates the chip that was active
- [ ] Keep All as the default chip when the To-dos view opens
- [ ] Confirm the chip appears in Desktop after it loads the web build that ships this task

---

2.  **List the to-dos due today**

---

"Today" means the to-do owner's today, the same rule that Overdue and due dates already follow. Say a teammate's to-do is due today in the teammate's time zone. A member viewing it sees it under Due today, even when the member's own date is different.

**Checklist**

- [ ] Show only to-dos not checked off whose due date is today in the to-do owner's profile time zone
- [ ] Leave out to-dos due before today, which stay under Overdue
- [ ] Leave out to-dos due after today and to-dos with no due date
- [ ] Show only to-dos the member can open, the same set the other chips draw from
- [ ] Sort the list by due date, the same way the other chips sort

---

3.  **Send the chip selection event**

---

Yara has added `due_today` to the tracking plan. That means this task can send the value without waiting for another Data review.

**Checklist**

- [ ] Send `filter_selected` with `filter` set to `due_today` when a member selects Due today
- [ ] Include `workspace_id`, `user_id`, `platform`, `app_version` and `plan` on the event, with the web build number in `app_version`
- [ ] Keep the events for `all`, `assigned_to_me` and `overdue` unchanged
```

Export-equivalent path: `export/002 - task-todos-due-today-filter-chip.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I've written the Web task for the Due today chip. All six quality checks passed. Everything in it comes from your answer or from `loomlist-context.md`.

**Things I added that you didn't state (delete any you don't want):**
- **Other time zones:** a teammate's to-do appears under Due today when it's due today in the teammate's time zone. This follows from the owner time zone rule in the context file.
- **Which to-dos show:** only to-dos the member can open, which matches how the context file defines the To-dos view.
- **Leaving out overdue to-dos:** these stay under Overdue, so the two chips never overlap.
- **Existing events:** the `all`, `assigned_to_me` and `overdue` events stay unchanged.
- **Web build number:** it goes in `app_version`, as the context file says Web does.
- **Desktop check:** confirm the chip shows up once Desktop loads the new web build.

**Still open, so I left them out of the task:**
- **Empty state:** what the list shows when nothing is due today.
- **Translations:** the "Due today" label needs strings for de-DE, fr-FR, es-ES, ja-JP and pt-BR. Without them, those locales will show the en-US label.

Tell me what you want for either one and I'll add it to the task.