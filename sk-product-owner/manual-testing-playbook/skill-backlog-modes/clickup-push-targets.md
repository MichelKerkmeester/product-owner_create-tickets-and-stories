---
title: "STK-007 -- ClickUp push targets"
description: "Validates that the closing line of a delivered quick task names the one fitting list from the local push targets catalog and adds a private doc option, and asks where with a private doc recommended when no catalog is present, with no ClickUp write in either run."
version: 1.0.0.0
---

# STK-007 -- ClickUp push targets

This scenario validates the ClickUp offer after a saved quick task, run once with a local push target and once without.

---

## 1. OVERVIEW

The STK-001 banner request runs twice in the skill runtime with ClickUp tooling connected. In Run A the sandbox holds `claude project/local/Product Owner - Local - Push Targets.md` filled as a push targets catalog that lists **Storefront Copy** (`https://app.clickup.com/9000000000/v/li/900000000001`) under Storefront and **Infrastructure** (`https://app.clickup.com/9000000000/v/li/900000000002`) under Platform, with no docs, and in Run B it holds no such file. The task itself is graded by STK-001. This scenario grades only the closing line and the side effects: the catalog is read from `claude project/local/`, the fitting list is named in Run A beside a private doc option, and in Run B replaced by a question that recommends a private doc. Neither run writes to ClickUp, because a push needs an explicit yes.

### Why this matters

A public copy of this repository must never carry a team's ClickUp links, and a user who has set one should not be asked where every task goes. An offer that ignores the local target, or one that pushes on its own, breaks both.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the closing line offers the local push target with a private doc option when one is set, and asks where with a private doc recommended when none is set
- Real user request: `The free-shipping banner wraps on small phones, can we get it shortened?`
- Prompt: `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.`
- Attachments: [fernhouse-context.md](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded, ClickUp tooling connected
- Precondition: `SID-001` identity handover passed in the skill runtime, the attachment sits at `context/fernhouse-context.md`, and the sandbox holds the filled catalog at `claude project/local/Product Owner - Local - Push Targets.md` for Run A and no catalog for Run B
- Expected execution process: Start fresh for Run A, submit Turn 1 and read the closing line, then start fresh for Run B and do the same
- Expected signals: The reply follows the Delivery Reply Shape and ends on the ClickUp closing line (`assets/interactive-response-templates.md` Section 3, The Closing Line). The catalog is read from `claude project/local/` (`SKILL.md` Section 7, Push Targets). Run A ends on `Want me to push this to Storefront Copy, or upload it as a private ClickUp doc instead?` and Run B ends on `Where in ClickUp should this go? Send a list link, or I'll upload it as a private doc, which I recommend for now.`. No ClickUp tool is called in either run, and no link value is written into the export
- Desired user-visible outcome: The same saved task in both runs, offered to the local list with a private doc option in Run A and with a where question in Run B
- Size band (advisory): 20 to 45 lines of artifact body
- Pass/fail: PASS if both runs save the task and end on the closing line their catalog state calls for, Run A naming Storefront Copy and not Infrastructure with the private doc option and Run B asking where with the private doc recommended, and no ClickUp write happens and no link reaches the export. FAIL if Run A asks where, names Infrastructure or omits the private doc option, Run B names a list it was never given or ends on the old `Want me to push this to ClickUp?`, a ClickUp tool writes anything, or the link appears in the export file
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, such as no ClickUp tooling in the runtime, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1, Run A | `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.` | Save and read back the quick task, then end on the closing line that names Storefront Copy and offers a private doc | One task export, no ClickUp write, catalog unchanged | Turn 1 reply, task export, tool call log |
| 1, Run B | `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.` | Save and read back the quick task, then end on the where question that recommends a private doc | One task export, no ClickUp write, no catalog created | Turn 1 reply, task export, tool call log |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.`

### Commands

1. `sandbox: stage context/fernhouse-context.md and the filled catalog in claude project/local/ -> record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly -> operator: read the closing line and the tool calls`
3. `sandbox: remove the catalog -> session: start fresh -> user: submit Turn 1 exactly -> operator: read the closing line and the tool calls`
4. `filesystem: search both task exports for the link -> operator: confirm it is absent`

### Expected

Step 1 fixes the baseline. Step 2 ends on `Want me to push this to Storefront Copy, or upload it as a private ClickUp doc instead?` and calls no ClickUp tool. Step 3 ends on `Where in ClickUp should this go? Send a list link, or I'll upload it as a private doc, which I recommend for now.` and calls no ClickUp tool. Step 4 finds the link in neither export.

### Evidence

Capture both replies, both tool call logs, both export paths and the search result for the link.

### Pass / fail

- **Pass**: Run A offers Storefront Copy and a private doc, Run B asks where with a private doc recommended, nothing is written to ClickUp and no export carries the link
- **Fail**: Run A asks where, picks Infrastructure or drops the private doc option, Run B invents a target or keeps the old closing line, a ClickUp write happens without a yes, or the link enters an export

### Failure triage

1. Check the Push Targets rules in `SKILL.md` Section 7 and the catalog's list names
2. Check the two ClickUp closing lines in `assets/interactive-response-templates.md` Section 3
3. Check that the catalog sits in `claude project/local/` for Run A and is gone for Run B

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| STK-007 | ClickUp push targets | Verify the offer names the fitting list from the local catalog with a private doc option, or asks where when there is no catalog | `$quick $task Change the free-shipping banner to "Free shipping over €50" and "Free shipping over £45", the current copy in context/fernhouse-context.md wraps to two lines on small phones.` | 1. Stage the catalog -> 2. Run A -> 3. Remove the catalog and run B -> 4. Search the exports | Step 2: offer names Storefront Copy and a private doc. Step 3: where question recommending a private doc. No ClickUp write | Both replies, tool call logs, export paths, link search | PASS if each run ends on the line its catalog state calls for with no ClickUp write and no link in an export. FAIL otherwise | 1. Check Push Targets. 2. Check the closing lines. 3. Check the sandbox catalog |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | ClickUp Handoff and the explicit-yes rule |
| [`SKILL.md`](../../SKILL.md) | Section 7 Push Targets: the catalog, the three offers and the private doc |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Section 3 closing lines |
| [`Product Owner - Local - Push Targets.md`](../../../claude%20project/templates/Product%20Owner%20-%20Local%20-%20Push%20Targets.md) | The catalog template Run A fills |
| [`fernhouse-context.md`](../../../benchmark/fixtures/companies/fernhouse/fernhouse-context.md) | Attachment: the banner strings STK-001 grades |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: STK-007
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/clickup-push-targets.md`
