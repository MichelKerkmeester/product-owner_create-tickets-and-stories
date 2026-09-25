<!-- Doc Mode | Guide | Doc Templates v0.107 -->
# Diagnosing and requeuing a failed notification retry

* * *
> **Status: Current behavior — verified for the notification retry pipeline, as described in the supplied engineering notes.** The notes do not say where to find the failed queue, how to read a notification's attempt count or who may use Requeue. Steps that depend on those facts are marked unverified.
* * *

## Overview
* * *
This guide shows support agents how to tell whether a notification that did not arrive has used up its automatic retries, and how to requeue it from the failed queue. Use it when a notification has been sent but has not reached its recipient.

The pipeline retries a failed notification on a 30 second backoff for five attempts. Attempt six moves the notification to the failed queue. From there, support can requeue it with the Requeue action, and the requeued notification restarts the backoff.

### Before you start
* * *
*   **Required context** — A notification that was sent but has not reached its recipient
*   **Known limitation** — The notes do not say where the failed queue is found, how to see which attempt a notification is on, or which roles can use Requeue. Confirm these with engineering before relying on the steps marked unverified

## Process
* * *
### 1. Work out where the notification is in the retry cycle
* * *
Automatic retries come first, so a notification that has not reached attempt six is still inside the retry cycle. The notes document no support action for that stage.

*   **Retry timing** — Each retry runs on a 30 second backoff
*   **Retry limit** — Five attempts run automatically
*   **Hand-off** — Attempt six moves the notification to the failed queue

Expected result: you know whether the notification is still retrying or has moved to the failed queue. How to see the current attempt is unverified.

### 2. Confirm the notification is in the failed queue
* * *
A notification in the failed queue reached it at attempt six, which means the automatic retries did not deliver it. This step tells you where the notification is. It does not tell you why it failed, because the notes give no cause.

Expected result: the notification appears in the failed queue. How to open the failed queue is unverified.

### 3. Requeue the notification
* * *
Use the Requeue action on the notification in the failed queue. The notes document Requeue for the failed queue only.

Expected result: the notification restarts the backoff. How to see the restart is unverified.

### Quality checks
* * *
*   [ ] **Confirm the location.** The notification is either still retrying or in the failed queue
*   [ ] **Requeue from the failed queue only.** The notes document no other starting point
*   [ ] **Confirm the restart.** The notes say Requeue restarts the backoff, and how to observe it is unverified

### Boundaries and exceptions
* * *
*   **Cause of failure** — The notes give none, so this guide cannot diagnose why the attempts failed
*   **Attempt six** — The notes say attempt six moves the notification to the failed queue. They do not say whether attempt six is itself a delivery try
*   **Attempts after a requeue** — The notes say the backoff restarts. They do not say whether the five-attempt limit restarts with it
*   **A second failure** — The notes do not say whether a requeued notification that fails again returns to the failed queue
*   **Access** — The notes do not say who can use Requeue
