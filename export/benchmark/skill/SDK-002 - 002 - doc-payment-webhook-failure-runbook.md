# Payment webhook failures: on-call runbook

* * *
> Status: Current behavior — practice as recorded in the INC-0412 incident notes, updated 2026-09-10. Steps the notes do not cover are listed under Not covered by the notes.
* * *

## Overview
* * *
This runbook tells whoever is on call in #payments-oncall what to do from the moment the webhook alert fires to the cleanup after it. It describes what the team does today, as the INC-0412 incident notes record it. Where the notes leave a step open, the runbook says so rather than filling the gap.

Pay now bookings wait in `payment_pending` until the payment provider confirms the payment by webhook. A booking still in that state after 30 minutes expires, and its room goes back on sale. A webhook failure therefore runs on a clock. During INC-0412, 1,284 bookings entered `payment_pending` between 12:02 and 12:49 UTC on 2026-09-09, and 94 of them expired before the fix.

The steps come from one cause: payment webhooks rejected with `signature_mismatch` after a signing-secret rotation. The notes describe no other cause. For any other reason, raise it in #payments-oncall rather than applying these steps by analogy.

### Before you start
* * *
*   **Starting condition** — The alert on `payments.webhook.4xx_rate` has paged #payments-oncall, and webhooks from the payment provider to `/v2/psp/webhooks` are being rejected
*   **Tools named in the notes** — The Payments / Webhooks dashboard, payments-service and booking-service logs, the `payment_pending` expiry job in booking-service, psp-replay and psp-reconcile
* * *

## Response steps
* * *
Run the steps in order. Pausing the expiry job comes before the cause is known, because bookings expire on a 30-minute clock. In INC-0412 the cause took 39 minutes to find, and the first bookings expired at 12:32.

### 1. Acknowledge the page and check the dashboard
* * *
The alert fires when `payments.webhook.4xx_rate` is above 5% for 5 minutes, and it pages #payments-oncall. The reason on the rejections points to the cause, so check it before anything else.

1. Acknowledge the page in #payments-oncall
2. Open the Payments / Webhooks dashboard and check the 4xx rate by reason
3. Check the payments-service logs, where each rejected webhook records its path, status, reason and event type

```text
2026-09-09T12:02:07Z WARN payments-service webhook rejected path=/v2/psp/webhooks status=401 reason=signature_mismatch type=payment.captured
```

Do not wait for the cause before step 2. The first bookings expired 30 minutes after the first rejection.

### 2. Pause the payment_pending expiry job
* * *
Pause the `payment_pending` expiry job in booking-service. While payment results are stuck, the job expires bookings whose guests may already have been charged. In INC-0412, 94 bookings expired before the job was paused at 12:36, and 71 of those guests had been charged.

The notes do not say whether the pause can be limited to the affected bookings.

### 3. Find and fix the cause
* * *
The fix depends on the cause. In INC-0412, payments-service still checked signatures with the old secret after the payment provider had started signing with the new one. The fix was to deploy the new secret to payments-service. The config reloaded at 12:49:31 with `secret_version=2026q3`, and the next webhook was accepted 13 seconds later.

The rotation order exists because INC-0412 began when the provider switched before payments-service did. See Review follow-ups.

### 4. Replay the rejected webhooks
* * *
The payment provider retries a failed webhook up to 8 times over 24 hours, and the gap grows with each attempt. A Pay now booking waits only 30 minutes, though. In INC-0412 most events were waiting on a later retry, some of them hours away, so retries alone would have left guests on the Confirming your booking screen. Replay the window instead.

1. Confirm that the logs show webhooks accepted with status 200
2. Run psp-replay for the window, from the first rejected webhook to the fix. In INC-0412 that was 12:02 to 12:49 UTC. The notes do not give the command or its parameters
3. Watch the `payment_pending` count fall. In INC-0412 the last booking from the window left the state at 13:12, 23 minutes after the fix

### 5. Resume the expiry job
* * *
Resume the expiry job once the `payment_pending` count is back at its normal level. The notes do not define that level. In INC-0412 the job resumed at 13:15, after the last booking from the window had left the state at 13:12.

### 6. Clean up expired bookings
* * *
psp-reconcile runs every 15 minutes. It reads captures from the payment provider's API rather than from webhooks, so it keeps working during a webhook outage. It refunds any capture whose booking has expired. Check its output for the window, then give Guest Support the list of expired bookings.

In INC-0412, 94 bookings expired. psp-reconcile refunded the 71 that had been charged, and the other 23 never had a successful charge.

### Done when
* * *
*   [] Webhooks are accepted with status 200 on `/v2/psp/webhooks`
*   [] Bookings from the window have left `payment_pending` or appear on the expired list
*   [] The `payment_pending` expiry job is running again
*   [] The psp-reconcile output for the window has been checked, and Guest Support has the expired list
* * *

## Not covered by the notes
* * *
Treat each item below as unknown until the notes or the Payments squad settle it.

*   **Other causes** — The notes cover one cause, `signature_mismatch` after a secret rotation. Their causes and fixes are not documented
*   **psp-replay** — The command, its parameters and how to confirm that a run has finished
*   **Normal payment_pending level** — The count that means the expiry job can resume
*   **Scoped pause** — Whether the expiry pause can cover only the affected bookings
*   **Escalation** — The notes name no path beyond #payments-oncall and no backup owner
*   **Guest Support list** — The format and delivery route for the expired-booking list
* * *

## Review follow-ups
* * *
These come from the follow-up table in the incident notes and the review on 2026-09-10. Each status is as the notes record it.

| Follow-up | Owner | Status |
| --- | --- | --- |
| Alert when `payments.webhook.4xx_rate` is above 5% for 5 minutes, paging #payments-oncall | Karim | Done on 2026-09-10 |
| Rotation order in the checklist: deploy the new secret to payments-service before switching it at the payment provider | Elif | Done on 2026-09-10 |
| Accept both the old and the new signing secret for 1 hour during a rotation | Elif | Proposal, not current practice |
| Runbook for webhook failures, linked from the Payments / Webhooks dashboard | Karim | Open. This document is the draft, and the notes record no link yet |
| Write up a dual-secret window for rotations | Elif | No status recorded in the notes |

The review also found that the expiry job kept expiring bookings until someone paused it by hand. The notes record no follow-up for that.
