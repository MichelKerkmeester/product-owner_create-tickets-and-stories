Before I draw anything, this is how I read the request. I haven't opened the screenshots or the returns doc. Everything below comes from your description of them.

**Question:** which screens does a customer pass through to start a return in the app, and where do they choose?

**Outcome:** a reader can follow a return from the order list to a confirmed return and see where the 30 day window ends it.

**Type:** a user flow, because the question is about screens and choices.

**Settled by your description**
* Five screens: the order list, the order detail with a Start a return button, the list of return reasons, the drop-off point or courier pickup choice, and the confirmation with a QR code. All are current behavior
* Returns are open for 30 days after delivery. After that the app shows Contact support. Current behavior
* A free pickup for orders over 100 euros is a proposal under review

**Left out:** the free pickup over 100 euros. It stays off the flow and is named on the board's source line as a proposal.

**Outline, 7 nodes and 7 connectors, in drawing order**
1. Order list, where the flow starts
2. Order detail, reached by tapping an order
3. Within 30 days? A decision with two exits
4. No exit: Contact support, an exit beside the main line
5. Yes exit: Pick a reason
6. Drop-off or pickup? A decision with two exits
7. Both exits lead to Return confirmed, the goal

**Framings.** I recommend the happy path with the 30 day exit beside it. The alternative is a state map of every exit, but the sources give one exit, so a map adds nothing.

**Look**
* The goal is Return confirmed, so it is the first glance. Order list and the drop-off or pickup choice come second. Contact support comes last
* Three zones: Find the order, Request the return and Done
* Balanced detail, a mixed audience and the Laptop reading distance, with the app's own words on every label

**Where I need your call**
* **Is this flow live in the app?** The Fernhouse company context (last updated 2026-09-18) says there is no self-serve return today and that CS creates returns in Admin. Your description says the app has this flow. I recommend your description governs, because it comes from the app itself and the context note may predate the release. The board will then draw it as current behavior. If the flow is still in design or beta, it is approved direction or a proposal, and the labels would carry that status
* **What must the board not do?** I recommend that it never shows the free pickup as part of the flow, and never adds a drop-off point screen or a pickup booking screen you didn't describe. Your five screens end in the confirmation, so both method exits go straight to it

**Assumed**
* The reader is the product team reviewing the returns flow. A different reader would change the audience setting. Tell me who it is if not
* The 30 day check sits after Order detail, because the Start a return button is on that screen. The Yes exit leads to the reasons list. What would settle it: the screen the app shows to an order older than 30 days

Is this the right reading of the board, including those recommended answers?