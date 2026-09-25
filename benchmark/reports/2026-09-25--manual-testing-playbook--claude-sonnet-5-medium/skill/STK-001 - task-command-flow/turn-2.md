Path: `export/002 - task-creator-payout-pause-indicator.md`
Verified: read-back succeeded; 60 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality summary:** All six dimensions are at or above their floors. Accuracy is the tightest, because every requirement traces to your three acceptance points.

I wrote this as a standalone task with three requirement groups: the required pause reason, the indicator in the payout row, and the pause and reason in payout history. The QA end-to-end check is the last item in the third group.

I added or assumed a few things you should check:
* **Blank reasons:** I treat an empty reason as missing. The pause is rejected and the payout stays unpaused.
* **Scope line:** About says who can pause a payout and how a pause ends are out of scope. You didn't say that, so remove it if those belong here.
* **Page reference:** The `Creator payouts` page name is a placeholder because you gave no Figma link or page name.
* **Not covered:** Creator notifications, admin-side views and the pause trigger.

I can send this to ClickUp if you approve. Tell me if you want any of the above changed first.