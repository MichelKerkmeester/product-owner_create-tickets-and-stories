Path: `export/002 - doc-notification-retry-requeue-guide.md`
Verified: read-back succeeded; 48 lines
HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: the em dash inside the `*   **Term** — definition` bullets and the `Status: Current behavior — ...` label, both sanctioned Doc Mode delimiters.

I wrote a Guide for support agents, marked as current behavior with your notes as the authority. It covers:

*   **Steps:** Check whether the notification is still retrying (30 second backoff, five attempts). Confirm it reached the failed queue at attempt six. Use Requeue, which restarts the backoff.
*   **Unverified steps:** The notes don't say how an agent sees the attempt count, where the failed queue appears, or what shows on screen after a requeue. I marked each step unverified instead of guessing.
*   **Not covered:** What happens if a requeued notification fails again, whether requeue resets the attempt count, and what causes a failure. These are listed under Boundaries and exceptions, so the guide doesn't help with root causes.

Quality summary:

*   **Source safety:** pass
*   **Shape fit:** pass (Guide)
*   **ClickUp layout:** pass
*   **Readability:** attention, because the guide is short by design, since the notes hold only four facts
*   **Voice:** pass

If engineering can answer the unverified points, send them and I'll fold them in. I can also push this to ClickUp if you approve. I won't do that without your go-ahead.