Path: `export/002 - bug-android-confirmation-total.md`

Verified: read-back succeeded; 78 lines

HVR self-scan: 0 hard blockers. Fixed: replaced a semicolon in the Frequency cell with a comma. Kept with reason: `**1. Observed Behavior**` and `**2. Expected Behavior**` (the two fixed corpus labels Bug Mode grants verbatim), `Not provided` / `n/a` (the template's own placeholder values), and the literal identifiers `RS-7Q4K2M`, `40217`, `8.12.1`, `8.12.0`, `price-mismatch`, `FE`, `BOOK`.

Quality summary
- Accuracy: every amount, version and count traces to ticket 58213 or your reply, and the arithmetic is shown per line (€258.00 + €12.00 = €270.00, €387.00 + €18.00 = €405.00)
- Completeness: field table, observed behavior, numbered steps, screen recording line, expected behavior, the four-item checklist and one BDD scenario
- Scope: one defect on the Android confirmation screen, Pay now only, with iOS, web and the 1-night case carried as boundary evidence
- Size: 599 words against the 800-word bug budget. `context/roamstay-support-ticket-58213.md` and `context/roamstay-context.md` unchanged, and `001` holds the untouched clarification

Additions you did not supply, so you can strike any of them: Frequency reads `Always (every Pay now Android booking of 2 nights or more, per reporter, 14 chats in 5 days)`, grounded in Maren's every-time claim with the count kept beside it rather than inside it. The reproduction steps follow Maren's test sequence, since that is the only run with a paired expected and actual figure. The title uses `FE` for a screen-only change, which is my reading of the evidence that iOS, web and the confirmation email are all right. The Pay at property line stays as a boundary note rather than a second defect.

Severity High, Android 14 on the test phone, the guest's model marked `Not provided`, the screenshot recorded as held in the support desk tool, and no open related bug are all in the report as you described them. Say the word if you want the ClickUp task created from it.