Before I model anything, I need to know which checkout this is. Your request names no source, and `context/` holds two products with a checkout payment: Roamstay and Fernhouse. I haven't called Figma yet.

**Reading so far**
- A sequence diagram fits the question "in what order do these parties exchange messages?".
- The board goes into the existing file `<draft-file-key>` as a new section beside what it holds. Nothing already there changes, and no new file is needed.
- Roamstay's `context/roamstay-context.md` describes the Pay now path across `booking-service`, `payments-service` and the payment provider. The provider confirms by webhook, and the booking waits in `payment_pending` until then, with a 30-minute expiry.
- Fernhouse's `context/fernhouse-context.md` only names `checkout-service` as owning the payment session and order creation. It gives no message order, so I would have to ask for or invent the calls.

**Question 1: which checkout payment should the board draw?**
- Recommended: Roamstay, the Pay now path, as `context/roamstay-context.md` describes it. The guest app starts the payment, `booking-service` creates the booking, `payments-service` charges through the provider, and the webhook confirms the booking.
- Why: it is the only source here that states the parties and the order of a payment, so every message traces to a line.

**Question 2: who reads it, and what should they decide?**
- Recommended: engineers and the PM on the Booking and Payments squads. The board should show where the booking waits on the webhook, so they can judge the `payment_pending` window.
- Why: the webhook wait is the part of the Roamstay flow most likely to be misread.

**Question 3: should the board show only the successful Pay now path?**
- Recommended: yes. The success path is one diagram of 5 participants and at most 12 messages, and a declined payment or an expired booking becomes a second diagram.
- Why: the sequence type draws one path per diagram, because `alt` blocks would render flat.

If you don't answer a question, I'll proceed on its recommendation and mark it assumed in the next playback. Nothing is written to the board until you say yes to a separate write question.