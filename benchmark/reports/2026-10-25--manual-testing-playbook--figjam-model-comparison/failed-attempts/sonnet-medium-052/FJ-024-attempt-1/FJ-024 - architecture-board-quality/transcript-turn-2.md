# FJ-024 turn 2 transcript

**User:** Use your recommended answers.

**Assistant:**

Here is the full reading before I model anything. Your recommended answers stand, and each is marked assumed.

**The reading**
- **Question the board answers:** how does a block change reach every device, and how does a sleeping iPhone get woken?
- **Outcome:** the reader knows which part to look at when a change doesn't arrive.
- **Reader:** engineers new to the sync path (assumed, no source names them).
- **Dials:** Balanced detail, Engineer audience, Laptop distance (all assumed).
- **Source class:** the platform doc facts as you quoted them, taken as current behavior (assumed, I haven't seen the doc).

**Outline, in drawing order**
- Desktop, web and iOS clients each hold a live two-way socket to the API gateway
- The gateway carries the body "Checks the session token" and "Keeps each client socket open"
- The gateway routes requests to sync-service (inferred, medium confidence, named as assumed on the source line)
- Sync-service carries "Merges edits to the same block" and writes to the blocks database
- The blocks database carries "Keeps 30 days of block history"
- Sync-service publishes every change to the change stream, dashed
- The change stream carries "Keeps events for 7 days"
- The push worker reads the stream, dashed, and carries "At most 1 wake-up per device per minute"
- The push worker calls Apple's push service, dashed, labelled "Apple Push: Wake sleeping iOS devices"

That is 9 parts and 8 connections. Every part earns its place, so the remove test cuts nothing.

**Two framings**
- **All three clients drawn (recommended):** it keeps iOS visibly apart from desktop and web, which is the client the wake-up path serves. It costs two near-identical boxes.
- **One "Clients" box:** it is tighter, but the reader loses which client the push worker exists for.

**The look**
- **First glance:** the change stream, because the write path and the wake path meet there. Focus reason: both paths meet here (assumed).
- **Title:** Block sync services
- **Subtitle:** How a block change reaches the change stream and wakes sleeping iOS devices, for engineers new to the sync path
- **Source line:** Sources: Loomlist platform doc as quoted in the request. The gateway to sync-service route is assumed.
- **Zones:** none. An architecture draws its lanes as zones already.

**What the board leaves out**
- File storage, because no source states which part uses it
- Apple's push service waking the iOS device, because an architecture has no edge from an outside system to a client. The push worker's edge label carries it instead

Is this reading right, or should I correct anything before I model it?
