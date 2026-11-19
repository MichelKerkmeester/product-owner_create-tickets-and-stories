# Grading brief addendum: third round `remeasure-supplied-values/run-1`

Read `grading-brief.md`, then `grading-brief-remeasure.md`, in this folder first. Everything in them holds for this round except what this addendum changes. `grading-brief-forecast.md` does not apply here.

## Gates, already answered

- Spec folder: `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/005-grading-and-report`. Do not ask about documentation.
- Nobody is at your prompt. Ask no question and wait for nothing. Where the evidence is thin, say so in your file.
- Write authority: exactly one file, the one your dispatch names under `scratch/grades/`. Read anything else, edit nothing else, run no git command that changes state, run no scenario.
- No em dashes anywhere in what you write.

## What changed

The first remeasure round left rows that dropped or reworded a supplied value. An investigation traced each miss (`scratch/miss-causes-tk003.md`, `scratch/miss-causes-tk005-tk006.md`, `scratch/miss-causes-docs-story.md`), the operator decided the changes on 2026-09-26, and this round reruns the affected pairs on them.

| Item | First round | This round |
|---|---|---|
| Run folder | `<RUN>/remeasure-operator-repairs/run-1/` | `<RUN>/remeasure-supplied-values/run-1/`, same layout |
| Product Owner commit | `39bcd29` | `b50f0a0` |
| Barter commit | `df2de5f0` | `7396d79e` |
| Playbook root | 2.1.0.0 | 2.2.0.0 |
| Skill, kernel | 1.11.0, v1.15.0 | 1.13.0, v1.16.0 |

Read every source at `b50f0a0`: the working tree is at that commit for every source and scenario file. Cite lines as they stand there.

## The rules under test

1. **Task Mode, both sides.** The Core Rules line that preserves source structure now also says a value, name or status a supplied source gives travels into the task as the source writes it, inside backticks: a value a requirement builds or checks (algorithm, header, endpoint, status code, count, range, timeout, schedule, threshold), an event, property or service name, and a status word such as `deprecated` or `proposed`. A supplied value is a constraint rather than HOW. A status keeps its word beside its meaning, and no generic stand-in replaces a named service (`sk-product-owner/references/task-mode.md` line 58, Project `Product Owner - Templates - Task Mode - v0.306.md` line 38). The Content Validation line asks for it (skill line 273, Project line 253)
2. **Doc Templates, both sides.** A Behavior reference keeps `## Behavior rules` as its primary body heading and puts the subject's wording in the H3s beneath it (skill `assets/doc-templates.md` line 116, Project `Product Owner - Assets - Doc Templates - v0.108.md` line 95). A phrase the source sets in backticks is literal copy and appears word for word in the sentence that states its rule, even where that sentence repeats its bold label (skill line 73, Project line 52)
3. **Story Mode, both sides.** An open question the source words itself is carried verbatim, so an `**Open:**` line quotes the source's question and then names who settles it (skill `references/story-mode.md` line 80, Project `Product Owner - Templates - Story Mode - v0.404.md` line 57)
4. **The root's verbatim rule, line 150.** A backticked value in a Pass clause is graded word for word where the source sets that value in backticks, gives it as a defined label such as a word from a status key, or the clause itself says verbatim for it. Elsewhere the same value stated in other words meets the clause. A value that is changed, generalized or left out still misses it. This replaces the orchestrator's earlier convention that every backticked value is word for word
5. **Relaxed clauses, both twins.** `long-be-integration-task.md` line 39 now asks for `event_id`, `X-Carrier-Signature`, `HMAC-SHA256` and `5 seconds` verbatim with any retry count or schedule the task states unchanged, and counts the Fulfilment board when the task or the reply's delivery or ClickUp line names it (Project: the block or the reply after it). `supplied-parent-subtask.md` line 39 lists `99` where it listed `1 to 99`. `proposal-decision-owner.md` line 39 accepts today's block-level last-writer-wins in the thread's words or restated

## Scenarios in this round

Both twins of `TK-003`, `TK-005`, `TK-006`, `DK-001`, `DK-003` and `ST-002`: 12 scenarios.

## What you return

The same shape as `grading-brief.md` section 3, into the file your dispatch names, with `model` `claude-opus-5-5-medium` and `after_failed_gate` `no` for every row, since no handover scenario is in this round and the last handover graded, round two's `PID-001`, passed. Add one line per scenario comparing it with its latest earlier verdict (round one's row where it exists, else the main run's): fixed, still failing for the same cause, or failing for a new cause. For every value named in the rules under test, say whether this round kept it, with the `file:line` that shows it.
