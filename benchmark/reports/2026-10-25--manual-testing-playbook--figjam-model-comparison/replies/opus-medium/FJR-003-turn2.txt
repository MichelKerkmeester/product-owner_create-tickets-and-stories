I'm taking the three recommended answers. Here's the full reading before I build anything from it.

**Brief**
- Reader: PMs and designers outside the Sync team, at Mixed detail, read on a laptop (accepted)
- Question: which services does a block edit pass through on protocol v3 today? (accepted)
- Outcome: the reader can say where a block edit goes and which service decides which version is kept
- Scope: current behavior only. Options A, B and C and the offline change queue stay off the board (accepted)
- Entry: a device starting a sync session
- Exit: the block saved through pages-service, with the device pulling back newer blocks
- Actors: Web and Desktop as one client node, because Desktop wraps the web client. iOS and Android as a second client node
- Decisions and states: none drawn. Last-writer-wins happens inside sync-service and isn't a separate part

**What each source settled**
- `loomlist-context.md`: sync-service owns sync sessions, device cursors and conflict handling, and every service reads block data through pages-service. This is current behavior
- `#sync-eng` thread: confirms v3 is block-level last-writer-wins. Options A, B and C are undecided until Joana decides on 2026-10-09
- Offline mode brief: describes a planned change, not current behavior, so nothing on the board comes from it

**Assumed (2, each shown as assumed on the board)**
- Entry point: no source names a gateway, but the architecture type needs one between the clients and sync-service. The Sync team (Joana) can confirm or name it
- Block storage: pages-service needs a store behind it for the board to pass its check, and no source names one. I'd draw it as "Block storage (not named in sources)". Hugo's Pages and Databases team can name it

**Will be listed as left out**
- Options A, B and C, not decided until 2026-10-09
- The offline change queue, which is still a proposal
- Where sync-service keeps device cursors, which no source says

Does this reading hold, including the two assumed parts, or do you want to correct anything?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.