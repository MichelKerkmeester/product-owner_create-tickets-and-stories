Path: export/002 - doc-payment-webhook-failure-runbook.md
Verified: read-back succeeded; 102 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the em dash in the status label and the bold definition delimiters, both granted to Doc Mode.

Quality summary: Every time, count and log line traces to the incident notes, and the Doc gate clears. Each review follow-up shows the status the notes record, and the rows without a recorded status say so. The proposed dual-secret acceptance is labelled as a proposal.

The runbook follows the INC-0412 order from acknowledging the page through pausing the expiry job, fixing the cause, replaying, resuming and cleaning up. The notes leave the psp-replay command, the normal `payment_pending` level, the scope of the pause and any escalation path unknown, so the runbook lists those as open rather than inventing them. The apology emails are gone, and the two source files are unchanged.

Three things I added that you should strike if unwanted:

- Step 6 keeps the handoff of the expired-booking list to Guest Support. I read that as operational cleanup, not the apology emails.
- The instruction to raise any other cause in #payments-oncall instead of applying these steps by analogy is my addition.
- The Done when checklist is my addition, built from the notes' end state.