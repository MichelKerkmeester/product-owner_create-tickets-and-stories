# Payment webhook failures runbook

* * *
> **Status: Current behavior — Payments on-call procedure, written from the INC-0412 incident notes and the 2026-09-10 review.** Where this runbook says a detail is not written down, the notes don't include it.
* * *

## Overview
* * *
This runbook takes whoever is on call in #payments-oncall from a webhook alert through to cleanup. Use it when the `payments.webhook.4xx_rate` alert pages the channel, or when Guest Support reports guests stuck on the Confirming your booking screen.

The payment provider sends the result of a Pay now payment to us only by webhook. While payments-service rejects webhooks, no Pay now booking can leave `payment_pending`. After 30 minutes, the `payment_pending` expiry job in booking-service expires each of those bookings. Pause the expiry job before you look for the cause, because expired bookings are what's left to clean up once the webhooks work again.

INC-0412 shows the cost. On 2026-09-09, payments-service answered every webhook from the payment provider with a 401 for 47 minutes, from 12:02 to 12:49 UTC. 1,284 bookings entered `payment_pending` and 1,190 recovered after the fix. 94 expired before anyone paused the expiry job. The payment provider had charged 71 of those guests, and psp-reconcile refunded them.

### What keeps working during a failure
* * *
*   **Pay now booking** — Waits in `payment_pending` until the payment provider confirms the payment by webhook. After 30 minutes the booking expires and its room goes back on sale
*   **Payment provider retries** — Up to 8 attempts over 24 hours, with a longer gap after each attempt. By the time you fix the cause, many events are waiting hours for their next attempt, so retries alone leave guests on the confirming screen
*   **psp-reconcile** — Runs every 15 minutes and reads captures from the payment provider's API, not from webhooks, so it keeps working during a webhook failure. It refunds any capture whose booking has expired
*   **psp-replay** — Replays the payment provider's webhook events for a time window, so bookings don't have to wait for the next retry

### Before you start
* * *
*   **Alert** — The alert pages #payments-oncall when `payments.webhook.4xx_rate` stays above 5% for 5 minutes. It was added on 2026-09-10. Before that, nothing watched the webhook error rate
*   **Dashboard** — Payments / Webhooks shows the webhook 4xx rate by reason
*   **Access** — You need to be able to pause and resume the expiry job in booking-service, deploy payments-service config and run psp-replay
*   **Not written down yet** — How to pause and resume the expiry job, the psp-replay command and its parameters, the dashboard link and the normal `payment_pending` count

## Response steps
* * *
### 1. Confirm the failure on the dashboard
* * *
Open the Payments / Webhooks dashboard and check the 4xx rate by reason. The reason tells you which cause to look for in step 3. Note the time of the first rejected webhook, because the replay in step 4 starts from it.

**Expected result:** a high 4xx rate on `/v2/psp/webhooks` with a single rejection reason. In INC-0412 the rate was 100%, all with reason `signature_mismatch`, and the payments-service logs showed:

```text
2026-09-09T12:02:07Z WARN payments-service webhook rejected path=/v2/psp/webhooks status=401 reason=signature_mismatch type=payment.captured
```

### 2. Pause the payment_pending expiry job
* * *
Pause the `payment_pending` expiry job in booking-service straight away, before you look for the cause. The job doesn't stop by itself. In INC-0412 it kept running until someone paused it by hand at 12:36, and 94 bookings had expired by then. The first bookings from the failure window expired at 12:32, 30 minutes after the first rejection.

**Expected result:** bookings stop expiring. An expiry shows in the booking-service logs like this:

```text
2026-09-09T12:32:05Z INFO booking-service booking expired state=payment_pending age_s=1800 ref=RS-4HX29P
```

**Not written down yet:** the command or control that pauses the job.

### 3. Find and fix the cause
* * *
Fix whatever makes payments-service reject the webhooks. The payment provider's retries start landing only after that.

If the reason is `signature_mismatch`, check that payments-service is checking signatures with the secret the payment provider signs with. In INC-0412, a planned rotation of the webhook signing secret switched the payment provider to the new secret at 12:02. Our config change with the new secret was merged but not yet deployed, so payments-service kept checking signatures with the old secret. Deploying the config with the new secret fixed it at 12:49.

**Expected result:** the config reload is logged, the 401s stop and webhooks are accepted again. In INC-0412 the payment provider's retries started landing at 12:50.

```text
2026-09-09T12:49:31Z INFO payments-service config reloaded secret_version=2026q3
2026-09-09T12:49:44Z INFO payments-service webhook accepted path=/v2/psp/webhooks status=200 type=payment.captured
```

For any reason other than `signature_mismatch`, no fix is written down. Keep the expiry job paused while you investigate.

### 4. Replay the failure window with psp-replay
* * *
Run psp-replay for the whole window, from the first rejected webhook to the fix. The payment provider's retries alone would leave most bookings waiting hours for the next attempt. In INC-0412 the replay covered 12:02 to 12:49 and ran at 12:58.

**Expected result:** bookings from the window leave `payment_pending`. In INC-0412 the last one left at 13:12, and 1,190 bookings recovered through retries and the replay.

**Not written down yet:** the psp-replay command and its parameters.

### 5. Resume the expiry job
* * *
Resume the `payment_pending` expiry job once the `payment_pending` count is back to its normal level. In INC-0412 the last booking from the window left `payment_pending` at 13:12 and the job resumed at 13:15.

**Not written down yet:** the count that counts as normal, and the command or control that resumes the job.

### 6. Check refunds and hand over to Guest Support
* * *
Check the psp-reconcile output. Every booking that expired after a successful charge should have a refund. psp-reconcile works from the payment provider's API, so it may already have issued the refunds during the failure. In INC-0412 it refunded 71 captures at 12:45, before the fix. The other 23 expired bookings never had a successful charge.

Then give Guest Support the list of bookings that expired in the window, with their booking references.

**Expected result:** every guest charged for an expired booking has been refunded, and nobody was charged twice.

### Cleanup checks
* * *
*   [ ] **Webhooks accepted again** with the 401s stopped on `/v2/psp/webhooks`
*   [ ] **Failure window replayed** with psp-replay, from first rejection to fix
*   [ ] **No booking from the window left** in `payment_pending`
*   [ ] **Expiry job resumed** in booking-service
*   [ ] **Expired captures refunded** by psp-reconcile, with no guest charged twice
*   [ ] **Expired bookings list sent** to Guest Support

### Boundaries and exceptions
* * *
*   **Other rejection reasons** — INC-0412 is the only failure behind this runbook, so step 3 covers `signature_mismatch` only. Steps 1, 2 and 4 to 6 don't depend on the cause
*   **Planned secret rotations** — The rotation checklist now deploys the new secret to payments-service before switching it at the payment provider. A rotation done in the old order can cause INC-0412 again

## Review follow-ups
* * *
The 2026-09-10 incident review found three gaps. Guest Support noticed the failure 19 minutes in, before anything alerted. The rotation switched the payment provider first and our side second. The expiry job kept expiring bookings until someone paused it by hand. These are the actions it agreed and where each one stands.

| Action | Owner | Status |
|--------|-------|--------|
| Alert when `payments.webhook.4xx_rate` is above 5% for 5 minutes, paging #payments-oncall | Karim | Done on 2026-09-10 |
| Rotation order in the checklist: deploy the new secret to payments-service before switching it at the payment provider | Elif | Done on 2026-09-10 |
| Accept both the old and the new signing secret for 1 hour during a rotation | Elif | proposed |
| Runbook for webhook failures, linked from the Payments / Webhooks dashboard | Karim | Open |

**Status: Proposal — not current behavior.** payments-service doesn't yet accept both secrets during a rotation, so none of the steps above rely on it.

This document is written for the runbook follow-up, which stays Open until it's linked from the Payments / Webhooks dashboard.
