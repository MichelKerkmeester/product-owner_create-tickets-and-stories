---
title: "FJ-048 -- A read-back judges a view taken after the write"
description: "This scenario validates a read-back judges a view taken after the write for `FJ-048`. It checks that a read-back after a later write judges a view rendered after that write, and reports a view that still shows the board before it as stale."
version: 1.0.0.0
---

# FJ-048 -- A read-back judges a view taken after the write

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-048`.

---

## 1. OVERVIEW

This scenario validates a read-back judges a view taken after the write for `FJ-048`. It checks that a read-back after a later write judges a view rendered after that write, and reports a view that still shows the board before it as stale.

### Why This Matters

A screenshot tool can return the board as it stood before the last write. A read-back that judges that view approves a board nobody has seen, so it takes its view inside the write call and names a stale one.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-048` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a read-back after a later write judges a view rendered after that write, and reports a view that still shows the board before it as stale
- Real user request: `Add one sticky note beside the first step of the board you just wrote, saying `Owner: support lead`, then read the board back.`
- Prompt: `Add one sticky note beside the first step of the board you just wrote, saying `Owner: support lead`, then read the board back.`
- Expected execution process: Write a board, add one note through the hybrid workflow, then read the board back with the view taken by `node.screenshot()` inside a `use_figma` call
- Expected signals: The read-back's view shows the new note. Any view that does not show it is reported `stale` and taken again before it is judged, and the reply's read-back line counts the note
- Desired user-visible outcome: A read-back that counts and shows the note the last write added
- Pass/fail: PASS if the judged view was rendered after the note's write and shows it, and any stale view was named and retaken. FAIL if the read-back judges a view without the note, or calls a stale view current

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Add one sticky note beside the first step of the board you just wrote, saying `Owner: support lead`, then read the board back.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-048 | A read-back judges a view taken after the write | Verify that a read-back after a later write judges a view rendered after that write, and reports a view that still shows the board before it as stale | `Add one sticky note beside the first step of the board you just wrote, saying `Owner: support lead`, then read the board back.` | 1. `figma: compose and write a board from any shipped example after its gate` -> 2. `figma: add the one note through `references/hybrid-workflow.md` after its gate` -> 3. `figma: read the board back with `get_figjam` and a view from `node.screenshot()` inside a `use_figma` call` | The read-back's view shows the new note. Any view that does not show it is reported `stale` and taken again before it is judged, and the reply's read-back line counts the note | The write's return, the note's write, the read-back view and the reply | PASS if the judged view was rendered after the note's write and shows it, and any stale view was named and retaken. FAIL if the read-back judges a view without the note, or calls a stale view current | 1. Check step 10 and Section 7 of `references/flow-mode.md` 2. Check Section 6 of `references/hybrid-workflow.md` |

### Commands

1. `figma: compose and write a board from any shipped example after its gate`
2. `figma: add the one note through `references/hybrid-workflow.md` after its gate`
3. `figma: read the board back with `get_figjam` and a view from `node.screenshot()` inside a `use_figma` call`

### Expected

The read-back's view shows the new note. Any view that does not show it is reported `stale` and taken again before it is judged, and the reply's read-back line counts the note

### Evidence

The write's return, the note's write, the read-back view and the reply

### Pass / Fail

- **Pass**: the judged view was rendered after the note's write and shows it, and any stale view was named and retaken
- **Fail**: the read-back judges a view without the note, or calls a stale view current

### Failure Triage

1. Check step 10 and Section 7 of `references/flow-mode.md`
2. Check Section 6 of `references/hybrid-workflow.md`

---

## 4. SOURCE FILES

### Playbook Sources

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and scenario summary |
| Feature catalog | No dedicated catalog entry: the packet has no feature catalog, so `SKILL.md` and the references below are the contract |

### Implementation And Test Anchors

| File | Role |
|---|---|
| [`references/flow-mode.md`](../../references/flow-mode.md) | The read-back rule |
| [`references/hybrid-workflow.md`](../../references/hybrid-workflow.md) | The extension read-back |
| [`references/quality-rubric.md`](../../references/quality-rubric.md) | The view checklist line |

---

## 5. SOURCE METADATA

- Group: Board write
- Playbook ID: FJ-048
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-write/fresh-read-back-after-write.md`
