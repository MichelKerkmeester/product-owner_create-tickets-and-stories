I haven't written the task yet. `$t` has to ask one clarification question before drafting, so I've saved that question instead.

Path: `export/001 - task-label-webhook-fix-clarification.md`
Verified: read-back succeeded; 14 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality summary:** The file holds one question and no draft. It only asks about gaps the three context files leave open. The scope, owner, discipline code and the rejection of polling only are taken as settled.

The question covers six things:
- **Title and ticket:** whether my suggested title works, and whether this task should update the "label webhook ticket" Noor mentions in the thread.
- **Duplicate-shipment guard:** whether it applies only when a shipment is created again after a failure, or to every new shipment. It also asks which statuses count as an "open" shipment.
- **Open carrier question:** whether a `SERVICE_UNAVAILABLE` failure can later be followed by a `label.created`. The API notes leave this unanswered.
- **The 10-minute GET:** what it should do when it finds `label_failed` or gets a `429`, since the thread doesn't say.
- **Other failure codes:** whether handling for `ADDRESS_INVALID` and `OTHER` stays unchanged.
- **Testing:** whether QA should rerun the 2026-09-15 slow-warehouse conditions.

Once you answer, the task will be saved as `export/002 - task-label-webhook-fix.md`.