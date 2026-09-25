I've written the bug report from Maren's ticket and saved it.

Path: `export/001 - bug-android-confirmation-total-missing-city-tax.md`
Verified: read-back succeeded; 110 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `Observed Behavior`, `Expected Behavior` and `Steps to Reproduce:` are the bug template's fixed labels, and the field names in the table come from the template.

**Quality:** All six quality checks pass (the fact-accuracy check against the ticket scores 9). It's one bug in the fixed template order, with a BDD section added.

**Summary:** On Android 8.12.1, the confirmation screen shows the room price as the total after a Pay now stay of 2 nights or more. City tax is left out, so the guest sees less than their card was charged. The report includes the booking RS-7Q4K2M figures (€387.00 shown, €405.00 charged), Maren's 2-night test (€258.00 shown, €270.00 charged) and the 1-night and iOS tests where the total was right. It also has the 14 Android chats and step-by-step reproduction with expected and actual results. Three things the ticket doesn't cover are listed as "Not known yet": Pay at property bookings, the web app, and whether Android 8.11.2 was correct.

Choices I made that you can change:
- **Title discipline:** I used `FE` because the screen is where the total is wrong. The cause hasn't been found, so change it to `BE` or `FS` if the Booking squad finds it in a service.
- **Frequency set to `Always`:** Maren's escalation says every Android Pay now guest with 2 nights or more is affected, and both her test phone and the guest's phone showed it.
- **Severity set to High:** this uses the ticket's High priority.
- **Two additions you didn't ask for:** a final repro step to cancel the test booking (Maren did this after her tests) and a BDD scenario checking that 1-night totals stay correct.

Device and Android OS version aren't in the ticket, so they're marked `Not provided`. Let me know if you want Pay at property added as its own repro once someone has tested it.