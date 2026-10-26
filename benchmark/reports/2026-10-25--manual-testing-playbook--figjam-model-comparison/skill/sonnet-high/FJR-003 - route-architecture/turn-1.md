I haven't drawn anything yet. "Block sync" has no source in your request, and Flow Mode doesn't draw services from memory. The only "block sync" in this workspace is the fictional Loomlist worked example, and I won't treat that as Barter's system.

I've noted the target. The board will go into the existing file `<draft-file-key>` as a new section beside what it already holds. Nothing on the file will change, and I won't create a new file. Nothing is written until you answer a separate write-gate question.

**Round one (answer all three, or say "go with the recommendations")**

1. **Source**
   - Reading: the request names no doc, repo path, route list or ticket, and I can't see the Barter services from here.
   - Question: which source should I read for the services behind block sync?
   - Recommended: the sync service's engineering doc, or the code that lists its routes, handlers and consumers. Attach it or give me the path.
   - Why: an architecture needs every deployable part, who calls whom, and what sits outside the system. Without a source I'd have to invent services.

2. **Reader and question**
   - Reading: "the services behind block sync" reads as "which parts take part in sync and how do they connect?", which is an architecture.
   - Question: who reads this board, and what do they decide after seeing it?
   - Recommended: an engineer or PM who needs the parts and their calls. A sequence diagram would answer the order of one sync instead, so say so if that's what you want.
   - Why: the reader's question picks the diagram type, and the two types answer different questions.

3. **What the board must not do**
   - Reading: you gave no limit on scope.
   - Question: what should the board leave out?
   - Recommended: one sync path only, with no deployment detail, monitoring or logging, and no services that sync never touches.
   - Why: an architecture holds at most 9 nodes and 12 connectors. A bigger system splits by path instead of shrinking.

If you don't answer one of these, I'll proceed on its recommendation and mark it assumed in the playback. You can correct it there before anything is written.