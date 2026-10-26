# FJ-022 turn 2 transcript

**User:** Use your recommended answers.

**Assistant:**

This is the playback. It settles my reading of the request, and a yes to it writes nothing.

Question: which screens does a Fernhouse customer pass through to start a return in the app, and where do they choose?

Settled by the sources, which are your description of the app and the returns doc (I haven't seen the files):
- Screens, in your order: order list, order detail with a Start a return button, return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code
- Returns are open for 30 days after delivery, and after that the app shows Contact support (current behavior)
- Left out: the free pickup for orders over 100 euros, a proposal under review

Assumed, taken from my recommendations:
- Reader: the Fernhouse product and design team
- Outcome: they can follow a return from the order list to a confirmed return and see where the 30-day window ends it
- The window check sits on the order detail, and the screen order is the order you listed
- Display settings: balanced detail, a mixed audience and the Laptop reading distance
- That is three Brief rows assumed. Your answer to this playback settles each one

One source conflict. `context/fernhouse-context.md`, last updated 2026-09-18 for the 4.8 releases, says there is no self-serve return today. It says the customer contacts CS and an agent creates the return in Admin. Your request describes a Start a return flow in the app.
- My reading: the flow arrived after that note, because 4.9.0 was the next app release then. So your app and returns doc govern, and every node is current behavior.
- If the flow is not live yet, I'd mark the board's subtitle as a planned flow and not as current behavior.

Outline, as a user flow running left to right. Its first line is the sentence the board answers. Every node and edge below comes from the sources above.
1. Order list: start, from your list
2. Order detail: screen, from your list
3. Within 30 days of delivery?: choice, from the returns doc, position assumed
4. Contact support: end, the exit for No, from the returns doc
5. Pick a return reason: screen, from your list
6. Drop-off point or courier pickup?: choice, from your list
7. Confirmation with QR code: end and goal, from your list

Seven connectors:
- Order list to Order detail
- Order detail to the window check
- The window check to Pick a return reason, labelled "Tap Start a return" (Yes)
- The window check to Contact support (No)
- Pick a return reason to the method choice
- The method choice to the confirmation, labelled "Drop-off point"
- The method choice to the confirmation, labelled "Courier pickup"

That is 7 nodes and 7 connectors, with 4 labelled decision exits.

Two framings:
- A, recommended: the window is a choice after Order detail, with Contact support beside the main line. It shows where the 30 days ends the flow. The cost is that the check's position is assumed
- B: no window node, with the 30-day rule as a line in the subtitle. It has 5 nodes and no assumed position. The cost is that Contact support leaves the board and the reader can't see which screen the exit comes from

Look, as proposed choices:
- The one accent marks the confirmation as the goal. Contact support is an exit and not a failure to flag
- Three zones: "Find the order" (order list, order detail), "Request the return" (window check, Contact support, reasons, method choice) and "Done" (confirmation)
- Title "Start a return", with the subtitle "How a Fernhouse customer starts a return in the app, from the order list to a confirmed return"
- Source line: "Sources: the app and the returns doc. Left out: free pickup for orders over 100 euros, a proposal under review"
- Four questions the board must pass: where the eye goes first (it should be the confirmation), whether Contact support reads as an exit and not a step, whether the method choice reads as one choice with two exits, and whether any node is a step the sources don't state

Is this the right reading of the board, with your app and returns doc governing over the 18 September company note?
