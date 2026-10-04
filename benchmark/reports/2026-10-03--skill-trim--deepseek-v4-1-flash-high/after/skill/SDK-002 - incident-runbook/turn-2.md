Path: `export/002 - doc-payment-webhook-runbook.md`

Verified: read-back succeeded; 106 lines

HVR self-scan: 1 hard blocker. Fixed: one Oxford comma in the INC-0412 recovery numbers. Kept with reason: em dashes in the `*   **Term** — definition` bullets, the delimiter ClickUp grants.

Quality summary
- Source safety: pass - the dual-secret window stays proposed, no vendor is named, every value is verbatim, no command or step outcome invented, and both `context/` files are byte-identical to their supplied hashes
- Shape fit: pass - Guide shaped as a runbook, an Overview plus a numbered procedure, the notes' six steps in order with the expiry job paused before the fix and resumed only once the count is normal
- ClickUp layout: pass - `* * *` directly under every content heading, `*   ` bullets, `*   []` checklists, sentence-case headings, no `---` dividers, no hyphen bullets, no spacer headings
- Readability: pass - one idea per paragraph, and each step carries an expected result and a worked example rather than mixed prose
- Voice: pass - 0 hard violations on the lint, 1,179 words against the 1,400 budget

The runbook follows on-call from the alert firing to the cleanup, and every claim traces to the incident notes, with the company context used only for background. The dual-secret window appears once, in the Follow-ups table, marked `proposed` and explicitly not in place, so no step depends on it.

Additions to check, none of them in the notes:
- The five-item Quality checks list, built from the six steps
- Why step 2 pauses the expiry job before step 3 finds the cause
- The Boundaries lines saying the steps refund rather than restore an expired booking, and that the how-to commands are not written down yet
- The "What this does not cover" line naming server errors, timeouts and a provider that sends nothing

Tell me if you want any of them removed or reworded.