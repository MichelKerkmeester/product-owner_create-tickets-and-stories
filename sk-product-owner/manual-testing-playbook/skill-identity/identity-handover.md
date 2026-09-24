---
title: "SID-001 -- Skill identity handover"
description: "Validates the skill runtime identity and filesystem delivery contract through the read-back proof and a real export path."
version: 1.0.0.0
---

# SID-001 -- Skill identity handover

This scenario validates the skill runtime before any other skill-side scenario runs. It passes only when the reply proves the filesystem delivery contract that the Project runtime cannot produce.

---

## 1. OVERVIEW

The runtime runs from `AGENTS.md` with `sk-product-owner/` loaded. A routine Quick task request must produce a saved task export, a path-first reply and the skill-only verification line. The Project runtime has no such contract, so a reply carrying Canvas Artifact language fails this scenario.

### Why this matters

Every later skill scenario assumes the runtime can save a file, read it back and report the real path. An identity mistake here invalidates the whole skill set.

---

## 2. SCENARIO CONTRACT

- Objective: Verify skill identity through the read-back confirmation and a real readable export path
- Real user request: `Can you write up a quick task for the payout pause toggle? Brands pause a pending payout for 24 hours with a required reason, and QA needs checklist items for the toggle, the reason field and the creator banner.`
- Prompt: `$quick $task Create a task for the payout pause toggle. Brands pause a pending payout for 24 hours with a required reason, and QA needs checklist items for the toggle, the reason field and the creator banner.`
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Expected execution process: Start a fresh skill session, submit Turn 1, inspect the export folder, then submit Turn 2 in the same session and compare both replies
- Expected signals: Turn 1 saves `export/[###] - task-payout-pause-toggle.md`, reads it back with non-empty content and replies with the path, the read-back fixture, the HVR self-scan line and a quality summary. Turn 2 repeats the same path and proof without inventing a new file
- Desired user-visible outcome: A saved export, a path-first reply and the skill-only delivery lines
- Pass/fail: PASS if the reply carries `read-back succeeded`, names a readable path with non-empty content, and carries no Project wording. FAIL if it claims no file was written, speaks Canvas Artifact, or names a path that does not read back
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$quick $task Create a task for the payout pause toggle. Brands pause a pending payout for 24 hours with a required reason, and QA needs checklist items for the toggle, the reason field and the creator banner.` | Route to Task Mode with Quick energy, save the task, read the exact path back, then reply path-first with the read-back fixture and the HVR self-scan line | The export prefix advances by one and no supplied source changes | Turn 1 reply, exported file, read-back result, side-effect ledger and folder listing |
| 2 | `Confirm what you did to verify the saved file, and name the exact delivery string you printed.` | Repeat the saved path and the read-back fixture, and state that Read returned non-empty content | The same file is named and no new export appears | Turn 2 reply, side-effect ledger and the unchanged folder listing |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$quick $task Create a task for the payout pause toggle. Brands pause a pending payout for 24 hours with a required reason, and QA needs checklist items for the toggle, the reason field and the creator banner.`

### Commands

1. `sandbox: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: list the export folder -> operator: open the new file and confirm non-empty content`
4. `user: submit Turn 2 in the same session -> operator: compare both replies against the skill contract`

### Expected

Step 1 fixes the baseline. Step 2 produces one task export and the skill delivery lines. Step 3 proves the path is real and readable. Step 4 proves the runtime keeps the same file identity across turns.

### Evidence

Capture both replies, the per-turn side-effect ledger, the export folder listing, the read-back result, the HVR self-scan line and the task artifact body.

Identity split proof from the worktree root:

- `grep -c "read-back succeeded" "AI Systems/Product Owner/AGENTS.md"` -> `1`, exit `0`
- `grep -c "read-back succeeded" "AI Systems/Product Owner/claude project/Custom Instructions.md"` -> `0`, exit `1`
- `grep -c "Canvas Artifact" "AI Systems/Product Owner/AGENTS.md"` -> `0`, exit `1`
- `grep -c "Canvas Artifact" "AI Systems/Product Owner/claude project/Custom Instructions.md"` -> `4`, exit `0`

The skill identity string `read-back succeeded` is absent from the Project kernel. The Project identity string `Canvas Artifact` is absent from the skill identity file. A reply that could have come from either runtime, or that carries the other runtime's string, is a FAIL.

Fixture payload (skill delivery line): Verified: read-back succeeded; N lines

### Pass / fail

- **Pass**: The reply carries `read-back succeeded`, names a readable export path and prints the HVR self-scan line
- **Fail**: The reply carries Canvas Artifact or `Export-equivalent path:`, claims no file was written, omits the read-back proof, or names a path that does not read back

### Failure triage

1. Re-run Turn 1 in a clean session and inspect the export folder before reading the reply
2. Compare the reply wording with the skill delivery contract in `AGENTS.md` Section 2
3. If the runtime emits Project vocabulary, stop the skill set and report the identity failure

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SID-001 | Skill identity handover | Verify the skill runtime through the read-back proof and a real export path | `$quick $task Create a task for the payout pause toggle. Brands pause a pending payout for 24 hours with a required reason, and QA needs checklist items for the toggle, the reason field and the creator banner.` | 1. Baseline -> 2. Submit Turn 1 fresh -> 3. Inspect and read back the export -> 4. Submit Turn 2 and compare | Step 1: baseline known. Step 2: one export and the skill lines. Step 3: readable file. Step 4: same file identity | Both replies, folder listing, read-back result and artifact body | PASS if the skill string and a readable path both appear. FAIL on Project wording or an unreadable path | 1. Re-run in a clean session. 2. Compare with the delivery contract. 3. Stop the set on identity drift |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Skill identity and filesystem delivery contract |
| [`SKILL.md`](../../SKILL.md) | Routing, export and read-back rules |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Contrast kernel that sets the Project identity string |

---

## 5. SOURCE METADATA

- Group: Skill identity
- Playbook ID: SID-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-identity/identity-handover.md`
