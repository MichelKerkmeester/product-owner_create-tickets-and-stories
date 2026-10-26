Before I draw anything, this is how I read the request. Nothing has been written to the board.

**Settled from your message**
- Type: architecture, because you named it and the brief is parts and how they connect
- Target: file `<draft-file-key>` takes the board as a new section beside what it holds, and nothing already there changes. That needs no plan call and no new file
- The path you described: three clients hold a live socket to the gateway, sync-service writes each block change to the blocks database and publishes it to the change stream, and the push worker reads the stream and wakes iOS devices through Apple's push service

**Assumed**
- Gateway to sync-service, labelled "Routes block changes". You didn't state this edge, but an architecture needs a gateway between clients and a service. Correct me if the gateway routes elsewhere

**Heads-up**
- An architecture has no connector from an outside service back to a client. The Apple push to iOS hop therefore rides in the push worker's edge label ("Apple Push: Wakes iOS devices"). A sequence diagram would draw that hop as its own message
- Your two plan lines name different plans, Loomlist Engineering and Barter. This only matters if the file can't take the board. In that case I'd stop and ask before creating anything

**Three questions, one reply covers them**

1. Reader, question and outcome
   - Reading: Loomlist engineers working on sync, asking which services carry a block change from a client to a woken iOS device. They should leave able to see where a change is written, published and pushed
   - Dials: balanced detail, engineer audience (exact names such as sync-service), laptop reading distance
   - Recommended: all of the above
   - Why: it follows your description without adding a source

2. File storage
   - Reading: ten parts against a nine-node budget, and you describe no call to or from file storage
   - Recommended: leave it off and name it under `Left out:`
   - Why: it is the only part with no stated connection
   - Alternative: tell me which service uses it and I'll split into two boards, live sync and wake path

3. What the board must not do
   - Recommended: no retry or failure paths, no message order, and no services beyond the nine you named
   - Why: you described one path, and the board should be one picture of it

Reply "use the recommended answers" to settle all three. The playback comes next, then the write gate, and the board is written only on your yes to the gate.