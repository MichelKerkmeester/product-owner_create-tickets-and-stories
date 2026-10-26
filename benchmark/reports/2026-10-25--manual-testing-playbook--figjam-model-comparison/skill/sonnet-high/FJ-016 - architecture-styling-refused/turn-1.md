The check fails on the styled copy with exit status 1. The styling line is the only difference from the original, which passes with exit status 0.

**Original example** (`assets/examples/architecture-loomlist-sync.md`, unmodified)
```text
  diagram 1, architecture: ok, 9 nodes and 8 connectors, widest rank 3 steps, longest path 6 steps, 0.9 connectors per step, labels average 10 characters, 0 crossing pairs
PASSED 1 diagram(s) in base.md
```
Exit status: 0

**Same file with one line added** to the Mermaid block, `    style sync fill:#CDF4D3,stroke:#66D575`
```text
89a90
>     style sync fill:#CDF4D3,stroke:#66D575
  diagram 1, architecture: the block carries styling: the architecture layout colours each lane itself, drop it
FAILED 1 of 1 diagram(s) in styled.md
```
Exit status: 1

The fill and stroke are a valid FigJam pair, so the colour rules didn't cause this. The only rule that fired is the architecture rule in `figjam_checks/flowchart.py`, which rejects any `style`, `classDef` or `linkStyle` line because the architecture layout colours lanes itself. That rule is also why architecture models need no accent line, unlike user flows and processes.

**Scratch copies:** I ran both files from a temporary folder and deleted it before replying. I confirmed `base.md` and `styled.md` are gone from the temp directory. The repo has no tracked changes, and nothing was saved to `export/`.

**Board:** This was a check run, so I didn't write to the FigJam file `<draft-file-key>` or create a new one. The skill also needs your yes at its write gate before it writes a board. If you want the board written, tell me which model to compose. The unstyled original is the one that passes.

An earlier command in the run ended with a stray `head: illegal line count -- 0` error. That was a typo of mine and has no bearing on the check results.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.