# Payment webhook failures runbook

* * *
> **Status: Current behavior — Payments on-call procedure, written from the INC-0412 incident notes and the 2026-09-10 review.** Where this runbook says a detail is not written down, the notes don't include it.
* * *

## Overview
* * *
This runbook takes whoever is on call in #payments-oncall from the moment the `payments.webhook.4xx_rate` alert pages or Guest Support reports guests stuck on the Confirming your booking screen through to cleanup. The payment provider sends Pay now results only by webhook, so while payments-service rejects webhooks, bookings wait in `payment_pending` until the booking-service expiry job expires them after 30 minutes.

Pause the expiry job before looking for the cause, because expired bookings are what's left to clean up once the webhooks work again. In INC-0412 on 2026-09-09, payments-service returned 401 to every webhook from 12:02 to 12:49 UTC, 47 minutes. Of 1,284 stuck bookings, 1,190 recovered and 94 expired before the pause, 71 of them charged and refunded by psp-reconcile.

### What keeps working during a failure
* * *
*   **Pay now booking** — Waits in `payment_pending` until the payment provider confirms by webhook, and after 30 minutes expires with its room back on sale
*   **Payment provider retries** — Up to 8 over 24 hours with growing gaps, so after a fix retries alone leave guests hours on the confirming screen
*   **psp-reconcile** — Reads captures from the payment provider's API every 15 minutes, not from webhooks, so it keeps refunding expired bookings' captures during a failure
*   **psp-replay** — Replays the payment provider's webhook events for a time window, so bookings don't have to wait for the next retry

### Before you start
* * *
*   **Alert** — Pages #payments-oncall when `payments.webhook.4xx_rate` stays above 5% for 5 minutes, and nothing watched that rate before it was added on 2026-09-10
*   **Dashboard** — Payments / Webhooks shows the webhook 4xx rate by reason
*   **Access** — You need to be able to pause and resume the expiry job in booking-service, deploy payments-service config and run psp-replay
*   **Not written down yet** — Pausing and resuming the expiry job, the psp-replay command and parameters, the dashboard link and the normal `payment_pending` count

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
Pause the `payment_pending` expiry job in booking-service straight away, before you look for the cause, because it doesn't stop by itself. In INC-0412 it kept running until someone paused it by hand at 12:36, and 94 bookings had expired by then. The first bookings from the failure window expired at 12:32, 30 minutes after the first rejection.

**Expected result:** bookings stop expiring. An expiry shows in the booking-service logs like this:

```text
2026-09-09T12:32:05Z INFO booking-service booking expired state=payment_pending age_s=1800 ref=RS-4HX29P
```

**Not written down yet:** the command or control that pauses the job.

### 3. Find and fix the cause
* * *
Fix whatever makes payments-service reject the webhooks. The payment provider's retries start landing only after that.

If the reason is `signature_mismatch`, check that payments-service is checking signatures with the secret the payment provider signs with.

In INC-0412, a planned rotation of the webhook signing secret switched the payment provider to the new secret at 12:02. Our config change with the new secret was merged but not yet deployed, so payments-service kept checking signatures with the old secret. Deploying that config fixed it at 12:49.

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
Check the psp-reconcile output: every booking that expired after a successful charge should have a refund. psp-reconcile works from the payment provider's API, so it may already have issued the refunds during the failure. In INC-0412 it refunded 71 captures at 12:45, before the fix, and the other 23 expired bookings never had a successful charge.

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
*   **Other rejection reasons** — Step 3 covers only `signature_mismatch`, since INC-0412 is the one source, while steps 1, 2 and 4 to 6 fit any cause
*   **Planned secret rotations** — The checklist now deploys the new secret to payments-service before the payment provider, because the old order can cause INC-0412 again

## Review follow-ups
* * *
The 2026-09-10 incident review found three gaps. Nothing alerted before Guest Support noticed the failure 19 minutes in, the rotation switched the payment provider before our side, and the expiry job kept expiring bookings until someone paused it by hand. These are the actions it agreed and where each one stands.

| Action | Owner | Status |
|--------|-------|--------|
| Alert when `payments.webhook.4xx_rate` is above 5% for 5 minutes, paging #payments-oncall | Karim | Done on 2026-09-10 |
| Rotation order in the checklist: deploy the new secret to payments-service before switching it at the payment provider | Elif | Done on 2026-09-10 |
| Accept both the old and the new signing secret for 1 hour during a rotation | Elif | proposed |
| Runbook for webhook failures, linked from the Payments / Webhooks dashboard | Karim | Open |

**Status: Proposal — not current behavior.** payments-service doesn't yet accept both secrets during a rotation, so none of the steps above rely on it.

This document is written for the runbook follow-up, which stays Open until it's linked from the Payments / Webhooks dashboard.
