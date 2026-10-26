I'll write the Story for the Fernhouse return flow, then draw its screens on a FigJam board. The Fernhouse context says there is no self-serve return today: a customer contacts CS, an agent creates the return in Admin and emails a label, the warehouse checks the item and the agent refunds. No return-flow brief, design link or screenshots came with the request, and the board can only show screens a source supplies. Before drafting, I need the decisions below in one response. Where you do not know, the recommendation stands and I list it as an open item.

**Operation:** Is this a new Story, or a refinement of an existing one? For a refinement, which file? Recommended: a new Story.

**Which flow:** Is the Story the customer-facing return request (a self-serve start-a-return flow), the CS agent's return creation in Admin, or both? Recommended: the customer-facing request on web, iOS and Android, because that is the part the context says does not exist yet. The agent side then stays out of scope.

**Role & value:** Who is the user, and what should they be able to do that they cannot today? Recommended: a Customer who can ask for a return without contacting CS, which targets the return requests CS handles each month (about `1,900`) and the `6 days` average from first contact to refund.

**Requirements:** Which hard constraints must the Story carry, with exact values and copy? Candidates from the context are the `30 days` return window from delivery, the return reasons, how the label reaches the customer, the refund rule, parcel and pallet items, and UK parcels. Send the exact strings and limits you want, per screen if the design is organised that way.

**Screens & decisions:** Which screens does the customer pass through, in order, and where do they choose? Send the design link, screenshots or a list of screen names. The FigJam board is drawn from these, so a screen I cannot read from a source is left off it.

**Board reader:** Who reads the board and what should they decide afterwards? Recommended: product and CS leads deciding whether the flow covers the cases CS sees today, with the question "which screens does a customer pass through to start a return, and where do they choose?"

**Shared machinery & kind:** Do web, iOS and Android share one mechanism, or does the work split into child stories that need an Epic? Recommended: one Story, with the three platforms sharing one flow.

**Validation:** What should I not assume about the flow? For example whether refunds can be exchanges or store credit, whether a CS agent still reviews every return, or whether the free-return rules differ by market.
