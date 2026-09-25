---
title: "SDK-002 -- Incident runbook"
description: "Validates a $doc request at Roamstay through the five-field Doc intake question to a ClickUp runbook for payment webhook failures that keeps the dual-secret window proposed."
version: 1.0.0.0
---

# SDK-002 -- Incident runbook

This scenario validates the Doc intake question under an explicit command and an engineering runbook built from Roamstay's INC-0412 incident notes.

---

## 1. OVERVIEW

`$doc` routes the request and does not supply the Doc context, so the runtime still asks its question and waits (`AGENTS.md` line 287). Turn 1 names both attachments but states no reader, authority, status, shape or scope. `AGENTS.md` line 285 and `doc-mode.md` line 198 set the question's minimum: source set, authority, status, shape and scope, each unless the user already stated it. The notes' own follow-up list names a runbook, so the question may propose a Guide or runbook for the user to confirm (`doc-mode.md` line 260). Turn 2 asks for a runbook, which is the Guide shape (`doc-mode.md` line 264).

The notes mix statuses. The alert on `payments.webhook.4xx_rate` and the rotation order are done, while accepting the old and the new signing secret for `1 hour` during a rotation is only `proposed`. Turn 2 asks for today's process and for the follow-ups with where each one stands, so a correct runbook lists the dual-secret window as proposed and never gives it as a step.

### Why this matters

An on-call engineer follows a runbook while Pay now bookings expire after `30 minutes` in `payment_pending`. A step that leans on an unbuilt dual-secret window, or a command the notes never gave, costs real bookings in the one moment the document exists for.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the Doc intake question under `$doc` and a ClickUp runbook that follows the incident notes' procedure and keeps the proposed dual-secret window proposed
- Real user request: `We need a doc on handling payment webhook failures, like the INC-0412 outage. Start with context/roamstay-payment-webhook-incident-notes.md, and context/roamstay-context.md has the company background.`
- Prompt: `$doc We need a doc on handling payment webhook failures, like the INC-0412 outage. Start with context/roamstay-payment-webhook-incident-notes.md, and context/roamstay-context.md has the company background.`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-payment-webhook-incident-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-payment-webhook-incident-notes.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit unchanged at `context/roamstay-context.md` and `context/roamstay-payment-webhook-incident-notes.md` before the export baseline (root, Company context and attachments)
- Expected execution process: Start fresh, submit Turn 1, capture the consolidated question and its clarification export, answer in Turn 2, then inspect the next doc export and compare `context/` with its baseline
- Expected signals: Turn 1 routes to Doc Mode, asks one consolidated question covering source set, authority, status, shape and scope, exports `export/[###] - doc-payment-webhook-runbook-clarification.md`, reads it back and replies with its path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (root section 5, Clarification turns), and creates no draft. Turn 2 saves `export/[###] - doc-payment-webhook-runbook.md` on the next number as a Guide shaped as a runbook, reads it back and replies with the path, the `Verified:` line, the `HVR self-scan:` line and one summary line each for Source safety, Shape fit, ClickUp layout, Readability and Voice (`doc-mode.md` line 412). Both `context/` files stay byte for byte unchanged
- Desired user-visible outcome: One question that settles the doc before any drafting, then a runbook the Payments on-call engineer can follow from the alert to the cleanup
- Size band (advisory): 60 to 150 lines in the doc body. Recorded only, never a Pass or Fail input (root section 5, Ticket realism)
- Pass/fail: PASS if Turn 1 asks one consolidated question covering source set, authority, status, shape and scope, exports it in the doc lane and reads it back with no draft, and Turn 2 delivers a runbook with an Overview and a numbered procedure body, `* * *` directly under every content heading, `*   ` bullets, sentence-case headings and no empty spacer heading in the file, carries the notes' six steps with the `payment_pending` expiry job paused before the fix and resumed only once the `payment_pending` count is back to normal, keeps `payments.webhook.4xx_rate` above `5%` for `5 minutes` paging `#payments-oncall`, the `Payments / Webhooks` dashboard, the `30 minutes` expiry, `psp-replay` and `psp-reconcile` verbatim, ends with the follow-ups where the alert and the rotation order are done and the `1 hour` dual-secret window is `proposed`, and states nothing the two attachments do not. FAIL if Turn 1 drafts or leaves any of the five fields out of the question, or Turn 2 gives the dual-secret window as a step or as something that exists, alters a value, invents a command, flag, link, root cause or step outcome, names a vendor the notes call the payment provider, or writes `---` dividers or hyphen bullets
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$doc We need a doc on handling payment webhook failures, like the INC-0412 outage. Start with context/roamstay-payment-webhook-incident-notes.md, and context/roamstay-context.md has the company background.` | Route to Doc Mode, read both attachments, ask one consolidated question covering source set, authority, status, shape and scope, plus the purpose and audience the request left open, export it as a doc-lane clarification, read it back and wait. Create no draft | Doc Mode selected, no reader, shape or status assumed, both `context/` files unchanged | Turn 1 reply, clarification export, read-back line and clean draft ledger |
| 2 | `A runbook for whoever is on call in #payments-oncall, from the alert firing to the cleanup. Those two files are all there is, the incident notes govern and the context doc is background only. Write it as what we do today, list the review follow-ups at the end with where each one stands, and leave out the guest apology emails.` | Build the runbook from the incident notes as a Guide, number the steps in the notes' order, keep every identifier, threshold and timer exact, mark a step whose outcome the notes do not give as unverified, list the follow-ups with their statuses, apply the ClickUp layout, save the next doc export, read it back and reply with the path, the `Verified:` line, the `HVR self-scan:` line and the five-line Doc summary | The dual-secret window stays proposed, and no step relies on it | Turn 2 reply, exported runbook and read-back line |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$doc We need a doc on handling payment webhook failures, like the INC-0412 outage. Start with context/roamstay-payment-webhook-incident-notes.md, and context/roamstay-context.md has the company background.`

### Commands

1. `sandbox: stage both attachments in context/ -> filesystem: record the export and context/ baselines`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question and covers the five Doc fields -> user: submit Turn 2 in the same session`
4. `filesystem: open the new doc export -> operator: check the shape, the ClickUp layout, the step order, every identifier and the follow-up statuses against context/roamstay-payment-webhook-incident-notes.md`
5. `filesystem: compare context/ with its baseline`

### Expected

Step 1 fixes both baselines. Step 2 returns one consolidated question and one clarification file in the doc lane. Step 3 proves the wait state and that no draft exists. Step 4 finds a runbook with an Overview and a numbered procedure body, the Guide's `## Process` that `doc-templates.md` line 232 lets it rename (lines 115 and 187), `* * *` directly under each content heading, `*   ` bullets, sentence-case headings and no empty spacer heading, since a file export never carries one (`doc-mode.md` line 97). The six steps keep the notes' order: open the `Payments / Webhooks` dashboard and check the 4xx rate by reason, pause the `payment_pending` expiry job in booking-service, fix the cause, run `psp-replay` for the window, resume the expiry job once the `payment_pending` count is normal, then check the `psp-reconcile` output and hand Guest Support the expired bookings. A step whose outcome the notes do not give is marked unverified rather than given an invented one (`doc-templates.md` line 237). Any figure from INC-0412 it cites keeps its value, such as `1,284` in the window, `1,190` recovered, `94` expired and `71` refunded, and any retry claim keeps `8 attempts` over `24 hours`. The follow-ups close the doc with the alert and the rotation order done and the `1 hour` dual-secret window `proposed`. Step 5 finds both attachments unchanged.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back lines, the fields the question covers, the doc headings with divider adjacency, the bullet markers, the numbered steps in order, every identifier and threshold, the follow-up statuses, the Doc quality summary and the `context/` comparison.

### Pass / fail

- **Pass**: Turn 1 asks one consolidated question covering source set, authority, status, shape and scope, exported in the doc lane and read back, with no early draft, and the runbook carries an Overview and a numbered procedure in the notes' order, passes the ClickUp layout gate, keeps every identifier, threshold and timer verbatim and lists the dual-secret window as proposed
- **Fail**: Turn 1 drafts or leaves one of the five fields out, or the runbook tells on-call to rely on the dual-secret window or lists it as done, resumes the expiry job before the `payment_pending` count is normal, invents a command, flag, link, root cause or step outcome, gives a vendor name where the notes say the payment provider, alters a value such as `5%`, `30 minutes` or `/v2/psp/webhooks`, or writes `---` dividers, hyphen bullets or empty spacer headings into the file

### Failure triage

1. Check the explicit-command rule in `AGENTS.md` line 287 and the minimum question fields in `AGENTS.md` line 285 and `doc-mode.md` line 198
2. Compare the question with the Doc Context and Clarification Question in `interactive-response-templates.md` line 129
3. Re-read the runbook against `context/roamstay-payment-webhook-incident-notes.md`, restore the step order and every exact value, and put the proposed label back on the dual-secret window (`AGENTS.md` line 126, `doc-mode.md` line 154)

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SDK-002 | Incident runbook | Verify the Doc intake question under a command and a runbook for payment webhook failures that keeps the dual-secret window proposed | `$doc We need a doc on handling payment webhook failures, like the INC-0412 outage. Start with context/roamstay-payment-webhook-incident-notes.md, and context/roamstay-context.md has the company background.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the doc export -> 5. Compare context/ | Step 2: one five-field question in the doc lane. Step 3: no draft. Step 4: runbook with the ClickUp layout, the six steps in order, exact identifiers and the dual-secret window proposed. Step 5: attachments unchanged | Both replies, ledger, export paths, read-back lines, layout checks, step order, identifiers and follow-up statuses | PASS if the question covers all five fields with no draft and the runbook keeps its sections, the layout, the step order, every value and the proposed label. FAIL otherwise | 1. Check the Doc intake. 2. Check the question. 3. Check steps, values and statuses |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Explicit-command intake rule, the Doc escalation question and the export protocol |
| [`doc-mode.md`](../../references/doc-mode.md) | Doc intake minimum, runbook as a Guide, source classification and ClickUp output contract |
| [`doc-templates.md`](../../assets/doc-templates.md) | Guide shape, the unverified-step rule and layout rules |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Doc Context and Clarification Question wording |
| [`roamstay-context.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Attachment: Roamstay company context |
| [`roamstay-payment-webhook-incident-notes.md`](../../../benchmark/fixtures/companies/roamstay/roamstay-payment-webhook-incident-notes.md) | Attachment: INC-0412 timeline, recovery steps and follow-ups with the proposed dual-secret window |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill document modes
- Playbook ID: SDK-002
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-document-modes/incident-runbook.md`
