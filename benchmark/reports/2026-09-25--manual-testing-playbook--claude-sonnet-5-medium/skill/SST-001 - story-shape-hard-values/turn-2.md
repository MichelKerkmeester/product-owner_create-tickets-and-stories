Path: `export/002 - PRD-payout-pause.md`
Verified: read-back succeeded; 78 lines
Kind: Story
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality summary: all four supplied hard values are in Requirements with their notation intact (`24 hours`, the required reason, `Pause payout`, the `paused` badge). Acceptance has three outcome-led criteria: pause with a reason, refusal without one, and automatic release. No Delivery section, because you didn't ask for one and no open question forced it.

I added a few things your notes didn't state, so please check them:
* The area segment "Payouts" in the title.
* The Problem line, which restates your "when it needs to hold it".
* Criterion 2, the refusal when the reason is empty, which I drew from "reason is required".
* The row no longer showing the badge after release, in criterion 3.

The notes leave these undecided, and I left them out of the PRD:
* Whether a brand can end a pause early.
* Whether a brand can pause the same payout again after release.
* Whether the badge text is exactly `paused` or `Paused`.

If you settle any of them, I'll add them as requirements. I can also push this to ClickUp if you approve it.