Round one of three. Nothing gets drawn or written until you've seen the playback and said yes at the write gate.

What the sources settle so far:
- Product: Loomlist. I'm reading "block sync" as sync-service, which keeps every device on the same version of each block (`context/loomlist-context.md`)
- Type: architecture, because you asked which services sit behind it
- Parts the sources name: the Desktop, Web, iOS and Android clients, sync-service, and pages-service, which every service reads block data through
- Not in any source: a gateway, the stores behind either service, and any queue or outside system. The architecture check needs one gateway node, so it would be drawn as an assumed "Entry point"
- Proposed, not current: Options A, B and C from the #sync-eng thread (Joana decides on 2026-10-09) and the offline change queue in Oskar's brief

**1. Who the board is for**
Reading: the sources suggest two readers. One is the Sync team weighing the options. The other is Support or Product explaining lost edits.
Question: who is this board for?
Recommended: PMs and designers outside the Sync team, at Mixed detail, read on a laptop.
Why: they need component names and plain verbs, not protocol detail.

**2. What it answers and what it must not do**
Reading: no source says what the reader decides after reading the board.
Question: what should the board answer, and what must it leave out?
Recommended: "Which services does a block edit pass through on protocol v3 today?" It shows current behavior only. Options A, B and C stay off the board and are listed under Left out.
Why: the conflict decision is open until 2026-10-09, so drawing an option would present a proposal as current behavior.

**3. Target file**
Reading: you asked for file `<test-file-key>`. Flow Mode only writes into a new file or a board this work already wrote, and I haven't read that file.
Question: can I use a new FigJam file in the Barter team plan, left in drafts with no project?
Recommended: yes, the new file.
Why: it's the fallback you gave, and it keeps the write away from anything someone else put on the existing board. If you want the existing file anyway, say so and I'll read it with `get_figjam` first. That read counts toward the six calls a month a Starter plan or a View or Collab seat gets.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.