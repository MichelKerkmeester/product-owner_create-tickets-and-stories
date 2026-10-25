I've read the Flow Mode rules and the state-diagram reference. Nothing is drawn or written yet. The reading comes first, as the rules require.

Before I draw anything, this is how I read the request.

Question: which statuses can a Roamstay booking have, and who sets Cancelled and No-show?
Outcome: support can follow a booking from Pending to its end and knows who to ask about a Cancelled or a No-show booking.
Type: a state diagram, because the question is about statuses and what moves a booking between them.

Settled by your message:
* Pending until the card is authorised, then Confirmed
* Confirmed covers Upcoming and In stay, drawn as one Confirmed section holding both
* Check-out ends the booking as Completed
* A guest can cancel while Pending or Confirmed
* The hotel marks No-show after a missed check-in
* Two notes: Cancelled is set by the guest, and No-show is set by the hotel

Target: a new board section in the existing file `<test-file-key>`, with no new file. You also named the Roamstay Product plan. An existing file keeps the plan it was made in, and I can't confirm from here which plan owns it, so I treat the file key as the target and the plan name as context.

Assumed, and each can be corrected:
* **Notes:** two notes get one sticky each beside their state, with no numbered pins or legend. The model can't carry a note, so each note is added after the board is drawn, and I'll name them in the write gate.
* **Moves:** No-show is reached from Confirmed, and the move is labelled "missed check-in". The "who sets it" detail lives in the note.
* **Detail:** balanced detail, a mixed audience and a laptop reading distance.

Left out: the 30-minute expiry of a booking stuck in `payment_pending`. It appears in the Roamstay context doc, but you didn't mention it and nothing in your message says what status it ends in.

Still open: the Roamstay context doc says that after the free cancellation deadline, or on a non-refundable rate, the guest contacts Guest Support to cancel. Your note says the guest sets Cancelled. Recommended: the note says "Set by the guest" and adds nothing about Support, because no source says who sets it in the Support case. If Support does it, tell me and I'll word the note that way.

Is this the right reading of the board?