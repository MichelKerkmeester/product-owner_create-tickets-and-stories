`export/002 - doc-notification-retry-guide.md`
Verified: read-back succeeded; 37 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the bold-lead definition dashes (sanctioned `**Term** — detail` delimiter) and the status-label dash (sanctioned `Status: {class} — {qualifier}` qualifier), the "Current behavior" label (your authority designation), the repeated "30 second backoff", "failed queue" and "Requeue action" (supplied identifiers, repetition sanctioned over synonyms)

Quality summary:

- Source safety: pass — every behavioral claim traces to your four note lines, the one gap (attempt count after a requeue) is labelled unknown instead of filled
- Shape fit: pass — Guide with a two-step process matching "diagnose and requeue", and Quality checks plus Boundaries each meet their include-when condition
- ClickUp layout: pass — `* * *` immediately after every content heading, `*   ` bullets, sentence-case headings, no spacer headings in the file export
- Readability: pass — takeaway-first opening, one idea per paragraph, status notice carried between title dividers
- Voice: pass — the self-scan above

The guide covers the diagnostic question (has the notification reached the failed queue, since attempt six is what delivers it there), the requeue through the Requeue action, and the resulting backoff restart. One thing your notes leave open, whether the attempt count resets alongside the restarted backoff, is surfaced in Boundaries rather than invented, so support will not promise a customer a specific number of remaining attempts.

Next step if you want it: I can extend the guide when you have that attempt-count answer, or refine any step's wording.