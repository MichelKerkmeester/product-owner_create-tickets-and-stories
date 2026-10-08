````markdown
# Payment webhook failures runbook

* * *

> Status: Current behavior — practice as recorded in the INC-0412 incident notes, reviewed on 2026-09-10 and not re-checked against the live system.

* * *

## Overview

* * *

This runbook is for whoever is on call in #payments-oncall when payments-service rejects webhooks from the payment provider. It takes you from the alert to cleanup. A Pay now booking waits in `payment_pending` until the provider's webhook confirms the payment, so a rejected webhook leaves the guest on the confirming screen and, after 30 minutes, expires the booking.

INC-0412 is the reference case. From 12:02 to 12:49 UTC on 2026-09-09, every webhook from the payment provider was rejected with a 401 for `signature_mismatch`. This runbook covers that reason only. The notes give no procedure for other reasons, so this runbook does not apply to them.

### Key terms

* * *

*   **payment_pending** — The booking state between Pay now and the payment provider's confirmation. A booking that stays here for 30 minutes expires
*   **Pay now** — The guest pays the full total at booking, and the payment provider charges the card
*   **psp-replay** — Replays webhook events for a time window. Used for events whose next provider retry is hours away
*   **psp-reconcile** — Runs every 15 minutes, reads captures from the payment provider's API rather than from webhooks, and refunds any capture whose booking has expired

## Response steps

* * *

Run the steps in order. Where INC-0412 recorded an outcome, the step gives it as the expected result.

### 1. Alert fires

* * *

The alert is `payments.webhook.4xx_rate` above 5% for 5 minutes, and it pages #payments-oncall. It was added after INC-0412, when no alert fired and Guest Support reported the problem 19 minutes in.

1. Acknowledge the page in #payments-oncall
2. Open the Payments / Webhooks dashboard and check the 4xx rate by reason
3. If the reason is anything other than `signature_mismatch`, stop following this runbook

Rejected webhooks log a line like this one:

```text
2026-09-09T12:02:07Z WARN payments-service webhook rejected path=/v2/psp/webhooks status=401 reason=signature_mismatch type=payment.captured
```

**Expected result:** The dashboard shows the 4xx rate by reason, and each rejected webhook logs `status=401` with `reason=signature_mismatch`.

### 2. Pause the expiry job

* * *

Pause the `payment_pending` expiry job in booking-service now, before the cause is known. Bookings expire 30 minutes after they enter `payment_pending`, so the first bookings from the window expire about half an hour after the first rejection. In INC-0412 the first expiries came at 12:32, and 94 bookings had expired by the time the job was paused at 12:36. The job kept expiring bookings until someone paused it by hand.

**Expected result:** The job expires no more bookings until it is resumed in step 5.

### 3. Find the cause

* * *

For `signature_mismatch`, the INC-0412 cause was that payments-service still checked signatures with the old secret after the provider had started signing with the new one.

The notes do not record how the cause was traced. Treat that method as unverified, and confirm it with Payments engineering before you rely on it.

Fix it by deploying the config with the new secret to payments-service. In INC-0412 the deploy reloaded `secret_version=2026q3`, and webhooks were accepted within 13 seconds:

```text
2026-09-09T12:49:31Z INFO payments-service config reloaded secret_version=2026q3
2026-09-09T12:49:44Z INFO payments-service webhook accepted path=/v2/psp/webhooks status=200 type=payment.captured
```

**Expected result:** The reload appears in the log, and webhooks are accepted with `status=200` in place of the 401 rejections.

### 4. Replay the window

* * *

Run psp-replay for the window from the first rejected webhook to the fix, which was 12:02 to 12:49 UTC in INC-0412. The provider retries a failed webhook up to 8 attempts over 24 hours, with a growing gap between attempts. A Pay now booking waits only 30 minutes, so the retries alone would have left guests waiting long after the fix.

**Expected result:** Bookings leave `payment_pending`. In INC-0412 the provider's retries began landing at 12:50, and the last booking from the window left the state at 13:12, 23 minutes after the fix.

### 5. Resume the expiry job

* * *

Resume the expiry job once the `payment_pending` count is back at its normal level. The notes give no figure for normal, so the on-call engineer judges it.

**Expected result:** In INC-0412 the job resumed at 13:15, after the last booking from the window had left the state at 13:12.

### 6. Cleanup

* * *

1. Check the psp-reconcile output for refunds of expired bookings
2. Give Guest Support the list of bookings that expired, with their booking references

psp-reconcile runs every 15 minutes and reads captures from the payment provider's API rather than from webhooks, so it keeps working while webhooks are rejected. It refunds any capture whose booking has expired.

**Expected result:** In INC-0412, 71 of the 94 expired bookings had been charged and were refunded. The other 23 had no successful charge.

## Before a secret rotation

* * *

Deploy the new secret to payments-service before switching it at the payment provider. In INC-0412 the provider switched first and payments-service switched second, which caused the rejections in step 1.

The notes also propose accepting both the old and the new signing secret for one hour during a rotation. That is a proposal, not current practice. See the follow-ups below.

## Review follow-ups

* * *

Statuses are as recorded in the INC-0412 notes on 2026-09-10. This runbook did not re-check them.

| Action | Owner | Status |
| --- | --- | --- |
| Alert when `payments.webhook.4xx_rate` is above 5% for 5 minutes, paging #payments-oncall | Karim | Done on 2026-09-10 |
| Rotation order in the checklist: deploy the new secret to payments-service before switching it at the payment provider | Elif | Done on 2026-09-10 |
| Accept both the old and the new signing secret for 1 hour during a rotation | Elif | Proposed, not current practice |
| Runbook for webhook failures, linked from the Payments / Webhooks dashboard | Karim | Open, and this document is the draft |
````

Export-equivalent path: export/NNN - doc-payment-webhook-failures-runbook.md

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: em dash in the status label and the definition bullets, under the ClickUp definition delimiter and status label exemptions.

Quality summary:
- Source safety: pass. Every step comes from the incident notes. The dual-secret window is labelled proposed, and the cause-tracing method is marked unverified.
- Shape fit: pass. Guide shape with ordered steps and expected results.
- ClickUp layout: pass.
- Readability: pass.
- Voice: pass.

Assumptions to check:
- **Scope:** I limited the runbook to `signature_mismatch`, because the two files describe no other failure reason. The alert pages on any 4xx, so step 1 says to stop for other reasons. To cover other failure types, I need a source for each.
- **Guest emails:** I left out the apology emails. I kept the step that gives Guest Support the list of expired bookings, since it is an operational handoff. Tell me if that should go too.
- **Names and statuses:** I kept the owner names from the notes. The statuses are as of 2026-09-10 and have not been re-checked.

The runbook follows INC-0412 from alert to cleanup, with an expected result after each step where the notes record one. The one step whose method the notes do not record is marked unverified.