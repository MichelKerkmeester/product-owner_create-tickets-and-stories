I'll create the "Due today" chip task. The Loomlist context covers the existing chips (All, Assigned to me, Overdue), so a few answers will pin down the rest:

**Platform:** An FE task covers one client. Which one is this for: Web (which also reaches Desktop with no Desktop release), iOS or Android? If you want more than one, should I write one task per platform?

**Rule:** Should "Due today" mirror Overdue: to-dos not checked off whose due date is today in the to-do owner's time zone? Should overdue to-dos stay out of it?

**Placement:** Does the chip sit after Overdue, keep the one-active-chip rule and leave All as the default?

**Back end and data:** Does todos-service already return a due-today list, or is this FE only against something still to be built? The `filter_selected` event would need a new `filter` value (for example `due_today`), and the Data team reviews tracking plans before client work starts. Is that plan already reviewed, or should the task name it as a dependency?

**Design and links:** Any Figma frame, parent task or epic to reference, including the empty state when nothing is due today?
