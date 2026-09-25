I wrote a parent task for recurring to-dos plus four subtasks (iOS, Android, Web, BE) and saved all five to `export/`.

Path: `export/001 - task-recurring-todos-parent.md` (`FS - TODO - Recurring to-dos`)
Verified: read-back succeeded; 139 lines

Path: `export/002 - task-recurring-todos-ios.md` (`FE - iOS - TODO - Recurring to-dos`)
Verified: read-back succeeded; 100 lines

Path: `export/003 - task-recurring-todos-android.md` (`FE - Android - TODO - Recurring to-dos`)
Verified: read-back succeeded; 101 lines

Path: `export/004 - task-recurring-todos-web.md` (`FE - Web - TODO - Recurring to-dos`)
Verified: read-back succeeded; 102 lines

Path: `export/005 - task-recurring-todos-be.md` (`BE - TODO - Recurring to-do occurrences, Ends and workspace limit`)
Verified: read-back succeeded; 115 lines

HVR self-scan: 4 hard blockers. Fixed: "offers" used in place of "has" (copula avoidance), 1 in the parent and 1 in each client subtask. Kept with reason: none.

**Quality:** All six quality checks pass at their minimum or better. Every value in Ines's brief made it into the tasks unchanged: the Repeat options, 1–99 for Custom, 1–365 for After, the 500 limit, the sheet and hint copy, the `recurring_todos` flag, both events and the 10% at 8 weeks goal. Titles follow the board's naming format, and the parent is FS because it covers both front end and back end work.

The parent states the shared rules once and links to each subtask. Each subtask links back to the parent and to the related subtasks. The three client subtasks are near-identical, as the brief says ("Same as iOS"). They differ on reminders: iOS and Android deliver them as notifications on the device, while Web shows them only while the app is open. The Web subtask also has a check that everything works in the Desktop app, since Desktop runs the web client.

**Things I added that aren't in the brief (delete if unwanted):**
- **BE, two edge cases:** checking off the same to-do on two devices before they sync still creates only one next occurrence. A to-do checked off from an older app version without Repeat still gets its next occurrence.
- **Wording:** "owner" in the brief became "to-do owner" (the person the to-do is assigned to), so it isn't confused with the workspace Owner role.

**Gaps for Ines:**
- The brief doesn't say which surface sends `todo_repeat_set` and `todo_occurrence_skipped`. Each subtask sends whatever the tracking plan Yara reviews assigns to it.
- It doesn't say whether BE also blocks Repeat on Free workspaces or only the apps hide it.
- It doesn't say what happens when a checked-off occurrence is unchecked.
- Showing past occurrences in a to-do's activity is recorded as deferred, and Ines decides after full rollout.

I can push these to ClickUp if you want, but I'll wait for your go-ahead first.