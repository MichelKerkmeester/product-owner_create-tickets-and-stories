# Deep Review Report - Product Owner mcp-figma (vendored transport packet)

**Session:** `fanout-deepseek-1792580474713-m4jej7` (generation 1, lineageMode `new`)
**Review target (bound):** `specs/product-owner/018-product-owner-deep-review/004-mcp-figma` (spec-folder), whose `spec.md` names the reviewed surfaces
**Surfaces actually reviewed:** `AI Systems/Product Owner/mcp-figma/` (58 files), `AI Systems/Product Owner/vendor.json`, `AI Systems/Product Owner/scripts/vendor-sync.py`, plus the only in-repo consumer (`AI Systems/Product Owner/sk-create-figjam/`) and the gates that guard the vendor copy
**Iterations:** 5 of 5 (`stopPolicy: max-iterations`, `convergenceMode: off`)
**Executed:** 2026-10-21, iterations 1-5, REVIEW verdict line per iteration

---

## 1. Executive Summary

- **Overall verdict: CONDITIONAL.** Six P1 findings are active and each has a named upstream fix site; no P0 finding survived adversarial replay. `hasAdvisories: true` applies to the eleven P2 findings, which do not block a shipped conditional pass.
- **Active counts:** P0 = 0, P1 = 6, P2 = 11. Total 17 open, 0 resolved, 0 repeated.
- **Scope summary:** all three in-scope surfaces were opened, plus the consumer packet that depends on one of them. The vendored copy is **in step**: 58 of 58 recorded `sha256` values match on disk and in the upstream tree, and `base_commit` `293caa90…` is the commit that last touched the upstream folder. Nothing in `mcp-figma/` has been edited in Product Owner, so every finding inside it names the upstream file as its fix site, per the staging spec's Focus.
- **What the review actually verified (not assumed):** the packet was tested against the **installed `figma-ds-cli` 1.2.0** (`--version`, `--help`, and per-command `--help` for `create`, `set`, `extract`, `export`, `fj`, `unstack`, `combos`, `use`, `arrange`), because the packet's own claims about the command surface cannot falsify themselves. That oracle produced the highest-value findings: the primitive verbs are `create` subcommands, not top-level aliases, and `extract` takes a positional output path, not `--out`.
- **Character of the P1 set:** one wrong command table, one unenforced identity check, one false success exit code, one broken repo-root resolution, one wrong flag on the front-door command, and one set of depth-dependent links that dangle in the position the packet ships in. Five of the six are places where the packet's prose promise and its executable behaviour disagree.
- **Release readiness:** `in-progress`. No P0 blocks a ship decision; the six P1s should land upstream before the next `vendor-sync.py pull` re-baselines the copy.

---

## 2. Planning Trigger

`/speckit:plan` **is required**: six P1 findings need upstream remediation across four files plus one shared helper, and each fix must then be pulled back into the vendored copy and re-baselined in `vendor.json`.

```json
{
  "triggered": true,
  "verdict": "CONDITIONAL",
  "hasAdvisories": true,
  "activeFindings": {
    "P0": 0,
    "P1": 6,
    "P2": 11,
    "ids": [
      "R1-P1-001", "R1-P1-002", "R1-P1-003", "R1-P1-004", "R2-P1-001", "R3-P1-001",
      "R1-P2-001", "R1-P2-002", "R1-P2-003", "R2-P2-001", "R2-P2-002",
      "R3-P2-001", "R3-P2-002", "R3-P2-003", "R4-P2-001", "R4-P2-002", "R4-P2-003"
    ]
  },
  "remediationWorkstreams": [
    "WS-1 command-surface truth (R1-P1-001, R2-P1-001)",
    "WS-2 fail-closed identity and exit codes (R1-P1-002, R1-P1-003)",
    "WS-3 depth-independent resolution (R1-P1-004, R3-P1-001)",
    "WS-4 supply chain and untrusted content (R2-P2-001, R2-P2-002)",
    "WS-5 metadata and single-source-of-truth clean-up (all P2 documentation findings)"
  ],
  "specSeed": [
    "Upstream skill spec: the command table must be generated from `<bin> --help` output, not from a research digest.",
    "Vendoring contract: a vendored packet's links and repo-root lookups must resolve from any depth, or the copy must carry a resolution note.",
    "Script contract: a guided operation that performs nothing must not exit 0."
  ],
  "planSeed": [
    "Correct the create-primitives row in tool-surface.md, feature-catalog.md (x2) and render-and-create.md against `figma-ds-cli create --help`.",
    "Replace `--out DESIGN.md` with a fresh positional path plus a refuse-if-exists step in README.md and INSTALL-GUIDE.md.",
    "Add the silships identity probe to `_common.sh:figma_bin` and let `safe-connect-daemon-health.sh` inherit it.",
    "Make `connect-safe.sh` exit non-zero (or prove health) when it cannot connect.",
    "Resolve `.utcp_config.json` by walking up to the folder that holds `.skilled`, as `vendor-sync.py` already does.",
    "Rewrite the six depth-dependent links to targets that survive vendoring.",
    "Pin `figma-developer-mcp` and the `install.sh` clone; add the untrusted-content guard to the MCP path."
  ],
  "findingClasses": [
    "documentation-contract",
    "missing-validation",
    "false-success-signal",
    "path-resolution",
    "cross-reference-integrity",
    "supply-chain",
    "duplication"
  ],
  "affectedSurfacesSeed": [
    "AI Systems/Product Owner/mcp-figma/references/tool-surface.md",
    "AI Systems/Product Owner/mcp-figma/feature-catalog/feature-catalog.md",
    "AI Systems/Product Owner/mcp-figma/feature-catalog/render-and-create/render-and-create.md",
    "AI Systems/Product Owner/mcp-figma/README.md",
    "AI Systems/Product Owner/mcp-figma/INSTALL-GUIDE.md",
    "AI Systems/Product Owner/mcp-figma/SKILL.md",
    "AI Systems/Product Owner/mcp-figma/scripts/_common.sh",
    "AI Systems/Product Owner/mcp-figma/scripts/connect-safe.sh",
    "AI Systems/Product Owner/mcp-figma/scripts/doctor.sh",
    "AI Systems/Product Owner/mcp-figma/scripts/install.sh",
    "AI Systems/Product Owner/mcp-figma/scripts/print-utcp-snippets.sh",
    "AI Systems/Product Owner/mcp-figma/references/mcp-wiring.md",
    "AI Systems/Product Owner/mcp-figma/references/troubleshooting.md",
    "AI Systems/Product Owner/mcp-figma/assets/utcp-figma-manual.md",
    "AI Systems/Product Owner/mcp-figma/manual-testing-playbook/manual-testing-playbook.md",
    "AI Systems/Product Owner/scripts/vendor-sync.py"
  ],
  "fixCompletenessRequired": true
}
```

---

## 3. Active Finding Registry

### P0 - none

No P0 finding was recorded in any iteration, and the two P0 candidates considered on replay (a documented path to an unconfirmed destructive verb; a credential leak) were ruled out with evidence in iteration 5.

### P1 - 6 active

| ID | Title | Dimension | file:line | Impact | Fix recommendation | findingClass | scopeProof | affectedSurfaceHints |
|---|---|---|---|---|---|---|---|---|
| R1-P1-001 | `tool-surface.md` inverts the truth about the primitive verbs: declares them top-level aliases and calls the real `create`-subcommand form "drift" | correctness | `AI Systems/Product Owner/mcp-figma/references/tool-surface.md:98` | An agent runs `figma-ds-cli rect …` and gets the root usage text instead of a node | Record `create rect\|ellipse\|text\|line\|component\|group\|autolayout\|al` and delete the "REFERENCE is drift" clause. The same inverted conclusion is repeated at `feature-catalog/feature-catalog.md:18`, `feature-catalog/feature-catalog.md:120` and `feature-catalog/render-and-create/render-and-create.md:28`, so all four sites move together | documentation-contract | Cited line opened; falsified against `figma-ds-cli create --help` (lists all eight as subcommands) and `figma-ds-cli --help` (none of the eight at top level) | `references/tool-surface.md`, `feature-catalog/*` |
| R1-P1-002 | `_common.sh` resolves `figma-cli` without the silships identity check `SKILL.md` makes mandatory | correctness / security | `AI Systems/Product Owner/mcp-figma/scripts/_common.sh:21` | A foreign `figma-cli` on PATH is accepted and every script drives it, though ALWAYS rule 1 requires a `--version`/`--help` proof and a fail-closed refusal | Probe the candidate before returning it; return failure when the probe fails. `examples/safe-connect-daemon-health.sh:34-38` inherits the fix | missing-validation | Rule read at `SKILL.md:268`; helper read at `_common.sh:19-23`; no call site performs the probe | `scripts/_common.sh`, `examples/safe-connect-daemon-health.sh` |
| R1-P1-003 | `connect-safe.sh` exits 0 after doing nothing whenever stdin is not a TTY | correctness | `AI Systems/Product Owner/mcp-figma/scripts/connect-safe.sh:20` | An agent (the packet's primary consumer, which runs non-interactive Bash) reads success from a no-op, and the install-guide checkpoints accept it | Exit `2` ("not attempted") or run `daemon status` and exit 0 only on a proven live connection | false-success-signal | Reproduced: `bash scripts/connect-safe.sh </dev/null` printed the notice and exited `0` | `scripts/connect-safe.sh`, `INSTALL-GUIDE.md` |
| R1-P1-004 | `doctor.sh` resolves `.utcp_config.json` one level above the repo root once vendored, so the optional-MCP check false-negatives | correctness | `AI Systems/Product Owner/mcp-figma/scripts/doctor.sh:48` | The one automated check of the optional path reports "not found" in the repo that ships it, while `AI Systems/.utcp_config.json` does carry the `figma` manual | Walk up to the folder holding `.skilled` (as `vendor-sync.py:74-84` does) instead of counting five levels | path-resolution | Resolution walked: 5 levels = `MEGA/Development/.utcp_config.json` (absent); 4 levels = `AI Systems/.utcp_config.json` (present, `figma` registered) | `scripts/doctor.sh` |
| R2-P1-001 | `README` and `INSTALL-GUIDE` invoke `extract` with a `--out` flag the binary does not define, at a fixed path the packet's own no-overwrite rule forbids | security | `AI Systems/Product Owner/mcp-figma/README.md:86` | The front-door command is wrong twice: the flag is not part of `extract [options] [output]`, and `DESIGN.md` is a constant path, which is the silent-overwrite case the packet forbids | Use a fresh positional path and add the refuse-if-exists step the example already implements. Same fix at `INSTALL-GUIDE.md:268` and `:291` | documentation-contract | Cited lines opened; falsified against `figma-ds-cli extract --help`; contradicted by the packet's own `figma-cli-reference.md:217` and `examples/inspect-export-readonly.sh:62` | `README.md`, `INSTALL-GUIDE.md` |
| R3-P1-001 | Seven cross-references resolve only at the upstream nesting depth, so they are dangling in the position the packet ships in | traceability | `AI Systems/Product Owner/mcp-figma/references/mcp-wiring.md:41` | Navigation to the Code Mode mechanics, the smart-router template, the skill catalog and `AGENTS.md` fails in the shipped copy; two of the seven are in the entry-point docs | Point at targets a depth change cannot break, or carry a resolution note. Sites: `README.md:203`, `SKILL.md:115`, `feature-catalog/feature-catalog.md:71`, `references/mcp-wiring.md:41`, `:170`, `references/troubleshooting.md:477` (two links) | cross-reference-integrity | Link sweep in both positions: upstream 0 broken, vendored 7 broken; none of the targets exists under Product Owner | `README.md`, `SKILL.md`, `references/*`, `feature-catalog/feature-catalog.md` |

### P2 - 11 active (advisories)

| ID | Title | Dimension | file:line | Disposition |
|---|---|---|---|---|
| R1-P2-001 | `install.sh --verbose` test can never be false, so the quiet branch is dead | correctness | `mcp-figma/scripts/install.sh:95` | Advisory. Compare `[ "$VERBOSE" = 1 ]` |
| R1-P2-002 | `INSTALL-GUIDE` version metadata trails the packet at `1.0.0.0` while `SKILL.md` and `README` declare `1.1.3.0` | traceability | `mcp-figma/INSTALL-GUIDE.md:4` | Advisory. Bump frontmatter, header and the Version History table |
| R1-P2-003 | `vendor-sync.py` can write a null `base_commit` and then report "in step at None" | correctness | `scripts/vendor-sync.py:135` | Advisory. Raise `SetupError` instead of returning `None` |
| R2-P2-001 | Nothing the packet executes is pinned or integrity-checked (`install.sh` clones the default branch and runs `npm install -g`; the manual uses `figma-developer-mcp@latest`) | security | `mcp-figma/scripts/install.sh:102` | Advisory hardening. Pin a tag and record it; pin the MCP version |
| R2-P2-002 | The optional MCP path pipes arbitrary Figma-authored text into the model with no untrusted-content instruction | security | `mcp-figma/references/mcp-wiring.md:29` | Advisory. One guard line in §5 |
| R3-P2-001 | Playbook index pins the skill at `1.0.0.0` | traceability | `mcp-figma/manual-testing-playbook/manual-testing-playbook.md:9` | Advisory |
| R3-P2-002 | Two of three pointers to the scenario index name Section 12 instead of Section 13 | traceability | `mcp-figma/manual-testing-playbook/manual-testing-playbook.md:35` | Advisory. Also `:135` |
| R3-P2-003 | `INSTALL-GUIDE` describes `extract` output as 9 sections; reference and catalog say 11 | traceability | `mcp-figma/INSTALL-GUIDE.md:268` | Advisory |
| R4-P2-001 | The Code Mode manual entry is copied in five places and the copies have diverged on the version pin | maintainability | `mcp-figma/assets/utcp-figma-manual.md:53` | Advisory. Keep the asset as the single source |
| R4-P2-002 | The daemon PID constant re-introduces the `figma-cli` name collision the packet warns about, and `doctor` reports its contents unvalidated | maintainability | `mcp-figma/scripts/_common.sh:49` | Advisory. Comment the two namespaces and validate the PID's process name |
| R4-P2-003 | The official Dev Mode MCP "not a supported path" sentence reads repo-wide while `sk-create-figjam` ships that route as its primary one | maintainability | `mcp-figma/references/mcp-wiring.md:154` | Advisory. Scope the sentence to "through Code Mode" |

---

## 4. Remediation Workstreams

**WS-1 - Command-surface truth (P1).** R1-P1-001 and R2-P1-001 are the same failure mode: a documented surface that the installed binary does not implement. Fix both by generating the rows from `<bin> <group> --help`, and add one verification step to the packet's own release process so a future edit cannot reintroduce a research-digest claim over a `--help` fact.

**WS-2 - Fail-closed identity and exit codes (P1).** R1-P1-002 and R1-P1-003 make the packet's guarantees unenforceable at the two places a machine reads them: the binary resolver and the guided connect's exit status. Fix the shared helper once; let the example script inherit it.

**WS-3 - Depth-independent resolution (P1).** R1-P1-004 and R3-P1-001 share one root cause: the packet assumes it sits at `.skilled/skills/mcp-tooling/mcp-figma`. `vendor-sync.py` already solved this problem for the manifest; apply the same walk-up technique to the doctor and to the six link sites.

**WS-4 - Supply chain and untrusted content (P2, hardening).** Pin what the packet executes and mark pulled content as data. Neither is an exploit today; both are cheap now.

**WS-5 - Metadata and single-source clean-up (P2).** The eleven P2 items: one version trail per file, one copy of the manual snippet, one section pointer per reference, one number for the extract section count.

**Sequencing note:** all fixes land **upstream** (`.skilled/skills/mcp-tooling/mcp-figma/…`), then `python3 scripts/vendor-sync.py push` from a working copy, then commit upstream, then `pull` to re-baseline `vendor.json`. Editing the vendored copy directly would be overwritten by the next pull and would break the byte-copy contract the manifest exists to prove.

---

## 5. Spec Seed

- The vendoring contract should state that a vendored packet must resolve its own links and repo-root lookups from **any** depth, or must ship a documented resolution note. Today the contract only covers byte equality, which is why a byte-perfect copy can still be unusable.
- A packet that documents an external tool's command surface should carry the `--help` transcript it was generated from, with a date, and the surface should be treated as data to regenerate rather than prose to maintain.
- Script contracts: a guided operation that performs nothing must not exit 0; a binary resolver that the rules describe as fail-closed must be fail-closed in code.
- Version metadata should have one rule: either every file's `version:` tracks the packet, or a file that does not carry the packet version must not claim a packet-level history it has not joined.

## 6. Plan Seed

1. `tool-surface.md:98`, `feature-catalog/feature-catalog.md:18`, `:120`, `feature-catalog/render-and-create/render-and-create.md:28` - correct the create-primitives conclusion against `figma-ds-cli create --help`.
2. `README.md:86`, `INSTALL-GUIDE.md:268`, `:291` - replace `extract --out DESIGN.md` with a fresh positional path and the refuse-if-exists step.
3. `scripts/_common.sh:19-23` - add the silships probe; `scripts/connect-safe.sh:20` - stop exiting 0 on a no-op.
4. `scripts/doctor.sh:48` - resolve the repo root by walking to the folder holding `.skilled`.
5. Six link sites - retarget to depth-independent references.
6. `scripts/install.sh:95` - fix the verbose test; `:102-104` - pin the clone.
7. `references/mcp-wiring.md:60`, `assets/utcp-figma-manual.md:53`, `scripts/print-utcp-snippets.sh:22`, `references/troubleshooting.md:406`, `mcp-servers/figma-mcp/README.md:44` - one pinned arg list, one source.
8. `vendor-sync.py:135` - fail on an unresolvable base commit.
9. Playbook and install-guide metadata - one version, one section pointer, one section count.

## 7. Traceability Status

**Core Protocols**

| Protocol | Status | Evidence | Unresolved drift |
|---|---|---|---|
| `spec_code` | **pass** | The three surfaces the staging spec declares exist; its byte-copy claim holds at 58/58 hashes on both trees; `base_commit` is the folder's last-touching commit; the out-of-scope list was honoured (no `specs/`, `export/`, `benchmark/reports/`, `claude-plugin/`, Product Context, screenshot or figma.com URL opened) | none |
| `checklist_evidence` | **not applicable** | `specs/product-owner/018-product-owner-deep-review/004-mcp-figma` carries no `checklist.md` | n/a |

**Overlay Protocols**

| Protocol | Status | Evidence | Unresolved drift |
|---|---|---|---|
| `skill_agent` | **pass** | `sk-create-figjam` states the handoff in four places (`SKILL.md:26`, `:65`, `:199`, `references/flow-mode.md:26`), delegates gating to the packet, and every `fj` verb it uses is classified at `tool-surface.md:149-152` and exists in the installed 1.2.0 | none |
| `agent_cross_runtime` | **not applicable** | No agent definition ships in either runtime tree | n/a |
| `feature_catalog_code` | **partial** | Catalog command forms agree with the binary (positional `extract`, destructive `arrange`, `init-agent` scope) | Disagrees with the front-door docs on `extract --out` (R2-P1-001) and shares the create-primitives error (R1-P1-001); section count 11 vs 9 (R3-P2-003) |
| `playbook_capability` | **partial** | 17 scenario files for 17 declared scenarios; the five IDs the examples cite all exist; spot-checked forms (`export screenshot -o`, `daemon status\|diagnose`, `connect --safe`) match the installed binary | 12 of 17 scenarios were not audited line by line; playbook metadata is stale (R3-P2-001, R3-P2-002) |

**`AC_COVERAGE`:** exempt. The lifecycle predicate is inactive - the staging folder is a review-scope note with no `checklist.md` and no `implementation-summary.md`, so the advisory signal has no input.

## 8. Deferred Items

- **Runtime execution of the packet's scripts against a live Figma session** - deferred, not skipped: no Figma Desktop session was open, and any mutating verb would change a user document. Every behavioural claim was checked against `--help` output, reproduced shell behaviour, and the packet's own example scripts. R1-P1-003 was the one behaviour reproducible without Figma, and it was reproduced.
- **12 of the 17 playbook scenarios** - structure, IDs and five command forms verified; per-scenario step-by-step audit deferred.
- **`vendor-sync.py` under a hostile upstream** - the failure path where `git log` cannot resolve a commit (R1-P2-003) is untested in `scripts/tests/test_vendor_sync.py`; a test that stubs a non-repo upstream would close it.
- **The `R2-P2-001` pin values** - choosing a version to pin is an operator decision, not a review finding.

## 9. Search Ledger

- **Dimensions covered:** 4 of 4 (`correctness`, `security`, `traceability`, `maintainability`), each with one full iteration plus a close-out replay.
- **Ruled-out directions (each with evidence, not intuition):** vendored drift from upstream; stale `vendor.json` entries; `vendor-sync.py pull` overwriting local edits; syntactically broken shell; credential exposure in the packet; committing the token through the documented `.env` workflow; a fabricated changelog trail; scenario-ID drift between playbook and examples; the consumer depending on undocumented `fj` behaviour; the consumer duplicating the gating taxonomy; a documented path to an unconfirmed destructive verb; a credential leak through the three scripts first opened in the final pass; scope mis-enumeration.
- **Command-surface sweep:** every `figma-ds-cli <token>` mention in all 58 files was matched against the 72 top-level commands of the installed 1.2.0. Exactly one unrecognized command token exists, `rect`, and its sites are R1-P1-001. Everything else resolves.
- **Source of truth used:** the installed binary, the two trees, and `git`. Not the packet's account of itself.
- **`hasSearchDebt`: false.** No dimension was left uncovered, and no candidate direction was dropped without a recorded reason.

## Dimension Expansion Map

- Completed pivots: 0 (convergence mode off; this loop ran to the iteration cap by configuration).
- Failed pivots: 0.
- Audited overrides: 0.
- Selected review directions, one per iteration: correctness → security → traceability → maintainability → close-out replay.
- Remaining frontier: the 12 un-audited playbook scenarios, and the hostile-upstream failure path in `vendor-sync.py`.

## Audit Appendix

### Convergence summary

`stopReason: maxIterationsReached`. Iterations 1-5 ran in order; convergence scoring was disabled by configuration, so the loop closed on the cap rather than on a similarity score. Per-iteration `newFindingsRatio`: 1.00, 0.30, 0.286, 0.176, 0.00 - the shape of a thorough pass whose last iteration is verification, not discovery.

### Coverage summary

| Iteration | Dimension | Findings (cumulative) | Verdict |
|---|---|---|---|
| 1 | correctness | 7 | CONDITIONAL |
| 2 | security | 10 | CONDITIONAL |
| 3 | traceability | 14 | CONDITIONAL |
| 4 | maintainability | 17 | PASS (P2 only) |
| 5 | close-out replay | 17 (0 new) | PASS |

### Ruled-out claims (with the evidence that killed them)

See §9. None of them is asserted from intuition: each names the command, hash comparison, or file read that settled it.

### Sources reviewed

`AI Systems/Product Owner/mcp-figma/` - `SKILL.md`, `README.md`, `INSTALL-GUIDE.md`, `references/{figma-cli-reference,tool-surface,mcp-wiring,troubleshooting}.md`, `assets/{utcp-figma-manual,env-template}.md`, `scripts/{_common,install,doctor,connect-safe,connect-yolo,daemon,unpatch,print-utcp-snippets}.sh`, `scripts/README.md`, `examples/{README,optional-mcp-context}.md`, `examples/{inspect-export-readonly,safe-connect-daemon-health}.sh`, `feature-catalog/feature-catalog.md` plus all 8 category files, `manual-testing-playbook/manual-testing-playbook.md` plus the 17 per-scenario files' IDs, `changelog/v1.0.0.0…v1.1.3.0.md`, `mcp-servers/{figma-cli,figma-mcp}/*`, and per-command `--help` output from the installed `figma-ds-cli` 1.2.0.
`AI Systems/Product Owner/` - `vendor.json`, `scripts/vendor-sync.py`, `scripts/tests/test_vendor_sync.py`, `benchmark/gates/{run_gates.sh,check_hub.py}`, `mode-registry.json`, `hub-router.json`, `.gitignore`.
`AI Systems/Product Owner/sk-create-figjam/` - `SKILL.md`, `references/flow-mode.md`.
Workspace - `specs/product-owner/018-product-owner-deep-review/004-mcp-figma/spec.md`, `specs/product-owner/018-product-owner-deep-review/004-mcp-figma/review/lineages/deepseek/steer.md`.

### Method limits

The vendored copy cannot be executed against Figma, so the review used the installed binary's own `--help` output as the oracle for surface claims, and reproduced the one script behaviour that needs no Figma (R1-P1-003). `vendor-sync.py status` was not executed directly - it was re-implemented in Python to recompute the same three-tree comparison, because the lineage's write surface forbids commands whose side effects leave the lineage. The result was then corroborated by reading `scripts/tests/test_vendor_sync.py`, which asserts the same behaviours.
