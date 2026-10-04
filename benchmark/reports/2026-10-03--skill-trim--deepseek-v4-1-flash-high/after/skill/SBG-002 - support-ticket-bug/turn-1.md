`export/001 - bug-android-confirmation-total-city-tax-clarification.md`

Verified: read-back succeeded; 15 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `Always`, `Not provided`, `FE` (literal field values and a discipline identifier the ticket, context and template fix) and "Root cause identified" (fixed checklist wording quoted from the bug template)

Quality summary: Bug Mode, Standard energy. One consolidated context question, saved alone as a question-only clarification and read back, with no draft and no answer to its own question. Fixed bug structure not yet applied, since turn 1 is intake. Completeness 9, Clarity 9, Actionability 8, Accuracy 9 (every point rests on a supplied ticket line), Relevance 9, Mechanism Depth 8.

`$bug` asks its context question before drafting, so the bug report is not written yet. The ticket already carries the observed and expected behavior, Maren's Android 8.12.1 reproduction and the iOS comparison, so the file asks only what the ticket leaves open:

- **Scope:** whether to cover Pay now stays of 2 nights or more only and leave Pay at property as an open check, and whether the queue search alone lets the report name web as not affected
- **Environment:** the test phone model and its Android version, and the guest's device, all of which will read `Not provided` if unsupplied
- **Frequency:** whether `Always` rests on the escalation's every-guest claim, since the 14 chats are a count rather than a frequency claim
- **Evidence:** the guest's screenshot, any screen recording and a Figma frame
- **Severity and title:** whether Severity matches the ticket's High priority, and whether the title takes `FE`
- **Validation:** whether Booking has a cause or a related bug, and whether to hold the report to EUR, en-GB and a per adult per night tax

Answer the points in one reply and the bug report follows as a new export. Any point you skip will read `Not provided`.