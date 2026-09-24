Path: `export/001 - doc-notification-retry-pipeline.md`
Verified: read-back succeeded; 51 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the em dashes in the status notice and the four bold-lead boundaries (both are the granted `*   **Term** — definition` and `Status: {class} — {qualifier}` delimiter shapes), `Requeue` capitalized mid-prose (literal identifier from the notes), and the "attempt six" wording (preserved source notation).

Quality summary: Source safety — pass (every claim traces to your notes, and the two points the notes leave unstated, whether attempt six also retries the delivery and whether the attempt count resets on requeue, are flagged in Boundaries rather than resolved). Shape fit — pass, Guide for a support agent diagnosing then requeueing. ClickUp layout — pass (`* * *` dividers, `*   ` bullets, sentence-case headings, no spacer headings in the file export). Readability — pass. Voice — pass.

The guide covers the retry mechanics (five attempts, 30 second backoff, attempt six into the failed queue), a timing-based diagnosis for where a notification sits, the Requeue step, and what a requeue restarts. Nothing was stated beyond what your notes support, and the quality checks give the agent an observable way to confirm the requeue took.

Next step if you want it: ClickUp delivery of this document — say the word and I'll push it.