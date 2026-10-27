Before I draw anything, this is how I read the request.

**Question:** which statuses can a Roamstay booking have, what moves it between them, and who sets Cancelled and No-show?
**Outcome:** support can read every booking status and know whether to ask the guest or the hotel about a Cancelled or No-show booking.

**Settled by your message.** You supplied no bookings doc, so I class all of it as current behavior on your word:
* Pending until the card is authorised, then Confirmed
* Confirmed covers Upcoming and In stay
* Check-out ends the booking as Completed
* A guest can cancel while Pending or Confirmed
* The hotel marks No-show after a missed check-in

**Outline, in drawing order.** The first line is the sentence the board answers.
* Which statuses can a booking have, what moves it between them, and who sets Cancelled and No-show?
* Start, then Pending
* Pending to Confirmed on card authorised
* Inside Confirmed: Upcoming to In stay on check in
* Confirmed to Completed on check out, taken from In stay
* Pending to Cancelled and Confirmed to Cancelled, both on guest cancels
* Confirmed to No-show on missed check-in, taken from Upcoming
* Completed, Cancelled and No-show each end the booking
* 7 states and 12 transitions, inside the 9 and 12 budget
* Two notes: one on Cancelled, one on No-show

**Two framings:**
* A state map of the full lifecycle, with the three end states and the two notes. It shows every exit and keeps Upcoming and In stay inside Confirmed. This is my recommendation, because your question is about statuses and who sets two of them
* A process with Guest and Hotel lanes. It shows who acts on every move, but it loses the nesting of Upcoming and In stay inside Confirmed, and you didn't say who moves the other statuses

**The look, all proposed:**
* Pending is the first glance. The composer draws it light blue, and the three end states in light gray. I'd put the focus mark on Cancelled, since you named it first
* Balanced detail, a mixed audience (support) and a Laptop reading distance
* One section only, the one around Confirmed
* Title "Booking status". Subtitle "Every status a Roamstay booking passes through, and who sets Cancelled and No-show". Source line "Source: your request. Left out: ..." with what is listed below
* The notes are two single stickies beside their states, one reading "Set by the guest, while the booking is Pending or Confirmed" and one "Set by the hotel after a missed check-in"

**Assumed.** Each of these stands unless you correct it:
* Upcoming moves to In stay on "check in". You named both states but not the trigger, so this is the one trigger I supplied. What would settle it is the bookings doc or your word
* Check-out is only possible from In stay, so that move carries the guard `[from In stay]`
* Only the guest sets Cancelled and only the hotel sets No-show, because those are the only actors you named
* The board must not show payment, refund or screen detail. This is my answer to what the board must not do

**Left out:**
* What happens to a Pending booking whose card is never authorised, because you didn't say
* Any other way a booking becomes Cancelled, such as the hotel or the system cancelling it, for the same reason

**Still open:** none.

Is this the right reading of the board?