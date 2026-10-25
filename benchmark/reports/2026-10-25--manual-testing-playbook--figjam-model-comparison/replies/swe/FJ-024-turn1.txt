The file is confirmed: a live FigJam board holding many composed boards already — including several earlier "Block sync" boards and one "Loomlist block sync". The new board will land at the right edge beside them.

Type check: the request names an architecture diagram, and the question it answers — which parts make up block sync and how they connect — is exactly what an architecture draws. One catch: the request lists ten parts, but nothing in the stated sync path connects to file storage, and ten is one over the nine-node budget. That goes into the playback as a named cut with a recommended answer.

Here is the playback — the reading before any drawing:

```text
Before I draw anything, this is how I read the request.

Question: which parts take part in Loomlist block sync and how do they connect?
Outcome: the Loomlist Engineering team can trace a block change from one client to the others and see which part owns each hop.

Settled by the request:
*   Desktop App, Web Client and iOS App, each holding a live socket to the API Gateway
*   API Gateway routing to Sync Service
*   Sync Service writing every block change to the Blocks Database and publishing it to the Change Stream
*   Push Worker reading the Change Stream and waking sleeping iOS devices through Apple Push Service

Left out: file storage. Nothing in the stated path calls it, so no edge can be drawn to it without inventing a call, and the ten parts together are one over the nine-node budget. If sync-service does write to file storage, name the call and I will draw it, either with the three clients folded into one node to stay in budget or as a second board.

Assumed: balanced detail, a mixed audience and the Laptop reading distance.

Outline:
*   Which parts take part in Loomlist block sync and how do they connect?
*   Clients: Desktop App, Web Client, iOS App
*   Edge: API Gateway
*   Services: Sync Service, Push Worker
*   Stores: Blocks Database
*   Events: Change Stream
*   External: Apple Push Service
*   Clients <-> API Gateway, "Holds live socket", three edges
*   API Gateway -> Sync Service, "Routes block sync"
*   Sync Service -> Blocks Database, "Writes block changes"
*   Sync Service -.-> Change Stream, "Publishes"
*   Change Stream -.-> Push Worker, "Reads"
*   Push Worker -.-> Apple Push Service, "Apple Push Service: Wakes iOS devices"

Two framings:
a) All ten parts you named: file storage stays only if you can name its caller, then the three clients fold into one node or the diagram splits into a sync path and a storage path.
b) Recommended: the nine parts the sync path actually connects. File storage is named as left out and every hop a block change takes stays on one board.

The look: Sync Service carries the focus marker, since every block change passes through it. No zones, the six lanes are the grouping. Title "Loomlist block sync", subtitle naming the engineering reader, source line naming this description and the file-storage cut.

Is this the right reading of the board?
```

**Is this the right reading of the board?** In particular: does file storage stay out, or should I draw it and name the call that connects it?