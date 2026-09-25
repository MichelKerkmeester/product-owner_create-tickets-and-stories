I've updated the bug report with your answers.

Path: `export/001 - bug-android-confirmation-total-missing-city-tax.md`
Verified: read-back succeeded; 114 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `Observed Behavior`, `Expected Behavior` and `Steps to Reproduce:` are the bug template's fixed labels, and the field names in the table come from the template.

**Quality:** The report stays in the fixed bug template order. Every field is now filled with what you or the ticket gave me, or marked `Not provided`.

**What changed:**
- **Severity:** now just High.
- **Device and OS:** the guest's phone model is `Not provided`. Maren's test phone shows Android 14, with its model also `Not provided`.
- **Screenshot:** stays on ticket 58213 in the support desk tool. Screen recording is still `Not provided`.
- **Web:** your 2026-09-25 check (3 nights, Pay now, right total) is now in Observed Behavior. The report now says web, iOS 8.12.0 and the confirmation email all show the full total.
- **References:** a new "Related bugs: None open" line.
- **Cause:** listed under "Not known yet", since nobody on Booking has looked at the code.

The report still assumes the title's discipline is `FE` (front end), and it still has the repro step to cancel the test booking and the 1-night BDD scenario. Pay at property and Android 8.11.2 are the two open questions left besides the cause.