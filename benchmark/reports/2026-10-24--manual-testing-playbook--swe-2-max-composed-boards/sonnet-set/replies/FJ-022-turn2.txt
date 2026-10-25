Your confirmation settled the reading, so I've built the model and it's ready. Nothing is on the board yet. This message is the write gate, and I'm waiting for your yes.

**Settled**
* The app screens and the returns doc govern over the 2026-09-18 context note. This is assumed, because I couldn't check whether the flow is live
* Reader is Fernhouse product and CS. The outcome is that they can see the full path and where the 30-day cut-off sends a customer to Contact support (both assumed, from your recommended answers)
* The board shows no CS or Admin steps, no free-pickup proposal and no screen between the method choice and the confirmation
* Detail is balanced, the audience is mixed, and the reading distance is laptop

**Assumed, correct me before the write**
* The returns doc doesn't say which screen shows Contact support after 30 days. I placed the window check right after Order detail. This is the one edge I inferred, so I re-read its source and it states no screen
* The method choice goes straight to the confirmation, so no drop-off or pickup detail screens are drawn

**Glance lines**
* First: the confirmation with QR code, marked as the goal
* Second: the 30-day check that sends a late customer to Contact support
* Last: the source line, which names the free-pickup proposal as left out

**Model check**
* `flow_check.py` passed: 7 nodes, 7 connectors, 4 labelled decision exits, 0 crossing pairs
* `compose_board.py` composed it
* Flow: Order list, Order detail, "Within 30 days?" (No leads to Contact support), Pick a return reason, "Drop-off or pickup?" (Drop-off point or Courier pickup, both leading to Confirmation with QR code)
* Zones: Find the order, Request the return, Done

**Gate**
* File: existing FigJam file `<test-file-key>`. You named the Fernhouse Product plan. I haven't verified it, because a board keeps the plan its file was created in
* Writes: one composed board section titled "Start a return", with a key and a source line. It lands 400 pixels to the right of everything already on the page and carries a `productowner` tag. No existing node is touched, and no new file or page is made
* Calls: `create_session`, one `use_figma` and one `get_figjam` read-back. I'll also read Figma's `figma-use` and `figma-use-figjam` guidance first if the server serves it. On a Starter plan or a View or Collab seat, reads count toward Figma's six tool calls a month
* Rollback: delete that one board section through `use_figma`, and only after your separate yes to the deletion

Write it?