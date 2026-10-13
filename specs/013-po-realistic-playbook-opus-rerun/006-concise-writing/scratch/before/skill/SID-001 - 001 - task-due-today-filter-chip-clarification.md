# Due today filter chip: questions before drafting

I'll create the task for a "Due today" chip on the To-dos view. The Loomlist context covers the three chips that exist today (All, Assigned to me and Overdue), one active at a time, with All as the default. Before drafting, I need the answers below in one reply:

**Platform:** FE tasks cover one client and the title carries it, as in `FE - Web - TODO - {Title}`. Which platform is this for: Web (which Desktop picks up with no release), iOS or Android? If it is more than one, should I write one task per platform?

**What counts as due today:** Should I mirror Overdue, so the chip shows to-dos not checked off whose due date is today in the to-do owner's time zone? Or should to-dos already checked off today stay in the list?

**Back end support:** todos-service owns the To-dos view queries. Does it already return due-today results, or does this need a BE task alongside? If it needs one, the work is FS rather than a small FE task.

**Chip placement and copy:** Where does the chip sit relative to the other three chips, and is "Due today" the final label? Is there a Figma link? The label needs strings in all six shipped locales, with en-US as the fallback.

**Analytics:** The To-dos view sends `filter_selected` with `filter` set to `all`, `assigned_to_me` or `overdue`. Adding a value such as `due_today` goes through a Data team tracking plan review before client work starts. Is that value in scope for this task, already approved or left out?

**Links:** Is there a parent task, story or related ticket to reference?
