# FJ-022 turn 3 transcript

**User:** Use your recommended answers.

**Assistant:**

This is the playback. Nothing is written to the board yet.

**What the board answers**
* Question: how does a Fernhouse customer start a return in the app, from the order list to a confirmed return?
* Outcome: the reader can confirm each screen between those two points and see both ways out of the 30-day check
* Settings: user flow type, Balanced detail, Mixed audience, Laptop distance

**What your sources settled**
Source: your description of the app and the returns doc. No screenshots or doc file reached me, so this is your account, classed as current behavior except the proposal.
* Entry is the order list and the exit is the confirmation with a QR code
* The screens are the order list, the order detail with a Start a return button, a list of return reasons, a drop-off point or courier pickup choice and the confirmation
* Returns are open for 30 days after delivery, and after that the app shows Contact support
* Free pickup for orders over 100 euros is a proposal under review, so it stays off the board

**Assumed, and what would settle each**
1. The reader is the Post-purchase and Storefront team. You settle it by naming another
2. The in-app flow is live, so it is drawn as current behavior. The app version that shipped it settles it, and the 2026-09-18 context note says otherwise
3. The 30-day check sits on the order detail, with Contact support as the No exit
4. The reason list comes before the method choice, because that is the order you listed them. The returns doc's order settles it
5. Both methods lead to one confirmation
6. Every screen label is my wording except Start a return and Contact support. The exact on-screen text settles it

**Outline**
`userIntent`: how a Fernhouse customer starts a return in the app, from the order list to a confirmed return.

Nodes, in drawing order:
1. Order list, the start
2. Order detail
3. Within 30 days of delivery?, a decision
4. Start a return
5. Pick a reason
6. Return method?, a decision
7. Confirmation with QR code, the goal
8. Contact support, an end

Connectors, 8 in all:
1. Order list to Order detail
2. Order detail to the 30-day decision
3. 30-day decision, Yes, to Start a return
4. 30-day decision, No, to Contact support
5. Start a return to Pick a reason
6. Pick a reason to Return method?
7. Return method?, Drop-off point, to the confirmation
8. Return method?, Courier pickup, to the confirmation

The remove test would cut Start a return first, since it could be a label on the Yes exit. It stays because it is the one exact button label you gave, and it is what Contact support replaces after 30 days.

**Two framings**
* Happy path on one row with the exits beside it. It shows both ways out of the 30-day check and both methods, at 8 nodes
* A shorter row with no 30-day decision, noting Contact support in the subtitle. It has 6 nodes but hides the exit this reader checks

I recommend the first, because the reader's outcome is to see both ways out of the window check.

**The look**
* Colour marks the 30-day decision, since its No exit ends the flow early. The confirmation is named the goal and stays unstyled
* Two zones. Check the order holds the order list, order detail, the 30-day decision and Contact support. Request the return holds Start a return, Pick a reason, Return method? and the confirmation
* Title: Start a return
* Subtitle: how a customer starts a return in the app, from the order list to the QR code confirmation
* Source line: Sources: a description of the app and the returns doc. Left out: free pickup for orders over 100 euros, a proposal under review

Is this reading right, or what should change?
