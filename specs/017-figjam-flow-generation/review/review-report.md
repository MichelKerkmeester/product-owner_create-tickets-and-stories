---
title: "Deep Review Report: FigJam Flow Generation, phases 003 to 006"
description: "Five-iteration deep review of the uncommitted FigJam flow generation work. Verdict CONDITIONAL with 4 active P1 and 6 active P2 findings."
---

# Deep Review Report: FigJam Flow Generation, phases 003 to 006

## 1. Executive Summary

- **Verdict:** CONDITIONAL
- **hasAdvisories:** false (the verdict is not PASS)
- **Active findings:** P0 0, P1 4, P2 6
- **Scope:** the uncommitted work of phases 003 to 006 in the Product Owner repository (the vendored figma packet, the parent hub conversion, Flow Mode and the Claude Code plugin), 41 playbook citation remaps, the 58-file vendored `mcp-figma/` packet checked against `vendor.json` hashes, four Sync Loop files and the Change Location flow model in the outer AI Systems repository. 118 files in all.
- **Run:** 5 of 5 iterations, executor cli-codex `gpt-6-luna` at reasoning max on the fast service tier, stop policy max-iterations, stop reason `maxIterationsReached`. All four dimensions covered.

Two findings were raised as P0 during the run and both were lowered in the closing replay. Each needs a precondition only a party with write access to this repository can plant, and that party could edit the scripts directly. The orchestrator re-read both code paths and agrees with the lower grades.

## 2. Planning Trigger

`/speckit:plan` is required for the four P1 findings. They are small and local, and fit inside the open phases 005 and 006 rather than a new packet.

```json
{
  "label": "Planning Packet",
  "triggered": true,
  "verdict": "CONDITIONAL",
  "hasAdvisories": false,
  "activeFindings": [
    {"id": "R1-P1-001", "severity": "P1", "file": "scripts/vendor-sync.py:164"},
    {"id": "R2-P1-001", "severity": "P1", "file": "sk-product-owner/references/flow-mode.md:116"},
    {"id": "R3-P1-001", "severity": "P1", "file": "sk-product-owner/references/flow-mode.md:136"},
    {"id": "R5-P1-001", "severity": "P1", "file": "hub-router.json:6"},
    {"id": "R2-P0-001", "severity": "P2", "file": "scripts/build-plugin.py:117"},
    {"id": "R1-P2-002", "severity": "P2", "file": "scripts/build-plugin.py:71"},
    {"id": "R4-P2-001", "severity": "P2", "file": "README.md:27"},
    {"id": "R4-P2-002", "severity": "P2", "file": "sk-product-owner/README.md:231"},
    {"id": "R5-P2-001", "severity": "P2", "file": "sk-product-owner/scripts/vendored/mermaid_extract.py:726"},
    {"id": "R2-P2-001", "severity": "P2", "file": "sk-product-owner/assets/examples/story/story-example-complete.md:51"}
  ],
  "remediationWorkstreams": ["path-containment", "flow-mode-contract", "hub-routing", "docs-and-advisories"],
  "specSeed": ["Flow Mode reply contract states its relation to the HVR self-scan", "Hosted route writes only into a verified dedicated page", "Hub artifact vocabulary covers clarification requests"],
  "planSeed": ["Contain vendor-sync paths", "Contain build-plugin paths", "Fix the Flow reply and rollback wording", "Add clarification to hub-router.json with a gold row", "Refresh README counts"],
  "findingClasses": ["class-of-bug", "matrix/evidence"],
  "affectedSurfacesSeed": ["scripts/vendor-sync.py", "scripts/build-plugin.py", "sk-product-owner/references/flow-mode.md", "AGENTS.md", "sk-product-owner/SKILL.md", "hub-router.json", "benchmark/gates/check_hub.py", "README.md", "benchmark/gates/README.md", "benchmark/router/README.md"],
  "fixCompletenessRequired": true
}
```

## 3. Active Finding Registry

The registry file keeps one row per severity a finding has held, so its raw counts read P0 2, P1 5, P2 5. The table below deduplicates by finding id and keeps the latest adjudicated severity.

### P1

**R1-P1-001: manifest paths can redirect sync writes outside package roots.** Correctness and security. `scripts/vendor-sync.py:164`. `resolve_dirs` joins `local_path` and `upstream_path` to their roots with no absolute-path, `..` or resolved-root check, and `copy_tree` (`:174`, `:185`) then runs `shutil.rmtree` on the target, or copies and unlinks include entries. A changed `vendor.json` plus one `pull` or `push` can overwrite or delete files outside the package. Raised P1, upgraded to P0 in iteration 2, back to P1 in iteration 5 because an operator must run a mutating command on a manifest a reviewer could see. Orchestrator check: the code matches the claim. Fix: reject absolute and traversal paths, resolve each package and include path beneath its root before any read or write, and add escape tests to `scripts/tests/test_vendor_sync.py`.

**R2-P1-001: hosted rollback can clear unrelated content on the target page.** Security, data loss. `sk-product-owner/references/flow-mode.md:116`. The hosted route's rollback is "clear the page the board landed on, which nothing else imports", but nothing requires that page to be empty or dedicated before the write. The `fj` route duplicates the page first. Fix: require a verified empty dedicated page before the first hosted write, or scope rollback to the generated diagram.

**R3-P1-001: Flow delivery reply conflicts with the global self-scan rule.** Traceability, contract conflict. `sk-product-owner/references/flow-mode.md:136` against `AGENTS.md:39`, `AGENTS.md:50` to `:52` and `sk-product-owner/SKILL.md:100`. Flow Mode allows the board URL and the read-back line "and nothing else". The Flow export exemption covers export steps 4 to 7 only, and step 8 plus the packet skill still require the HVR self-scan in every delivery response. Fix: either exempt Flow from the self-scan in AGENTS.md and the skill, or add the scan line to the Flow reply shape and the template.

**R5-P1-001: clarification requests can be routed to the Figma tool packet.** Correctness, routing. `hub-router.json:6`. The hub `SKILL.md:18` sends every clarification request to `product-owner`, but `artifactWords` has no clarification term, so a clarification that names a tool goes to `mcp-figma`. Orchestrator check, by running `route_stage_one` from `benchmark/gates/check_hub.py`: "I need a clarification about the figma-ds-cli setup" and "Ask me clarifying questions about the figma cli export" both return `mcp-figma`. Fix: add clarification words to `artifactWords`, add a gold row, and have `check_hub.py` compare the SKILL.md routing table with `hub-router.json`.

### P2

**R2-P0-001: plugin build can delete an external `skills` directory through a symlinked parent.** `scripts/build-plugin.py:117`. When `claude-plugin` is a symlink, `shutil.rmtree(plugin / "skills")` deletes inside the link target. `build()` reads `claude-plugin/.claude-plugin/plugin.json` first (`:110`), so the target must already look like a plugin. Raised P0 in iteration 2, lowered to P2 in iteration 5. Fix in the same change as R1-P2-002: refuse symlinked path components and check the resolved target is under the repository root.

**R1-P2-002: plugin build can package content from a symlinked hub source.** `scripts/build-plugin.py:71`. The symlink scan runs only inside packet walks, and the four `HUB_FILES` enter the source map unchecked, so `copyfile` follows a symlinked hub file and the hash check passes on the copied bytes. The self-test plants its symlink under `sk-product-owner/references` and never covers this. Fix: check every `HUB_FILES` source and add a self-test row.

**R4-P2-001: published benchmark totals disagree with the current checks.** `README.md:27` and `:679`, `benchmark/gates/README.md:86`, `benchmark/router/README.md`. The READMEs still say 9 gates, 117 router fixtures, 189 differential inputs and 35 format cases, while the runners now give 10 gates, 123 fixtures and 201 inputs. This is the README update phase 005 already lists as outstanding.

**R4-P2-002: Product Owner README contains a prose semicolon.** `sk-product-owner/README.md:231`, reported by the format validator as an advisory.

**R5-P2-001: the one-accent colour rule has no check.** `sk-product-owner/scripts/vendored/mermaid_extract.py:726` drops `classDef` and `style` lines before `flow_check.py` sees the model, and the read-back in `flow-mode.md` does not check colour. Fix: reject style directives in `flow_check.py`, or name a colour check in the read-back.

**R2-P2-001: fictional examples still contain clickable Figma URLs.** `sk-product-owner/assets/examples/story/story-example-complete.md:51` and related bug examples. The URLs are synthetic (`figma.com/design/marquee/...`), the file was last committed 2026-10-17 and this work did not touch it. Out of scope here, so this is a deferred advisory.

## 4. Remediation Workstreams

1. **Path containment (P1, P2):** R1-P1-001, R2-P0-001, R1-P2-002. One defect class across `vendor-sync.py` and `build-plugin.py`, with tests and self-test rows. Ship together.
2. **Flow Mode contract (P1):** R3-P1-001, R2-P1-001. Wording in `flow-mode.md`, `AGENTS.md` and `sk-product-owner/SKILL.md`, plus the playbook citation remap if line numbers shift.
3. **Hub routing (P1):** R5-P1-001. `hub-router.json`, a gold row in `check_hub.py` and an inventory comparison.
4. **Advisories (P2):** R4-P2-001 and R4-P2-002 fold into the outstanding 005 README work. R5-P2-001 goes with workstream 2. R2-P2-001 is deferred.

## 5. Spec Seed

- Phase 005 spec: Flow Mode's reply contract states whether the HVR self-scan line is part of a Flow delivery.
- Phase 005 spec: the hosted route writes into a dedicated page the gate names and confirms empty, and rollback is scoped to that page.
- Phase 004 spec: the hub artifact vocabulary covers clarification requests, and `check_hub.py` proves the SKILL.md table and `hub-router.json` agree.
- Phase 003 and 006 specs: the sync and build scripts refuse any path that resolves outside its root.

## 6. Plan Seed

- T1: containment helper plus escape tests in `vendor-sync.py` and `test_vendor_sync.py`.
- T2: symlinked-parent and hub-file refusals in `build-plugin.py`, with two self-test rows.
- T3: Flow reply and self-scan reconciliation across `flow-mode.md`, `AGENTS.md`, `sk-product-owner/SKILL.md` and `flow-templates.md`.
- T4: dedicated-page rule and scoped rollback in `flow-mode.md`.
- T5: clarification words in `hub-router.json`, a gold row and the table-versus-router comparison in `check_hub.py`.
- T6: style-directive rejection in `flow_check.py` plus a self-test model.
- T7: README count refresh and the semicolon fix.
- Then rerun `run_gates.sh`, the router fixtures, the differential corpus and the format gate, and remap playbook citations if any cited line moved.

## 7. Traceability Status

### Core Protocols

- **spec_code: partial.** Phases 003 and 004 map their criteria to built evidence. Phases 005 and 006 are open: unchecked goal criteria and scaffold task files, as their own docs state.
- **checklist_evidence: partial.** Same split. 005 and 006 closure evidence is not yet claimed.
- **AC_COVERAGE:** advisory-shortfall for 005 and 006 (open phases), pass for 003 and 004.

### Overlay Protocols

- **skill_agent: fail,** from R3-P1-001 and R5-P1-001.
- **agent_cross_runtime: partial.** Flow aliases, framing and precedence agree across `router-contract.md`, `route_contract.py` and kernel section 11. No live plugin session was run in this review.
- **feature_catalog_code: pass.** `systems.cjs` `extraSources` matches the outer README and the feature catalog.
- **playbook_capability: pass.** The remapped citations point at in-range, matching lines.

## 8. Deferred Items

- R2-P2-001, pre-existing example URLs.
- Hosted board read-back and every board criterion, blocked until the hosted Figma MCP is connected (phase 002).
- A live `claude --plugin-dir claude-plugin` session showing `$flow` routing, the outstanding 006 item.
- Phase 005 and 006 closure evidence.

## Dimension Expansion Map

- Completed pivots: 0. Failed pivots: 0. Audited overrides: 0. No Council artifacts.
- Selected review directions: correctness (1), security (2), traceability (3), maintainability (4), adversarial replay and severity calibration (5).
- Remaining frontier: none inside the static scope. Live board and plugin evidence are the deferred items above.

## 9. Search Ledger

hasSearchDebt: true. The reducer holds four debt rows:

- **SL-006 (blocked): outer validator runtime.** Codex's sandbox could not load `libsimdutf.36.dylib`. Cleared outside the loop: the orchestrator ran `validate-output-format.cjs --system` for product-owner, barter-copywriter, barter-deal-templates and sales-direct-communication on the host Node, and all four exited 0 ("Product Owner output format validation passed across 44 source files").
- **SL-306 (deferred): phase 005 and 006 closure evidence.**
- **SL-307 (blocked): hosted board read-back,** no Figma MCP connected.
- **SL-308 (deferred): live plugin activation.**

Required bug classes (11) are all in `candidateCoverage.covered`, including vendor manifest path escape, plugin symlink reachability and exposure, hosted rollback scope, Flow delivery conflict, hub artifact words, Flow style enforcement, hub negation, flow_check parser edges, plugin manifest contract and Change Location model conformance.

## 10. Audit Appendix

### Convergence summary

| Iteration | Focus | New findings ratio | Graph score | Codex time |
|---|---|---|---|---|
| 1 | Inventory and correctness | 1.00 | 0.400 | 307 s |
| 2 | Security | 0.60 | 0.650 | 318 s |
| 3 | Traceability | 1.00 | 0.683 | 417 s |
| 4 | Maintainability | 1.00 | 0.707 | 351 s |
| 5 | Adversarial replay | 0.29 | 0.725 | 612 s |

Graph convergence stayed STOP_BLOCKED, and the stop policy kept it as telemetry. Every iteration passed `verify-iteration.cjs` (narrative, route proof, delta) on the first dispatch, and no write-containment violation was reported.

### Claim adjudication

Iterations 1 and 2 first recorded failed adjudication: iteration 1 wrote its P1 packet fields as bullets, and the orchestrator's packet parser did not read `~~~json` fences. Iteration 2 added the typed packets, the parser was fixed, and every later event passed.

### Read-only checks the reviewers ran

`run_gates.sh` 10 of 10, `build-plugin.py --self-test` 5 of 5, `route_contract.py --self-check` 5 expectations, the Product Owner format gate over 44 source files. No source file was modified by the loop.

### Ruled-out claims

- The flow_check parser handles comments, ampersand edges, self-loops and per-decision exit counts correctly, and quoted labels are masked.
- Both plugin manifests parse, name and version agree, the marketplace points to `./`, and no MCP server is registered.
- The Change Location model has a provenance row per node, and its stated counts match its edges.
- No Barter flow, board URL or screenshot path was found in the Flow Mode files.

### Sources reviewed

The 118 scope files in `deep-review-config.json`, the phase 003 to 006 spec docs and the parent `goal.md`.
