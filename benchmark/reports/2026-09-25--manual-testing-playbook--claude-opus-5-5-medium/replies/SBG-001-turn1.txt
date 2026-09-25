I've written the bug report and saved it to export.

Path: `export/001 - bug-ios-cart-badge-stale-after-remove.md`
Verified: read-back succeeded; 75 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `**1. Observed Behavior**` and `**2. Expected Behavior**` are the fixed Bug Mode labels, which are allowed to break sentence case.

**Quality summary:** All six quality checks pass. Accuracy is strongest because every specific claim comes from what you told me or from the Fernhouse context file. Completeness is the weakest because the device models, iOS version and a screen recording are missing, so those fields say "Not provided".

**Summary:** The report is a Medium bug on iOS 4.8.0: removing an item leaves the tab bar badge on the old count until the app restarts, while Android 4.8.2 and web update straight away. The reproduction steps use your 2 + 1 cart, and the step where the bug shows says "Expected: 2" and "Actual: 3". Frequency is "Always" because it happened every time on both test phones.

**Things I added that you didn't give me (remove any that are wrong):**
- The title follows the Fernhouse naming format, `FE - iOS - CART - …`. I chose the front-end code (FE) because only iOS is affected, but that's a guess, not a known root cause. If it turns out to be a backend (cart-service) problem, the code changes.
- The expected result comes from the context file, which says the badge counts units, not lines. So removing the 1-unit line should show "2".
- One user expectation says the iOS badge updates correctly when an item is added. That comes from your badge reading "3" after adding.
- I added a short Given/When/Then scenario for QA to test against.

Next step: if you send the phone models, iOS versions or a screen recording, I'll add them to the report.