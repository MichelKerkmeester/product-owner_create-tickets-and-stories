# Review Report — Product Owner `sk-create-figjam`

Run: `fanout-deepseek-1792580434639-g9yydk` · lineage `deepseek` · mode `review` · executor `cli-pi` / `deepseek-v4.1-flash`
Target: `AI Systems/Product Owner/sk-create-figjam/` (read-only, review target type `skill`)
Artifact dir: `specs/product-owner/018-product-owner-deep-review/002-sk-create-figjam/review/lineages/deepseek`
Stop policy: `max-iterations`, cap 5, reached. Convergence score is telemetry only in this run (mode `off`).

---

## Executive Summary

Five iterations covered all four review dimensions: correctness of the Python checks (1), the security trust boundary (2), traceability of routing, cross-references and the vendored copy (3), maintainability and next-change cost (4), and a consolidation pass that replayed the active findings (5).

Eleven findings are active: **zero P0, one P1, ten P2**. Nothing was found that corrupts a written board, executes untrusted model text, leaks a secret, or writes outside a temp directory. The single P1 is a gate gap: `scripts/flow_check.py` never applies the twelve-connector budget that `references/flow-mode.md:298` states for every diagram type, because the user-flow entry in the budget table carries `None` for connectors. Iteration 5 proved it by running the check on a nine-node, thirteen-connector user flow, which passed with exit 0.

The packet is in good shape otherwise. Every one of the 81 local links resolves, all 52 playbook scenarios are indexed, all seven examples and six templates pass the check, each example's quoted read-back matches live output, the style guide's palette record and its ten contrast ratios measure true, the vendored extractor is byte-identical to the digest its manifest records, and an unsupported model header produces the exit code the README promises.

**Verdict: CONDITIONAL** — recomputed from the findings registry, not from any iteration's self-reported line.

---

## Planning Trigger

Planning is needed for one workstream only: the user-flow connector budget. The ten P2 findings are advisories that can be batched into a documentation and hygiene pass, or deferred with the reasons recorded in the registry. No `/speckit:plan` is required to ship the packet as it stands for the six types whose budgets match; it is required before claiming the check enforces the shared budget for a user flow.

---

## Active Finding Registry

### P0 — none

### P1 — one

| Id | Finding | Evidence | Fix file |
|----|---------|----------|----------|
| `R1-P1-001` | A user flow is never held to the 12-connector budget the shared rule states | `scripts/figjam_checks/flowchart.py:47` (`USER_FLOW: (9, None)`), `:236` (`if max_edges is not None`), `references/flow-mode.md:298`, `references/types/user-flow.md:66`; confirmed by a passing 13-connector run in iteration 5 | `scripts/figjam_checks/flowchart.py` (or `references/types/user-flow.md:66` if the intent is that the user flow sets its own cap) |

### P2 — ten

| Id | Dimension | Finding | Evidence |
|----|-----------|---------|----------|
| `R1-P2-001` | correctness | The first declared node is excused from the way-in rule whatever its shape | `scripts/figjam_checks/flowchart.py:155`, `:233` |
| `R1-P2-002` | correctness | An arrow table in the sequence check is defined and never read | `scripts/figjam_checks/sequence.py:24` against `:83` |
| `R1-P2-003` | correctness | The state check accepts `TD` while its message and type reference allow `LR` or `TB` | `scripts/figjam_checks/state.py:21`, `:46`, `references/types/state.md:60` |
| `R2-P2-001` | security | The contract never says source material is data rather than instructions, while six diagnostics echo a raw model line back | `references/flow-mode.md:256`, `SKILL.md:175`, `scripts/figjam_checks/sequence.py:76`, `gantt.py:59`, `er.py:48/79/99` |
| `R2-P2-002` | security | `--self-test` can report a full pass while a shipped template or example was dropped from the proof | `scripts/flow_check.py:229-230`, `:226-228`, docstring at `:38-40` |
| `R3-P2-001` | traceability | `references/flow-mode.md` declares itself `ON-DEMAND` while the contract loads it on every Flow route | `references/flow-mode.md:20` against `SKILL.md:64`, `assets/flow-templates.md:18` |
| `R3-P2-002` | traceability | The contract names `vendor.json` but never says where it lives, and the README names a different control | `SKILL.md:156`, `README.md:62`, `AI Systems/Product Owner/vendor.json` |
| `R4-P2-001` | maintainability | The packet file map is written twice and the two copies already disagree | `SKILL.md:141-157` against `README.md:49-63` |
| `R4-P2-002` | maintainability | The seven-type vocabulary is declared twice with nothing asserting the two agree | `SKILL.md:77` against `scripts/flow_check.py:70-71` |
| `R4-P2-003` | maintainability | The largest reference (441 lines) is loaded on every Flow route | `SKILL.md:64`, `references/flow-mode.md` Sections 6 to 8 |

---

## Remediation Workstreams

1. **Budget enforcement (`R1-P1-001`)** — set `BUDGET[USER_FLOW] = (9, 12)` in `scripts/figjam_checks/flowchart.py`, then add a planted fixture to `scripts/figjam_checks/fixtures.py` with thirteen connectors so `--self-test` proves the cap. If instead the user flow is meant to be uncapped, say so at `references/types/user-flow.md:66` and amend `references/flow-mode.md:298` so the shared rule stops claiming a cap that one type exempts. Either way one document and one table must agree afterwards.
2. **Rule precision (`R1-P2-001`, `R1-P2-003`)** — key the start exemption to the `stadium` shape rather than declaration order, and settle whether `TD` is a synonym of `TB` for state diagrams, then align `state.py:46` and `references/types/state.md:60` with the answer.
3. **Trust boundary (`R2-P2-001`)** — add one rule to `references/flow-mode.md` Section 4 and one `NEVER` entry to `SKILL.md` Section 4 stating that source material is data and never instructions, and quote the offending text at the six diagnostic sites rather than echoing it.
4. **Verification integrity (`R2-P2-002`)** — make `--self-test` fail, or say so in its summary, when a packet-owned shipped model carries no Mermaid block, so the proof cannot shrink silently.
5. **Documentation consistency (`R3-P2-001`, `R3-P2-002`, `R4-P2-001`, `R4-P2-002`)** — one loading level per file, one location for the vendor manifest, one file map (link `README.md` Section 3 to `SKILL.md` Section 3 instead of restating it), and one assertion tying the router's type tuple to the check's dispatch keys.
6. **Dead code and load cost (`R1-P2-002`, `R4-P2-003`)** — delete the unused `ARROWS` table, and consider splitting the write-route, read-back and delivery sections of `references/flow-mode.md` into an `ON_DEMAND` reference the way `references/hybrid-workflow.md` was split.

---

## Spec Seed

A follow-up spec would need, at minimum:

- the intended connector budget for each of the seven types, stated once and referenced by the others;
- the intended direction vocabulary for state diagrams (`LR`, `TB`, and whether `TD` is accepted as a synonym);
- the intended reading of a type's own loading level: does the reference header or `SKILL.md` Section 2 win;
- the trust-boundary rule for source material, in the same voice as the existing "Never invent" rule.

## Plan Seed

- Task 1: `flowchart.py` budget fix plus the thirteen-connector fixture, verified by `--self-test` and by re-running the iteration-5 scratch model.
- Task 2: the three documentation alignments (`flow-mode.md:20`, `SKILL.md:156`/`README.md:62`, `state.py:46`/`state.md:60`).
- Task 3: `README.md` Section 3 reduced to a link, so the file map has one owner.
- Task 4: the untrusted-source rule and the quoted diagnostics.
- Task 5: the `--self-test` coverage assertion.
- Task 6: delete `ARROWS`; decide on the `flow-mode.md` split.

---

## Traceability Status

| Protocol | Level | Status | Where |
|----------|-------|--------|-------|
| `spec_code` | core | partial | Every budget but the user-flow connector count matches its reference: process 12/16, architecture 9/12 with a ten-row allowed-edge table, sequence 5/12 with 3–20 character ids, state 9/12 with choices of 2 to 3, ER 9/12/10, gantt 12 tasks with sections past 8 and 5 parallel. |
| `checklist_evidence` | core | pass | The 52-file manual-testing playbook is complete against its index in both directions, and two scenario expectations match the code's wording verbatim. |
| `skill_agent` | overlay | pass | `SKILL.md:169` requires the check before the gate; the check was executed on eight models this session. |
| `agent_cross_runtime` | overlay | notApplicable | No agent file in the packet; `claude-plugin/` is out of scope by the review steer. |
| `feature_catalog_code` | overlay | notApplicable | The packet ships no `feature-catalog/`. |
| `playbook_capability` | overlay | pass | Two pre-write-check scenarios checked against live output; nine playbook files carry no `FJ-` id, which the index does not explain. |

---

## Deferred Items

- **The Figma write path.** Nothing here executed `generate_diagram`, `use_figma` or `get_figjam`; every write-route finding would need a live session. Not deferred as a finding because the packet's write rules were read, not exercised.
- **`AI Systems/Product Owner/claude project/knowledge/` mirrors.** They exist with the exact names the self-test globs, but reviewing mirror parity is outside this review's target.
- **The `fj` route.** `references/flow-mode.md:354-362` was read for consistency only; `figma-cli` behaviour is `../mcp-figma/`'s surface.
- **The nine playbook files without an `FJ-` id.** Recorded as an observation in the traceability table rather than a finding, because the index is complete and the ids are cosmetic.
- **`R1-P2-003` (`TD` for state diagrams).** Carried open rather than resolved: `TD` and `TB` are one Mermaid direction, so this may be deliberate and only the wording stale.

---

## Audit Appendix

**Iterations.** `iterations/iteration-001.md` through `iteration-005.md`, one per dispatched iteration, each ending in its own verdict line; `deltas/iter-001.jsonl` through `iter-005.jsonl` carry the matching structured records; every iteration record was handed to `.skilled/skills/system-deep-loop/runtime/scripts/append-mode-event.cjs` and the ledger receipts are in `deep-review-ledger/` and `deep-review-audit-ledger/`.

**Sources.** `specs/product-owner/018-product-owner-deep-review/002-sk-create-figjam/review/lineages/deepseek/steer.md` was read before init and before every iteration; its seven rulings were applied, including the target binding (the packet, not the staging spec), the out-of-scope list, the P0/P1/P2 rule, and the spread of dimensions across iterations.

**Execution evidence gathered.** Eight `flow_check.py` runs: all seven examples, all six templates, and five purpose-built scratch models under `.scratch/` (thirteen-connector user flow, `pie`, `graph TD`, `%% type:` on a sequence block, architecture in `TD`). Every run used `PYTHONDONTWRITEBYTECODE=1`; a search for `__pycache__` and `*.pyc` under the packet after the runs returned nothing, and no file in the reviewed packet was modified.

**Static evidence gathered.** A link check over all 81 packet markdown files (zero broken), a playbook index reconciliation (52 files, 52 links, 43 ids both ways), a palette reconciliation against `common.ACCENT_PAIRS` and `LANE_PAIR` (ten rows, all ratios true), a SHA-256 comparison of the vendored extractor against `AI Systems/Product Owner/vendor.json` and against the upstream file at `base_commit 330427cf`, and a heading check for the ten section cross-references between references.

**State.** `deep-review-config.json` (immutable after init), `deep-review-state.jsonl` (gateway-owned projection), `deep-review-findings-registry.json` (11 open, 0 resolved, all four dimensions covered), `deep-review-strategy.md`, `deep-review-dashboard.md`. No file outside this lineage directory was created or modified.

**Scope violations.** None. Nothing under `AI Systems/Product Owner/specs/`, `export/`, `benchmark/reports/`, `claude-plugin/`, `AI Systems/Product Context` was opened, and no screenshot or `figma.com` URL was fetched.
