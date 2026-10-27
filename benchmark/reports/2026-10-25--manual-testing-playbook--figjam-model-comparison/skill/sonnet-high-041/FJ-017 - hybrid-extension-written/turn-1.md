Before I draw anything, this is how I read the request.

**Question:** which statuses can a Roamstay booking have, what moves it between them, and who sets the two statuses support asks about?
**Outcome:** support can follow a booking from Pending to its end and knows who to ask about a Cancelled or a No-show booking.
**Type:** a state diagram. The reader's question is about statuses and what moves a booking between them, so the word "plan" in your request refers to the Figma plan and not to a schedule.

**Settled by your description** (taken as current behavior):
* Pending until the card is authorised, then Confirmed
* Confirmed covers Upcoming and In stay
* Check-out ends the booking as Completed
* A guest can cancel while Pending or Confirmed
* The hotel marks No-show after a missed check-in

**Notes:** two single stickies added after the board is drawn, one beside Cancelled saying the guest sets it and one beside No-show saying the hotel sets it. They are a second write, so the next message names them.

**Assumed**, each corrected by a word from you:
* Check-in is what moves Upcoming to In stay, because you name a missed check-in but not the move itself
* Check-out leaves from In stay, because it only happens during a stay
* Only the guest sets Cancelled. If the hotel or the payment system can also cancel a booking, the sticky would send support to the wrong person, so tell me and I will change the note
* Completed, Cancelled and No-show are final, and nothing leaves them
* Balanced detail, a mixed audience and the Laptop reading distance, which fits support reading the board on a screen

**Left out:** what happens to a Pending booking whose card is never authorised, because you gave no exit for it.

**Still open:** you wrote that a guest can cancel while Confirmed, and Confirmed covers In stay.
* Reading: a guest can cancel during Upcoming and during In stay
* Recommended: draw it as written, as one move from Confirmed
* Why: the other reading adds a limit you did not state

Is this the right reading of the board?