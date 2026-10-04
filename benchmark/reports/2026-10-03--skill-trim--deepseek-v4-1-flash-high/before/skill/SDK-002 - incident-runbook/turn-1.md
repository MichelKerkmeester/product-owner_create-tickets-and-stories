Path: `export/001 - doc-payment-webhook-failure-handling-clarification.md`

Verified: read-back succeeded; 26 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `signature_mismatch`, `/v2/psp/webhooks`, `401`, `4xx`, `Open`, `Done` and `proposed` are literal identifiers and supplied source status labels preserved verbatim.

Quality summary
*   Source safety: pass. Both supplied sources used, no conflicts created, nothing promoted past its supplied status, source files unchanged
*   Shape fit: pass. One consolidated Doc clarification in the `$doc` lane, at the next number
*   ClickUp layout: not applicable to a clarification file
*   Readability: pass. Unresolved fields only, grouped so one reply settles all of them
*   Voice: pass. No hard blockers; source status words kept as the notes wrote them

I read the incident notes and the company context and found no conflict between them, so nothing is blocked on authority. The remaining gaps are what the document should make a reader able to do, who reads it, whether it covers all payment webhook failure modes or only the secret-rotation case the notes actually record, and whether Karim's action list is current verified procedure or a proposed runbook, given the follow-up table still lists the runbook as Open. Answer the five fields in that file in one response and I will draft the document next.

Note on an addition I did not make: a general "handling payment webhook failures" runbook would need failure modes, causes and diagnostics that no supplied source covers, so I asked rather than inventing them.