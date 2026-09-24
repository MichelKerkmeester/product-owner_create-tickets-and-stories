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
