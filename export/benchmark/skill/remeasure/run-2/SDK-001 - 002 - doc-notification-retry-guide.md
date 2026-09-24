# Notification retry support guide

* * *
> **Status: Current behavior — the engineering notes, which are authoritative for this document**
* * *

## Overview
* * *
This guide shows a support agent how to diagnose a failed notification retry and put the notification back into the retry cycle. It covers the 30 second backoff that decides when a notification reaches the failed queue, and the **Requeue** action that returns a failed notification to service. Use it when a customer reports a missed notification and you need to know whether the retry recovers on its own or the notification needs a requeue.

* * *
## Retry behavior
* * *
### The 30 second backoff
* * *
A notification that fails delivery gets five more chances before support has to act. The retry runs those five attempts on a 30 second backoff: each attempt starts 30 seconds after the previous one. While attempts remain, the notification recovers on its own and nobody has to touch it.

* * *
### Attempt six and the failed queue
* * *
Attempt six is where the queue changes. When the five backoff attempts are spent, attempt six moves the notification to the failed queue. From there it waits for support rather than for another retry.

* * *
## Process
* * *
### Diagnose a failed retry
* * *
The failed queue is the diagnostic signal. A notification sitting there has spent all five attempts, so it will not recover unless you requeue it. A notification that has not reached the failed queue yet is still inside the retry window, because its attempts are not spent.

* * *
### Requeue the notification
* * *
1. Open the failed queue and find the notification whose retry failed
2. Run the **Requeue** action on it

Requeue only works from the failed queue, so this is the one way back into the retry cycle. The notification then leaves the failed queue and restarts the backoff, which means the full cycle runs again: five attempts 30 seconds apart, and if delivery still fails, attempt six moves it back to the failed queue. You can requeue it again from there.

* * *
### Quality checks
* * *
*   [ ] After the requeue, the notification retries on the 30 second backoff
*   [ ] If five more attempts fail, attempt six returns the notification to the failed queue

* * *
## Boundaries
* * *
*   **Failure causes** — the notes do not record why an attempt fails, so this guide cannot answer that question
*   **Adjacent systems** — the supplied notes do not cover queueing internals, delivery channels or analytics
