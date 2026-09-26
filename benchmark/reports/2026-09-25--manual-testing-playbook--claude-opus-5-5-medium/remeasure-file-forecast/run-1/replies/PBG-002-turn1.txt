```markdown
I'll write the bug report for Guest Support ticket 58213. The ticket already gives the charge, the expected total, Maren's reproductions and the workaround. I only need the points below, in one reply:

**Scope:**
- Should the report cover only Pay now stays of 2 nights or more on Android 8.12.1, with Pay at property marked as Not provided? Or will Booking check Pay at property first so the report can include it?
- Maren confirmed iOS 8.12.0 shows the right total. Nobody has written in from web, but nobody tested web either. Should I record web as not tested, or has someone checked it?

**Expected behavior:**
- Should the fix only make the confirmation total match the charge, city tax included (€405.00 for RS-7Q4K2M)? Or should the confirmation screen also show a City tax line like the payment step? The product context says the confirmation screen shows the reference, dates, guests and total. That means a new line would be a change to the screen and not part of this fix

**Environment and field table:**
- What model and Android version is the Guest Support test phone? Do we know the guest's device? If not, I'll write Not provided
- The ticket priority is High. Should the severity also be High, or does Booking want to set it?
- The bug has one reproduction on one test phone, plus 14 guest chats. Unless someone has reproduced it on a second device, I'll set Frequency to Not provided and put the counts in Observed Behavior. Has anyone reproduced it on another device?

**Evidence:**
- Can you share the guest's screenshot or any screenshots or recordings from Maren's tests? If not, I'll write Not provided
- Did Android 8.11.2 show the right total, or is that unknown?
- Is there a Figma frame for the confirmation screen?

**Title and links:**
- My proposed title is `FE - Guest app - BOOK - Confirmation total leaves out city tax on Android`. Is FE the right discipline?
- Is there a ClickUp link for ticket 58213 or a related bug?

**Validation:**
- Maren only tested city tax per adult per night, in EUR, with the app set to en-GB. Should I limit the report to those conditions and leave out per-stay city tax, other currencies and other locales rather than claim they're affected?
```

Export-equivalent path: `export/001 - bug-android-confirmation-total-missing-city-tax-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** I checked this question against the intake criteria. It asks for everything missing in one go, repeats nothing the ticket or product context already answers and doesn't guess at the cause.

**Summary:** You asked for a bug report with `$bug`, and the process is to ask one question first and wait for your answer. Maren's notes already cover most of the report. They give what the guest saw and what was charged, repro steps for 1, 2 and 3 nights, the iOS comparison, 14 chats since 2026-09-16 and the fact that the confirmation email shows the right total.

The open points are:
- whether Pay at property and web are in scope
- whether the fix only corrects the total or also adds a City tax line
- device details and severity
- whether any screenshots or recordings exist
- the title and the ClickUp link

Once you answer, I'll write the bug report.