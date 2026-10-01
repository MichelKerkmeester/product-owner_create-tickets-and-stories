# Router in kernel check: Product Owner kernel v1.20.0 on DeepSeek V4.1 Flash at thinking high

The Project packaging ran eight routing, intake and identity scenarios after the router moved into the kernel. Section 11 now carries the router code, the judgement tables the Router Contract document held are back in the kernel, and that document is gone. The question was whether every request still reaches the right lane and still asks before drafting where the scenario requires it.

- **Model:** `opencode-go/deepseek-v4.1-flash`, thinking high, through `run/pi_playbook_runner.py` with `--side project`
- **Harness change:** this copy of the runner stages `benchmark/fixtures/companies/*/*.md` at `context/`, where every scenario's precondition expects it. The copy it came from predates the fixtures, and a first attempt without them reported every source missing, so that attempt is not graded here.
- **Grader:** Claude Opus 5.5 in Claude Code, reading each scenario's pass and fail lines against the replies. No second grader read this run.

## The ask-first finding

The first pass on the new kernel drafted on turn 1 in `PTK-006`, `PST-001` and `PEP-002`, where each scenario requires one question first. To tell the change from model noise, the same three ran on both kernels:

| Kernel | Samples | Asked first | Folders |
|---|---|---|---|
| Previous, v1.19.0 at `10f7fee6` | 3 per scenario | 6 of 9 | kept in the session scratchpad, not tracked |
| v1.20.0 before the fix | 4 per scenario | 4 of 12, Story 0 of 4 | the top level, `rerun-ask-first`, `rerun-ask-first-2`, `rerun-ask-first-3` |
| v1.20.0 with the Ask before drafting line | 4 per scenario | 12 of 12 | `reinforced-1` to `reinforced-4` |

The rule was already in the kernel's ESCALATE IF list. The larger kernel diluted it, so one line in the header block now restates it. Every reinforced sample then delivered on turn 2. The measured line sat above the Purpose line, and the committed kernel keeps it at the end of the same header block, so a residency row's declared span stays contiguous.

## Verdicts on the committed kernel

| ID | Scenario | Verdict | Folder |
|---|---|---|---|
| PIR-001 | Vague intake, kind and energy | PASS | `reinforced-others` |
| PIR-002 | Conflicting commands | PASS | `reinforced-others` |
| PID-001 | Project identity handover | PASS | `reinforced-others` |
| PBG-001 | Quick bug | PASS | `reinforced-others` |
| PDK-001 | Behavior reference | PASS | `reinforced-others` |
| PTK-006 | Data tracking task | PASS, 4 of 4 | `reinforced-1` to `reinforced-4` |
| PST-001 | Story hard values | PASS, 4 of 4 | `reinforced-1` to `reinforced-4` |
| PEP-002 | Epic natural wording | PASS, 4 of 4 | `reinforced-1` to `reinforced-4` |

## Advisories

None of these changes a verdict.

- `PIR-001` in `reinforced-others` renders both turns without the `Export-equivalent path:` and `HVR self-scan:` lines. The earlier sample on the same kernel printed both.
- `PDK-001` writes em dashes in its source-basis callout and term list. The Doc template itself uses them, so they follow the house ClickUp format.
