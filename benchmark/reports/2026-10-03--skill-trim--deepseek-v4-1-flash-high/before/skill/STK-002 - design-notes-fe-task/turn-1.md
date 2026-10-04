**Path:** `export/001 - task-stay-limits-date-picker.md`

**Verified:** read-back succeeded; 170 lines

**HVR self-scan:** 0 hard blockers. Fixed: none. Kept with reason: none — headings are sentence case, UI copy is carried in backticks exactly as Ines signed it off.

**Quality summary**
*   Routing: `$task` → Task Mode, Canonical Task template, numbered requirement groups, `- []` checklists, `---` dividers
*   Title follows the ticket convention `{Discipline} - {Surface} - {Feature code} - {Title}`: `FE - Guest app - SRCH - Stay limits in the date picker`
*   Accuracy: every limit, state, copy key and edge case traces to Ines's notes, with supplied values (`1 night`, `30 nights`, `365 days`, `14 nights`, `45-night`, the six keys) kept verbatim
*   Completeness: five limits, four picker states, helper text and accessibility behaviour, the copy table, four edge cases and the platform layout rules are all covered
*   Relevance: no tracking, pricing or flexible-dates work enters the task, and the notes' "Not in this work" list is carried as a scope boundary
*   Size: 886 words, inside the 900-word task budget

**Summary**
The task hands the front end the picker's stay limits as outcomes a build can verify: the `1 night` to `30 nights` stay range, the `365 days` check-in window, and the property-page minimum stay, all read from services rather than hard-coded. It also fixes the four picker states, the grey-day helper text (including the screen-reader announcement), the six copy keys, and the documented edge cases for re-picking, earlier searches, month breaks and week start.

Two judgement calls are worth a look. Guest app is read as iOS, Android and web together, per the conventions file, so this stays one FE task rather than three. The feature code is `SRCH` because the date picker belongs to the Search area, even though the property-page minimum stay is applied by the same picker component.