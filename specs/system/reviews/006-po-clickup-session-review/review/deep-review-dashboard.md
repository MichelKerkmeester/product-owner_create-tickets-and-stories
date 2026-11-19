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
- Review Target: Session work 2026-11-10: Product Owner packets 026 (browser-first ClickUp doc page writer in mcp-click-up/references/mcp-tools.md section 8), 027 (Mark-as-done between two dividers, format validator and fixtures), 028 (feedback ticket template), commits 246b3f54..47b8b333 (files)
- Started: 2026-11-10T18:34:20Z
- Status: INITIALIZED
- Iteration: 5 of 5
- Provisional Verdict: CONDITIONAL
- hasSearchDebt: true
- hasAdvisories: false
- Session ID: 2026-11-10T18:34:20Z
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
| P1 (Required) | 5 |
| P2 (Suggestions) | 13 |
| Resolved | 0 |

<!-- /ANCHOR:findings-summary -->
<!-- ANCHOR:progress -->
## 4. PROGRESS

| # | Focus | Dimensions | Ratio | P0/P1/P2 | Status |
|---|-------|------------|-------|----------|--------|
| null | correctness | correctness | 1.00 | 0/1/3 | complete |
| null | security | security | 1.00 | 0/1/2 | complete |
| null | traceability | traceability | 0.94 | 0/1/3 | complete |
| null | maintainability | maintainability | 0.88 | 0/0/4 | complete |
| null | correctness replay of every open finding plus cross-dimension sweep | correctness/security/traceability/maintainability | 0.10 | 0/0/0 | complete |

<!-- /ANCHOR:progress -->
<!-- ANCHOR:dimension-coverage -->
## 5. DIMENSION COVERAGE

| Dimension | Status | Open findings |
|-----------|--------|--------------:|
| correctness | covered | 11 |
| security | covered | 3 |
| traceability | covered | 4 |
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
- Last 3 ratios: 0.94 -> 0.88 -> 0.10
- convergenceScore: 0.90
- openFindings: 18
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
- candidateCoverage: covered=20, ruledOut=10, deferred=1, blocked=3

### Search Debt
- iteration 3 count_drift (blocked): The gate's pair selection code was not read, so its 63 cannot be reconciled; no claim is made either way; evidence=AI Systems/Product Owner/benchmark/gates/rule_parity.py:52
- iteration 3 stale_evidence (deferred): The gate harness was not located this iteration; carried to iteration 4; evidence=AI Systems/Product Owner/specs/system/026-browser-first-doc-writer/tasks.md:52
- iteration 4 vendored_manifest_integrity (blocked): The SHA-256 of references/mcp-tools.md at HEAD was not computed, so neither side of the comparison exists; evidence=AI Systems/Product Owner/vendor.json:1
- iteration 5 spec_evidence_mismatch (blocked): run_gates.sh never located despite five passes of searching; evidence=AI Systems/Product Owner/specs/system/028-feedback-ticket-template/spec.md:94

### Ruled-Out Candidates
- iteration 1 spec_mismatch (ruled_out): symbol diff returned identical bodies; evidence=AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:143, AI Systems/z — Claude Project Sync Loop/validate-output-format.cjs:197
- iteration 1 boundary_handling (ruled_out): loop bound covers both directions; evidence=AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:153
- iteration 1 state_transition (ruled_out): verified by direct read; evidence=AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:1583
- iteration 1 state_transition (ruled_out): verified by direct read; evidence=AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:445
- iteration 2 secret_exposure (ruled_out): Pattern scan across the whole tracked tree found documentation placeholders only.; evidence=AI Systems/Product Owner/SYNC.md:18
- iteration 2 write_surface (ruled_out): Cannot combine --write with an explicit file list.; evidence=AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:34
- iteration 2 write_surface (ruled_out): No write primitive present in either script.; evidence=AI Systems/Product Owner/benchmark/gates/rule_parity.py:191
- iteration 3 mirror_parity (ruled_out): Anchored body diff is identical to the end of the file; evidence=AI Systems/Product Owner/sk-product-owner/assets/examples/task/task-example-feedback.md:10, AI Systems/Product Owner/claude project/knowledge/Product Owner - Examples - Task - Feedback Ticket.md:7
- iteration 3 mirror_parity (ruled_out): Declaration present, so the pair is diffed; evidence=AI Systems/z — Claude Project Sync Loop/systems.py:1796
- iteration 4 doc_code_drift (ruled_out): Zero em dashes on every changed prose surface; all semicolon hits resolve to fenced code; evidence=AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:594
- iteration 4 harness_parity (ruled_out): diff is empty for all three fixtures; evidence=AI Systems/Product Owner/benchmark/format/fixtures/markasdone-divider-silent.md:1
- iteration 4 doc_code_drift (ruled_out): All five named files exist and match their stated roles; evidence=AI Systems/z — Claude Project Sync Loop/feature-catalog/output-format-gate/output-format-validator.md:44
- iteration 5 state_transition (ruled_out): counterevidence at mcp-tools.md:589 and :608 refutes the gaps-only premise; evidence=AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:565, AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:566, AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:589
- iteration 5 doc_count_drift (ruled_out): direct read of both expressions and their initialisers; evidence=AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:694, AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:776

### Clean Search Proof
- iteration 1 spec_mismatch (ruled_out): symbol diff returned identical bodies; evidence=AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:143, AI Systems/z — Claude Project Sync Loop/validate-output-format.cjs:197
- iteration 1 boundary_handling (ruled_out): loop bound covers both directions; evidence=AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:153
- iteration 1 state_transition (ruled_out): verified by direct read; evidence=AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:1583
- iteration 1 state_transition (ruled_out): verified by direct read; evidence=AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:445
- iteration 2 secret_exposure (ruled_out): Pattern scan across the whole tracked tree found documentation placeholders only.; evidence=AI Systems/Product Owner/SYNC.md:18
- iteration 2 write_surface (ruled_out): Cannot combine --write with an explicit file list.; evidence=AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:34
- iteration 2 write_surface (ruled_out): No write primitive present in either script.; evidence=AI Systems/Product Owner/benchmark/gates/rule_parity.py:191
- iteration 3 mirror_parity (ruled_out): Anchored body diff is identical to the end of the file; evidence=AI Systems/Product Owner/sk-product-owner/assets/examples/task/task-example-feedback.md:10, AI Systems/Product Owner/claude project/knowledge/Product Owner - Examples - Task - Feedback Ticket.md:7
- iteration 3 mirror_parity (ruled_out): Declaration present, so the pair is diffed; evidence=AI Systems/z — Claude Project Sync Loop/systems.py:1796
- iteration 4 doc_code_drift (ruled_out): Zero em dashes on every changed prose surface; all semicolon hits resolve to fenced code; evidence=AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:594
- iteration 4 harness_parity (ruled_out): diff is empty for all three fixtures; evidence=AI Systems/Product Owner/benchmark/format/fixtures/markasdone-divider-silent.md:1
- iteration 4 doc_code_drift (ruled_out): All five named files exist and match their stated roles; evidence=AI Systems/z — Claude Project Sync Loop/feature-catalog/output-format-gate/output-format-validator.md:44
- iteration 5 state_transition (ruled_out): counterevidence at mcp-tools.md:589 and :608 refutes the gaps-only premise; evidence=AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:565, AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:566, AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:589
- iteration 5 doc_count_drift (ruled_out): direct read of both expressions and their initialisers; evidence=AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:694, AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:776
- iteration 5 state_transition (not_applicable): requires running the format harness, outside a read-only review iteration; evidence=AI Systems/Product Owner/benchmark/format/fixtures/markasdone-divider-silent.md:1

<!-- /ANCHOR:search-debt -->
<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
- Dimension: none. All four dimensions are complete and this is the fifth and last configured iteration. - Focus area: release decision on the 2 open P1s and the 13 open P2s. - Reason: `stopPolicy` is `max-iterations`, so the loop ends here regardless of ratio. - Blocked carry-forward: `run_gates.sh` unlocated across five passes, `vendor.json` hash unrecomputed, the 14 playbook files unread, the silent fixture's silence not re-derived. - Productive carry-forward: reading a gate's own docstring as the oracle, which produced R3-P1-001 and again refuted the delivery-gate claim this pass. - Required evidence: nothing further is reachable inside this loop.

<!-- /ANCHOR:next-focus -->
<!-- ANCHOR:active-risks -->
## 12. ACTIVE RISKS
- 5 active P1 finding(s) — required before release; not a P0 but still blocks PASS.
- Claim-adjudication gate last failed at run 5 (missing packets: R2-P1-001, R3-P1-001). STOP is vetoed until every active P0/P1 has a typed claim-adjudication packet.
- 4 search-debt obligation(s) remain deferred or blocked. Verdict is CONDITIONAL until they are covered or ruled out.

<!-- /ANCHOR:active-risks -->
