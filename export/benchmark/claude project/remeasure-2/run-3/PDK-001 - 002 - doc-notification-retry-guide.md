<!-- Doc Mode, Templates - Doc Mode v0.108, creation, Guide -->

# Support guide: diagnose and requeue a failed notification retry

* * *
> **Status: Current behavior — the supplied engineering notes govern every claim in this guide.**
* * *

## About this guide
* * *

Support agents use this guide to work out where a notification sits in the retry pipeline and, when it has reached the failed queue, return it to the retry cycle with the **Requeue** action. You need visibility of the failed queue and the ability to use the **Requeue** action, because the diagnosis reads the queue and support applies the **Requeue** action from there. The scope is the retry cycle, the failed queue and the **Requeue** action. Anything the supplied notes leave open is listed under What the supplied notes do not cover

* * *

## How the retry pipeline behaves
* * *

### The retry cycle
* * *

A failing notification retries on a 30 second backoff for five attempts. While those attempts run, the notification needs no support action

* * *

### The failed queue
* * *

Attempt six moves the notification to the failed queue. A notification listed there has finished its retry cycle, and the notes record one way out: the **Requeue** action

* * *

### What the Requeue action does
* * *

A requeued notification restarts the backoff: five attempts on the 30 second backoff, with attempt six returning it to the failed queue if it fails again

* * *

## Diagnose and requeue
* * *

### Diagnose where the notification sits
* * *

The failed queue is the signal, because attempt six is the only documented way a notification reaches it

1.  If the notification is listed and no one has requeued it yet, its retry cycle has ended and it is ready for the **Requeue** action
2.  If the notification is not listed, it is either still working through its attempts or it has already succeeded. Expected result: no support action yet
3.  If someone has already requeued it, the notification restarted its backoff. The notes do not say where it sits while the new attempts run, so check that its current cycle has ended before you requeue it again

* * *

### Requeue the notification
* * *

The notes cover the action, not the screens around it

1.  Open the failed queue
2.  Find the notification you diagnosed in the previous step
3.  Apply the **Requeue** action

**Expected result:** the notification restarts the backoff, as described under What the Requeue action does

* * *

## What the supplied notes do not cover
* * *

*   Why a delivery attempt fails, including any error messages or logs
*   How long a notification waits in the failed queue, and anything that happens to it while it waits
*   Where a requeued notification sits while its new attempts run and whether it can be requeued more than once
*   The screens or navigation around the failed queue and the **Requeue** action
