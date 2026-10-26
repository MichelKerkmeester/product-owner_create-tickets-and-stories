Before I draw anything, this is how I read the request.

**Question:** in what order do the guest app, the booking API, the payment provider and the partner hub exchange messages when a guest pays at checkout?

**Outcome:** the Roamstay product and engineering team can follow the checkout calls in order for an authorised card and for a declined card, and see where the room hold is released.

**Settled by the sources:** your summary of the payments brief gives the calls in order for both outcomes. I could not find the brief itself in the workspace, so your summary is the only text I am drawing from.

**Assumed:**
* The readers are the Roamstay product and engineering team, which is my reading of "our Roamstay Product plan".
* Detail is balanced, the audience is engineers and the board is read on a laptop.

**Framing:** a sequence board can't branch, so I recommend two diagrams, written in this order and read left to right:
1. *Checkout payment, card authorised.* Post the booking, Hold the room, Authorise card, Authorised, Confirm the hold, Tell the partner hub, 201 Created. That is 4 participants and 7 messages.
2. *Checkout payment, card declined.* Post the booking, Hold the room, Authorise card, Declined, Release the hold, 402 Card declined. That is 4 participants and 6 messages.

The alternative is the authorised path only, with the decline named as left out. It is cheaper, but it drops half of what the brief gives you.

**Look:** the first glance is Authorise card on board 1 and 402 Card declined on board 2. Messages use plain requests and replies, with no async arrow, because the brief doesn't say the hub's message is fire-and-forget. I also left out the endpoint path, because the brief doesn't name one.

**Not drawn:** anything the brief doesn't state, such as webhooks, retries or a pending wait.

**Inferred:** the provider's two replies, Authorised and Declined. The brief implies them, since the hold is confirmed or released afterwards, but doesn't state them. I'd keep both.

**Still open:** the brief clashes with the Roamstay company context, which was last reviewed on 2026-09-18.
* **The context says:** only `payments-service` talks to the payment provider, and a Pay now booking waits in `payment_pending` until the provider confirms by webhook.
* **Your brief says:** the booking API asks the provider to authorise the card and answers 201 straight after.

Both can't describe the same flow as written. My reading is that the brief may cover a path with no webhook wait, such as Pay at property, where the context says the booking confirms at once.

*Recommended:* draw the brief as you gave it, treat it as current behaviour and report the clash on a `Finding:` line. You named the brief as the source, and rewriting its calls to match the context would put my guess on the board. If the brief describes a proposed design, I'd say so in the board's labels instead.

Is this the right reading of the board, with the brief governing where it differs from the company context?