Question: which statuses does a Roamstay booking pass through, and what moves it from one to the next? That is a state diagram.
Outcome: support can read every status, see what moves a booking on and spot the statuses a booking ends in.
Reader: support, from "so support can spot them". Detail balanced, audience mixed, reading distance Laptop, all assumed.
Destination: a new board section in the existing FigJam file <draft-file-key>. No new file is created and nothing already on the file changes.

Settled by your message: Pending until the card is authorised, Confirmed covering Upcoming and In stay, check-in from Upcoming to In stay, check-out to Completed, a guest cancel from Pending or Confirmed and a hotel-marked No-show after a missed check-in. No doc was attached, so I read each line as current behavior on your word.

Outline, in drawing order:
* States (7): Pending, Confirmed holding Upcoming and In stay, Completed, Cancelled, No-show
* Labelled moves (6): card authorised, check in, check out [from In stay], guest cancels from Pending, guest cancels from Confirmed, missed check-in [from Upcoming]
* Unlabelled moves (6): entry at Pending, entry at Upcoming, and exit from In stay, Completed, Cancelled and No-show
* Remove test: nothing to cut, because you named every state and move

Two framings:
* One machine with Confirmed as a section around Upcoming and In stay: 7 states and 12 moves. It keeps check-in, and the two moves that leave the section as a whole carry a guard naming their starting state.
* A coarse machine with Confirmed as one state: 5 states and 9 moves. It drops Upcoming, In stay and the check-in move you asked for.
* Recommended: the first, because you named check-in.

Look: the composer draws every state the machine ends from in light gray with a heavy outline, keyed as Final state. Pending, the first state, is light blue and the other states are white. A different colour for the end states is a design-file edit that changes every board, and a one-off colour on a single state is a hand edit in FigJam. The title is "Booking status", with the subtitle "Every status a Roamstay booking passes through and what moves it on", and the source line names your request.

Still open (a point you skip stands on its recommendation, marked assumed):
1. Cancelling during In stay. Confirmed includes In stay, so your wording lets a guest cancel mid-stay, drawn as one "guest cancels" move from Confirmed as a whole. Is that intended? Recommended: draw it as stated, because no narrower rule was given. If cancelling is Upcoming only, the label becomes "guest cancels [from Upcoming]".
2. End states. You called Completed an end, and nothing you wrote moves a booking out of Cancelled or No-show. Are those two end states as well, in the same gray? Recommended: yes, because no reinstatement move is stated.
3. Pink accent. Which end state, if any, takes the pink outline that reads first? Recommended: Cancelled, the only end state two statuses lead into. The alternative is no accent, which leaves the three end states equal and puts Pending first.

Assumed: check-out leaves from In stay and a missed check-in from Upcoming, which is why those two labels carry a guard. No timing is drawn for No-show, because you gave none.
Left out: a card that is never authorised while the booking is Pending, because no status or move is stated for it.

Is this the right reading of the board?