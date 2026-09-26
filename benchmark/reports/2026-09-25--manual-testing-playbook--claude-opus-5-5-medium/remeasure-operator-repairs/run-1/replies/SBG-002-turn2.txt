I've written the bug report for the Booking squad.

Path: `export/002 - bug-android-confirmation-total-city-tax.md`
Verified: read-back succeeded; 92 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `**1. Observed Behavior**` and `**2. Expected Behavior**` keep their capital letters because they are the fixed labels in the bug template.

**Quality check:** every section of the bug template is filled in. Each amount matches Maren's Back office breakdown and her test results. The report does not name a cause, because nobody on Booking has looked at the code yet.

The report pairs the expected and actual total in the key step (€270.00 vs €258.00) and backs it with the booking RS-7Q4K2M evidence. It also covers the cases that work (1-night stays, iOS, and your web check on 2026-09-26) and the 14 support chats.

**Choices I made that you didn't give me — change any you disagree with:**
- **Title starts with `FE`:** you didn't answer that question. `FE` is the code for Guest app screens. If the cause turns out to be outside the screen, change it to `FS` or `BE`.
- **Pay at property:** you didn't answer this either. The report lists it as untested with no guest reports, and doesn't include it in the bug.
- **Frequency is "Always":** this rests on Maren saying every Pay now guest on Android with 2+ nights is affected, plus the failure showing up on two phones (the guest's and the test phone).
- **Device is "Not provided":** we don't have the model for either phone. The OS field shows Android 14 for the test phone only.
- **Missing links:** there's no Figma link, so Flows and Components say "Not provided". The guest's screenshot is referenced by its ticket number instead of being included.
- **Added by me:** step 7 (cancel the test booking) is my addition, based on Maren cancelling hers. I also added the one BDD scenario.

I can push this to ClickUp if you'd like. I'll only do that once you say yes.