Ran `flow_check.py` against a temp copy of the Loomlist architecture example, unmodified and with one added `style` line. The source fixture was not changed.

**Added line** (inside the Mermaid block, one added line, nothing else changed):

```mermaid
style sync fill:#CDF4D3,stroke:#66D575
```

This is the valid Light green palette pair, so the failure is not an invalid colour.

**Baseline — unmodified example**

```text
  diagram 1, architecture: ok, 9 nodes and 8 connectors, widest rank 3 steps, longest path 6 steps, 0.9 connectors per step, labels average 10 characters, 0 crossing pairs
PASSED 1 diagram(s) in architecture-loomlist-sync.md
```

`exit status: 0`

**Styled copy — same model plus the one `style` line**

```text
  diagram 1, architecture: the block carries styling: the architecture layout colours each lane itself, drop it
FAILED 1 of 1 diagram(s) in architecture-loomlist-sync.md
```

`exit status: 1`

**Verification that it fails on styling alone**

* The `diff` shows exactly one added line and no other edits.
* The styled run reports exactly one rule problem, and it is the styling refusal. No second rule problem appears, so nothing else in the model is failing.
* Removing that single line returns the same file to `PASSED` with exit `0`.
* The check's own `--self-test` passed `142 of 142`, including:
  * `PASS  styling in an architecture fails with 'the architecture layout colours each lane itself'`
  * `PASS  examples/architecture-loomlist-sync.md passes`

The rule is architecture-specific: `references/style-guide.md` and `references/types/architecture.md` both state an architecture takes no colour from the model because the layout colours each lane itself.