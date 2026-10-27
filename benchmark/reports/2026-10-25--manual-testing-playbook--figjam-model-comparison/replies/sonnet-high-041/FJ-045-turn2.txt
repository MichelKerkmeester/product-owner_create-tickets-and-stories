Here is the full reading before I draw anything. The next step is the model, then a separate write confirmation.

One caveat first. I have your description of the app and the returns doc plus `context/fernhouse-context.md`, but not the screenshots or the returns doc themselves. Every node below rests on your description.

### What is settled
- Question: how does a signed-in customer start a return in the app
- Outcome: Post-purchase and CS can check each step and the 30-day cut-off against the returns doc
- Status: current behavior, so your app and returns doc govern the screens (accepted from my recommendation, assumed)
- Window: 30 days from delivery, which the context doc also states (captured)
- Both methods end on one confirmation with a QR code (accepted, assumed)
- Contact support appears at the window check, after the order detail (assumed)
- Opening an order from the list is a tap on that order (assumed, since no source names the trigger)
- Signed-in only, because the context doc says guests have no order history to come back to (assumed)
- Detail level Balanced, audience Mixed, reading distance Laptop (assumed)

What would settle the assumed status is the 4.9.0 release notes or the app version that carries the flow. If it is not live, the labels take a proposal status.

### Outline
1. userIntent: show the screens a signed-in customer passes through to start a return, and where the 30-day window sends them to support
2. Node: Order list (start)
3. Node: Order detail (screen)
4. Node: Within 30 days of delivery? (decision)
5. Node: Return reasons (screen)
6. Node: Drop-off or courier? (decision)
7. Node: Confirmation with QR code (goal)
8. Node: Contact support (exit)
9. Edge: Order list to Order detail, opens an order
10. Edge: Order detail to the window check
11. Edge: window check to Return reasons, labelled Yes with the Start a return button
12. Edge: window check to Contact support, labelled No
13. Edge: Return reasons to the method choice
14. Edges: method choice to the confirmation, one labelled Drop-off point and one labelled Courier pickup

That is 7 nodes and 7 edges, inside the 9-node budget. The remove test cuts nothing, since each node is a step you named. I added no screens for picking a drop-off point or a pickup slot, because no source shows them. The method choice is one decision with both exits meeting at the confirmation.

### Two framings
- A, recommended: the happy path runs on one straight line to the confirmation, with Contact support beside it. It matches the order you gave the screens in and keeps the cut-off visible without a second main line.
- B: a state map that gives every exit equal weight. It loses the main line and the QR goal, and it invites the post-confirmation states you want kept out.

### The look
- Accent: the window decision. It is the node a reviewer would keep if they could keep only one, because it is where the app diverts to support. The confirmation stays green as the goal and Contact support stays orange as an exit.
- Glance lines. First: the 30-day window decision. Second: the two places it leads, the QR confirmation and Contact support. Last: the reasons and the method choice, which stay readable without competing.
- Zones: none. Seven nodes read as one line, and a tint for two nodes would only add a key entry.
- Title: Start a return
- Subtitle: how a customer starts a return in the app, from the order list to the QR confirmation, for Post-purchase and CS to check against the returns doc
- Source line: the Fernhouse app and returns doc as described in the request, and the Fernhouse context doc for the window
- Critique questions for the sketch: does the eye land on the window check first, can a reader follow the Yes path without crossing a line, do the Contact support and QR ends read as different outcomes, and does the key explain every colour

### Left out so far
- Everything after the confirmation: the parcel handover, the warehouse check and the refund
- Screens inside each method, because no source shows them
- Item selection on an order with several items, because the sources don't mention it
- Orders not yet delivered, because the window starts at delivery and the sources don't say what the button does before that
- Guest customers

**Does this reading match?** Recommended: yes, move on to the model. I'd take that unless a row above is wrong, and a correction to any row replays just that row.