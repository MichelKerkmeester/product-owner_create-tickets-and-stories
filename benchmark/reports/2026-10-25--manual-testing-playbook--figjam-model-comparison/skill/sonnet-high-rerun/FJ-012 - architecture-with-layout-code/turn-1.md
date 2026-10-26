Architecture is the right type here. Your list is parts of a system, and the question it answers is which parts exist and how they connect. Nothing is written yet, and I've made no Figma calls.

**What I have so far**
- **Target:** the existing file `<test-file-key>`, as a new section beside what it holds. The write gate will confirm this after one read of the file.
- **Parts (10):** desktop client, web client, iOS client, API gateway, sync-service, push worker, blocks database, file storage, change stream, Apple's push service.
- **Source:** your message alone. It names the parts but states no calls between them.

**1. Reader, question and outcome**
- Reading: the request doesn't say who opens the board or what they decide from it.
- Recommended:
  - Reader: Loomlist engineers.
  - Question: which parts does a block change pass through between a client and a push notification?
  - Outcome: they can say which service owns each hop.
  - Left off the board: call order, retries and deployment detail.
- Why: an architecture board shows what connects to what, and call order belongs to a sequence diagram.

**2. Connections**
- Reading: no call is stated, so every connector below would be drawn as assumed.
  - Each client calls the API gateway.
  - The gateway routes to sync-service.
  - Sync-service reads and writes the blocks database and file storage.
  - Sync-service publishes to the change stream.
  - The push worker consumes the change stream and calls Apple's push service.
- Two limits come from this diagram type's fixed edge rules:
  - Only a service can feed the change stream, so the database can't be drawn as its source.
  - Apple's push service delivering to the iOS client can't be drawn, so I'd name it under `Left out:`.
- Question: is that shape right, and is there a doc, repo or service map that states the calls?
- Recommended: accept it as assumed. A source would turn the connectors into captured facts.

**3. Size**
- Reading: 10 parts is one over this type's budget of 9 nodes (the 9 connectors are within the limit of 12).
- Recommended: one board with file storage left out and named under `Left out:`. It sits beside the sync-to-push path rather than on it.
- The alternative is two boards by request path, block sync and push delivery, which keeps all 10 parts.

Do the three recommendations stand, or what changes?