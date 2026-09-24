```markdown
<!-- Doc Mode, Guide shape, Assets - Doc Templates -->

# Diagnosing and requeuing a failed notification retry

* * *
> **Status: Current behavior — verified for the notification retry pipeline.** The supplied engineering notes are the source of record for every rule below
* * *

## Overview
* * *

Use this guide when a notification stops delivering and you need to know where it sits in the retry cycle, or when it has reached the failed queue and you need to send it back. It follows the notification from the first retry attempt to the support requeue, so you can tell whether to wait or act. It is written for support agents who can see the notification queues

* * *

### Before you start
* * *

*   **Required context** — The notification must already sit in the failed queue. The Requeue action exists only there

* * *

## Process
* * *

### 1. Locate the notification
* * *

A retried notification runs on a 30 second backoff for five attempts. Attempt six moves the notification to the failed queue. A notification you find in the failed queue has therefore been through all six attempts and waits there for support.

If the notification is not in the failed queue yet, it is still inside the retry cycle. That cycle continues on its own, and the Requeue action becomes available only once attempt six moves the notification across

* * *

### 2. Requeue from the failed queue
* * *

Open the failed queue and use the Requeue action on the notification. A requeued notification restarts the backoff, so it begins the schedule again instead of resuming where it stopped. It waits 30 seconds, then runs up to five more attempts. If it keeps failing, attempt six returns it to the failed queue

* * *

### Quality checks
* * *

*   [ ] The notification has left the failed queue after the Requeue action
*   [ ] The retry restarted from the beginning of the 30 second backoff, and a renewed failure returns the notification to the failed queue at attempt six

* * *

### Boundaries and exceptions
* * *

*   **Scope of the fix** — Requeuing returns the notification to the retry cycle. It does not address why the delivery failed, and the supplied notes do not explain the cause
*   **Timings** — The 30 second interval, the five-attempt limit and the move at attempt six are the only timings the supplied notes give. Nothing here covers other notification types or longer failures
```

**Export-equivalent path:** `export/002 - doc-notification-retry-support-guide.md`

**HVR self-scan:** 0 hard blockers. Fixed: none. Kept with reason: the `Status: Current behavior — ...` label delimiter and the bold-lead bullet dashes (both sanctioned ClickUp contract shapes), plus the source's own "30 second" spacing.

Quality:
- Source safety: pass — one authoritative source, one class (current behavior), no conflicts to resolve
- Shape fit: pass — Guide, matched to the diagnose-and-requeue job, and the support agent needs no other document to finish
- ClickUp layout: pass — `* * *` dividers, `*   ` bullets, dividers after every heading, sentence case, no spacer headings in this export
- Readability: pass — takeaway-first paragraphs, checklist short, narrative register in the steps
- Voice: pass — 0 hard blockers

The guide walks the agent from locating the notification, through confirming it reached the failed queue at attempt six, to the Requeue action and what the restarted cycle does. Two assumptions, in plain prose so you can correct either: technical depth stays operational because the notes supply no code or configuration, and "restarts the backoff" is read as the whole 30 second, five-attempt schedule beginning again, so a renewed failure lands in the failed queue at attempt six once more. No related-guidance links exist because none were supplied. Anything to adjust, or shall it stand?