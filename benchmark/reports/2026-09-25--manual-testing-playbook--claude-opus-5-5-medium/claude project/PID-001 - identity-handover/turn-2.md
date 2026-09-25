```markdown
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
```

Export-equivalent path: `export/002 - task-due-today-filter-chip.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality: All six checks pass, and Accuracy is at its floor of 9. Every checklist item describes something a tester can see or check in the event data.

**Summary:** The task has three requirement groups: the chip itself, which to-dos it shows and the analytics event. Most of it comes from your answers:

- The chip goes after Overdue.
- It shows to-dos not checked off that are due today in the owner's time zone.
- It sorts by due date like the other chips.
- One chip is active at a time.
- It reuses the existing chip, with no Figma.
- It is Web only, with no dependencies.
- It sends `filter_selected` with `filter` set to `due_today`.

**I added these myself.** Remove any you don't want:

- **Why the chip exists:** your reply didn't give a reason, so I wrote the About section's user-value line myself. It says members have no chip for what's due today.
- **Empty list:** if nothing is due today, the chip stays active and the list is empty. I made up this rule. Tell me if there is an existing empty-state design to reference instead.
- **Translations:** the label ships in all six locales with en-US as the fallback. This is based on the context file, but you never confirmed translations are part of this task.
- **Desktop check:** confirming Desktop picks up the chip on its next load. This is from the context file.
- **No due date:** to-dos without a due date are left out explicitly.
- **Event properties:** the standard property list on `filter_selected`, taken from the context file's analytics conventions.