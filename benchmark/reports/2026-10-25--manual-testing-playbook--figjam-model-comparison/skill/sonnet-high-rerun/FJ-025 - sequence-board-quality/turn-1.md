Nothing is written yet. This is how I read the request, and I need your answer before I build the model.

**Question:** in what order do the guest app, the booking API, the payment provider and the partner hub exchange messages when a guest pays at checkout?
**Type:** sequence, which matches that question.
**Outcome:** the reader can follow the checkout calls in order, from the booking post to the 201.
**Source:** your message quoting the payments brief. I found no copy of the brief in the repository, so your wording is the source, and I've marked it current behavior as assumed.
**Target:** the existing file `<draft-file-key>`, as a new section beside what it holds, with nothing already on it changed. No new file is needed, so the Barter team plan (in drafts, no project) applies only if that file can't be written to. The key doesn't tell me which plan owns the file. If it isn't in Roamstay Product, say so before the gate.

**What the board would draw** (4 participants, 7 messages, authorised card):
1. GuestApp to BookingApi: Post the booking
2. BookingApi to itself: Hold the room
3. BookingApi to PaymentProvider: Authorise the card
4. PaymentProvider to BookingApi: Card authorised
5. BookingApi to itself: Confirm the hold
6. BookingApi to PartnerHub: Tell the hub (open arrow, no reply)
7. BookingApi to GuestApp: 201 Created

**Left out:** the declined-card path (release the hold, return 402)

**Assumed, and stands unless you correct it**
* The reader is the Roamstay product and payments team, with balanced detail, engineer-level labels and a laptop reading distance
* The brief gives no path or event name, so labels use its words rather than a path like `POST /bookings`. Give me the path if you want it on the board
* Message 4 exists because the brief has the hold confirmed only after the card is authorised, so the provider must answer first
* Message 6 is fire-and-forget because the brief has the API answer the app straight after telling the hub. Tell me if the app waits on the hub

**Three questions, each with my recommended answer**
1. **One board or two?** A sequence draws one path per diagram, because a branch renders flat. You asked for one board, so I recommend one board with the authorised path and the decline named under Left out. The alternative is a second board in the same file, "Checkout payment, declined card", with Authorise the card, Card declined, Release the hold and 402 to the app. It costs one more write and adds on a yes.
2. **What must the board not show?** I recommend no retries, timeouts or webhooks, so it holds only the calls in the brief.
3. **Which participants?** The company context says only `payments-service` talks to the payment provider, while the brief has the booking API asking it. I recommend drawing the brief's version, since it is the supplied source. The alternative puts the payments service between them, which makes 5 participants and 8 messages.

Is this the right reading of the board, with those recommended answers standing?