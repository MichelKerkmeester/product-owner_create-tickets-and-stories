`export/002 - doc-notification-retry-requeue-guide.md`

Verified: read-back succeeded; 44 lines

HVR self-scan: 0 hard blockers. Fixed: (none needed). Kept with reason: em dashes only in the two sanctioned Doc shapes (the `**Term** — definition` bullets and the `Status: Current behavior — ...` label), and the labels Retry cycle and Requeue repeat on purpose under the synonym-cycling rule.

Quality: Source safety pass — every claim traces to one of the four supplied note lines, current behavior labeled, nothing invented. Shape fit pass — Guide for support agents, diagnose-then-requeue ordering. ClickUp layout pass — `* * *` dividers after every heading, `*   ` bullets, sentence case, no bullet terminal periods, no spacer headings in the file export. Readability pass. Voice pass.

The guide covers the five attempt, 30 second backoff cycle, attempt six into the failed queue, when the Requeue action applies and what a requeue restarts. Two gaps in the notes are surfaced as boundaries rather than filled: why the original delivery failed, and the total elapsed time before the failed queue. If the notes cover either, paste those lines and I'll fold them in; no ClickUp tooling is connected in this runtime, so file export is the delivery.