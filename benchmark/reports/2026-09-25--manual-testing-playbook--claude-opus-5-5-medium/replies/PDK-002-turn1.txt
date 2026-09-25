```markdown
I'll create a new document on handling payment webhook failures. I've read both files. They don't contradict each other: the 30-minute `payment_pending` expiry matches in both. Before I draft, I need the decisions below, all in one reply:

**1. Purpose, shape & audience:**
- A runbook for the next webhook failure (Guide). This would close the open follow-up "Runbook for webhook failures, linked from the Payments / Webhooks dashboard" (owner Karim)
- A post-mortem of INC-0412 (Narrative overview)
- Or a runbook that uses INC-0412 as its worked example
- Who reads it: Payments on-call engineers only, or Guest Support too for the handoff step?

**2. Scope of failures:**
- The notes only cover one failure: a 401 `signature_mismatch` on `/v2/psp/webhooks` after a secret rotation
- No source covers other failures, such as 5xx errors or timeouts in payments-service, other 4xx reasons, or an outage at the payment provider
- Should the doc stay limited to signature failures? If not, please send a source for the other failure types

**3. Authority & status:**
- The six steps in "What I did, in order" are Karim's account of one incident
- Should I write them as the team's agreed procedure (current), or as what was done in INC-0412 (history)?
- Who signs off the procedure: Karim, Elif or someone else?

**4. Missing operational detail:**
The notes name these steps but don't say how to do them:
- How to pause and resume the `payment_pending` expiry job in booking-service
- The psp-replay command and its parameters
- The dashboard link and the alert's name or route
- The number of `payment_pending` bookings that counts as "normal" before the expiry job is resumed

Can you send these? If not, I'll mark each one as not supplied and won't invent it.

**5. Prevention & proposals:**
- The rotation order is marked Done in the follow-ups: deploy the new secret to payments-service first, then switch it at the payment provider. Should the doc include it?
- The dual-secret window (accept both secrets for 1 hour) is marked "proposed" (owner Elif). Should I include it, labelled as a proposal, or leave it out?

**6. Guest remedy:**
- After INC-0412, Guest Support sent an apology email and offered the same room at the same price. Is that standard policy, or was it a one-off for this incident?
```

Export-equivalent path: `export/001 - doc-payment-webhook-failures-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality status: this is an intake question, so there's no document to score yet. Source check: the two files agree and neither overrides the other.

The notes back a runbook for signature failures well, but some parts are missing:
- **How-to detail:** they don't say how to pause the expiry job, run psp-replay or decide when to resume.
- **Other failure types:** no source covers them.
- **Status of the steps:** it's unclear whether Karim's steps are the agreed procedure or one person's account of one incident.

Once you answer, I'll draft the document as `002`.