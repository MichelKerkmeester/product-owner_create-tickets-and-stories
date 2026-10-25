Before I draw anything, this is how I read the request.

**Question:** which screens does a Fernhouse customer pass through to start a return in the app, and where do they choose?

**Outcome:** a reader can follow a return from the order list to a confirmed return with a QR code, and see where the 30 day window ends it.

**Type:** a user flow, because the question is the screens one customer passes through and where they choose. A list would name the screens without showing the two branches.

**Outline, in drawing order:**
- Order list, the entry, then the order detail
- Order detail, which holds Start a return, then the 30 day check
- Within 30 days?, No to Contact support and Yes to the return reasons
- Contact support, the exit once the window has closed
- Return reasons, the list the customer picks from, then the method choice
- Drop-off or courier pickup?, Drop-off to the drop-off point and Courier pickup to the courier pickup
- Choose a drop-off point, then the confirmation
- Choose a courier pickup, then the confirmation
- Return confirmed with QR code, the goal

**Two framings:**
- A happy path with the 30 day exit beside it. I recommend this one, because it reads in one pass and keeps Contact support visible without competing with the goal
- A state map of every return status, which would show the warehouse check and the refund. Neither source gives those steps

**The look:** the title Start a return, a one sentence subtitle, and a source line naming the app and the returns doc. Three zones, Find the order, Request the return and Done. First glance is the confirmed return with its QR code, the goal the flow reaches. Second glance is the drop-off or courier pickup choice that leads to it. Last glance is Contact support, the exit after 30 days.

**Settled by the app and the returns doc you supplied:** the order list, the order detail with its Start a return button, the list of return reasons, the choice between a drop-off point and a courier pickup, and the confirmation with a QR code. The returns doc also sets the 30 day window after delivery and the Contact support screen after it.

**Actors:** the customer, with the app checking the 30 day window.

**Left out:** the free pickup for orders over €100, a proposal under review in the returns doc.

**Assumed:** balanced detail, a mixed audience and laptop reading distance, with labels in the app's own words.

**One clash:** the Fernhouse company context says there is no self-serve return today, and that a CS agent creates the return in Admin. Your two sources describe the app's own Start a return flow. I take the app and the returns doc as governing for this board, because they are the sources you named and they carry the screens you want drawn.

Is this the right reading of the board, with the app and the returns doc governing?