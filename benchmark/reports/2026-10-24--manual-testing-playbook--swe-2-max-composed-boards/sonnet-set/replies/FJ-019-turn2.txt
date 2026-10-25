The model passes the pre-write check and composes, but no board is written yet. The write needs your yes.

**Playback of the reading**
- **Question:** which parts carry a block change from one Loomlist client to the others.
- **Reader:** Sync and Mobile engineers. This is assumed.
- **Outcome:** the reader can see which part sits between a client edit and the other devices.
- **Calls, assumed because no source states them:**
  - Each client calls the API gateway.
  - The gateway routes to sync-service.
  - sync-service writes the blocks database directly, not through pages-service.
  - sync-service publishes to the change stream.
  - The push worker consumes the stream and calls Apple's push service to wake the device.
- **Detail:** balanced, for engineers, so labels keep exact names such as `sync-service`.
- **Reading distance:** laptop.
- **Check:** 9 nodes, 8 connectors, 6 lanes defined, 0 crossings.

**Left out**
- File storage, because no source names a part that calls it.
- Conflict handling and offline behavior, because they are undecided until 2026-10-09.
- pages-service and notifications-service, because neither is on your list.

**Glance lines**
- **First glance:** sync-service.
- **Second glance:** the change stream path to Apple's push service.
- **Last glance:** the source line with the left-out items.

**Gate**
- **Plan and file:** Loomlist Engineering, existing FigJam file `<test-file-key>`. No new file is created.
- **Writes:** one board section titled "Block sync" with a subtitle, 9 nodes and 8 connectors in the lanes Clients, Edge, Services, Stores, External and Events, plus a key and a source line. It lands 400 pixels right of the existing content, so nothing there is covered.
- **Calls:** `create_session`, one `use_figma` and one `get_figjam` read-back. A Starter plan or a View or Collab seat has six tool calls a month, so this spends three of them.
- **Rollback:** delete that one section, only after you say yes to the deletion.

Write it?