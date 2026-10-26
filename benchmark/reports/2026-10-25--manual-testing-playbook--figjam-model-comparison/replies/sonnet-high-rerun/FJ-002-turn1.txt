I haven't written anything to the board yet. "How block sync works" fits two diagram types that answer different questions, so I need your pick first.

**Reading:** I found Loomlist sources in `context/`. They are `loomlist-context.md` (the "Edit on two devices" flow, the sync session and conflict definitions, the known constraints) and the `#sync-eng` lost-edit thread. Together they say:
- Each device uploads changed blocks in a sync session and pulls newer ones.
- When two devices change the same block between sessions, sync-service keeps the version that reaches it last.
- The replaced edit is not kept anywhere, including page history.
- The thread's Options A, B and C are proposals. The thread is pinned "not decided", and I found no recorded decision after the 2026-10-09 date.

**Question:** Which question should the board answer?
- **Sequence:** in what order do a device and sync-service exchange messages, and what happens when two devices edit the same block?
- **Architecture:** which parts make up sync (the four client surfaces, sync-service, pages-service) and how do they connect?

**Recommended:** Sequence, with Device A, Device B and sync-service as the parties.

**Why:** the sources describe an ordered exchange and a conflict outcome, and they give no connector detail for an architecture. The sources name no message names or status codes, so I'd mark those as a gap rather than invent them. I'd draw v3 as current behavior only and leave the three options off the board.

When you answer, I'll follow with the reader and outcome round, then a playback and the write gate. The gate will name file `<draft-file-key>`, which gets the board as a new section beside what it already holds. You didn't mention an existing board section to replace, so none will be touched.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.