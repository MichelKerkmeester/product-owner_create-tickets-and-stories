Here is the playback. Nothing is drawn or written yet.

**Question:** which services carry a block change from a client to a woken iOS device?
**Outcome:** a Loomlist engineer can see where a change is written, published and pushed.

**Settled by your message**
- Nine parts, one board, in the file you named
- Clients hold a live socket to the gateway
- sync-service writes every block change and publishes it to the change stream
- The push worker reads the stream and wakes sleeping iOS devices through Apple's push service

**Assumed, with what would settle each**
- Reader, question and outcome above, because you accepted my reading. A source naming the audience would settle it
- Gateway to sync-service, labelled "Routes block changes". The sync-service doc or you would settle it
- sync-service writes to the blocks database, since you named no other store for its writes
- Balanced detail, engineer audience and laptop distance

**Left out**
- File storage: no stated connection, and ten parts is one over the nine-node budget
- The Apple Push to iOS hop as a connector: an architecture has no edge from an outside service back to a client, so the label "Apple Push: Wakes iOS devices" carries it
- Retry and failure paths, message order and any service beyond the nine you named

**Outline, in drawing order**
1. userIntent: which services carry a block change from a client to a woken iOS device?
2. Nodes, by lane: Desktop client, Web client and iOS client (clients), API gateway (gateway), sync-service and Push worker (services), Change stream (async), Blocks database (datastore), Apple Push (external)
3. Edges, each solid unless it touches the stream or Apple:
   - Each of the three clients <-> API gateway, "Live socket"
   - API gateway -> sync-service, "Routes block changes"
   - sync-service -> Blocks database, "Writes blocks"
   - sync-service -> Change stream, "Publishes changes" (dashed)
   - Change stream -> Push worker, "Consumes changes" (dashed)
   - Push worker -> Apple Push, "Apple Push: Wakes iOS devices" (dashed)

The remove test cuts nothing. That is nine nodes and eight connectors, and "Live socket" appears on three edges, under the limit of four.

**Two framings**
- One architecture of the whole path (recommended). It buys the write path and the wake path in one picture and costs the order of the calls, which a sequence would show
- Two boards, live sync and wake path. It buys less crowding and costs a second board and the change stream drawn twice, which nine nodes don't need

**The look, as I'd draw it**
- Colour mark: sync-service, with the key entry "Writes every block change", since every change passes through it
- Zones: the six architecture lanes, each named on the board
- Title "Loomlist block sync", subtitle "The services that carry a block change from a Loomlist client to a woken iOS device, for engineers on sync", and a source line naming your request and the file storage cut
- At the gate I'll show the checked sketch and answer four critique questions about it, starting with where the eye lands first

Is this the right reading of the board?