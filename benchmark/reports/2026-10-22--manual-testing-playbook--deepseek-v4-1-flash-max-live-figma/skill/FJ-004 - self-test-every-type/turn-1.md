Self-test run against the packet. No artifact was authored, and the packet's own rules keep Flow Mode out of `export/`, so nothing was saved there. The repository is unchanged (clean `git status`) and the self-test wrote only to a temp directory.

**Command**

```
sk-create-figjam/scripts/flow_check.py --self-test
```

**Summary line and exit status**

```
142 of 142 self-test checks passed
exit status 0
```

**Where the 142 checks come from**

| Check group | Count | What it proves |
| --- | --- | --- |
| Good-model fixtures | 9 | One passing model per type, plus a sequence beside a user flow |
| Planted rule failures | 107 | Each rule fails on a planted model with its own message and a code of 1 |
| Shipped models | 14 | Every template and worked example still passes the rules it teaches |
| Palette and contract | 12 | 10 palette rows measure their recorded ratios, the pair record matches the check, SKILL.md `DIAGRAM_TYPES` matches the types dispatched |

**Every template and example is read**

All 14 markdown models under `assets/` appear as a PASS line, and each one re-checked alone parses real diagrams rather than passing on an empty file.

| File | Diagrams |
| --- | --- |
| `flow-templates.md` | 6 |
| `templates/process.md` | 3 |
| `templates/state.md` | 3 |
| `templates/er.md` | 3 |
| `templates/architecture.md` | 2 |
| `templates/sequence.md` | 2 |
| `templates/gantt.md` | 2 |
| 7 files under `examples/` | 1 each |

**The one line that is not a PASS**

```
SKIP  Product Owner - Assets - Flow Templates.md is not in this install
```

This is the claude.ai Project Knowledge mirror of the packet assets, not a packet template. There is no `claude project/` directory in this checkout, so the script reports the absence and does not count it. The packet's own `assets/flow-templates.md` was read and passed. No count hides behind that skip.

Nothing failed. Zero `FAIL` lines, zero unreadable models, and no asset file missing from the run, since the script sweeps `assets/` with `rglob("*.md")` and would have failed any model that lost its Mermaid block.

To re-run after an asset edit, the same command prints the same 142-line proof, and one model can be checked alone with `flow_check.py <path>`.