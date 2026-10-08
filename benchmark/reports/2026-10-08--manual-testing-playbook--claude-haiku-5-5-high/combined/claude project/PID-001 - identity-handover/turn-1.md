```markdown
# Due today filter chip clarification

I'll write the task once these points are settled. Please answer all of them in one reply.

1. Which clients get the chip: Web, Desktop, iOS, Android or a subset? Each client needs its own FE task
2. Can the chip filter the To-dos view data the app already loads, or does todos-service need a new query for it? A service change makes this FS work, not FE
3. Confirm the definition: a to-do not checked off whose due date is today in the owner's time zone, matching Overdue? Say what changes if not
4. Should a to-do that is checked off and due today appear under this chip? I propose no
5. Confirm placement and rules: a fourth chip after Overdue, one chip active at a time, All as the default? Say what changes if not
6. What should the list show when nothing is due today?
7. The chip label ships in six locales. Do translations come with this task or in a separate ticket?
8. Should the chip send `filter_selected` with `filter` set to `due_today`? The value is new, and new events need a tracking plan the Data team reviews before client work starts. Has that review happened?
9. What must be true when this is done? Share the outcomes you expect, or say what a tester checks first
10. Is there a Figma frame for the chip, or related tasks?
11. I am assuming the chip sits beside Overdue and does not replace it. Confirm or correct
```

Export-equivalent path: `export/NNN - task-due-today-filter-chip-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality status: clarification only. No draft yet, because the platforms, the data source and the analytics review are still open and the acceptance criteria are missing.

I read `context/loomlist-context.md`. It confirms the To-dos view has three chips today (All, Assigned to me, Overdue) and that Overdue uses the owner's time zone. Question 2 matters most: if the filter needs a todos-service change, this is FS work and the title and discipline code change. The task follows once you answer.