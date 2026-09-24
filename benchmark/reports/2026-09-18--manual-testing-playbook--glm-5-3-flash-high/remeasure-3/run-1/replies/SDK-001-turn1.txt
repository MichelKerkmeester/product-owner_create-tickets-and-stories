Path: `export/001 - doc-notification-retry-pipeline-clarification.md`
Verified: read-back succeeded; 13 lines
HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: straight quotes and hyphens (card punctuation rules), bold-lead question headers per the supplied Doc intake template

Quality: the question is single-topic, multi-line, one consolidated ask, and it covers every unresolved Doc-gate field (source, authority, status, shape, scope, depth, verification) without re-asking purpose or audience, which you already stated.

Here is the one question, also saved to the file:

**Source set:** Paste the engineering notes. Are they the sole source, or should any other file, link or ticket govern?
**Authority & conflicts:** If the notes contradict anything else you supply, which source controls each conflict? Do the notes declare their own status anywhere?
**Document status:** Should the result describe current behavior, approved direction, proposal, retired material or unknown? If the notes mix statuses, tell me which claims carry which status so nothing gets promoted silently
**Scope & shape:** What must be included or excluded? A behavior reference fits "how it works" for a support audience (states, retry flows, outcomes, boundaries), but confirm, or tell me to infer the shape from the notes once they arrive
**Depth & boundaries:** How much technical HOW does the support team need - retry timings, error states, identifiers, log or dashboard names? Anything they never touch that should stay out?
**Validation:** Which claims should I treat as unverified rather than fact?

Doc Mode routes this as a new-document creation, and I'm holding the draft until you answer so nothing unsupported gets written. Paste the notes together with your answers and I'll produce the document as `export/002 - doc-...md`.