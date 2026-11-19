# Grading brief addendum: remeasure round `remeasure-operator-repairs/run-1`

Read `grading-brief.md` in this folder first. Everything in it holds for this round except what this addendum changes.

## What changed

The round reran 26 scenarios after the operator's rulings of 2026-09-25 were repaired in the sources, to see whether the repairs change what the runtimes do.

| Item | Main run | This round |
|---|---|---|
| Run folder | `<RUN>` | `<RUN>/remeasure-operator-repairs/run-1/`, same layout: `skill/`, `claude project/`, `replies/`, `run-status.json`, `manifest.json` |
| Product Owner commit | `3023c5e` | `39bcd29` |
| Barter commit | `c15c05e9` | `df2de5f0` |
| Playbook | 2.0.0.0 | 2.1.0.0 |
| Skill, kernel | 1.10.0, v1.14.0 | 1.11.0, v1.15.0 |

Read every source at `39bcd29`: the working tree is at that commit and clean for `sk-product-owner`, `claude project`, `AGENTS.md` and `benchmark/fixtures`. Cite root and source lines as they stand there. Write a fresh copy of the root with `git -C "AI Systems/Product Owner" show 39bcd29:sk-product-owner/manual-testing-playbook/manual-testing-playbook.md` if you want a fixed file to cite.

## The rulings, now in the text

1. An explicit command (`$task`, `$bug`, `$doc`, `$story`, `$epic` and every short alias) asks its question first and waits, however much context the request carries. Only `$quick` or `$q` skips routine intake (`AGENTS.md` line 287, kernel line 108, the Bug, Story and Doc Mode intake lines)
2. An Epic omits `#### **References**` when no link is supplied, never writing it empty or with an invented link
3. On the Project side, a promise to write or save a file is a file claim (root lines 179 and 189, kernel line 101)
4. `SDK-001` and `PDK-001` now expect a direct draft on Turn 1 and a follow-up change on Turn 2. Whether Turn 2 updates the earlier export in place or saves the next number is not graded
5. A cause labelled as an unverified hypothesis is not a stated root cause
6. With no error message supplied, the bug's error line reads `Not provided` or is left out, never asserting that none appears
7. A runbook's general "Expected result" lines drawn from an incident are allowed, and `Status: Approved direction` is a Doc Mode class, not an invented approval

## Scenarios in this round

Both twins of `TK-002` to `TK-005`, `BG-002`, `DK-001`, `DK-003`, `ST-002` to `ST-004` and `EP-001`, plus `PID-001`, `PEP-002`, `PTK-006` and `PIR-002`: 26 scenarios.

## What you return

The same shape as `grading-brief.md` section 3, into `scratch/grades/remeasure-<batch>.md`, with `model` `claude-opus-5-5-medium` and `after_failed_gate` left as `pending`: the orchestrator fills it once this round's `PID-001` verdict is settled. Add one line per scenario comparing it with its main-run verdict in `<RUN>/results.csv`: fixed, still failing for the same cause, or failing for a new cause.
