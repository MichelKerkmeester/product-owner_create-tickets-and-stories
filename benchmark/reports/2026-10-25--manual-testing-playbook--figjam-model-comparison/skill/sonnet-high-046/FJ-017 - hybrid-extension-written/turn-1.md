Before I draw anything, this is how I read the request. A state diagram fits, because you're asking which statuses a booking passes through and what moves it between them.

**Question:** which statuses does a Roamstay booking pass through, what moves it on, and who sets Cancelled and No-show?
**Outcome:** support can read the lifecycle and knows whether to ask the guest or the hotel about a Cancelled or No-show booking.

**Settled by your message** (the only source, read as current behavior):
* Pending until the card is authorised, then Confirmed
* Confirmed covers Upcoming and In stay
* Check-out ends the booking as Completed
* A guest can cancel while Pending or Confirmed
* The hotel marks No-show after a missed check-in
* A note on Cancelled and a note on No-show each say who sets it

**Assumed**, each open to correction:
* Upcoming moves to In stay on check-in, because your message names no event for that move. A bookings doc or your word settles it
* Every status is current behavior, because no bookings doc came with the request. A doc to check against settles it
* Balanced detail, a mixed audience and the Laptop reading distance

**Outline**, in drawing order:
1. Intent: which statuses a Roamstay booking passes through, what moves it on and who sets Cancelled and No-show
2. Start, then Pending
3. Pending to Confirmed: card authorised
4. Inside the Confirmed section, Upcoming to In stay: check in
5. Confirmed to Completed: check out [from In stay]
6. Pending to Cancelled and Confirmed to Cancelled: guest cancels
7. Confirmed to No-show: missed check-in [from Upcoming]
8. Completed, Cancelled and No-show each end the booking

That is 7 states and 6 moves between them, and the remove test cuts nothing because each one comes from your message.

**Two framings**
* **One machine with Confirmed as a section** around Upcoming and In stay. It shows every exit in one view, and the guards say which inner state each exit leaves. Recommended, because it keeps your own grouping
* **A flat chain with the exits beside it.** Its labels are simpler, but it loses the grouping and the guards that tell support where a booking can still be cancelled or marked No-show

**Look**
* States carry your words: "In stay" and "No-show"
* Title "Booking status", with a subtitle saying who reads the board and why
* Cancelled is marked with the pink outline, as a recommendation, since the board exists to answer who sets it
* The source line names your message as the only source
* Two single notes, one beside each state. Cancelled reads "Set by the guest, while Pending or Confirmed" and No-show reads "Set by the hotel after a missed check-in". They are an extension, so the write gate will name them

**What the board must not do:** your message gives no refund rule, no payment state, no other way to cancel and no timing for the no-show. I recommend the board implies none of them and adds no state beyond the seven, because support would act on whatever it implies.

**Left out:** a note on Completed, who else can cancel, the timing of No-show and who triggers check-in, because your message doesn't state them.

Nothing is written until you answer here and then approve the write. Is this the right reading, including that the board implies nothing beyond the seven statuses and six moves?