I haven't written anything to Figma yet. The request names the ten parts but no calls between them, and an architecture board needs those. No Loomlist source I can read names the gateway, change stream, push worker or file storage.

What I have so far:
- **Type:** architecture, because you asked which services sit behind block sync and how they connect
- **Parts:** the ten you listed
- **Target:** the existing file `<test-file-key>`, in the Loomlist Engineering plan as you named it. I read "new board" as a new framed board inside that file, so I won't create a file. The board lands to the right of what's already there.
- **Assumed defaults:** balanced detail, mixed audience and a laptop reading distance. Tell me if the board will be shown on a meeting screen or a wall.

I need three answers. Each has a recommendation, so a plain "yes" accepts it.

1. Who reads the board, and what should they do after reading it?
   - Reading: the request names the subject but not the reader or the decision
   - Recommended: the Sync team, to see which parts a block change passes through
   - Why: the Loomlist context page lists sync-service under the Sync team

2. Which part calls which? A link to the sync-service doc settles this. Otherwise, do you confirm this wiring?
   - Desktop, Web and iOS clients call the API Gateway
   - The API Gateway routes to Sync Service
   - Sync Service writes to the Blocks DB and publishes to the Change Stream
   - The Push Worker consumes the Change Stream and calls Apple Push to wake iOS devices
   - Why: it uses each part once on the shortest path, but it comes from the part names and not from a source. Anything you don't confirm goes on the board's source line as assumed. The edge labels stay plain verbs unless the doc gives protocols such as WebSocket or HTTPS.

3. What touches file storage, and should it share this board?
   - Reading: ten parts is one over the architecture budget of 9 nodes, and nothing says which part uses file storage
   - Recommended: if nothing on the sync path calls it, leave it off and list it under `Left out:`. If Sync Service reads or writes it, I draw two boards in the same file, the sync path and the file path.
   - Why: a node with no connector is wrong by the board's own rules, and splitting only helps when file storage has a path of its own

After your answers I'll send the full playback of the reading. The write gate is a separate message that names the plan, the file, the calls it will spend and the rollback, and I write only after a "yes" to that.