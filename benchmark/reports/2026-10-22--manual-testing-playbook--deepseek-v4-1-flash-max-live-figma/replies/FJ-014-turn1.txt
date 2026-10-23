## Result: the check fails on the node budget, exit status 1

**Run 1, the requested case.** A straight user flow with 10 nodes (`start([Signup start])` through `done([Done])`, 9 connectors), written to a temp file outside the repo:

```
  diagram 1, user flow: 10 nodes, at most 9: split the flow
  diagram 1, user flow: the longest path runs 10 steps, at most 8: split the flow
FAILED 1 of 1 diagram(s) in straight-10.md
```

`EXIT=1`

The node budget line is the one asked for, and it fires: `10 nodes, at most 9`. The budget comes from `figjam_checks/flowchart.py:47`, `BUDGET = {USER_FLOW: (9, 12), …}`, enforced at line 249.

The second line is real and not a defect. `layout.py` sets `MAX_LONGEST_PATH = 8`, so drawing 10 steps as one unbroken chain trips the path measure as well as the node budget. Both trace to the same 10-step length.

**Run 2, isolating the budget rule.** To rule out the failure being only a side effect of the path measure, I ran a 10-node flow that is wide instead of long, with a longest path of exactly 8 steps:

```
  diagram 1, user flow: 10 nodes, at most 9: split the flow
FAILED 1 of 1 diagram(s) in straight-10.md
```

`EXIT=1` with the node budget as the only reported problem. The budget rule stands on its own.

**Run 3, the 9-node boundary.** Same shape with one node removed:

```
  diagram 1, user flow: ok, 9 nodes and 9 connectors, widest rank 2 steps, longest path 8 steps, 1.0 connectors per step, labels average 8 characters, 0 crossing pairs
PASSED 1 diagram(s) in straight-10.md
```

`EXIT=0`. The cap is exactly 9, so the check is not failing everything.

**Run 4, harness integrity.** `python3 scripts/flow_check.py --self-test` reported `142 of 142 self-test checks passed`, `EXIT=0`, so a failure means the model broke a rule rather than the checker being unsound.

| Run | Model | Exit | Node budget line |
| --- | --- | --- | --- |
| 1 | straight 10 nodes | 1 | yes |
| 2 | wide 10 nodes | 1 | yes, alone |
| 3 | 9 nodes control | 0 | not raised |
| 4 | `--self-test` | 0 | 142 of 142 |

One finding worth recording: a strictly straight chain cannot reach the 9-node budget and pass, because the 8-step longest-path cap binds first. Only a flow with at least one branch lands on 9 nodes and clears both rules.

No artifact was produced, so there is no export path and no board write. The check runs before the write gate, so a failure here opens no gate and touches no Figma file. Fixtures lived in `/var/folders/.../tmp.tkP4rrtIoB/figjam-budget`, `git status` is clean, `export/` is empty, and no Mermaid file was left in the repository.

`HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.`