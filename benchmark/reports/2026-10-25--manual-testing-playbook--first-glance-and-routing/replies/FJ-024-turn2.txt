The model passed the pre-write check and composes. Here is the write gate. It covers the write only, and your yes to the reading doesn't cover it.

```text
Question: which parts carry a block change from one client to the others, and how does a sleeping iOS device get woken?
Outcome: Loomlist engineers can say which part to check when a block change does not reach a device.
First glance: sync-service, where every block change is written and published.
Second glance: the Change Stream that carries each change on to the Push Worker.
Last glance: Apple Push Service, the outside hop that wakes sleeping iOS devices.
File: the existing FigJam file <test-file-key>, with no new file created. It keeps the plan it was made in. You named that plan as Loomlist Engineering, and I have not verified it.
Writes: one composed board titled "Block sync" with 9 nodes and 8 connectors in 6 lanes, plus a subtitle, a key and a source line, at the laptop reading distance. It lands 400 pixels to the right of everything already on the page, so nothing existing is covered.
Left out, named on the board's source line: file storage (no connection stated) and the Apple push to iOS device wake-up (the architecture type has no edge from an outside system to a client).
Assumed, from your reading: the gateway routes to sync-service, and block writes land in the blocks database.
Extensions: none.
Calls: create_session, one use_figma (after loading Figma's figma-use and figma-use-figjam skills) and one get_figjam read-back. No whoami and no create_new_file.
Limit: if the file's plan is Starter, or you hold a View or Collab seat, Figma allows six tool calls a month and read tools count against that. If the read-back is refused, the reply says "Read-back: not possible" and I won't call the board done.
Rollback: delete the one board section the write returns. That deletion goes through use_figma and waits for its own yes.
Write it?
```