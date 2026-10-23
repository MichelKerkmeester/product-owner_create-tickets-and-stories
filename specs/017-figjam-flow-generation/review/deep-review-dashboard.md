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
- Review Target: Uncommitted work of specs/017-figjam-flow-generation phases 003-006 (vendored figma packet, parent hub conversion, Flow Mode, Claude Code plugin) in the Product Owner repo plus four Sync Loop files and the Change Location flow model in the outer AI Systems repo (files)
- Started: 2026-10-20T05:23:58Z
- Status: INITIALIZED
- Iteration: 5 of 5
- Provisional Verdict: FAIL
- hasSearchDebt: true
- hasAdvisories: false
- Session ID: 2026-10-20T05:23:58Z
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
| P0 (Blockers) | 2 |
| P1 (Required) | 5 |
| P2 (Suggestions) | 5 |
| Resolved | 0 |

<!-- /ANCHOR:findings-summary -->
<!-- ANCHOR:progress -->
## 4. PROGRESS

| # | Focus | Dimensions | Ratio | P0/P1/P2 | Status |
|---|-------|------------|-------|----------|--------|
| 1 | inventory pass, then correctness: executable surfaces | correctness | 1.00 | 0/1/1 | complete |
| 2 | security: path containment, symlink handling, public-repository leakage, and Flow Mode write gate | security | 0.60 | 2/2/1 | complete |
| 3 | traceability: phase specs/checklist evidence, Flow route parity, playbook citations, and feature catalog source perimeter | traceability | 1.00 | 0/1/0 | complete |
| 4 | maintainability: benchmark documentation, self-test strength, route-contract drift guards, comment hygiene and HVR punctuation | maintainability | 1.00 | 0/0/2 | complete |
| 5 | closing adversarial replay and severity calibration | correctness/security/traceability/maintainability | 0.29 | 0/4/3 | complete |

<!-- /ANCHOR:progress -->
<!-- ANCHOR:dimension-coverage -->
## 5. DIMENSION COVERAGE

| Dimension | Status | Open findings |
|-----------|--------|--------------:|
| correctness | covered | 12 |
| security | covered | 0 |
| traceability | covered | 0 |
| maintainability | covered | 0 |

<!-- /ANCHOR:dimension-coverage -->
<!-- ANCHOR:blocked-stops -->
## 6. BLOCKED STOPS
No blocked-stop events recorded.

<!-- /ANCHOR:blocked-stops -->
<!-- ANCHOR:graph-convergence -->
## 7. GRAPH CONVERGENCE
- graphConvergenceScore: 0.72
- graphDecision: STOP_BLOCKED
- graphBlockers: {"count":11,"description":"Dimension coverage (50%) is below threshold (80%). 11 gap(s) found. STOP is blocked until all required dimensions have meaningful coverage.","severity":"blocking","type":"uncovered_dimensions"}

<!-- /ANCHOR:graph-convergence -->
<!-- ANCHOR:trend -->
## 8. TREND
- Last 3 ratios: 1.00 -> 1.00 -> 0.29
- convergenceScore: 0.71
- openFindings: 12
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
- candidateCoverage: covered=15, ruledOut=19, deferred=2, blocked=2

### Search Debt
- iteration 1 outer_output_gate_runtime (blocked): Restore a working Node runtime or required simdutf library, then rerun the outer validator.; evidence=../z — Claude Project Sync Loop/systems.cjs:72, ../z — Claude Project Sync Loop/systems.cjs:266, ../z — Claude Project Sync Loop/validate-output-format.cjs:1291
- iteration 3 phase_closure_checklist_evidence (deferred): Revisit when either phase is proposed as complete or its acceptance criteria are updated.; evidence=specs/017-figjam-flow-generation/003-vendored-figma-and-sync/tasks.md:44, specs/017-figjam-flow-generation/003-vendored-figma-and-sync/implementation-summary.md:95, specs/017-figjam-flow-generation/004-parent-hub-conversion/tasks.md:44, specs/017-figjam-flow-generation/004-parent-hub-conversion/implementation-summary.md:97, specs/017-figjam-flow-generation/005-flow-mode/tasks.md:34, specs/017-figjam-flow-generation/005-flow-mode/implementation-summary.md:48, specs/017-figjam-flow-generation/006-claude-code-plugin/tasks.md:34, specs/017-figjam-flow-generation/006-claude-code-plugin/implementation-summary.md:48
- iteration 3 hosted_board_readback_evidence (blocked): The review strategy records that no hosted Figma MCP was connected; the board criterion is explicitly blocked by environment.; evidence=specs/017-figjam-flow-generation/005-flow-mode/goal.md:59, /Users/michelkerkmeester/MEGA/Development/AI Systems/Product Context/a — Screenshots/Barter Managed/Dashboard/Flows/Change Location/change-location-flow-model.md:17
- iteration 3 plugin_live_flow_activation (deferred): Defer until an authorized Claude --plugin-dir session can provide evidence.; evidence=claude-plugin/.claude-plugin/plugin.json:4, specs/017-figjam-flow-generation/006-claude-code-plugin/acceptance-criteria.md:57

### Ruled-Out Candidates
- iteration 1 flow_checker_seeded_rule_regression (ruled_out): The positive model passed and all six representative invalid models failed as expected.; evidence=sk-product-owner/scripts/flow_check.py:44, sk-product-owner/scripts/flow_check.py:70, benchmark/gates/run_gates.sh:47, sk-product-owner/scripts/flow_check.py:134
- iteration 1 router_contract_drift (ruled_out): No current fixture or differential mismatch was reported by the gate suite.; evidence=benchmark/router/route_contract.py:881, benchmark/gates/run_gates.sh:37, benchmark/router/differential.py:687
- iteration 1 vendor_hash_drift (ruled_out): Vendor sync status reported 58 Figma files and one Mermaid extractor file in step.; evidence=vendor.json:1, benchmark/gates/run_gates.sh:43, scripts/build-plugin.py:87
- iteration 2 flow_checker_symlink_input_escape (ruled_out): No security-impacting escape was established for the read-only input path.; evidence=sk-product-owner/scripts/flow_check.py:70, sk-product-owner/scripts/flow_check.py:156
- iteration 2 extractor_output_path_escape (ruled_out): No untrusted model content controls the explicit output path.; evidence=sk-product-owner/scripts/vendored/mermaid_extract.py:1395, sk-product-owner/scripts/vendored/mermaid_extract.py:1413
- iteration 2 plugin_manifest_secret_or_mcp_registration (ruled_out): No MCP server registration or secret-like value was present.; evidence=claude-plugin/.claude-plugin/plugin.json:1, claude-plugin/.claude-plugin/marketplace.json:1
- iteration 2 private_flow_or_board_leakage (ruled_out): Search found no copied Barter flow or actual board/account/path data.; evidence=sk-product-owner/references/flow-mode.md:74, sk-product-owner/references/flow-mode.md:114, sk-product-owner/assets/flow-templates.md:111, sk-product-owner/assets/flow-templates.md:121
- iteration 2 vendored_extractor_hash_drift (ruled_out): Computed SHA-256 equals vendor.json entry.; evidence=vendor.json:1, sk-product-owner/scripts/vendored/mermaid_extract.py:1
- iteration 3 phase_acceptance_status_drift (ruled_out): Open phases are labeled unchecked/Unmet rather than complete.; evidence=specs/017-figjam-flow-generation/003-vendored-figma-and-sync/acceptance-criteria.md:52, specs/017-figjam-flow-generation/004-parent-hub-conversion/acceptance-criteria.md:52, specs/017-figjam-flow-generation/005-flow-mode/goal.md:57, specs/017-figjam-flow-generation/006-claude-code-plugin/goal.md:54, specs/017-figjam-flow-generation/003-vendored-figma-and-sync/tasks.md:44, specs/017-figjam-flow-generation/003-vendored-figma-and-sync/implementation-summary.md:95, specs/017-figjam-flow-generation/004-parent-hub-conversion/tasks.md:44, specs/017-figjam-flow-generation/004-parent-hub-conversion/implementation-summary.md:97, specs/017-figjam-flow-generation/005-flow-mode/tasks.md:34, specs/017-figjam-flow-generation/005-flow-mode/implementation-summary.md:48, specs/017-figjam-flow-generation/006-claude-code-plugin/tasks.md:34, specs/017-figjam-flow-generation/006-claude-code-plugin/implementation-summary.md:48
- iteration 3 flow_route_cross_runtime_drift (ruled_out): No static Flow intent or resource-map drift was found.; evidence=sk-product-owner/ROUTER.md:36, sk-product-owner/ROUTER.md:50, sk-product-owner/references/router-contract.md:329, benchmark/router/route_contract.py:329, claude project/Custom Instructions.md:487, claude project/Custom Instructions.md:553
- iteration 3 playbook_citation_line_drift (ruled_out): No stale or out-of-range remapped target was found.; evidence=sk-product-owner/manual-testing-playbook/manual-testing-playbook.md:151, sk-product-owner/manual-testing-playbook/skill-backlog-modes/data-tracking-task.md:1, sk-product-owner/manual-testing-playbook/skill-interactive-routing/conflicting-commands.md:1, sk-product-owner/manual-testing-playbook/skill-story-modes/story-with-nested-tasks.md:1
- iteration 3 feature_catalog_extra_sources_drift (ruled_out): No extraSources documentation drift was found.; evidence=/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/z — Claude Project Sync Loop/systems.cjs:72, /Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/z — Claude Project Sync Loop/systems.cjs:266, /Users/michelkerkme/MEGA/Development/AI Systems/AI Systems/z — Claude Project Sync Loop/README.md:318, /Users/michelkerkme/MEGA/Development/AI Systems/AI Systems/z — Claude Project Sync Loop/feature-catalog/output-format-gate/output-format-validator.md:32
- iteration 4 vacuous_self_test (ruled_out): Each reviewed harness contains a clean baseline or scratch-world setup and explicit expected results.; evidence=sk-product-owner/scripts/flow_check.py:134, benchmark/gates/check_hub.py:243, scripts/build-plugin.py:144, scripts/tests/test_vendor_sync.py:75
- iteration 4 duplicated_router_contract_drift (ruled_out): Static guard paths cover the identified copies and inputs.; evidence=benchmark/router/differential.py:306, benchmark/router/differential.py:467, benchmark/router/differential.py:569, benchmark/router/differential.py:616, benchmark/router/differential_corpus.json:32, claude project/Custom Instructions.md:553
- iteration 4 code_comment_metadata_leak (ruled_out): Exact comment search returned no matches.; evidence=benchmark/gates/check_hub.py:1, benchmark/router/differential.py:1, scripts/build-plugin.py:1
- iteration 5 hub_negation_contract (ruled_out): Current behavior follows the stated within-clause rule for reviewed forms; vocabulary parity is included in the artifactWords gate recommendation.; evidence=hub-router.json:30, SKILL.md:34, benchmark/gates/check_hub.py:63, benchmark/gates/check_hub.py:66, benchmark/gates/check_hub.py:203, benchmark/gates/check_hub.py:212
- iteration 5 flow_checker_parser_edges (ruled_out): The inspected edges map to explicit graph edges or fail closed under the documented Flow grammar.; evidence=sk-product-owner/scripts/vendored/mermaid_extract.py:357, sk-product-owner/scripts/vendored/mermaid_extract.py:390, sk-product-owner/scripts/vendored/mermaid_extract.py:659, sk-product-owner/scripts/vendored/mermaid_extract.py:711, sk-product-owner/scripts/vendored/mermaid_extract.py:791, sk-product-owner/scripts/flow_check.py:56
- iteration 5 plugin_manifest_contract (ruled_out): Reviewed manifest fields are consistent and builder checks align with skills-only shape.; evidence=claude-plugin/.claude-plugin/plugin.json:1, claude-plugin/.claude-plugin/marketplace.json:1, scripts/build-plugin.py:110, scripts/build-plugin.py:113
- iteration 5 change_location_model_conformance (ruled_out): Static comparison of model and its own provenance table found no inconsistency.; evidence=/Users/michelkerkmeester/MEGA/Development/AI Systems/Product Context/a — Screenshots/Barter Managed/Dashboard/Flows/Change Location/change-location-flow-model.md:5, /Users/michelkerkme/MEGA/Development/AI Systems/Product Context/a — Screenshots/Barter Managed/Dashboard/Flows/Change Location/change-location-flow-model.md:17, /Users/michelkerkme/MEGA/Development/AI Systems/Product Context/a — Screenshots/Barter Managed/Dashboard/Flows/Change Location/change-location-flow-model.md:19, /Users/michelkerkme/MEGA/Development/AI Systems/Product Context/a — Screenshots/Barter Managed/Dashboard/Flows/Change Location/change-location-flow-model.md:30

### Clean Search Proof
- iteration 1 flow_checker_seeded_rule_regression (ruled_out): The positive model passed and all six representative invalid models failed as expected.; evidence=sk-product-owner/scripts/flow_check.py:44, sk-product-owner/scripts/flow_check.py:70, benchmark/gates/run_gates.sh:47, sk-product-owner/scripts/flow_check.py:134
- iteration 1 router_contract_drift (ruled_out): No current fixture or differential mismatch was reported by the gate suite.; evidence=benchmark/router/route_contract.py:881, benchmark/gates/run_gates.sh:37, benchmark/router/differential.py:687
- iteration 1 vendor_hash_drift (ruled_out): Vendor sync status reported 58 Figma files and one Mermaid extractor file in step.; evidence=vendor.json:1, benchmark/gates/run_gates.sh:43, scripts/build-plugin.py:87
- iteration 2 flow_checker_symlink_input_escape (ruled_out): No security-impacting escape was established for the read-only input path.; evidence=sk-product-owner/scripts/flow_check.py:70, sk-product-owner/scripts/flow_check.py:156
- iteration 2 extractor_output_path_escape (ruled_out): No untrusted model content controls the explicit output path.; evidence=sk-product-owner/scripts/vendored/mermaid_extract.py:1395, sk-product-owner/scripts/vendored/mermaid_extract.py:1413
- iteration 2 plugin_manifest_secret_or_mcp_registration (ruled_out): No MCP server registration or secret-like value was present.; evidence=claude-plugin/.claude-plugin/plugin.json:1, claude-plugin/.claude-plugin/marketplace.json:1
- iteration 2 private_flow_or_board_leakage (ruled_out): Search found no copied Barter flow or actual board/account/path data.; evidence=sk-product-owner/references/flow-mode.md:74, sk-product-owner/references/flow-mode.md:114, sk-product-owner/assets/flow-templates.md:111, sk-product-owner/assets/flow-templates.md:121
- iteration 2 vendored_extractor_hash_drift (ruled_out): Computed SHA-256 equals vendor.json entry.; evidence=vendor.json:1, sk-product-owner/scripts/vendored/mermaid_extract.py:1
- iteration 3 phase_acceptance_status_drift (ruled_out): Open phases are labeled unchecked/Unmet rather than complete.; evidence=specs/017-figjam-flow-generation/003-vendored-figma-and-sync/acceptance-criteria.md:52, specs/017-figjam-flow-generation/004-parent-hub-conversion/acceptance-criteria.md:52, specs/017-figjam-flow-generation/005-flow-mode/goal.md:57, specs/017-figjam-flow-generation/006-claude-code-plugin/goal.md:54, specs/017-figjam-flow-generation/003-vendored-figma-and-sync/tasks.md:44, specs/017-figjam-flow-generation/003-vendored-figma-and-sync/implementation-summary.md:95, specs/017-figjam-flow-generation/004-parent-hub-conversion/tasks.md:44, specs/017-figjam-flow-generation/004-parent-hub-conversion/implementation-summary.md:97, specs/017-figjam-flow-generation/005-flow-mode/tasks.md:34, specs/017-figjam-flow-generation/005-flow-mode/implementation-summary.md:48, specs/017-figjam-flow-generation/006-claude-code-plugin/tasks.md:34, specs/017-figjam-flow-generation/006-claude-code-plugin/implementation-summary.md:48
- iteration 3 flow_route_cross_runtime_drift (ruled_out): No static Flow intent or resource-map drift was found.; evidence=sk-product-owner/ROUTER.md:36, sk-product-owner/ROUTER.md:50, sk-product-owner/references/router-contract.md:329, benchmark/router/route_contract.py:329, claude project/Custom Instructions.md:487, claude project/Custom Instructions.md:553
- iteration 3 playbook_citation_line_drift (ruled_out): No stale or out-of-range remapped target was found.; evidence=sk-product-owner/manual-testing-playbook/manual-testing-playbook.md:151, sk-product-owner/manual-testing-playbook/skill-backlog-modes/data-tracking-task.md:1, sk-product-owner/manual-testing-playbook/skill-interactive-routing/conflicting-commands.md:1, sk-product-owner/manual-testing-playbook/skill-story-modes/story-with-nested-tasks.md:1
- iteration 3 feature_catalog_extra_sources_drift (ruled_out): No extraSources documentation drift was found.; evidence=/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/z — Claude Project Sync Loop/systems.cjs:72, /Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/z — Claude Project Sync Loop/systems.cjs:266, /Users/michelkerkme/MEGA/Development/AI Systems/AI Systems/z — Claude Project Sync Loop/README.md:318, /Users/michelkerkme/MEGA/Development/AI Systems/AI Systems/z — Claude Project Sync Loop/feature-catalog/output-format-gate/output-format-validator.md:32
- iteration 4 vacuous_self_test (ruled_out): Each reviewed harness contains a clean baseline or scratch-world setup and explicit expected results.; evidence=sk-product-owner/scripts/flow_check.py:134, benchmark/gates/check_hub.py:243, scripts/build-plugin.py:144, scripts/tests/test_vendor_sync.py:75
- iteration 4 duplicated_router_contract_drift (ruled_out): Static guard paths cover the identified copies and inputs.; evidence=benchmark/router/differential.py:306, benchmark/router/differential.py:467, benchmark/router/differential.py:569, benchmark/router/differential.py:616, benchmark/router/differential_corpus.json:32, claude project/Custom Instructions.md:553
- iteration 4 code_comment_metadata_leak (ruled_out): Exact comment search returned no matches.; evidence=benchmark/gates/check_hub.py:1, benchmark/router/differential.py:1, scripts/build-plugin.py:1
- iteration 5 hub_negation_contract (ruled_out): Current behavior follows the stated within-clause rule for reviewed forms; vocabulary parity is included in the artifactWords gate recommendation.; evidence=hub-router.json:30, SKILL.md:34, benchmark/gates/check_hub.py:63, benchmark/gates/check_hub.py:66, benchmark/gates/check_hub.py:203, benchmark/gates/check_hub.py:212
- iteration 5 flow_checker_parser_edges (ruled_out): The inspected edges map to explicit graph edges or fail closed under the documented Flow grammar.; evidence=sk-product-owner/scripts/vendored/mermaid_extract.py:357, sk-product-owner/scripts/vendored/mermaid_extract.py:390, sk-product-owner/scripts/vendored/mermaid_extract.py:659, sk-product-owner/scripts/vendored/mermaid_extract.py:711, sk-product-owner/scripts/vendored/mermaid_extract.py:791, sk-product-owner/scripts/flow_check.py:56
- iteration 5 plugin_manifest_contract (ruled_out): Reviewed manifest fields are consistent and builder checks align with skills-only shape.; evidence=claude-plugin/.claude-plugin/plugin.json:1, claude-plugin/.claude-plugin/marketplace.json:1, scripts/build-plugin.py:110, scripts/build-plugin.py:113
- iteration 5 change_location_model_conformance (ruled_out): Static comparison of model and its own provenance table found no inconsistency.; evidence=/Users/michelkerkmeester/MEGA/Development/AI Systems/Product Context/a — Screenshots/Barter Managed/Dashboard/Flows/Change Location/change-location-flow-model.md:5, /Users/michelkerkme/MEGA/Development/AI Systems/Product Context/a — Screenshots/Barter Managed/Dashboard/Flows/Change Location/change-location-flow-model.md:17, /Users/michelkerkme/MEGA/Development/AI Systems/Product Context/a — Screenshots/Barter Managed/Dashboard/Flows/Change Location/change-location-flow-model.md:19, /Users/michelkerkme/MEGA/Development/AI Systems/Product Context/a — Screenshots/Barter Managed/Dashboard/Flows/Change Location/change-location-flow-model.md:30

<!-- /ANCHOR:search-debt -->
<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
[All dimensions covered]

<!-- /ANCHOR:next-focus -->
<!-- ANCHOR:active-risks -->
## 12. ACTIVE RISKS
- 2 active P0 finding(s) blocking release.
- 5 active P1 finding(s) — required before release; not a P0 but still blocks PASS.
- 4 search-debt obligation(s) remain deferred or blocked. Verdict is CONDITIONAL until they are covered or ruled out.

<!-- /ANCHOR:active-risks -->
