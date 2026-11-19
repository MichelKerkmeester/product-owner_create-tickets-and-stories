# Brief: find the cause of each content miss

The operator chose on 2026-09-26 to look for the source cause of the rows that still fail on a dropped or reworded value, propose rule changes for the operator's decision, and then rerun those rows. This brief covers the read-only investigation only. Nothing in the repository is edited from it.

## Gates, already answered

- Spec folder: `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/005-grading-and-report`. Do not ask about documentation.
- Nobody is at your prompt. Ask no question and wait for nothing. Where the evidence is thin, say so in your file.
- Write authority: exactly one file, the one your dispatch names under `scratch/`. Read anything else, edit nothing else, run no git command that changes state, run no scenario.
- No em dashes anywhere in what you write.

## Where things are

All paths below are relative to `AI Systems/Product Owner/` unless they start with `specs/`.

| What | Path |
| --- | --- |
| Skill sources | `AGENTS.md`, `sk-product-owner/SKILL.md`, `sk-product-owner/references/*.md`, `sk-product-owner/assets/*.md` |
| Project sources | `claude project/Custom Instructions.md` (the kernel), `claude project/knowledge/*.md` |
| Playbook root | `sk-product-owner/manual-testing-playbook/manual-testing-playbook.md`, grading rules at lines 150 and 185 to 214 |
| Scenario files | `sk-product-owner/manual-testing-playbook/skill-*/` and `project-*/`, the Project twin under the matching `project-*` folder with the same file name |
| Fixtures | `benchmark/fixtures/companies/<company>/`, named in each scenario's `- Attachments:` bullet |
| Main run, on commit `3023c5e` | `benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`: `replies/<ID>-turn<n>.txt`, `results.csv`, `grading-notes.md` |
| Round one, on commit `39bcd29` | the same folder's `remeasure-operator-repairs/run-1/`: `replies/`, `results.csv`, `grading-notes.md` |
| Round two, on commit `b591571` | the same folder's `remeasure-file-forecast/run-1/` (Project rows only) |
| Skill exports | `export/benchmark/skill/` for the main run, `export/benchmark/skill/remeasure-operator-repairs/run-1/` for round one |

The content rules the runtimes saw did not change between `3023c5e` and `b591571` except where `git -C "AI Systems/Product Owner" diff 3023c5e b591571 -- <file>` shows it. The working tree today equals `b591571` for every source file. Check a diff before you cite a line for an older run.

Rules found so far that mention carrying a value unchanged, as starting points and not as a conclusion: `sk-product-owner/references/story-mode.md` lines 75 and 80, `sk-product-owner/SKILL.md` line 268, `AGENTS.md` line 270, `sk-product-owner/references/quality-scoring.md` line 155, and playbook root line 188. Search further. There may be others, and there may be none for your artifact kind.

## The question, for each miss your dispatch names

1. **The source.** The exact text of the value in the fixture or the turn that supplies it, with `file:line`.
2. **The demand.** The Pass clause that requires it, quoted, with the scenario `file:line`.
3. **What was written.** What each runtime wrote in its place, in every run where the row appears, with `file:line` in the reply or export. Say which runs kept it and which did not.
4. **The rules.** Every rule, skill side and Project side, that requires carrying this kind of value unchanged into this artifact kind, quoted with `file:line`. Then every rule that pushes the other way: rewording source prose, condensing, a template slot that renames or reshapes it, voice rules, size bands. Say plainly if no rule for this artifact kind protects it.
5. **The cause class**, exactly one, with the evidence that decides it:
   - `rule gap`: no rule for this artifact kind requires the value to travel unchanged
   - `rule conflict`: a rule the runtime followed pushed it to drop or reword the value
   - `runtime fault`: a clear rule required it and the runtime did not follow it
   - `scenario defect`: the Pass clause demands something no rule requires and the source does not make binding
   Then one line on what evidence would move it to another class.
6. **The smallest change that would remove the cause**, only for `rule gap`, `rule conflict` or `scenario defect`: the file and line, the current text quoted, the proposed text, and its counterpart in the other packaging (skill source and Project kernel or knowledge mirror). For `runtime fault`, propose no rule change, and say whether anything in the sources makes the fault likelier.

## The shape of the return

Your file opens with a table of one row per miss: `Row`, `Value`, `Kept in`, `Dropped in`, `Class`, `Change in one line`. Then one section per miss answering questions 1 to 6. Cite `file:line` for every claim. Quote rather than paraphrase. Mark as inference anything you did not read.

Your final message is the path of your file and the table, nothing else.
