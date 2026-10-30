Here is the reading, before any model exists. Your "use the recommended answers" settles round one, so every recommendation below stands as assumed.

**Question:** which parts carry a block change from one client to the others, and which part owns each rule?
**Outcome:** an engineer new to block sync can say which part checks the token, merges edits, keeps history, holds events and limits wake-ups.
**Dials:** Balanced detail, Engineer audience, Laptop distance.

**What the sources settled**
- **Type:** architecture, nine parts in its fixed lanes.
- **Calls:** the platform doc states every call except one. Gateway to sync-service is the only route the layout allows, so I'm drawing it. You accepted it last round.
- **Rules:** the five rules go in as short lines under their parts.

**Outline, in drawing order**
- **Clients:** Desktop App, Web App and iOS App
- **Edge:** API Gateway
- **Services:** sync-service and Push Worker
- **Stores:** Blocks Database
- **Events:** Change Stream
- **External:** Apple Push Service
- **Edges (8):**
  - three two-way `WebSocket` lines, one per client to the gateway
  - gateway to sync-service, `Routes sync traffic`
  - sync-service to Blocks Database, `Writes Blocks`
  - sync-service to Change Stream, `Publishes changes`
  - Change Stream to Push Worker, `Consumes changes`
  - Push Worker to Apple Push Service, `Apple Push: Wakes iOS device`
- **Body lines:**
  - Gateway: `Checks the session token` and `Keeps each client socket open`
  - sync-service: `Merges edits to the same block`
  - Blocks Database: `Keeps 30 days of block history`
  - Change Stream: `Keeps events for 7 days`
  - Push Worker: `At most one wake-up per device per minute`

**Two framings**
- **One board with the wake-up branch:** the whole path from client to sleeping iOS device on one board, at 9 nodes and 8 connectors. This is my recommendation, because it answers the question in one view.
- **Two boards, write path and wake-up path:** each is simpler, but a reader has to join them to see that the stream feeds the wake-up. It only earns its place if file storage returns.

**The look**
- **First glance:** sync-service, because every change is written and published there.
- **Second glance:** the Change Stream, then the API Gateway.
- **Last glance:** Apple Push Service.
- **Zones:** the six lanes are the zones, so I add none.
- **Title and subtitle:** `Block sync`, with the subtitle "How a block change travels from a client to every other client, including a sleeping iOS device, for engineers new to block sync".
- **Source line:** "Source: the platform doc. Left out: file storage, no call stated in the doc".

**Assumed**
- **Reader:** engineers new to block sync, because no source names one. Say a different reader and I change the audience and the bodies.
- **File storage:** left off the board, because the doc states no call to or from it. A call from you brings it back.

**Left out:** file storage, no call stated in the doc.

Is this the right reading of the board?