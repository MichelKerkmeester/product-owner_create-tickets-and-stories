# Skill trim check: Product Owner Skill v1.16.4.0 against v1.16.3.0 on DeepSeek V4.1 Flash at thinking high

Skill v1.16.4.0 cuts `SKILL.md` from 7,814 to under 5,000 words by pointing at the mode references that already carry the detail on the same route. This run puts all 23 skill-side playbook scenarios through the new `SKILL.md` and through a copy holding the old one, then compares the two runs scenario by scenario, to show the cut lost no rule.

- **Model:** `opencode-go/deepseek-v4.1-flash`, thinking high, through `run/pi_playbook_runner.py` with `--side skill`, one sample per scenario per side
- **after:** the working tree at Skill v1.16.4.0, before commit
- **before:** a scratch copy of the same tree with the old `SKILL.md` and the worked examples' old frontmatter put back, so `SKILL.md` is the one difference that matters
- **Comparison:** `run/compare_runs.py`, mechanical only. Per scenario it reads what each turn saved, whether turn 1 saved only a clarification, whether every reply carries the `Verified:` read-back line and the `HVR self-scan:` line, how many backticked values from the scenario's Expected signals appear in the final deliverables, and what `validate-output-format.cjs --system product-owner` says about each deliverable

## Results

| Measure | after (v1.16.4.0) | before (v1.16.3.0) |
|---|---|---|
| Scenarios completed | 23 of 23 | 23 of 23 |
| Expected values found in the deliverables | 189 of 222 | 189 of 222 |
| Deliverables the format gate fails | 1 (SDK-001) | 1 (SDK-001) |
| Turn 1 saved only a clarification | 19 | 16 |
| Turns carrying the `Verified:` read-back line, plain or bold | 43 of 43 | 42 of 43 |
| Scenarios where every turn carries `HVR self-scan:` | 23 | 22 |

Rows where the two runs differ, from `compare.txt`:

| Scenario | Difference | Reading |
|---|---|---|
| SST-003, STK-002, STK-004 | after asked on turn 1, before drafted | The scenarios require the ask, so after passes and before fails all three |
| SDK-003 | before turn 2 has no read-back or self-scan line | A before-side miss |
| SEP-001, SEP-003, STK-001 | flagged on the read-back line in after | The line is there in bold, `**Verified:**`, which the exact-match check misses. The count above reads both forms |
| SBG-002, SBG-003, SST-002, STK-002, STK-003, SDK-001 | one or two expected values differ | Values each side missed are facts from the scenario input, such as `14 nights` or `context/`, none of them text either `SKILL.md` carries. Each side misses some the other found, and the totals tie |

## Reading

The cut lost no rule these scenarios exercise. Every scenario the old `SKILL.md` passed on a rule it stated, the new one passes too, and the three ask-first scenarios that differ go the new side's way. The old file's second statement of the read-back line was the nested-Story detail, which now lives in `sk-product-owner/references/story-mode.md` on the route that needs it.

Two caveats bound this reading. It is one DeepSeek sample per scenario per side, and the 2026-10-01 ask-first run showed single samples of the Task cases varying between runs, so a one-scenario swing is within noise. And the final `SKILL.md` differs from the one the after run used in two places, made after the run to keep the Sync Loop carrier walk green: two bullets in the Two-Layer section restored word for word from the old file, and the worked examples' `trigger_phrases` written as flow-style lists. Both restore old text or change frontmatter only, so neither removes a rule.

## Files

- `after/skill/<ID> - <name>/` and `before/skill/<ID> - <name>/`: `meta.json` and `turn-<N>.md` per reply. Event streams, transcripts and each scenario's `exports/` sandbox stay local, as `.gitignore` states
- `after/replies/` and `before/replies/`: `<ID>-turn<N>.txt` per turn
- `after-stdout.txt` and `before-stdout.txt`: the runner's per-scenario status lines
- `compare.txt` and `compare.csv`: the comparison, printed and per field
- `run/`: the runner, `collect_exports.py` and `compare_runs.py` as used
