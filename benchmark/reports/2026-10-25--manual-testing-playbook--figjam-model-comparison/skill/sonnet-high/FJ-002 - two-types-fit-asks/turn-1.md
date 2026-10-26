Nothing is written yet. This is intake round one for a board in the existing file `<draft-file-key>`. The board will go in as a new section beside what the file holds, and nothing already on it changes. That target needs no new file and no plan.

**Reading of the sources**
- Sources: `context/loomlist-context.md` and `context/loomlist-sync-conflict-thread.md`. Protocol v3 is current behavior. Options A, B and C in the thread are proposals, and the thread's own pinned status is "not decided".
- Settled: each device uploads changed blocks in a sync session and pulls newer ones. When two devices change the same block between sessions, sync-service keeps the version that reaches it last (block-level last-writer-wins). The replaced edit is stored nowhere, page history included.
- Open: the messages inside a session beyond "upload, then pull", what the device cursor does, and whether sync-service reads or writes blocks through pages-service.

**1. Reader, question and outcome**
- Reading: the thread opens with the Support lead asking what to tell members about lost edits. The context page says support agents can see sync status but not page content.
- Question: who reads the board, and what do they decide from it?
- Recommended: Support agents and product managers. The question is "which version of a block survives when two devices edit it, and why can't we restore the other?" The outcome is that they can explain a lost edit to a member.
- Why: it is the question the thread opens with, and the sources state it in full.

**2. Diagram type**
- Reading: two types fit. A sequence shows the order of the exchange between Phone, Laptop and sync-service. An architecture shows which parts exist and how they connect.
- Question: which one answers the reader's question?
- Recommended: a sequence with Phone, Laptop and sync-service as participants, showing both sessions and the overwrite.
- Why: "the last to arrive wins" is a question of order, and the sources say little about how the parts connect. The cost is that the messages inside a session beyond upload and pull become named gaps, not guesses.

**3. What the board must not do**
- Reading: the thread's decision date was 2026-10-09, which has passed, and no outcome is in the sources. The offline brief is a separate epic.
- Question: what must the board not do, and did Joana's decision land?
- Recommended: draw protocol v3 as it runs today. Leave options A, B and C and offline mode off the board, and name them on the `Left out:` line. If a decision landed, send the source and I will mark it approved direction instead of current behavior.
- Why: a proposal drawn as behavior would tell Support something untrue.

Answer each, correct a reading, or say "use the recommended answers". Next is the full playback, then the write gate.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.