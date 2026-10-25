Before I draw anything, this is how I read the request. Nothing is written yet.

- Question: which parts take part in block sync and how do they connect?
- Reader: engineers and product people on the Sync team
- Outcome: they can see which part carries a block change from one client to the others
- Settled by you: the nine parts drawn are the Desktop, Web and iOS clients, the API gateway, sync-service, the push worker, the blocks database, the change stream and Apple's push service
- Settled by the lane rules: each client calls the gateway, and the gateway routes to sync-service. sync-service writes to the blocks database and publishes to the change stream. The push worker consumes the stream and calls Apple's push service to wake iOS devices.
- Left out: file storage. It is the tenth part, one over the architecture budget of nine, and no call in the wiring touches it.
- Left out: `pages-service`. The context page says it owns block data, but you did not name it, so I won't draw it.
- Assumed, wiring: no Loomlist source states these calls, so the source line on the board will say they come from the lane rules. A sync doc or your correction settles it.
- Assumed, file storage: I took the cut branch without confirmation that sync never touches file storage. If it does, I'd split into two boards instead of cutting.
- Assumed, dials: balanced detail, a mixed audience (`sync-service` reads `Sync Service`) and laptop reading distance.
- Still open: none

Is this the right reading of the board?