I've read the Flow Mode rules, the sequence type and the worked Roamstay example. Nothing is written to the board yet, because the reading comes first and the write gate follows it.

**Question:** in what order do the guest app, the booking API, the payment provider and the partner hub exchange messages when a guest pays at checkout?

**Outcome (assumed):** an engineer can read the checkout calls in order, with paths and status codes, for an authorised card and for a declined one.

**Settled by your message:**
* The guest app posts the booking
* The booking API holds the room
* The booking API asks the payment provider to authorise the card
* The booking API confirms the hold, tells the partner hub and answers the app with 201
* A declined card releases the hold and returns 402

**Source gap:** the payments brief isn't in the repository, so your message is my only source for the call order.

**Assumed, each corrected by saying so:**
* The hold, the confirm and the release are drawn as the booking API messaging itself, because no room store is named
* The provider's answer to the authorise request is drawn as "Authorised" and "Declined", because your message implies it but doesn't name it
* The partner hub message is drawn as fire-and-forget, with no reply, labelled "Notify partner hub" rather than an invented event name
* The happy path and the decline path are two diagrams in the same file, because a sequence can't draw a branch. That makes 4 participants and 7 messages on the first and 4 participants and 6 messages on the second
* Reading distance is Laptop and the audience is engineers

**One clash in the sources:** `context/roamstay-context.md` says only `payments-service` talks to the payment provider. It also says the provider reports results by webhook and the booking waits in `payment_pending`. Your description has the booking API calling the provider directly, with a 201 returned in the same flow. I can't tell from the sources which one governs the checkout payment.

I recommend your description governs, with the booking API drawn as the caller. The board's source line would then name the difference with the context file, so a reader doesn't take the diagram as the webhook flow.

Is this the right reading, and does your description govern over the context file?