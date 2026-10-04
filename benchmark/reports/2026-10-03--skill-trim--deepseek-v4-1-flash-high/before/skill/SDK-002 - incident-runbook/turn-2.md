Path: `export/002 - doc-payment-webhook-failure-runbook.md`

Verified: read-back succeeded; 98 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the em dash appears only inside the `*   **Term** — definition` shape, which Doc Mode grants, and the literal identifiers and supplied values are kept verbatim, `payments.webhook.4xx_rate`, `/v2/psp/webhooks`, `signature_mismatch`, `payment_pending`, `#payments-oncall`, the two log lines, and the status words `proposed`, `Open` and `Done on 2026-09-10`.

Quality summary
*   Source safety: pass. Every step and number traces to the incident notes; the context doc supplies only background, per your call. The dual-secret window stays proposal and the runbook row stays Open
*   Shape fit: pass. Guide shape for a reader who follows an order, scoped from the alert to the cleanup
*   ClickUp layout: pass. `* * *` dividers under every heading, `*   ` bullets, sentence-case headings, no spacer headings, no `---`, no hyphen bullets, no bullet ending in a full stop
*   Readability: pass. 1,151 words against a 1,400 budget, one idea per paragraph, steps in the recorded order
*   Voice: pass. No hard blockers and no always-cut modifiers left in place

The document opens with what the runbook is for and the INC-0412 instance, then runs six steps from the dashboard check to the cleanup and handoff to Guest Support, follows with boundaries and related guidance, and closes on the 2026-09-10 review actions with each one's standing. Guest apology emails and the wider guest-impact detail are left out as you asked, and step 6 stops at giving Guest Support the expired list.

Two additions of mine, so you can strike them: the six-step grouping and its headings are my structure around the notes' ordered action list, and the Boundaries items (retry gap, `psp-reconcile` independence, `psp-replay` and `psp-reconcile` left undefined by the notes) are drawn from statements in the notes rather than separate headings there. Say the word and I will adjust either, or push the runbook into ClickUp if you have that tooling connected.