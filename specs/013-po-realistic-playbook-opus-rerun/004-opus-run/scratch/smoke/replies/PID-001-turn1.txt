```markdown
I'll create your "Due today" chip task. Before drafting, I need the answers below in one reply.

**Platform:**
- FE covers one client. Which one is this task for: Web, iOS or Android?
- A Web change also reaches Desktop the next time Desktop loads. Should the task call Desktop out, or is Web enough?
- If you want it on more than one platform, should I write one task per platform?

**What the chip shows:**
- Should "Due today" follow the Overdue rule: not checked off, and due date equal to today in the to-do owner's time zone?
- Should to-dos checked off today still show under the chip, or drop out like they do under Overdue?
- Should overdue to-dos stay out of "Due today"?
- Is the chip limited to what the member can already open in the To-dos view, the same as the other chips?

**Chip row behavior:**
- Where does the chip sit: after Overdue, or somewhere else?
- One chip active at a time with All as the default still holds. Is that right?
- What should the list show when nothing is due today? Is there copy or a design for that empty state?

**Why and success:**
- Who is this for, and what problem does it solve? For example, Theo checking what his team has to finish today
- What does success look like for you?

**Dependencies:**
- todos-service owns the To-dos view queries. Does it already return due-today to-dos, or is back end work needed? If it is, this becomes FS or needs a paired BE task
- The To-dos view sends `filter_selected` with `filter` set to `all`, `assigned_to_me` or `overdue`. Should the new chip send `due_today`? New values go into a tracking plan the Data team reviews before client work starts. Is there a tracking plan ticket to link?
- The app ships in 6 locales. Is the chip label copy ready, or should the task require translations?

**Design and links:**
- Figma link for the chip and empty state?
- Any parent task, epic or related tickets to reference?

**Validation:**
- What am I likely to get wrong about this chip?
```

Export-equivalent path: `export/001 - task-todos-due-today-filter-chip-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality: this is a clarification block, so it holds only the questions and no task draft. I haven't scored a draft yet.

**What's missing before I can draft:** `$task` still requires one round of questions before a draft. `loomlist-context.md` gives the current chips (All, Assigned to me and Overdue), the owner time zone rule and how analytics are named. It doesn't cover these:
- **Platform:** FE covers one client, and the title needs a platform: `FE - {Platform} - TODO - …`.
- **The chip's rule:** exactly which to-dos "Due today" should show.
- **Back end support:** whether todos-service can already return due-today to-dos.
- **Tracking plan:** the Data team must review a tracking plan before client work starts.

Once you answer, I'll write the task as the next number in the task lane. You can also send `$quick` if you'd like me to draft now and set defaults for these open points myself, and I'll list each default so you can change it.