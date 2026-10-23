Ran it. Here is the run, verbatim.

**Model** (kept outside the repo, at `/tmp/fj015-PvW4xZ/end-node-bad-fill.md`):

```markdown
flowchart TD
    start([Open the order]) --> track[Track the parcel]
    track --> shown([Status shown])
    style shown fill:#00FF00
```

**Run** — `python3 sk-create-figjam/scripts/flow_check.py <model>`:

```text
  diagram 1, user flow: fill #00ff00 is not a FigJam light fill: pick a pair from references/style-guide.md
FAILED 1 of 1 diagram(s) in end-node-bad-fill.md
```

**Exit status: 1** (rule failure, as documented in the script's usage block: `0` passes, `1` a rule fails, `2` unreadable)

**Control run** — the same three-node flow with the end node on the accepted green pair `fill:#CDF4D3,stroke:#66D575`:

```text
  diagram 1, user flow: ok, 3 nodes and 2 connectors, widest rank 1 steps, longest path 3 steps, 0.7 connectors per step, labels average 14 characters, 0 crossing pairs
PASSED 1 diagram(s) in end-node-good-fill.md
```

**Exit status: 0.** The control isolates the cause: the only difference between the two runs is the fill value, and the palette problem is the sole problem the failing run printed — no shape, connector, budget, label or direction rule fired.

**Checker health** — `flow_check.py --self-test`: `142 of 142 self-test checks passed`, exit `0`, including `PASS  the palette record names the pairs the check accepts`. So the failure is the rule firing, not a broken install or a drifted palette record.

Why `#00FF00` is refused, from the packet's own authority:

* The check's accepted set is `ACCENT_PAIRS` in `scripts/figjam_checks/common.py` — nine light fills and the neutral lane pair, nothing else. `#00FF00` is in neither, and `colour_problems()` reports it before checking its stroke
* `references/style-guide.md` Section 3 states "The check accepts exactly the pairs in this record", and its departures table records the reason for refusing saturated fills: FigJam sets white text on them (1.85:1 on `#66D575`, under the 4.5:1 text gate), Mermaid cannot set a text colour, and the generator's text colour on a saturated fill was never observed
* `references/types/user-flow.md` Section 5 caps a user flow at one accent from that guide, so the fix is the light green pair `#CDF4D3` / `#66D575`, or light blue `#C2E5FF` / `#3DADFF` as the neutral default

Two operational notes:

* Nothing was saved to `export/` and no model file entered the repository — `git status --porcelain` is clean, and both scratch models sit in `/tmp/fj015-PvW4xZ/` if you want to re-run them
* No board was written and no write gate was approached. This was the pre-write check standing alone, so there is no board URL or read-back to report

If you want this recorded as a reusable negative fixture rather than a one-off run, say so and I'll shape it as a Doc or a task — `figjam_checks/fixtures.py` already carries a planted-model per rule, and a saturated-fill case is a gap there today.