# Payment webhook failures runbook

* * *
> Status: Current behavior — the Payments on-call procedure, taken from the INC-0412 incident notes and review of 2026-09-10. The review follow-ups at the end carry their own status
* * *

## Overview
* * *
This runbook takes the engineer on call in #payments-oncall from the moment the webhook error alert fires to the moment the last affected booking is either confirmed or refunded. Follow it when payments-service starts rejecting webhooks from the payment provider, because every rejected webhook leaves a Pay now booking stuck in `payment_pending` while its 30-minute expiry clock keeps running.

The procedure comes from INC-0412. On 2026-09-09, from 12:02 to 12:49 UTC, payments-service answered every webhook with a 401 after a signing secret rotation. 1,284 bookings entered `payment_pending` in those 47 minutes. 1,190 recovered after the fix, and 94 expired before the expiry job was paused.

* * *

### Why a rejected webhook costs bookings
* * *
A Pay now booking learns its payment result only by webhook. When payments-service rejects the webhook, the booking cannot leave `payment_pending`, even when the guest's card was charged. After 30 minutes in `payment_pending`, booking-service expires the booking and puts its room back on sale. In INC-0412 the first bookings from the window expired at 12:32, 30 minutes after the first 401.

The payment provider's retries do not close that gap on their own. The provider retries a failed webhook up to 8 attempts over 24 hours, and the gap between attempts grows with each one. By the time the cause is fixed, most events are waiting on a later attempt, some of them hours away, so guests stay on the Confirming your booking screen long after the fix unless the missed webhooks are replayed.

psp-reconcile protects guests who were charged. It runs every 15 minutes and reads captures from the payment provider's API rather than from webhooks, so it keeps working during a webhook failure. It refunds any capture whose booking has expired, which means a charged guest whose booking expired gets their money back but loses the booking.

* * *

### Before you start
* * *
*   **Alert** — `payments.webhook.4xx_rate` above 5% for 5 minutes pages #payments-oncall
*   **Dashboard** — Payments / Webhooks, which shows the 4xx rate by reason
*   **Tools** — psp-replay replays webhook events for a time window, and psp-reconcile refunds captures on expired bookings
*   **Not documented yet** — the commands for psp-replay, the way to pause and resume the expiry job in booking-service, the dashboard link and where psp-reconcile output is read

* * *

## Responding to the alert
* * *
Work through the steps in order. Step 2 comes before finding the cause because the expiry job keeps expiring bookings for as long as you are still looking.

* * *

### 1. Confirm the failure on the dashboard
* * *
Open the Payments / Webhooks dashboard and check the 4xx rate by reason. The reason tells you where to look in step 3. In INC-0412 the rate was 100% and every rejection was a 401 on `/v2/psp/webhooks` with reason `signature_mismatch`. The payments-service logs showed the same:

```text
2026-09-09T12:02:07Z WARN payments-service webhook rejected path=/v2/psp/webhooks status=401 reason=signature_mismatch type=payment.captured
```

Note the time of the first rejection. It is the start of the window you replay in step 4, and it tells you when the first bookings will expire.

* * *

### 2. Pause the `payment_pending` expiry job
* * *
Pause the `payment_pending` expiry job in booking-service as soon as the failure is confirmed. The job does not stop by itself during a webhook failure. In INC-0412 it kept expiring bookings until it was paused by hand at 12:36, and 94 bookings had expired by then.

While the job is paused, bookings stay in `payment_pending` instead of expiring, so they can still confirm once their webhook arrives.

* * *

### 3. Find and fix the cause
* * *
Fix whatever makes payments-service reject the webhooks. The fix is done when the 401s stop and the logs show webhooks accepted again.

*   **`signature_mismatch` after a secret rotation** — payments-service is still checking signatures with the old secret while the payment provider signs with the new one. Deploy the config with the new secret. In INC-0412 that took from 12:41, when the cause was found, to 12:49
*   **Any other reason** — the incident notes document no other cause or fix

The logs from the INC-0412 fix show what recovery looks like:

```text
2026-09-09T12:49:31Z INFO payments-service config reloaded secret_version=2026q3
2026-09-09T12:49:44Z INFO payments-service webhook accepted path=/v2/psp/webhooks status=200 type=payment.captured
```

Within a minute of the fix, the payment provider's retries start landing and bookings begin to move out of `payment_pending`.

* * *

### 4. Replay the missed webhooks with psp-replay
* * *
Run psp-replay for the whole failure window, from the first rejection to the fix. The provider's retries only cover events whose next attempt happens to come soon, and the rest could be hours away. In INC-0412 psp-replay ran at 12:58 for 12:02 to 12:49, and the last booking from the window left `payment_pending` at 13:12.

* * *

### 5. Resume the expiry job
* * *
Resume the `payment_pending` expiry job once the `payment_pending` count is back to its normal level. Resuming earlier would expire bookings whose webhook is still on its way. In INC-0412 the job was resumed at 13:15, three minutes after the last booking from the window left `payment_pending`. The incident notes do not give a number for the normal level.

* * *

### 6. Check psp-reconcile and hand off to Guest Support
* * *
Check the psp-reconcile output to confirm that every charged guest whose booking expired has been refunded. Then give Guest Support the list of expired bookings, so they can follow up with those guests. In INC-0412, 71 of the 94 expired bookings had a charge that psp-reconcile refunded at 12:45, and the other 23 never had a successful charge.

* * *

### Quality checks
* * *
*   [ ] **The 4xx rate is back to normal** on the Payments / Webhooks dashboard, and the logs show webhooks accepted with status 200
*   [ ] **The replay covered the full window**, from the first rejection to the fix
*   [ ] **The `payment_pending` count is back to its normal level**
*   [ ] **The expiry job is running again**
*   [ ] **Every expired booking with a charge is refunded** in the psp-reconcile output
*   [ ] **Guest Support has the list of expired bookings**

* * *

### Boundaries and exceptions
* * *
*   **Covered failures** — webhooks rejected by payments-service with a 4xx. The incident notes cover 401s with reason `signature_mismatch` only, and no source covers 5xx errors, timeouts or the payment provider not sending webhooks
*   **Expired bookings** — this runbook refunds charged guests through psp-reconcile but does not restore an expired booking. Its room went back on sale when it expired
*   **Step details** — the commands and links listed as not documented under Before you start are still missing, so the steps name what to do but not the exact command

* * *

## Review follow-ups
* * *
The INC-0412 review on 2026-09-10 agreed four follow-ups. The status below is the one recorded in the incident notes.

| Action | Owner | Status |
|--------|-------|--------|
| Alert when `payments.webhook.4xx_rate` is above 5% for 5 minutes, paging #payments-oncall | Karim | Done on 2026-09-10 |
| Rotation order in the checklist: deploy the new secret to payments-service before switching it at the payment provider | Elif | Done on 2026-09-10 |
| Accept both the old and the new signing secret for 1 hour during a rotation | Elif | Proposed |
| Runbook for webhook failures, linked from the Payments / Webhooks dashboard | Karim | Open |

The dual-secret window is a proposal and not current behavior. This runbook is the document the last follow-up asks for, and it is still recorded as Open.
