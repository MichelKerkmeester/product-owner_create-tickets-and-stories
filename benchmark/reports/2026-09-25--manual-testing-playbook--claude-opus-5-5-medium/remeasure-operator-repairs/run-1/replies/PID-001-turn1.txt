```markdown
# Due today filter chip: task clarification

I've read context/loomlist-context.md. The questions below cover what it leaves open. Please answer them all in one reply and I'll write the task from your answers.

**1. Platform**

- An FE task covers one client. Is this for Web, iOS or Android? A Web change also reaches Desktop the next time it loads, with no Desktop release
- If it's for more than one platform, should I write one task per platform?

**2. Problem and audience**

- What problem does the chip solve, and who is it for? Examples: Theo checking what his agency has due today, or a mobile member checking off the day's to-dos

**3. What counts as due today**

- Should it follow the Overdue rule: the to-do isn't checked off and its due date is today in the to-do owner's time zone?
- Or should to-dos that were checked off today stay in the list?

**4. Chip placement and behavior**

- Where should it sit next to All, Assigned to me and Overdue?
- Does the one-active-chip rule still apply? If so, Due today can't be combined with Assigned to me
- What should the chip label and the empty state say when nothing is due today?
- The app ships in en-US, de-DE, fr-FR, es-ES, ja-JP and pt-BR. Will translations be supplied, or does this task include them?

**5. Back end and data dependencies**

- todos-service owns the To-dos view queries. Does a due-today query already exist, or does this task depend on a BE ticket? If the client can't filter this by itself, the work becomes FS or needs a paired BE task
- Today `filter_selected` sends `all`, `assigned_to_me` or `overdue`. Should a `due_today` value be added? The Data team reviews new tracking before any client work starts, so has that review happened, or should I list it as a dependency?

**6. Design and acceptance**

- Is there a Figma link for the chip and its empty state?
- Do you already have acceptance criteria, or should I draft them from your answers so you can remove any you don't want?

**7. Validation**

- What am I likely to get wrong about this chip?
```

Export-equivalent path: `export/001 - task-due-today-filter-chip-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality status:** This is a clarification, so it has no artifact score. It asks everything in one message and doesn't answer its own questions.

**Summary:** `$task` means I ask before drafting, even for a small task, so I haven't written the task yet. I've already taken these from the context page: the title format (`FE - {Platform} - TODO - ...`), the three current chips, the Overdue time-zone rule and the `filter_selected` event values. The open points are the platform, what "due today" means, the chip's placement and behavior, and whether it depends on back-end or tracking-plan work. Once you answer, the task will be `export/002 - task-due-today-filter-chip.md`.