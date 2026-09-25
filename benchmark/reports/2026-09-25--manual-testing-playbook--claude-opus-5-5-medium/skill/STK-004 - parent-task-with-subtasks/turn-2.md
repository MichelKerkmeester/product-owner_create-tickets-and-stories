I updated the parent task in place, under the same filename.

Path: `export/001 - task-recurring-todos-parent.md`
Verified: read-back succeeded; 152 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** All six quality checks pass at their minimum or better. Every value from Ines's brief is still in, and the release plan you gave is new: iOS and Android aim for 5.4.0, and Web and BE ship dark before that.

- **Shared rules:** these are now the only place the rules are written, numbered 1 to 5, so each subtask can point at them. Two parts that were only in the old subtasks moved up into them: the repeat icon on the to-do row (rule 2), and how each surface delivers the next reminder (rule 3).
- **Subtasks:** the four are listed as plain titles, with no links yet: `FE - iOS - TODO - Recurring to-dos`, `FE - Android - TODO - Recurring to-dos`, `FE - Web - TODO - Recurring to-dos` and `BE - TODO - Recurring to-dos`. Each has one line on its scope from the brief and its release target. The Web line says every check must also pass in the Desktop app, because Desktop runs the web client.
- **Rule 5:** says Data turns the flag on once all three clients are out. With iOS and Android on 5.4.0, that means after 5.4.0 is out on both. The brief doesn't say whether "out" means the release has started or its 7-day rollout has finished.

The two BE edge cases I added last time aren't in the parent. They were one check-off on two devices creating a single next occurrence, and check-offs from older app versions. The BE lead can add them if they want them.

The four subtask files from the previous turn (`002` to `005`) are still in `export/`. I didn't delete them, but you can drop them since the leads will write their own.

I can push the parent to ClickUp if you want, but I'll wait for your go-ahead first.