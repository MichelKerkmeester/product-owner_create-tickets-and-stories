# Product Owner Routing and Repository Hygiene — Research Synthesis

Ten iterations of read-only investigation into `AI Systems/Product Owner/`, run as the `deepseek` fan-out lineage for `specs/z-staging-po-019s`. Every claim below was established in an iteration, cited to repository evidence, and passed `verify-iteration.cjs`. Nothing was changed in the system under study.

---

## 1. Verdict

The routing **algorithm** is sound and gated. The routing **contract** is not: three stage-one authorities disagree, two leaf maps are never compared, and seven mode hand-offs are undefined or contradictory in ways that produce a wrong artifact rather than a slow reply.

The repository is also cleaner than its reputation suggests. No dead code file exists, no dead document exists, and the code compiles and lints clean. What is missing is enforcement around the edges: the build copy, the links, four config entries and the README counts are all unread by any gate, which is exactly why each has drifted.

**Fix the contract before trimming the kernel.** The kernel is 70,010 bytes and 17 percent of it can go, but the largest block, Section 11, is held byte-equal to `router-contract.md` by `differential.py`; trimming it without the source change fails the gate, and trimming anything else has no retention gate at all.

---

## 2. Method

| Iteration | Question | Result |
|---|---|---|
| 1 | How does the parent route, where is routing duplicated, what is the smallest source set? | 7 findings, verified |
| 2 | Which router copies are gate-held equal, which drift unchecked? | 8 findings, verified |
| 3 | Where is a mode hand-off undefined, duplicated or contradictory? | 8 findings, verified |
| 4 | Is routing in the right Project layer, what could shrink? | 8 findings, verified |
| 5 | Concrete ranked changes with files, risk, gate and byte effect | 8 findings, verified |
| 6 | Which README claims are stale? | 8 findings, verified |
| 7 | Which scripts, functions, flags and config entries are dead? | 8 findings, verified |
| 8 | Which references, assets, examples and playbooks are dead? | 7 findings, verified |
| 9 | How does the code deviate from the sk-code-skilled standards? | 8 findings, verified |
| 10 | Ranked synthesis and what cannot be settled | this document |

Evidence rules applied throughout: every count was resolved against the file that holds it, never against another document; every reachability claim was checked against the load path the runtime actually uses (leaf manifest, ROUTER map, lane tokens), not against a link graph; and no file was called dead until it was searched by name and by stem.

---

## 3. P0 — wrong artifacts, not slow replies

### 3.1 Three stage-one authorities, no precedence

Stage one exists as hub `SKILL.md` prose, `ROUTER.md`'s table, and `hub-router.json`. Rules 3 and 4 are both stated as absolute and collide on a request that opens with a tool and also names an artifact; no gold row covers that collision. [SOURCE: AI Systems/Product Owner/SKILL.md:1-40] [SOURCE: AI Systems/Product Owner/ROUTER.md:36-60] [SOURCE: AI Systems/Product Owner/hub-router.json:1-30]

Two smaller defects sit in the same cluster:

- `DEFAULT_RESOURCE` names the two ALWAYS cards in `ROUTER.md` and `interactive-mode.md` in `router-contract.md`. The contract's value is read by nothing — `route_contract.py` never mentions the constant. [SOURCE: AI Systems/Product Owner/sk-product-owner/references/router-contract.md:49]
- `router-contract.md`'s ALWAYS lane names `sk-product-owner/SKILL.md`, a path its own load guard refuses because the inventory is packet-relative. That entry can never load.

**Order:** state first-match-wins in the hub rule text; add the collision row to `benchmark/hub-routing-cases.json`; delete `DEFAULT_RESOURCE` or give it the `ROUTER.md` value; then make `hub-router.json` the single authority and reduce the hub prose to a pointer.

### 3.2 Two leaf maps that no gate compares

`ROUTER.md`'s `RESOURCE_MAP` is held by the root-router contract; `leaf-manifest.json` is held by the manifest walk; nothing compares them to each other, and their key sets differ. The FLOW lane escapes the differential's table parity entirely, so FigJam routing has no executable contract. [SOURCE: AI Systems/Product Owner/ROUTER.md:36-60] [SOURCE: AI Systems/Product Owner/leaf-manifest.json:1-20] [SOURCE: AI Systems/Product Owner/benchmark/router/differential.py:573-613]

**Order:** add one lane-parity comparison covering every lane including FLOW, and run it before any map edit. This is the highest-cost fix and should be scheduled last, not first.

### 3.3 Seven hand-offs with no single contract

| # | Hand-off | Defect |
|---|---|---|
| 1 | Flow kept in the default packet | Hub says it stays; packet hands off to `sk-create-figjam` |
| 2 | Story → Task | Story Mode calls a single unit Task Mode; `task-mode.md` and `routing.md` disagree about the bundle's task path and the `$story`/`$task` conflict |
| 3 | Bug + FigJam paired output | The rule allows a paired board but the bug scaffold has no Flows group to receive it |
| 4 | Bug → Task | Undefined at routing time: grouped bugs, consolidation tickets and bug-fix tasks all claim the same shape |
| 5 | Interactive clarification | The clarification-lane sentence omits Task while the template prints a Task shape |
| 6 | Quick fallback | Stated three ways across `routing.md`, the packet `SKILL.md` and the hub |
| 7 | Energies Raw and Deep | Both documented as selectable, neither emitted by the resolver |

A sixth pointer problem belongs here: the ClickUp hand-off has one owner but three pointer forms.

[SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:139] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/task-mode.md:1-40] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:74] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:24]

**Order:** one contract per file, one playbook scenario per contract. Do not bundle them; bundling is how one gets dropped.

---

## 4. P1 — gates that do not reach the thing they describe

| Gap | Evidence | Consequence |
|---|---|---|
| `check_hub.py` replays 37 gold rows against its own Python replica | [SOURCE: AI Systems/Product Owner/benchmark/gates/check_hub.py:296-303] | Prose routing rules are untested |
| `differential.py` holds only Section 11 equal to the pseudocode | [SOURCE: AI Systems/Product Owner/benchmark/router/differential.py:691-705] | A kernel routing rule can be rewritten as long as the code block is untouched |
| Five guards run, two READMEs say four | [SOURCE: AI Systems/Product Owner/README.md:706] | The guard that protects the prose is the undocumented one |
| 33 gold rows claimed in two documents, 37 in the file | [SOURCE: AI Systems/Product Owner/benchmark/gates/README.md:22] | Stale derived count, updated in one of three places |
| Plugin copy one line behind its source | [SOURCE: AI Systems/Product Owner/claude-plugin/skills/product-owner/sk-product-owner/references/router-contract.md:343-344] | A shipped build lacks the `just do it` branch |
| `build-plugin.py` in no gate | [SOURCE: AI Systems/Product Owner/scripts/build-plugin.py:37-38] | Nothing compares the build to the sources |
| No link check anywhere | 13 real broken links in the vendored code-mode playbooks; 13 in-scope files write placeholders as links | Link drift is invisible until a reader hits it |

The kernel economy finding belongs at this level too: 70,010 bytes total, Section 11 at 588 lines and 27,025 bytes fixed by parity, and 12,202 bytes (about 17 percent) shrinkable across Sections 5, 7 and 8, the six-line empty Section 10, and the 18 Full detail pointers that name five targets. The knowledge-lane map is stated three times and the kernel's `RESOURCE_MAP` names 17 paths a Project cannot read. [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:221-224]

---

## 5. P2 — documentation, hygiene and standards

**Documentation currency.** Four stale claims, all counted against the file that holds the number: gold rows 33 vs 37 in `benchmark/gates/README.md` and the manual-testing playbook; guards four vs five in `README.md` and `benchmark/router/README.md`; examples 20 vs 21 in `sk-product-owner/README.md`; and the playbook contradicting itself inside one file. Every other audited count held — 141 route fixtures, 220 differential inputs, 59 format cases over 19 fixtures, 63 knowledge files, 29 changelog notes, 12 gates, 4 packets, 21 plus 7 worked examples.

**Dead code and dead documents: none.** All 31 runtime files and all 73 routed leaves are reached. The real leftovers are four config entries with no reader (`toolSurface.bashAllowlist`, `toolSurface.workspaceWrites`, the empty `extensions.transport-axis.crossHubPairing`, `defaultResourceSemantics`), one unlaned reference (`routing.md`), one unlinked hub release note, and one stale corpus group name (`known-divergences`).

**Standards.** 22 Python files compile; shellcheck reports nothing across nine scripts; both CommonJS files parse; ten JSON files are well formed. Deviations are documentation and types: no script explains why it omits `set -e` (the behavior is right for a counting runner), the 1,702-line format gate lacks `'use strict'`, 59 Python lines exceed 120 characters, and `hvr_lint.py` annotates no return. The exit-code discipline — 64 for a usage error, 66 for a missing target, shared across Python and JavaScript — is the pattern new scripts should copy.

---

## 6. Fix order

1. `DEFAULT_RESOURCE` and the unloadable ALWAYS entry in `router-contract.md`.
2. First-match-wins in the hub rule text plus the collision gold row.
3. The seven hand-off contracts, one file and one scenario each.
4. `hub-router.json` as stage-one authority, hub prose reduced to a pointer.
5. Kernel trim in the order Section 10, pointers, Section 8, Section 7, Section 5 — with human parity review.
6. Build-freshness and link rows in `run_gates.sh`; placeholders rewritten.
7. Leaf-map unification and FLOW parity (largest and riskiest).
8. Counts, unread config entries, `routing.md` lane, hub release note link.
9. Vendored link fix pushed upstream through `vendor-sync.py`.

---

## 7. What this repository cannot settle

- **Which stage-one source is intended authority.** An owner decision, not an evidence question.
- **Whether a trimmed kernel keeps every rule a Project needs.** No automated gate enforces retention of non-Section-11 rules; this needs human parity review.
- **Whether the Project is deployed.** No receipt exists in this repository, so no deployment claim is made.
- **The playbook's dated-run claim.** `benchmark/reports/` was out of scope; unverified, not false.
- **Whether the four unread registry fields have consumers.** None in this repository or in `.skilled`; an external advisor could read them.

---

## 8. Provenance disclosure

- Iteration 1's ledger row carries a timestamp and a `durationMs` that were written by hand rather than read from a clock. The ledger is append-only, so the row was not corrected; it is disclosed here instead of being presented as measured.
- Every iteration records `durationMs: 0`, which is a placeholder, not a measured elapsed time.
- Route proof for all ten iterations comes from each `deltas/iter-0NN.jsonl` artifact, because the state projection carries no leaf-dispatch fields. `verify-iteration.cjs` warns about this on every run; the warning is expected, not a failure.

---

## 9. Verification receipt

- 10 of 10 questions answered; 88 key findings recorded by the reducer, 0 open, 0 uncovered.
- `reduce-state.cjs`: 10 iterations completed, `corruptionCount` 0, status COMPLETE, terminal stop `max-iterations`.
- `verify-iteration.cjs`: each of iterations 1–10 returned `OK ... narrative + route-proof + delta`.
- All ten iteration files, deltas and this synthesis exist on disk under `specs/z-staging-po-019s/research/lineages/deepseek/`.
- No file outside that directory was written; no nested CLI, agent or subprocess was dispatched.
