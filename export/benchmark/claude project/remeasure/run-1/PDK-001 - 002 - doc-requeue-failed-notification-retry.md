<!-- Doc Mode. Template: Guide v0.100. Source: engineering notes, designated authoritative. Quality: pass -->

# Requeue a failed notification retry

* * *
> **Status: Current behavior — verified against the engineering notes for the notification retry pipeline.** The notes are the governing source for every claim in this guide.
* * *

## Overview
* * *
This guide takes a support agent from a failed notification to a requeued retry: first confirming the notification exhausted its 30 second backoff attempts, then requeueing it from the failed queue. It covers the retry schedule, the failed queue and the Requeue action. It does not cover why a notification fails, because the engineering notes do not cover failure causes.
* * *

### Before you start
* * *
*   **Required context** — The notification sits in the failed queue, where it lands when attempt six follows the five 30 second backoff attempts
*   **Known limitation** — The notes cover the retry schedule and the Requeue action, so this guide diagnoses by queue state and not by failure cause
* * *
## Process
* * *
### 1. Confirm the notification exhausted its retries
* * *
The retry runs on a 30 second backoff for five attempts. Attempt six moves the notification to the failed queue. That sequence is the diagnosis, because the queue tells you where the notification stands without opening anything else.

*   **Notification in the failed queue** — Its five attempts ran, attempt six followed, and the notification is waiting on a requeue
*   **Notification not in the failed queue** — It is still inside the retry window, so let attempt six run before you requeue
* * *
### 2. Requeue the notification
* * *
Support can requeue from the failed queue with the **Requeue** action. A requeued notification restarts the backoff, which means a fresh run of five attempts on the 30 second backoff. The earlier attempt count does not carry over.

**Expected result**
* * *
The notification restarts the backoff. If the new attempts also fail, attempt six returns the notification to the failed queue.
* * *
## Boundaries and exceptions
* * *
*   **Failure cause** — The notes do not say what makes a notification fail, so this guide diagnoses by queue state only
*   **Requeue limit** — The notes do not state how many times a notification can be requeued. Each requeue restarts the 30 second backoff, so every run gets its own five attempts
