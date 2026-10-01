```
I'll create your task. Quick questions:

**Format & scope:**
Front end work in one client. Which platform shows this chip, Web, Desktop, iOS, Android, or all of them?

**Requirements:**
- Does Due today join All, Assigned to me and Overdue as a fourth chip, keeping one chip active at a time with All as the default?
- Which to-dos appear under it, only those whose due date is today, or overdue to-dos as well?
- What is the exact chip label copy, and what does the list show when nothing is due today?
- Which acceptance criteria should QA check?

**Design & platform:**
- Is there a Figma reference for the chip?
- Do four chips need to fit one row, scroll, or wrap on a narrow window or a phone?

**Dependencies:**
- Does this task cover the `filter_selected` value the new chip sends, or does the Data team tracking-plan review become a separate ticket?
- Any parent or related task for the To-dos view filters?

**Validation:**
- Should I assume Overdue and Due today stay separate chips rather than becoming one combined filter?
- What should I not assume about the owner's time zone, to-dos with no due date, or the list sort order?
```

Export-equivalent path: `export/NNN - task-due-today-filter-chip-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the chip labels `All`, `Assigned to me`, `Overdue` and `Due today`, and the event name `filter_selected`, written as the supplied Loomlist context writes them.

Quality status: clarification gate passed. Clarity and completeness read against the Task intake question, the assumption challenge asks about the overdue boundary, the time zone and the sort order, and no draft is rendered ahead of your answer.

Routed mode: Task Mode, selected by the explicit `$task` command at standard energy, with the Loomlist context page consulted for the chips that exist today. The three open items it cannot settle are the platform, whether Due today includes overdue to-dos, and the acceptance criteria, so the question above covers them in one pass. Answer it and I will draft the task next.