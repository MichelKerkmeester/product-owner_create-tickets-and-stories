Round 2 is settled on the recommended answers. One correction to my last message: the playback carries the outline, not the checked model. The model, its check result and the sketch come with the write gate, after your answer here.

Question: which screens does a guest pass through to change their booking dates, and where does the flow branch?
Outcome: the product team agrees the branches (room not free, price higher, lower or the same) before design and build.

Settled by your description:
* Entry is the booking page, exit is the updated booking
* Two decisions, the room check with 2 exits and the price comparison with 3

Assumed, and each one stands unless you correct it:
* Reader, question, outcome and the Left out list from round 1
* Guest actors: Change dates, the date pick, the room choice and the payment
* System actors: the room check, the price comparison, the credit and the no-charge case. These are drawn as automatic
* After other rooms, the guest picks one and the flow rejoins at the price comparison
* Source class: current behavior. A link to the screens or the spec would settle it
* Detail level Balanced, audience Mixed, reading distance Laptop

Outline, in drawing order (9 nodes, 11 connectors, 5 labelled decision exits):

1. Booking page (start)
2. Booking page to Pick new dates, labelled "Tap Change dates"
3. Pick new dates (screen)
4. Pick new dates to the room check
5. Room free on new dates? (decision, system)
6. Yes goes to the price comparison
7. No goes to Choose another room
8. Choose another room (screen, the guest picks one)
9. Choose another room to the price comparison
10. How does the new price compare? (decision, system)
11. Higher goes to Pay the difference (guest)
12. Lower goes to Get the difference as credit (system)
13. Same goes to Nothing charged (system)
14. All three outcomes go to Updated booking (end, the goal)

Two framings:
* One board with a straight spine, recommended. The room check leads straight to the price comparison and Choose another room hangs off as a detour. The common path reads in a line and the detour stays visible, but the detour's return edge adds one crossing risk that the composer has to route
* Two boards, "1. Pick dates and room" and "2. Settle the price". Each board is smaller, but the price branch loses its lead-in and the reader has to hold the room check in mind across two boards. Your request says one new board and the path fits the budget, so I don't recommend the split

The look, as five proposed choices:

1. Colour: the one accent goes on the price decision, because that three-way split is what the outcome is about. No end is a failure, and Updated booking is the goal
2. Zones: two, "Find a room" (Booking page, Pick new dates, Room free on new dates?, Choose another room) and "Settle the price" (the price comparison, the three outcomes and Updated booking). They mark where each decision sits. Without zones the board still passes the check
3. Title: Change booking dates
4. Subtitle: How a Roamstay guest changes the dates of a booking in the app, from the booking page to the updated booking
5. Source line: Source: the team's description of the flow. Left out: card entry and payment failures, cancellation, change fees and deadlines, the case with no other room free, where the credit goes afterwards

The sketch will be tested against four questions:

* Does the eye land first on the price decision, and is that the node the board most needs read?
* Does Choose another room read as a detour rather than a second main route?
* Do the three price exits read as equals?
* Does each outcome rejoin at Updated booking without a crossing?

Is this reading right? Say yes, or correct any row.