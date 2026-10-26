This reads as an architecture board, so I've loaded the Flow Mode references and run no checks or writes yet. Three things need your input first.

**What your request settles**
- **Type:** architecture, because the question is which parts make up the system and how they connect.
- **Parts:** 10 nodes from your list: Desktop, Web and iOS clients, API gateway, sync-service, push worker, blocks database, file storage, change stream and Apple's push service.
- **Target:** file `<draft-file-key>`, as a new section beside what it already holds. Nothing already on it changes, so no plan is picked and no new file is created. I'd use the Barter drafts fallback only if that file can't take the write. I can't confirm from here that the file sits in the Loomlist Engineering plan.
- **Source:** your message only, with no doc, repo or schema yet.
- **Budget:** an architecture board holds 9 nodes and 12 connectors, so 10 parts won't fit on one board. I'll propose two boards split by path in the playback, "Block sync" and "Push delivery".

**1. Reader and question**
- Reading: the request names the parts but not who reads the board or what they decide from it.
- Question: who is the board for, and what should they be able to answer after reading it?
- Recommended: engineers on the sync team and new joiners, answering "which parts carry a block change from a client to the push notification?"
- Why: that question needs the parts you listed and nothing else.

**2. What the board must leave out**
- Reading: the architecture layout has no edge from an outside service back to a client, so delivery from Apple's push service to the iOS device can't be drawn.
- Question: what must the board not show?
- Recommended: leave out auth, retries, conflict handling and the Apple-to-iOS delivery, and name each under `Left out:`.
- Why: each of those is a different diagram, and a cut that is named is not a gap the reader has to guess at.

**3. How the parts connect**
- Reading: you listed the parts but not the calls between them. I won't invent calls.
- Question: which doc, repo path or schema states the calls, or is this path right?
- Recommended: if there's nothing to point at, I'll draw the path below and mark it assumed on the source line.
  - The three clients call the API gateway.
  - The API gateway routes to sync-service.
  - sync-service reads and writes the blocks database and file storage.
  - sync-service produces to the change stream.
  - The push worker consumes from the change stream and calls Apple's push service.
- Why: it is the shortest path through the allowed edges that uses your whole list, and you can correct it in the playback before anything is written.