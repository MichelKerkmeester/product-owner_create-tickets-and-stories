Round one of three, and nothing is written yet. This is what your message already settles:

* Reader: support, who need to know who to ask about a Cancelled or No-show booking
* Question: which statuses a booking passes through, and who sets Cancelled and No-show
* Outcome: support can name who to ask for each of those two statuses
* Type: state diagram, because the question is about statuses and what moves a booking between them
* Start and ends: Pending is the start, and Completed, Cancelled and No-show are treated as final
* States: Pending, Confirmed (holding Upcoming and In stay), Completed, Cancelled and No-show
* Moves: card authorised, guest cancels from Pending or Confirmed, check-out to Completed, and the hotel marks No-show after a missed check-in
* Notes: one on Cancelled and one on No-show, each naming who sets it
* Target: a new FigJam file in drafts on the <figma-plan-5> team plan, no project, with `whoami` confirming the plan before the write gate
* Source: your message, taken as current behavior and assumed until a bookings doc says otherwise

Three things are still open:

**1. Detail, audience and reading distance**
Reading: a board for support, read at a desk.
Question: do these three settings fit?
Recommended: Balanced detail, Mixed audience, Laptop distance.
Why: support needs every status and the two setters, not exact event names or a wall-sized view.

**2. Cancelling once the guest is In stay**
Reading: you said a guest can cancel while Confirmed, and Confirmed covers Upcoming and In stay. I read check-in as the move from Upcoming to In stay, check-out as leaving In stay, and No-show as leaving Upcoming.
Question: can a guest still cancel after check-in?
Recommended: draw it as you said, from Confirmed as a whole, with the In stay case marked assumed.
Why: the board then claims nothing you did not say. If In stay cannot be cancelled, tell me and I'll limit that move to Upcoming.

**3. What the board must not do**
Reading: none of your five moves covers a failed card authorisation, a Pending booking that expires, a hotel or system cancellation or a refund.
Question: should the board stay to the moves you stated and name those gaps?
Recommended: yes, draw only the stated moves and list the four gaps under `Left out:`.
Why: a missing arrow could otherwise be read as "this cannot happen".

Do you want the recommended answers for all three, or do you want to correct any?