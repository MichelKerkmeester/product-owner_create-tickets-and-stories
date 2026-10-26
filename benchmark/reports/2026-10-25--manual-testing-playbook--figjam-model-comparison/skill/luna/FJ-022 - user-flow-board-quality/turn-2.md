**Playback**

**Question:** How does a Fernhouse customer start a return in the app, and where does the 30-day limit direct them?

**Outcome:** The reader can follow the path from the order list to a QR code confirmation, or to Contact support after 30 days.

Your confirmed app and returns-doc summary governs this flow. The older context note that self-serve returns are not live is superseded for this board. The €100 free pickup remains a proposal under review, so I’ll leave it out. The individual reason labels weren’t supplied, so I’ll show the reason-selection step without naming options.

I found an existing “Start a return” section in the FigJam file. I’ll add a separate section titled “Start a return in the app” and leave the existing one intact. The board stops at QR confirmation or Contact support; CS, warehouse, and refund handling are outside scope.

**Outline**

How does a Fernhouse customer start a return in the app, and where does the 30-day limit direct them?

- Entry: Order list
- Assumed move: Open an order to reach its detail. An app interaction would confirm the tap target
- Screen: Order detail with a Start a return button
- Move: Tap Start a return
- Decision: Within 30 days?
- Yes: Choose a return reason
- No: Contact support
- Move: Continue from reason selection to return-method choice
- Decision: Drop-off or pickup?
- Drop-off: Choose a drop-off point
- Pickup: Choose a courier pickup
- Either method: Return confirmed with QR code

**Framings:** I recommend a left-to-right user flow with the QR confirmation on the main path and the 30-day and method choices branching beside it. An eligibility-first decision tree would foreground the cutoff but make the customer’s screen sequence harder to follow.

**Look:** The confirmation with QR code gets the first glance; the drop-off or pickup choice gets the second; Contact support after 30 days is the last glance. I’ll use three zones: Find the order, Request the return, and Done. At laptop distance, the yes/no and drop-off/pickup exits should remain clear, and the proposal stays out of the flow.

Is this the right reading and outline, including the assumed tap from the order list to order detail?