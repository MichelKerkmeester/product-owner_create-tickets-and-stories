Here is the playback before I model anything. Your answer to it settles the reading, and it doesn't approve a write.

**Question:** which parts make up Loomlist block sync, and how do they connect?
**Outcome:** engineers and the product owner can name every part a block change passes through and see what sits outside the system.

**Settled by your request:** the ten parts and the type.
**Settled by your answer to the three questions:** the reader, the refusals and the connections below.

**Assumed, each marked on the board and correctable now:**
* Reader and outcome, as above. A source for them would settle it
* Connections, all eight. Only you or a sync doc can confirm them. The board's source line will say they are not yet confirmed
* File storage is off the sync path. A call that reaches it would settle that and change the scope
* Balanced detail, a mixed audience and the Laptop reading distance. Labels read "Sync Service" and "Blocks DB" rather than the code names

**Refusals:** no call order, no payloads, no deployment detail and no unconfirmed connection drawn as fact.

**The outline, in drawing order:**
1. The question above, in one sentence. The write call receives it too
2. Nodes, 9 of the 9 allowed
   * Clients lane: Desktop App, Web App, iOS App
   * Edge lane: API Gateway
   * Services lane: Sync Service, Push Worker
   * Stores lane: Blocks DB
   * Events lane: Change Stream
   * External lane: Apple Push
3. Connectors, 8 of the 12 allowed. Each client calls the gateway (3), the gateway routes sync requests to Sync Service, Sync Service writes Blocks DB, Sync Service publishes to the Change Stream, the Push Worker consumes the stream and the Push Worker calls Apple Push

**Left out:** file storage, off the sync path, cut because ten parts is one over the budget.

**Two framings:**
* One board for the sync path. It answers the question on its own and costs the file-storage part. This is my recommendation
* Two boards, sync and file handling. It keeps all ten parts and costs a second board, but file storage has no confirmed connection yet, so it would be drawn on a guess

**The look, as proposed choices:**
* First glance: Sync Service, where a block change is written and published. The Change Stream is the second glance and Apple Push the last
* Zones: the six lanes, which are zones already
* Title "Block sync". Subtitle "The parts a block change passes through in Loomlist sync, for engineers and the product owner". Source line "Source: the request, connections assumed, not yet confirmed. Left out: file storage, off the sync path"
* Detail, audience and distance as assumed above

**Still open:** none.

Is this the right reading of the board?