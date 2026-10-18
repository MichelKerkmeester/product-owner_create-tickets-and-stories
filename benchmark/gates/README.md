---
title: "Gates: rule parity, example lint and the gate runner"
description: "Counts a named rule's verbatim phrases on both sides of every declared pair, lints the worked examples and replies, and runs every gate from one command"
trigger_phrases:
  - "rule parity"
  - "pair-level rule check"
---

# Gates: rule parity, example lint and the gate runner

* * *

## 1. Overview

`benchmark/gates/` holds the pair-level rule check, the example lint and the one runner for every gate this system owns. `benchmark/parity/` already confirms every declared mirror exists and every kernel statement stays where it is declared to live. `benchmark/format/` already confirms a delivered artifact has the right shape. Neither reads whether a rule stated in a skill document is the same rule stated in its Project mirror, so a mirror can drift in wording while both of those stay green.

Current state:

*   Three files: `rule_parity.py`, `example_lint.py` and `run_gates.sh`
*   `example_lint.py` runs the system validator in artifact mode over every worked example and every Project example mirror, and reads the worked replies in the Delivery Reply Shape section of the response templates asset and its mirror line by line
*   `run_gates.sh` runs the router fixtures, the format fixtures, rule parity, the example lint and its self-test, keeps going after a red gate and exits with the count of failures
*   It reads the 38 declared pairs for `product-owner` from the shared `z — Claude Project Sync Loop/systems.py`, never from a local map
*   It names six rules this system states and the verbatim spans that carry them, then counts each span on both sides of every pair
*   It never writes `systems.py`, and it never writes anything under `sk-product-owner/` or `claude project/knowledge/`

* * *

## 2. Files

| File | Responsibility |
|---|---|
| `rule_parity.py` | Loads `SYSTEMS['product-owner']['pairs']` from the shared declaration, reads each declared source and mirror, counts every rule phrase on both sides, and checks a floor per rule (how many pairs teach it today) |
| `example_lint.py` | Validates every example under `sk-product-owner/assets/examples/` and every `Product Owner - Examples - *.md` mirror with its preamble set aside, then checks each worked reply for the path line, the read-back line on the skill only, the self-scan and quality lines, the Open items shape and one closing line. `--self-test` breaks one example and one reply in a scratch copy and requires both to fail |
| `run_gates.sh` | Runs every gate above plus the router and format fixtures, prints `ok` or the failing gate's own output, and exits with the number of failed gates. The shared parity and residency checks stay in `benchmark/parity/`, because they refuse a declaration with uncommitted edits |

* * *

## 3. The six rules

Each rule names a verbatim span, chosen so a reader can grep for it and land on the lines this gate reads. A whole sentence is used where the exact statement is the contract, so a mirror cannot keep a keyword while reversing the rule around it.

| Rule | Span(s) | Read from | Pairs today |
|---|---|---|---|
| Requirement items close under the bold Checklist sub-label | `**Checklist**` | `references/task-mode.md:108` | 9 |
| Checklist and bullet items are never closed with a period | `Checklist and bullet items must not end with \`.\`` | `references/task-mode.md:110` | 1 |
| Acceptance criteria close with the mark-as-done checkbox | `_Mark as done, if the criteria are met_` | `references/story-mode.md:151` | 8 |
| Bug reports carry the two fixed corpus labels in order | `1. Observed Behavior`, `2. Expected Behavior` | `references/bug-mode.md:123` | 7 |
| The ClickUp definition delimiter is the named exception to the em-dash ban | `` *   **Term** — definition `` | `references/hvr-core.md:41`, `references/doc-mode.md:104` | 2 |
| Bullet items never end with a full stop | `Bullet items never end with a full stop.` | `references/hvr-core.md:35` | 1 |

The "pairs today" column is the floor `rule_parity.py` carries for that rule. A count below the floor fails even when every per-pair phrase count matches, because a rule can leave its only owning pair with both sides sitting at 0 and 0, which a pure equality check reads as agreement.

* * *

## 4. Why these six and not the Human Voice word or phrase lists

`references/hvr-core.md` and `references/human-voice-rules.md` also state the hard-blocker word list, the hard-blocker phrase list and the banned metaphors. Those are checked against actual reply text by `benchmark/grader/hvr_lint.py` instead, because that is a question about what a runtime wrote, not about whether the two documents agree on the rule. Rule parity here checks the declaration, and the linter in `benchmark/grader/` checks behavior. The two are not redundant. A mirror can state a rule correctly while a runtime still violates it, and a runtime can happen to comply while the mirror has quietly drifted.

* * *

## 5. Reading the shared declaration safely

Two things make `z — Claude Project Sync Loop/systems.py` unusual to read from another system's own tooling:

*   It is owned by a different, possibly concurrently running process. `rule_parity.py` reads it as source text and executes it into a private namespace (`sys.dont_write_bytecode = True`, then `compile` and `exec`) rather than `import systems`, so a normal import cannot leave a compiled `.pyc` behind under that directory's `__pycache__`
*   Four of this system's declared sources are shared rule files (`hvr-core.md`, `human-voice-rules.md`, `conciseness.md`, `conciseness-rationale.md`), carried as regular-file copies of cards in the shared knowledge tree. The path-containment guard stays lexical (`os.path.abspath`, never `os.path.realpath` or `Path.resolve()`), so a system that carries them as symlinks instead still reads each row through the link under the name the declaration gives it, rather than rejecting it as an escape from the skill root

* * *

## 6. Run

From the system root:

```bash
bash benchmark/gates/run_gates.sh
python3 benchmark/gates/rule_parity.py
python3 benchmark/gates/example_lint.py
python3 benchmark/gates/example_lint.py --self-test
```

The runner prints one line per gate and `all 5 gates pass` with exit 0 on a healthy tree. The example lint prints `PASSED N example files and the worked replies on both packagings`, or one line per finding naming the file and the real line, then `FAILED`. A run that finds no example file fails, because a lint that read nothing would print a pass it did not earn.

Expected result on a healthy tree: a pair count, a per-rule count against its floor, then `PASSED 6 rules hold on both sides of every pair that teaches them`. Exit 0.

A finding prints as `FAILED N rule parity finding(s)` followed by one line per finding, naming the rule, the phrase, the exact count on each side and both file paths. Exit 1.

### Testing against a sandbox instead of the real tree

`CW_ROOT` overrides where `sk-product-owner/` and `claude project/knowledge/` are read from, without changing where the shared declaration itself is read from:

```bash
CW_ROOT=/path/to/a/sandbox/copy python3 benchmark/gates/rule_parity.py
```

This is how this gate's own injection proof was run: a full sandbox copy of both trees was built with symlinks dereferenced (`cp -RL`, since a bare `cp -R` leaves the four symlinked sources dangling once they are outside `sk-product-owner/references/`), one file was edited inside the copy, and the real system directory was never touched.

* * *

## 7. Exit codes

| Exit | Meaning |
|---|---|
| 0 | every rule holds on both sides of every pair that teaches it, and every declared pair was readable |
| 1 | at least one rule parity finding, a count mismatch or a floor not met |
| 2 | the shared declaration could not be read or executed, `product-owner` is not declared, or it declares no pairs |

* * *

## 8. Related

*   [`../parity/README.md`](../parity/README.md), the wrappers into the shared gate that checks declaration completeness and kernel residency
*   [`../grader/README.md`](../grader/README.md), the reply linter and twin comparison this rule check does not replace
*   [`z — Claude Project Sync Loop/systems.py`](../../../z%20—%20Claude%20Project%20Sync%20Loop/systems.py), the shared declaration this gate reads and never writes
