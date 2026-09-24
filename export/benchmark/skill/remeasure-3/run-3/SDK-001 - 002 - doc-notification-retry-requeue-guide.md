# Diagnose and requeue a failed notification retry

* * *
> **Status: Current behavior — per the engineering notes, which govern this guide**
* * *

## Overview
* * *
This guide takes a support agent from a failed notification to a diagnosis and a fix: confirm the failure is retry exhaustion, then requeue the notification from the failed queue. It exists because a notification can fail twice for different reasons, and the failed queue only answers for one of them, so knowing where a notification sits in the retry cycle decides whether a requeue is the right move.
* * *

### Before you start
* * *
*   **Required access** — the failed queue, where the Requeue action lives
* * *

## Process
* * *
### 1. Confirm the notification exhausted its retries
* * *
Retry exhaustion has one signature: the notification ends up in the failed queue. The cycle that puts it there runs the same way every time, so queue placement is the diagnosis.

*   **Retry cycle** — the retry runs on a 30 second backoff for five attempts, and attempt six moves the notification to the failed queue
*   **What the placement tells you** — a notification in the failed queue has been through its attempts, because the only route into that queue in these notes is attempt six

Until attempt six, the notification is still inside its attempt window and may still come back on its own, so wait rather than requeue, because the notes give no way to interrupt or shortcut a cycle that is still running.
* * *
### 2. Requeue the notification
* * *
Requeueing sends the notification straight back into the cycle you diagnosed in step 1. Use the Requeue action on the failed queue, then set expectations with whoever is waiting: the notification restarts the 30 second backoff, runs its five attempts again and lands back in the failed queue if attempt six fails again.

*   **Requeue action** — support requeues from the failed queue with the Requeue action
*   **Backoff restart** — a requeued notification restarts the backoff, so it repeats the same 30 second, five-attempt cycle
*   **If it fails again** — the same rule applies, because attempt six moves the notification back to the failed queue, where the Requeue action is available again
* * *

### Quality checks
* * *
*   [ ] You confirmed the notification reached the failed queue through attempt six before you requeued it
*   [ ] After the requeue, the notification restarts its backoff, which means it runs the 30 second, five-attempt cycle again
* * *

### Boundaries and exceptions
* * *
*   **Requeue limit** — the notes do not say how many times a notification can be requeued, so the limit is unknown
*   **Failures outside the retry cycle** — the notes cover the backoff, the attempt count and the failed queue, so they do not say how to diagnose a failure that never reaches the failed queue
* * *
