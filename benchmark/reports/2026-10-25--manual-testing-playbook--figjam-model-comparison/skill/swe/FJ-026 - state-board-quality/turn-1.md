The model passes the pre-write check and composes cleanly. Here is the playback before anything is drawn.

Playback, how I read the request:

Question: which statuses exist and what moves a Roamstay booking between them?
Outcome: a Guest Support agent reads any booking's status and spots at a glance whether it has ended, and on which event.

Settled by the request:
* States: Pending, Confirmed covering Upcoming and In stay, and three ends, Completed, Cancelled and No-show
* Moves: card authorised, check-in, check-out, guest cancels from Pending or Confirmed, and missed check-in
* Colour: a state model carries no styling, so the composer's roles do the colouring the request asks for. Every status the machine ends from draws in light gray and the key names it Final state, which makes Completed, Cancelled and No-show the one filled group on the board

Outline, one line per node and edge:
1. start to Pending
2. Pending to Confirmed on card authorised
3. Confirmed holds Upcoming to In stay on check-in, entered on Upcoming
4. Confirmed to Completed on check-out
5. Pending to Cancelled and Confirmed to Cancelled on guest cancels
6. Confirmed to No-show on missed check-in
7. Completed, Cancelled and No-show each to end

Two framings:
* A state map with Confirmed as one composite holding Upcoming and In stay. Recommended, because it keeps the "covers" relation the request states and shows every exit, which is what support needs
* A flat flow from Pending to the three ends. Simpler, but it loses the "covers" relation and draws the two cancel paths as unrelated lines

The look:
* First glance: the gray end states as a group. No single node is marked, because the board exists to make that group stand out
* Detail Balanced, audience Mixed, distance Laptop, assumed. Zones: none beyond Confirmed, which is its own zone
* Title "Booking status", subtitle "Every status a Roamstay booking passes through, and what moves it on, for Guest Support"

Assumed: the three dial settings above, and Confirmed entering on Upcoming, since check-in is the only stated way into In stay.

Two things to name before the gate:
* The Roamstay context file also records a booking in payment_pending expiring after 30 minutes. The lifecycle you stated does not include it and names no status it ends in, so I recommend leaving it out and saying so on the source line. An earlier board in this file made the same call
* This file already holds two boards titled "Booking status", earlier draws of the same lifecycle. The new board lands to the right of everything on the page, and after the write I will ask whether to remove the earlier two. The left-hand one carries two sticky notes that would go with it

Is this the right reading of the board?