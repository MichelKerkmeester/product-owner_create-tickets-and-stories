```markdown
I'll create the payment webhook failure document. Before drafting, I need the unresolved decisions below in one response:

**Purpose and audience:** I read this as a new document. Which job should it do: an on-call runbook for webhook failures, a post-incident write-up of INC-0412, or a guide to handling webhook failures in general? Who reads it: Payments on-call, Guest Support, or both?

**Scope:** The notes cover one failure, a 401 signature mismatch after a secret rotation. Should the document cover only that case, or every payment webhook failure? If it covers every failure, the notes say nothing about timeouts, server errors, duplicate or missing events, or a provider outage. Name a source for each, or drop them from scope.

**Source set:** You said to start with the incident notes. Is more material coming? If so, please add the rotation write-up, the runbook draft and any payment provider documentation on webhook retries. The retry policy (8 attempts over 24 hours) currently comes only from the incident notes.

**Document status:** Each claim needs a status. Please confirm how to treat these:
- The 4xx alert and the rotation order are marked Done on 2026-09-10. Should I present them as current behavior, or mark them as unverified as of that date?
- The one-hour dual-secret window is marked proposed. Should it stay as a labelled proposal?
- The webhook failure runbook is marked Open. Is this document meant to be that runbook?

**Shape:** Guide (ordered steps for handling a failure), Narrative overview (an incident write-up) or Proposal (for the dual-secret window), or a mix? Or should I infer the shape from your answer on purpose?

**Names:** Keep the people named in the incident notes, or use roles such as Payments on-call and Guest Support?

**Validation:** I found no contradictions inside the supplied notes. Tell me if you know of one I missed.
```

Export-equivalent path: export/NNN - doc-payment-webhook-failures-clarification.md

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I have not drafted the document yet. The incident notes support the INC-0412 timeline and the 401 signature failure well, but they do not cover other webhook failures, and the purpose, audience and shape are still open. Once you answer the question above, the draft comes next.