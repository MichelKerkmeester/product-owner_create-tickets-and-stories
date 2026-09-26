```markdown
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
```

Export-equivalent path: `export/002 - task-due-today-filter-chip.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** Passes all six checks. Actionability is the one that matters most for a task, and every checklist item describes something a tester can see.

**Summary:** This is a Web-only front end task with two parts:
- **The chip:** where it sits, which to-dos it shows, how they sort and the one-active-chip rule
- **Tracking:** the `due_today` value on `filter_selected`

**Things I added that you didn't mention.** Remove any you don't want:
- **The time zone item.** A to-do owned by someone in another time zone shows when it's due today in the owner's time zone. This follows from the context file's rule that due dates use the owner's time zone.
- **The Due today and Overdue boundary.** I explained that the two chips never overlap. This follows from the Overdue definition in the context file.
- **The event properties.** The list of properties on `filter_selected` comes from the context file's analytics conventions.

**Two open points that aren't in the task.** You didn't answer these, so I left them out rather than guess:
- **Empty list:** what the list shows when nothing is due today.
- **Translations:** who provides the chip label in the five locales other than en-US. The context file says a missing string falls back to en-US.

Send me an answer for either one and I'll add it.