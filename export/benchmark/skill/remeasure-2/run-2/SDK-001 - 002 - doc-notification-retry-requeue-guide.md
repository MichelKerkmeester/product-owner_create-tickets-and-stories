# Diagnosing and requeuing a failed notification retry

* * *
> **Status: Current behavior — the engineering notes are the governing source for every claim in this guide**
* * *

## Overview
* * *
This guide takes a support agent through diagnosing a failed notification retry and requeuing it from the failed queue. It covers the 30 second backoff, the failed queue and the Requeue action.

* * *

### How the retry behaves
* * *
A retry runs on a 30 second backoff for five attempts. Attempt six then moves the notification to the failed queue. That sequence doubles as the diagnostic: a notification sitting in the failed queue has been moved there by attempt six, while a notification that is not yet in the failed queue may still be inside its backoff window.

* * *
## Process
* * *
### 1. Confirm the notification reached the failed queue
* * *
Check whether the notification appears in the failed queue. If it does, attempt six has moved it there, the retries are finished and the Requeue action applies. If it does not, the notification may still be inside its backoff window, which means there is nothing to requeue yet.

* * *
### 2. Requeue from the failed queue
* * *
Use the Requeue action on the notification in the failed queue. The requeued notification restarts the backoff, which means the same cycle runs again: five attempts, 30 seconds apart, before attempt six can move it back to the failed queue.

* * *
## Boundaries and exceptions
* * *
*   **Why and how the notification entered the cycle** — the notes start from a notification that is already retrying and do not say what put it there
*   **Failed-queue access** — where the failed queue and the Requeue action appear is outside the notes
