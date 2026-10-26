Here is the playback of the reading so far. I haven't modelled or drawn anything.

**Brief rows**
- **Reader:** engineers on the sync team and new joiners. Captured from your answer.
- **Question:** which parts carry a block change from a client to the push notification? Captured.
- **Outcome:** the reader can name the part to open for a sync or a push problem. Captured.
- **Scope:** the 10 parts you listed, with auth, retries, conflict handling and the Apple-to-iOS delivery left out. Captured.
- **Entry and exit:** the Desktop, Web and iOS clients start it. It ends at Apple's push service, and the change stream is the hand-off between the two boards. Captured.
- **Actors:** the nine kinds of part you named, each in its lane. The three clients are the client lane, the API gateway is the gateway lane, sync-service and the push worker are services, the blocks database and file storage are stores, the change stream is the event lane and Apple's push service is the outside system. Captured.
- **Decisions and states:** none, because an architecture has no branches.
- **Sources and class:** your message only. Every call between the parts is **assumed**, class unknown, until a doc or repo path confirms it.

**Assumed**
1. The calls and their direction are the path you accepted. The clients call the gateway, the gateway routes to sync-service, and sync-service reads and writes the blocks database and file storage. sync-service produces to the change stream, and the push worker consumes it and calls Apple's push service. A doc or repo path would settle this.
2. The edge labels are my wording, from the source side: "Sends sync requests" from each client, "Routes sync requests", "Reads and writes blocks", "Stores and fetches files", "Produces block changes", "Consumes block changes" and "Apple Push: Sends notifications".

**Outline, in drawing order**
Board 1, "1. Block sync", has 8 nodes and 7 connectors, ending on the change stream as the hand-off:
- The first line is the board's question: how does a block change travel from the clients to the change stream?
- Desktop, Web and iOS clients each send sync requests to the API gateway, which is 3 connectors.
- The API gateway routes sync requests to sync-service.
- sync-service reads and writes the blocks database, stores and fetches files in file storage, and produces block changes to the change stream.

Board 2, "2. Push delivery", has 5 nodes and 4 connectors:
- The first line is the board's question: how does a block change become a push notification?
- The API gateway routes sync requests to sync-service.
- sync-service produces block changes to the change stream.
- The push worker consumes block changes from the change stream.
- The push worker calls Apple's push service ("Apple Push: Sends notifications").

**Two framings**
1. Two boards by path (recommended). Each board stays within the 9-node, 12-connector budget and keeps all three clients as separate nodes. The cost is that board 2 repeats the gateway and sync-service. The check requires a way in for sync-service, and a bare 3-node chain would read as a list.
2. One board with the three clients merged into one node. It has 8 nodes and 7 connectors and fits the budget. The cost is that Desktop, Web and iOS are no longer separate parts, which is what you listed.

**The look, all proposed**
- First glance: sync-service on board 1 and the push worker on board 2.
- Detail and audience: Balanced for engineers, with exact part names. Reading distance is Laptop.
- Zones: none, because the lanes already group the parts.
- Subtitle: it says the calls come from the team's description and not from a doc, so the assumed edges are visible without cluttering every label.
- Source line: "Sources: the team's description of Loomlist block sync, calls assumed. Left out: auth, retries, conflict handling, delivery from Apple's push service to the iOS device."

Does this reading hold, with two boards as in framing 1?