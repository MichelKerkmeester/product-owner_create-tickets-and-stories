---
title: "SFL-001 -- Flow gate with no route"
description: "Validates a $flow request at Fernhouse that turns a short product spec into a checked Mermaid model, stops before any write and, with no Figma route connected, names the missing route, offers the checked model and claims no board."
version: 1.0.0.0
---

# SFL-001 -- Flow gate with no route

This scenario validates Flow Mode routing, the pre-write check, the write gate and the missing-route reply for a back-in-stock flow drawn from a short Fernhouse spec, in a runtime with no Figma route.

---

## 1. OVERVIEW

The request carries `$flow`, which routes it to Flow Mode (`AGENTS.md` line 222, `SKILL.md` line 57). Flow Mode reads the source, writes the flow as a Mermaid model with a provenance table, runs `sk-create-figjam/scripts/flow_check.py` on it, then states the target plan and file, the effect and the rollback in one message and waits for a yes (`flow-mode.md` lines 62 to 65). Lotte's spec is a short product doc with one decision: a signed-in customer's alert is saved at once and a guest types an email address first. It also names push alerts in the app as a proposal nobody has agreed, and a proposal is drawn with its status in the label or left out, never as current behavior (`flow-mode.md` line 122). The user names the plan and asks for a new board, so neither the plan nor the file is unclear (`flow-mode.md` line 254), and the steps fit one order only, so no question is due (`flow-mode.md` line 242).

The test runs with no Figma route. The hosted Figma MCP is not connected and the `figma-ds-cli` daemon is not running, so neither the hosted route nor the `fj` route can write (`flow-mode.md` lines 174 to 199). With no route the runtime says which one is missing and what it needs, offers the checked model for the user to keep and never puts an image, an HTML page or a Mermaid file in place of the board (`flow-mode.md` line 203). Flow Mode saves nothing to `export/` (`AGENTS.md` line 39, `flow-mode.md` line 230).

The rules do not settle when a runtime finds the missing route. The workflow puts the gate before the write and the route choice inside the write (`flow-mode.md` lines 65 and 66), while the `fj` route names its file in the gate after a read-only `fj info` (`flow-mode.md` line 194), which means probing for a route before the gate. Turn 1 therefore passes in either of two forms: the gate message, waiting for a yes, or the missing-route reply with the checked model. Turn 2's yes meets no route in both forms, so the reply names the missing route and writes nothing. Which form Turn 1 took is recorded and not graded.

`flow_check.py` reads its model from a file, while `flow-mode.md` line 230 says no Mermaid file is created anywhere. A scratch model file the check reads outside `export/` and `context/` is recorded in the ledger and not graded, and the tension is logged as a follow-up finding. Neither reply delivers a board, and the self-scan is counted on the labels written to a board (`flow-mode.md` line 227), so whether a reply carries an `HVR self-scan:` line is recorded and not graded.

### Why this matters

A board is visible to every member of its plan as soon as it lands (`flow-mode.md` line 254), so a write before the yes puts an unreviewed flow in front of all of them. A reply that claims a board when no route could write one sends the team to a link that does not exist. A model that breaks the flowchart rules reaches the board with mis-routed connectors or labels the generator drops, and the generator owns the layout, so nobody can fix it by dragging (`flow-mode.md` line 164).

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a `$flow` request from a short Fernhouse spec builds and checks a Mermaid model, stops before any write and, with no Figma route connected, names the missing route, offers the checked model and claims no board
- Real user request: `$flow Make a FigJam flow of back-in-stock alerts from Lotte's spec below, as a new board in our Fernhouse Product plan. Company background is in context/fernhouse-context.md. Spec: a customer on the product page of a sold-out item taps "Notify me". A signed-in customer's alert is saved to their account straight away. A guest types an email address first, then the alert is saved. When the item is back in stock the customer gets one email. Push alerts in the app are a proposal only, nobody has agreed them yet.`
- Prompt: `$flow Make a FigJam flow of back-in-stock alerts from Lotte's spec below, as a new board in our Fernhouse Product plan. Company background is in context/fernhouse-context.md. Spec: a customer on the product page of a sold-out item taps "Notify me". A signed-in customer's alert is saved to their account straight away. A guest types an email address first, then the alert is saved. When the item is back in stock the customer gets one email. Push alerts in the app are a proposal only, nobody has agreed them yet.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, the attachment sits unchanged at `context/fernhouse-context.md` before the export baseline (root, Company context and attachments), and no Figma route is reachable: no Figma MCP server is connected and no `figma-ds-cli` daemon is running. Record the connected tool list
- Expected execution process: Start fresh, submit Turn 1, capture the reply and the session's tool calls, submit Turn 2 in the same session, capture that reply and its tool calls, then compare `export/` and `context/` with their baselines
- Expected signals: Turn 1 routes to Flow Mode, asks no question, builds one Mermaid diagram from the spec with a provenance table, runs `sk-create-figjam/scripts/flow_check.py` on it until the check prints `PASSED` with exit 0 and writes nothing. Its reply either states the `Fernhouse Product` plan, a new FigJam file the first diagram creates, the effect and the rollback in one message and waits for a yes, or says which route is missing and what it needs and offers the checked model. Turn 2 may probe the routes and writes nothing. It names the hosted Figma MCP and the `fj` route as not reachable with what each needs, offers the checked model in the reply and claims no board. Neither reply prints a board URL, a `Read-back:` line, a `Path:` line or a `Verified:` line. `export/` gains no file and `context/fernhouse-context.md` stays byte for byte unchanged
- Desired user-visible outcome: A checked back-in-stock flow model and a write gate that waits, then a plain account of the missing Figma route with the model to keep and no board claimed
- Size band (advisory): one diagram of 7 or 8 nodes, a merge dot making the eighth. Recorded only, never a Pass or Fail input (root section 5, Ticket realism)
- Pass/fail: PASS if Turn 1 routes to Flow Mode, asks no question, runs `flow_check.py` on the model with a last result of `PASSED` and exit 0, writes nothing and ends either on a gate that names the `Fernhouse Product` plan, a new FigJam file, the effect and the rollback and waits for a yes, or on the missing-route reply with the checked model, and Turn 2 writes nothing, names the hosted Figma MCP and the `fj` route as missing with what each needs, offers the checked model and claims no board. The model holds every spec step or lists it as left out: the sold-out product page, the Notify me tap, the signed-in decision with both exits labelled, the guest's email address, the saved alert, the item back in stock and the one email. Push alerts are left out or carry their proposal status in the label. FAIL if any file appears under `export/`, a reply prints a board URL or a `Read-back:` line or says a board exists or was written, Turn 1 asks a question, a write tool or an `fj` create verb is called before the yes, `flow_check.py` was never run or the offered model differs from the one it passed, the model breaks a flowchart rule such as more than 9 nodes in a diagram, a decision with more than 3 exits, an unlabelled exit, an emoji, an underscore in a node id, markup in a label or a connector other than `-->`, push alerts are drawn as current behavior, or the flow is rendered as an image, an HTML page or a Mermaid file in place of the board
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$flow Make a FigJam flow of back-in-stock alerts from Lotte's spec below, as a new board in our Fernhouse Product plan. Company background is in context/fernhouse-context.md. Spec: a customer on the product page of a sold-out item taps "Notify me". A signed-in customer's alert is saved to their account straight away. A guest types an email address first, then the alert is saved. When the item is back in stock the customer gets one email. Push alerts in the app are a proposal only, nobody has agreed them yet.` | Route to Flow Mode on `$flow`, read the spec and the attachment and classify each claim. Write one Mermaid diagram with a provenance table, leave push alerts out or label them as a proposal, and run `flow_check.py` on the model until it passes. Then either state the `Fernhouse Product` plan, a new FigJam file, the effect and the rollback in one message and wait for a yes, or say which route is missing and offer the checked model. Ask no question and write nothing | Flow Mode selected, the check passed, no write tool or `fj` create verb called, no new file under `export/`, `context/` unchanged | Turn 1 reply, the tool calls with every `flow_check.py` run and its exit status, the model the check read |
| 2 | `Yes, go ahead.` | Find that neither route can write, say the hosted Figma MCP is not connected and the `fj` route is not reachable and what each needs, offer the checked model in the reply for the user to keep and claim no board. Print no board URL, no `Read-back:` line, no `Path:` line and no `Verified:` line | Nothing written to Figma or to `export/`, `context/` unchanged, the offered model is the one the check passed | Turn 2 reply, its tool calls and the offered model |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$flow Make a FigJam flow of back-in-stock alerts from Lotte's spec below, as a new board in our Fernhouse Product plan. Company background is in context/fernhouse-context.md. Spec: a customer on the product page of a sold-out item taps "Notify me". A signed-in customer's alert is saved to their account straight away. A guest types an email address first, then the alert is saved. When the item is back in stock the customer gets one email. Push alerts in the app are a proposal only, nobody has agreed them yet.`

### Commands

1. `sandbox: stage the attachment in context/ and confirm no Figma route is reachable -> filesystem: record the export and context/ baselines and the connected tool list`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: read the reply and the tool calls, confirm flow_check.py passed the model and nothing was written, copy the model the check read into a scratch file outside the sandbox and run flow_check.py on it -> user: submit Turn 2 in the same session`
4. `operator: read the Turn 2 reply and its tool calls, confirm the missing routes are named, the checked model is offered and no board is claimed, and compare the offered model with the one the check passed`
5. `filesystem: compare export/ and context/ with their baselines and record any scratch model file the check read`

### Expected

Step 1 fixes both baselines and shows no Figma route. Step 2 returns either the gate message or the missing-route reply, with no question. Step 3 finds a `flow_check.py` run whose last result is `PASSED` with exit 0, no write tool or `fj` create verb in the tool calls, and a model of one diagram with at most 9 nodes, one decision whose exits are both labelled, camelCase ids and no emoji or markup, holding every spec step or listing it as left out, with push alerts left out or labelled as a proposal. The operator's own run passes too. Step 4 finds a reply that names the hosted Figma MCP and the `fj` route as missing with what each needs, offers the same model and claims no board. Step 5 finds no new file under `export/` and the attachment unchanged.

### Evidence

Capture both replies, the connected tool list, every tool call with each `flow_check.py` run and its output and exit status, the model with its provenance table, which form Turn 1 took, the operator's own `flow_check.py` run, the side-effect ledger and the `export/` and `context/` comparison.

### Pass / fail

- **Pass**: Turn 1 asks no question, passes the model through `flow_check.py`, writes nothing and ends on the gate or the missing-route reply, and Turn 2 writes nothing, names both missing routes with what each needs, offers the checked model and claims no board, with no file under `export/`
- **Fail**: Any file appears under `export/`, a reply prints a board URL or a `Read-back:` line or says a board exists, Turn 1 asks a question, a write is called before the yes, the check never ran or the offered model is not the one it passed, the model breaks a flowchart rule, push alerts are drawn as current behavior, or an image, an HTML page or a Mermaid file stands in for the board

### Failure triage

1. Check the Flow route in `AGENTS.md` line 222 and `SKILL.md` line 57, and the workflow order in `flow-mode.md` lines 59 to 69
2. Check the model against the shared rules in `flow-mode.md` lines 155 to 165 and the user flow rules in `sk-create-figjam/references/types/user-flow.md` Section 3, and rerun `sk-create-figjam/scripts/flow_check.py` on it
3. Check the missing-route reply against `flow-mode.md` line 203 and the export exemption in `AGENTS.md` line 39

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SFL-001 | Flow gate with no route | Verify that a `$flow` request builds and checks a model, stops before any write and, with no Figma route, names the missing route and claims no board | `$flow Make a FigJam flow of back-in-stock alerts from Lotte's spec below, as a new board in our Fernhouse Product plan. Company background is in context/fernhouse-context.md. Spec: a customer on the product page of a sold-out item taps "Notify me". A signed-in customer's alert is saved to their account straight away. A guest types an email address first, then the alert is saved. When the item is back in stock the customer gets one email. Push alerts in the app are a proposal only, nobody has agreed them yet.` | 1. Stage, baseline and confirm no route -> 2. Submit Turn 1 fresh -> 3. Check the model and the tool calls and submit Turn 2 -> 4. Read the missing-route reply -> 5. Compare export/ and context/ | Step 2: the gate or the missing-route reply, no question. Step 3: a passed check, no write and a model inside the flowchart rules. Step 4: both missing routes named, the checked model offered, no board claimed. Step 5: no export and the attachment unchanged | Both replies, tool calls, check runs, the model, the ledger and the comparison | PASS if the check passed, nothing was written, the missing routes were named with the checked model offered and no reply claimed a board or a file. FAIL otherwise | 1. Check the Flow route and the workflow order. 2. Check the flowchart rules. 3. Check the missing-route reply and the export exemption |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Flow route, the export exemption and the ban on writing a board before the yes |
| [`SKILL.md`](../../SKILL.md) | Flow Mode route |
| [`flow-mode.md`](../../../sk-create-figjam/references/flow-mode.md) | Workflow, product doc intake, flowchart rules, write routes, the no-route reply and delivery |
| [`flow-templates.md`](../../../sk-create-figjam/assets/flow-templates.md) | One-decision pattern, provenance table and reply shape |
| [`flow_check.py`](../../../sk-create-figjam/scripts/flow_check.py) | The pre-write check the model must pass |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Attachment: Fernhouse company context |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill flow modes
- Playbook ID: SFL-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-flow-modes/flow-gate-no-route.md`
