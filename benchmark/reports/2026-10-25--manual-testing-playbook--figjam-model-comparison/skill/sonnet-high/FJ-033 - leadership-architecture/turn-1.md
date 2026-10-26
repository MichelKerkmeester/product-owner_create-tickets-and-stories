Before I draw anything, this is how I read the request.

**Question:** how does block sync work, in the parts a leadership reader needs to follow?
**Outcome:** leadership can see that the sync platform stores every change and that sleeping iPhones are woken through Apple's push service.
**Settled by the sources:** your description only. It names the desktop, web and iOS apps, the sync platform, the stored changes and Apple's push service. No engineering doc was supplied, so I treat it as current behavior.
**Type:** architecture, because the question is which parts connect. A sequence would answer the order of one sync, which you did not ask for.

**Outline, in drawing order**
1. Intent: show leadership how the apps reach the sync platform, where changes are kept and how sleeping iPhones are woken
2. Nodes: Desktop app, Web app, iOS app, Entry point, Sync platform, Change store, Apple push service
3. Edges: each app to Entry point (Sends changes), Entry point to Sync platform (Routes sync requests), Sync platform to Change store (Stores every change), Sync platform to Apple push service (Apple push service: Wakes sleeping iPhones)

That is 7 nodes and 6 connectors across 5 of the 6 lanes, inside the 9 and 12 budget. The Events lane stays empty because no source names a queue.

**Two framings**
- Parts and connections (recommended): it answers your question directly and needs nothing beyond what you told me
- One change's journey as a sequence: it shows the order, but it needs steps your description does not give

**Look**
- First glance: the Sync platform, marked with a focus line, because it is the one part every change passes through
- Title: "How block sync works"
- Subtitle: "How the desktop, web and iOS apps stay in step through the sync platform, for the leadership update"
- Source line: "Source: product team description of block sync. Left out: Apple's hop to the phone, any internal parts"
- Critique question for the sketch: does the eye land on the Sync platform first, and is that the node leadership most needs read?

**Assumed**
- Audience is leadership, so labels use capability names and no infrastructure products. A doc or your word settles it
- Entry point: the architecture layout needs a gateway between the apps and the service. I name it in capability words rather than invent a product, and mark it assumed on the source line. The engineering owner can confirm the real name or that none exists
- Change store: I read "stores every change" as one store, and its real database is not named
- The board must not name queues, workers or protocols that no source states
- Reading distance is Meeting screen, labels up to 32 characters, because a leadership update is usually shown on a call. Laptop stands if you say otherwise

**Left out:** Apple's hop from its push service to the phone has no allowed arrow in the architecture layout. The edge label "Wakes sleeping iPhones" carries it, and no arrow runs back to the iOS app.

**Target:** the file key you gave settles it. I confirm it at the write gate.

Is this the right reading of the board?