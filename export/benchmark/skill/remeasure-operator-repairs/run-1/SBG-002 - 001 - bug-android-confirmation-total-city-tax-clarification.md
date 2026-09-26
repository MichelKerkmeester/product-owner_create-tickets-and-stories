# Android confirmation total leaves out city tax, clarification

Ticket 58213 gives me the observed and expected behavior, the reproduction on Android 8.12.1 and the iOS 8.12.0 comparison. Before I write the bug report for the Booking squad, please answer the points below in one reply. For any point you skip, I'll write `Not provided` rather than fill it in.

**Scope:** Pay at property is untested and nobody has reported it. Should the report cover Pay now only and list Pay at property as an open check, or should it wait for someone to test Pay at property? Web has no reports either. Is it fine to name web as not affected based only on the queue search?

**Environment:** Maren's reproduction names Android 8.12.1 but not the test phone model or its Android OS version. Can you supply them? If not, both fields will say `Not provided`.

**Evidence:** Can you attach or link the guest's screenshot from the ticket? Did anyone record a screen video of the 2-night reproduction? Is there a Figma link for the confirmation screen and its total?

**Severity and title:** Maren set the ticket priority to High. Should the bug's Severity also be High? The title will follow `{Discipline} - Guest app - BOOK - {Title}`. Should the discipline be `FE`, or should the squad pick it once the root cause is known, given that the confirmation email shows the right total?

**Validation:** Has the Booking squad already found or ruled out a cause, or linked a related bug? Unless you say otherwise, the report will state no root cause and will leave "Root cause identified" open on the checklist.
