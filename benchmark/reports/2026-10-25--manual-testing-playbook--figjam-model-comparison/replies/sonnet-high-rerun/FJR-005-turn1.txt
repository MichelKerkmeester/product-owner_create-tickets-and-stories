I'm still on intake and have written nothing to FigJam. I read the Roamstay notes in `context/` for booking statuses, and they cover only part of a lifecycle. Before I model anything, here is my reading.

**Playback**

Reading
*   The type is a state diagram, because the question is which statuses exist and what moves a booking between them
*   The sources state `payment_pending`, confirmed, expired and cancelled, from `roamstay-context.md` (Checkout and payment, Cancellation) and `roamstay-payment-webhook-incident-notes.md`
*   A Pay now booking waits in `payment_pending` until the payment provider's webhook arrives, then moves to confirmed
*   A booking still in `payment_pending` after 30 minutes expires
*   A Pay at property booking confirms at once
*   A guest cancels under Trips before the free cancellation deadline. After it, they contact Guest Support
*   Nothing in the notes names a status for check-in, a stay in progress, completion or a no-show
*   `sk-create-figjam/assets/examples/state-roamstay-booking.md` does draw those, but it says every state in it is invented, so I did not use it as a source

Questions

1. **Reader and outcome.** Is the board for the Booking squad and Guest Support, so they can agree the status list before a story is written?
   *   Recommended: yes
   *   Why: the notes name `booking-service` as the owner of booking states, and Guest Support is the team that reads them

2. **Which booking, and which statuses.** Is "booking" the Roamstay booking in `context/`? Is there a doc with the full status list?
   *   Recommended: draw only the four sourced statuses and name the rest as gaps under `Left out:`
   *   Why: a partial lifecycle of real statuses beats a full one I invented
   *   Gaps I would name:
       *   check-in and stay
       *   completed
       *   no-show
       *   whether a `payment_pending` booking can be cancelled
       *   what moves a booking out of confirmed other than cancelling

3. **What the board must not do.** Should it stay on booking status and leave out refunds, payouts and the expiry-job pause from INC-0412?
   *   Recommended: yes
   *   Why: those are payment states, and mixing them in would make a second machine on the same board

Unanswered questions go ahead on the recommendations, marked assumed. The target is the existing file `<draft-file-key>`, so the board lands as a new section beside what it holds and no plan or new file is needed. The write gate comes after this playback has its answer.

Is this the right reading of the board?