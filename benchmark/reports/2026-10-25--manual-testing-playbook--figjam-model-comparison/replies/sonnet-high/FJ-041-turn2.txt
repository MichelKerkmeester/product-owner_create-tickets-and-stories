Thanks, I've taken those as your answers. The type is a user flow, the reader is the product and design team, and failure paths and back-office steps stay out. Nothing is written to the board yet.

Playback

- Reader: the product and design team
- Question: which screens does a customer pass through to return an item, and where do they choose?
- Outcome: the team agrees the customer-side steps and the two outcomes before a story is written
- Scope: the customer side only. Failure paths and back-office steps are out
- Entry: the customer opens an order
- Exit: the customer sees a confirmation
- Actors: the customer
- Decisions: refund or store credit is the one choice. "Pick a reason" is a plain step, because you gave no list of reasons and I won't invent one
- Detail, audience, distance: balanced, mixed audience, laptop (the defaults)
- Source: your request only

Assumed, with what would settle each
- One confirmation shared by both outcomes. A returns doc or the confirmation screens would settle it
- The flow is current behaviour, not a proposal. You can settle it by telling me

Outline, in drawing order
1. The sentence the board answers: how a customer gets from an open order to a return confirmation, and where they choose refund or store credit
2. Node: Order opened (start)
3. Node: Return an item
4. Node: Pick a reason
5. Node: Refund or store credit? (decision)
6. Node: Confirmation shown (goal)
7. Edges: Order opened to Return an item, then Pick a reason, then the decision
8. Edges: the decision to Confirmation shown, once labelled Refund and once labelled Store credit

That is five nodes and five connectors. Each node is a step you named, so the remove test cuts nothing.

Two framings
- Recommended: both choices run into one confirmation. It keeps the board to what you described and stays short.
- Alternative: one confirmation per choice, six nodes. It only helps if the two confirmations differ, and nothing you gave says they do.

Look, all proposed
- The marked node is the decision, because the choice is the part a reader would keep if they could keep one
- No zones, because five nodes read as one group
- Title: Fernhouse return flow
- Subtitle: How a customer starts a return from an order, picks a reason and chooses a refund or store credit
- Source line: Source: the request. Left out: failure paths and back-office steps

An answer you skip stands as the recommendation and stays marked assumed.

Does this reading hold, or what should change?