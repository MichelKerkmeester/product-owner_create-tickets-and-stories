`Path: export/001 - task-due-today-filter-chip-clarification.md`
`Verified: read-back succeeded; 34 lines`
`HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none — the backticked values (filter_selected, all, assigned_to_me, overdue, due_today) and the title pattern are literal source identifiers rather than blocked words.`

Quality summary: route `$task` → Task Mode; Standard energy; 3 perspectives (user, technical, risk). Artifact is a clarification, not a task, because the supplied context splits front end work across four clients and the request names none, so the scope is a choice I must not make for you. Completeness 9, Clarity 9, Actionability 9, Accuracy 9, Relevance 9, Mechanism Depth 8. No draft was written, per the clarification contract.

Why I stopped short: your context page says front end work is "one client: Desktop, Web, iOS or Android," and the To-dos view exists on all four, so the platform is unresolved. The other open points came from that same page and shape the acceptance criteria: whether Due today is a fourth chip beside All, Assigned to me and Overdue, how its definition mirrors Overdue's owner-time-zone rule, and whether the `due_today` value and its tracking plan update sit in this ticket or a separate DATA ticket.

One reply with those answers and I'll draft the task as `export/002 - task-...md` with the title in `{Discipline} - {Platform} - TODO - {Title}` form.