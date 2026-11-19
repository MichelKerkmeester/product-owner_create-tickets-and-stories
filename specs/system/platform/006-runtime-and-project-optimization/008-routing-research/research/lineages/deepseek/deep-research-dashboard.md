---
title: Deep Research Dashboard
description: Auto-generated reducer view over the research packet.
---

# Deep Research Dashboard - Session Overview

Auto-generated from JSONL state log, iteration files, findings registry, and strategy state. Never manually edited.

<!-- ANCHOR:overview -->
## 1. OVERVIEW

Reducer-generated observability surface for the active research packet.

<!-- /ANCHOR:overview -->
<!-- ANCHOR:status -->
## 2. STATUS
- Topic: Product Owner routing in the parent hub, how its modes connect, routing in the Claude Project, README currency, dead code and documents, and code alignment with sk-code-skilled, as specs/z-staging-po-019s/spec.md scopes it
- Started: 2026-10-21T18:11:08Z
- Status: COMPLETE
- Iteration: 10 of 10
- Session ID: fanout-deepseek-1792606106702-iitd40
- Parent Session: none
- Lifecycle Mode: new
- Generation: 1
- continuedFromRun: none
- stopReason: max-iterations

<!-- /ANCHOR:status -->
<!-- ANCHOR:progress -->
## 3. PROGRESS

| # | Focus | Track | Ratio | Findings | Status |
|---|-------|-------|-------|----------|--------|
| 1 | Parent hub routing: stage one, stage two and the smallest source set | - | 0.74 | 9 | complete |
| 2 | Which router copies a gate holds equal, and which drift unchecked | - | 0.78 | 10 | complete |
| 3 | How the modes connect: hand-offs, energies and the then-FLOW pair | - | 0.70 | 9 | complete |
| 4 | Routing in the Claude Project layer, and what can shrink without losing a must-fire rule | - | 0.68 | 9 | complete |
| 5 | Ranked routing and mode-link changes with files, risk, gate and kernel bytes | - | 0.60 | 10 | complete |
| 6 | README currency: which claims the files no longer support | - | 0.66 | 8 | complete |
| 7 | Dead code: scripts, gates and config entries nothing reads | - | 0.70 | 8 | complete |
| 8 | Dead documents: references, assets, examples and playbooks nothing loads | - | 0.62 | 7 | complete |
| 9 | Code standards: the Product Owner's own Python, shell, JavaScript and JSON | - | 0.60 | 8 | complete |
| 10 | Synthesis: what is wrong, what to change first, and what the repository cannot settle | - | 0.45 | 10 | complete |

- iterationsCompleted: 10
- keyFindings: 88
- openQuestions: 0
- resolvedQuestions: 10

<!-- /ANCHOR:progress -->
<!-- ANCHOR:questions -->
## 4. QUESTIONS
- Answered: 10/10
- [x] How does the Product Owner parent route a request to a mode, where is routing logic stated more than once, where do the copies disagree, and what is the smallest set of routing sources that still serves the CLI, the hub and the Claude Project?
- [x] Which router copies are held equal by a gate such as benchmark/router/differential.py, and which drift unchecked?
- [x] Where is a hand-off between modes undefined, duplicated or contradictory?
- [x] Is routing embedded in the right Claude Project layer, and what could shrink without losing a rule that must fire every turn?
- [x] What are the concrete, ranked routing and mode-link changes, each with the files it touches, its risk, the gate that proves it and the byte effect on the kernel?
- [x] Which README claims are stale against the files they describe?
- [x] Which scripts, functions, flags and config entries are dead code?
- [x] Which references, assets, examples and playbook files are dead documents?
- [x] How does the Product Owner's own Python, shell, JavaScript and JSON deviate from the sk-code-skilled standards?
- [x] What is the ranked synthesis of every finding, and what can the repository not settle?

<!-- /ANCHOR:questions -->
<!-- ANCHOR:uncovered-questions -->
## Uncovered Questions
- Count: 0
- None

<!-- /ANCHOR:uncovered-questions -->
<!-- ANCHOR:trend -->
## 5. TREND
- newInfoRatio sparkline: ▇██▇▆▆▆▅▅▅▅▆▆▆▅▅▄▄▃▁
- score sparkline: ▇██▇▆▆▆▅▅▅▅▆▆▆▅▅▄▄▃▁
- Last 3 ratios: 0.62 -> 0.60 -> 0.45
- Stuck count: 0
- Guard violations: none recorded by the reducer pass
- convergenceScore: 0.45
- coverageBySources: {"other":69}
- Advisory events: none

<!-- /ANCHOR:trend -->
<!-- ANCHOR:dead-ends -->
## 6. DEAD ENDS
- Looking for a Product Owner activation manifest for compiled routing under .skilled: no manifest exists, and the resolver falls back to legacy by design (iteration 1)
- Treating leaf-manifest.json as a routing source: it is a generated inventory of (workflowMode, leaf) pairs with no intent or policy (iteration 1)
- Treating mode-registry.json aliases as hub routing keywords: they are advisor aliases (task, bug, story, epic, prd, doc, figjam, cupt) and are not read by stage one (iteration 1)
- Treating the compiled router as the current stage-one authority: the command returns {"servingAuthority":"legacy"} for product-owner, so the legacy rules are the live authority (iteration 1)
- Counting the gold-row replay as a stage-one specification gate: it tests a replica against expectations, not the prose against the replica (iteration 2)
- Looking for a second Python fence or a pasted router definition in SKILL.md or routing.md: both are refused by copy parity, which is why the prose copies are prose only (iteration 2)
- Treating sk-create-figjam/ROUTER.md as an existing copy: the file is absent and a hub gate forbids it (iteration 2)
- Treating the differential corpus group named known-divergences as an exemption: compare_input applies to every corpus input with no exception list, so those two entries must now agree (iteration 2)
- Looking for a Deep or Raw branch in the executable router: detect_energy has two returns and no other energy vocabulary (iteration 3)
- Looking for a Flows group in the bug report template: the scaffold has no such group, which is what makes the Bug-plus-FigJam pair unwritable (iteration 3)
- Treating 'Section 7 Push Targets' as a dangling pointer: Section 7 INTEGRATION POINTS does contain a Push Targets subsection (iteration 3)
- Treating the Doc shapes as inconsistent: the five shapes are named identically in routing.md, doc-mode.md and doc-templates.md (iteration 3)
- Treating the Story-with-nested-tasks bundle as a two-artifact conflict: Story Mode explicitly says it is one dependent deliverable and only two explicit commands conflict (iteration 3)
- Looking for a Broken Full detail pointer: all 18 name one of five targets and all five exist in the knowledge folder (iteration 4)
- Moving routing out of the kernel into Knowledge: retrieval by relevance cannot guarantee a decision that must fire on every turn, and differential explicitly treats a Router Contract knowledge document as a failure (iteration 4)
- Quoting a kernel-only shrink of Section 11: copy parity makes the kernel and router-contract.md one edit (iteration 4)
- Treating kernel-review.json as a live version record: its own note says nothing reads it and the live versions are the kernel H1 and the dated notes in SYNC.md (iteration 4)
- Adding a compiled activation manifest for product-owner to make the directive live: the hub gate and the gold rows would then measure a router nobody exercised, and admission needs a scored scenario per mode first (iteration 5)
- Deleting the stage-one prose without moving its worked examples into hub-router.json: the examples in rules 3 and 4 are the only place the tool-signal-versus-artifact collision is explained (iteration 5)
- Looking for a gate that would prove a kernel prose deletion safe: none exists; only the hand parity review in SYNC.md covers rule retention (iteration 5)
- Trimming Section 11 to shrink the kernel: copy parity makes the kernel and router-contract.md a single edit, so a kernel-only trim cannot land (iteration 5)
- Looking for a gate that reads a README count: none does, which is why three documents kept the old number while one was updated (iteration 6)
- Treating 'all 12 gates pass' as stale: run_gates.sh declares twelve entries and the four clone-time skips are exactly the ones its README names (iteration 6)
- Treating the claude project README's 63-file upload list as stale: the folder holds 63 markdown files, 35 core and 28 examples (iteration 6)
- Treating the root README's 21 plus 7 example split as stale: the knowledge folder holds exactly 5 Task, 4 Bug, 7 Doc, 5 Story and 7 Flow mirrors (iteration 6)
- Calling figjam_checks/fixtures.py dead because flow_check does not import it at module load: it is imported inside the self-test at line 211 and every planted model in it is used (iteration 7)
- Calling route_contract.py --self-check dead: the root README documents it as a one-sample-per-layer smoke test (iteration 7)
- Calling the five benchmark/parity wrappers dead: they are documented manual checks, and run_gates.sh explains why they are not in the automatic list (iteration 7)
- Searching for a script basename with a single reference: every basename resolved to at least a caller and its own definition (iteration 7)
- Searching for a zero-reference top-level function or UPPER constant in the 21 definition-bearing files: none was found, in code-only reference counting (iteration 7)
- Calling figjam assets/templates/user-flow.md dead: no such file exists, and user flow patterns live in assets/flow-templates.md, which every Flow route loads (iteration 8)
- Calling the 35 benchmark company fixtures dead: every one is named by at least one playbook scenario (iteration 8)
- Calling the figjam playbook's 52 scenarios unlinked: its index links them with a Feature File anchor the first extractor missed (iteration 8)
- Counting inbound markdown links as reachability: it marked 549 files orphan, including every routed reference, because the manifest and the lane tables are the real load path (iteration 8)
- Searching for a leaf that no lane names: every leaf is covered either by name or by a directory token, so the only miss is routing.md getting prose mention instead of a lane (iteration 8)
- Calling the nine missing -e flags a defect: a runner that must count failures cannot exit on the first one, and run_gates.sh documents the counting behaviour (iteration 9)
- Looking for tabs or missing trailing newlines in JSON: none in ten files (iteration 9)
- Searching for a Python stderr or exit-code rule in the standard: the standard states neither, so printing gate findings to stdout and using exit codes is not a deviation (iteration 9)
- Treating the 191-character component headers as line-length violations: they are the house header rule, and the 59 remaining lines are measured with comment lines exempted (iteration 9)
- Treating unquoted-variable style as weak: shellcheck at info level reports nothing on any of the nine scripts (iteration 9)
- Blending the P0 hand-off findings into one fix: each contract lives in a different file and needs its own scenario, and bundling them is how one gets silently dropped (iteration 10)
- Looking for dead code or dead documents to rank: none exists, so the ranked list is contracts, gates and documentation instead (iteration 10)
- Reporting the four documented energies as a kernel bug: the kernel may legitimately offer Raw as an intake signal the resolver never emits, which is why it is an owner question rather than a defect (iteration 10)
- Searching for a gate that would have caught the stale plugin copy, the link drift or the four unread config entries: no gate reads any of them (iteration 10)
- Treating the routing defect count as a reason to rewrite the router: three implementations are already held equal by differential.py, and the defects are contract statements, not algorithms (iteration 10)

<!-- /ANCHOR:dead-ends -->
<!-- ANCHOR:divergent-pivots -->
## 6A. DIVERGENT PIVOTS
- Completed pivots: 0
- Failed pivots: 0
- Audited overrides: 0
- Saturated: none yet
- Pivot lineage: none yet
- Remaining frontier: none recorded

<!-- /ANCHOR:divergent-pivots -->
<!-- ANCHOR:next-focus -->
## 7. NEXT FOCUS
[All tracked questions are resolved]

<!-- /ANCHOR:next-focus -->
<!-- ANCHOR:active-risks -->
## 8. ACTIVE RISKS
- None active beyond normal research uncertainty.

<!-- /ANCHOR:active-risks -->
<!-- ANCHOR:blocked-stops -->
## 9. BLOCKED STOPS
No blocked-stop events recorded.

<!-- /ANCHOR:blocked-stops -->
<!-- ANCHOR:graph-convergence -->
## 10. GRAPH CONVERGENCE
- graphConvergenceScore: 0.00
- graphDecision: [Not recorded]
- graphBlockers: none recorded

<!-- /ANCHOR:graph-convergence -->
