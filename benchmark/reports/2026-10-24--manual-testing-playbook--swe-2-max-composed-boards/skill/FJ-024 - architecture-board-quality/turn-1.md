The file is confirmed FigJam and already holds several composed boards — a new board will land to the right of existing content. One note on the plan: `whoami` shows this account's plans are "<figma-plan-3>", "<figma-plan-1>" and "<figma-plan-2>" — none named "Loomlist Engineering". Since the file key targets an existing file, the new board lands in whatever plan already owns that file rather than a plan I pick.

Before I model anything, one playback of what the request settles, and the one row still open.

**Reading the request — architecture.** The reader's question is "which parts carry a Loomlist block change, and how do they connect?" Drawn for the Sync engineers, at Balanced detail, Mixed audience, Laptop distance.

What the description settles:

*   Parts: Desktop, Web and iOS clients, an API gateway, sync-service, a push worker, the blocks database, the change stream, Apple's push service — and file storage
*   Moves: every client holds a live socket to the gateway, the gateway hands sync traffic to sync-service, sync-service writes every block change and publishes it to the change stream, the push worker reads the stream and calls Apple's push service to wake a sleeping iOS device
*   Source: the description in your request, read as current behavior, and consistent with the Loomlist context page (sync-service owns sync sessions, push goes through the platform push services)

One open row:

*   Reading: file storage is named in the parts list, but no described call touches it — every write you describe lands on the blocks database
*   Question: does a service call file storage on the sync path, or does it stay off this board?
*   Recommended: leave it off the board, named in the reply's `Left out:` line
*   Why: every node needs a stated connector and an architecture board holds at most 9 nodes; the described path already fills 9. If something does call it, name the caller — that is 10 nodes, and the work splits into two boards by request path

Assumed unless you correct it: nothing on the sync path touches file storage, so the board draws the other 9 parts.