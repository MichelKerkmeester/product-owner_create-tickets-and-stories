# INC-0412, payment webhooks rejected after a secret rotation

Source: incident notes in the Payments squad space, written up from the #payments-oncall channel and the payments-service logs
Written by Karim, Backend Engineer, Payments, on call that day. First draft on 2026-09-09, updated after the incident review on 2026-09-10

## Summary

On 2026-09-09, from 12:02 to 12:49 UTC, payments-service answered every webhook from the payment provider with a 401. That's 47 minutes. Pay now bookings kept coming in, but none of them could leave `payment_pending`, because the payment result reaches us by webhook.

1,284 bookings entered `payment_pending` in the window. 1,190 recovered after the fix, through the payment provider's own retries and a replay with psp-replay. 94 expired after 30 minutes in `payment_pending`, before I paused the expiry job. Of those 94, 71 guests had been charged and psp-reconcile refunded them. The other 23 never had a successful charge.

## Timeline (UTC)

| Time | What happened |
|------|---------------|
| 12:02 | Planned rotation of the webhook signing secret. The payment provider starts signing with the new secret. Our config change with the new secret is merged but not yet deployed |
| 12:02 | First 401 on `/v2/psp/webhooks`, reason `signature_mismatch` |
| 12:21 | Guest Support posts in #payments-oncall: guests stuck on the Confirming your booking screen |
| 12:24 | I acknowledge and open the Payments / Webhooks dashboard. 4xx rate at 100%. No alert had fired |
| 12:32 | First bookings from the window expire |
| 12:36 | I pause the `payment_pending` expiry job in booking-service. 94 bookings had expired by then |
| 12:41 | Cause found: payments-service still checks signatures with the old secret |
| 12:45 | psp-reconcile refunds 71 captures whose booking had expired |
| 12:49 | Config deployed with the new secret. The 401s stop |
| 12:50 | The payment provider's retries start landing and bookings move out of `payment_pending` |
| 12:58 | psp-replay run for 12:02 to 12:49, for events whose next retry was still hours away |
| 13:12 | Last booking from the window leaves `payment_pending`. 1,190 recovered in total |
| 13:15 | Expiry job resumed |

## From the logs

```text
2026-09-09T12:02:07Z WARN payments-service webhook rejected path=/v2/psp/webhooks status=401 reason=signature_mismatch type=payment.captured
2026-09-09T12:02:09Z WARN payments-service webhook rejected path=/v2/psp/webhooks status=401 reason=signature_mismatch type=payment.captured
2026-09-09T12:32:05Z INFO booking-service booking expired state=payment_pending age_s=1800 ref=RS-4HX29P
2026-09-09T12:49:31Z INFO payments-service config reloaded secret_version=2026q3
2026-09-09T12:49:44Z INFO payments-service webhook accepted path=/v2/psp/webhooks status=200 type=payment.captured
```

## Why the retries didn't save everyone

The payment provider retries a failed webhook up to 8 attempts over 24 hours, and the gap grows with each attempt. That covers most outages, but a Pay now booking only waits 30 minutes in `payment_pending`. By 12:49 most events were waiting on a later attempt, some of them hours away, so the retries alone would have left guests on the confirming screen long after the fix. That's why I ran psp-replay for the whole window.

psp-reconcile runs every 15 minutes and reads captures from the payment provider's API, not from webhooks, so it kept working through the incident. It refunds any capture whose booking has expired.

## What I did, in order

1. Opened the Payments / Webhooks dashboard and checked the 4xx rate by reason
2. Paused the `payment_pending` expiry job in booking-service
3. Found and fixed the cause, here by deploying the new secret
4. Ran psp-replay for the window
5. Resumed the expiry job once the `payment_pending` count was back to its normal level
6. Checked the psp-reconcile output and gave Guest Support the list of expired bookings

## Guest impact

- 94 guests lost their booking. 71 of them were charged and refunded by psp-reconcile on the same afternoon
- Guest Support emailed all 94 on 2026-09-10 with an apology and the same room at the same price where it was still free
- Nobody was charged twice

## Review on 2026-09-10

Present: Karim, Elif (Engineering Manager, Payments), Maren (Guest Support), Dario (Search, as the outside reader).

- We found out from Guest Support, 19 minutes in. Nothing watched the webhook error rate
- The rotation switched the payment provider first and our side second
- The expiry job kept expiring bookings until someone paused it by hand
- Elif to write up a dual-secret window for rotations

## Follow-ups

| Action | Owner | Status |
|--------|-------|--------|
| Alert when `payments.webhook.4xx_rate` is above 5% for 5 minutes, paging #payments-oncall | Karim | Done on 2026-09-10 |
| Rotation order in the checklist: deploy the new secret to payments-service before switching it at the payment provider | Elif | Done on 2026-09-10 |
| Accept both the old and the new signing secret for 1 hour during a rotation | Elif | proposed |
| Runbook for webhook failures, linked from the Payments / Webhooks dashboard | Karim | Open |
