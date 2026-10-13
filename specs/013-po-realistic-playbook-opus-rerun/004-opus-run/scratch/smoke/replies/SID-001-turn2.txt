I've written the Web task for the "Due today" chip on the To-dos view.

Path: `export/002 - task-due-today-filter-chip.md`
Verified: read-back succeeded; 56 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality summary:** Everything in it comes from your answers or `context/loomlist-context.md`. The task has an About section and three checklist groups: the chip, the list it shows and the tracking event. The title follows the naming rule in the context file: `FE - Web - TODO - Due today filter chip`. There are no Figma or Epic references, since you said there's no Figma and nothing depends on it. The earlier question file (001) is unchanged.

The chip uses the existing chip component and sits right after Overdue. Only one chip can be active at a time, and All stays the default. It shows to-dos not checked off that are due today in the owner's time zone, sorted by due date. Selecting it sends `filter_selected` with `filter` set to `due_today`, which Yara has already added to the tracking plan.

**Things I added that you didn't state (remove any you don't want):**
- A to-do owned by someone in another time zone counts when it's due today in the owner's time zone, even if the viewer's date is different
- The list only shows to-dos the member can open, the same as the rest of the To-dos view
- The other three `filter` values are still sent as before
- The event includes the standard properties listed in the context file

**Not in the task, because you didn't answer or mention them:**
- Whether todos-service already supports a "due today" query
- What the view shows when nothing is due today
- Translations of the "Due today" label for the other five languages the app ships in

Tell me if any of these should go in.