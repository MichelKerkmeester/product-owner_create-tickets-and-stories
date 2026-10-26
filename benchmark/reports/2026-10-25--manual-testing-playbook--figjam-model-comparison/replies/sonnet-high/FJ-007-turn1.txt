Before I draw anything, this is how I read the request. Nothing is written yet.

**Type:** state diagram, because the question is which statuses a booking can be in and what moves it between them.

**Question:** which statuses exist, and who sets Cancelled and No-show?
**Outcome:** support can see how a booking reaches Cancelled or No-show and who sets each, so they know who to ask.

**Settled by your request:**
* A booking is Pending until the card is authorised, then Confirmed.
* Confirmed covers Upcoming and In stay.
* Check-out ends a booking as Completed.
* A guest can cancel while it is Pending or Confirmed.
* The hotel marks No-show after a missed check-in.

Your message is the only source, so I'm treating it as current behavior until you point me to a doc.

**Notes (two, as single stickies beside their states):**
* Cancelled: "Set by the guest, while a booking is Pending or Confirmed"
* No-show: "Set by the hotel, after a missed check-in"

**Assumed:** your request names check-in and check-out but not which state each leaves from. I'd draw it this way:
* Check in moves Upcoming to In stay.
* Check-out leaves from In stay.
* Missed check-in leaves from Upcoming.

**Reading to check:** the guest-cancel arrow leaves the whole Confirmed section, so the board shows a guest can cancel during In stay too. If cancel should stop at check-in, tell me and I'll label it "from Upcoming".

**Not on the board:** who moves a booking into Pending, Confirmed or Completed, any hotel-initiated cancellation, refunds and time limits. Your request names none of them, so I recommend leaving them off and listing them as left out in the reply.

**Look:** balanced detail, a mixed audience and laptop reading distance. The composer draws Completed, Cancelled and No-show in light gray as final states. I'd set no accent on a single node, because Cancelled and No-show matter equally to support. The title would be "Booking status lifecycle".

The file and the plan details come with the write question, after this.

Is this the right reading of the board?