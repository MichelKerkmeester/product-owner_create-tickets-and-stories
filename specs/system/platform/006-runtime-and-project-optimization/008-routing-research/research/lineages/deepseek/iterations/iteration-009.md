# Iteration 9: Code standards: the Product Owner's own Python, shell, JavaScript and JSON

## Focus
Question 9: hold the system's own code to the sk-code-skilled standards it claims to follow. Read the Python, shell, JavaScript and config quality standards in .skilled/skills/sk-code/sk-code-skilled/references/, then ran the checks they name against 22 Python files, 9 shell scripts, 2 CommonJS files and 10 JSON files, excluding benchmark/reports/, node_modules, vendored packets and the generated plugin copy.

## Findings
1. The code is sound where soundness is checkable. All 22 Python files compile; none has a bare except, a mutable default argument or shell=True; both CommonJS files pass node --check; all 10 in-scope JSON files parse, none holds a tab and every one ends with a newline. The three errors a refactor would introduce most easily are absent. Fix: none. [SOURCE: AI Systems/Product Owner/benchmark/gates/check_hub.py:1-40] [SOURCE: AI Systems/Product Owner/scripts/vendor-sync.py:1-50]
2. Shell is shellcheck-clean and strict-mode non-compliant at the same time: shellcheck reports zero findings at info level across all nine scripts, quoting included, yet every one runs set -uo pipefail and none sets -e, while the standard says every script must enable set -euo pipefail. The behaviour is deliberate, because a gate runner must run every gate and count failures, and run_gates.sh's header says exactly that, but no script carries the one line that names the deviation from the standard. Fix: add that line to the nine headers; do not add -e, which would break the counting. [SOURCE: AI Systems/Product Owner/benchmark/gates/run_gates.sh:1-30] [SOURCE: AI Systems/Product Owner/benchmark/format/run_fixtures.sh:28] [SOURCE: .skilled/skills/sk-code/sk-code-skilled/references/shell/quality-standards/overview-and-priority-blockers.md:55-70]
3. The format gate, the largest CommonJS file in the system at 1,702 lines, does not declare 'use strict', while the 60-line Code Mode server does. The standard requires CommonJS .js and .cjs modules to declare it, and this is the one file where an accidental global would be hardest to trace. Fix: benchmark/format/validate-output-format.cjs line 1. [SOURCE: AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:1-15] [SOURCE: AI Systems/Product Owner/scripts/code-mode.cjs:20] [SOURCE: .skilled/skills/sk-code/sk-code-skilled/references/javascript/quality-standards/overview-modules-and-docs.md:43-53]
4. Fifty-nine Python lines exceed the standard's 120-character maximum across 12 files, after exempting the box-drawing header lines. The worst are route_contract.py with 15 and check_hub.py with 16; two regex constructions run to 260 and 145 characters, so the length is the price of a legible pattern rather than sloppy wrapping. Fix: none required for the regexes, or extract the three long patterns into named fragments. [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:295] [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:314] [SOURCE: AI Systems/Product Owner/benchmark/gates/check_hub.py:63] [SOURCE: .skilled/skills/sk-code/sk-code-skilled/references/python/quality-standards.md:271-275]
5. Type hints are complete in 18 of 22 Python files and missing in four. hvr_lint.py annotates no return on any of its five functions and annotates arguments on only two; rule_parity.py annotates 1 of 4; twin_divergence.py 1 of 2. The standard asks for type hints on every function signature, and these four are the grader and parity modules a reader is most likely to call from another script. Fix: annotate hvr_lint.py first. [SOURCE: AI Systems/Product Owner/benchmark/grader/hvr_lint.py:151] [SOURCE: AI Systems/Product Owner/benchmark/grader/hvr_lint.py:168] [SOURCE: AI Systems/Product Owner/benchmark/grader/hvr_lint.py:199] [SOURCE: .skilled/skills/sk-code/sk-code-skilled/references/python/quality-standards.md:139-141]
6. extract_deliverable(raw: str) annotates its argument and not its return, which is the half-signature a caller trusts most and the one a type checker cannot use. The same shape appears in lint(text: str, confidence: str = "high"), fully annotated on the way in and silent on the way out. Fix: add the return types; the functions return str, list[tuple[int, str]] and int respectively. [SOURCE: AI Systems/Product Owner/benchmark/grader/hvr_lint.py:151] [SOURCE: AI Systems/Product Owner/benchmark/grader/hvr_lint.py:199]
7. Only one of 22 Python modules has an external test file, scripts/tests/test_vendor_sync.py, and it covers the vendoring script rather than the router or the gates. Behaviour coverage instead lives in planted fixtures inside each gate: check_hub, example_lint, route_contract and flow_check all carry a self-test that a deliberately broken input must fail. That is a legitimate pattern, and it is stronger than a smoke test, but nothing runs those self-tests together except the individual rows in run_gates.sh, so a new gate can be added without one. Fix: state the self-test requirement in run_gates.sh beside the list. [SOURCE: AI Systems/Product Owner/scripts/tests/test_vendor_sync.py:1-20] [SOURCE: AI Systems/Product Owner/benchmark/gates/run_gates.sh:41-54]
8. The exit-code discipline is the strongest part of the code and is documented where it is most easily got wrong: check_report.sh reserves 64 for no argument and 66 for a missing directory specifically because 1 and 2 already mean one and two findings, and validate-output-format.cjs uses 64 and 66 for the same two cases, so a caller reads the same code the same way in both languages. Fix: none; treat as the pattern new scripts copy. [SOURCE: AI Systems/Product Owner/benchmark/grader/check_report.sh:23-46] [SOURCE: AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:24-31]

## Ruled Out
- Calling the nine missing -e flags a defect: a runner that must count failures cannot exit on the first one, and run_gates.sh documents the counting behaviour
- Treating the 191-character component headers as line-length violations: they are the house header rule, and the 59 remaining lines are measured with comment lines exempted
- Treating unquoted-variable style as weak: shellcheck at info level reports nothing on any of the nine scripts

## Dead Ends
- Searching for a Python stderr or exit-code rule in the standard: the standard states neither, so printing gate findings to stdout and using exit codes is not a deviation
- Looking for tabs or missing trailing newlines in JSON: none in ten files

## Edge Cases
- Ambiguous input: The vendored mermaid_extract.py and the generated plugin copy are excluded because neither is edited here; their standards compliance belongs upstream
- Contradictory evidence: The shell standard mandates -e while the repository's gate design forbids it; the behaviour is right and the documentation of the choice is what is missing
- Missing dependencies: No linter configuration exists in the repository, so these checks are what a reader runs by hand, not what a gate enforces
- Partial success: Line length and annotation counts are lexical measurements, not a type check

## Sources Consulted
- specs/z-staging-po-019s/research/lineages/deepseek/steer.md
- .skilled/skills/sk-code/sk-code-skilled/references/python/quality-standards.md
- .skilled/skills/sk-code/sk-code-skilled/references/shell/quality-standards/overview-and-priority-blockers.md
- .skilled/skills/sk-code/sk-code-skilled/references/javascript/quality-standards/overview-modules-and-docs.md
- AI Systems/Product Owner/benchmark/gates/run_gates.sh
- AI Systems/Product Owner/benchmark/gates/check_hub.py
- AI Systems/Product Owner/benchmark/gates/rule_parity.py
- AI Systems/Product Owner/benchmark/grader/hvr_lint.py
- AI Systems/Product Owner/benchmark/grader/check_report.sh
- AI Systems/Product Owner/benchmark/grader/twin_divergence.py
- AI Systems/Product Owner/benchmark/router/route_contract.py
- AI Systems/Product Owner/benchmark/format/validate-output-format.cjs
- AI Systems/Product Owner/benchmark/format/run_fixtures.sh
- AI Systems/Product Owner/scripts/code-mode.cjs
- AI Systems/Product Owner/scripts/vendor-sync.py
- AI Systems/Product Owner/scripts/tests/test_vendor_sync.py

## Assessment
- New information ratio: 0.6
- Questions addressed: How does the Product Owner's own Python, shell, JavaScript and JSON deviate from the sk-code-skilled standards?
- Questions answered: How does the Product Owner's own Python, shell, JavaScript and JSON deviate from the sk-code-skilled standards?

## Reflection
- What worked and why: Reading the standards first and then running exactly the checks they name turned a vague style question into six named deviations and three clean results
- What did not work and why: The first pass walked the whole tree and spent its output on specs containment copies and node_modules, which are neither in scope nor edited here
- What I would do differently: Bound the file set to the folders the system owns before running any tree-wide check, and exclude comment lines from length measurements

## Questions Remaining
- What is the ranked synthesis of every finding, and what can the repository not settle?

## Recommended Next Focus
Question 10: synthesis. Rank every verified finding from iterations 1 to 9 by cost and confidence, name the files to change, state what the repository cannot settle, and write the close-out.
