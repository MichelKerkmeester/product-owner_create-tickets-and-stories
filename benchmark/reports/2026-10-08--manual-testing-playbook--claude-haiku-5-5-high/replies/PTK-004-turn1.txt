```markdown
I'll create the parent task and its four subtasks. Before drafting, I need the decisions below in one response.

**Parent scope:** Should the parent cover the whole brief, with iOS, Android, Web and BE as its children? Desktop stays inside the Web subtask, as the brief says.

**Titles:** Loomlist's convention gives the parent no platform and gives each child its own. I propose:

- Parent: `FS - TODO - Recurring to-dos`
- iOS: `FE - iOS - TODO - Recurring to-dos`
- Android: `FE - Android - TODO - Recurring to-dos`
- Web: `FE - Web - TODO - Recurring to-dos`
- BE: `BE - TODO - Recurring to-dos`

Confirm these, or name a different feature code.

**Design:** The brief names three Anouk frames but gives no links. Send the Figma links for Repeat picker, Custom interval and Occurrence menu, and say whether they are approved or still in review.

**Free plan:** The brief opens the upgrade sheet on Free, and the Loomlist context names Web as the only surface for billing changes. On iOS and Android, does the sheet link to Web or offer an in-app path?

**Tracking:** Should Yara's tracking-plan review be a named dependency on the parent? Which subtask fires `todo_repeat_set` and `todo_occurrence_skipped`: each client, or BE?

**Reminder hand-off:** Is the format for handing the next reminder to reminders-service already agreed? If not, I will name it as a BE dependency.

**Open item:** The brief leaves open whether a series shows past occurrences in activity until Ines decides. Should the parent name it as open, or leave it out?

**Since planning:** Did anything change after the 10 September planning session that the brief does not show?

Unless you say otherwise, I will write each child's checklist only from what the brief states.
```

Export-equivalent path: `export/NNN - task-recurring-todos-parent-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality status: not scored. This is a clarification with no draft.

`$task` asks its context question before drafting, even with a full brief. Answer the points above and I will draft the parent and the four subtasks. The artifact comes next once you reply.