I haven't written the bug report yet. `$bug` requires me to ask one round of questions and wait for your answers before drafting, so I saved those questions to a file instead.

Path: `export/001 - bug-android-confirmation-total-city-tax-clarification.md`
Verified: read-back succeeded; 14 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

The ticket already covers what's broken, what should happen, the steps to reproduce and the iOS comparison, so the file only asks about what's missing:

- **Pay at property:** nobody has tested it. Should the report cover Pay now only and list Pay at property as an open check, or wait until someone tests it?
- **Web:** can the report say web isn't affected when the only basis is that no web chats turned up in the queue search?
- **Test phone:** Maren's tests don't name the phone model or its Android OS version.
- **Evidence:** I need the guest's screenshot, any screen recording and any Figma link for the confirmation screen.
- **Severity and title:** should Severity match the ticket's High priority? Should the title start with `FE`, or should the squad choose once they know the cause, since the confirmation email shows the right total?
- **Known cause or related bug:** has the Booking squad already found or ruled out a cause, or linked a related bug?

Once you answer, the report will be saved as `export/002 - bug-...md`. Any point you skip will say `Not provided`, and it won't name a root cause unless you give me one.