Before I draw anything, this is how I read the request. I haven't made a model or written to the board.

**Question:** which parts carry a block change from one client to the others, and how does a sleeping iOS device get woken?
**Outcome:** an engineer can see every part a block change passes through and where the iOS wake-up branches off.
**Type:** architecture, because you asked for the parts and how they connect. A sequence would answer the order of one sync, which you didn't ask for.

**Settled by your request** (current behavior, as you described it)
- The desktop, web and iOS clients each hold a live socket to the API gateway
- sync-service writes every block change to the blocks database
- sync-service publishes every block change to the change stream
- The push worker reads the change stream and wakes sleeping iOS devices

**Assumed** (correct any of these)
- **Reader:** engineers on the Loomlist Engineering team, read from the plan you named. A different reader changes the labels and not the parts
- **Gateway to sync-service:** the API gateway routes to sync-service. You didn't state this call. I read it from the sockets ending at the gateway and sync-service receiving the changes
- **Push worker to Apple's push service:** the push worker calls Apple's push service to do the waking, drawn as one call out
- **Dials:** balanced detail, an engineer audience that keeps names as you wrote them (such as `sync-service`) and a laptop reading distance

**Left out**
- **File storage:** you listed it but named no call to or from it. The architecture check rejects a part with no connection, so drawing it would mean inventing a call. With it the board has 10 parts, one over the budget of 9
- **Apple's push service to the iOS device:** the architecture lanes have no edge from an outside system back to a client, so the board ends at Apple's push service

**Still open:** which parts, if any, call file storage. I recommend leaving it off and naming it under `Left out:`, because no call is stated. If something does call it, tell me which part. I'd then offer an overview board and a detail board together rather than shrink one.

Is this the right reading of the board, with file storage left off?