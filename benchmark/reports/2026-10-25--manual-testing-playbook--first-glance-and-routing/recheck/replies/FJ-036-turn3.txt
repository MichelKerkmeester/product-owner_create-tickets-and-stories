Round 3 is folded into this playback. Your request answers decisions and states, and the one open row is its source class. I've marked that row assumed instead of asking a third time.

**Settled**
* Reader: the Roamstay product team
* Question: what does a guest see and pay when they change their dates?
* Outcome: the reader can check that every price outcome has a screen and spot any case the app doesn't cover
* Type: user flow, Balanced detail, Mixed audience, Laptop reading distance
* Stays out: payment failures, cancellations, host approval, change fees and deadlines
* No confirm screen between picking dates and the price outcome
* After other rooms, the guest picks a room and the price check runs on it

**Assumed**
* Source class: current behavior, because your request describes the app in the present tense. A live product doc or a Figma frame for the flow would settle it. If the flow is planned, the labels would carry that status.

**The outline**
The question line: what does a guest see and pay when they change their dates?

Nodes, nine of the nine allowed:
1. Booking page, flow start [Entry]
2. Pick new dates, screen [Entry]
3. Room free on those dates?, decision [Decisions]
4. Other rooms shown, screen [Decisions]
5. How does the new price compare?, decision [Decisions]
6. Pay the difference, screen, the guest acts [Actors]
7. Difference returned as credit (automatic), system step [Actors]
8. Nothing charged (automatic), system step [Actors]
9. Updated booking shown, flow end and goal [Exit]

Connectors, eleven:
1. Booking page to Pick new dates, "Tap Change dates" [stated]
2. Pick new dates to Room free [stated]
3. Room free to Other rooms shown, "No" [stated]
4. Room free to price comparison, "Yes" [inferred, since your request states only the No exit]
5. Other rooms shown to price comparison, "Pick a room" [your round 2 answer]
6. Price comparison to Pay the difference, "Higher" [stated]
7. Price comparison to Difference returned as credit, "Lower" [stated]
8. Price comparison to Nothing charged, "Same" [stated]
9. Pay the difference to Updated booking [stated]
10. Difference returned as credit to Updated booking [stated]
11. Nothing charged to Updated booking [stated]

**Two framings**
* One board from the booking page to the updated booking, with the room detour and the three price branches beside the main line. It costs a wider board, but it shows every outcome in order. Recommended, because your question covers both availability and price.
* A price-only board that starts at the price comparison. It is tighter, but it drops the room detour, which is one of the cases you want checked.

**The look, all proposed**
* First glance: the price comparison decision, because it is the node the question turns on. The alternative is the default, which makes Updated booking the accented goal.
* Zones: two. "Find a room" holds nodes 1 to 4 and "Settle the price" holds nodes 5 to 9.
* Title: Change booking dates
* Subtitle: How a Roamstay guest moves a booking to new dates, from the booking page to the updated booking
* Source line: the request for this flow, no screenshots. Left out: payment failures, cancellations, host approval, change fees and deadlines.

**Named gaps**
* The request doesn't say what the guest sees when no other room is free
* It doesn't say what happens when the guest turns down every other room

Neither gets a node. Both go on a `Finding:` line so the team can decide them.

Is this reading right, with the source class assumed as current behavior? Reply yes, or correct any line.