# Notification retries: diagnosing and requeueing a failure

* * *
> **Status: Current behavior — per the authoritative engineering notes, covering the retry cycle, the failed queue and the Requeue action**
* * *

## Overview
* * *
Support agents use this guide to diagnose where a notification sits in its retry cycle and to requeue it once the cycle ends. Start here when a notification has not arrived and you need to know whether it is still retrying or already sitting in the failed queue. A notification retries on a 30 second backoff for five attempts. Attempt six then moves the notification to the failed queue, where support can requeue it, restarting the 30 second backoff.
* * *

## Process
* * *
### 1. Diagnose where the notification sits
* * *
Diagnosis comes down to one question: has the notification reached the failed queue. Attempt six is the step that moves a notification to the failed queue.

*   **Not in the failed queue** — the notification is still working through its five attempts on the 30 second backoff, so the requeue does not apply yet
*   **In the failed queue** — attempt six has already moved the notification, so the retry cycle is finished and the next action is the requeue in step 2
* * *

### 2. Requeue the notification
* * *
Support requeues from the failed queue with the Requeue action. Apply it to the notification you diagnosed in step 1. A requeued notification restarts the 30 second backoff. What that restart means for the attempt count is covered under Boundaries and exceptions.
* * *

### Quality checks
* * *
*   [ ] **Confirm the queue** — the notification was in the failed queue before you used the Requeue action
*   [ ] **Check the retry** — the notification is retrying again after the Requeue action, which means the 30 second backoff restarted
* * *

### Boundaries and exceptions
* * *
*   **Waiting after the failed queue** — a notification in the failed queue does not retry again on its own, because attempt six, the step that moved the notification there, has already run
*   **Attempt count after a requeue** — the supplied engineering notes say a requeued notification restarts the backoff. They do not say whether the attempt count resets too, so the remaining attempts stay unknown
