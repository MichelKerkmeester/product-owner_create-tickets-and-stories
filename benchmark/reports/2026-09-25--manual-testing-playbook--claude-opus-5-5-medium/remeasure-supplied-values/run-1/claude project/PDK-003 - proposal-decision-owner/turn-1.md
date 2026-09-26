```markdown
I'll write up where sync conflicts and lost edits stand, using the #sync-eng thread export and the Loomlist context page. Before drafting, I need the unresolved decisions below in one response:

**Purpose & audience:** Who reads this, and what should they do after reading it? Each of these readers needs a different document:
*   Joana, preparing the 2026-10-09 decision (trade-offs between the options)
*   Support agents answering `lost-edit` tickets (what to tell members now)
*   Oskar, planning offline editing (what has to be true before it ships)
*   Leadership, who want a short status

**Technical detail:** How much protocol detail should it carry? The thread covers block-level last-writer-wins in v3, the per-field split in Option A, the stored base version and conflict copy in Option B and the protocol v4 migration in Option C. I can keep all of that or reduce it to what each option means for members.

**Source set:** Should I use only these two files? The thread cites two items that weren't supplied:
*   Tomasz's doc `Sync conflicts, options for v3 and after`
*   Selin's frame `Sync / Conflict copy`

Can you share them? If not, I'll describe the options only as the thread states them and list both by name, without links.

**Authority & figures:** Please confirm how I should handle these:
*   Yara's 0.8% is a share of sync sessions, and Marta's 40 tickets is a support count. They measure different things, so I'll report them separately and won't combine them into one rate
*   Tomasz says Option A fixes "the to-do half", and Yara measured 58%. Her 58% counts sessions that changed only a checkbox, due date or assignee. Option A's field list also includes reminder. I'll use Yara's figure as the measured one and present Tomasz's words as his reading
*   Marta's "33 of the 40" is her own read of the August tickets. Tomasz's 3 weeks, 6 to 8 weeks and two quarters are his estimates. Option C is deliberately unsized. I'll label all of these as estimates

**Document status:** My plan is to present v3 as current behavior and Options A, B and C as proposals, with no approved direction and a decision due 2026-10-09. Has anything changed since the thread was exported on 2026-09-22? For example, has Tomasz's two-week spike on Option B started or produced results?

**Scope:** What should "lost edits" cover?
*   Only edits lost to conflicts, as in the thread
*   Also the second loss path from the context page, which the thread doesn't mention: an edit made without a connection is retried until the app closes and is then lost

Should these also be in or out: the Support wording to use until the decision, the dependency on offline editing, and Saskia's rule that any block with formatting goes straight to a conflict copy under Option B?

**Shape:** Pick one, or ask me to choose once the purpose is settled:
*   Narrative overview: a project status in prose
*   Proposal: the options side by side with trade-offs
*   Guide: for Support, if the document is mainly about what to tell members

**Validation:** Is anything in the thread already out of date or disputed that I shouldn't present as fact?
```

Export-equivalent path: `export/001 - doc-sync-conflicts-lost-edits-status-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the bold question labels, because they are the Doc intake template's own format.

Quality: not scored, because this is only the intake question.

I've read both files, but I haven't written the document yet. `$d` asks one question before drafting, and some of the answers change what the document is.

The biggest open question is who reads it: Joana's decision, Support's replies to members and Oskar's offline plan each need something different. There are also two gaps you should know about:
*   **Missing sources:** the thread cites Tomasz's options doc and Selin's design frame, but I don't have either.
*   **Lost edits outside conflicts:** the context page describes a second way edits get lost, when an edit made offline is dropped once the app closes. The thread never mentions it.

Once you answer, I'll write the document.