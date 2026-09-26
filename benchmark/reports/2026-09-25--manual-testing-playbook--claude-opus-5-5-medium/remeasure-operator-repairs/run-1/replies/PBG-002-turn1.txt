```markdown
I'll write the bug report for ticket 58213. The ticket already gives me the observed and expected totals, Maren's reproduction on 1, 2 and 3 nights, the iOS comparison and the 14 related chats. Please answer the points below in one reply and I'll draft straight after.

**1. Scope:** Should the report cover Pay now stays of 2 nights or more only? Pay at property is untested, so I'd list it as an open question rather than as a symptom. Per-stay city tax, other currencies and other locales are untested too. Should those stay out of the report?

**2. Expected behavior:** Should the report ask only for a Total that matches the charge (€405.00 for RS-7Q4K2M)? Or should the confirmation screen also show the City tax line, the way the payment step does?

**3. Severity and frequency:** Is Maren's High priority the severity? For frequency, the bug showed on both the guest's phone and the test phone for every stay of 2 nights or more. Can I write "Always (Pay now, 2+ nights, reproduced on two devices)", or should it read Not provided?

**4. Environment:** The ticket gives Android 8.12.1 and en-GB. Do you have the device model and Android OS version for the guest's phone or the Support test phone? If not, those fields will read Not provided.

**5. Evidence:** Can you add the guest's screenshot of the confirmation screen, or a link to it? Is there a screen recording? If not, both will read Not provided.

**6. Previous behavior:** Did Android 8.11.2 show the correct total? If nobody has checked, I won't call this a regression.

**7. Title and root cause:** Is `FE - Guest app - BOOK - Confirmation total leaves out city tax on Android` the title you want? The iOS app and the confirmation email both show the right total, but I'll leave the root cause as the checklist item and won't point at the app or at `booking-service`. Tell me if you know more.
```

Export-equivalent path: `export/001 - bug-android-confirmation-total-city-tax-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** I haven't drafted the bug report yet. `$bug` has to ask one combined question and wait for the answer first. The points above only cover what the ticket and company context leave open. Everything else comes straight from Maren's notes.

**Next step:** Once you answer, I'll write the report under the next number in the bug lane (`export/002 - bug-...`). If you skip a point, that field will read Not provided and I won't guess a value.