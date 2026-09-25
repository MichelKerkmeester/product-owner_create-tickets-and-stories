I haven't written the task yet. The request leaves open a few things that change what the task is, so I saved one set of questions to answer first.

Path: `export/001 - task-due-today-filter-chip-clarification.md`
Verified: read-back succeeded; 16 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the lists "All, Assigned to me and Overdue", "Web, iOS or Android" and "`all`, `assigned_to_me` or `overdue`" are three items each because the Loomlist context fixes those values.

Quality: this is a clarification file, so it holds only the questions and no draft.

1. **Platform:** Is this for Web (Desktop picks it up with no release of its own), iOS or Android? The task title names the platform, as in `FE - Web - TODO - …`.
2. **What "due today" means:** Should it work like Overdue, showing unchecked to-dos due today in the to-do owner's time zone? Or should to-dos checked off today stay in the list?
3. **Back end:** todos-service runs the To-dos view queries. If it can't already return due-today results, this needs back end work too and isn't a small front end task.
4. **Placement and label:** Where does the chip sit next to the other three chips, and is "Due today" the final label? Is there a Figma link?
5. **Analytics:** Tracking the new chip means a new value such as `due_today` in the `filter_selected` event. The Data team has to review that before client work starts, so is it in scope, already approved or left out?
6. **Links:** Is there a parent task, story or related ticket?

Once you answer, the task will be saved as `export/002 - task-due-today-filter-chip.md`.