**Doc Mode** — the request routes as a clear natural-language Doc ("document how X works", audience: support team), so it proceeds to the Doc context gate. The engineering notes are promised but not yet supplied, and under the source-safety gate a promised source does not defer the one consolidated clarification: it asks for the notes together with every other unresolved field (their status, the needed technical depth, and the shape) in a single question, then waits.

**Deliverable Block** — `export/001 - doc-notification-retry-pipeline-clarification.md`:

```markdown
# Notification retry pipeline documentation - clarification

I'll document how the notification retry pipeline works for the support team. Before drafting, I need the unresolved decisions below in one response:

**Source notes:**
- Paste the engineering notes you mentioned

**Authority & status:**
- Do the notes describe current behavior, approved direction, a proposal, retired material, or a mix?
- Do the notes govern, or is there another controlling source for any behavior they cover?

**Depth & purpose:**
- What should support readers do after reading: predict pipeline outcomes, troubleshoot a stuck notification, or both?
- How much technical HOW do they need: retry timings, states and outcomes, internal mechanics, or operator-facing troubleshooting steps only?

**Scope & shape:**
- Anything that must be included or excluded?
- The wording suggests a behavior reference, but the notes may point to a troubleshooting guide or runbook instead. Confirm the shape, or ask me to infer it once the notes arrive

**Validation:**
- Which claims remain unverified, and what should I avoid presenting as fact?
```

**Export-equivalent path:** `export/001 - doc-notification-retry-pipeline-clarification.md`

**Quality:** clarity, completeness, assumption challenge, perspective diversity and mechanism depth all 8+; the question is consolidated, waits, and self-answers nothing — pass.

`HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.`

One consolidated question, waiting on your notes plus the four decisions above (status, technical depth, scope, shape). Once you answer, the document becomes the next deliverable in this lane as `export/002 - doc-notification-retry-pipeline.md` — no ClickUp connector is present, so there is nothing to offer there.