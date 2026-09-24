**Deliverable Block — clarification (intake, Doc lane)**

```markdown
I'll document how the notification retry pipeline works for the support team. Before drafting, I need the unresolved decisions below in one response:

**Source set:** Paste the engineering notes here — they are the governing source, so the draft waits for them

**Status & authority:** Do the notes describe current production behavior, or a mix (current, approved-but-not-shipped, proposed, legacy)? If mixed, tell me which parts carry which status so nothing gets promoted into current fact

**Operation:** Is this a new support-facing document, or a refinement of an existing one? If a refinement, paste the existing document — I will preserve its structure, identifiers and status labels and change only what you name

**Scope & depth:** Should the document stick to what support needs to explain and troubleshoot the pipeline, or also cover internal implementation detail (code paths, queue/service names, config)? Anything to explicitly exclude?

**Validation:** Which claims in the notes are unverified, and what should I avoid presenting as fact?
```

**Export-equivalent path:** `export/001 - doc-notification-retry-pipeline-clarification.md`

`HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none — intake wording, no HVR-qualifying prose to trim.`

**Quality:** clarification clarity, completeness and Doc safety gates — pass. One consolidated question, nothing self-answered.

**Assumption to correct if wrong:** I plan to draft this as a **behavior reference** — "how it works" reads as predict-the-outcome documentation, which fits a support audience that needs to explain retry behavior and know where it stops. If you'd rather have a troubleshooting guide (ordered steps) instead, say so in the same reply.

Route: Doc Mode, create operation, Standard energy. I'm waiting on the engineering notes plus the answers above — nothing gets drafted until they arrive.