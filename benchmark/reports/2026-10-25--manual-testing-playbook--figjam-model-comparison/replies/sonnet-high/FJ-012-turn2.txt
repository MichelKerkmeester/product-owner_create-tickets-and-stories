Here is how I read the request. Nothing is drawn or written yet.

**Question:** which parts take part in block sync and how do they connect?

**Outcome:** engineers and PMs on sync work can see where a block change travels and where a push leaves the system.

**Settled by your answers**
- Type: architecture
- Reader: engineers and PMs on sync work
- Kept off the board: request order and data fields
- Split: two boards in the same file, since 10 parts is one over the budget of 9 nodes
  - "1. Block sync" has the Desktop, Web and iOS clients, API Gateway, Sync Service, Blocks DB, File Storage and Change Stream. That is 8 nodes and 7 connectors
  - "2. Push wake-up" has Change Stream, Push Worker and Apple Push. That is 3 nodes and 2 connectors. Change Stream is the hand-off between the two

**Assumed (2 rows)**
- The calls. No source states them, so I draw the proposal as given, with every connector a plain request or call. The clients each send requests to the gateway, the gateway routes to Sync Service, and Sync Service writes Blocks DB and File Storage. It also publishes to Change Stream, which feeds Push Worker, and Push Worker calls Apple Push. The board's source line will say the calls are proposed and not confirmed against code. Checking the sync-service routes and the stream consumers settles this row
- Push Worker is its own deployable part, as you named it, and not `notifications-service`. `context/loomlist-context.md` says nothing else in the product sends push, so asking the sync owners settles this row

**Left out:** the push reaching the iOS device, because the architecture layout has no edge from an outside service back to a client. Android and its push service are left out because your request doesn't name them.

**Still open:** none beyond the two assumed rows.

Is this the right reading of the board?