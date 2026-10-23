---
title: "PTK-007 -- ClickUp push targets"
description: "Validates that a Claude Project with the ClickUp connector ends a rendered quick task on the where question when no push targets file is uploaded, names the one fitting list from an uploaded catalog, and writes nothing to ClickUp."
version: 1.0.0.0
---

# PTK-007 -- ClickUp push targets

This scenario validates the ClickUp offer after a rendered quick task in a Claude Project, with and without the private push targets file.

---

## 1. OVERVIEW

The PTK-001 banner request runs twice in a Claude Project with the claude.ai ClickUp connector present. Push targets reach a Project only through the private Knowledge file `Product Owner - Local - Push Targets.md`, so without it the Project asks where, and with it the Project names the one list whose name and team fit the task. The task itself is graded by PTK-001. This scenario grades only the closing line and the side effects.

### Why this matters

A Project that named a target nobody uploaded would be inventing one, and a Project that ignored an uploaded target would make the user repeat it. A Project that pushed without a yes would break the approval rule.

---

## 2. SCENARIO CONTRACT

- Objective: Verify a Project with the ClickUp connector asks where with no push targets file, names the fitting list from the uploaded catalog, and writes nothing
- Real user request: `The free-shipping banner wraps on small phones, can we get it shortened?`
- Prompt: `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached and the claude.ai ClickUp connector present. Run A has no push targets file. Run B also has a copy of `claude project/templates/Product Owner - Local - Push Targets.md` filled as a push targets catalog that lists **Storefront Copy** (`https://app.clickup.com/9000000000/v/li/900000000001`) under Storefront and **Infrastructure** (`https://app.clickup.com/9000000000/v/li/900000000002`) under Platform, with no docs, uploaded
- Precondition: `PID-001` identity handover passed in the Project runtime, and the attachment sits at `context/fernhouse-context.md`
- Expected execution process: Start fresh, submit Turn 1 and read the closing line and the connector calls
- Expected signals: Run A renders the Deliverable Block and ends on `Where in ClickUp should this go? Send a list link, or I'll upload it as a private doc, which I recommend for now.` and names no link. Run B ends on `Want me to push this to Storefront Copy, or upload it as a private ClickUp doc instead?` (`Custom Instructions.md`, the paragraph after the export-equivalent labels, and `Product Owner - Assets - Interactive Response Templates`, The Closing Line). Neither run calls a connector tool
- Desired user-visible outcome: The rendered task, ending on the where question in Run A and on the Storefront Copy offer in Run B
- Size band (advisory): 20 to 45 lines of artifact body
- Pass/fail: PASS if Run A ends on the where question and names no link, Run B names Storefront Copy and not Infrastructure, and neither calls a connector tool. FAIL if a run names a list it was never given, Run B ignores the catalog, names Infrastructure, either ends on the old `Want me to push this to ClickUp?`, or a connector call writes anything
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, such as no ClickUp connector in the Project, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.` | Render the quick task block, then end on the where question in Run A, or on the Storefront Copy offer in Run B | No connector call, Run A names no link | Turn 1 reply of each run and the connector call log |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.`

### Commands

1. `project: confirm the ClickUp connector is present -> record the connector call baseline`
2. `session: start fresh with no push targets file -> user: submit Turn 1 exactly -> operator: read the closing line and the connector calls`
3. `project: upload the filled push targets copy -> session: start fresh -> user: submit Turn 1 exactly -> operator: read the closing line and the connector calls -> project: remove the copy`

### Expected

Step 1 confirms the connector. Step 2 ends on `Where in ClickUp should this go? Send a list link, or I'll upload it as a private doc, which I recommend for now.` Step 3 ends on `Want me to push this to Storefront Copy, or upload it as a private ClickUp doc instead?` Neither shows a connector call.

### Evidence

Capture the reply and the connector call log.

### Pass / fail

- **Pass**: Run A ends on the where question and names no link, Run B names Storefront Copy, and neither calls a connector tool
- **Fail**: A run names an invented target, Run B ignores the catalog, names Infrastructure, either keeps the old closing line, or a run writes to ClickUp

### Failure triage

1. Check the ClickUp offer paragraph and the Local - Push Targets row in `Custom Instructions.md`
2. Check The Closing Line in `Product Owner - Assets - Interactive Response Templates`

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PTK-007 | ClickUp push targets | Verify a Project asks where without a push targets file and names the fitting list from an uploaded catalog | `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.` | 1. Confirm the connector -> 2. Submit Turn 1 fresh -> 3. Upload the copy and submit Turn 1 fresh | Step 2: where question. Step 3: the Storefront Copy offer. No connector call | Replies and connector call log | PASS if each run ends on its expected line and writes nothing. FAIL otherwise | 1. Check the kernel offer. 2. Check the closing line mirror |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | The ClickUp offer and the push targets file it consults |
| [`Product Owner - Local - Push Targets.md`](../../../claude%20project/templates/Product%20Owner%20-%20Local%20-%20Push%20Targets.md) | The template Run B fills |
| [`Product Owner - Assets - Interactive Response Templates.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates.md) | The Project closing line |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Attachment: the banner strings PTK-001 grades |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PTK-007
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/clickup-push-targets.md`
