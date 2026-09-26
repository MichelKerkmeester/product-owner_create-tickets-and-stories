# Payment webhook failures runbook

* * *
> Status: Current behavior — the Payments on-call procedure, from the INC-0412 incident notes and review of 2026-09-10. The review follow-ups carry their own status
* * *

## Overview
* * *
This runbook takes the #payments-oncall engineer from the webhook error alert to the last affected booking confirmed or refunded, when payments-service rejects provider webhooks.

In INC-0412, on 2026-09-09 from 12:02 to 12:49 UTC, payments-service answered every webhook with a 401 after a signing secret rotation. 1,284 bookings entered `payment_pending` in those 47 minutes, 1,190 recovered, and 94 expired before the expiry job was paused.

* * *

### Why a rejected webhook costs bookings
* * *
A Pay now booking learns its payment result only by webhook, so a rejection keeps it in `payment_pending`, even when charged. After 30 minutes booking-service expires it and resells the room, first at 12:32 in INC-0412.

The provider retries up to 8 attempts over 24 hours with growing gaps, so guests stay on the Confirming your booking screen unless webhooks are replayed.

psp-reconcile runs every 15 minutes from the provider's API rather than webhooks, and refunds any capture whose booking expired, so a charged guest gets their money back but loses the booking.

* * *

### Before you start
* * *
*   **Alert** — `payments.webhook.4xx_rate` above 5% for 5 minutes pages #payments-oncall
*   **Dashboard** — Payments / Webhooks, with the 4xx rate by reason
*   **Tools** — psp-replay, to replay a window of webhook events, and psp-reconcile
*   **Not documented yet** — the psp-replay commands, how to pause and resume the booking-service expiry job, the dashboard link and where psp-reconcile output is read

* * *

## Responding to the alert
* * *
Work in order. Step 2 comes before the cause because the expiry job keeps expiring bookings while you look.

* * *

### 1. Confirm the failure on the dashboard
* * *
Check the 4xx rate by reason on the Payments / Webhooks dashboard to guide step 3. In INC-0412 the rate was 100%, all 401s on `/v2/psp/webhooks` with reason `signature_mismatch`:

```text
2026-09-09T12:02:07Z WARN payments-service webhook rejected path=/v2/psp/webhooks status=401 reason=signature_mismatch type=payment.captured
```

Note the first rejection's time, which starts the step 4 replay window and the expiry clock.

* * *

### 2. Pause the `payment_pending` expiry job
* * *
Pause the `payment_pending` expiry job in booking-service once the failure is confirmed, because it does not stop by itself. Paused, bookings stay in `payment_pending` and can still confirm. In INC-0412 it was paused by hand at 12:36, after 94 had expired.

* * *

### 3. Find and fix the cause
* * *
Fix whatever makes payments-service reject webhooks, until the 401s stop and the logs show webhooks accepted.

*   **`signature_mismatch` after a secret rotation** — payments-service still checks the old secret, so deploy the config with the new one
*   **Any other reason** — the incident notes document no other cause or fix

In INC-0412 the cause was found at 12:41 and fixed at 12:49:

```text
2026-09-09T12:49:31Z INFO payments-service config reloaded secret_version=2026q3
2026-09-09T12:49:44Z INFO payments-service webhook accepted path=/v2/psp/webhooks status=200 type=payment.captured
```

Within a minute, provider retries start landing and bookings leave `payment_pending`.

* * *

### 4. Replay the missed webhooks with psp-replay
* * *
Run psp-replay for the whole failure window, from first rejection to fix, because most retries could be hours away. In INC-0412 it ran at 12:58 for 12:02 to 12:49, and the last booking left `payment_pending` at 13:12.

* * *

### 5. Resume the expiry job
* * *
Resume the expiry job once the `payment_pending` count is normal again, a level the incident notes do not give, since resuming earlier expires bookings still awaiting a webhook. In INC-0412 it resumed at 13:15, three minutes after the last booking left.

* * *

### 6. Check psp-reconcile and hand off to Guest Support
* * *
Confirm in psp-reconcile that every charged, expired booking was refunded, then give Guest Support the expired bookings list. In INC-0412, psp-reconcile refunded 71 of the 94 at 12:45, and the other 23 were never charged.

* * *

### Quality checks
* * *
*   [ ] **The 4xx rate is back to normal** on the dashboard, with webhooks logged at status 200
*   [ ] **The replay covered the full window**
*   [ ] **The `payment_pending` count is back to normal**
*   [ ] **The expiry job is running again**
*   [ ] **Every expired booking with a charge is refunded** in the psp-reconcile output
*   [ ] **Guest Support has the list of expired bookings**

* * *

### Boundaries and exceptions
* * *
*   **Covered failures** — 4xx rejections from payments-service, though the notes cover only `signature_mismatch` 401s, and nothing covers 5xx, timeouts or the provider not sending
*   **Expired bookings** — this runbook refunds charged guests through psp-reconcile but does not restore an expired booking
*   **Step details** — steps name the action but not the command, since the items under Before you start are missing

* * *

## Review follow-ups
* * *
The INC-0412 review on 2026-09-10 agreed four follow-ups, with status from the incident notes.

| Action | Owner | Status |
|--------|-------|--------|
| Alert when `payments.webhook.4xx_rate` is above 5% for 5 minutes, paging #payments-oncall | Karim | Done on 2026-09-10 |
| Rotation order in the checklist: deploy the new secret to payments-service before switching it at the payment provider | Elif | Done on 2026-09-10 |
| Accept both the old and the new signing secret for 1 hour during a rotation | Elif | Proposed |
| Runbook for webhook failures, linked from the Payments / Webhooks dashboard | Karim | Open |

The dual-secret window is a proposal, not current behavior. This runbook answers the last follow-up, still recorded as Open.
