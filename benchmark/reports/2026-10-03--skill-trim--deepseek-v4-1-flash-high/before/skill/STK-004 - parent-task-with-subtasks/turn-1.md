All five artifacts are saved and read back.

`export/001 - task-recurring-to-dos.md`

Verified: read-back succeeded; 158 lines

`export/002 - task-recurring-to-dos-ios.md`

Verified: read-back succeeded; 116 lines

`export/003 - task-recurring-to-dos-android.md`

Verified: read-back succeeded; 116 lines

`export/004 - task-recurring-to-dos-web.md`

Verified: read-back succeeded; 116 lines

`export/005 - task-recurring-to-dos-be.md`

Verified: read-back succeeded; 109 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `Repeat`, `Ends` and `Skip this one` are the supplied UI labels, and `recurring_todos`, `todo_repeat_set`, `todo_occurrence_skipped`, `Add a due date to repeat` and `This workspace has 500 repeating to-dos. End one to add another.` are literal identifiers and copy, repeated rather than reworded.

Quality summary: Accuracy and Relevance hold because every claim traces to the brief and the shared values (`recurring_todos`, 1 to 99, 1 to 365, 500, the two events and their enum values, the flag rollout) stay verbatim. Completeness covers the four named subtasks, Desktop inheriting through Web, the plan gate, the time-zone rule and the out-of-scope list. Actionability holds through `- []` checklists a QA engineer can verify. Clarity and mechanism depth hold because the parent states each shared rule once and the subtasks reference it. Parent 868 words, subtasks 464 to 502 words, all inside budget.

Summary: The parent is titled `FS - TODO - Recurring to-dos` because it splits FE and BE, and it lists four linked subtasks under the board title format, `FE - iOS/Android/Web - TODO - Recurring to-dos` and `BE - TODO - Recurrence engine`. The shared rules (repeat options, Ends, occurrences, the 500 limit, owner time zone, plans and flag, tracking) live once in the parent, and each subtask carries only its own client or engine work. Desktop gets no subtask, since the brief routes it through the web client.

Three additions to confirm or strike, since the brief did not name them: the BE ticket title `Recurrence engine`, the assignment of the two tracking events to the three client subtasks, and the parent linking its four sibling subtask files. Also note that `context/loomlist-recurring-todos-parent-task.md` already holds a board parent for this work, and the PM's open item on past occurrences in the activity is recorded in the parent as out of the first release. Tell me if you want the subtasks wired to that existing ticket, the parent synced to it, or the tracking events moved onto a Data ticket.