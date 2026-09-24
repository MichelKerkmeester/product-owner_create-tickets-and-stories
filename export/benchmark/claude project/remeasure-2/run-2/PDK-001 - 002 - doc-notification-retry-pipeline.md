<!-- Doc, Guide, Templates - Doc Mode v0.108 -->

# Diagnosing and requeueing a failed notification

* * *
> **Status: Current behavior — the engineering notes supplied for this guide are the governing source.** The guide covers retry timing, the failed queue and the Requeue action exactly as the notes state them, and adds no behavior the notes do not support.
* * *

## Overview
* * *
This guide shows a support agent how to confirm that a notification exhausted its retries, and how to send it back into the retry cycle from the failed queue. Use it when a reported notification never arrived and the failed queue is the likely place to look. The pipeline gives a failing notification five retry attempts, 30 seconds apart. Attempt six moves the notification to the failed queue, where it waits until someone requeues it with the Requeue action.
* * *
### Before you start
* * *
*   **Required context** — Access to the failed queue, where a notification lands after attempt six
*   **Required context** — The retry timings in the Overview, so you can tell a notification still working through its retries from one that has already reached the failed queue
* * *
## Process
* * *
### 1. Confirm the notification exhausted its retries
* * *
Check the failed queue for the reported notification before you act. A notification still working through its five retry attempts has not reached the failed queue yet, so there is nothing to requeue. Each attempt trails the last by 30 seconds, so all five attempts pass in about two minutes.
* * *
### 2. Requeue the notification
* * *
Open the notification in the failed queue and use the Requeue action. A notification that is not in the failed queue has not reached attempt six yet, so there is nothing to requeue there.
* * *
### 3. Tell the customer what happens next
* * *
A requeued notification restarts the backoff. The 30 second, five attempt pattern runs again from the start, which means a notification can work its way back to the failed queue. Tell the customer the process and its timing, not a delivery promise, because the notes cover what the pipeline does, not whether a later round succeeds.
* * *
### Quality checks
* * *
*   [ ] Was the notification in the failed queue when you acted, rather than still working through its retries?
*   [ ] Did you requeue it with the Requeue action from the failed queue?
*   [ ] Did you tell the customer that the backoff restarts, without promising delivery?
* * *
### Boundaries and exceptions
* * *
*   **Failure causes** — The notes cover timing, the failed queue and the Requeue action. They do not say why a delivery fails, so treat a failed-queue listing as the signal that retries ran out, not as a diagnosis
*   **Requeue limits** — The notes set no limit on how often you can requeue. Every requeue restarts the 30 second backoff, so each round of retries starts from zero again
