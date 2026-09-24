# Notification retry requeue guide

* * *
> Status: Current behavior — verified for the notification retry pipeline as supplied in the engineering notes
* * *

## Overview
* * *
This guide is for support agents. Use it when a notification keeps failing and you need to know whether its retry schedule ran out. It covers how to confirm that a notification reached the failed queue, how to requeue it and what the restarted schedule does.

A retry runs on a 30 second backoff for five attempts. Attempt six moves the notification to the failed queue, and a requeued notification restarts the backoff.
* * *
## Process
* * *
### 1. Diagnose the notification
* * *
Check the failed queue. A notification there has run its full retry schedule, because attempt six moves it to the failed queue once the five attempts are done. If the notification is not in the failed queue, its schedule has not reached attempt six, so there is nothing to requeue yet.
* * *
### 2. Requeue the notification
* * *
Use the Requeue action on the notification in the failed queue.

*   **Requeue** — the support action that sends a notification from the failed queue back into the retry schedule
* * *
### 3. What the restarted schedule does
* * *
The requeued notification restarts the 30 second backoff. It does not skip the backoff or retry immediately. The restarted schedule matches the first run: five attempts on the 30 second backoff, after which attempt six moves the notification back to the failed queue.
* * *
### Quality checks
* * *
*   [ ] The notification is no longer in the failed queue after the Requeue action
*   [ ] The retried notification restarts the 30 second backoff instead of retrying immediately
* * *
### Boundaries and exceptions
* * *
*   **Failure cause** — the notes do not cover why a notification fails or how to read failure details, so this guide stops at the failed queue and the Requeue action
*   **Requeue limit** — the notes do not state whether a notification can be requeued more than once
* * *
