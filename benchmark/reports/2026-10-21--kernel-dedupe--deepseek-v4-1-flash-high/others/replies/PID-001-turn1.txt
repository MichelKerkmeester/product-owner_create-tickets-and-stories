```markdown
# Task intake: Due today filter chip on the To-dos view

The request settles the surface, the artifact and the chip label `Due today`. Eight points are open before I draft, and each carries a recommended answer so a single yes takes all eight.

**1. Platform**
The To-dos view runs on Web, Desktop, iOS and Android, and FE covers one client.
Recommended: Web only, because Desktop wraps the web client and picks the chip up on its next load with no Desktop release.

**2. Chip position**
Three chips exist today: All, Assigned to me and Overdue, one active at a time with All the default.
Recommended: a fourth chip after Overdue with Overdue kept, because the two ask different questions and Overdue covers due dates before today.

**3. Filter rule**
Overdue shows to-dos not checked off whose due date is before today in the owner's time zone.
Recommended: to-dos not checked off whose due date is today in the owner's time zone, because it reuses the rule Overdue applies and the time zone convention the context page sets for due dates.

**4. Empty result**
The context page describes no message for a chip that matches nothing.
Recommended: a short message naming the filter, because a blank list under an active chip reads as a failed load.

**5. Service scope**
The To-dos view queries live in `todos-service`.
Recommended: front end only, filtering the list the client already holds, because a new query makes this an FS ticket with a `todos-service` change beside it.

**6. Analytics**
The view sends `filter_selected` with `filter` set to `all`, `assigned_to_me` or `overdue`, and a new event goes into a tracking plan the Data team reviews before client work starts.
Recommended: a fourth value `due_today` on `filter_selected`, with the Data review as a dependency, because a filter the warehouse cannot read is a filter nobody can measure. Confirm whether an added value needs that review or only a new event does.

**7. Acceptance criteria**
The request names none, so I would write them from the answers above.
Recommended: six criteria covering the chip label and position, the active state with All still the default, the list contents, a to-do with no due date staying out, the empty case and the `filter_selected` payload.

**8. Design reference**
No design link is supplied.
Recommended: a Figma frame for the chip row if design has one, because the reference block holds supplied links only and stays out of the ticket when there are none.

Anything I should not assume about the chip, the list or the owner's time zone goes in the same answer.
```

Export-equivalent path: `export/NNN - task-due-today-filter-chip-clarification.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: not scored, clarification only | Kind: Task | Energy: Standard

The question settles the platform, the chip's place beside Overdue and the filter rule with its owner time zone. It also covers the empty result, whether a `todos-service` change rides along, the `due_today` event value, the acceptance criteria and the design reference. The task comes next once you answer.

### Open items
None identified

Answer in one message and I'll draft the task.