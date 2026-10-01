```
# FE - Web - TODO - Due today filter chip

## About

---

The To-dos view filters by All, Assigned to me and Overdue. A member planning their day has no filter for the to-dos due today, so they read the whole list and pick today's items out by eye.

Due today adds a fourth chip listing to-dos that are not checked off and are due today in the owner's time zone. It sits immediately after Overdue and reuses the existing chip. Selecting it sends `filter_selected` with `filter` set to `due_today`, and the tracking plan already carries that value.

### Requirements

---

**Due today chip**

---

The chip reuses the existing component and needs no design, so the work is the filter and its selected state. One chip stays active at a time, as with the three filters today. Web ships it first, Desktop receives it through the web client it loads, and the mobile apps follow later.

**Checklist**

- [] The To-dos view shows Due today immediately after Overdue
- [] Selecting Due today lists to-dos that are not checked off with a due date of today in the owner's time zone
- [] The list keeps the due date sort the other chips use
- [] One chip is active at a time, and All stays the default when the view opens
- [] Selecting the chip sends `filter_selected` with `filter` set to `due_today`
- [] The chip reuses the existing filter chip component with no new visual treatment
```

Export-equivalent path: `export/NNN - task-due-today-filter-chip.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the chip labels `All` `Assigned to me` `Overdue` `Due today` and the event identifiers `filter_selected`, `filter` and `due_today`, written as the Loomlist context page and your answer write them.

Quality status: six dimensions pass. Actionability decides a task, and every checklist item names something a tester can watch on Web. Mechanism Depth comes from the planning problem in About, not from implementation reasoning, so the task stays in WHAT and WHY.

Two additions, both yours to strike:

- The checklist is derived from your answers rather than quoted from you, because the acceptance criteria question went unanswered. It reads as the testable form of the four things you settled.
- I left the empty state out. You did not say what the list shows when nothing is due today, so I assumed Due today inherits whatever the three existing chips already show on a filter with no results and wrote no copy for it. Say the word if that state needs its own treatment.

Title carries the `FE - Web - TODO` codes because the work is front end in one client and belongs to the To-dos area, and the board reads that format. Once you confirm the two points above I can adjust the file before anyone picks it up.