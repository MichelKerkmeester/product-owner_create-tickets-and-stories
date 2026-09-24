# Diagnosing and requeuing a failed notification retry

* * *
> **Status: Current behavior — verified for the notification retry pipeline.** The engineering notes are the governing source for every claim in this guide.
* * *

## Overview
* * *
Use this guide to confirm that a notification exhausted its delivery attempts and to return it to the delivery pipeline. It is written for support agents who work the notification failed queue. The work is two steps, both done from that queue: confirm the retries ran out, then requeue with the Requeue action.
* * *
###   

### Before you start
* * *
*   **Required context** — Support access to the notification failed queue, where the Requeue action is available
*   **Known limitation** — The engineering notes are the only source. They cover the retry timing and the requeue path. Anything else about the pipeline is outside this guide
* * *
##   

## Process
* * *
### 1. Confirm the notification exhausted its retries
* * *
The failed-queue entry is the diagnosis. It means the automatic retries are used up and no further retry runs until support requeues.

*   **Retry timing** — Five attempts on a 30 second backoff, then attempt six moves the notification to the failed queue
* * *
###   

### 2. Requeue the notification
* * *
A requeued notification restarts the backoff, so the 30 second backoff for five attempts runs again from the beginning. If all five attempts fail again, attempt six returns the notification to the failed queue, where it can be requeued once more.

*   **Action** — The Requeue action, applied from the notification failed queue
* * *
###   

### Quality checks
*   [ ] The notification sits in the failed queue, past attempt six
*   [ ] After the Requeue action, the notification restarts the 30 second backoff for five more attempts
*   [ ] If all five attempts fail again, the notification returns to the failed queue at attempt six
* * *
###   

### Boundaries and exceptions
* * *
*   **Failure cause** — Diagnosing why delivery attempts fail needs sources beyond the engineering notes. This guide confirms exhaustion and performs the requeue, and it stops there
*   **Escalation** — For a notification that fails again after a requeue, the notes supply no step beyond requeuing a second time
