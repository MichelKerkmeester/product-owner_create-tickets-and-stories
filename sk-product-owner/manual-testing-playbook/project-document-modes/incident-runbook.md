---
title: "PDK-002 -- Incident runbook"
description: "Validates a $doc request at Roamstay through the Project's five-field Doc intake question to a ClickUp runbook Deliverable Block for payment webhook failures that keeps the dual-secret window proposed."
version: 1.0.0.0
---

# PDK-002 -- Incident runbook

This scenario validates the Doc intake question under an explicit command and an engineering runbook built from Roamstay's INC-0412 incident notes in a Claude Project.

---

## 1. OVERVIEW

`$doc` routes the request and does not supply the Doc context, so the Project still asks its question and waits (`Custom Instructions.md` line 108). Turn 1 names both attachments but states no reader, authority, status, shape or scope. `Custom Instructions.md` line 130 and `Product Owner - Templates - Doc Mode` line 174 set the question's minimum: source set, authority, status, shape and scope, each unless the user already stated it. The notes' own follow-up list names a runbook, so the question may propose a Guide or runbook for the user to confirm (`Product Owner - Templates - Doc Mode` line 236). Turn 2 asks for a runbook, which is the Guide shape (`Custom Instructions.md` line 122). The final runbook renders as its own block with an export-equivalent label and no file claim.

The notes mix statuses. The alert on `payments.webhook.4xx_rate` and the rotation order are done, while accepting the old and the new signing secret for `1 hour` during a rotation is only `proposed`. Turn 2 asks for today's process and for the follow-ups with where each one stands, so a correct runbook lists the dual-secret window as proposed and never gives it as a step.

### Why this matters

An on-call engineer follows a runbook while Pay now bookings expire after `30 minutes` in `payment_pending`. A step that leans on an unbuilt dual-secret window, or a command the notes never gave, costs real bookings in the one moment the document exists for.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the Doc intake question under `$doc` and a ClickUp runbook that follows the incident notes' procedure and keeps the proposed dual-secret window proposed
- Real user request: `We need a doc on handling payment webhook failures, like the INC-0412 outage. Start with context/roamstay-payment-webhook-incident-notes.md, and context/roamstay-context.md has the company background.`
- Prompt: `$doc We need a doc on handling payment webhook failures, like the INC-0412 outage. Start with context/roamstay-payment-webhook-incident-notes.md, and context/roamstay-context.md has the company background.`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-payment-webhook-incident-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-payment-webhook-incident-notes.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and both attachments sit unchanged at `context/roamstay-context.md` and `context/roamstay-payment-webhook-incident-notes.md` before the Canvas panel baseline (root, Company context and attachments)
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the consolidated question and its clarification block, answer in Turn 2, then inspect the rendered runbook and compare `context/` with its baseline
- Expected signals: Turn 1 routes to Doc Mode, asks one consolidated question covering source set, authority, status, shape and scope, renders it as its own clarification block with `Export-equivalent path: export/[NNN] - doc-payment-webhook-runbook-clarification.md` and the `HVR self-scan:` line (root section 5, Clarification turns), claims no file and creates no draft. Turn 2 renders the runbook as its own block under `Export-equivalent path: export/[NNN] - doc-payment-webhook-runbook.md`, then replies with the `HVR self-scan:` line and one summary line each for Source safety, Shape fit, ClickUp layout, Readability and Voice (`Custom Instructions.md` line 217), and claims no file. Both `context/` files stay byte for byte unchanged
- Desired user-visible outcome: One question that settles the doc before any drafting, then a runbook block the Payments on-call engineer can follow from the alert to the cleanup
- Size band (advisory): 60 to 150 lines in the doc body. Recorded only, never a Pass or Fail input (root section 5, Ticket realism)
- Pass/fail: PASS if Turn 1 asks one consolidated question covering source set, authority, status, shape and scope, rendered as its own block with a doc-lane clarification label and no draft, and Turn 2 renders a runbook with an Overview and a numbered procedure body, `* * *` directly under every content heading, `*   ` bullets and sentence-case headings, carries the notes' six steps with the `payment_pending` expiry job paused before the fix and resumed only once the `payment_pending` count is back to normal, keeps `payments.webhook.4xx_rate` above `5%` for `5 minutes` paging `#payments-oncall`, the `Payments / Webhooks` dashboard, the `30 minutes` expiry, `psp-replay` and `psp-reconcile` verbatim, ends with the follow-ups where the alert and the rotation order are done and the `1 hour` dual-secret window is `proposed`, states nothing the two attachments do not and claims no file. FAIL if Turn 1 drafts or leaves any of the five fields out of the question, or Turn 2 gives the dual-secret window as a step or as something that exists, alters a value, invents a command, flag, link, root cause or step outcome, names a vendor the notes call the payment provider, writes `---` dividers or hyphen bullets, or prints `Path:`, `Saved:` or `Verified:` and claims a save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$doc We need a doc on handling payment webhook failures, like the INC-0412 outage. Start with context/roamstay-payment-webhook-incident-notes.md, and context/roamstay-context.md has the company background.` | Route to Doc Mode, read both attachments, ask one consolidated question covering source set, authority, status, shape and scope, plus the purpose and audience the request left open, render it as a doc-lane clarification block with its export-equivalent label and wait. Create no draft | Doc Mode selected, no reader, shape or status assumed, both `context/` files unchanged | Turn 1 reply, rendered clarification block and the no-file-write statement |
| 2 | `A runbook for whoever is on call in #payments-oncall, from the alert firing to the cleanup. Those two files are all there is, the incident notes govern and the context doc is background only. Write it as what we do today, list the review follow-ups at the end with where each one stands, and leave out the guest apology emails.` | Render the runbook from the incident notes as a Guide, number the steps in the notes' order, keep every identifier, threshold and timer exact, mark a step whose outcome the notes do not give as unverified, list the follow-ups with their statuses, apply the ClickUp layout, then reply with the export-equivalent label, the `HVR self-scan:` line and the five-line Doc summary. Claim no file | The dual-secret window stays proposed, and no step relies on it | Turn 2 reply, rendered runbook block and its labels |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$doc We need a doc on handling payment webhook failures, like the INC-0412 outage. Start with context/roamstay-payment-webhook-incident-notes.md, and context/roamstay-context.md has the company background.`

### Commands

1. `sandbox: stage both attachments in context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question and covers the five Doc fields -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered runbook -> operator: check the shape, the ClickUp layout, the step order, every identifier, the follow-up statuses and the export-equivalent label against context/roamstay-payment-webhook-incident-notes.md`
5. `sandbox: compare context/ with its baseline`

### Expected

Step 1 fixes both baselines. Step 2 returns one consolidated question as its own clarification block. Step 3 proves the wait state and that no draft exists. Step 4 finds a runbook with an Overview and a numbered procedure body, the Guide's `## Process` that `Product Owner - Assets - Doc Templates` line 211 lets it rename (lines 94 and 166), `* * *` directly under each content heading, `*   ` bullets and sentence-case headings. The six steps keep the notes' order: open the `Payments / Webhooks` dashboard and check the 4xx rate by reason, pause the `payment_pending` expiry job in booking-service, fix the cause, run `psp-replay` for the window, resume the expiry job once the `payment_pending` count is normal, then check the `psp-reconcile` output and hand Guest Support the expired bookings. A step whose outcome the notes do not give is marked unverified rather than given an invented one (`Product Owner - Assets - Doc Templates` line 216). Any figure from INC-0412 it cites keeps its value, such as `1,284` in the window, `1,190` recovered, `94` expired and `71` refunded, and any retry claim keeps `8 attempts` over `24 hours`. The follow-ups close the doc with the alert and the rotation order done and the `1 hour` dual-secret window `proposed`. Spacer headings are not graded here. The skill twin fails them because a file export never carries one, and `Product Owner - Templates - Doc Mode` line 73 allows them in ClickUp-bound content, which the kernel does not say a rendered block is. Step 5 finds both attachments unchanged.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the fields the question covers, the doc headings with divider adjacency, the bullet markers, the numbered steps in order, every identifier and threshold, the follow-up statuses, the Doc quality summary and the `context/` comparison.

### Pass / fail

- **Pass**: Turn 1 asks one consolidated question covering source set, authority, status, shape and scope, rendered as a doc-lane clarification block, with no early draft, and the rendered runbook carries an Overview and a numbered procedure in the notes' order, passes the ClickUp layout gate, keeps every identifier, threshold and timer verbatim, lists the dual-secret window as proposed and claims no file
- **Fail**: Turn 1 drafts or leaves one of the five fields out, or the runbook tells on-call to rely on the dual-secret window or lists it as done, resumes the expiry job before the `payment_pending` count is normal, invents a command, flag, link, root cause or step outcome, gives a vendor name where the notes say the payment provider, alters a value such as `5%`, `30 minutes` or `/v2/psp/webhooks`, writes `---` dividers or hyphen bullets, or the reply claims a local save

### Failure triage

1. Check the explicit-command rule in `Custom Instructions.md` line 108 and the Doc intake minimum in `Custom Instructions.md` line 130 and `Product Owner - Templates - Doc Mode` line 174
2. Compare the block with the Doc Context and Clarification Question in `Product Owner - Assets - Interactive Response Templates` line 106
3. Re-read the rendered runbook against `context/roamstay-payment-webhook-incident-notes.md`, restore the step order and every exact value, and put the proposed label back on the dual-secret window (`Custom Instructions.md` line 134, `Product Owner - Templates - Doc Mode` line 130)

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PDK-002 | Incident runbook | Verify the Doc intake question under a command and a runbook for payment webhook failures that keeps the dual-secret window proposed in a Project | `$doc We need a doc on handling payment webhook failures, like the INC-0412 outage. Start with context/roamstay-payment-webhook-incident-notes.md, and context/roamstay-context.md has the company background.` | 1. Stage and Canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the runbook block -> 5. Compare context/ | Step 2: one five-field question as its own block. Step 3: no draft. Step 4: runbook with the ClickUp layout, the six steps in order, exact identifiers, the dual-secret window proposed and the label. Step 5: attachments unchanged | Both replies, rendered blocks, labels, layout checks, step order, identifiers and follow-up statuses | PASS if the question covers all five fields with no draft and the block keeps its sections, the layout, the step order, every value and the proposed label with no file claim. FAIL otherwise | 1. Check the Doc intake. 2. Check the clarification block. 3. Check steps, values and statuses |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project explicit-command rule, Doc intake minimum, Deliverable Block and export-equivalent contract |
| [`Product Owner - Templates - Doc Mode - v0.110.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Doc%20Mode%20-%20v0.110.md) | Project Doc intake minimum, source classification and ClickUp output contract |
| [`Product Owner - Assets - Doc Templates - v0.107.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Doc%20Templates%20-%20v0.107.md) | Project Guide shape, the unverified-step rule and layout rules |
| [`Product Owner - Assets - Interactive Response Templates - v0.102.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates%20-%20v0.102.md) | Project Doc Context and Clarification Question wording |
| [`roamstay-context.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Attachment: Roamstay company context |
| [`roamstay-payment-webhook-incident-notes.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-payment-webhook-incident-notes.md) | Attachment: INC-0412 timeline, recovery steps and follow-ups with the proposed dual-secret window |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project document modes
- Playbook ID: PDK-002
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-document-modes/incident-runbook.md`
