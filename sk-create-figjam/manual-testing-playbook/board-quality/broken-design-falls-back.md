---
title: "FJ-045 -- A broken design falls back with named findings"
description: "This scenario validates that a broken design falls back with named findings for `FJ-045`. It checks that a design file with a pink zone tint, the accent's pair on a role and an unknown group still draws the board, in the shipped value for each bad token, and that the reply names each fallback on its own Finding line."
version: 1.0.3.0
driver: operator-only
---

# FJ-045 -- A broken design falls back with named findings

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-045`.

---

## 1. OVERVIEW

This scenario validates that a broken design falls back with named findings for `FJ-045`. It checks that a design file with a pink zone tint, the accent's pair on a role and an unknown group still draws the board, in the shipped value for each bad token, and that the reply names each fallback on its own `Finding:` line.

### Why This Matters

The design file is edited by hand, so a bad edit is a matter of time. A bad edit that stops every board leaves the team with no boards, and one that draws silently leaves them wondering why their edit did nothing. Falling back token by token and saying so keeps both the board and the reason in front of the user.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-045` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a design file with a pink zone tint, the accent's pair on a role and an unknown group still draws the board in the shipped value for each bad token, and that the reply names each fallback on its own `Finding:` line
- Real user request: `$flow how a Fernhouse customer starts a return in the app, on a new board in our Fernhouse Product plan. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support.`
- Prompt: `$flow how a Fernhouse customer starts a return in the app, on a new board in our Fernhouse Product plan. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support.`
- Expected execution process: The operator breaks a saved copy of the design file in three ways and confirms the design check names all three. Flow Mode then runs as usual: the playback, the gate, the write on its yes and the read-back. The composer prints a `DESIGN` line for each bad token and counts them on the `COMPOSED` line, and the reply turns each into a `Finding:` line. The operator restores the design file afterwards
- Expected signals: The design check prints three `DESIGN` lines and exits 1: `shadow` left out as a group the composer does not read, `role.goal` back to `"lightGreen"` because `lightPink` is the accent's own pair, and `zone.cycle` back to the five shipped tints because pink sits under 45 degrees of hue from the accent. The compose prints the same three lines and a `COMPOSED` line ending `3 design warnings`. The board is written after the gate's yes. Its goal, Return confirmed, is light green and not pink, no zone is pink and the key names the goal `Goal reached`. The reply carries three `Finding:` lines above the `HVR self-scan:` line, each naming the token, what the design asked for and what the board drew instead. The read-back names the accented node as the first glance, and the overview shows it first. A fresh reader answers from the colour screenshot. Q1: What does a customer see more than 30 days after delivery? Answer: Contact support. Q2: Which two ways can the item go back? Answer: a drop-off point or a courier pickup. Q3: Where does a return end? Answer: Return confirmed with a QR code. After the restore the design file shows no change
- Desired user-visible outcome: A board drawn in the shipped look for the three bad tokens, and a reply that says which tokens fell back and why
- Pass/fail: PASS if the board is drawn, each of the three bad tokens draws its shipped value, the reply carries one `Finding:` line per `DESIGN` line above the self-scan, the restored design file shows no change and every expected signal is present. FAIL if an expected signal is missing, the compose stops, a pink zone or a pink goal is drawn, a `DESIGN` line has no `Finding:` line, a `Finding:` line follows the self-scan or the design file is left changed. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$flow how a Fernhouse customer starts a return in the app, on a new board in our Fernhouse Product plan. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-045 | A broken design falls back with named findings | Verify that a design file with a pink zone tint, the accent's pair on a role and an unknown group still draws the board in the shipped value for each bad token, and that the reply names each fallback on its own `Finding:` line | `$flow how a Fernhouse customer starts a return in the app, on a new board in our Fernhouse Product plan. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support.` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> bash: cp sk-create-figjam/assets/figjam-design.md <scratch>/figjam-design.md` -> 2. `bash: in the json block of sk-create-figjam/assets/figjam-design.md add "pink" to the end of zone.cycle, set role.goal to "lightPink" and add a top-level group "shadow": {"blur": 4} -> bash: python3 sk-create-figjam/scripts/compose_board.py --design-check -> bash: echo "exit $?"` -> 3. `session: start fresh -> user: submit the prompt exactly -> operator: confirm the reply is the playback and nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows` -> 4. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, with nothing written yet` -> 5. `user: Yes, go ahead. -> operator: record the reply, the DESIGN and COMPOSED lines, every tool call and the get_figjam read, then screenshot the whole board` -> 6. `bash: cp <scratch>/figjam-design.md sk-create-figjam/assets/figjam-design.md -> bash: git diff --exit-code -- sk-create-figjam/assets/figjam-design.md -> bash: echo "exit $?"` -> 7. `reader: give a fresh reader the colour screenshot and ask Q1 to Q3 -> operator: record the answers` | Step 2 prints three `DESIGN` lines naming `shadow`, `role.goal` and `zone.cycle` and exits 1. Step 3 ends on the playback and step 4 on the gate, with nothing written. Step 5 finds the same three `DESIGN` lines, a `COMPOSED` line ending `3 design warnings`, a board with a light green goal that is not pink, no pink zone and the accented node read back as the first glance, and a reply with three `Finding:` lines above the `HVR self-scan:` line. Step 6 exits 0. Step 7: the reader answers from the colour screenshot. Q1: What does a customer see more than 30 days after delivery? Answer: Contact support. Q2: Which two ways can the item go back? Answer: a drop-off point or a courier pickup. Q3: Where does a return end? Answer: Return confirmed with a QR code. | The broken design block, the design check output, every reply, the `DESIGN` and `COMPOSED` lines, every tool call, the get_figjam read, the overview screenshot and the restore's exit status | PASS if the board is drawn, each of the three bad tokens draws its shipped value, the reply carries one `Finding:` line per `DESIGN` line above the self-scan, the restored design file shows no change and every expected signal is present. FAIL if an expected signal is missing, the compose stops, a pink zone or a pink goal is drawn, a `DESIGN` line has no `Finding:` line, a `Finding:` line follows the self-scan or the design file is left changed. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When the design check names fewer than three tokens, check the floors in `assets/figjam-design.md` Section 7 and `scripts/figjam_checks/design.py` 2. When a `DESIGN` line has no `Finding:` line, check the reply rule in `references/flow-mode.md` Section 8 3. When the board draws a bad token, compare the `THEME` the design check prints with the code the write sent |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and pick a plan the operator owns -> bash: cp sk-create-figjam/assets/figjam-design.md <scratch>/figjam-design.md`
2. `bash: in the json block of sk-create-figjam/assets/figjam-design.md add "pink" to the end of zone.cycle, set role.goal to "lightPink" and add a top-level group "shadow": {"blur": 4} -> bash: python3 sk-create-figjam/scripts/compose_board.py --design-check -> bash: echo "exit $?"`
3. `session: start fresh -> user: submit the prompt exactly -> operator: confirm the reply is the playback and nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows`
4. `user: Yes, that reading is right. -> operator: confirm the passing check and the gate, with nothing written yet`
5. `user: Yes, go ahead. -> operator: record the reply, the DESIGN and COMPOSED lines, every tool call and the get_figjam read, then screenshot the whole board`
6. `bash: cp <scratch>/figjam-design.md sk-create-figjam/assets/figjam-design.md -> bash: git diff --exit-code -- sk-create-figjam/assets/figjam-design.md -> bash: echo "exit $?"`
7. `reader: give a fresh reader the colour screenshot and ask Q1 to Q3 -> operator: record the answers`

### Expected

Step 2 prints three `DESIGN` lines naming `shadow`, `role.goal` and `zone.cycle` and exits 1. Step 3 ends on the playback and step 4 on the gate, with nothing written. Step 5 finds the same three `DESIGN` lines, a `COMPOSED` line ending `3 design warnings`, a board with a light green goal that is not pink, no pink zone and the accented node read back as the first glance, and a reply with three `Finding:` lines above the `HVR self-scan:` line. Step 6 exits 0. Step 7: the reader answers from the colour screenshot. Q1: What does a customer see more than 30 days after delivery? Answer: Contact support. Q2: Which two ways can the item go back? Answer: a drop-off point or a courier pickup. Q3: Where does a return end? Answer: Return confirmed with a QR code.

### Evidence

The broken design block, the design check output, every reply, the `DESIGN` and `COMPOSED` lines, every tool call, the get_figjam read, the overview screenshot and the restore's exit status

### Pass / Fail

- **Pass**: the board is drawn, each of the three bad tokens draws its shipped value, the reply carries one `Finding:` line per `DESIGN` line above the self-scan and the restored design file shows no change
- **Fail**: the compose stops, a pink zone or a pink goal is drawn, a `DESIGN` line has no `Finding:` line, a `Finding:` line follows the self-scan or the design file is left changed. Anything written before the gate's yes also fails it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

### Failure Triage

1. When the design check names fewer than three tokens, check the floors in `assets/figjam-design.md` Section 7 and `scripts/figjam_checks/design.py`
2. When a `DESIGN` line has no `Finding:` line, check the reply rule in `references/flow-mode.md` Section 8
3. When the board draws a bad token, compare the `THEME` the design check prints with the code the write sent

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
| [`assets/figjam-design.md`](../../assets/figjam-design.md) | The design file and its floors |
| [`scripts/figjam_checks/design.py`](../../scripts/figjam_checks/design.py) | Reads the design and falls back token by token |
| [`references/flow-mode.md`](../../references/flow-mode.md) | The reply's `Finding:` lines |

---

## 5. SOURCE METADATA

- Group: Board quality
- Playbook ID: FJ-045
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-quality/broken-design-falls-back.md`
