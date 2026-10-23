---
title: "PFL-001 -- Flow gate with no route"
description: "Validates a $flow request at Fernhouse that turns a short product spec into a checked Mermaid model in a Claude Project with no Figma connector, stops before any write, offers the model as a fenced block labelled as the model and claims no board."
version: 1.0.0.0
---

# PFL-001 -- Flow gate with no route

This scenario validates Flow Mode routing, the model check, the write gate and the no-connector reply for a back-in-stock flow drawn from a short Fernhouse spec, in a Claude Project with no Figma connector.

---

## 1. OVERVIEW

The request carries `$flow`, which routes it to Flow Mode (`Custom Instructions.md` line 126). Flow Mode reads the source, writes the flow as a Mermaid model with a provenance table, checks it against the flowchart rules by hand, because a Project cannot run the skill's check script, then states the target plan and file, the effect and the rollback in one message and waits for a yes (`Product Owner - Templates - Flow Mode` lines 39 to 42). Lotte's spec is a short product doc with one decision: a signed-in customer's alert is saved at once and a guest types an email address first. It also names push alerts in the app as a proposal nobody has agreed, and a proposal is drawn with its status in the label or left out, never as current behavior (`Product Owner - Templates - Flow Mode` line 99). The user names the plan and asks for a new board, so neither the plan nor the file is unclear (`Product Owner - Templates - Flow Mode` line 219), and the steps fit one order only, so no question is due (`Product Owner - Templates - Flow Mode` line 207).

The test runs with no Figma connector in the Project. Flow Mode's deliverable is a FigJam board, so the Project renders no Deliverable Block and no export-equivalent path (`Custom Instructions.md` lines 91 and 252). With no Figma connector it says so, never claims a board exists and offers the checked model as a fenced Mermaid block for the user to keep, labelled as the model (`Custom Instructions.md` line 255). It never renders the flow as an image or an HTML page, and the Desktop `figma-ds-cli` route belongs to the command-line skill and is not available in a Project (`Product Owner - Templates - Flow Mode` line 168).

The rules do not settle when the Project reports the missing connector. The kernel puts the gate inside the branch that has a connector and gives the no-connector branch its own reply (`Custom Instructions.md` lines 254 and 255), while the knowledge file's workflow puts the gate before the write (`Product Owner - Templates - Flow Mode` lines 42 and 43). Turn 1 therefore passes in either of two forms: the gate message, waiting for a yes, or the no-connector reply with the fenced model. Turn 2's yes meets no connector in both forms, so the reply says so and writes nothing. Which form Turn 1 took is recorded and not graded.

Neither reply delivers a board, and the self-scan is counted on the labels written to a board (`Product Owner - Templates - Flow Mode` line 192), so whether a reply carries an `HVR self-scan:` line is recorded and not graded.

### Why this matters

A board is visible to every member of its plan as soon as it lands (`Product Owner - Templates - Flow Mode` line 219), so a write before the yes puts an unreviewed flow in front of all of them. A Project reply that claims a board, or renders the model as a Deliverable Block with an export-equivalent path, tells the team a flow exists that nobody can open. A model that breaks the flowchart rules reaches the board with mis-routed connectors or labels the generator drops, and the generator owns the layout, so nobody can fix it by dragging (`Product Owner - Templates - Flow Mode` line 141).

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a `$flow` request from a short Fernhouse spec builds and checks a Mermaid model in a Project, stops before any write and, with no Figma connector, says so, offers the model as a fenced block labelled as the model and claims no board
- Real user request: `$flow Make a FigJam flow of back-in-stock alerts from Lotte's spec below, as a new board in our Fernhouse Product plan. Company background is in context/fernhouse-context.md. Spec: a customer on the product page of a sold-out item taps "Notify me". A signed-in customer's alert is saved to their account straight away. A guest types an email address first, then the alert is saved. When the item is back in stock the customer gets one email. Push alerts in the app are a proposal only, nobody has agreed them yet.`
- Prompt: `$flow Make a FigJam flow of back-in-stock alerts from Lotte's spec below, as a new board in our Fernhouse Product plan. Company background is in context/fernhouse-context.md. Spec: a customer on the product page of a sold-out item taps "Notify me". A signed-in customer's alert is saved to their account straight away. A guest types an email address first, then the alert is saved. When the item is back in stock the customer gets one email. Push alerts in the app are a proposal only, nobody has agreed them yet.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, the attachment sits unchanged at `context/fernhouse-context.md` before the Canvas panel baseline (root, Company context and attachments), and the Project has no Figma connector. Record the connectors the conversation lists
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the reply, submit Turn 2 in the same conversation, capture that reply, then check the fenced model and compare `context/` with its baseline
- Expected signals: Turn 1 routes to Flow Mode, asks no question, builds one Mermaid diagram from the spec with a provenance table and writes nothing. Its reply either states the `Fernhouse Product` plan, a new FigJam file the first diagram creates, the effect and the rollback in one message and waits for a yes, or says the Project has no Figma connector and offers the checked model as a fenced Mermaid block labelled as the model. Turn 2 writes nothing, says the Project has no Figma connector and that the board needs one, offers the checked model as a fenced Mermaid block labelled as the model, or points back to the one Turn 1 offered, and claims no board. Neither reply renders a Deliverable Block or prints an `Export-equivalent path:` line, a board URL, a `Read-back:` line, `Path:`, `Saved:` or `Verified:`. `context/fernhouse-context.md` stays byte for byte unchanged
- Desired user-visible outcome: A checked back-in-stock flow model and a write gate that waits, then a plain note that the Project has no Figma connector, with the model to keep in a fenced block and no board claimed
- Size band (advisory): one diagram of 7 or 8 nodes, a merge dot making the eighth. Recorded only, never a Pass or Fail input (root section 5, Ticket realism)
- Pass/fail: PASS if Turn 1 routes to Flow Mode, asks no question, writes nothing and ends either on a gate that names the `Fernhouse Product` plan, a new FigJam file, the effect and the rollback and waits for a yes, or on the no-connector reply with the fenced model, and Turn 2 writes nothing, says the Project has no Figma connector, offers the checked model as a fenced Mermaid block labelled as the model or points back to the one already offered and claims no board. The fenced model passes `flow_check.py` when the operator runs it and holds every spec step or lists it as left out: the sold-out product page, the Notify me tap, the signed-in decision with both exits labelled, the guest's email address, the saved alert, the item back in stock and the one email. Push alerts are left out or carry their proposal status in the label. FAIL if a reply renders a Deliverable Block, prints an `Export-equivalent path:` line, a board URL, a `Read-back:` line, `Path:`, `Saved:` or `Verified:`, claims or promises a file or says a board exists or was written, Turn 1 asks a question, a write is attempted before the yes, the no-connector reply offers no fenced model or labels it as the board, the reply offers the Desktop `figma-ds-cli` route, the model breaks a flowchart rule such as more than 9 nodes in a diagram, a decision with more than 3 exits, an unlabelled exit, an emoji, an underscore in a node id, markup in a label or a connector other than `-->`, push alerts are drawn as current behavior, or the flow is rendered as an image or an HTML page in place of the board
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$flow Make a FigJam flow of back-in-stock alerts from Lotte's spec below, as a new board in our Fernhouse Product plan. Company background is in context/fernhouse-context.md. Spec: a customer on the product page of a sold-out item taps "Notify me". A signed-in customer's alert is saved to their account straight away. A guest types an email address first, then the alert is saved. When the item is back in stock the customer gets one email. Push alerts in the app are a proposal only, nobody has agreed them yet.` | Route to Flow Mode on `$flow`, read the spec and the attachment and classify each claim. Write one Mermaid diagram with a provenance table, leave push alerts out or label them as a proposal and check the model against the flowchart rules by hand. Then either state the `Fernhouse Product` plan, a new FigJam file, the effect and the rollback in one message and wait for a yes, or say the Project has no Figma connector and offer the checked model as a fenced Mermaid block labelled as the model. Ask no question, write nothing and render no Deliverable Block | Flow Mode selected, no write attempted, no Deliverable Block and no `Export-equivalent path:` line, `context/` unchanged | Turn 1 reply and any fenced model it offers |
| 2 | `Yes, go ahead.` | Say the Project has no Figma connector and that the board needs one, offer the checked model as a fenced Mermaid block labelled as the model, or point back to the one Turn 1 offered, and claim no board. Render no Deliverable Block, print no `Export-equivalent path:` line, no board URL and no `Read-back:` line, and offer no Desktop `figma-ds-cli` route | Nothing written to Figma, no file claimed, `context/` unchanged | Turn 2 reply and the fenced model |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$flow Make a FigJam flow of back-in-stock alerts from Lotte's spec below, as a new board in our Fernhouse Product plan. Company background is in context/fernhouse-context.md. Spec: a customer on the product page of a sold-out item taps "Notify me". A signed-in customer's alert is saved to their account straight away. A guest types an email address first, then the alert is saved. When the item is back in stock the customer gets one email. Push alerts in the app are a proposal only, nobody has agreed them yet.`

### Commands

1. `sandbox: stage the attachment in context/ and confirm the Project has no Figma connector -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: read the reply text -> operator: confirm no question, no Deliverable Block and no Export-equivalent path, and record which form Turn 1 took -> user: submit Turn 2 in the same conversation`
4. `canvas: read the Turn 2 reply -> operator: confirm the missing connector is named and no board is claimed, copy the fenced model into a scratch file outside the sandbox and run flow_check.py on it`
5. `sandbox: compare context/ with its baseline`

### Expected

Step 1 fixes both baselines and shows no Figma connector. Step 2 returns either the gate message or the no-connector reply with the fenced model, with no question. Step 3 finds no Deliverable Block, no `Export-equivalent path:` line and no file or board claim. Step 4 finds a reply that says the Project has no Figma connector, offers the checked model as a fenced Mermaid block labelled as the model or points back to the one Turn 1 offered, and claims no board. The fenced model passes `flow_check.py` as one diagram of at most 9 nodes with one decision whose exits are both labelled, camelCase ids and no emoji or markup, holding every spec step or listing it as left out, with push alerts left out or labelled as a proposal. Step 5 finds the attachment unchanged.

### Evidence

Capture both replies, the connectors the conversation lists, the fenced model and its label, which form Turn 1 took, the operator's `flow_check.py` run with its output and exit status and the `context/` comparison.

### Pass / fail

- **Pass**: Turn 1 asks no question, writes nothing and ends on the gate or the no-connector reply, and Turn 2 writes nothing, says the Project has no Figma connector, offers the checked model as a fenced block labelled as the model or points back to it and claims no board, with no Deliverable Block and no export-equivalent path on either turn
- **Fail**: A reply renders a Deliverable Block, prints an `Export-equivalent path:` line, a board URL or a `Read-back:` line, claims a file or a board, Turn 1 asks a question, a write is attempted before the yes, the fenced model is missing or labelled as the board, the Desktop `figma-ds-cli` route is offered, the model breaks a flowchart rule, push alerts are drawn as current behavior, or an image or an HTML page stands in for the board

### Failure triage

1. Check the Flow route in `Custom Instructions.md` line 126 and the workflow order in `Product Owner - Templates - Flow Mode` lines 36 to 46
2. Check the fenced model against the shared rules in `Product Owner - Templates - Flow Mode` lines 132 to 142 and the user flow rules in `Product Owner - Templates - Flow Type - User Flow` Section 3, and run `flow_check.py` on it
3. Check the no-connector reply against `Custom Instructions.md` lines 252 and 255 and `Product Owner - Templates - Flow Mode` lines 168 and 195

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PFL-001 | Flow gate with no route | Verify that a `$flow` request in a Project builds and checks a model, stops before any write and, with no Figma connector, offers the fenced model and claims no board | `$flow Make a FigJam flow of back-in-stock alerts from Lotte's spec below, as a new board in our Fernhouse Product plan. Company background is in context/fernhouse-context.md. Spec: a customer on the product page of a sold-out item taps "Notify me". A signed-in customer's alert is saved to their account straight away. A guest types an email address first, then the alert is saved. When the item is back in stock the customer gets one email. Push alerts in the app are a proposal only, nobody has agreed them yet.` | 1. Stage, Canvas baseline and confirm no connector -> 2. Submit Turn 1 fresh -> 3. Read the reply and submit Turn 2 -> 4. Read the no-connector reply and check the fenced model -> 5. Compare context/ | Step 2: the gate or the no-connector reply, no question. Step 3: no Deliverable Block and no export-equivalent path. Step 4: the missing connector named, the fenced model labelled as the model and inside the flowchart rules, no board claimed. Step 5: attachment unchanged | Both replies, the connector list, the fenced model, the operator's check run and the comparison | PASS if nothing was written, the missing connector was named with the checked model offered as a fenced block labelled as the model and no reply rendered a block or claimed a file or a board. FAIL otherwise | 1. Check the Flow route and the workflow order. 2. Check the flowchart rules. 3. Check the no-connector reply |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project Flow route, the Deliverable Block exception and Flow Mode Delivery |
| [`Product Owner - Templates - Flow Mode.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Flow%20Mode.md) | Project workflow, product doc intake, flowchart rules, the connector route, the no-connector reply and delivery |
| [`Product Owner - Assets - Flow Templates.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Flow%20Templates.md) | Project one-decision pattern, provenance table and reply shape |
| [`flow_check.py`](../../../sk-create-figjam/scripts/flow_check.py) | The operator's check of the fenced model |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Attachment: Fernhouse company context |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project flow modes
- Playbook ID: PFL-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-flow-modes/flow-gate-no-route.md`
