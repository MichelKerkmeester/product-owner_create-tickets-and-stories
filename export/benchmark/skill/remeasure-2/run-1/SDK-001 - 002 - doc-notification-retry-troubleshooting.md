# Notification retry troubleshooting guide

* * *
> Status: Current behavior — sourced from the engineering notes, designated authoritative for this guide
* * *

## Overview
* * *
This guide shows support agents how to diagnose a notification whose retries failed and how to return it to the retry cycle. A notification that reaches the failed queue leaves it when support uses the Requeue action, so it will not retry again until someone acts.
* * *

### Before you start
* * *
*   **Required context** — access to the failed queue and the Requeue action
* * *

## Process
* * *
### 1. Confirm the notification is in the failed queue
* * *
Find the notification first, because where it sits decides what you do next. The retry runs on a 30 second backoff for five attempts, so each attempt waits 30 seconds after the one before. An attempt that fails at 10:00:00, for example, is followed by the next attempt at 10:00:30. When the five attempts have run, attempt six moves the notification to the failed queue.

A notification you find in the failed queue has been through all five attempts, so the requeue in the next step is the action to take. If the notification is not there, it is still inside the retry cycle, which means there is nothing to requeue yet.
* * *

### 2. Requeue the notification
* * *
Requeue the notification from the failed queue with the Requeue action. The engineering notes describe no other support action for a failed notification. The requeued notification restarts the 30 second backoff, so the five attempts run again. If the notification keeps failing, attempt six returns it to the failed queue and you can requeue it again.
* * *

### Quality checks
* * *
*   [ ] The notification is no longer in the failed queue
*   [ ] If the notification fails again, it returns to the failed queue through attempt six
* * *

### Boundaries and exceptions
* * *
*   **Failure cause** — the engineering notes do not describe how to inspect why a notification failed, so this guide stops at the requeue
*   **Where the failed queue lives** — the engineering notes do not describe where to find the failed queue in the product, so this guide assumes you can already reach it
*   **Attempt six timing** — the engineering notes do not say whether attempt six waits the 30 second interval before it moves the notification
*   **First attempt after a requeue** — the engineering notes do not say whether the notification's next attempt happens at once or after the 30 second wait
