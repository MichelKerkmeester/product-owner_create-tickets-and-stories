I've written the runbook as today's procedure. It follows the on-call engineer from the alert firing to the cleanup, and the review follow-ups are at the end.

Path: `export/002 - doc-payment-webhook-failures-runbook.md`
Verified: read-back succeeded; 127 lines
HVR self-scan: 0 hard blockers. Fixed: Oxford comma in step 1. Kept with reason: em dashes in the definition bullets (the `*   **Term** — definition` format ClickUp uses) and in the status notice (the status-label format).

**Check:** everything traces to the incident notes, with the company context used only for background · no conflicts between the two files · the guest apology emails are left out · the runbook uses the step-by-step guide layout and ClickUp formatting.

The runbook explains why a rejected webhook costs bookings: the 30-minute expiry, and the provider's retries spreading out over hours. It then has six numbered steps, from checking the dashboard to handing the expired bookings to Guest Support. Each step includes the INC-0412 timings and log lines as a worked example. The follow-up table keeps the statuses the incident notes recorded on 2026-09-10, and the dual-secret window is marked as a proposal, not something in place today.

**Gaps and additions to check:**
- **Missing details:** the notes say to run psp-replay, pause and resume the expiry job, open the dashboard and read the psp-reconcile output, but not how. The runbook marks each of these as not documented yet instead of guessing, so on-call can't run the steps word for word until someone adds the commands and links.
- **Other failure types:** the runbook says the notes only cover 401 `signature_mismatch` failures. Server errors, timeouts and the provider not sending at all have no documented cause or fix.
- **My additions, not in the notes:**
  - Why step 2 comes before finding the cause
  - The six-item quality checklist, which I built from the steps
  - The line saying the runbook doesn't restore expired bookings
  - Capitalising the dual-secret status from "proposed" to "Proposed"

  Tell me if you want any of them removed.