# Notification retry diagnosis and requeue

* * *

## Overview
* * *
Use this guide to take a notification that has exhausted its retries and send it back through the retry cycle. It is written for support agents, and the work happens in the failed queue, where a notification lands once its sixth attempt completes. Diagnosis here means placing the notification on the retry timeline, not finding why it failed. The rules in step 1 come first, because they are what a requeue restarts

* * *

## Process
* * *
### 1. Confirm the retry state
* * *
Before you requeue anything, place the notification on the retry timeline. Three rules govern the retry, and together they decide when a notification fails and what a requeue will do

*   **Backoff** — a retry runs on a 30 second backoff
*   **Attempts** — the retry runs for five attempts
*   **Failed queue** — attempt six moves the notification to the failed queue

A notification you find in the failed queue has used its five attempts, because the sixth is what moved it. A notification still inside the retry cycle is running the 30 second backoff, and your work starts when its sixth attempt moves it to the failed queue

* * *
### 2. Requeue the notification
* * *
Support can requeue from the failed queue, and the **Requeue** action is the step that does it

*   Find the notification in the failed queue
*   Apply the **Requeue** action

**Expected result**
* * *
The notification restarts the backoff, so all five attempts run again on the 30 second backoff. Its sixth attempt moves the notification to the failed queue if the failure repeats

* * *
### Quality checks
* * *
*   [ ] The notification restarts the 30 second backoff after the **Requeue** action
*   [ ] A notification whose failure repeats returns to the failed queue on its sixth attempt

* * *
### Boundaries and exceptions
* * *
*   **Requeue is not a repair** — a requeued notification restarts the backoff, so it repeats every rule in step 1
*   **Why it failed** — this guide does not cover what makes an attempt fail, so it places a notification on the retry timeline instead
