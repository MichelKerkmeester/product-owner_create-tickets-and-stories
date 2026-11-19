---
title: Deep Review Dashboard
description: Auto-generated reducer view over the review packet.
---

# Deep Review Dashboard - Session Overview

Auto-generated from JSONL state log, iteration files, findings registry, and strategy state. Never manually edited.

<!-- ANCHOR:overview -->
## 1. OVERVIEW

Reducer-generated observability surface for the active review packet.

<!-- /ANCHOR:overview -->
<!-- ANCHOR:status -->
## 2. STATUS
- Review Target: The whole Product Owner system and its nested skills in AI Systems/Product Owner: hub SKILL.md, ROUTER.md and AGENTS.md, sk-product-owner, sk-create-figjam, the vendored mcp-click-up, mcp-aside-devtools, mcp-chrome-devtools, mcp-code-mode and mcp-figma packages, vendor.json and scripts/vendor-sync.py, claude project/, benchmark/ gates and fixtures, manual-testing-playbook/, SYNC.md, READMEs, USER-GUIDE.md and changelogs (directory)
- Started: 2026-11-10T20:08:17Z
- Status: INITIALIZED
- Iteration: 10 of 10
- Provisional Verdict: CONDITIONAL
- hasSearchDebt: true
- hasAdvisories: false
- Session ID: 2026-11-10T20:08:17Z
- Parent Session: none
- Lifecycle Mode: new
- Generation: 1
- continuedFromRun: none

<!-- /ANCHOR:status -->
<!-- ANCHOR:dimension-expansion -->
## 2A. DIMENSION EXPANSION
- Completed pivots: 0
- Failed pivots: 0
- Audited overrides: 0
- Swept: none yet
- Pivot lineage: none yet
- Remaining frontier: none recorded

<!-- /ANCHOR:dimension-expansion -->
<!-- ANCHOR:findings-summary -->
## 3. FINDINGS SUMMARY

| Severity | Count |
|----------|------:|
| P0 (Blockers) | 0 |
| P1 (Required) | 7 |
| P2 (Suggestions) | 21 |
| Resolved | 0 |

<!-- /ANCHOR:findings-summary -->
<!-- ANCHOR:progress -->
## 4. PROGRESS

| # | Focus | Dimensions | Ratio | P0/P1/P2 | Status |
|---|-------|------------|-------|----------|--------|
| 1 | correctness | correctness | 1.00 | 0/1/3 | complete |
| 1 | correctness | correctness | 0.47 | 0/1/2 | complete |
| 1 | traceability: sk-doc alignment (sk-create-skill package shape, README, changelog, frontmatter, manual-testing-playbook and feature-catalog modes) | traceability | 0.12 | 0/0/2 | complete |
| 1 | sk-create-figjam, manual-testing-playbook and the vendored mcp packages: registration drift, broken references and stale examples | correctness | 1.00 | 0/1/1 | complete |
| 1 | traceability: Claude Project mirror and release traceability (claude project/ kernel, knowledge, README and kernel-review.json against sk-product-owner/sk-create-figjam sources, SYNC.md, systems.py declarations, version triangle, playbook capability) | traceability | 1.00 | 0/0/2 | complete |
| null | maintainability: vendored package sync (vendor.json, scripts/vendor-sync.py, 7 packages) against Skilled /doctor:overlay + repin | maintainability | 0.12 | 0/0/2 | complete |
| null | security | security | 1.00 | 0/1/2 | complete |
| null | maintainability | maintainability | 1.00 | 0/0/5 | complete |
| null | maintainability: sk-code language-standard alignment for benchmark/ and scripts/ | maintainability | 0.12 | 0/0/2 | complete |
| null | correctness replay of every open finding plus cross-dimension sweep | correctness/security/traceability/maintainability | 0.18 | 0/0/0 | complete |

<!-- /ANCHOR:progress -->
<!-- ANCHOR:dimension-coverage -->
## 5. DIMENSION COVERAGE

| Dimension | Status | Open findings |
|-----------|--------|--------------:|
| correctness | covered | 18 |
| security | covered | 3 |
| traceability | covered | 0 |
| maintainability | covered | 7 |

<!-- /ANCHOR:dimension-coverage -->
<!-- ANCHOR:blocked-stops -->
## 6. BLOCKED STOPS
No blocked-stop events recorded.

<!-- /ANCHOR:blocked-stops -->
<!-- ANCHOR:graph-convergence -->
## 7. GRAPH CONVERGENCE
- graphConvergenceScore: 0.00
- graphDecision: none
- graphBlockers: none

<!-- /ANCHOR:graph-convergence -->
<!-- ANCHOR:trend -->
## 8. TREND
- Last 3 ratios: 1.00 -> 0.12 -> 0.18
- convergenceScore: 0.82
- openFindings: 28
- persistentSameSeverity: 0
- severityChanged: 0
- repeatedFindings (deprecated combined bucket): 0

<!-- /ANCHOR:trend -->
<!-- ANCHOR:corruption-warnings -->
## 9. CORRUPTION WARNINGS
No corrupt JSONL lines detected.

<!-- /ANCHOR:corruption-warnings -->
<!-- ANCHOR:search-debt -->
## 10. SEARCH DEBT
- graphCoverageMode: graphless_fallback
- candidateCoverage: covered=27, ruledOut=23, deferred=7, blocked=0

### Search Debt
- iteration 3 command_injection (deferred): No subprocess or os.system search was run; budget was spent on the secret surface. The functions read use shutil/pathlib only, which is suggestive but not a search result.; evidence=AI Systems/Product Owner/scripts/vendor-sync.py:403
- iteration 3 secret_exposure (deferred): The check itself was malformed; re-run as `git ls-files context` next iteration.; evidence=AI Systems/Product Owner/.gitignore:35
- iteration 6 test_coverage (deferred): rule line not verified this iteration; evidence=AI Systems/Product Owner/benchmark/grader/check_report.sh:65
- iteration 7 data_loss_path (deferred): budget exhausted before the pull body read; carried as the first required-evidence item in Next Focus; evidence=AI Systems/Product Owner/scripts/vendor-sync.py:52
- iteration 8 vendor_manifest_asymmetry (deferred): Separating a genuine per-package difference from a stale exclude needs vendor-sync.py --verify against the upstream tree, outside this iteration's read-only budget.; evidence=AI Systems/Product Owner/vendor.json:239
- iteration 9 capability_gap (deferred): body comparison deferred to the traceability pass; evidence=AI Systems/Product Owner/manual-testing-playbook/
- iteration 10 secret_artifact_leak (deferred): budget: .gitignore *.har sweep dropped at the tool-call ceiling; evidence=AI Systems/Product Owner/mcp-chrome-devtools/references/cdp-patterns.md:412

### Ruled-Out Candidates
- iteration 1 cross_reference_integrity (ruled_out): complete existence sweep returned zero misses; evidence=AI Systems/Product Owner/ROUTER.md:96-132, AI Systems/Product Owner/leaf-manifest.json:4-114
- iteration 1 routing_precedence (ruled_out): traced each documented example through the declared classes; evidence=AI Systems/Product Owner/hub-router.json:24-81, AI Systems/Product Owner/ROUTER.md:43-44
- iteration 1 version_parity (ruled_out): four-way equality confirmed; evidence=AI Systems/Product Owner/SKILL.md:14, AI Systems/Product Owner/changelog/v1.0.28.0.md:3
- iteration 2 gate_cannot_fail (ruled_out): all five self-test and suite gates execute assertions and fail on planted defects; evidence=AI Systems/Product Owner/benchmark/gates/check_hub.py:701, AI Systems/Product Owner/benchmark/gates/example_lint.py:337, AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:636, AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:1761, AI Systems/Product Owner/scripts/tests/test_vendor_sync.py:352
- iteration 2 exit_code_handling (ruled_out): exit codes match the documented contract at every runner inspected; evidence=AI Systems/Product Owner/benchmark/gates/run_gates.sh:99, AI Systems/Product Owner/benchmark/router/run_fixtures.sh:28, AI Systems/Product Owner/benchmark/format/run_fixtures.sh:250
- iteration 2 dead_path (ruled_out): both paths derive to the same folder from the same start point; evidence=AI Systems/Product Owner/benchmark/gates/run_gates.sh:66, AI Systems/Product Owner/benchmark/gates/rule_parity.py:68
- iteration 4 frontmatter_contract_violation (ruled_out): all required fields present and well formed; evidence=AI Systems/Product Owner/sk-product-owner/SKILL.md:2
- iteration 4 shape_contract_violation (ruled_out): README.md and dated run folders both present; evidence=AI Systems/Product Owner/benchmark/README.md:1
- iteration 4 shape_contract_violation (ruled_out): no universal rule exists in this repository; evidence=.skilled/skills/sk-doc/sk-create-skill/SKILL.md:48
- iteration 4 shape_contract_violation (ruled_out): not a mandatory shape element; evidence=.skilled/skills/sk-doc/sk-create-skill/SKILL.md:167
- iteration 4 shape_contract_violation (ruled_out): contract present and complete; evidence=AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md:24
- iteration 8 stale_example (ruled_out): Count verified accurate: 69 markdown files minus the index is 68.; evidence=AI Systems/Product Owner/sk-product-owner/SKILL.md:290
- iteration 8 stale_example (ruled_out): 7 declared, 7 present, ids match one-to-one.; evidence=AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md:36
- iteration 8 manual_name_drift (ruled_out): Name is used consistently at source and in the package docs.; evidence=AI Systems/Product Owner/.utcp_config.json:16
- iteration 8 manual_name_drift (ruled_out): Namespace consistent; only the version pin is at issue.; evidence=AI Systems/Product Owner/.utcp_config.json:66
- iteration 5 stale_review_record (ruled_out): declared dated record, no live reader; evidence=AI Systems/Product Owner/claude project/kernel-review.json:12, AI Systems/z — Claude Project Sync Loop/episodes/hand-run/000-packet-record/research/iteration-9.md:56
- iteration 5 tracked_vs_ignored_surface (ruled_out): verified by git index query; evidence=AI Systems/Product Owner/.gitignore:15, AI Systems/Product Owner/.gitignore:15
- iteration 5 version_scheme_drift (ruled_out): all three schemes agree with their own changelogs and the README; evidence=AI Systems/Product Owner/claude project/README.md:63
- iteration 7 capability_gap (ruled_out): four structural blockers, each verified by direct read; evidence=.skilled/commands/doctor/scripts/overlay-engine.cjs:73
- iteration 7 config_manifest_drift (ruled_out): byte-identical to the recorded hashes; evidence=AI Systems/Product Owner/vendor.json:1
- iteration 3 secret_exposure (ruled_out): No literal credential in any tracked runtime config; credential references are ${VAR} placeholders.; evidence=AI Systems/Product Owner/.utcp_config.json:79, AI Systems/Product Owner/.env.example:15
- iteration 3 secret_exposure (ruled_out): None of the private files appears in git ls-files, so no pre-ignore commit exists.; evidence=AI Systems/Product Owner/.gitignore:10, AI Systems/Product Owner/.gitignore:16
- iteration 3 confusing_deputy (ruled_out): Deliberate and documented in four places.; evidence=AI Systems/Product Owner/mcp-figma/references/mcp-wiring.md:82, AI Systems/Product Owner/mcp-figma/references/troubleshooting.md:396
- iteration 3 path_traversal (ruled_out): Spelling guard plus resolved containment on the written tree; the docstring's claim holds for the manifest value.; evidence=AI Systems/Product Owner/scripts/vendor-sync.py:322, AI Systems/Product Owner/scripts/vendor-sync.py:363
- iteration 9 capability_gap (ruled_out): shape difference explained by packet kind; evidence=AI Systems/Product Owner/mcp-code-mode/
- iteration 9 documentation_contradiction (ruled_out): self-disclaimed historical record, not a false current claim; evidence=AI Systems/Product Owner/claude project/kernel-review.json:1
- iteration 6 error_handling (ruled_out): verified by direct read; evidence=AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:110
- iteration 6 documentation_contract (ruled_out): declared in vendor manifest; evidence=AI Systems/Product Owner/vendor.json:1
- iteration 6 documentation_contract (ruled_out): prior-iteration ruling honored; evidence=AI Systems/Product Owner/benchmark/reports/README.md
- iteration 10 packaging_hygiene_gap (ruled_out): tracked as claimed; ignored file is local-only by design; evidence=AI Systems/Product Owner/.gitignore:34, AI Systems/Product Owner/context/README.md:1
- iteration 10 stale_documentation (ruled_out): no version or count present; evidence=AI Systems/Product Owner/USER-GUIDE.md:1
- iteration 10 cross_reference_integrity (ruled_out): single hub identity, no duplicate; evidence=AI Systems/Product Owner/graph-metadata.json:1

### Clean Search Proof
- iteration 1 cross_reference_integrity (ruled_out): complete existence sweep returned zero misses; evidence=AI Systems/Product Owner/ROUTER.md:96-132, AI Systems/Product Owner/leaf-manifest.json:4-114
- iteration 1 routing_precedence (ruled_out): traced each documented example through the declared classes; evidence=AI Systems/Product Owner/hub-router.json:24-81, AI Systems/Product Owner/ROUTER.md:43-44
- iteration 1 version_parity (ruled_out): four-way equality confirmed; evidence=AI Systems/Product Owner/SKILL.md:14, AI Systems/Product Owner/changelog/v1.0.28.0.md:3
- iteration 2 gate_cannot_fail (ruled_out): all five self-test and suite gates execute assertions and fail on planted defects; evidence=AI Systems/Product Owner/benchmark/gates/check_hub.py:701, AI Systems/Product Owner/benchmark/gates/example_lint.py:337, AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:636, AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:1761, AI Systems/Product Owner/scripts/tests/test_vendor_sync.py:352
- iteration 2 exit_code_handling (ruled_out): exit codes match the documented contract at every runner inspected; evidence=AI Systems/Product Owner/benchmark/gates/run_gates.sh:99, AI Systems/Product Owner/benchmark/router/run_fixtures.sh:28, AI Systems/Product Owner/benchmark/format/run_fixtures.sh:250
- iteration 2 dead_path (ruled_out): both paths derive to the same folder from the same start point; evidence=AI Systems/Product Owner/benchmark/gates/run_gates.sh:66, AI Systems/Product Owner/benchmark/gates/rule_parity.py:68
- iteration 4 frontmatter_contract_violation (ruled_out): all required fields present and well formed; evidence=AI Systems/Product Owner/sk-product-owner/SKILL.md:2
- iteration 4 shape_contract_violation (ruled_out): README.md and dated run folders both present; evidence=AI Systems/Product Owner/benchmark/README.md:1
- iteration 4 shape_contract_violation (ruled_out): no universal rule exists in this repository; evidence=.skilled/skills/sk-doc/sk-create-skill/SKILL.md:48
- iteration 4 shape_contract_violation (ruled_out): not a mandatory shape element; evidence=.skilled/skills/sk-doc/sk-create-skill/SKILL.md:167
- iteration 4 shape_contract_violation (ruled_out): contract present and complete; evidence=AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md:24
- iteration 8 stale_example (ruled_out): Count verified accurate: 69 markdown files minus the index is 68.; evidence=AI Systems/Product Owner/sk-product-owner/SKILL.md:290
- iteration 8 stale_example (ruled_out): 7 declared, 7 present, ids match one-to-one.; evidence=AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md:36
- iteration 8 manual_name_drift (ruled_out): Name is used consistently at source and in the package docs.; evidence=AI Systems/Product Owner/.utcp_config.json:16
- iteration 8 manual_name_drift (ruled_out): Namespace consistent; only the version pin is at issue.; evidence=AI Systems/Product Owner/.utcp_config.json:66
- iteration 5 stale_review_record (ruled_out): declared dated record, no live reader; evidence=AI Systems/Product Owner/claude project/kernel-review.json:12, AI Systems/z — Claude Project Sync Loop/episodes/hand-run/000-packet-record/research/iteration-9.md:56
- iteration 5 tracked_vs_ignored_surface (ruled_out): verified by git index query; evidence=AI Systems/Product Owner/.gitignore:15, AI Systems/Product Owner/.gitignore:15
- iteration 5 version_scheme_drift (ruled_out): all three schemes agree with their own changelogs and the README; evidence=AI Systems/Product Owner/claude project/README.md:63
- iteration 7 capability_gap (ruled_out): four structural blockers, each verified by direct read; evidence=.skilled/commands/doctor/scripts/overlay-engine.cjs:73
- iteration 7 config_manifest_drift (ruled_out): byte-identical to the recorded hashes; evidence=AI Systems/Product Owner/vendor.json:1
- iteration 3 secret_exposure (ruled_out): No literal credential in any tracked runtime config; credential references are ${VAR} placeholders.; evidence=AI Systems/Product Owner/.utcp_config.json:79, AI Systems/Product Owner/.env.example:15
- iteration 3 secret_exposure (ruled_out): None of the private files appears in git ls-files, so no pre-ignore commit exists.; evidence=AI Systems/Product Owner/.gitignore:10, AI Systems/Product Owner/.gitignore:16
- iteration 3 confusing_deputy (ruled_out): Deliberate and documented in four places.; evidence=AI Systems/Product Owner/mcp-figma/references/mcp-wiring.md:82, AI Systems/Product Owner/mcp-figma/references/troubleshooting.md:396
- iteration 3 path_traversal (ruled_out): Spelling guard plus resolved containment on the written tree; the docstring's claim holds for the manifest value.; evidence=AI Systems/Product Owner/scripts/vendor-sync.py:322, AI Systems/Product Owner/scripts/vendor-sync.py:363
- iteration 9 capability_gap (ruled_out): shape difference explained by packet kind; evidence=AI Systems/Product Owner/mcp-code-mode/
- iteration 9 documentation_contradiction (ruled_out): self-disclaimed historical record, not a false current claim; evidence=AI Systems/Product Owner/claude project/kernel-review.json:1
- iteration 6 error_handling (ruled_out): verified by direct read; evidence=AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:110
- iteration 6 documentation_contract (ruled_out): declared in vendor manifest; evidence=AI Systems/Product Owner/vendor.json:1
- iteration 6 documentation_contract (ruled_out): prior-iteration ruling honored; evidence=AI Systems/Product Owner/benchmark/reports/README.md
- iteration 10 packaging_hygiene_gap (ruled_out): tracked as claimed; ignored file is local-only by design; evidence=AI Systems/Product Owner/.gitignore:34, AI Systems/Product Owner/context/README.md:1
- iteration 10 stale_documentation (ruled_out): no version or count present; evidence=AI Systems/Product Owner/USER-GUIDE.md:1
- iteration 10 cross_reference_integrity (ruled_out): single hub identity, no duplicate; evidence=AI Systems/Product Owner/graph-metadata.json:1
- iteration 10 cross_reference_integrity (not_applicable): no feature catalog in this surface; evidence=AI Systems/Product Owner/SKILL.md:66

<!-- /ANCHOR:search-debt -->
<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
- **Dimension:** terminal -- all four dimensions are complete (correctness replayed here, security at iteration 3, traceability at iteration 4, maintainability at iteration 9). - **Focus area:** none; the loop reached `max-iterations` with 4 P1 and 21 P2 active. - **Reason:** `stopPolicy: max-iterations` -- all 10 iterations run and convergence is telemetry only. Hand-off is to `/speckit:plan` for the four P1s, in the order R10-REF-001, R10-REF-002, R10-REF-003, then R3-P1-001. - **Rotation status:** closed. - **Blocked/productive carry-forward:** productive -- the three refinements are remediation-ready and each names the exact edit surface. - **Required evidence:** none outstanding. - **Recovery note:** budget edge case 4 above is the one process deviation; it did not change a finding. Review verdict: CONDITIONAL

<!-- /ANCHOR:next-focus -->
<!-- ANCHOR:active-risks -->
## 12. ACTIVE RISKS
- 7 active P1 finding(s) — required before release; not a P0 but still blocks PASS.
- Claim-adjudication gate last failed at run 10 (missing packets: R10-REF-001, R10-REF-002, R10-REF-003). STOP is vetoed until every active P0/P1 has a typed claim-adjudication packet.
- 7 search-debt obligation(s) remain deferred or blocked. Verdict is CONDITIONAL until they are covered or ruled out.

<!-- /ANCHOR:active-risks -->
