# Skill-side ask-first check: Product Owner Skill v1.16.2 on DeepSeek V4.1 Flash at thinking high

Skill v1.16.2 adds the kernel's two ask-first triggers to `AGENTS.md` and `SKILL.md` for every artifact kind: a source the user promised but has not sent, and a decision the user calls unsettled. This run checks the three skill-side scenarios those triggers touch, each of which requires a saved clarification and no draft on turn 1.

- **Model:** `opencode-go/deepseek-v4.1-flash`, thinking high, through `run/pi_playbook_runner.py` with `--side skill`
- **Rules under test:** `AGENTS.md` and `sk-product-owner/` at Skill v1.16.2, before commit. The `stk-head-<N>` runs use a detached worktree at HEAD `541b8955`, Skill v1.16.1
- **Grader:** Claude Opus 5.5 in Claude Code, reading which file turn 1 saved. A `-clarification` file means the scenario asked first

## Results

| Scenario | Skill v1.16.2 | Skill v1.16.1 (HEAD) |
|---|---|---|
| SST-001 Story | 2 of 2 ask first (`run-1`, `run-2`) | not run |
| SEP-002 Epic | 2 of 2 ask first (`run-1`, `run-2`) | not run |
| STK-006 Task | 3 of 5 ask first (`run-1`, `stk-new-3`, `stk-new-5`), drafted in `run-2` and `stk-new-4` | 1 of 3 ask first (`stk-head-1`), drafted in `stk-head-2` and `stk-head-3` |

## Reading

The new triggers do not make the skill side ask less. STK-006 drafts a full task in some runs on both versions, so the skill-side Task case is unreliable on DeepSeek before and after this change. The Project side asks first in 12 of 12 samples of the same three scenarios on kernel v1.21.0, in `../2026-10-01--kernel-diet--deepseek-v4-1-flash-high/`. Closing the skill-side Task gap is a separate change to the Task Mode reference, left for the operator's decision.

## Files

- `run-<N>/replies/`, `stk-new-<N>/replies/`, `stk-head-<N>/replies/`: `<ID>-turn<N>.txt` per turn
- `run-log.jsonl`, `manifest.json` and `stdout.txt` in each folder hold the session records
