Here is the playback. Nothing is written yet, and the next reply after your answer is the write gate.

### Rows as they stand

- Reader: Roamstay product and design team, assumed from your accepted answer
- Question: how does a guest change the dates of a booking in the app (captured)
- Outcome: they can check that every availability and price case is covered before it is built, assumed
- Scope: the date change only. Cancelling, a failed card payment and host approval stay off the board and go under Left out, assumed
- Entry: the booking page, where the guest taps Change dates (captured)
- Exit: the updated booking is shown (captured)
- Actors: the guest, and the app for the availability and price checks (captured)
- Decisions: whether the room is free, then whether the new price is higher, lower or the same (captured)
- After the other rooms: the guest picks a room and the flow rejoins at the price check, assumed
- Sources and class: your message, taken as current behavior, assumed
- Trigger into the availability check: the app checks as soon as the dates are picked. Your message gives the order but no trigger, so this is assumed

### Outline

The board's intent: a Roamstay product reviewer can see what a guest gets for every availability and price case when they change the dates of a booking.

Nodes, in drawing order:

1. Booking page, where the flow starts (Entry)
2. Pick new dates (Scope)
3. Room free?, a choice (Decisions)
4. See other rooms (Decisions, assumed)
5. New price?, a choice with three exits (Decisions)
6. Pay the difference (Decisions)
7. Difference added as credit (Decisions)
8. Nothing charged (Decisions)
9. Updated booking shown, the goal (Exit)

Connectors:

1. Booking page to Pick new dates, "Taps Change dates"
2. Pick new dates to Room free?, "Dates picked", automatic, assumed
3. Room free? to New price?, "Yes"
4. Room free? to See other rooms, "No"
5. See other rooms to New price?, "Picks a room", assumed
6. New price? to Pay the difference, "Higher"
7. New price? to Difference added as credit, "Lower"
8. New price? to Nothing charged, "Same"
9. Pay the difference to Updated booking shown
10. Difference added as credit to Updated booking shown
11. Nothing charged to Updated booking shown

That is 9 nodes, 11 connectors and 5 labelled exits, which sits at the user-flow budget of 9 nodes.

The remove test cut nothing. Nothing charged could fold into the "Same" connector and save a node. I kept it so the three price outcomes read as a set.

### Two framings

- A, recommended: one path with the branches beside it, as outlined above. Booking page to the updated booking runs on one straight line, and the other-rooms detour and the three price outcomes sit beside it. It costs nothing in coverage, and a reviewer sees the order a guest meets each case in.
- B: an outcome map. One choice after the date pick lists the four places a guest can end up: pay, credit, nothing charged or other rooms. It reads faster. It costs the rejoin through other rooms, which is the case a review is most likely to miss.

### The look, proposed

- Glances. First: the New price? choice, because it is the only three-way choice and holds the rule the request spends most words on. Second: the three outcomes under it. Last: the other-rooms detour and the source line. The goal stays green and is not marked, so the board has one accent.
- Detail and audience: Balanced and Mixed, with plain verbs and the product's own words. Reading distance: Laptop. All three are assumed.
- Zones: two. "Find a room" holds the booking page, Pick new dates, Room free? and See other rooms. "Settle the price" holds New price?, the three outcomes and the updated booking.
- Text: the title is "Change booking dates". The subtitle is "How a Roamstay guest changes the dates of a booking in the app, from the booking page to the updated booking". The source line is "Sources: the product brief in the request, taken as current behavior. Left out: cancelling, a failed card payment, host approval".
- Four questions the sketch has to answer:
  - Does the eye land on New price? first, and is that the node the board most needs read?
  - Does every price outcome end on the updated booking?
  - Does the other-rooms rejoin read as a detour and not a second main route?
  - Is anything on the board a step you would not miss?

Is this reading right, with framing A and the look as proposed? Say yes, or correct a row, a node or the look, and name B if you prefer it.