The check fails on the palette, as expected. Because it failed, nothing was written to FigJam.

**Model:** I used the shipped Fernhouse return user flow from `assets/examples/user-flow-fernhouse-return.md` and changed one line. The end node's style went from `fill:#CDF4D3` to `fill:#00FF00`, and the stroke stayed `#66D575`. The model is at `/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/tmp.6RBXsNAoyJ/model.md`.

**Command:** `python3 -I scripts/flow_check.py model.md`

```text
  diagram 1, user flow: fill #00ff00 is not a FigJam light fill: pick a pair from references/style-guide.md
FAILED 1 of 1 diagram(s) in model.md
```
**Exit status: 1**, which means a rule failed.

The palette rule is the only failure. `#00FF00` isn't one of FigJam's light fills in `ACCENT_PAIRS` (`scripts/figjam_checks/common.py:47`).

To confirm that one edit caused the failure, I ran the unchanged example the same way. It passed with exit status 0: `PASSED 1 diagram(s)`, 9 nodes and 9 connectors.

**Board write:** I didn't write to FigJam file `<test-file-key>` and didn't create a new file. Rule 3 of the skill says nothing is written until every diagram passes the check, and this model fails on purpose. A write would also need your yes at the write gate first. If you want a board in that file, the end node needs a palette fill such as `#CDF4D3`. Once that version passes the check, I can compose it and ask for your yes before writing.