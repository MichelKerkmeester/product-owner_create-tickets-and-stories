Before I draw anything, this is how I read the request.

**Question:** in what order do the guest app, the booking API, the payment provider and the partner hub exchange messages for a Roamstay checkout payment?

**Outcome:** the payments team can trace the checkout calls in order, with their status codes, for an authorised card and for a declined one.

**Framing:** two boards, one per path, because `alt` fragments render flat. The alternative is one board for the authorised card with the decline left out. I recommend the pair, because the request describes both paths.

**Outline — board 1, authorised card (4 participants, 7 messages):**
1. GuestApp → BookingApi: POST /bookings
2. BookingApi → BookingApi: Hold the room
3. BookingApi → PaymentProvider: Authorise card
4. PaymentProvider ⇢ BookingApi: Authorised
5. BookingApi → BookingApi: Confirm the hold
6. BookingApi ⤳ PartnerHub: BookingCreated (fire-and-forget)
7. BookingApi ⇢ GuestApp: 201 Booking confirmed

**Outline — board 2, declined card (3 participants, 6 messages):**
1. GuestApp → BookingApi: POST /bookings
2. BookingApi → BookingApi: Hold the room
3. BookingApi → PaymentProvider: Authorise card
4. PaymentProvider ⇢ BookingApi: Declined
5. BookingApi → BookingApi: Release the hold
6. BookingApi ⇢ GuestApp: 402 Payment declined

**Settled by the sources:** the payments brief in the request gives both paths in order, the hold, the provider exchange, the partner hub notify and the 201 and 402 replies.

**Already on the file:** this exact pair exists, "1. Checkout payment, authorised card" and "2. Checkout payment, declined card" (sections 73:562, 74:954), plus two more versions of the same checkout ("1. Checkout payment, happy path" / "2. Checkout payment, declined card" at 91:2621, 92:2769 and "Checkout payment, card authorised" / "Checkout payment, happy path" at 121:4040, 122:4181). Recommended: draw the pair fresh, then remove the earlier exact-titled pair on a separate yes after the write, so the plan keeps one copy. The other two versions stay untouched.

**Assumed:** the reader is the payments team on the Roamstay Product plan, an engineer audience so paths and status codes stay in the labels, Balanced detail and Laptop reading distance.

**First glance:** message 3, Authorise card, on board 1 and message 4, Declined, on board 2, each marked as the focus.

**Left out:** nothing. Both paths in the brief are drawn.

Is this the right reading of the board?