`export/002 - doc-notification-retry-requeue-guide.md`

Verified: read-back succeeded; 46 lines

HVR self-scan: 0 hard blockers. Fixed: Oxford comma in the step 2 outcome list, always-cut "just" in "the cycle you just diagnosed". Kept with reason: em dashes in the definition-delimiter bullets and the `Status: Current behavior —` label (granted ClickUp exemptions), "Requeue" capitalized as the literal action identifier.

Quality summary:

- Source safety: pass — every claim traces to the notes; the two things the notes do not state (requeue limit, failures outside the cycle) are labelled unknown rather than invented
- Shape fit: pass — Guide, since support follows an ordered procedure; diagnosis is step 1, requeue is step 2
- ClickUp layout: pass — `* * *` dividers after every content heading, `*   ` bullets, sentence-case headings, no spacer headings in the file export
- Readability: pass — takeaway-first paragraphs, one idea each, checklist short with rationale in prose
- Voice: pass

The guide gives support agents the retry cycle first (30 second backoff, five attempts, attempt six into the failed queue), then the diagnosis rule (failed-queue placement means retry exhaustion, so wait rather than requeue anything still mid-cycle) and the requeue consequence (the backoff restarts and the same rules apply). The one genuine gap in the notes, how many times a notification can be requeued, is kept visible as a boundary. If you want, I can extend it with notes on the failed queue's other fields or a troubleshooting section when you have more source material.