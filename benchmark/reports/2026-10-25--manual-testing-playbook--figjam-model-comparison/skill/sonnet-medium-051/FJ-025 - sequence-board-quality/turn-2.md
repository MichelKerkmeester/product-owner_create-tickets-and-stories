Before I draw anything, this is how I read the request.

**Question:** in what order do the guest app, the booking API, the payment provider and the partner hub exchange messages when a guest pays at checkout?
**Outcome:** the payments team can read the checkout calls in order, with the status codes, for an authorised card and for a declined one.
**Dials:** Balanced detail, Engineer audience, Laptop reading distance.

**Settled by the sources:** your summary of the payments brief gives the four parties, every call in order, the 201 on success and the 402 on a declined card.

**Outline, in drawing order**

Diagram 1, "1. Checkout payment, happy path":
* GuestApp to BookingApi: Post the booking
* BookingApi to itself: Hold the room
* BookingApi to PaymentProvider: Authorise card
* PaymentProvider to BookingApi: Authorised, as a reply
* BookingApi to itself: Confirm the hold
* BookingApi to PartnerHub: Tell the partner hub, as a fire-and-forget message
* BookingApi to GuestApp: 201, as a reply

Diagram 2, "2. Checkout payment, declined card":
* The same first three messages
* PaymentProvider to BookingApi: Declined, as a reply
* BookingApi to itself: Release the hold
* BookingApi to GuestApp: 402, as a reply

**Two framings**
* Two diagrams, one path each. The happy path and the decline each read as a straight line, and the cost is a second board to open. I recommend this one
* One diagram for the happy path, with the decline as a note naming the messages it replaces. It is shorter to open, and the cost is that the decline is a note rather than a drawn path

**The look**
* First glance: Authorise card on both diagrams, because it is the call that decides the checkout
* Second glance: Authorised on diagram 1 and Declined on diagram 2
* Last glance: Tell the partner hub, which does not hold up the answer to the app
* Subtitles: one sentence each, from the booking request to the confirmed booking and from the booking request to the 402
* Source line: the payments brief as you summarised it
* Zones: none, because a sequence takes no zone line

**Left out:** retries, timeouts and partner hub failures, because the brief states none of them.

**Assumed**
* The reader is the payments team, settled by your correction
* The message to the partner hub is fire-and-forget, because the brief lists no answer from it, settled by your correction
* The brief describes current behavior rather than a proposal, settled by your confirmation of its status
* Labels use plain verbs plus 201 and 402, because the brief gives no endpoint paths, settled by you sending the paths

**Still open:** nothing that blocks the model.

Is this the right reading of the board?