Before I draw anything, this is how I read the request. Nothing has been written to the file.

**Reader:** support
**Question:** which statuses does a booking pass through, what moves it between them, and who sets Cancelled and No-show?
**Outcome:** support can see where a booking ended up and who to ask about a cancellation or a no-show.
**Type:** a state diagram, because the question is about statuses and what moves a booking between them.

**Settled by your request.** There is no doc, so I took all of this as current behavior:
* Pending until the card is authorised, then Confirmed
* Confirmed covers Upcoming and In stay
* Check-out ends the booking as Completed
* A guest can cancel while Pending or Confirmed
* The hotel marks No-show after a missed check-in
* Two short notes: Cancelled is set by the guest, and No-show is set by the hotel

**Assumed:**
* The move from Upcoming to In stay is labelled "check in". You named both statuses but not what moves a booking between them
* Balanced detail, a mixed audience and a laptop reading distance

**Left out:**
* Any window for the No-show mark, because the request gives none
* Cancellation by the hotel or by Roamstay, because the request names only the guest
* Payment and refund steps, because the board answers a status question and not a money question

Is this the right reading, including the "check in" label and the three omissions? If you don't answer, I'll go ahead on these assumptions and show you the write step before anything touches the file.