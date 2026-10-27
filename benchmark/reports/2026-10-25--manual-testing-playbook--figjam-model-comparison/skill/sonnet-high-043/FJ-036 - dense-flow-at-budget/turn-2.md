Nothing is drawn or written yet. This is the full reading for you to correct before I model it.

### What the board answers
- Question: how does a Roamstay guest change the dates on a booking in the app?
- Outcome: the product and design team can see where the guest chooses and decide whether the three price outcomes and the other-rooms detour need separate screens
- The sentence the board answers: "Show where a guest changes booking dates and where the flow branches on room availability and price"

### Settled from your message
- Entry: the booking page, where the guest taps Change dates
- Exit: the updated booking
- Choices: whether the room is free on the new dates, and whether the new price is higher, lower or the same
- Type: user flow, with Balanced detail, Mixed audience and laptop reading distance
- Destination: a new section in file <draft-file-key>, with nothing already on the file changed

### Assumed, because your message doesn't state it
- Reader: the product and design team in a review. A named reader would replace this
- Source class: current behavior. If the flow is a proposal, the node labels carry that status
- Left out: payment failures, cancellations, card refunds and host-side steps
- Where "room is free" leads: straight to the price check
- Other rooms: the guest picks one, and the price check then runs on that room

The last two are inferred edges. Nothing in your message states either.

### Outline, in drawing order
1. Booking page (start)
2. Pick new dates, reached by the edge "Tap Change dates"
3. Room free on those dates? Yes goes to 5, No goes to 4
4. See other rooms, which goes to 5 on the edge "Pick a room"
5. New price? Higher goes to 6, Lower goes to 7, Same goes to 8
6. Pay the difference
7. Get the difference as credit
8. Nothing charged
9. Updated booking (goal), reached from 6, 7 and 8

That is nine nodes and eleven connectors, inside the nine-node budget. I left out the merge dot by sending the three outcomes straight to the updated booking, since the dot would make ten. The remove test cut a separate "Pick a room" node, which the edge label now carries.

### Two framings
- Path with the branches beside it: the main route runs on one straight line, with the other-rooms detour and the two non-paying outcomes beside it. It shows every choice the guest makes. This is my recommendation
- Outcome-first: grouped by what the guest ends up owing. It reads faster for finance, but it folds availability into one label and hides the other-rooms detour, which is a product decision

### The look
- Accent: the "New price?" decision, because it is the one node you'd keep if you could keep only one
- Zones: two, "Find a room" (nodes 1 to 4) and "Settle the price" (nodes 5 to 9)
- Title: Change booking dates
- Subtitle: How a Roamstay guest changes the dates on a booking, for the product and design team to review
- Source line: your description of the flow in this chat, with the left-out items named
- Critique question the gate will answer: does the eye land first on "New price?", and is that the node this review needs read first?

Does this reading stand, in particular the two edges your message didn't state? Correct any line, or say yes and the next reply is the write gate.