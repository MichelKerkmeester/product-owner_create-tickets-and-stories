```markdown
I'll create your task. Before drafting, I need the answers below in one reply.

**Format & scope:**
- This is front end (FE) work under the TODO feature code. Each FE task covers one client, so the title will read `FE - {Platform} - TODO - Due today filter chip`
- Which client is this for? A Web change also reaches Desktop the next time it loads, with no Desktop release
- If iOS and Android need the chip too, should I write one task per platform or an FS parent that splits into them?

**Requirements:**
- What counts as "due today"? I'd start from the Overdue rule: not checked off, with a due date equal to today in the to-do owner's time zone. Should to-dos already checked off today or overdue to-dos also appear?
- Where does the chip go relative to All, Assigned to me and Overdue? Does the one-active-chip rule still apply?
- What should the list show when nothing is due today?
- Do you already have acceptance criteria you want included?

**Design & platform:**
- Is there a Figma link for the chip and the empty state?

**Dependencies:**
- Does todos-service already support a due-today query, or does this need a BE ticket first?
- Analytics: `filter_selected` would need a new `filter` value, most likely `due_today`. The Data team reviews tracking plan changes before any client work starts. Has that been approved, or should I list it as a blocking dependency?
- The app ships in six locales (en-US, de-DE, fr-FR, es-ES, ja-JP and pt-BR). Who provides the chip label strings?
- Are there any related or dependent tickets?

**Validation:**
- You called this small. I read that as meaning the query already exists and only the chip is new. Is that right?
- What else am I likely to get wrong?
```

Export-equivalent path: `export/001 - task-due-today-filter-chip-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I haven't drafted the task yet because `$task` needs your answers first. I'll write it once you reply.

The questions are based on the Loomlist context file. They cover the three existing chips, the rule that only one chip is active at a time, how Overdue uses the to-do owner's time zone, and the rule that analytics tracking plans are reviewed before client work. Two things in the questions are my own suggestions, not from the context: defining "due today" the same way as Overdue, and naming the analytics value `due_today`. Correct either one in your reply if it's wrong.