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
