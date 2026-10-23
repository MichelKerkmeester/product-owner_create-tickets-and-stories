# Kernel dedupe check: Product Owner kernel v1.2.2 on DeepSeek V4.1 Flash at thinking high

The kernel dropped from 75,165 to 68,758 bytes. The cut removed table padding and rules the kernel stated twice, and it kept every rule and left Section 11, Router Code, byte-identical. This run asks the 2026-10-01 kernel-diet questions again: does DeepSeek still ask first where a scenario requires it, and do routing, intake and identity hold? It also adds `PFL-001`, the Project Flow scenario, which the earlier run predates.

- **Model:** `llmgateway/deepseek-v4.1-flash`, thinking high, through `run/pi_playbook_runner.py` with `--side project`
- **Rules under test:** `claude project/Custom Instructions.md` at v1.2.2, before commit, 68,814 bytes after the fix below
- **Grader:** Claude Opus 5.5 in Claude Code, reading each scenario's pass and fail lines against the replies and checking the required values by search. No second grader read this run.

## Harness changes

- **Provider:** the baseline used `opencode-go`, which answered every call with a 429 on this day. Those attempts are kept in `transport-429/` and carry no verdict. The same model through `llmgateway` ran every session on its first attempt.
- **Skill folder:** the repository root now holds `sk-create-figjam` beside `sk-product-owner`. The runner took the first `sk-` folder it listed, so this copy picks the folder that holds the root playbook and is not an `sk-create-` packet, in `load_playbook` and `load_waves`.

## Ask-first samples

`PTK-006`, `PST-001` and `PEP-002` each require one question and no draft on turn 1. They ran four times in sequence, in `ask-first-1` to `ask-first-4`.

| Run | PTK-006 | PST-001 | PEP-002 |
|---|---|---|---|
| ask-first-1 | asks | asks | asks |
| ask-first-2 | asks | asks | asks |
| ask-first-3 | asks | asks | asks |
| ask-first-4 | asks | asks | asks |

All 12 turn-1 replies render one question block under a `-clarification` label, carry the `HVR self-scan:` line and a recommendation per point, and hold no draft. All 12 turn-2 replies render the artifact with its path and self-scan lines and no file claim. In every `PEP-002` draft the `# Epic - ` H1, `## Scope`, `23%`, `31%` and `2026-10-09` are present and `## Requirements` is absent. Every `PTK-006` draft has `### Requirements`, `booking_confirmed`, the `checkout_complete` removal on `2026-11-01` and `date_changed`. Every `PST-001` draft has `## Problem`, `## Solution`, `## Requirements`, the local-date badge and the filter kept on the way back to results. This matches the baseline's 12 of 12.

## Other scenarios

All six sessions in `others` ended `ok` on their first attempt.

| ID | What it checks | Observed | Verdict |
|---|---|---|---|
| PID-001 | Project identity, task lane labels | Turn 1 asks under the `task` clarification label, turn 2 renders the Web task with `## About`, `### Requirements`, the owner's time zone and the supplied `filter_selected` value | PASS |
| PBG-001 | Quick bug renders at once | One bug block with no question, `Always`, `Medium`, `iOS 4.8.0`, `Not provided` for Device and OS Version, expected badge "2" | PASS |
| PIR-001 | Vague intake asks energy and kind first | Energy first, then the deliverable type, then an Epic with the four child stories, `19%`, `25%`, `12 months`, 2027 and Pay now, and no point value | PASS |
| PIR-002 | Conflicting deliverables get one question | One question naming Bug and Story, then a Story with the `50` item limit and the most-recently-added rule | PASS |
| PDK-001 | Behavior reference renders without a question | Doc block on both turns, every value verbatim, `* * *` under every content heading, no hyphen bullets or `---` inside the document, the two-code rule labelled retired since `2026-05-01` on turn 2 | PASS |
| PFL-001 | Flow with no Figma connector | Turn 1 prints `Read-back: not possible, the connector has no read tool` with nothing written, which the fail line names | FAIL, then fixed below |

## The PFL-001 finding

To tell a regression from an old defect, PFL-001 ran three times on each kernel, the old one from a scratch copy of the system.

| Kernel | Turn 1 | Verdict | Folders |
|---|---|---|---|
| Before the cut, 75,165 bytes | Intake rounds, a question every time, no fenced model | 0 of 3 | `pfl-old-kernel-1` to `-3` |
| After the cut | The fenced model at once, with a `Read-back:` line every time | 0 of 3 | `pfl-new-kernel-1` to `-3` |
| After the cut plus one clause | The fenced model, no `Read-back:` line | 2 of 3 | `pfl-fixed-kernel-1` to `-3` |

The cut did not create the failure, since the old kernel failed every sample too, but it changed its form. The clause added to the kernel's no-connector bullet reads "print no `Read-back:` line because nothing was written". With it, all three turn-1 replies drop the line and every model passes `flow_check.py`. The one remaining fail, `pfl-fixed-kernel-1`, asks the reader question on turn 1, which the old kernel did in all three samples, because Flow Mode Delivery opens a run with intake rounds.

## Files

- `ask-first-<N>/replies/<ID>-turn<N>.txt`, `others/replies/<ID>-turn<N>.txt` and `pfl-*/replies/PFL-001-turn<N>.txt` hold the replies
- `run-log.jsonl`, `manifest.json` and `<folder>.stdout.txt` hold the session records
- `transport-429/` holds the attempts the `opencode-go` quota refused
