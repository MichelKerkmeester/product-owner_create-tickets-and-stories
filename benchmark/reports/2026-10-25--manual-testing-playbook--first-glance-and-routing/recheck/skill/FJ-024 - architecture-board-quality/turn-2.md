The model passes the check and composes. Nothing is written yet.

**Question:** which parts take part in block sync and how do they connect?
**Outcome:** engineers and product colleagues in Loomlist Engineering can see which parts carry a block change from a client to the others and to a sleeping iOS device.
**First glance:** sync-service, where every block change is written and published.
**Second glance:** the Change Stream that carries each change on to the Push Worker.
**Last glance:** Apple Push Service, the outside hop that wakes sleeping iOS devices.

**Plan and file:** Loomlist Engineering, existing FigJam file `<test-file-key>`. No new file is created.
**Writes:** one new board section titled "Loomlist block sync", with 9 nodes and 8 connectors in 6 lanes, a subtitle, a key and a source line, at Laptop reading distance. Everything already in the file stays untouched. The board lands 400 pixels to the right of the existing content.
**Left out:** file storage, because no call to or from it was given. The source line says so. The Apple Push Service to iOS device hop isn't drawn either, because the architecture lanes have no edge from an outside system back to a client.
**Extensions:** none.
**Calls:** one `create_session`, one `use_figma` to compose the board and one `get_figjam` read-back. If the file's plan is on Starter or you have a View or Collab seat, that uses 3 of the 6 monthly tool calls.
**Rollback:** delete the one board section the write returns, through `use_figma`. That needs its own yes first, so a separate call and a separate question.

Write it?