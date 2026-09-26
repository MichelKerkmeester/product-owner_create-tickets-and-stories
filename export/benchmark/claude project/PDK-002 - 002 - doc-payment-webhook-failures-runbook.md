# Payment webhook failures runbook

* * *
> **Status: Current behavior — Payments on-call procedure, written from the INC-0412 incident notes and the 2026-09-10 review.** Details marked not written down are missing from the notes.
* * *

## Overview
* * *
This runbook takes #payments-oncall from the `payments.webhook.4xx_rate` page, or Guest Support reporting guests stuck on Confirming your booking, to cleanup. Pay now results arrive only by webhook, so while payments-service rejects them, bookings sit in `payment_pending` until the booking-service expiry job expires them after 30 minutes.

In INC-0412 on 2026-09-09, payments-service returned 401 to every webhook from 12:02 to 12:49 UTC, 47 minutes. Of 1,284 stuck bookings, 1,190 recovered and 94 expired, 71 of them charged and refunded by psp-reconcile.

### What keeps working during a failure
* * *
*   **Pay now booking** — Waits in `payment_pending`, then expires after 30 minutes with its room back on sale
*   **Payment provider retries** — Up to 8 over 24 hours with growing gaps, so guests can wait hours
*   **psp-reconcile** — Reads captures from the payment provider's API every 15 minutes and refunds expired bookings' captures
*   **psp-replay** — Replays the payment provider's webhook events for a time window

### Before you start
* * *
*   **Alert** — Pages #payments-oncall when `payments.webhook.4xx_rate` stays above 5% for 5 minutes, added on 2026-09-10
*   **Dashboard** — Payments / Webhooks shows the webhook 4xx rate by reason
*   **Access** — Pausing and resuming the booking-service expiry job, deploying payments-service config and running psp-replay
*   **Not written down yet** — Pausing and resuming the expiry job, psp-replay's command and parameters, the dashboard link and the normal `payment_pending` count

## Response steps
* * *
### 1. Confirm the failure on the dashboard
* * *
The 4xx reason points to the cause in step 3. Note the first rejected webhook's time, where the step 4 replay starts.

**Expected result:** a high 4xx rate on `/v2/psp/webhooks` with one reason, in INC-0412 100% `signature_mismatch`:

```text
2026-09-09T12:02:07Z WARN payments-service webhook rejected path=/v2/psp/webhooks status=401 reason=signature_mismatch type=payment.captured
```

### 2. Pause the payment_pending expiry job
* * *
Pause it before finding the cause, because it doesn't stop itself. In INC-0412 bookings began expiring at 12:32, 30 minutes after the first rejection, and 94 had expired by the manual pause at 12:36.

**Expected result:** bookings stop expiring. An expiry logs as:

```text
2026-09-09T12:32:05Z INFO booking-service booking expired state=payment_pending age_s=1800 ref=RS-4HX29P
```

**Not written down yet:** the command or control that pauses the job.

### 3. Find and fix the cause
* * *
Retries land only after the fix. For `signature_mismatch`, check payments-service verifies with the payment provider's signing secret.

In INC-0412, a planned rotation moved the payment provider to the new secret at 12:02, while our config was merged but not deployed. Deploying it fixed the failure at 12:49.

**Expected result:** the config reload logs and webhooks are accepted, in INC-0412 with retries landing from 12:50.

```text
2026-09-09T12:49:31Z INFO payments-service config reloaded secret_version=2026q3
2026-09-09T12:49:44Z INFO payments-service webhook accepted path=/v2/psp/webhooks status=200 type=payment.captured
```

No fix is written down for other reasons, so keep the job paused while investigating.

### 4. Replay the failure window with psp-replay
* * *
Replay from the first rejected webhook to the fix, so bookings skip the hours-long wait for the next retry. In INC-0412 it covered 12:02 to 12:49 and ran at 12:58.

**Expected result:** window bookings leave `payment_pending`, in INC-0412 the last at 13:12, with 1,190 recovered by retries and replay.

**Not written down yet:** the psp-replay command and its parameters.

### 5. Resume the expiry job
* * *
Resume it once `payment_pending` is back to normal, in INC-0412 at 13:15.

**Not written down yet:** the normal count, and the command or control that resumes the job.

### 6. Check refunds and hand over to Guest Support
* * *
Every booking that expired after a charge should have a psp-reconcile refund, possibly issued during the failure. In INC-0412 it refunded 71 captures at 12:45, and the other 23 were never charged.

Then send Guest Support the window's expired bookings with their references.

**Expected result:** every charged guest with an expired booking is refunded, and nobody was charged twice.

### Cleanup checks
* * *
*   [] **Webhooks accepted again** on `/v2/psp/webhooks`
*   [] **Failure window replayed** from first rejection to fix
*   [] **No booking from the window left** in `payment_pending`
*   [] **Expiry job resumed** in booking-service
*   [] **Expired captures refunded** by psp-reconcile, with no guest charged twice
*   [] **Expired bookings list sent** to Guest Support

### Boundaries and exceptions
* * *
*   **Other rejection reasons** — Step 3 covers only `signature_mismatch`, the one INC-0412 cause, while steps 1, 2 and 4 to 6 fit any cause
*   **Planned secret rotations** — The checklist now deploys the new secret to payments-service first, because the old order can repeat INC-0412

## Review follow-ups
* * *
The 2026-09-10 review found nothing alerted until Guest Support noticed 19 minutes in, and agreed these actions.

| Action | Owner | Status |
|--------|-------|--------|
| Page #payments-oncall when `payments.webhook.4xx_rate` is above 5% for 5 minutes | Karim | Done on 2026-09-10 |
| Checklist rotation order: new secret to payments-service before the payment provider | Elif | Done on 2026-09-10 |
| Accept old and new signing secrets for 1 hour during a rotation | Elif | proposed |
| Webhook failures runbook, linked from the Payments / Webhooks dashboard | Karim | Open |

**Status: Proposal — not current behavior.** payments-service doesn't yet accept both secrets, so no step relies on it.
