### Playback — Loomlist block sync

**Reader and outcome:** Loomlist Engineering should be able to trace a block change through the sync services and follow the change stream to the iOS wake path.

**Target:** Add two framed diagrams to the existing FigJam file in the Loomlist Engineering plan (`<test-file-key>`). The file already contains board content, so these diagrams will be added alongside it.

**Scope:** The request names 10 components, above the 9-node architecture limit. I’ll split them into two diagrams in the same file:

- **Block sync:** Desktop, web, and iOS clients; API gateway; sync-service; blocks database; file storage; change stream
- **iOS push wake:** Change stream; push worker; Apple Push Service

The change stream appears in both diagrams to connect the paths. The request states that clients hold live sockets to the gateway, sync-service writes each block change and publishes it to the change stream, and the push worker reads the stream and wakes sleeping iOS devices. You accepted the recommended gateway-to-sync-service route and push-worker-to-Apple-Push connection.

**Assumption:** The request does not specify how file storage connects. I’ll show sync-service reading and writing file storage, labeled as assumed. Protocols, retries, and failure behavior are outside the requested scope.

Does this reading match, including the file-storage assumption? This confirms the interpretation only; it does not authorize the board write.