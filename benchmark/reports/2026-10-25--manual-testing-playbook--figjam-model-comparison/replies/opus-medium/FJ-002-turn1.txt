I've read the Loomlist sources and I'm stopping for the first intake round. Nothing has been written to Figma yet. Flow Mode confirms what the board should show before it drafts the diagram, and it asks your approval again before writing to the board.

**What the sources already establish**
- **Sources:**
  - `context/loomlist-context.md`: describes how sync works today.
  - `context/loomlist-sync-conflict-thread.md`: the #sync-eng thread. Tomasz's description of protocol v3 is current behavior. Options A, B and C are proposals, with no decision until Joana decides on 2026-10-09.
  - `context/loomlist-offline-mode-brief.md`: a proposal for future offline mode.
- **How a sync session works:** a device uploads its changed blocks to sync-service and pulls newer ones.
- **What happens in a conflict:** protocol v3 uses block-level last-writer-wins. When two devices change the same block between their sync sessions, the version that reaches sync-service last is kept. The other version isn't stored anywhere, so page history never has it.
- **Offline edits today:** an edit made without a connection is retried until the app closes, then lost.
- **Scale:** 0.8% of sync sessions that upload edits overwrite a block another device changed, per Yara's figure for the last 30 days.

**Round one**

1. **Who reads the board, and what do they decide?**
   - Reading: the thread began with 40 `lost-edit` tickets, and the offline brief is waiting on the conflict decision.
   - Recommended: Support, Mobile and the offline-mode teams. The question the board answers is "what happens to an edit when two devices change the same block?" Readers will use it ahead of the 2026-10-09 decision.
   - Why: the readers named in the sources are the ones asking this question.

2. **Which diagram type?** Two types fit.
   - A sequence diagram shows the order of messages: Device A, Device B, sync-service and page history, ending with the second upload replacing the first.
   - A process diagram shows the steps and who acts at each one.
   - Recommended: sequence.
   - Why: a lost edit comes from message order, and a sequence diagram shows exactly where the first version disappears.

3. **What must the board leave out?**
   - Reading: Options A, B and C haven't been decided, and offline mode is only proposed.
   - Recommended: draw v3 as it works today, including offline retry until the app closes. Leave Options A to C and offline mode off the board, and list them under `Left out:` with the reason "not decided until 2026-10-09".
   - Why: drawing a proposal as a step would make it look like current behavior.

**About the target file:** I've noted `<test-file-key>` and your fallback of a draft in the Barter team plan with no project. Before writing, I'll check that this key is a FigJam file and confirm that the new board will sit beside what's already there without touching it. I'll ask you about the write separately, once the diagram is agreed.

If you don't answer a question, I'll go with the recommended answer and mark it as assumed.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.