Your three recommendations are in. Nothing is written yet, and I've made no Figma calls. This is the reading, and it needs one answer before I build the model.

**The Brief**
- **Reader:** Loomlist engineers (assumed, settled by your naming the real audience)
- **Question:** which parts does a block change pass through between a client and a push notification?
- **Outcome:** the reader can say which service owns each hop
- **Scope:** the block sync and push path. File storage, call order, retries and deployment detail stay off the board
- **Entry:** the desktop, web and iOS clients
- **Exit:** Apple's push service
- **Actors:** sync-service and the push worker are the two services
- **Decisions and states:** none, because an architecture shows parts and calls
- **Sources and class:** your request, as your description of the system. It states the parts but no calls

**What is captured and what is assumed**
- Captured: the 10 parts and the existing file as the target
- Assumed:
  - The reader, question and outcome above
  - All 8 connections, because no source states a call
  - Sync-service as the publisher to the change stream
- A doc, repo or service map would turn the connections from assumed to captured. The board's source line will say they are assumed, since a board has no marker for it.

**Outline** (`userIntent`: which parts does a block change pass through between a client and a push notification?)
- Nodes (9), by lane:
  - Clients: desktop, web, iOS
  - Gateway: API gateway
  - Services: sync-service, push worker
  - Datastore: blocks database
  - Async: change stream
  - External: Apple push
- Connections (8), with draft labels:
  - Each of the three clients calls the gateway: "Syncs blocks"
  - Gateway calls sync-service: "Routes sync requests"
  - Sync-service calls the blocks database: "Reads and writes blocks"
  - Sync-service publishes to the change stream: "Publishes block changes"
  - The change stream feeds the push worker: "Consumes changes"
  - Push worker calls Apple push: "Apple push: Sends notifications"
- Left out:
  - File storage, over the 9-node budget
  - Apple's push service reaching the iOS client, because the board has no outside-to-client arrow

**Two framings**
- **One board, recommended:** the path reads left to right from clients to Apple push. It gives one picture and costs file storage.
- **Two boards, block sync and push delivery:** this keeps all 10 parts. It costs a second board, and sync-service would appear on both.

**The look**
- First glance: sync-service, the one part every hop touches (assumed)
- Detail level and audience: Balanced, with exact service names for engineers
- Reading distance: Laptop
- Zones: the six lanes already group the parts, so there are no extra zones
- Title: "Block sync services"
- Subtitle: "How a block change reaches the sync-service, the blocks database and Apple push"
- Source line: "Sources: Loomlist request. Connections assumed, no service doc. Left out: file storage, Apple push to iOS"

Is this reading right, or what changes?