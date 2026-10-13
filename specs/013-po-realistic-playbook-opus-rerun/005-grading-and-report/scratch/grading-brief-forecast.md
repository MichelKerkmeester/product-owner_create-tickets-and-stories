# Grading brief addendum: second round `remeasure-file-forecast/run-1`

Read `grading-brief.md`, then `grading-brief-remeasure.md`, in this folder first. Everything in them holds for this round except what this addendum changes.

## What changed

The first remeasure round showed the Project runtime still naming a path or a file for an artifact still to come in eight rows. The operator chose one more repair, and this round reruns those eight on it.

| Item | First round | This round |
|---|---|---|
| Run folder | `<RUN>/remeasure-operator-repairs/run-1/` | `<RUN>/remeasure-file-forecast/run-1/`, same layout |
| Product Owner commit | `39bcd29` | `b591571` |
| Barter commit | `df2de5f0` | `e9eec279` |
| Playbook | 2.1.0.0 | 2.1.1.0 |
| Skill, kernel | 1.11.0, v1.15.0 | 1.12.0, v1.16.0 |

Read every source at `b591571`: the working tree is at that commit and clean for the sources. Cite lines as they stand there.

## The rule under test

Kernel line 101 (NEVER 3) now says the Project never says it saved, verified, read back, pushed, will write, will save or will update a file, and a reply names only the export-equivalent label of the block it renders, never a path or file for an artifact still to come. Kernel line 228 and the Interactive Mode knowledge file line 70 say a clarification reply says the artifact comes next once the user answers, without naming its path or file. Root lines 179 and 189 count both a promise to write or save a file and a forecast path for the next artifact, such as "the task will be `export/002 - ...`", as a file claim.

The dividing line from the first round holds: a forward statement that attaches an `export/` path or the word file to the next artifact is a claim, and one that names only the next number is not. The block's own `Export-equivalent path:` label for the block rendered in that reply is never a claim.

## Scenarios in this round

`PID-001`, `PBG-002`, `PTK-005`, `PTK-006`, `PST-003`, `PST-004`, `PEP-001` and `PEP-002`, all Project side. `PID-001` is the handover: say plainly whether it passes.

## What you return

The same shape as before, into `scratch/grades/forecast.md`, with `after_failed_gate` left as `pending`. Add one line per scenario comparing it with its first-round verdict in `<RUN>/remeasure-operator-repairs/run-1/results.csv`: fixed, still failing for the same cause, or failing for a new cause.
