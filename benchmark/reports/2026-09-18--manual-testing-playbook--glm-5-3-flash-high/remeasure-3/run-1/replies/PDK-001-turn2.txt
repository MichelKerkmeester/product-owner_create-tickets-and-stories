All intake is resolved: Guide shape, support-agent audience, diagnose-and-requeue purpose, the notes as the sole authoritative source, all claims current behavior, no conflicts. Drafted, validated against the six-dimension floors (Accuracy 9, no invented claims; the two gaps the notes carry are labelled rather than filled), voice-passed, and delivered.

---

**Block: `export/002 - doc-notification-retry-pipeline-guide.md`**

```markdown
<!-- Doc Mode | Guide (Doc Templates v0.107) | Quality: pass -->

# Diagnose and requeue a failed notification retry

* * *
> **Status: Current behavior — the notification retry pipeline, as supplied in the engineering notes.** Every rule below comes from those notes
* * *

## Overview
* * *

This guide shows a support agent how to diagnose a failed notification retry and requeue the notification. The diagnosis and the requeue each rest on one documented fact: a notification in the failed queue has exhausted its retry cycle, and the Requeue action there restarts the backoff.

Use this guide when a notification sits in the failed queue and a customer is waiting. The queue membership itself is the diagnostic, because the only documented path into that queue is the exhausted retry cycle.

* * *

## Diagnose and requeue
* * *

### 1. Confirm the retry cycle exhausted itself
* * *

A retry cycle runs five attempts on a 30 second backoff, and then attempt six moves the notification to the failed queue. That placement is the diagnosis: the notification exhausted its cycle. What made each attempt fail is not documented.

*   **Backoff** — The retry cycle runs on a 30 second backoff
*   **Attempts** — Five. Attempt six moves the notification to the failed queue

* * *

### 2. Requeue the notification
* * *

With the state confirmed, the fix is the Requeue action in the failed queue. It carries one documented outcome: the requeued notification restarts the backoff, which means the retry cycle begins again.

*   **Requeue action** — Available to support in the failed queue
*   **Outcome** — A requeued notification restarts the backoff

* * *

### Boundaries and exceptions
* * *

*   **Failure causes** — The notes do not say what makes an attempt fail, so this guide covers the retry mechanic and the requeue, not root cause analysis
*   **Repeat failures** — The notes do not restate the attempt six rule for a notification that fails again after a requeue, so a second failed cycle is not covered here
```

---

**Export-equivalent path:** `export/002 - doc-notification-retry-pipeline-guide.md`

**Quality summary:**
- Source safety: pass — one authoritative source, every claim traces to it, both source gaps labelled instead of filled
- Shape fit: pass — Guide, ordered diagnose-then-requeue, opening states outcome, audience and starting condition
- ClickUp layout: pass — `* * *` dividers, `*   ` bullets, sentence-case headings, no spacer headings in the export
- Readability: pass — takeaway-first paragraphs, one idea each
- Voice: pass — no hard blockers

**Assumption you can correct:** I read "diagnose" as confirming the exhausted-retry state from queue membership, since the notes supply no failure-cause diagnostics. If you want the guide to name what agents should check in other systems, tell me and I will extend it.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the em dash in the status label and the four definition bullets, both sanctioned by the Doc Mode exemptions.

Need anything else, or shall this stand as delivered?