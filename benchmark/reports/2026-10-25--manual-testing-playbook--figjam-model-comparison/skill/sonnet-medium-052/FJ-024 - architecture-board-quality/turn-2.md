Here is the reading before I write the model.

**Question:** which parts take part in block sync and how do they connect?
**Outcome:** Loomlist Engineering can tell which part to open for a problem with writes, delivery or wake-ups.
**Detail, audience, distance:** Balanced, Engineer, Laptop.

**What the sources settled**
- **Parts (9):** the desktop, web and iOS clients, API gateway, sync-service, push worker, blocks database, change stream and Apple's push service.
- **Calls (8):** the three clients hold a live socket to the gateway. sync-service writes every block change to the blocks database. It also publishes each change to the change stream. The push worker reads the stream and wakes sleeping iOS devices through Apple's push service.
- **Rules shown as part bodies:** the gateway checks the session token and keeps each socket open. sync-service merges edits to the same block. The blocks database keeps 30 days of history. The change stream keeps events for 7 days. The push worker sends at most one wake-up per device per minute.

**Look**
- Title `Block sync`, with a subtitle running from a client's block change to the wake-up of a sleeping iOS device.
- The first glance goes to sync-service, where every change is written and published.

**Left out:** file storage, because no source states a call to or from it. The board also shows no message order and no upload path.

**Assumed**
- **Reader:** Loomlist Engineering. No source names them. Your confirmation would settle it.
- **Gateway to sync-service:** the edge reads `Routes sync requests`. The doc excerpt would settle it.

**Still open:** none. Entry is the three clients, exit is Apple's push service, and the board has no decisions or states.

Is this the right reading of the board?