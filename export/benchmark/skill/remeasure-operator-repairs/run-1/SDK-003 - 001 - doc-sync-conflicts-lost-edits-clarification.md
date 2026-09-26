# Sync conflicts and lost edits, questions before drafting

I'll write a new document from `context/loomlist-sync-conflict-thread.md`, with `context/loomlist-context.md` as the company background. The two files agree on how protocol v3 handles conflicts, so I have no source conflict to settle. Before drafting, I need the decisions below in one reply:

**Purpose and audience:** Who reads this and what should it help them do? For example, Joana preparing the 2026-10-09 decision, the Sync and Mobile engineers running the spike, Support explaining lost edits to members or leadership wanting a status read.

**Shape:** Should it be a status write-up in prose that tells where things stand, or a decision brief that lays Options A, B and C side by side for Joana? The word "where we are" points to the status write-up, but I'd like you to confirm.

**Status and recommendation:** I plan to label v3 last-writer-wins as current behavior and all three options as proposals, with the decision still open and Joana as the owner. Should the document stay neutral, or should it record the lean toward Option B that Tomasz, Selin and Marta stated in the thread? Either way I won't present it as a decision.

**Source set and recency:** Can I use only the two files above? The thread export stops on 2026-09-22. Has anything changed since then, such as the spike on Option B starting, early results or new ticket counts for September? If so, please share them or tell me to leave them out.

**Scope:** Which of these belong in the document?

*   The current Support line to members and the fact that a lost edit can't be restored from page history
*   The ticket and session numbers, including Marta's estimate that 33 of the 40 August tickets would have kept both texts under Option B, which is her own read rather than a measured figure
*   The mobile storage and rich text risks Saskia raised, and her formatting fallback
*   Oskar's condition that offline editing does not ship on top of v3 as it is today
*   The spike plan and the open questions it has to answer before 2026-10-09

**Technical depth:** Should it explain the protocol mechanics, such as the base version clients would need to keep for Option B and the protocol v4 migration for Option C, or keep to product-level outcomes?
