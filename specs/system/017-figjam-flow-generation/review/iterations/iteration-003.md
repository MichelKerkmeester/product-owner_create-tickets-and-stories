# Deep Review — Iteration 3

## Dimension

Traceability: phase 003–006 specifications and checklist evidence, Flow intent parity across the skill and runtime routers, remapped playbook citations, and the outer Sync Loop feature catalog.

## Files Reviewed

* Phase goals, specifications, acceptance criteria, task lists, and implementation summaries for phases 003–006
* Parent FigJam goal decisions D1–D7 and the Change Location flow model
* `AGENTS.md`, hub `SKILL.md`, `mode-registry.json`, `hub-router.json`, Product Owner `SKILL.md`, `ROUTER.md`, and `router-contract.md`
* `benchmark/router/route_contract.py` and `claude project/Custom Instructions.md` Section 11
* The 23 modified manual-testing-playbook files with remapped citations
* Outer Sync Loop `systems.cjs`, `README.md`, and `feature-catalog/output-format-gate/output-format-validator.md`

## Findings by Severity

### P0

None new in this iteration

### P1

#### R3-P1-001 — Flow delivery reply conflicts with the global self-scan rule

* Case: A Flow request reaches its successful delivery step after the board has been written and read back
* File: [SOURCE: sk-product-owner/references/flow-mode.md:136]
* Evidence: Flow Mode restricts the reply to the board URL and read-back, then prohibits any file output [SOURCE: sk-product-owner/references/flow-mode.md:136] [SOURCE: sk-product-owner/references/flow-mode.md:138] [SOURCE: sk-product-owner/references/flow-mode.md:141]. The Flow exception in the export protocol replaces steps 4–7 only [SOURCE: AGENTS.md:39]. Step 8 still says to emit the HVR self-scan beside the path and read-back [SOURCE: AGENTS.md:50] [SOURCE: AGENTS.md:52], and the packet skill requires it in every delivery response [SOURCE: sk-product-owner/SKILL.md:100]
* User impact: The Flow reply cannot follow both instructions: adding the scan breaks the board-only reply, while omitting it breaks the general delivery rule
* Finding class: class-of-bug
* Scope proof: Direct comparison of the Flow reply contract, the root export exception and steps 8, and the packet skill’s export/HVR rules found no stated precedence or Flow scan exemption
* Recommendation: State whether Flow skips the global self-scan, or revise the Flow reply contract and both runtime instructions so the response shape is consistent

~~~json
{
  "findingId": "R3-P1-001",
  "claim": "A successful Flow delivery is specified to contain only the board URL and read-back, while the global HVR self-scan requirement remains active after the Flow exception for export steps 4–7.",
  "evidenceRefs": ["AGENTS.md:39", "AGENTS.md:50", "AGENTS.md:52", "sk-product-owner/SKILL.md:88", "sk-product-owner/SKILL.md:100", "sk-product-owner/references/flow-mode.md:136", "sk-product-owner/references/flow-mode.md:138", "sk-product-owner/references/flow-mode.md:141"],
  "counterevidenceSought": "The mode-specific reply says ‘and nothing else,’ and the root instruction exempts Flow from export steps 4–7. That does not name step 8 or reconcile the packet skill’s ‘every delivery response’ rule.",
  "alternativeExplanation": "Flow may be treated as a non-artifact delivery, making the global artifact scan inapplicable; the instructions currently call the board a deliverable and do not state that exemption.",
  "finalSeverity": "P1",
  "confidence": 0.91,
  "downgradeTrigger": "The authoritative instructions explicitly exempt Flow from the global scan, or revise the Flow reply shape to include it without contradicting the board-only contract."
}
~~~

### P2

None new in this iteration

## Traceability Checks

* Core `spec_code`: partial. Phases 003–004 map completed criteria to implementation evidence. Phases 005–006 remain open, with unchecked goal criteria, Unmet acceptance rows and placeholder summaries
* Core `checklist_evidence`: partial. Phase 003–004 tasks are specific and carry evidence; phase 005–006 task files remain generic scaffolds, and their acceptance evidence is not supplied
* Overlay `skill_agent`: fail. Flow routing is present, but the Flow reply contract conflicts with the global self-scan requirement in R3-P1-001
* Overlay `agent_cross_runtime`: partial. Static Flow aliases, natural-language framing, precedence and resource mapping agree across the router contract, Python route contract and Claude Project instructions; this pass did not execute the runtimes
* Overlay `feature_catalog_code`: pass. `systems.cjs` declares `SKILL.md` and `skill:ROUTER.md` as `extraSources`; the outer README and feature catalog both describe those sources as added to the perimeter
* Overlay `playbook_capability`: pass. The remapped citation targets checked against current source lines remain in bounds; no stale line target was found
* The Change Location model states 8 nodes, 8 connectors and two labelled exits; phase 005 still leaves live-board read-back unchecked because no hosted board evidence is recorded
* No source or out-of-scope file was modified

## Next Dimension

Maintainability. Revisit phase 005–006 checklist evidence when either phase is proposed as complete, and keep the hosted board criterion blocked until the Figma route can be exercised.

## Verdict

The new P1 reply-contract conflict is active. Two P0 findings from earlier iterations also remain active, so the run remains blocking.

Review verdict: FAIL
