# Diagnosing and requeueing a failed notification retry

* * *
> **Status: Current behavior — verified for the retry backoff, the failed queue and the Requeue action, per the engineering notes supplied as authoritative.** Steps the notes do not describe are marked unverified where they appear.
* * *

## Overview
* * *
This guide is for support agents. After following it, you can tell whether a notification is still retrying or has failed for good, and you can requeue it from the failed queue. Read it when a customer reports a notification that never arrived and you need to decide whether to wait or act.

A retry runs on a 30 second backoff for five attempts. Attempt six moves the notification to the failed queue, so a notification is in one of two situations: still inside the retry cycle, or in the failed queue. Only the second one needs you.

### Before you start
* * *
The notes do not say how an agent sees a notification's attempt count or where the failed queue appears in the support tooling. Both are unverified, so confirm them with engineering before relying on this guide for a live case.

*   **Required context** — The notification you are checking and access to the Requeue action
*   **Known limitation** — The notes do not describe what causes an attempt to fail, so this guide cannot help you name a root cause

## Process
* * *
### 1. Check whether the notification is still retrying
* * *
Work out where the notification sits before you act, because a requeue is only described for the failed queue. If the notification has not reached attempt six, it is still inside the retry cycle and the backoff is running.

*   **Retry cycle** — Each retry waits a 30 second backoff, for five attempts
*   **Attempt six** — The notification moves to the failed queue

Expected result: a notification that has not reached attempt six is still retrying, and you wait for the backoff to run. How you read the attempt count is unverified.

### 2. Confirm the notification is in the failed queue
* * *
A notification that has been moved at attempt six sits in the failed queue. That is the only place the notes give you a way to act, so a notification you cannot find there is either still retrying or outside what the notes cover.

Expected result: the notification appears in the failed queue. Where you find that queue is unverified.

### 3. Requeue the notification
* * *
Use the Requeue action on the notification in the failed queue. A requeued notification restarts the backoff, which means it goes through the retry cycle again from its start.

Expected result: the notification leaves the failed queue and its backoff restarts. The notes do not say what you see on screen after the action, so that part is unverified.

### Boundaries and exceptions
* * *
*   **Repeat failures** — The notes do not say what happens when a requeued notification fails all its attempts again, or whether the attempt count resets on requeue
*   **Requeue outside the failed queue** — The notes describe Requeue only for the failed queue, so do not assume it works on a notification still retrying
*   **Causes of failure** — Not covered by the notes
