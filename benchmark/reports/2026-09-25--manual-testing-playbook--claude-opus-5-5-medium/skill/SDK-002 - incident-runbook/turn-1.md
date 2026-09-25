I have a few questions before I write the doc. I haven't drafted anything yet, and I saved the questions to a file.

Path: `export/001 - doc-payment-webhook-failures-clarification.md`
Verified: read-back succeeded; 21 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Check:** no conflicts between the two files · the incident notes don't cover some of what the doc would need · no draft or answers in the file.

The two files agree on every number and time I checked. The problem is how far they go. They describe one kind of failure: 401 rejections because the signing secret didn't match, after the secret was changed. What's missing:

- **Other failures:** "payment webhook failures" could also mean server errors, timeouts or the payment provider not sending at all. Nothing you gave me covers those.
- **Status of the steps:** Karim's six steps are what he did during one incident. They haven't been confirmed as the team's procedure. That matters most for pausing the booking expiry job, which belongs to the Booking squad's booking-service.
- **How-to detail:** the notes say to run psp-replay, check psp-reconcile, pause the expiry job and open the dashboard. They don't say how.

The file asks you to settle these points in one reply:

1. Who the doc is for. My guess is a runbook for the Payments on-call engineer, which is Karim's open follow-up.
2. Whether to cover only signature failures or other failure types too.
3. Whether the steps count as the agreed procedure or as a draft.
4. How to run each tool.
5. Whether to include the proposed plan to accept both secrets for an hour during a change, as a labelled proposal.
6. Whether to include the INC-0412 timeline as an example.
7. Whether you agree the doc should be a step-by-step guide.

Once you answer, the doc will be saved as `002`.