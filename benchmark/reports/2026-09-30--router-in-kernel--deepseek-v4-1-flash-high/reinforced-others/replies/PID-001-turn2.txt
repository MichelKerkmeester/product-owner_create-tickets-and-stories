```markdown
# FE - Web - TODO - Due today filter chip on the To-dos view

## About

---

The To-dos view filters by three chips today: `All`, `Assigned to me` and `Overdue`. A member planning the day has no way to see only the work due today, so they read past the to-dos already dated earlier in the week. The `Due today` chip follows `Overdue` and lists to-dos that are not checked off and due today in the owner's time zone.

The chip reuses the existing filter chip component, so the work is one filter, one list rule and one analytics value on the Web client. Desktop receives the change through the web client. The mobile apps are out of scope.

### Requirements

---

1.  **Add the Due today chip**

---

The chip row gains a fourth chip after `Overdue`. It reuses the existing filter chip component with no new visual design, and the row keeps its existing behavior of one active chip, with `All` as the default.

**Checklist**

- [] The To-dos view chip row shows `Due today` directly after `Overdue`
- [] The chip label reads `Due today`
- [] The chip reuses the existing filter chip component, with no new visual design
- [] Only one chip is active at a time, and `All` stays the default on open
- [] The `Due today` label is available in all six locales the app ships

---

2.  **Show the to-dos due today**

---

The chip selects to-dos that are not checked off and whose due date is today in the owner's time zone, the same time-zone rule the `Overdue` chip uses. The list sorts by due date, as it does under the other chips.

**Checklist**

- [] Selecting `Due today` lists every to-do that is not checked off and due today in the owner's time zone
- [] A to-do dated before today or after today does not appear
- [] A checked-off to-do does not appear
- [] A to-do with no due date does not appear
- [] The list sorts by due date, as it does under the other chips
- [] The list keeps the existing empty state when no to-do is due today

---

3.  **Report the chip selection**

---

Selecting the chip reports the filter the member picked on the To-dos view.

**Checklist**

- [] Selecting the chip sends `filter_selected` with `filter` set to `due_today`

> `due_today` is already in the tracking plan, so no tracking plan change is part of this task.
```

Export-equivalent path: `export/001 - task-due-today-filter-chip.md`

Quality status: complete at the small-task shape. Scope holds to Web, every supplied label and analytics value travels in backticks, the requirements state WHAT and the outcome, and the checklist is QA-ready.

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: the chip labels `All`, `Assigned to me`, `Overdue` and `Due today` and the analytics names `filter_selected`, `filter` and `due_today`, all supplied values carried verbatim in backticks.

Two things to check before this hardens. The locale checklist item is my addition, since your answer did not cover it, so strike it if the string ships untranslated for now. I also read the rule as excluding checked-off to-dos and anything dated before today, which is what separates the chip from `Overdue`.

Nothing else is open, so the task is ready to copy into your tracker or push through the ClickUp connector once it is connected.