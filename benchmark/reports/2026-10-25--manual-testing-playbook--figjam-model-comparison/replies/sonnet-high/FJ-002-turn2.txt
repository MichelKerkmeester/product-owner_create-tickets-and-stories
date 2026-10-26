Nothing is written. This is the full playback, and it waits for one answer. The model, the check and the write gate come after it. I took your "use the recommended answers" as the answer to round one, so those rows below are settled.

**The Brief**

| Row | Value | Status |
|---|---|---|
| Reader | Support agents and product managers | captured, your recommended answer |
| Question | Which version of a block survives when two devices edit it, and why can't we restore the other? | captured |
| Outcome | The reader can explain a lost edit to a member | captured |
| Scope | Protocol v3 as it runs today, one conflict walked end to end | captured |
| Entry | A member edits one block on the Phone | captured, from the thread |
| Exit | The Phone pulls and receives the Laptop's version | assumed, see below |
| Actors | Phone, Laptop, SyncService | captured, from the context page |
| Messages | Upload changed blocks, keep the version that arrived last, pull newer blocks | captured in kind, assumed in order |
| Sources | `loomlist-context.md` (current behavior) and `loomlist-sync-conflict-thread.md` (current behavior for v3, proposal for options A, B and C) | captured |

**Assumed, and what settles each**
- The Laptop's upload reaches SyncService after the Phone's, and the Phone pulls afterwards. The sources say the last arrival wins, not who arrives last. I took the order from the thread's story, where the phone edit is the one that disappears. Tomasz or Joana would settle it.
- The Phone's pull comes in a later session and returns the Laptop's version. That follows from "pulls newer ones", but no source states the order.

**Outline**
- `userIntent`: which version of a block survives when two devices edit it
- Three participants, in this order: Phone, Laptop, SyncService
- Five messages:
  1. Phone to SyncService: Upload edited block
  2. Laptop to SyncService: Upload edited block
  3. SyncService to itself: Keep the version that arrived last
  4. Phone to SyncService: Pull newer blocks
  5. SyncService to Phone: Laptop version
- This is inside the sequence budget of 5 participants and 12 messages. The remove test cut two "block saved" replies, because no source states them.

**Two framings**
- One conflict walked end to end (recommended). It matches the thread's story, so Support can follow it with a member's ticket. The cost is that one scenario can read as the only case, so the subtitle states the condition: the same block, changed between two sync sessions.
- The general session loop of upload then pull, with the rule as a note. It covers every case but never shows a version being lost, which is the reader's question.

**The look**
- First glance: message 3, where the Phone's version is replaced. It is named with a `%% focus: 3` line.
- Detail and audience: Balanced and Mixed, plain verbs and no endpoint names, because none are in the sources. Reading distance: Laptop.
- Zones: none, because a sequence takes none.
- Title: "Two devices edit one block".
- Subtitle: "The version that reaches sync-service last is kept, and the replaced edit is stored nowhere, page history included".
- Source line: the two context files, with the `Left out:` items below.
- The four critique questions the gate answers about the sketch:
  1. Does the eye land first on message 3?
  2. Can a Support agent say who loses without reading the subtitle?
  3. Does any label need a term from outside the sources?
  4. Is the Phone's pull clearly after the overwrite?

**Left out**
- Options A, B and C, which are proposals with no decision recorded
- Offline mode, which is a separate epic
- Joana's 2026-10-09 decision, because no outcome is in the sources
- pages-service and the device cursor, because the sources don't state how either takes part
- The 0.8% overwrite rate, because it is a measure and not a step

Is this reading right? I recommend yes, because every row traces to a source or is named as assumed above. If it is, I'll write the model, run the check and bring you the write gate.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.