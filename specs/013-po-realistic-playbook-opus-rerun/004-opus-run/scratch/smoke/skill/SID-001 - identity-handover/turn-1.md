I haven't written the task yet. There are a few things I need to know first, and I've saved those questions to a file.

Path: `export/001 - task-due-today-filter-chip-clarification.md`
Verified: read-back succeeded; 11 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**What I need to know:**
- **Platform:** A front end task covers one client: Web (which Desktop users get automatically), iOS or Android. Which one is this? If it's more than one, should I write one task per platform?
- **Which to-dos count:** Should the chip show to-dos not checked off that are due today in the to-do owner's time zone, the same way Overdue works? Should overdue to-dos stay out of it?
- **Chip position:** Does it go after Overdue, with only one chip active at a time and All still the default?
- **Back end and tracking:** Does todos-service already return a list of to-dos due today? The `filter_selected` event would also need a new value such as `due_today`, and the Data team reviews tracking changes before client work starts. Has that review happened, or should the task list it as a dependency?
- **Links:** Is there a Figma frame, parent task or epic to reference, including a design for when nothing is due today?

Once you answer, the task will be saved as `export/002 - task-due-today-filter-chip.md`.