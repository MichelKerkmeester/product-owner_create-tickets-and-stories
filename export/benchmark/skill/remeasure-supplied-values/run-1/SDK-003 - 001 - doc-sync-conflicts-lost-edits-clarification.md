# Sync conflicts and lost edits: questions before drafting

I'll write a new document on where the sync conflict and lost edit work stands. Before drafting, I need the decisions below in one reply.

**Purpose and audience:** Who reads this and what should they do after reading it? For example, Joana using it to prepare the 2026-10-09 decision, Support and Product leads getting a status update, or engineers on Sync and Mobile Platform who need the option details. The answer sets how much protocol detail goes in, such as how block-level last-writer-wins drops an edit and why Option B needs clients to keep a base version.

**Source set:** I have `context/loomlist-sync-conflict-thread.md` and `context/loomlist-context.md`. The thread cites Tomasz's doc `Sync conflicts, options for v3 and after`, which I don't have. Should I work from the thread's summary of the three options, or can you share that doc?

**Authority:** I found no contradictions between the two files. Both say v3 keeps the version that reaches sync-service last, and that the losing edit never reaches page history. Can the thread govern the options, numbers and next steps, with the context page governing product facts such as surfaces, plans and page history windows?

**Status:** My plan is to present v3 behavior as current and Options A, B and C as proposals under review, with Joana as decision owner and 2026-10-09 as the decision date. Tomasz's estimates (about 3 weeks, 6 to 8 weeks, two quarters) and Marta's view that 33 of the 40 August tickets would have kept both texts would be attributed to them as estimates. The spike on Option B has no results yet. Should the document stay neutral on the options, or carry a recommendation labelled as proposal? The thread leans B with Saskia's formatting fallback, but nothing is decided.

**Shape:** A narrative status overview (situation, evidence, options, open questions, next steps) or a decision brief that compares A, B and C side by side for Joana? Name one, or tell me to pick from the purpose.

**Scope:** Which of these belong in the document?
- Support guidance until the decision (edits made on two devices at the same time can overwrite each other)
- Offline editing as a dependency, given Oskar's point that it will push the 0.8% up and should not ship on v3 as it is
- Option C in full, or only as the long-term option nobody is sizing now
- The open questions the spike should answer: mobile storage cost of base versions and how often the merge falls back to a conflict copy
