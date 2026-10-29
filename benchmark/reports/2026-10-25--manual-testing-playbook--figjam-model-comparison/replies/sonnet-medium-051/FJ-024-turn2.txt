Playback of the reading before I draw anything.

The board answers: which services does a block change pass through, and what wakes a sleeping iOS device? A Loomlist engineer should be able to place a new service or find where a sync bug lives. The board shows parts and the calls between them, and no call order or retries.

Settings: Balanced detail, Engineer audience, Laptop distance.

What each source settled (your description is the only source, and it states current behavior):
- Parts: desktop client, web client, iOS client, API gateway, sync-service, push worker, blocks database, change stream and Apple's push service
- Calls: each client holds a live socket to the gateway, sync-service writes every block change and publishes it to the change stream, and the push worker reads the stream and wakes sleeping iOS devices
- Target: file <test-file-key>, as a new section in the Loomlist Engineering plan

Assumed, and what would settle each:
- Reader, question and outcome: taken from my recommendation, since no source names them. You settle them by naming the reader and the question
- Gateway routes to sync-service: you did not state it, and the lanes require a gateway between clients and services. You settle it by saying how clients reach sync-service

Left out:
- File storage: no part is described as calling it. It returns when you name a caller, and then the board has 10 parts and splits in two
- Apple's push service to the iOS device: no edge exists for it, so it rides in the push worker's edge label

The outline, one line per part and call:
1. Lane Clients: desktop client, web client, iOS client
2. Lane Gateway: API gateway
3. Lane Services: sync-service, push worker
4. Lane Stores: blocks database
5. Lane Events: change stream
6. Lane Outside: Apple push service
7. Each client to the API gateway, two-way, "Live socket", three edges
8. API gateway to sync-service, "Routes block changes"
9. Sync-service to blocks database, "Writes blocks"
10. Sync-service to change stream, dotted, "Produces block changes"
11. Change stream to push worker, dotted, "Consumes"
12. Push worker to Apple push service, dotted, "Apple push service: Wakes sleeping iOS devices"

That is 9 nodes and 8 connectors, inside the limit of 9 and 12.

Two framings:
- One board, with the change stream as the fork where the write path turns into the wake path. It shows the whole story in one view but leaves file storage off. This is my recommendation
- Two boards, "1. Block sync" and "2. Push wake-up". Each is easier to read, but the reader has to join them across boards, and it only pays off once file storage has a caller

The look I propose:
- First glance: the change stream, because every block change passes through it and it is where the push path begins
- Second glance: sync-service, which feeds it
- Last glance: Apple's push service
- Zones: the six lanes, so no zone lines
- Title: "Loomlist block sync services"
- Subtitle: "From a block change on any client to a woken iOS device, for Loomlist engineers"
- Source line: "Source: the sync services description. Left out: file storage, no caller stated."

Does this reading hold, or should I correct any row?