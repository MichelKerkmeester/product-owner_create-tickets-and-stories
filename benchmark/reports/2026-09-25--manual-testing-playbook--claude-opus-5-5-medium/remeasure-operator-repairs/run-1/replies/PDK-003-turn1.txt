```markdown
I'll write a new document on where sync conflicts and lost edits stand. I've read both files. They agree with each other: protocol v3 is block-level last-writer-wins, the overwritten edit is not kept anywhere and nothing is decided until Joana decides on 2026-10-09. Before I start, I need the answers below in one reply:

**Purpose & audience:** Who is this for, and what should they do after reading it? For example, Joana and the Sync team preparing for the 2026-10-09 decision, Support needing a clear account for members, or leadership wanting a status update. The answer changes how much protocol detail goes in, such as base versions, the new message type and what each option needs from each client.

**Status per claim:** Here is how I plan to label things. Please correct anything that's wrong:
- Current behavior: v3 last-writer-wins, lost edits missing from page history, the 40 tickets in August against 22 in July, the 0.8% session rate and the 58% / 42% split
- Approved next step: Tomasz's two-week spike on Option B with Saskia's formatting fallback, plus a write-up of Option A as a first step, and v3 and the Support message staying as they are until 2026-10-09
- Proposal: Options A, B and C, with the effort estimates labelled as Tomasz's estimates and "33 of 40" labelled as Marta's estimate
- Should the document lean towards B because it has the most support, or stay neutral as Joana did?

**Sources not supplied:** The thread refers to the doc `Sync conflicts, options for v3 and after` and the design frame `Sync / Conflict copy`, but I don't have either. Can you share them? If not, I'll mention them by name only and describe the options just as the thread does. The spike hasn't produced results yet, so the document will say that it's still running and won't guess what it will find. Is that right?

**Scope:** Should any of these go in or stay out?
- Oskar's point that offline editing will raise the conflict rate and shouldn't ship on v3 as it is
- Saskia's concerns about mobile storage and rich text merges
- What Support tells members today
- Sizing Option C, which Joana has said nobody does now. I'll leave this out unless you say otherwise

**Shape:** Which of these fits best?
- A narrative overview: a status write-up in prose
- A proposal: the current state and the options side by side, with the open decision
- Or I can pick once you've confirmed the purpose

**Delivery:** Is this going into ClickUp as a document, or only into the export file?
```

Export-equivalent path: `export/001 - doc-sync-conflicts-status-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I haven't drafted anything yet. `$d` means I ask these questions first and wait for your answers. I didn't find any conflicts between the two files. The open questions are about who the document is for, how each claim should be labelled, the two sources that weren't supplied and what's in scope. Once you answer, I'll write the document and number it `002` in the doc series.