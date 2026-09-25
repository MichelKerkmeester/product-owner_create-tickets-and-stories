I've written the task for the Web "Due today" chip.

Path: `export/002 - task-due-today-filter-chip.md`
Verified: read-back succeeded; 50 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the lists "All, Assigned to me and Overdue" and "`all`, `assigned_to_me` and `overdue`" have three items because those are the existing chips and filter values.

Quality summary: every section the task template requires is there, and everything in it comes from your answer or the Loomlist context page. It covers Web only; Desktop gets the chip through the web client and iOS and Android are out of scope. The first question file, `001 - task-due-today-filter-chip-clarification.md`, is unchanged.

The task adds Due today after Overdue, reusing the existing chip component. It shows unchecked to-dos due today in the to-do owner's time zone, sorted by due date, with one chip active at a time. It uses the same "today" rule as Overdue, so a to-do moves from Due today to Overdue at the owner's midnight and is never in both lists. A second group covers the `filter_selected` event with `filter` set to `due_today`, and says the tracking plan is already updated.

**Needs your call:**
- **Back end support:** you said "front end" but didn't say whether todos-service already returns due-today results. The task assumes it does. If it doesn't, this needs a back end task too.
- **Things I added that you didn't ask for** (remove any you don't want):
  - With nothing due today, the list stays empty rather than switching back to All
  - The label needs a translated string in all six app languages, with US English as the fallback
  - A note that a to-do owned by someone in another time zone can look like it's due tomorrow or yesterday to the viewer
  - A check that the existing `all`, `assigned_to_me` and `overdue` values keep being sent as they are now
  - A check that the chip looks the same as the existing ones

I can push this to ClickUp if you want. I won't do that unless you say so.