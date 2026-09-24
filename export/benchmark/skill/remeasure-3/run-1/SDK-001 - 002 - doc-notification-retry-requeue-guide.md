<!-- Doc Mode, Guide shape, source: supplied engineering notes, status: current behavior -->

# Diagnose and requeue a failed notification retry

* * *
> Status: Current behavior — governed by the supplied engineering notes
* * *

## Overview
* * *
This guide shows a support agent how to diagnose a notification whose retry attempts have run out and how to send it back through the pipeline. A notification reaches the failed queue because the retry runs on a 30 second backoff for five attempts, and attempt six moves the notification to the failed queue. Because a requeue restarts that backoff, the same notification can reach the failed queue more than once, so check where the notification is before you act.
* * *

## Diagnosis and requeue
* * *
### 1. Confirm the notification reached the failed queue
* * *
Find the notification in the failed queue. That placement is the outcome the documented cycle produces: five attempts on a 30 second backoff, and then attempt six moves the notification out of the retry cycle. A notification that is not there yet has not reached attempt six, because placement in the failed queue happens at attempt six.
* * *

### 2. Requeue the notification
* * *
Use the Requeue action from the failed queue. That action returns the notification to the retry cycle.
* * *

### 3. Tell the affected user what happens next
* * *
A requeued notification restarts the backoff from the beginning rather than resuming where it stopped, so it runs through the same five attempts before attempt six moves it to the failed queue again. Tell the affected user the retry timing starts from the beginning.
* * *

### Quality checks
* * *
*   [ ] The notification has left the failed queue and restarted the 30 second backoff
*   [ ] A repeat failure follows the same documented pattern: five attempts, then attempt six moves the notification back to the failed queue
* * *

### Boundaries and exceptions
* * *
*   **No failure detail** — no error codes or attempt details are documented, so the failed-queue placement is the signal this guide diagnoses from
*   **Not covered here** — why an attempt fails, what happens after a second failed-queue placement and whether a successful attempt ends the cycle early, so do not infer these from the rules above
