Here is how I read the request, built on your accepted recommendations. No model is drawn and nothing is written.

**Question:** in what order do the guest app, the booking API, the payment provider and the partner hub exchange messages when a guest pays at checkout?

**Outcome:** Booking and Payments engineers can read the checkout calls in order, with status codes, for an authorised card and for a declined card.

**Settled by your answers**
* Reader: Booking and Payments engineers
* Scope: two boards, one per path, and neither shows webhooks, `payment_pending` or retries
* Source governing: your payments brief

**Settled by the sources** (the brief as you worded it)
* Entry: GuestApp posts the booking
* Exit: 201 to the app when the card is authorised, 402 when it is declined
* Parties: GuestApp, BookingApi, PaymentProvider and PartnerHub
* Decision: the card is authorised or declined. The decline does not involve PartnerHub

**Board 1, happy path** (4 parties, 7 messages)
1. GuestApp posts the booking to BookingApi
2. BookingApi holds the room
3. BookingApi asks PaymentProvider to authorise the card
4. PaymentProvider answers "Authorised"
5. BookingApi confirms the hold
6. BookingApi tells PartnerHub
7. BookingApi answers GuestApp with 201

**Board 2, declined card** (3 parties, 6 messages)
1. GuestApp posts the booking to BookingApi
2. BookingApi holds the room
3. BookingApi asks PaymentProvider to authorise the card
4. PaymentProvider answers "Declined"
5. BookingApi releases the hold
6. BookingApi answers GuestApp with 402

**Left out:** the `payment_pending` hold and webhook confirmation from `context/roamstay-context.md`. That file has the provider confirming by webhook after the booking waits. Your brief has the booking API answering 201 in the same run. The brief governs, so the webhook step stays off both boards.

**Assumed**
* Source class: the brief is current behavior, which I can't confirm because it isn't in the workspace. If it is a proposal, the subtitle will say so
* Hub message: drawn as fire-and-forget, because the brief names no reply and the 201 doesn't wait for one
* Detail level: balanced, with engineer wording and a laptop reading distance

**Inferred, medium confidence:** the provider's "Authorised" and "Declined" replies. Your wording only says it authorises and that a card can be declined.

**Still open:** your wording gives no request path or hub message name, so labels use your verbs, such as "Post the booking" and "Tell the partner hub". If the brief has the real path or event name, give it to me and I'll use that.

Is this the right reading of the board?