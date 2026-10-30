**Settled so far**
* Reader and outcome: support, who must pick out the end states (Completed, Cancelled, No-show) at a glance.
* Question: which statuses a Roamstay booking can be in, and what moves it between them.
* Type: state diagram. The doc gives states and the events that move them.
* States: Pending, Confirmed (Upcoming and In stay), Completed, Cancelled and No-show.
* Moves: card authorised, check-in, check-out, guest cancels from Pending or Confirmed, and hotel marks No-show after a missed check-in.
* Rules shown under each state's name: the 15-minute Pending limit, date changes while Upcoming, room charges while In stay, the 48-hour cancel rule and No-show from 6 hours after check-in time.
* Colour: the composer already draws every state the booking ends in light gray and keys it "Final state". That needs no extension. It colours by kind, so the three end states share one gray.
* Target: file `<test-file-key>` takes the board as a new section beside what it holds. Nothing there changes and no new file is created. I'll read the file once before the write gate.
* Assumed: Balanced detail, a mixed audience and Laptop reading distance. Also that a cancel leads to a state called Cancelled, since the doc names the event and not the state.

**Reading: what the board must not do**
Question: what must this board not show?
Recommended: no state or move the doc doesn't state, so no card-declined path, no expiry path and no refund amounts.
Why: support will read an invented path as policy.

**Reading: the 15-minute limit**
The doc caps Pending at 15 minutes. It doesn't say where a booking goes when the card check ends without authorisation.
Question: should the board draw that exit?
Recommended: no. Pending's body carries the 15 minutes and the board lists the exit under Left out.
Why: any state or arrow here would be one the doc doesn't give.

**Reading: cancelling after check-in**
Confirmed includes In stay, so a cancel arrow from Confirmed also reads as open from In stay. The 48-hour rule suggests cancelling happens before check-in, but the doc doesn't say so.
Question: should the board narrow the cancel to before check-in?
Recommended: no. Draw it from Confirmed as the doc words it, and report the In stay case as a Finding.
Why: the board shouldn't narrow the doc.

Take the recommended answers, or correct any of them?