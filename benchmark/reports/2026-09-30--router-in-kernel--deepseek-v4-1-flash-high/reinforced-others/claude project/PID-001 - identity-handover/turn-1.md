```markdown
# Task clarification - Due today filter chip on the To-dos view

The context page settles the To-dos view, the chip row as it stands and the Overdue time-zone rule, so I need the open decisions below in one reply before I draft the task.

**Platform and scope**

- Which clients ship the chip: Web only, Web and Desktop together, or iOS and Android as well
- Does an existing To-dos view query support the filter already, or does todos-service need a new one, which would make this FS rather than FE
- Does the chip appear for every role and plan that can open the To-dos view

**Chip rule**

- What problem does the chip solve that the three chips above the list do not cover today
- Confirm the rule: to-dos not checked off whose due date is today in the owner's time zone, with overdue to-dos excluded
- Does a to-do with a reminder set for today but no due date belong in the chip
- Does the chip only filter the list, or does it also show a count

**Chip row and list**

- Where does the chip sit among All, Assigned to me and Overdue, and does one chip stay active at a time with All still the default
- Does the list keep sorting by due date, with to-dos that have no due date at the bottom
- What does the list show when nothing is due today

**Copy and design**

- The exact chip label, and any Figma frame or design reference for the chip row
- Does a new label ship in all six locales in this task, or later

**Analytics**

- Does `filter_selected` take a new `due_today` value alongside `all`, `assigned_to_me` and `overdue`
- If it does, does the tracking plan need Data team review before this work starts, and who owns that

**Dependencies and validation**

- Any related task, ticket, parent or thread I should link, and any target release or deadline
- Is there a reason not to add the chip, such as query cost on a large workspace or noise for members with nothing due
- What am I likely to get wrong about the rule, the chip row or the platform scope?
```

Export-equivalent path: `export/001 - task-due-today-filter-chip-clarification.md`

Quality status: clarification lane. `$task` selected Task Mode at Standard energy, and Task Mode requires the context question before drafting, so no artifact exists yet and the six-dimension artifact gate has not run. The question covers every field Task Mode needs and adds no speculative draft.

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: the enumerations `All`, `Assigned to me` and `Overdue` and `all`, `assigned_to_me` and `overdue`, both supplied by the context page and fixed by the product rather than chosen by me.

One assumption I did not turn into a question, so correct it now if it is wrong: the task title follows the house shape `FE - {Platform} - TODO - {Title}`, with TODO as the feature code and the platform segment filled once you name the client.

The task takes the next number in this lane once you answer, and the analytics enum question is the one I would not skip, because a fourth chip changes a value the Data team already reviews.