# Grading brief: Product Owner playbook run on claude-opus-5-5 medium

Every grader gets this brief. It fixes what is graded, against which text, with what evidence, and the shape of what you return. Where the root leaves a reading open, do not settle it: grade by the text, and list the open reading under "Open readings" so the orchestrator can put it to the operator.

## 1. Paths and commits

Workspace root: `/Users/michelkerkmeester/MEGA/Development/AI Systems`. Every path below is relative to it.

| What | Where |
|---|---|
| Product Owner system (nested git repo) | `AI Systems/Product Owner/` |
| Run folder, `<RUN>` | `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/` |
| Playbook root at the run commit | `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/005-grading-and-report/scratch/root-at-run.md`, line numbers identical to the committed root |
| Scenario files | `AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/<folder>/<slug>.md` |
| Fixtures (attachments) | `AI Systems/Product Owner/benchmark/fixtures/companies/<company>/` |
| Skill templates | `AI Systems/Product Owner/sk-product-owner/assets/` (`task-templates.md`, `bug-report-template.md`, `story-template.md`, `epic-template.md`, `doc-templates.md`, `interactive-response-templates.md`) and `references/*-mode.md` |
| Project templates | `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - * Mode - v*.md`, `Product Owner - Assets - * Template - v*.md` and the kernel `claude project/Custom Instructions.md` |
| Collected deliverables | `AI Systems/Product Owner/export/benchmark/` |
| Your draft output | `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/005-grading-and-report/scratch/grades/<batch>.md` |

The run used Product Owner commit `3023c5e` and Barter commit `c15c05e9`, and both working trees were clean for the sources. Read the working-tree files directly, and cite lines as they stand at `3023c5e`. If `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` prints anything, read with `git -C "AI Systems/Product Owner" show 3023c5e:<path>` instead.

Per scenario, inside `<RUN>`:

- `skill/<ID> - <slug>/` or `claude project/<ID> - <slug>/`: `turn-<n>.md` (the reply), `events-turn-<n>.jsonl` (the Claude event stream, every tool call and result), `transcript-turn-<n>.md`, `meta.json`, and on the skill side `exports/export/` (every file the runtime wrote) and `exports/context/` where present
- `replies/<ID>-turn<n>.txt`: the same reply text, what the linter reads
- `run-status.json` and `manifest.json` at the top

## 2. The rules

Read root sections 5 and 2 in `root-at-run.md` before grading anything: Company context and attachments (lines 79 to 98), Side-effect ledger (100 to 106), Scenario acceptance rules (142 to 150), Clarification turns (152 to 159), Rendering without a Canvas panel (161 to 163), Export names (165 to 171), Handovers in an automated run (173 to 175), Identity handover rule (177 to 179), Defect severity (181 to 196) and Ticket realism (198 to 214).

**Verdict.** Root line 150: a turn that misses any Pass clause fails the scenario, even when no Fail example names the miss. There is no verdict between `PASS` and `FAIL`. `SKIP` only for a named runtime blocker. The scenario file's `- Pass/fail:` contract bullet is the fullest statement of the Pass clauses. Grade every clause in it, and read Expected signals for what each clause means.

**Invented facts and named additions.** Root line 187. Something the attachments state is supplied, exactly like something the turns state: attachments are sources in this playbook. To keep the test objective, an item counts as an addition only when it adds a capability, flow, message, validation rule, value, scope boundary or claim about current behavior that neither the turns nor the attached files contain. The direct test or negation of a supplied condition is not an addition. An addition is invented only when no naming line in the chat response covers it. A line that names a criterion or other whole item as an addition covers every clause inside it. A line describing one behavior covers that behavior only. Naming never excuses an invented status, approval, evidence, root cause or platform detail. A root cause labelled as an unverified hypothesis is not invented. Items between the two readings are listed as borderline and never decide a verdict alone.

**Protected facts.** Every hard value the scenario lists as verbatim must appear verbatim. A supplied value generalized, a conflict silently resolved, or a proposal promoted to current behavior is blocking (root line 188).

**Skill delivery proof.** A read-back claim is true only when the event stream shows a Read of that exact export path after the last Write or Edit to it, and that Read returned file content. Record the `N` the reply printed beside the line range the Read returned and the file's real line count (`wc -l`). A wrong `N` alone is recorded, not failed, unless the scenario's Pass clause makes the count a condition. List any wrong `N` under Open readings.

**Project delivery proof.** Rendering without a Canvas panel, root line 163. Record which form the block took (fenced, or opened by its own heading). Commentary before a block is advisory except in `PID-001`. Any claim that a file was saved, written or read back on the Project side is blocking.

**Format gate.** For every skill export and every Project block, run the shared format gate and record its result:

```bash
cd "$(ls -d "/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems"/z*Sync\ Loop)"
node validate-output-format.cjs --system product-owner "<absolute path to the file>"
```

For a Project block, copy the block's text out of the reply into a file under your `scratch/grades/blocks/` folder first and run the gate on that. A format gate finding is evidence. It decides a verdict only through a Pass clause or the Ticket realism item "A required section of the routed template missing".

**Ticket realism.** Root lines 198 to 214. Blocking: wrong artifact word, a required section of the routed template missing (read from that runtime's own template: the skill asset for `S`, the Project knowledge mirror for `P`), an invented fact, placeholder or toy content, context facts ignored or altered. Advisory: size band, commentary, asking for a fact an attachment already states, a Task or Bug title with no discipline code. The two exemptions: a placeholder quoted verbatim from an attached source (`Conflicting edit from {device name}` in the Loomlist sync thread) is not toy content, and the exempt fixed slots the root lists.

**Handovers.** Grade every scenario whatever the handovers return. Leave `after_failed_gate` as `pending` in every row: the orchestrator fills it once both handover verdicts are settled.

## 3. What you return

Write one Markdown file, `scratch/grades/<batch>.md`, and end your final message with its path and a one-line tally (PASS and FAIL per runtime). Use no em dashes anywhere. In it, per scenario, in ID order, skill then Project:

1. **Draft row**, one CSV line with exactly these nine columns in order: `id,runtime,model,result,turns_run,turns_declared,after_failed_gate,facts_intact,note`. `runtime` is `skill` or `project`, `model` is `claude-opus-5-5-medium`, `result` is `PASS`, `FAIL` or `SKIP`, `turns_run` and `turns_declared` from `run-status.json`, `after_failed_gate` is `pending`, `facts_intact` is `yes` when every supplied fact reached the deliverable unaltered and `no` otherwise. `note` is one quoted sentence or two: what decided the verdict and where, and any advisory item. Double any `"` inside the note.
2. **Pass clauses**: a table, one row per clause of the `- Pass/fail:` bullet, with Met or Unmet and the evidence that decides it: a reply line (`turn-2.md` line 14), a stream event (the Read of that path, lines returned), or a file line (`export/004 - task-....md` line 31).
3. **Blocking items hit**, each with the rule and its root line, or "None".
4. **Advisory items**, or "None".
5. **Read-back table** (skill only): turn, export path, `N` printed, the Read after the last write and the lines it returned, real `wc -l`.
6. **Realism entry per export** (one per skill file written, one per Project block): path or block, kind, the routed template's required sections present or missing, three or more company facts checked against the fixture with the fixture line, any placeholder, the body line count against the scenario's size band (advisory), and a Task or Bug title's discipline code (advisory).
7. **Open readings**: anything the root leaves open that your verdict touched, stated as a question the operator can answer.

Then, after all scenarios, a **Twin notes** section: for each pair in your batch, agree or differ, and when they differ, whether the cause looks like a rule gap (the two packagings say different things), a parity gap (one packaging lacks a rule the other has) or a runtime fault (both say the same and one runtime did not follow it), with the rule lines on both sides.

## 4. Limits

- Read only. Do not edit, move or delete anything outside `scratch/grades/`. Never touch `export/`, the run folder, the fixtures or any source
- Do not run the runner, the collector or any `claude` command, and never pass `--write` to the format gate
- Quote evidence, never paraphrase a value you are checking
- If a file you need is missing, say which and grade what the evidence supports
