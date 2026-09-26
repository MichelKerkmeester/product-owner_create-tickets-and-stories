```markdown
# Recurring to-dos parent task and subtasks, clarification

I'll write the parent task and its four subtasks from Ines's brief of 2026-09-08. The brief already covers behavior, limits, plans, rollout and ownership. Please answer the open points below in one reply:

**1. Titles and codes:**
- I plan to use `FS - TODO - Recurring to-dos` for the parent. The subtasks would be `FE - iOS - TODO - Recurring to-dos`, `FE - Android - TODO - Recurring to-dos`, `FE - Web - TODO - Recurring to-dos` and `BE - TODO - Recurring to-dos`
- Should the BE subtask keep TODO, or use REM because it hands the next reminder to reminders-service?
- Do you want different title wording for any of them?

**2. Where the shared behavior goes:**
- Option A: the parent states the member rules once. That covers the options table, Ends, Skip this one, the 500 limit, time zones and Free gating. Each subtask then keeps only its own surface and checks
- Option B: the parent only links its subtasks
- Desktop gets the feature through the web client. Should the Web subtask name Desktop in its checks?

**3. Tracking and rollout:**
- The context page says tracking plans belong to DATA. Should I add a fifth subtask, `DATA - TODO - Recurring to-dos tracking plan`, for `todo_repeat_set` and `todo_occurrence_skipped`? Or should Yara's review stay as a blocker line in the parent?
- Which side sends each event: each client, BE or both? The brief doesn't say
- The flag rollout is Data's work after release. Should it stay in the parent's About as context only?

**4. Gaps in the brief:**
Unless you give a rule, I'll leave each of these out of the checklists and list it as open in the parent:
- A Monthly series that starts on the 29th, 30th or 31st, when it reaches February
- Custom every N months: does it follow the same day-of-month rule as Monthly?
- A member unchecks the occurrence they checked off: does the new occurrence go away?
- A member removes the due date from a repeating to-do
- A Plus or Team workspace moves down to Free while it has active series
- Can a guest with edit access set Repeat?

**5. Links:**
- Do you have ClickUp URLs for the parent, the subtasks or an Epic? Do you have Figma links for `Recurring to-dos / Repeat picker`, `Recurring to-dos / Custom interval` and `Recurring to-dos / Occurrence menu`? If not, I'll name each one as plain text and won't make up a link

**6. Validation:**
- Did anything change after the brief was posted that I should know about?
```

Export-equivalent path: `export/001 - task-recurring-todos-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: Oxford comma in the event question. Kept with reason: bold-plus-colon intake headers, which the interactive intake format requires.

Quality status: this is the clarification only. The task set hasn't been drafted or scored yet.

`$task` always asks its questions before drafting, so I haven't started the tasks. The brief is detailed, so the questions only cover what it leaves open:

- **Titles and codes:** I've proposed titles that follow the board's naming rules. You only need to confirm whether BE uses TODO or REM.
- **Structure:** whether the shared rules sit once in the parent.
- **Tracking:** whether Data's tracking work gets its own subtask.
- **Gaps:** six edge cases the brief doesn't cover.
- **Links:** the missing ClickUp and Figma links.

Once you reply, the parent and its subtasks will each come as a separate block, numbered after this one.