I've loaded the Flow Mode packet and the Fernhouse context file, and I'm at the reading step. Nothing has been written to your FigJam file.

**Reading of the board**

Question: which screens does a Fernhouse customer pass through to start a return in the app, and where do they give up?
Outcome: a reader can follow a return from the order list to the QR confirmation, see where the 30 day window ends it and see the three places support says customers drop out.
Type: user flow, because the question is about screens and choices.
Target: a new board section inside the existing file `<test-file-key>`, in the Fernhouse Product plan as you named it. I read "new board" as a new section in that file, not a new file.

**Settled by what you gave me**

- Screens in order: order list, order detail with Start a return, reason list, drop-off or courier pickup choice, confirmation with a QR code
- The 30 day window after delivery, then the app shows Contact support (current behavior, per the returns doc)
- Three support notes, each pinned to the node it names:
  - Reason list: too many reasons
  - Drop-off or pickup choice: pickup fee unclear
  - 30 day cut-off: no warning before day 30

**Left out:** the free pickup for orders over 100 euros. It is a proposal under review, so it stays off the board.

**Assumed**

- Reader: the product team reviewing where returns lose customers. Your answer settles it
- Contact support is the exit of a "Within 30 days?" check right after the order detail. You did not say which screen shows it, and the returns doc or a screenshot would settle it
- The drop-off or pickup choice is one decision with two exits that both lead to the confirmation. You named no screens between them, so I add none
- Labels come from your wording, because no screenshot or returns doc reached this session. The source line on the board will say so
- The three notes read as "Support reports", because they are support's account and not measured drop-off figures
- Balanced detail, mixed audience, laptop reading distance

**Conflict to settle:** the Fernhouse company context, last updated 2026-09-18, says "There is no self-serve return today". Under it, the customer contacts CS and an agent creates the return in Admin. You describe an in-app flow as current behavior. Recommended: your description governs. It comes from the app and the returns doc, and the context file is five weeks old and names 4.9.0 as the next app release. If the flow is not live yet, I would label it as unreleased on the board.

Is this the right reading of the board, with the in-app flow treated as live today?