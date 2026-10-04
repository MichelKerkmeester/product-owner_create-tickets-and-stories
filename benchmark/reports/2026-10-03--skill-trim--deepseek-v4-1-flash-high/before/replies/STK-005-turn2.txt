`export/002 - task-android-recurring-todos.md`

Verified: read-back succeeded; 197 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the three-item enumerations `days, weeks or months` and `never, on date, after`, kept because the parent's own rule fixes those options, and `carries` in the reminder and assignee items, kept because it is the parent's own wording.

**Quality summary**

*   Template: Subtask scaffold, H1 board title `FE - Android - TODO - Recurring to-dos`, `## About`, `### Requirements`, three optional context labels (`Flows`, `Parent task`, `Related tasks`), `---` dividers as Task Mode requires
*   Requirements: eleven numbered groups across three categories, every actionable line a `- []` checklist item, WHAT and WHY only, no build steps
*   Supplied values carried as written in backticks: `recurring_todos`, `daily`, `weekdays`, `weekly`, `monthly`, `custom`, `1` to `99`, `1` to `365`, `500`, `never`, `on date`, `after`, `todo_repeat_set`, `todo_occurrence_skipped`, `Skip this one`, the limit sheet copy and the release version `5.4.0`
*   No fabricated Figma or ClickUp URLs, no `[Assumes: ...]` tags, no scope beyond the Android client

The parent's shared rules stay stated once, and the subtask restates only the values its Android checks must verify, so the group is QA-ready without drift. The engine boundary is fixed in the artifact: Android renders the next due date BE returns and derives no date from the device, which is now a checklist item rather than an assumption.

One gap left open: the Android Figma links for the three flows were not supplied, so the flows are named as plain text rather than dead links. Send them whenever they exist and the three bullets become ordinary links, and the file stays at this path.

Your source material in `context/` was read only and is unchanged.