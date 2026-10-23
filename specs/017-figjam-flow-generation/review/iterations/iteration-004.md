# Deep Review — Iteration 4

## Dimension

Maintainability: documentation accuracy and editing cost across the hub, Product Owner packet, Flow Mode, benchmark guides and Sync Loop references; self-test strength; route-contract drift guards; code-comment hygiene; and Human Voice punctuation.

## Files Reviewed

* `README.md`, `SKILL.md`, `AGENTS.md`, `SYNC.md`, `sk-product-owner/README.md`, `sk-product-owner/SKILL.md`, `sk-product-owner/ROUTER.md`, and the Flow Mode reference and templates
* `benchmark/gates/README.md`, `benchmark/gates/run_gates.sh`, `benchmark/gates/check_hub.py`, `benchmark/router/README.md`, `benchmark/router/differential.py`, `benchmark/router/differential_corpus.json`, and `benchmark/router/route_contract.py`
* `benchmark/format/validate-output-format.cjs`, `scripts/build-plugin.py`, `scripts/tests/test_vendor_sync.py`, and `sk-product-owner/scripts/flow_check.py`
* Outer Sync Loop `systems.cjs`, `validate-output-format.cjs`, `README.md`, and the output-format feature catalog, plus the Change Location flow model

## Findings by Severity

### P0

None new in this iteration

### P1

None new in this iteration

### P2

#### R4-P2-001 — Published benchmark totals disagree with the current checks

* Case: A maintainer uses the README benchmark summaries to decide how many checks and cases a complete run should report
* File: [SOURCE: README.md:679]
* Evidence: The gate runner declares ten entries and derives its total from that array [SOURCE: benchmark/gates/run_gates.sh:37] [SOURCE: benchmark/gates/run_gates.sh:49], while the root README and gate README say nine gates [SOURCE: README.md:679] [SOURCE: benchmark/gates/README.md:86]. The root README also says 35 format cases in its overview and 59 in the detailed table [SOURCE: README.md:27] [SOURCE: README.md:676]. The router README lists 94 synonyms while the current recorded output lists 114 [SOURCE: benchmark/router/README.md:103] [SOURCE: README.md:167]
* User impact: Maintainers cannot use the published totals as a reliable check that the expected corpus and gates ran
* Finding class: class-of-bug
* Scope proof: The runner has ten declared gate commands, its total is computed from `GATES`, the two root README counts disagree in the same file, and the router README count conflicts with the current differential output
* Affected surface hints: ["root README", "gate README", "router README", "benchmark gate runner"]
* Recommendation: Reconcile the published counts with the current runners and corpus, or generate those totals from the same source that prints the gate results

#### R4-P2-002 — Product Owner README contains a semicolon flagged by the voice gate

* Case: A reader follows the packet README as the user-facing guide to the Product Owner skill
* File: [SOURCE: sk-product-owner/README.md:231]
* Evidence: The local format validator reports a prose-semicolon advisory at this line; its source-file punctuation pass reports advice outside the strict instruction-file set [SOURCE: benchmark/format/validate-output-format.cjs:110] [SOURCE: benchmark/format/validate-output-format.cjs:1346]
* User impact: The guide contradicts the documented punctuation standard and leaves a known warning in routine source validation
* Finding class: instance-only
* Scope proof: The validator run identifies this exact line, while the Flow Mode reference and templates produced no punctuation warning
* Recommendation: Split the sentence at the semicolon and keep the packet guide aligned with the voice standard

## Traceability Checks

* The route-contract guard compares the reference pseudocode with the Claude Project kernel copy, the route tables with the executable Python contract, and behavior across the differential inputs; corpus coverage also requires command, false-prefix, topic and shape coverage [SOURCE: benchmark/router/differential.py:306] [SOURCE: benchmark/router/differential.py:467] [SOURCE: benchmark/router/differential.py:616]
* Static review found the self-tests use clean baselines and isolated planted defects with explicit expected exit codes. The vendor-sync tests create scratch upstream and product-owner repositories. Runtime self-tests were not executed in this pass
* The comment search found no spec paths, phase numbers or finding ids in code comments
* The local output-format validator passed across 44 source files. It emitted the packet README advisory recorded as R4-P2-002; the Flow Mode files had no semicolon or em-dash warning
* Core `spec_code` and `checklist_evidence`, and the traceability overlays, were not reassessed in this maintainability pass. Their iteration 3 statuses remain the latest traceability results
* No source or out-of-scope file was modified

## Next Dimension

Final iteration 5: check only for uncovered maintainability evidence and confirm the open findings and convergence state without reopening the swept review directions

## Verdict

No P0 or P1 finding was added. The two active P0 findings from earlier iterations remain open, so the run remains blocking under the verdict contract

Review verdict: FAIL
