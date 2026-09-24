`export/002 - doc-notification-retry-requeue-guide.md`

Verified: read-back succeeded; 35 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: three em dashes, the `Status: Current behavior —` label delimiter and the two definition-dash delimiters, each sanctioned by Doc Mode's narrow exemption.

Quality: Source safety, pass — every claim traces to the notes as the designated governing source, and the two derived readings (below) are the only sentences that go past it. Shape fit, pass — the support agent's two jobs (diagnose, then requeue) map onto the Guide's ordered Process, with the failure mechanics placed before the steps. ClickUp layout, pass — `* * *` dividers, `*   ` bullets, sentence-case headings, no spacers, H2 stays at three. Readability, pass. Voice, pass.

Every factual claim is the notes' own: 30 second backoff, five attempts, attempt six moves the notification to the failed queue, the Requeue action, and the restarted backoff. Two derivations, so you can veto either: the 30 second backoff read as the spacing between attempts, and "restarts the backoff" read as the full five-attempt cycle running again before attempt six applies.

The guide stays inside the notes' coverage and says so: why the notification entered the retry cycle and where the failed queue and Requeue action surface are recorded as outside the source rather than invented. If you want a refinement, say what changes and I'll edit in place as `002`, preserving the current structure.