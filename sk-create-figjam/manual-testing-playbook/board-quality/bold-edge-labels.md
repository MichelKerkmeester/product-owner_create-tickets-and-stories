---
title: "FJ-051 -- Edge labels take their Bold from their words"
description: "This scenario validates edge labels take their Bold from their words for `FJ-051`. It checks that on a composed process board a short key before a colon is Bold, every label leaving a decision is Bold throughout and any other label stays Medium on one line."
version: 1.0.0.0
---

# FJ-051 -- Edge labels take their Bold from their words

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-051`.

---

## 1. OVERVIEW

This scenario validates edge labels take their Bold from their words for `FJ-051`. It checks that on a composed process board a short key before a colon is Bold, every label leaving a decision is Bold throughout and any other label stays Medium on one line.

### Why This Matters

At overview zoom a reader scans the outcomes of a decision before any card. A label set all in one weight makes "Decline: No impact" read like a step's caption. Setting the key and the branch names in Bold lets the outcomes stand out without a colour or a sticky.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-051` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a composed process board sets a short key and its colon in Bold, sets every decision exit in Bold throughout and leaves any other label Medium, each on one line
- Real user request: `$figjam a process of how a Fernhouse feature request is handled, on a new board in our Fernhouse Product plan, with a lane for the requester, the product owner and the product lead. The product owner logs it and checks the impact. No impact: decline it. Low impact today: park it. Has impact: the product lead asks whether it is a small feature or a main feature or new product. Both end in planning.`
- Prompt: `$figjam a process of how a Fernhouse feature request is handled, on a new board in our Fernhouse Product plan, with a lane for the requester, the product owner and the product lead. The product owner logs it and checks the impact. No impact: decline it. Low impact today: park it. Has impact: the product lead asks whether it is a small feature or a main feature or new product. Both end in planning.`
- Expected execution process: Model the process with labels in the wording `references/style-guide.md` Section 5 sets, such as `"Decline: No impact"`, `"Park: Low impact today"` and `"Do it: Has impact"`, quoted because of the colon. Run the check and the self-test, then write and read the board back
- Expected signals: The model quotes every label with a colon and the check passes. `python3 scripts/compose_board.py --self-test` reports the row `an edge label sets a short key, or any decision exit, in Bold and leaves a step's label Medium` as passing. On the written board, each outcome label sets only its key and colon in Bold, such as **Decline:** No impact, each label leaving the size decision, such as **Small feature** and **Main feature or new product**, is Bold throughout, and a label leaving a step stays Medium. Every label is one line under the 40-character cap and sentence case
- Desired user-visible outcome: A board whose decision outcomes stand out at overview zoom
- Pass/fail: PASS if the self-test row passes and every label on the written board carries the weight Section 5 sets on one line. FAIL if a key is Medium, a decision exit is Medium or only partly Bold, a step's label is Bold, a label wraps, or the model carries an unquoted colon

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$figjam a process of how a Fernhouse feature request is handled, on a new board in our Fernhouse Product plan, with a lane for the requester, the product owner and the product lead. The product owner logs it and checks the impact. No impact: decline it. Low impact today: park it. Has impact: the product lead asks whether it is a small feature or a main feature or new product. Both end in planning.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-051 | Edge labels take their Bold from their words | Verify that a composed process board sets a short key and its colon in Bold, sets every decision exit in Bold throughout and leaves any other label Medium, each on one line | `$figjam a process of how a Fernhouse feature request is handled, on a new board in our Fernhouse Product plan, with a lane for the requester, the product owner and the product lead. The product owner logs it and checks the impact. No impact: decline it. Low impact today: park it. Has impact: the product lead asks whether it is a small feature or a main feature or new product. Both end in planning.` | 1. `bash: python3 scripts/compose_board.py --self-test` -> 2. `session: start fresh -> user: submit the prompt exactly` -> 3. `user: yes to the playback, then yes to the gate` -> 4. `operator: read each label's font ranges on the written board` | Step 1 reports the label weight row passing. Step 4 finds every key, decision exit and step label in the weight Section 5 sets, each on one line | The self-test output, the model, the replies and each label's font ranges | PASS if the self-test row passes and every label on the written board carries the weight Section 5 sets on one line. FAIL if a key is Medium, a decision exit is Medium or only partly Bold, a step's label is Bold, a label wraps, or the model carries an unquoted colon | 1. Check `references/style-guide.md` Section 5, Edge label wording 2. Check `labelBold` and `connect` in `assets/compose-board.js` 3. Check `label_weight_checks` in `scripts/compose_board.py` |

### Commands

1. `bash: python3 scripts/compose_board.py --self-test`
2. `session: start fresh -> user: submit the prompt exactly`
3. `user: yes to the playback, then yes to the gate`
4. `operator: read each label's font ranges on the written board`

### Expected

Step 1 reports the label weight row passing. Step 4 finds every key, decision exit and step label in the weight Section 5 sets, each on one line

### Evidence

The self-test output, the model, the replies and each label's font ranges

### Pass / Fail

- **Pass**: the self-test row passes and every label on the written board carries the weight Section 5 sets on one line
- **Fail**: a key is Medium, a decision exit is Medium or only partly Bold, a step's label is Bold, a label wraps, or the model carries an unquoted colon

### Failure Triage

1. Check `references/style-guide.md` Section 5, Edge label wording
2. Check `labelBold` and `connect` in `assets/compose-board.js`
3. Check `label_weight_checks` in `scripts/compose_board.py`

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
| [`references/style-guide.md`](../../references/style-guide.md) | The edge label wording and weights |
| [`assets/compose-board.js`](../../assets/compose-board.js) | Sets each label's Bold range |
| [`scripts/compose_board.py`](../../scripts/compose_board.py) | The label weight self-test row |

---

## 5. SOURCE METADATA

- Group: Board quality
- Playbook ID: FJ-051
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-quality/bold-edge-labels.md`
