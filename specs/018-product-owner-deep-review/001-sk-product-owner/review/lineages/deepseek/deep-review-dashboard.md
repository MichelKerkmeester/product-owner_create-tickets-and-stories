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
- Review Target: AI Systems/Product Owner/sk-product-owner (skill)
- Started: 2026-10-21T11:02:33Z
- Status: INITIALIZED
- Iteration: 5 of 5
- Provisional Verdict: CONDITIONAL
- hasSearchDebt: false
- hasAdvisories: false
- Session ID: fanout-deepseek-1792580414886-kf3maf
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
| P1 (Required) | 2 |
| P2 (Suggestions) | 13 |
| Resolved | 0 |

<!-- /ANCHOR:findings-summary -->
<!-- ANCHOR:progress -->
## 4. PROGRESS

| # | Focus | Dimensions | Ratio | P0/P1/P2 | Status |
|---|-------|------------|-------|----------|--------|
| 1 | correctness | correctness | 1.00 | 0/1/2 | complete |
| 2 | traceability | traceability | 1.00 | 0/1/4 | complete |
| 3 | maintainability | maintainability | 1.00 | 0/0/4 | complete |
| 4 | security | security | 1.00 | 0/0/2 | complete |
| 5 | traceability | traceability | 1.00 | 0/0/1 | complete |

<!-- /ANCHOR:progress -->
<!-- ANCHOR:dimension-coverage -->
## 5. DIMENSION COVERAGE

| Dimension | Status | Open findings |
|-----------|--------|--------------:|
| correctness | covered | 15 |
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
- graphConvergenceScore: 0.00
- graphDecision: none
- graphBlockers: none

<!-- /ANCHOR:graph-convergence -->
<!-- ANCHOR:trend -->
## 8. TREND
- Last 3 ratios: 1.00 -> 1.00 -> 1.00
- convergenceScore: 0.00
- openFindings: 15
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
- candidateCoverage: covered=14, ruledOut=12, deferred=0, blocked=0

### Search Debt
[None yet]

### Ruled-Out Candidates
- iteration 1 contract_contradiction (ruled_out): Thresholds agree; the Story/Epic carve-out is documented in the routing detail; evidence=AI Systems/Product Owner/sk-product-owner/references/routing.md:31
- iteration 3 example_budget (ruled_out): Grammar is consistent across all 22 examples; only the word caps break; evidence=AI Systems/Product Owner/sk-product-owner/assets/examples/doc/doc-example-guide.md:9
- iteration 4 secret_exposure (ruled_out): No secret exists in the packet and the environment contract keeps it out of tracked files; evidence=AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/skill-backlog-modes/clickup-push-targets.md:15, AI Systems/Product Owner/.env.example:7
- iteration 4 external_write_gate (ruled_out): Three independent gates confirmed by direct read; evidence=AI Systems/Product Owner/sk-product-owner/SKILL.md:191
- iteration 5 anchor_drift (ruled_out): Anchors current and in range today; fragility recorded as an edge case, not a defect; evidence=AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/skill-story-modes/story-refinement.md:15
- iteration 5 cross_runtime_parity (ruled_out): Parity holds by name and kind; runtime-proof divergence is the documented design; evidence=AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/manual-testing-playbook.md:45
- iteration 5 playbook_coverage_gap (ruled_out): Re-read confirmed both P1 findings rather than dissolving them; evidence=AI Systems/Product Owner/sk-product-owner/references/quality-scoring.md:160, AI Systems/Product Owner/sk-product-owner/references/router-contract.md:17

### Clean Search Proof
- iteration 1 contract_contradiction (ruled_out): Thresholds agree; the Story/Epic carve-out is documented in the routing detail; evidence=AI Systems/Product Owner/sk-product-owner/references/routing.md:31
- iteration 3 example_budget (ruled_out): Grammar is consistent across all 22 examples; only the word caps break; evidence=AI Systems/Product Owner/sk-product-owner/assets/examples/doc/doc-example-guide.md:9
- iteration 4 secret_exposure (ruled_out): No secret exists in the packet and the environment contract keeps it out of tracked files; evidence=AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/skill-backlog-modes/clickup-push-targets.md:15, AI Systems/Product Owner/.env.example:7
- iteration 4 external_write_gate (ruled_out): Three independent gates confirmed by direct read; evidence=AI Systems/Product Owner/sk-product-owner/SKILL.md:191
- iteration 5 anchor_drift (ruled_out): Anchors current and in range today; fragility recorded as an edge case, not a defect; evidence=AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/skill-story-modes/story-refinement.md:15
- iteration 5 cross_runtime_parity (ruled_out): Parity holds by name and kind; runtime-proof divergence is the documented design; evidence=AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/manual-testing-playbook.md:45
- iteration 5 playbook_coverage_gap (ruled_out): Re-read confirmed both P1 findings rather than dissolving them; evidence=AI Systems/Product Owner/sk-product-owner/references/quality-scoring.md:160, AI Systems/Product Owner/sk-product-owner/references/router-contract.md:17

<!-- /ANCHOR:search-debt -->
<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
- Dimension: none — this is the fifth and final iteration (`stopPolicy: max-iterations`, `maxIterations: 5`) - Focus area: synthesis of 15 active findings (0 P0, 2 P1, 13 P2) - Reason: the iteration ceiling is reached, so synthesis runs with `stopReason: maxIterationsReached` and convergence treated as telemetry throughout - Rotation status: correctness, traceability, maintainability and security each covered; no dimension left unreviewed - Required evidence: the findings registry reduced from the five deltas, plus the terminal close-out record - Recovery note: none --- Review verdict: CONDITIONAL

<!-- /ANCHOR:next-focus -->
<!-- ANCHOR:active-risks -->
## 12. ACTIVE RISKS
- 2 active P1 finding(s) — required before release; not a P0 but still blocks PASS.

<!-- /ANCHOR:active-risks -->
