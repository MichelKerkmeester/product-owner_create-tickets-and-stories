# Payment webhook failures doc: questions before drafting

I'll write a new document from the INC-0412 notes and the Roamstay company context. The two sources agree on every figure I checked, so there is no conflict to settle. Before I draft, I need the decisions below in one reply:

**Purpose & audience:** Who reads this and what do they do with it? My reading is a runbook for whoever is on call in #payments-oncall, linked from the Payments / Webhooks dashboard, which would close Karim's open follow-up. The other option is an explainer for readers outside Payments, like Dario at the review. Which one, or both?

**Scope:** The notes cover one failure type: 401s with reason `signature_mismatch` after a secret rotation. "Payment webhook failures" could also mean 5xx or timeouts from payments-service, or the payment provider not sending at all, and no source covers those. Should I:
- Keep the doc to 4xx and signature failures only
- Cover the other failure types, if you send a source for them
- Name them in the doc as not yet documented

**Status & authority:** The six steps in "What I did, in order" are what Karim did once, on 2026-09-09. Can the doc present them as the Payments procedure for every webhook failure? Or should it carry a draft status until Karim or Elif confirms them? This matters most for step 2: the `payment_pending` expiry job belongs to booking-service. Is Payments on-call allowed to pause it without the Booking squad?

**Missing operational detail:** The notes name psp-replay, psp-reconcile, the expiry job and the dashboard, but not how to run, pause or open any of them. Can you send commands, links or owners? If not, I'll mark each gap as unknown in the doc and won't fill it in.

**Proposals & history:** Should the doc include these, and how?
- The dual-secret window (accept both secrets for 1 hour during a rotation) is still proposed. Should the doc include it as a labelled proposal, or leave it out?
- Should INC-0412 appear as a worked example with its timeline, or only as a link back to the incident notes?

**Shape:** For an on-call reader I'd write a Guide: detection, triage by 4xx reason, the recovery steps in order, then guest follow-up with Guest Support. Confirm that, or name another shape (Behavior reference, Narrative overview or Proposal).
