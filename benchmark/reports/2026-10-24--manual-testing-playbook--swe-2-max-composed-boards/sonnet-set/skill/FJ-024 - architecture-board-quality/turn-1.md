Nothing is written yet. I checked the model and composed it as an architecture board, and it needs two corrections from you and one yes before it goes into the file.

**What I read from your request**
- **Type:** architecture, because you asked which services make up block sync and how they connect.
- **Reader:** Loomlist Engineering. I assumed this, so labels use your exact names, such as `sync-service`.
- **Distance:** laptop. I assumed this too.
- **Source:** your message only. I read it as current behavior.

**Two things I changed or need confirmed**
1. **File storage is left out.** You named it as a part but gave it no connection. An architecture draws no part without a connector, and I won't invent one. Tell me which service reads or writes it and I'll add it. The board would then have 10 nodes, one over the 9-node budget, so I'd split it into two boards. My recommendation is to leave it out for now. The source line on the board says so.
2. **Gateway to sync-service is assumed.** You said clients hold a live socket to the gateway and that sync-service writes block changes, but you didn't say the gateway routes to sync-service. The edge is labelled "Routes sync traffic". Sync-service needs a way in, so I drew it. Correct me if traffic reaches it another way.

**What the board will hold**
- Three clients: desktop, web and iOS. Each has a two-way live socket to the API gateway.
- The gateway routes to sync-service.
- Sync-service writes to the blocks database and publishes to the change stream.
- The push worker consumes the change stream and calls Apple's push service to wake iOS devices.

That is 9 nodes, 8 connectors and 6 lanes. `flow_check.py` passed and the composer produced the code.

The hop from Apple's push service to the iOS app is not drawn, because an architecture has no edge from an outside system back to a client. The edge label "Wakes iOS device" carries it.

**Glance lines**
- First glance: sync-service writing a block and publishing it to the change stream.
- Second glance: the push worker waking iOS devices through Apple.
- Last glance: the source line naming file storage as left out.

There is no accent colour, because the lanes set every colour.

**Write gate**
- **Plan:** Loomlist Engineering, as you said. I can't confirm from here that the file belongs to that plan.
- **File:** the existing FigJam file `<test-file-key>`, with no new file created. The new board section lands 400 pixels to the right of what is already on the page. Nothing existing is touched.
- **Writes:** one composed board with a title, a subtitle, a key and a source line.
- **Calls:** `create_session`, one `use_figma` call and one `get_figjam` read-back. A Starter plan or a View or Collab seat is limited to six tool calls a month, and these three count against that.
- **Rollback:** delete the one board section the write returns. I'll only do that after you say yes to the deletion. Your existing content stays as it is.

Reply "yes" to write the board as described, or send corrections first, such as the file storage connection or a different route into sync-service.