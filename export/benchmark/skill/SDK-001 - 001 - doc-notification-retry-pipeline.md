# Notification retry pipeline: diagnose and requeue

* * *
> **Status: Current behavior — sourced from the engineering notes, which the requester designated authoritative for this guide**
* * *
## Overview
* * *
A notification that fails to deliver is not lost. The pipeline gives it five attempts on a 30 second backoff, then moves it to the failed queue when attempt six runs and leaves it there until someone requeues it. This guide is for support agents chasing a failed notification: it shows how to tell whether the notification is still cycling or already waiting in the failed queue, and how to send it back through the pipeline with the Requeue action. It covers the retry mechanics, because the notes do not say why a delivery fails in the first place.

* * *
## How the retry behaves
* * *
### 1. Five attempts on a 30 second backoff
* * *
A failing delivery does not go straight to the failed queue. The retry runs on a 30 second backoff for five attempts, and while those attempts are cycling the notification is still inside the pipeline: it has neither delivered nor reached the failed queue, so there is nothing yet for support to act on.

* * *
### 2. Attempt six moves the notification to the failed queue
* * *
After the five attempts, attempt six moves the notification to the failed queue. From there nothing moves it along until support acts, because the only way out that the notes give is the Requeue action.

* * *
## What to do when a notification fails
* * *
### 1. Work out which state it is in
* * *
Timing decides the diagnosis. If the delivery failed recently, the notification may still be inside its five attempts, so give the 30 second backoff its window before you conclude anything. Once attempt six has run, the notification waits in the failed queue, and that queue is also the first place to check when an expected delivery never arrived.

* * *
### 2. Requeue it from the failed queue
* * *
Support requeues from the failed queue with the Requeue action. Find the notification in the failed queue, then apply Requeue to it. That action is the step the notes give you, and the only support action they describe.

* * *
### 3. What a requeue does
* * *
A requeued notification restarts the backoff, which means it runs the 30 second backoff again. Because the retry rules are the same, a notification that fails a second time reaches the failed queue again, where the same Requeue action applies.

* * *
### Quality checks
* * *
*   [ ] After a requeue, the notification is back in the retry cycle, waiting out its 30 second backoff
*   [ ] If the delivery fails again, the notification returns to the failed queue after attempt six, ready for another Requeue

* * *
### Boundaries and exceptions
* * *
*   **Root causes** — the notes cover the retry mechanics, so they do not explain why a delivery failed. Finding that cause is outside this guide
*   **Attempt six** — the notes say it moves the notification to the failed queue, and they do not say whether it also tries the delivery once more
*   **What a requeue guarantees** — the notes say a requeued notification restarts the backoff, and they do not say whether the attempt count resets with it
*   **One action** — the Requeue action is the only support action the notes describe, so anything else you can do from the failed queue is outside this guide
