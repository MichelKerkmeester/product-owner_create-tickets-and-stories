I've read the Flow Mode files and your message. No write has happened. I haven't seen the app screenshots or the returns doc, only your description of them, so everything below rests on that description. Here is what I've settled so far:

- **Type:** user flow, because the question is which screens a customer passes through and where they choose
- **Question:** how a Fernhouse customer starts a return in the app
- **Entry and exits:** the flow starts at the order list. It ends at the confirmation with a QR code, or at Contact support once the 30 days have passed
- **Screens, in your order:** order list, order detail with Start a return, the list of return reasons, the drop-off or courier pickup choice, then the confirmation
- **Decisions:** whether the order is within 30 days of delivery, and drop-off point versus courier pickup
- **Left out:** the free pickup for orders over €100. It's a proposal under review, so it stays off the board and is named on the source line and in the reply
- **Target:** the existing file `<draft-file-key>`, with the board added as a new section beside whatever is already there. You named two destinations, a new board in the Fernhouse Product plan and that file. I read the file as the target. A section added to a file sits in the file's own plan, so no plan choice is needed. The Barter team plan, in drafts with no project, applies only if I end up needing a new file, which I don't expect. I'll read the file once before the write gate and flag any section there that shares the board's title.
- **Proposed shape:** 7 nodes. Drop-off point and Courier pickup are the two labelled exits of one decision, and both reach the one confirmation. Your sources describe no separate screen for each choice, so I won't invent "Choose a drop-off point" or "Book a courier pickup" screens.
- **Assumed:** the 30 day check sits on the order detail. Within the window, Start a return leads to the reasons. After it, the app shows Contact support. Your message doesn't say whether Contact support replaces the button or appears after a tap. The returns doc or a screenshot of an expired order would settle it.
- **Look, proposed:** left to right, balanced detail, mixed audience, read on a laptop, with the confirmation as the goal and Contact support as the exit below the main line

I have three questions, one per block:

**1. Reader and outcome**
- Reading: your request names no reader.
- Question: who reads this board, and what should they be able to do afterwards?
- Recommended: a Fernhouse product or support colleague who follows a return from the order list to the confirmation and sees where the 30 day window ends it.
- Why: that sets the labels to the app's own words and keeps the board to the path.

**2. What the board must not do**
- Reading: the only hard line in your message is the free pickup proposal.
- Question: what else must the board not do?
- Recommended: it must not show the free pickup as live, must not add screens beyond the five you listed, and must not cover what support does with a return after the customer submits it.
- Why: a board that refuses nothing is where invented steps creep in.

**3. Is the self-serve return live in the app?**
- Reading: the Fernhouse context note, last updated 2026-09-18, says there is no self-serve return and customers contact CS. You describe a Start a return button in the app. The note predates today, 2026-10-26, and names 4.9.0 as the next release, so the flow may have shipped after it.
- Question: is the flow live, and which source governs?
- Recommended: the app and the returns doc govern. I'd draw it as current behavior and put the discrepancy on a `Finding:` line.
- Why: the app and the doc are your sources and the note is the older of the two.

Answer any of these, or say "use the recommended answers". Any answer you skip proceeds on its recommendation and is marked assumed. I'll then play the full reading back for your confirmation before drawing anything. Is the reading above right, and which answers do you want to give?