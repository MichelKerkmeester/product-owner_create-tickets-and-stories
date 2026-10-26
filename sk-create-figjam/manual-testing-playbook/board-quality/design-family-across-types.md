---
title: "FJ-044 -- Seven boards read as one family"
description: "This scenario validates that the seven diagram types read as one family for `FJ-044`. It checks that the seven shipped examples composed under the shipped design share one title block, one type scale, one key layout and order, one set of line looks and one zone tint rule."
version: 1.0.1.0
---

# FJ-044 -- Seven boards read as one family

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-044`.

---

## 1. OVERVIEW

This scenario validates that the seven diagram types read as one family for `FJ-044`. It checks that the seven shipped examples composed under the shipped design share one title block, one type scale, one key layout and order, one set of line looks and one zone tint rule.

### Why This Matters

A team reads many boards, and each type is learned once. When a key changes its order, a request changes its colour or a zone takes a member's hue from one type to the next, every board has to be learned again. The design file is meant to give every type the same furniture, and only boards side by side show whether it does.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-044` and confirm the expected signals without contradictory evidence.

- Objective: Verify that the seven shipped examples composed under the shipped design share one title block, one type scale, one key layout and order, one set of line looks and one zone tint rule
- Real user request: `As the operator, compose the seven sk-create-figjam examples onto one new FigJam file in a plan you own and compare their furniture: the title block, the type sizes, the key, the line looks and the zone tints. Return the seven overview screenshots and the comparison.`
- Prompt: `As the operator, compose the seven sk-create-figjam examples onto one new FigJam file in a plan you own and compare their furniture: the title block, the type sizes, the key, the line looks and the zone tints. Return the seven overview screenshots and the comparison.`
- Expected execution process: Run the design check, compose each example under `assets/examples/` with `scripts/compose_board.py`, send each code file unchanged as one `use_figma` call on one new FigJam file, screenshot each board's overview and compare the furniture across the seven
- Expected signals: The design check exits 0 with `THEME {}`. Each example prints a `COMPOSED` line drawn in the design `FigJam default` with no `DESIGN` line, and each `use_figma` call returns no warning. Every board opens on the same title block: a 64 pixel bold title and a 28 pixel subtitle in even lines at an 80 pixel margin. Every key is a light gray section titled `Key`, as wide as its diagram, with its entries in the design file's kind order, then the lines, the arrows and the step pin, and `In focus` last. Every connector is gray except an async message, which is blue, and the accent, which is pink. A sequence's requests and replies both end in a closed head. Participants are white. No zone or gantt band shares a hue with a node inside it, no two neighbouring zones share a tint and pink appears only on the accent. Every board scores 2 on the rubric's `Matches the active design` criterion
- Desired user-visible outcome: Seven boards that a reader who has learned one can read without learning the others
- Pass/fail: PASS if every board scores 2 on `Matches the active design`, the comparison finds no difference in the title block, the type sizes, the key, the line looks or the tint rule beyond what each type draws and every expected signal is present. FAIL if an expected signal is missing, any `DESIGN` line prints, any board's furniture differs from the others or a zone shares a hue with a node inside it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `As the operator, compose the seven sk-create-figjam examples onto one new FigJam file in a plan you own and compare their furniture: the title block, the type sizes, the key, the line looks and the zone tints. Return the seven overview screenshots and the comparison.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-044 | Seven boards read as one family | Verify that the seven shipped examples composed under the shipped design share one title block, one type scale, one key layout and order, one set of line looks and one zone tint rule | `As the operator, compose the seven sk-create-figjam examples onto one new FigJam file in a plan you own and compare their furniture: the title block, the type sizes, the key, the line looks and the zone tints. Return the seven overview screenshots and the comparison.` | 1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and create one new FigJam file in a plan the operator owns -> bash: python3 sk-create-figjam/scripts/compose_board.py --design-check -> bash: echo "exit $?"` -> 2. `bash: compose each of the seven examples in sk-create-figjam/assets/examples/ with python3 sk-create-figjam/scripts/compose_board.py <example> --out <scratch>/<example name>.js` -> 3. `operator: send each code file unchanged as one use_figma call on the new file and record the warnings and counts each call returns` -> 4. `operator: screenshot each board's overview and compare the title block, the type sizes, the key, the line looks and the zone tints across the seven` -> 5. `operator: score Matches the active design in references/quality-rubric.md Section 7 on each board, naming a location and a fix for each point lost` | Step 1 exits 0 with `THEME {}`. Step 2 prints seven `COMPOSED` lines drawn in the design `FigJam default` and no `DESIGN` line. Step 3 returns seven boards and no warning. Step 4 finds one title block, one key layout and order, gray connectors with a blue async message and the pink accent, closed heads on requests and replies, white participants and no zone sharing a hue with a node inside it. Step 5 scores 2 on every board | The design check output, the seven `COMPOSED` lines, the seven call results, the seven overview screenshots, the comparison and the seven scores with a reason each | PASS if every board scores 2 on `Matches the active design`, the comparison finds no difference in the title block, the type sizes, the key, the line looks or the tint rule beyond what each type draws and every expected signal is present. FAIL if an expected signal is missing, any `DESIGN` line prints, any board's furniture differs from the others or a zone shares a hue with a node inside it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker | 1. When a `DESIGN` line prints, read `assets/figjam-design.md` Section 8 against the composer's built-in design with `--design-check` 2. When a key differs, compare its entries with the kind order in `assets/figjam-design.md` Section 4 3. When a tint shares a hue with a node, check the zone rule in `references/style-guide.md` Section 2 |

### Commands

1. `sandbox: confirm the hosted Figma MCP is connected, record the tool list and create one new FigJam file in a plan the operator owns -> bash: python3 sk-create-figjam/scripts/compose_board.py --design-check -> bash: echo "exit $?"`
2. `bash: compose each of the seven examples in sk-create-figjam/assets/examples/ with python3 sk-create-figjam/scripts/compose_board.py <example> --out <scratch>/<example name>.js`
3. `operator: send each code file unchanged as one use_figma call on the new file and record the warnings and counts each call returns`
4. `operator: screenshot each board's overview and compare the title block, the type sizes, the key, the line looks and the zone tints across the seven`
5. `operator: score Matches the active design in references/quality-rubric.md Section 7 on each board, naming a location and a fix for each point lost`

### Expected

Step 1 exits 0 with `THEME {}`. Step 2 prints seven `COMPOSED` lines drawn in the design `FigJam default` and no `DESIGN` line. Step 3 returns seven boards and no warning. Step 4 finds one title block, one key layout and order, gray connectors with a blue async message and the pink accent, closed heads on requests and replies, white participants and no zone sharing a hue with a node inside it. Step 5 scores 2 on every board

### Evidence

The design check output, the seven `COMPOSED` lines, the seven call results, the seven overview screenshots, the comparison and the seven scores with a reason each

### Pass / Fail

- **Pass**: every board scores 2 on `Matches the active design` and the comparison finds no difference in the title block, the type sizes, the key, the line looks or the tint rule beyond what each type draws
- **Fail**: any `DESIGN` line prints, any board's furniture differs from the others or a zone shares a hue with a node inside it. Record SKIP only when the hosted Figma MCP is unavailable in this environment, naming that blocker

### Failure Triage

1. When a `DESIGN` line prints, read `assets/figjam-design.md` Section 8 against the composer's built-in design with `--design-check`
2. When a key differs, compare its entries with the kind order in `assets/figjam-design.md` Section 4
3. When a tint shares a hue with a node, check the zone rule in `references/style-guide.md` Section 2

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
| [`assets/figjam-design.md`](../../assets/figjam-design.md) | The design every board is drawn in |
| [`assets/examples/`](../../assets/examples/) | The seven models composed side by side |
| [`references/quality-rubric.md`](../../references/quality-rubric.md) | The `Matches the active design` criterion |

---

## 5. SOURCE METADATA

- Group: Board quality
- Playbook ID: FJ-044
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-quality/design-family-across-types.md`
