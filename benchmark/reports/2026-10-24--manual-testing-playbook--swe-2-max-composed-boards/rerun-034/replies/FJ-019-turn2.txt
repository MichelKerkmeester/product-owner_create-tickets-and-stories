I'm using your answer as the recommendation on all three questions. Each one stays marked assumed, so correct any of them before I build the model. This is the playback, so nothing is written yet and no model exists.

**Question:** which parts take part in block sync, and how do they connect?

**Outcome:** Sync and Mobile Platform engineers can see which parts carry a block change from one device to the others.

**What your request settled**
* The nine parts on the board: desktop, web and iOS clients, API gateway, sync-service, push worker, blocks database, change stream and Apple's push service
* Type: architecture
* Target: file `<test-file-key>`, Loomlist Engineering plan

**Assumed**
* The reader is Sync and Mobile Platform engineers
* The calls come from my draft, not from a source. Each edge label is a placeholder for you to correct:
  * Desktop, web and iOS to API gateway: "Sync requests"
  * API gateway to sync-service: "Routes sync"
  * Sync-service to blocks database: "Writes blocks"
  * Sync-service to change stream: "Publishes changes"
  * Change stream to push worker: "Consumes changes"
  * Push worker to Apple's push service: "Apple Push: Wakes device"
* File storage is not drawn. Question 2 had no recommended call for it, and drawing it would mean inventing one. Without a call it would sit on the board unconnected, which the architecture check refuses. Leaving it out brings the board to 9 nodes and 8 connectors, so one board fits and no split is needed
* Detail is balanced, the audience is mixed (so `sync-service` reads "Sync Service") and the reading distance is laptop

**Still open**
* File storage: naming the part that reads or writes it, or the doc that states the calls, would add it back. Adding it would take the board to 10 nodes, so it would split into two boards
* Push worker: the context page says push for mentions, replies and shares is the only push the product sends. I can't tell if your push worker is a separate sync wake-up path or part of that path. I'll draw it as you named it and won't call it part of notifications

**Left out:** file storage, because no call to it is stated. The Android client and its push service, because they are not in your list.

**Tool check:** the tool listing in this turn shows no Figma tools, only the OpenCode ones. I'll list the tools again before the write step. If the Figma connection hasn't come back by then, the board can't be written, and I'll offer you the checked model instead.

Is this the right reading of the board?