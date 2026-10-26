Here is how I read the request now. Your recommended answers are in, and I've read the Roamstay sources: `roamstay-context.md` and `roamstay-payment-webhook-incident-notes.md`. Nothing is drawn or written yet.

**Question:** in what order do the guest app, `booking-service`, `payments-service` and the payment provider exchange messages when a guest pays with Pay now?

**Outcome:** engineers and the PM on the Booking and Payments squads can see where the booking waits on the webhook, and can judge the 30-minute `payment_pending` window.

**What the sources settled**
- **Parties.** Four participants: GuestApp, BookingService, PaymentsService and PaymentProvider. Only `payments-service` talks to the provider, and the provider reports back by webhook (`roamstay-context.md`).
- **Entry.** The guest picks Pay now at checkout.
- **Exit.** The booking leaves `payment_pending` as confirmed, and the guest sees the confirmation screen.
- **The webhook.** It arrives as `payment.captured` at `POST /v2/psp/webhooks`, and `payments-service` answers 200 when it accepts it. The incident notes and their log lines state this.
- **The wait.** The booking sits in `payment_pending` and expires after 30 minutes.

**Outline, nine messages in order**
1. GuestApp to BookingService: Create booking, Pay now
2. BookingService to itself: Hold in payment_pending (30 min)
3. BookingService to PaymentsService: Request the charge
4. PaymentsService to PaymentProvider: Charge the full total
5. PaymentProvider to PaymentsService, asynchronous: POST /v2/psp/webhooks payment.captured
6. PaymentsService to PaymentProvider, reply: 200 OK
7. PaymentsService to BookingService: Payment confirmed
8. BookingService to itself: Confirm the booking
9. BookingService to GuestApp, reply: Booking confirmed

**Assumed, with how each gets settled**
- **Messages 3 and 7.** The sources say `payments-service` owns the charge and `booking-service` owns the booking state. They don't say how the two talk to each other. I drew direct calls with plain verbs and no endpoint. The Payments squad's API brief would settle it.
- **Message 9.** The sources say the guest sees a confirmation screen, but not how the app learns the result. I drew a reply from `booking-service`. If the app polls or gets a push, the Booking squad can confirm and I'd relabel it.

**Left out**
- Pay at property, which has no payment wait.
- The declined or expired path, kept for a second diagram if you want one.
- The confirmation email and the `booking_confirmed` analytics event, because neither changes the payment order.
- INC-0412, the 401 failure on 2026-09-09, which is a failure path.
- The provider's retries.
- The proposed dual-secret window, which is a proposal and not current behavior.

**Framing:** I recommend the success path alone, with the webhook wait visible as messages 2 to 7. The alternative is a state map of `payment_pending`, which would hide the call order you asked about.

Is this the right reading of the board?