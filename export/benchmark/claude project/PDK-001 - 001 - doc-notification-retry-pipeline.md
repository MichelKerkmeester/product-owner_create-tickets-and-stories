# Diagnose and requeue a failed notification retry

* * *

## Overview
* * *
After this guide you can tell whether a failed notification is still retrying or has exhausted its attempts, and you can put it back into the retry cycle. It is written for support agents. Start here when a customer reports a notification that did not arrive.

It covers the retry timing, the failed queue and the Requeue action.

* * *
## How the retry behaves
* * *
A notification that fails to deliver retries on a 30 second backoff for five attempts. When attempt six comes due, the notification moves to the failed queue instead of retrying again.

The failed queue means the five attempts are used up. If the notification is not in the failed queue, it is either delivered or still inside the retry window, so give the 30 second backoff time to finish before you treat the delivery as failed.

* * *
## Process
* * *
### 1. Check the failed queue
* * *
Look for the reported notification in the failed queue. If it is there, its five attempts are used up and it stays there until it is requeued. If it is not there, it has not yet reached attempt six, which means a later attempt can still deliver it.

* * *
### 2. Requeue the notification
* * *
Use the Requeue action on the notification in the failed queue. A requeued notification restarts the 30 second backoff, so the retry cycle begins again.

* * *
### Quality checks
* * *
*   [ ] The notification no longer appears in the failed queue
*   [ ] The notification is retrying again on the 30 second backoff

* * *
### Boundaries and exceptions
*   **Attempt count after a requeue** — the backoff restarts, but whether the five attempt counter resets with it is not documented here. Do not tell the customer how many attempts remain
*   **Failure cause** — this guide covers timing and requeueing. It does not explain why the delivery failed, and root cause diagnosis sits outside its scope
