# Kernel diet check: Product Owner kernel v1.21.0 on DeepSeek V4.1 Flash at thinking high

Kernel v1.21.0 drops from 70,557 to 61,977 characters by trimming tables alone: the padding, the Resource Loading Levels table, the Smart Routing Matrix and the first Executable Contract paragraph. No rule left the kernel, and Section 11, Router Code, is byte-identical to v1.20.0. The question was whether DeepSeek still asks first where a scenario requires it, the behavior the 2026-09-30 run had to reinforce, and whether routing, intake and identity hold on the smaller kernel.

- **Model:** `opencode-go/deepseek-v4.1-flash`, thinking high, through `run/pi_playbook_runner.py` with `--side project`, the runner copy from the 2026-09-30 report that stages the company fixtures
- **Rules under test:** `claude project/Custom Instructions.md` v1.21.0, before commit
- **Grader:** Claude Opus 5.5 in Claude Code, reading each scenario's pass and fail lines against the replies and checking the required values by search. No second grader read this run.

## Ask-first samples

`PTK-006`, `PST-001` and `PEP-002` each require one question and no draft on turn 1. They ran four times in sequence, in `ask-first-1` to `ask-first-4`.

| Run | PTK-006 | PST-001 | PEP-002 |
|---|---|---|---|
| ask-first-1 | asks | asks | asks |
| ask-first-2 | asks | asks | asks |
| ask-first-3 | asks | asks | asks |
| ask-first-4 | asks | asks | asks |

12 of 12 turn-1 replies render one question block under a `-clarification` label and hold no draft section. Some ask in the imperative, "Send both" or "Confirm whether", rather than with a question mark. Each was read to confirm it asks before drafting.

## Other scenarios

All five sessions in `others` ended `ok` on their first attempt.

| ID | What it checks | Observed | Verdict |
|---|---|---|---|
| PID-001 | Project identity, task lane labels | Turn 1 asks under the `task` clarification label, turn 2 renders the task, both carry the path and `HVR self-scan:` lines and claim no file | PASS |
| PBG-001 | Quick bug renders at once | One bug block on turn 1 with no question | PASS |
| PIR-001 | Vague intake asks energy and kind first | One question naming energy and deliverable type, then an Epic carrying `19%`, `25%`, `12 months`, 2027 and Pay now | PASS |
| PIR-002 | Conflicting deliverables get one question | One question naming Bug and Story, then a Story with the `50` item limit and the most-recently-added rule | PASS |
| PDK-001 | Behavior reference renders without a question | Doc block with an Overview and `## Behavior rules` on both turns | PASS |

## Files

- `ask-first-<N>/replies/<ID>-turn<N>.txt` and `others/replies/<ID>-turn<N>.txt` hold the replies
- `run-log.jsonl`, `manifest.json` and `stdout.txt` in each folder hold the session records
