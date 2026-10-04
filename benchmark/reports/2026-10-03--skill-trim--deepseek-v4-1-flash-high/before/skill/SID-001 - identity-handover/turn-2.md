`Path: export/002 - task-due-today-filter-chip-web.md`
`Verified: read-back succeeded; 54 lines`
`HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none — the three-item lists (chip set, platform list, filter enum) are source-fixed content taxonomies rather than the triad tic, and the backticked values (filter_selected, due_today, all, assigned_to_me, overdue) are literal identifiers.`

Quality summary: `$task` → Task Mode, Standard energy, 3 perspectives (user, technical, delivery). Word count 390 against the 900-task cap, so one requirement group per surface rather than padding. Completeness 9, Clarity 9, Actionability 9, Accuracy 9, Relevance 9, Mechanism Depth 8. Title follows `FE - Web - TODO - {Title}`, with the apps and Desktop excluded because the answer named them as later or automatic. One conciseness pass removed a design-constraint sentence About repeated from requirement 1.

Two lines are mine rather than yours, so strike them if they overreach: the regression guard that switching back to another chip restores its existing results, and the note that the other chips keep sending `all`, `assigned_to_me` and `overdue`. The Desktop-inheritance sentence and the no-due-date-at-bottom sort detail come from your reply and the Loomlist context page.

Your earlier clarification stays at `export/001 - task-due-today-filter-chip-clarification.md`, untouched. Next step if useful: I can add a `**User Story**` block to requirement 2, or split the analytics item into its own ticket if Data wants it separate.