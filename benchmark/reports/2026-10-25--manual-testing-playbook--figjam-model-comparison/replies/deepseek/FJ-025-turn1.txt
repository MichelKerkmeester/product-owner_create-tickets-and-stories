Before I draw anything, this is how I read the request.

Question: in what order do the guest app, the booking API, the payment provider and the partner hub exchange messages at checkout?
Outcome: the payments team can follow the calls in order, with the status code, for a card that is authorised.

Outline, in drawing order
GuestApp to BookingApi: Post the booking
BookingApi to itself: Hold the room
BookingApi to PaymentProvider: Authorise the card
PaymentProvider to BookingApi: Authorised
BookingApi to itself: Confirm the hold
BookingApi to PartnerHub: Booking created
BookingApi to GuestApp: 201 Created

Framing: the authorised path as its own diagram, with the declined path as a second diagram if you want it. One diagram holding both paths renders flat here, so a reader cannot tell which messages a decline skips.
Look: title "Checkout payment, card authorised", four participants and seven messages, balanced detail, an engineer audience so status codes stay in the labels, laptop reading distance, first glance on the authorisation call.
Settled by the sources: the payments brief gives the six moves in order, from the guest app posting the booking to the 201 answer. It also gives the declined card as a released hold and a 402 answer.
Left out: the declined-card path, the hold release and the 402 answer, kept for a second diagram.
Assumed: the payment provider's reply between the authorisation request and the hold confirmation, since the brief gives the request and the confirmation but not the answer that joins them.
Assumed: the message to the partner hub reads "Booking created", because the brief says the API tells the hub without naming what it sends.
Still open: none.

Is this the right reading of the board?