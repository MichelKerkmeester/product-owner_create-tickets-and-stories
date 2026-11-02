# Deep Review Report — Product Owner Claude Project packaging

**Review target:** `specs/z-staging-po-019r` — the Product Owner claude.ai Project package.
**Lineage:** `specs/z-staging-po-019r/review/lineages/deepseek` (session `fanout-deepseek-1792598333413-h7kxu3`, generation 1, lineage mode `new`).
**Iterations:** 3 of 3. **Stop reason:** `maxIterationsReached` (stop policy `max-iterations`; convergence reported as telemetry only).
**Artifacts:** `iterations/iteration-001.md` … `iteration-003.md`, `deltas/iter-001.jsonl` … `iter-003.jsonl`, `deep-review-state.jsonl` (via the append gateway), `deep-review-findings-registry.json`.

---

## 1. Executive Summary

**Overall verdict: CONDITIONAL**

- `hasAdvisories`: false — the verdict is CONDITIONAL on active P1 findings, not on P2 advisories.
- Active findings: **P0 = 0, P1 = 6, P2 = 7** (13 total, all first seen in this lineage; 0 resolved, 0 repeats).
- Dimensions covered: correctness, traceability, maintainability. Security was in scope and produced no finding: the review looked for secret exposure, fabricated credentials and instruction injection from supplied sources, and the kernel already carries the injected-instruction rule (`Custom Instructions.md:111`).
- Convergence telemetry: final convergence score 0.74 (weighted new-severity ratio 1.00 → 0.34 → 0.26). Convergence did not stop the loop; the iteration cap did.

**Scope reviewed.** The kernel (`claude project/Custom Instructions.md`, 906 lines, H1 v1.2.2), all 62 knowledge files, `claude project/README.md`, `AI Systems/Product Owner/README.md`, `AI Systems/Product Owner/SYNC.md`, the skill sources in `sk-product-owner/` and `sk-create-figjam/`, the vendored `mcp-click-up/` and `mcp-figma/` packets, and `AI Systems/Media Editor/USER-GUIDE.md` as the setup-UX benchmark. Out of scope and never opened: `Product Owner/specs/`, `export/`, `benchmark/reports/`, `claude-plugin/`, `AI Systems/Product Context`, every screenshot and every figma.com URL.

**What is solid.** The 2026-10-21 kernel cut lost no rule. Every deleted sentence was tested against the current kernel plus all 62 knowledge files; the eight deduped rules each survive in one place, and the remaining deletions are reformulations whose rule is intact. The ClickUp parameter values (`markdown_description`, `include: ["description"]`, `content_format: "text/md"`, `visibility: "PRIVATE"`) match the vendored packet's captured schema.

**What blocks PASS.** Six P1 findings fall into three clusters: a kernel that contradicts its own Flow exception in its ALWAYS rules; a routing signal that exists in the knowledge mirror and the skill but not in the kernel's router; and a connector story that documents the wrong surface (CLI Code Mode install, CLI Figma daemon) while the Project's ClickUp document recipe omits required fields and its Figma tool names have no repository evidence.

## 2. Planning Trigger

`/speckit:plan` is **required**: the verdict is CONDITIONAL and six P1 findings need code and document changes before the package can ship.

```json
{
  "triggered": true,
  "verdict": "CONDITIONAL",
  "hasAdvisories": false,
  "activeFindings": [
    {"id": "R1-P1-001", "severity": "P1", "title": "Kernel ALWAYS 1 and ALWAYS 6 lack the Flow exception the same block grants", "file": "AI Systems/Product Owner/claude project/Custom Instructions.md:82", "findingClass": "cross_file_contradiction", "affectedSurface": "kernel rule block"},
    {"id": "R1-P1-002", "severity": "P1", "title": "Just do it selects Quick energy in the mirror and skill but not in the kernel router", "file": "AI Systems/Product Owner/claude project/Custom Instructions.md:511", "findingClass": "routing_drift", "affectedSurface": "kernel router code and Section 4 table"},
    {"id": "R2-P1-001", "severity": "P1", "title": "Only the CLI Code Mode install is documented for ClickUp and Figma", "file": "AI Systems/Product Owner/README.md:173", "findingClass": "missing_surface_instructions", "affectedSurface": "product README and Project upload guide"},
    {"id": "R2-P1-002", "severity": "P1", "title": "The Figma connector has no setup, enablement or surface statement", "file": "AI Systems/Product Owner/claude project/Custom Instructions.md:255", "findingClass": "missing_surface_instructions", "affectedSurface": "Project upload guide and kernel Flow delivery"},
    {"id": "R3-P1-001", "severity": "P1", "title": "Private-doc recipe omits name and parent plus the container-resolution rule", "file": "AI Systems/Product Owner/claude project/Custom Instructions.md:299", "findingClass": "missing_required_parameter", "affectedSurface": "kernel ClickUp delivery and Project upload guide"},
    {"id": "R3-P1-002", "severity": "P1", "title": "Flow knowledge asserts a Figma connector tool set no repository document evidences", "file": "AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:311", "findingClass": "unverified_capability_claim", "affectedSurface": "Flow Mode knowledge mirror"}
  ],
  "remediationWorkstreams": [
    {"id": "WS-1", "severity": "P1", "scope": "Kernel rule consistency", "findings": ["R1-P1-001", "R1-P1-002", "R1-P2-003"], "files": ["AI Systems/Product Owner/claude project/Custom Instructions.md"], "outcome": "one Flow exception that reaches every rule stating the deliverable obligation, one energy detector that matches the knowledge mirror, and ask-first lists that name Flow"},
    {"id": "WS-2", "severity": "P1", "scope": "Project-surface connector setup and verification", "findings": ["R2-P1-001", "R2-P1-002", "R2-P2-001", "R2-P2-002"], "files": ["AI Systems/Product Owner/README.md", "AI Systems/Product Owner/claude project/README.md"], "outcome": "a setup path per connector for the Project surface, one probe per connector with expected output, and troubleshooting rows"},
    {"id": "WS-3", "severity": "P1", "scope": "Transport recipes", "findings": ["R3-P1-001", "R3-P1-002", "R3-P2-001", "R3-P2-002"], "files": ["AI Systems/Product Owner/claude project/Custom Instructions.md", "AI Systems/Product Owner/claude project/README.md", "AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md", "AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Hybrid Workflow.md"], "outcome": "a complete ClickUp document recipe, a Figma capability statement the connector reports rather than assumes, and an evidence-surface sentence for each transport"},
    {"id": "WS-4", "severity": "P2", "scope": "Documentation hygiene", "findings": ["R1-P2-001", "R1-P2-002"], "files": ["AI Systems/Product Owner/claude project/knowledge/Product Owner - Rules - Flow Quality Rubric.md", "AI Systems/Product Owner/README.md"], "outcome": "Knowledge titles instead of skill paths, and one example count and route list per README"}
  ],
  "specSeed": [
    "Decide the Project surface contract for the ClickUp and Figma connectors: which surface hosts each, where it is enabled, and which capability statement the kernel may assert.",
    "Decide whether the kernel's ALWAYS list is a summary with named exceptions or an exhaustive rule set, then make rules 1 and 6 match rules 5-8.",
    "Decide whether just-do-it is a Quick-energy signal; if yes, the router code is the place to carry it.",
    "Record the claude.ai connector schema evidence date next to the parameter table, and state which surface each capture covers."
  ],
  "planSeed": [
    "Edit kernel ALWAYS 1 and 6 to carry the Flow exception; bump the kernel H1 and record the change in SYNC.md.",
    "Add just-do-it to the Section 4 Quick row and to the natural_quick regex; add a router fixture for it.",
    "Replace or retitle README section 'Connect ClickUp and Figma (optional)' with a Project-surface setup path, keeping the CLI Code Mode install in an operator appendix.",
    "Add a Figma connector section to claude project/README.md beside the ClickUp section, with the no-connector fallback stated in the same place.",
    "Add one probe per connector to the smoke matrix, each with expected output and a failure interpretation.",
    "Complete the private-doc recipe with name, parent, parent.type resolution and create_page.",
    "Rewrite the Flow knowledge tool naming so the tool set is reported by the connector, with the no-tool path beside it.",
    "Fix the Flow Quality Rubric loading line and the README count and route summary."
  ],
  "findingClasses": ["cross_file_contradiction", "routing_drift", "missing_surface_instructions", "missing_required_parameter", "unverified_capability_claim", "parity_residue", "stale_counts", "incomplete_enumeration", "missing_validation", "documentation_gap", "provenance_doubt"],
  "affectedSurfacesSeed": ["kernel rule block", "kernel router code", "kernel ClickUp delivery", "kernel Flow delivery", "Project Knowledge Flow mirrors", "product README setup path", "Project upload guide", "smoke matrix", "troubleshooting section"],
  "fixCompletenessRequired": true
}
```

## 3. Active Finding Registry

### P0 — 0 active

None.

### P1 — 6 active

| ID | Title | Dimension | File:line | What a fix changes |
| --- | --- | --- | --- | --- |
| R1-P1-001 | Kernel ALWAYS 1 and ALWAYS 6 state the Deliverable-Block and ClickUp-offer rules without the Flow exception the same block grants | correctness | `AI Systems/Product Owner/claude project/Custom Instructions.md:82` | `Custom Instructions.md` rules 1 and 6 |
| R1-P1-002 | Just do it selects Quick energy in the knowledge mirror and the skill but not in the kernel's router code or its Quick row | traceability | `AI Systems/Product Owner/claude project/Custom Instructions.md:511` | `Custom Instructions.md:131` and the `natural_quick` regex |
| R2-P1-001 | The only "Connect ClickUp and Figma" instructions are the CLI Code Mode install, so a Project user never learns to add or enable either connector | traceability | `AI Systems/Product Owner/README.md:173` | `README.md` and `claude project/README.md` |
| R2-P1-002 | The Figma connector has no setup, enablement or no-connector statement for a Project user, although Flow Mode Delivery is built on it | traceability | `AI Systems/Product Owner/claude project/Custom Instructions.md:255` | `claude project/README.md` (a Figma section) and `README.md` (surface statement) |
| R3-P1-001 | The private-doc recipe omits `name` and `parent` plus the container-resolution rule the source skill carries | correctness | `AI Systems/Product Owner/claude project/Custom Instructions.md:299` | `Custom Instructions.md:299` and `claude project/README.md:125` |
| R3-P1-002 | The Flow knowledge asserts a Figma connector tool set no repository document evidences for that surface | traceability | `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:311` | that file and a `SYNC.md` decision sentence |

Adjudication summary: every P1 was re-read at its cited line before recording, and each carries the claim, evidence, counterevidence, alternative explanation, confidence and downgrade trigger in its iteration file. No P1 was upgraded from a P2 without a second read.

### P2 — 7 active (advisories)

| ID | Title | Dimension | File:line |
| --- | --- | --- | --- |
| R1-P2-001 | Flow Quality Rubric mirror tells the reader to load a skill path that does not exist in the Project | maintainability | `.../knowledge/Product Owner - Rules - Flow Quality Rubric.md:11` |
| R1-P2-002 | Package README contradicts itself on the example count and omits Flow from the route summary | traceability | `AI Systems/Product Owner/README.md:24` |
| R1-P2-003 | Kernel ask-first rules enumerate every command except `$flow` and `$figjam` | correctness | `AI Systems/Product Owner/claude project/Custom Instructions.md:115` |
| R2-P2-001 | Neither connector has a check-that-it-works step with an expected result | traceability | `AI Systems/Product Owner/claude project/README.md:166` |
| R2-P2-002 | No troubleshooting entry covers a missing or disabled connector, and the one ClickUp symptom is written for the CLI | maintainability | `AI Systems/Product Owner/README.md:882` |
| R3-P2-001 | ClickUp parameters are evidenced for the Code Mode manual, which the packet says was not the claude.ai connector | traceability | `AI Systems/Product Owner/mcp-click-up/SKILL.md:26` |
| R3-P2-002 | The Flow tag step assumes the connector exposes a Figma Plugin API method | traceability | `.../knowledge/Product Owner - Templates - Flow Mode.md:320` |

## 4. Remediation Workstreams

### WS-1 — Kernel rule consistency (P1: R1-P1-001, R1-P1-002; P2: R1-P2-003)

1. Give ALWAYS 1 and ALWAYS 6 the same "except Flow Mode" qualifier ALWAYS 5 and strict steps 6-8 already carry, so the two obligations and their exception live in one voice.
2. Add `just do it` to the Section 4 Quick row and to the `natural_quick` regex, then add a router fixture so the signal cannot drift again quietly.
3. Name Flow's own intake in the two ask-first enumerations (lines 9 and 115) instead of leaving it out.

### WS-2 — Project-surface connector setup and verification (P1: R2-P1-001, R2-P1-002; P2: R2-P2-001, R2-P2-002)

1. Retitle or split the product README's "Connect ClickUp and Figma (optional)" section: a Project-surface path for a Claude Desktop or claude.ai user, and the existing Code Mode install kept as an operator appendix with its Node 24 constraint.
2. Add a Figma connector section to `claude project/README.md`, beside the ClickUp section, that names the no-connector fallback in the same place.
3. Add one probe per connector to the smoke matrix, each with the expected output and what a failure means.
4. Add troubleshooting rows: connector absent from the chat menu, connector present but off, board read-back not possible, and the Project's own `Export-equivalent path:` wording.

### WS-3 — Transport recipes (P1: R3-P1-001, R3-P1-002; P2: R3-P2-001, R3-P2-002)

1. Complete the private-doc recipe with `name`, `parent` (`{id, type}`), `visibility`, `create_page: false`, and the container-resolution rule from `sk-product-owner/SKILL.md:307-308`, including what happens when the user accepts the private doc with no link.
2. Rewrite the Flow knowledge tool naming as what the connector reports, with the no-tool path beside it, and carry the source's own caution that the native prefix is unconfirmed.
3. Record the evidence surface and capture date for the ClickUp parameters next to the table, and keep the kernel's conditional wording.
4. Put the `setSharedPluginData` tag step under the same conditional, with the skip path written beside it.

### WS-4 — Documentation hygiene (P2: R1-P2-001, R1-P2-002)

1. Replace the `references/types/` loading line with the matching Knowledge title.
2. Make `README.md` state one example count (28) and one route list (six routes including Flow).

## 5. Spec Seed

- Define the Project surface contract: for each connector, the surface that hosts it, where a user enables it, the capability the kernel may assert, and the fallback when it is absent.
- Define whether the ALWAYS list is exhaustive or summary-shaped with named exceptions; then hold every rule to that decision.
- Decide the Quick-energy signal vocabulary in one place (the router code) and have the knowledge mirror point at it rather than restate it.
- Require an evidence-surface date for every transport parameter table, distinguishing the hosted server, the Code Mode manual and the claude.ai connector.

## 6. Plan Seed

1. Kernel edits (ALWAYS 1/6, Quick row + regex, ask-first lists), H1 bump, `SYNC.md` entry.
2. Product README restructure (setup path, operator appendix, troubleshooting rows).
3. Project README additions (Figma connector section, probes, complete private-doc recipe, evidence-surface sentence).
4. Flow knowledge corrections (tool naming, tag step, rubric loading line).
5. A router fixture for just-do-it and a smoke-matrix addition for each connector; rerun `bash benchmark/router/run_fixtures.sh` and `bash benchmark/format/run_fixtures.sh`.
6. Operator review of kernel v1.2.2+ per the parity note, recorded as a dated sentence.

## 7. Traceability Status

### Core Protocols

| Protocol | Status | Evidence | Unresolved drift |
| --- | --- | --- | --- |
| `spec_code` | partial | The spec's four focus questions are each answered across iterations 1-3, with one line per parameter in `iterations/iteration-003.md`. | Focus 3 (setup UX) is answered negatively; the fix needs an operator statement the repository cannot supply. |
| `checklist_evidence` | notApplicable | `specs/z-staging-po-019r/` has no `checklist.md`; it is a review scope, not a lifecycle folder. | None. |

### Overlay Protocols

| Protocol | Status | Evidence | Notes |
| --- | --- | --- | --- |
| `skill_agent` | fail | `sk-product-owner/SKILL.md:307-308` carries fields and a rule the Project mirror dropped (R3-P1-001); `sk-product-owner/references/interactive-mode.md:74` disagrees with the kernel router (R1-P1-002). | Two distinct sources, one cluster. |
| `agent_cross_runtime` | notApplicable | No agent definition is part of the reviewed package. | — |
| `feature_catalog_code` | partial | The ClickUp feature catalog backs the tool names and fields for the hosted server; it covers no claude.ai connector surface and no Figma connector. | R3-P2-001, R3-P1-002. |
| `playbook_capability` | deferred | The playbooks under `sk-create-figjam/manual-testing-playbook/` exercise the CLI `fj` route; the Product Owner playbook grades the CLI packaging. | A Project-surface playbook is the missing instrument, not a missing check. |

**AC_COVERAGE:** not applicable. The target is a review-scope staging folder with no `implementation-summary.md` and no `checklist.md`, so the lifecycle predicate is inactive.

## 8. Deferred Items

- **Project-surface playbook.** A playbook scenario that sets up a connector, runs a probe and grades the outcome would have caught R2-P1-001/002 and R2-P2-001 without a manual reading.
- **Connector schema capture.** A dated capture of the claude.ai ClickUp and Figma connector tool lists would turn R3-P1-002, R3-P2-001 and R3-P2-002 from doubts into facts or retractions.
- **Kernel rule-shape decision.** Whether the ALWAYS list is exhaustive is a design decision (WS-1) rather than a bug fix; it is deferred to the spec seed.
- **The `Product Owner - Examples - Doc - README.md` link change.** The 2026-10-21 edit replaced markdown links with code spans in that example; the source example still links. It is not a rule loss and not a finding, but a maintainer may want the example to keep link syntax as its shape demonstration.
- **Shared card filesystem wording.** `[SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Rules - Conciseness.md:145]` mentions "read-back confirmation where the runtime can write files". The parity note declares the four shared cards byte copies, so this is declared state, not drift; changing it means changing the shared card for every system.

## Dimension Expansion Map

- Completed pivots: 0. Failed pivots: 0. Audited overrides: 0.
- Swept directions: kernel rule-loss audit (iteration 1, ruled out); benchmark surface-conflation (iteration 2, ruled out); ClickUp parameter values (iteration 3, ruled out).
- Selected review directions and their frontier: correctness (kernel self-consistency — exhausted for this text), traceability (setup surface and transport provenance — frontier is the connector schema), maintainability (parity residue — one file left). Security was swept with no finding.
- Remaining frontier: live connector capability, which a repository review cannot enter.

## 9. Search Ledger

- `searchCoverage`: required classes `rule_loss_on_dedupe`, `cross_file_contradiction`, `routing_drift`, `parity_residue`, `stale_counts`, `incomplete_enumeration`, `missing_surface_instructions`, `missing_validation`, `documentation_gap`, `missing_required_parameter`, `unverified_capability_claim`, `provenance_doubt`, `surface_conflation` — all covered or ruled out; none deferred, none blocked.
- `candidateCoverage`: 13 active findings from 16 ledger rows; 3 candidates ruled out (6 rows recorded `ruled_out` with their reasons in the iteration files: dedupe rule loss, Media Editor surface conflation, ClickUp parameter names).
- `searchDebt`: none (`hasSearchDebt: false`).
- `ruledOutCandidates`: the 2026-10-21 kernel cut lost no rule; the benchmark's advise-only row does not transfer to remote connectors; `markdown_description` / `include` / `visibility: PRIVATE` / `content_format: "text/md"` match the captured server schema; `mcp-figma/` documents a CLI, not a connector.
- `cleanSearchProof`: each iteration records its ledger rows with method, path and evidence refs; three iterations ran to the cap with no blocked class.

## 10. Audit Appendix

**Convergence summary.** Iteration 1: 2 P1 + 3 P2, ratio 1.00. Iteration 2: 2 P1 + 2 P2, ratio 0.34. Iteration 3: 2 P1 + 2 P2, ratio 0.26. Final convergence score 0.74; graph convergence 0 (coverage-graph seeding was skipped by scope, see below). Stop reason `maxIterationsReached`, not convergence.

**Coverage summary.** 62 knowledge files were scanned for skill-only mechanics and cross-file contradiction; the four shared cards were exempted by the declared byte-copy rule; the kernel was read end to end plus its HEAD diff. Files reviewed per iteration are listed in each iteration file and in the state log.

**Sources reviewed.** `Custom Instructions.md`, `claude project/README.md`, `claude project/knowledge/` (62 files), `AI Systems/Product Owner/README.md`, `SYNC.md`, `sk-product-owner/SKILL.md`, `sk-product-owner/references/interactive-mode.md`, `sk-create-figjam/references/flow-mode.md`, `sk-create-figjam/references/quality-rubric.md`, `sk-create-figjam/references/types/user-flow.md`, `mcp-click-up/SKILL.md`, `mcp-click-up/INSTALL-GUIDE.md`, `mcp-click-up/feature-catalog/*`, `mcp-click-up/references/mcp-tools.md`, `mcp-figma/SKILL.md`, `AI Systems/Media Editor/USER-GUIDE.md`, `specs/z-staging-po-019r/spec.md`, `steer.md`.

**Cross-reference appendix.**

*Core protocols:* `spec_code` partial; `checklist_evidence` notApplicable.

*Overlay protocols:* `skill_agent` fail (R3-P1-001, R1-P1-002); `agent_cross_runtime` notApplicable; `feature_catalog_code` partial (R3-P2-001, R3-P1-002); `playbook_capability` deferred.

**Resource Map Coverage Gate:** skipped. `specs/z-staging-po-019r/resource-map.md` was absent at init, so `resource_map_present` is false; the reducer emitted `resource-map.md` in the lineage directory as a derived artifact only.

**Scope notes.** `step_seed_coverage_graph` was not run because `upsert.cjs` writes the shared coverage graph outside this lineage's artifact directory; the iteration records therefore omit `graphEvents` and the graph rollup is zero. The one gateway call that landed outside the lineage (repository-root ledger directories from a mistyped run directory) was removed and is disclosed in `iterations/iteration-001.md` under SCOPE VIOLATIONS.

**Open questions the repository cannot settle.**

1. Which surfaces expose the claude.ai ClickUp and Figma connectors and where a user adds them.
2. What tool names and schemas the claude.ai ClickUp connector exposes, including whether it accepts a document create without `parent`.
3. What the claude.ai Figma connector exposes, given that the only source marks `generate_diagram` remote-only and says no source confirms the native prefix.
4. Whether a Project runtime resolves ALWAYS 1 against Flow Mode in practice.

**Question for the operator before release.** The six P1 findings are all document-and-rule edits inside the reviewed package except R3-P1-002's evidence gap, which needs a connector schema capture. The package can reach PASS on edits alone if the Flow tool naming is rewritten as connector-reported rather than asserted.
