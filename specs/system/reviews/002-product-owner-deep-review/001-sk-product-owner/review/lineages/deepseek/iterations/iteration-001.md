# Review Iteration 001 — Correctness

- Session: `fanout-deepseek-1792580414886-kf3maf` (generation 1, lineageMode new)
- Iteration: 1 of 5
- Dimension: correctness
- Stop policy: `max-iterations` (convergence is telemetry only)
- Review target: `AI Systems/Product Owner/sk-product-owner`
- Review scope per `specs/product-owner/018-product-owner-deep-review/001-sk-product-owner/spec.md` Files to Change and `steer.md`

## Files Reviewed

- `AI Systems/Product Owner/sk-product-owner/SKILL.md:1-321` — bootstrap, routing table, five-phase flow, energy levels, export and read-back rule, 17 ALWAYS rules, 16 NEVER rules, success criteria.
- `AI Systems/Product Owner/sk-product-owner/references/routing.md:1-81` — routing steps, confidence thresholds, semantic topic table, Story shape resolution.
- `AI Systems/Product Owner/sk-product-owner/references/quality-scoring.md:46-190` — six dimensions, bands, floors, pre-reply checklist, revision ladder.
- `AI Systems/Product Owner/sk-product-owner/references/conciseness.md:116-161` — format rule, deliverable prohibition enumeration, the two narrow overrides.
- `AI Systems/Product Owner/sk-product-owner/references/story-mode.md:184-232` — create workflow and refinement workflow.
- `AI Systems/Product Owner/sk-product-owner/references/doc-mode.md` headings — Section 4 source authority, Section 6 refinement, Section 1 output contract presence.
- `AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md` headings — Section 3 Delivery Reply Shape.
- `AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/manual-testing-playbook.md:9-108` — scenario count and turn arithmetic.
- `AI Systems/Product Owner/sk-product-owner/README.md:415` — packaging and shared-card provenance statement.

## Findings by Severity

### P0 Findings

None. No correctness failure was confirmed that breaks every delivery path.

### P1 Findings

1. **The skill's own quality rubric carries Project-only delivery rules that contradict the skill export contract** -- `AI Systems/Product Owner/sk-product-owner/references/quality-scoring.md:160` -- The file is an ON_DEMAND reference that the skill loads for a borderline quality dimension, and inside its pre-reply checklist it requires "The Deliverable Block appears before commentary and is the only claimed delivery evidence" (:160) and "Response follows the Delivery Reply Shape: the correct export-equivalent path" (:161), then repeats the requirement as prohibition :187 ("Never skip the Deliverable Block, template compliance or quality scoring. Never claim a deliverable exists without rendering it."). `SKILL.md:127` requires the opposite delivery proof for this packet: Read the exact export path, require non-empty content, "A path string, planned write, or Write result alone does not pass verification", and print the `Path:` line. `SKILL.md:170` (ALWAYS 12) names Flow Mode as "the one exception", and `references/conciseness.md:143` scopes export-equivalent reporting to packaging "where the packaging renders the deliverable in a panel instead of saving a file". A Doc, Task, Bug, Story or Epic route that consults this rubric is therefore told that rendering a block is the delivery and that an export-equivalent path is correct — the exact false-delivery state `SKILL.md:127` exists to block. The same block also imports Project-era vocabulary at :143 ("Project Knowledge consultation matches the routed path"), which no skill route performs. The prose is Project-kernel text (`claude project/Custom Instructions.md:2` defines the Deliverable Block and the export-equivalent path as that kernel's only delivery proof) that was written back into the skill source instead of the skill text being the source.

```
Finding class: contract-contradiction
Scope proof: All three cited positions are inside the declared target `AI Systems/Product Owner/sk-product-owner`; the kernel file was opened read-only as provenance evidence only.
Affected surface hints: references/quality-scoring.md (fix target), SKILL.md:127 and ALWAYS 12 (governing rule), claude project/knowledge (downstream mirror to re-check after the fix)
Case: A Doc request where the operator asks for a runbook; the model loads quality-scoring.md for the Accuracy dimension, reads that the Deliverable Block is the only claimed delivery evidence, renders the artifact in chat and reports an export-equivalent path, so nothing is written under export/ and the read-back proof never runs.
```

```json
{
  "type": "claim-adjudication",
  "claim": "quality-scoring.md instructs Project-side delivery proof (Deliverable Block, export-equivalent path) as the skill's own quality gate, contradicting SKILL.md:127 and ALWAYS 12.",
  "evidenceRefs": [
    "AI Systems/Product Owner/sk-product-owner/references/quality-scoring.md:160",
    "AI Systems/Product Owner/sk-product-owner/references/quality-scoring.md:161",
    "AI Systems/Product Owner/sk-product-owner/references/quality-scoring.md:187",
    "AI Systems/Product Owner/sk-product-owner/SKILL.md:127",
    "AI Systems/Product Owner/sk-product-owner/SKILL.md:170",
    "AI Systems/Product Owner/sk-product-owner/references/conciseness.md:143"
  ],
  "counterevidenceSought": "Checked whether quality-scoring.md scopes these lines to the Project runtime, whether SKILL.md permits a panel-rendered delivery anywhere except Flow, and whether conciseness.md section 8.4 widens the exception. Found no runtime scoping in the checklist, no skill-side panel render, and an exception in 8.4 limited to packaging that cannot save a file.",
  "alternativeExplanation": "The block may be intentional legacy text retained for the parity gate, and a reader may treat it as advisory because the checklist heading says 'pre-reply quality checklist'. Rejected as the whole explanation: the file is routed as the quality authority for borderline scores, and :187 restates it as a numbered prohibition with no runtime qualifier, so the governing reading contradicts the export rule rather than merely duplicating Project text.",
  "finalSeverity": "P1",
  "confidence": "high",
  "downgradeTrigger": "Downgrade to P2 if the file gains an explicit runtime qualifier that marks every imported Project-only check as inapplicable in the skill runtime, or if SKILL.md ALWAYS 12 is amended to accept a rendered block as delivery."
}
```

### P2 Findings

1. **The bootstrap describes the four shared cards as living in a directory that does not exist in the packet** -- `AI Systems/Product Owner/sk-product-owner/SKILL.md:67` -- The ALWAYS resource-loading prose says resources are discovered "from `references/` (the mode workflows and four byte copies of shared cards in `z — Knowledge/`) and `assets/`". No `z — Knowledge/` directory exists inside the packet or inside `AI Systems/Product Owner/`; the repository's only such directory is `AI Systems/z — Knowledge/`, which is outside this packet and is not part of the recursive discovery roots the sentence names. The four cards are present in place as regular files (`references/hvr-core.md`, `references/conciseness.md`, `references/conciseness-rationale.md`, `references/human-voice-rules.md`), and `README.md:415` states the provenance correctly ("regular-file copies of cards in `z — Knowledge/`"). The parenthetical reads as a discovery root, so a resolver who follows it looks for a directory under `references/` and finds none.

```
Finding class: doc-path-claim
Scope proof: SKILL.md and README.md are both inside the declared target; the filesystem check covered the packet and its parent only.
Affected surface hints: SKILL.md:67 (fix target), README.md:415 (correct wording to copy)
Case: A maintainer regenerates the packet's resource inventory from the Section 2 prose and drops the four shared cards because the directory named in the ALWAYS row does not exist under references/.
```

2. **The related-resource line understates the manual-testing playbook by two scenarios** -- `AI Systems/Product Owner/sk-product-owner/SKILL.md:319` -- SKILL.md calls the playbook "The 48 artifact scenarios". `manual-testing-playbook/manual-testing-playbook.md:22` states "The playbook covers 50 scenarios in two mirrored sets of 25", and the package contains 50 scenario files (10 backlog, 4 document, 7 story per set, plus flow, identity and two interactive per set, in both the `project-*` and `skill-*` trees). A reader who plans a run from the bootstrap expects a smaller package than the one on disk.

```
Finding class: stale-count
Scope proof: Counted only files under the declared target's manual-testing-playbook/ tree; the hub's own statement is cited at :22.
Affected surface hints: SKILL.md:319 (fix target), manual-testing-playbook/manual-testing-playbook.md:22 (authority for the count)
Case: A reviewer schedules a 48-scenario regression pass from SKILL.md's description, then discovers two scenarios were never run when the playbook index reports 50.
```

## Traceability Checks

| Protocol | Level | Status | Evidence |
|----------|-------|--------|----------|
| `spec_code` | core | partial | `specs/product-owner/018-product-owner-deep-review/001-sk-product-owner/spec.md:13` declares `AI Systems/Product Owner/sk-product-owner/` in scope; the three findings land inside that path. The staging spec carries no acceptance criteria to trace against, so the protocol is scored on scope fidelity only. |
| `checklist_evidence` | core | partial | The packet's own gates are `SKILL.md:240-275` (Routing Checks, Quality Floors, Blocking Gates) and `references/quality-scoring.md` Section 6; finding P1-1 sits between those two authorities. |
| `skill_agent` | overlay | partial | `SKILL.md` names itself as the executable identity at `SKILL.md:232` and the packet at `SKILL.md:229-234`; the agent entry points that load it were not compared in this iteration (deferred to iteration 2). |
| `agent_cross_runtime` | overlay | notApplicable | The packet declares no runtime mirror of its own; `SKILL.md:310` and `README.md:415` place the Claude Project packaging under `../claude project/`, which is a separate hand-written surface outside this target's files. |
| `feature_catalog_code` | overlay | notApplicable | No feature catalog exists in this packet. |
| `playbook_capability` | overlay | partial | The playbook count claim was checked against the playbook itself (P2-2); per-scenario capability coverage was not audited in this iteration and is scheduled for iteration 5. |

## Integration Evidence

- Hub routing: `SKILL.md:44` states the hub [`../SKILL.md`](../SKILL.md) selects this packet and [`../ROUTER.md`](../ROUTER.md) maps intents to leaves; both `AI Systems/Product Owner/SKILL.md` and `AI Systems/Product Owner/ROUTER.md` exist.
- Flow handoff: `SKILL.md:57` and `SKILL.md:72` route `$flow`/`$figjam` to `../sk-create-figjam/`; the arrow resolves to an existing packet directory and `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` exists.
- ClickUp transport: `SKILL.md:283-291` defers mechanics to `../mcp-click-up/`; `AI Systems/Product Owner/mcp-click-up/SKILL.md` exists.

## Edge Cases

- **Ambiguous path base.** `SKILL.md:77` and `references/routing.md:81` cite `benchmark/router/route_contract.py`, which exists at `AI Systems/Product Owner/benchmark/router/route_contract.py` but not under the packet. The citation is resolvable from the system root and is therefore not recorded as a broken path here; it is queued for the references-and-paths iteration, which will settle whether the packet's docs should use a root-relative or `../../` form.
- **Numbered list starting off-list.** `references/quality-scoring.md:183-187` opens a delivery-prohibition list at item 7 with no items 1-6 anywhere in the file. It is the same imported-kernel block as P1-1 and is carried into iteration 4 (maintainability) rather than double-counted here.
- **Section numbering gaps.** `references/conciseness.md` jumps 5 → 7 → 8 → 12. The internally cited sections (8, 8.4) do exist, so no reference dangles; recorded as a cosmetic observation, not a finding.

## Confirmed-Clean Surfaces

- Confidence thresholds agree between `SKILL.md:62` and `references/routing.md:31-34` (LOW at 0.40, FALLBACK below 0.40, documentation and story override at 0.85).
- Every reference and asset named in the CONDITIONAL row at `SKILL.md:72` exists: five mode references, six assets, and the Story/Epic pair loaded one-at-a-time.
- Quality floors agree between `SKILL.md:250-259` and `references/quality-scoring.md:46-90` (five at 8, Accuracy at 9).
- The three-cycle ceiling agrees between `SKILL.md:275` and `references/quality-scoring.md` Section 6.
- The refinement rules agree between `SKILL.md:143-147`, `references/doc-mode.md` Section 6 and `references/story-mode.md:218-231`.
- Cross-section citations into `assets/interactive-response-templates.md` Section 3 and `references/conciseness.md` Section 8.4 both resolve to real headings.

## Ruled Out

- **Rule 10 versus rule 17 bullet punctuation.** Read as a contradiction at first pass; `references/conciseness.md:116-121` separates authoring punctuation from format selection and `SKILL.md:175` exempts code, tables and supplied copy, so the two rules do not collide. Ruled out.
- **Story/Epic "conflict" under the 2+ command rule.** `SKILL.md:59` sends 2+ commands to Interactive Mode while `references/routing.md:1-3` says Story and Epic never conflict. The routing detail carves the case out explicitly and SKILL.md routes the lane to that detail at `SKILL.md:77`, so this is a compression rather than a contradiction. Ruled out.
- **`$quick` bypassing a Doc gate.** `SKILL.md:151` and `references/doc-mode.md:363-376` both refuse the bypass. Ruled out.

## Next Focus

- Dimension: traceability
- Focus area: references and paths — resolve every markdown link target and every named file across `SKILL.md`, `references/` and `assets/`; settle the `benchmark/router/` path base and the `../SKILL.md`/`../ROUTER.md` hub citations
- Reason: iteration 1 confirmed three consistency defects and left path resolution and contract consistency unevaluated; the packet cites dozens of sibling paths and one base-ambiguous directory
- Rotation status: correctness covered at iteration 1; security, traceability and maintainability remain
- Required evidence: `[SOURCE: path:line]` for each resolved or unresolved target
- Recovery note: none

Review verdict: CONDITIONAL
