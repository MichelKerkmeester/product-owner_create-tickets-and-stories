Here is how I read the board. I haven't drawn or written anything.

Question: which parts take part in block sync, and how do they connect?

Outcome: the Sync team can see which parts a block change passes through, from a client to the other devices.

Settled by your answers
- Type: architecture
- Reader: the Sync team
- Parts drawn (nine): Desktop App, Web Client, iOS App, API Gateway, Sync Service, Blocks DB, Change Stream, Push Worker and Apple Push
- Calls (eight):
  - Each of the three clients calls the API Gateway
  - The API Gateway routes to Sync Service
  - Sync Service writes to the Blocks DB and publishes to the Change Stream
  - The Push Worker consumes the Change Stream and calls Apple Push to wake iOS devices

Left out: file storage. No part on the sync path calls it, and drawing it would leave an orphan node.

Assumed, with what settles each
- The eight calls are my wiring, not a doc's. The board's source line will say so. The sync-service doc settles it.
- Edge labels are plain verbs such as Routes, Writes and Publishes, with no protocols. A doc naming WebSocket or HTTPS settles it.
- Balanced detail, mixed audience and laptop reading distance, with no objection from you

Proposed look, all recommended
- Title "Block sync", with a subtitle saying it shows the parts that carry a block change to the other Loomlist devices
- The first glance lands on Sync Service, because every change is written and published there
- No zones beyond the six fixed lanes, since the lanes already group the parts

Still open: none.

Is this the right reading of the board?