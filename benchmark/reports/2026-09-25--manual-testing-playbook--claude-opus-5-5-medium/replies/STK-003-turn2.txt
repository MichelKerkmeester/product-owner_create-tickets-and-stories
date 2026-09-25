I've updated the task with your four points. It keeps the same filename.

Path: `export/001 - task-label-webhook-fix.md`
Verified: read-back succeeded; 124 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** all six dimensions are at or above their floors. Your done definition now closes the task as group 6, Done, with its two checks word for word.

- **Board and deadline:** About now says the task sits on the Fulfilment board with no parent task and has to be live before the November peak.
- **Warehouse system timeout:** group 1 moves the warehouse system call out of the request and into the queued work, and it keeps the 8-second timeout. Group 2 now says a call that hits that timeout doesn't count as processed, so the event is tried again.
- **Late `label.created`:** group 4 now says one that arrives after the 10-minute GET took the label changes nothing. That means no second label copy, no new tracking number and no warehouse system call. The reverse case stays: a GET that returns a label already taken from the webhook isn't processed again.

**What I cut:** I replaced the earlier Verification group with your done definition. Its checks for the signature, alerting and a missing webhook weren't in your definition, so they're gone from the done checks. Those behaviours are still required in groups 1, 4 and 5.

**Decisions for you:**
- **Peak date:** no date was supplied, so the task says "before the November peak". I can add the date if you want one on the board.
- **Staging replay:** the task doesn't say whether staging calls the carrier's test environment or a stand-in, because none of the sources say.

Joris still needs to confirm the three open notes, two with Noor and one with the carrier.

If you want this on the Fulfilment board, I can push it to ClickUp once you say so.