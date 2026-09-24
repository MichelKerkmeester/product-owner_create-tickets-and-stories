# Notification retry failure and requeue guide

* * *
> **Status: Current behavior — per the engineering notes**
* * *

## Overview
* * *
When a notification runs out of delivery attempts it lands in the failed queue, and support can send it through the retry cycle again. This guide explains when that happens and how to do it. It is written for support agents, and it applies once a notification has been through attempt six.

*   **Retry cycle** — five attempts on a 30 second backoff, after which attempt six moves the notification to the failed queue
*   **Requeue** — the failed queue action that restarts a notification's backoff

## Process
* * *
### 1. The retry cycle
* * *
The retry pipeline makes five attempts on a 30 second backoff. Attempt six moves the notification to the failed queue, so a notification you find there has been through the full cycle.

**Example**
* * *
A notification fails. The pipeline retries, waiting 30 seconds between attempts, until the five attempts are used. Attempt six moves the notification to the failed queue. After support requeues it, the 30 second backoff starts again from the beginning, so the notification repeats the cycle.

### 2. When a notification can be requeued
* * *
Requeue lives in the failed queue, so where the notification sits decides what you can do.

*   **Still cycling** — the notification has not reached the failed queue, which means its five attempts are still running and there is nothing to requeue yet
*   **In the failed queue** — the notification has been through attempt six, and the Requeue action is available

### 3. How to requeue
* * *
Use the Requeue action on the notification in the failed queue. The notification then restarts its 30 second backoff, so the five attempts run again from the beginning. A notification that fails again goes through the same sequence and ends up back in the failed queue, where you can requeue it once more.

### Boundaries and exceptions
* * *
*   **Guide scope** — the notes cover the retry timing, the failed queue and the Requeue action, and they do not say why the original delivery failed
*   **Total duration** — the notes give the 30 second interval between attempts, not the time from the first failure to the failed queue, so avoid quoting an elapsed total to a merchant
