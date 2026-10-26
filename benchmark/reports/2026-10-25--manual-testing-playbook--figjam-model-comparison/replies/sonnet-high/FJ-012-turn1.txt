Nothing is written to the board yet. Your request lists the parts but not the calls between them, so I need a few answers before I draw.

**Settled so far**
- Type: architecture. Your question is which parts make up block sync and how they connect, and that is what an architecture answers
- Parts: Desktop, Web and iOS clients, API Gateway, Sync Service, Push Worker, Blocks DB, File Storage, Change Stream and Apple Push, which makes 10
- Target: the existing file `<test-file-key>`, as a new section beside what it already holds. You ruled out a new file, so the Loomlist Engineering plan and the Barter drafts fallback don't apply. The write gate will confirm this before anything is drawn

**What the sources don't cover.** `context/loomlist-context.md` names `sync-service` as owner of sync sessions and device cursors. It names no gateway, change stream, push worker or file storage, and no calls between any of them. It also says push goes out through each platform's push service from `notifications-service`, and that nothing else in the product sends push. The only drawing of these links I have is the worked example in the skill, which is a fictional fixture. I treat it as a proposal, not a source.

**1. Reader and what stays off**
- Reading: the request names no reader
- Question: who reads the board, what do they decide from it and what must it not show?
- Recommended: engineers and PMs on sync work, who decide where a block change travels and where a push leaves the system. It shows no request order and no data fields
- Why: those are a sequence's and an ER diagram's questions, and mixing them in makes the board harder to read

**2. The calls**
- Reading: your list gives the parts and no connections
- Question: do these calls hold, and is the Push Worker part of `notifications-service` or a separate worker?
- Recommended, marked assumed until you confirm:
  - Desktop, Web and iOS each send requests to the API Gateway
  - API Gateway routes to Sync Service
  - Sync Service writes Blocks DB
  - Sync Service stores files in File Storage
  - Sync Service publishes to Change Stream
  - Change Stream feeds Push Worker
  - Push Worker calls Apple Push to wake the iOS device
- Why: it is the shortest path that uses every part you named. I have no source for a live two-way socket on Desktop or Web, so all three clients draw as plain requests. The board shows the outbound call to Apple Push and leaves out the push reaching the phone, because the architecture layout has no edge from an outside service back to a client

**3. Budget**
- Reading: 10 parts against a budget of 9 nodes and 12 connectors per architecture
- Question: split into two boards or drop a part?
- Option A: two boards in the same file
  - "1. Block sync" has the three clients, gateway, Sync Service, Blocks DB, File Storage and Change Stream (8 nodes, 7 connectors)
  - "2. Push wake-up" has Change Stream, Push Worker and Apple Push (3 nodes, 2 connectors)
- Option B: one board of 9 nodes without File Storage
- Recommended: A
- Why: B drops a part you named, and nothing I have says sync never touches file storage. The context page lists files and images as block types. The cost of A is that board 2 is small

Answer any of these you want to change. A question you skip proceeds on its recommendation, marked assumed in the playback.