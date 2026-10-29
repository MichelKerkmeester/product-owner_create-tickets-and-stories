# FJ-032 turn 2 transcript

**User:** Use your recommended answers.

**Assistant:**

This is round 2 of 3. Still nothing written to the board.

**Settled so far**
* Reader (assumed): the Roamstay product and engineering team
* Question (assumed): which booking statuses exist and what moves a booking between them
* Outcome (assumed): the team agrees the status values and allowed moves before a story is written
* Must not do (corrected by your answer): draw nothing you didn't state, so no authorisation failure, refund or booking change
* Dials (assumed): Balanced detail, Mixed audience, Laptop distance
* Source: your message only

**1. Entry**
Reading: you didn't say how a booking starts, only that it is Pending until the card is authorised.
Question: does every booking enter at Pending when it is created?
Recommended: yes, a start dot into Pending.
Why: Pending is the first state you named.

**2. Exit**
Reading: Completed follows check-out. Cancelled and No-show are where your cancel and no-show moves land.
Question: are Completed, Cancelled and No-show all final, with no reopening?
Recommended: yes, all three end the booking.
Why: you described no move out of any of them.

**3. Triggers for the moves you didn't name**
Reading: you named the triggers card authorised, guest cancels, check-out and missed check-in. Nothing says what moves Upcoming to In stay.
Question: what moves a booking from Upcoming to In stay?
Recommended: `check-in`, with Check-out and the no-show move both leaving only from the inner state they belong to (`check-out [from In stay]`, `missed check-in [from Upcoming]`).
Why: In stay can only follow a check-in, and an inner-state guard keeps those two moves from reading as open from every state inside Confirmed.

Take the recommended answers, or correct any of them?
