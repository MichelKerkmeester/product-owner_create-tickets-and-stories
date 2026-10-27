# FJ-036 turn 3 transcript

**User:** Use your recommended answers.

**Assistant:**

Here is the full reading for you to check before I draw anything.

The question and the outcome
- Question: which screens does a guest pass through to change their booking dates, and where does the path branch on room availability and price? This sentence is the intent the board is drawn to answer
- Outcome: the product and design team can confirm that the room check and all three price outcomes end on the updated booking

What your description settled (class: current behavior, assumed)
- Entry: the booking page
- Exit: the updated booking
- Actors: the guest, and the app for the room check and the price comparison
- Decisions: room free on the new dates, then the new price against the old (higher, lower or same)

What I assumed, and what would settle each
- Reader, question and outcome as above. Your yes settles them
- Scope is only the path you described. Your yes settles it
- The guest picks a room after seeing other rooms, then rejoins at the price comparison. A screenshot of the other-rooms screen or the product doc would settle it
- The source class is current behavior. A screenshot or doc would settle it

No row is unasked.

The outline, in drawing order. Nine nodes and eleven connectors, so no split is needed.
- Booking page, starts the flow (Entry)
- Tap Change dates, leads to Pick new dates (Entry, Actors)
- Pick new dates leads to Room free? (Decisions)
- Room free? exits: Yes goes to the price check, No goes to See other rooms (Decisions)
- See other rooms leads to Pick a room (assumed) (Decisions)
- Pick a room (assumed) leads to the price check (Decisions)
- New price? exits: Higher goes to Pay the difference, Lower goes to Get the difference as credit, Same: no charge goes straight to the updated booking (Decisions)
- Pay the difference and Get the difference as credit each lead to Updated booking, which ends the flow (Exit)

The remove test cut nothing. The next candidate is merging See other rooms with Pick a room, and I'd keep them apart so the assumed step shows as its own node.

Two framings
- Full decision map, recommended. Both decisions are drawn and the pay and credit outcomes each get a node. This is the one that shows the reader every branch you listed
- Collapsed path. The price outcomes become labels on the connectors into Updated booking, which gives 7 nodes. It reads faster but hides the pay and credit steps as screens

The look, five proposed choices
1. Accent: the price decision, because it is the branch the board most needs read. Updated booking is named as the goal and left unstyled
2. Detail, audience and distance: Balanced, Mixed and Laptop, because the readers are a product team looking at a laptop screen
3. Zones: none. Nine nodes on one main line read without grouping
4. Text: title "Change booking dates", subtitle "How a Roamstay guest changes the dates of a booking in the app, from the booking page to the updated booking", and a source line "Source: the product description in the request. Left out: failed payments, backing out and cancelling"
5. Critique: the next message will answer the four critique questions about the sketch

What the board will leave out
- Failed payments, backing out and cancelling, by your scope answer
- What the guest sees when no other room is free, because your description does not say

Is this reading right, or which row should I change?
