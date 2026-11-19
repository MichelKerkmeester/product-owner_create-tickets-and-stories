# Deep Review Report: Product Owner system and nested skills

## 1. Executive Summary

- **Verdict:** CONDITIONAL
- **hasAdvisories:** true
- **Active findings as the reviewer filed them:** P0 0, P1 4, P2 21. The registry shows 7 P1 rows because iteration 10 re-filed three open P1s as refinement rows
- **After orchestrator adjudication:** P1 3 confirmed and 1 downgraded to P2. Of the P2s, 1 is refuted, 1 is declined, 1 is by design and 2 are owner decisions. The rest are confirmed
- **Scope:** the whole Product Owner system in `AI Systems/Product Owner`: hub `SKILL.md`, `ROUTER.md` and `AGENTS.md`, `sk-product-owner`, `sk-create-figjam`, the vendored `mcp-click-up`, `mcp-aside-devtools`, `mcp-chrome-devtools`, `mcp-code-mode` and `mcp-figma` packets, `vendor.json` and `scripts/vendor-sync.py`, `claude project/`, `benchmark/`, `manual-testing-playbook/`, `SYNC.md`, READMEs and changelogs, plus the Sync Loop twin and the Skilled sk-doc, sk-code and overlay contracts
- **Executor:** cli-pi, `opencode-go/deepseek-v4.1-flash` at max effort, 10 iterations (stop policy max-iterations). Iterations 1 and 2 ran in sequence. Iterations 3 to 9 ran as seven parallel lanes on the operator's request, each on its own focus. Iteration 10 replayed every open finding. Wall time 21 minutes
- **Operator review focus:** drift, bugs and refinement opportunities, alignment with Skilled sk-doc and sk-code, how easily the vendored mcp and browser packets sync from Skilled, and whether the Skilled overlay and repin support could replace `scripts/vendor-sync.py`

## 2. Planning Trigger

Remediation runs in Product Owner packet `specs/system/030-system-review-and-vendor-sync`.

```json Planning Packet
{
  "triggered": true,
  "verdict": "CONDITIONAL",
  "hasAdvisories": true,
  "activeFindings": [
    {"id": "F01", "severity": "P1", "file": "AI Systems/Product Owner/SKILL.md:87"},
    {"id": "F03", "severity": "P1", "file": "AI Systems/Product Owner/mcp-chrome-devtools/references/cdp-patterns.md:412"},
    {"id": "F04", "severity": "P1", "file": "AI Systems/Product Owner/mcp-chrome-devtools/README.md:95"}
  ],
  "remediationWorkstreams": ["WS1 hub doc drift", "WS2 browser capture rules upstream", "WS3 gates and config", "WS4 Claude Project kernel", "WS5 vendor sync conveniences"],
  "specSeed": ["The hub rules match what check_hub.py enforces", "Browser captures never land in the repository", "One command syncs every vendored entry"],
  "planSeed": ["Five parallel work packages with separate file sets", "Upstream fixes commit in Skilled first, then vendor-sync pulls them"],
  "findingClasses": ["contract_drift", "rule_gap", "producer_consumer_mismatch", "duplicate_artifact_drift", "doc_count_drift", "maintainability"],
  "affectedSurfacesSeed": ["AI Systems/Product Owner/SKILL.md", "AI Systems/Product Owner/ROUTER.md", "AI Systems/Product Owner/AGENTS.md", "AI Systems/Product Owner/benchmark/", "AI Systems/Product Owner/scripts/", "AI Systems/Product Owner/claude project/", "Skilled mcp-chrome-devtools", "Skilled mcp-aside-devtools"],
  "fixCompletenessRequired": true
}
```

## 3. Active Finding Registry

The reviewer used three id styles across lanes, so the rows carry one id each here. `It` is the iteration that filed it.

| ID | It | Sev | Title | File:line | Orchestrator verdict |
|----|----|-----|-------|-----------|----------------------|
| F01 | 1, 10 | P1 | Hub NEVER rule forbids the packet `ROUTER.md` that all seven packets carry and the gate requires | `SKILL.md:87`, `:82` | Confirmed. `check_hub.py:216-230` requires the file. The prose is the stale side |
| F02 | 2, 10 | P1 | Release gate runs a diverged fork of the Sync Loop validator | `benchmark/format/validate-output-format.cjs:1` | Downgraded to P2. The file is the reference implementation by design. `reference-parity.cjs` holds the shared validator to its exact output and runs in the Sync Loop harness. The real gap: Product Owner's own gates never run that check |
| F03 | 3 | P1 | Browser evidence artifacts carry live session secrets with no redaction rule and no ignore boundary | `mcp-chrome-devtools/references/cdp-patterns.md:412` | Confirmed. Upstream rule gap plus a missing `.gitignore` boundary here |
| F04 | 8, 10 | P1 | Vendored docs name `chrome_devtools_1` and `chrome_devtools_2`, which `.utcp_config.json` never registers | `mcp-chrome-devtools/README.md:95` | Confirmed as a mismatch. The vendored docs describe Skilled's own config, which registers both. The fix is a local statement in the hub, not a rename |
| F05 | 1 | P2 | `scripts/` claimed as a declared repo-root-hub path but absent from `repoPaths` | `SKILL.md:69` | Confirmed |
| F06 | 1 | P2 | `ROUTER.md` names a parser script that is not in the repository | `ROUTER.md:73` | Confirmed. The script lives in the shared skill folder |
| F07 | 1 | P2 | `INSTALL-GUIDE.md` exclusion justified by a `ROOT_RESOURCES` array the packet does not have | `ROUTER.md:19` | Confirmed |
| F08 | 2 | P2 | Release runner passes while five parity and residency scripts never run | `benchmark/gates/run_gates.sh:29` | By design. The runner header says they refuse an uncommitted declaration and run from `benchmark/parity/` after a commit |
| F09 | 2 | P2 | Gate wiring derives the existence-check path from the second whitespace token | `benchmark/gates/run_gates.sh:65` | Confirmed |
| F10 | 8 | P2 | `figma-developer-mcp@latest` and an unversioned `mcp-remote` float | `.utcp_config.json:75` | Confirmed. The fix depends on what the vendored docs pin |
| F11 | 3 | P2 | Aside redaction rule is scoped to an undefined term and weaker than its catalog leaf | `mcp-aside-devtools/SKILL.md:135` | Confirmed. Upstream fix |
| F12 | 3 | P2 | `vendor-sync.py` validates its discovered upstream root but not its override root | `scripts/vendor-sync.py:105` | Confirmed |
| F13 | 4 | P2 | 92 changelog entries in a placement `sk-create-changelog` deprecated | `sk-create-changelog/SKILL.md:10` | Refuted. Section 4 says changelogs live under `.skilled/changelog/` and in each skill's own `changelog/` folder. Only spec-folder changelogs are deprecated |
| F14 | 4 | P2 | `.gitignore` omits Python cache directories | `.gitignore:2` | Confirmed |
| F15 | 5 | P2 | Kernel retrieval table undercounts the example documents | `claude project/Custom Instructions.md:192` | Confirmed. The last release added one example |
| F16 | 5 | P2 | Upload guide names a smoke matrix no playbook carries | `claude project/README.md:213` | Confirmed |
| F17 | 6 | P2 | Format validator has no JSDoc and no bracketed console prefix | `benchmark/format/validate-output-format.cjs:1718` | Declined. sk-code requires JSDoc on exported functions and this CLI script exports none. A console prefix would change output the fixtures and the twin parity check pin |
| F18 | 6 | P2 | Five parity wrappers omit `-e` with no stated reason | `benchmark/parity/run_*.sh` | Confirmed |
| F19 | 7 | P2 | `vendor.json` exclude list mixes build output with upstream content and gives no reason | `vendor.json` | Confirmed as a documentation gap |
| F20 | 7 | P2 | Two sync mechanisms with no cross-reference in any Product Owner doc | `scripts/vendor-sync.py` | Confirmed as a documentation gap |
| F21 | 9 | P2 | Hub layout block calls the browser trees packets and not packets in one line | `SKILL.md:66` | Confirmed |
| F22 | 9 | P2 | About 11,800 words load before task work and `AGENTS.md` restates registry precedence | `AGENTS.md:205` | Owner decision. A token diet changes behaviour and needs a benchmark run |
| F23 | 9 | P2 | Vendored packets have no local-edit path | `vendor.json:1` | Partly refuted. `push` is the local-edit path and `pull` refuses to overwrite local edits (`vendor-sync.py:509`). The docs do not say so |
| F24 | 9 | P2 | Kernel review record cannot say whether the kernel is current | `claude project/kernel-review.json:1` | Confirmed. The repository rule is dated sentences in `SYNC.md` and no ledger |
| F25 | 9 | P2 | `SYNC.md` is 22,351 words in 136 lines with two headings | `SYNC.md:6` | Owner decision. A restructure of the parity note is its own piece of work |

Evidence and claim-adjudication packets are in `iterations/iteration-0NN.md` for the iteration in the `It` column.

## 4. Operator Focus Answers

### Alignment with Skilled sk-doc

- **Package shape:** `package_skill.py --check --strict` passes for the hub, `sk-product-owner` and `sk-create-figjam`. The two "skilled contract" gates in `run_gates.sh` run the same validator on every release
- **One warning:** `sk-product-owner/SKILL.md` holds 5,000 words against a recommended maximum of 3,000
- **Changelog placement:** aligned. See F13
- **Hub contract:** one real drift, F01. The hub prose forbids what the upstream packet contract and the local gate both require
- **Checker gap in Skilled:** `sk-skill-check.cjs` returns `VALIDATOR_OUTPUT_INVALID` for a skill that lives outside a `.skilled/skills` folder, so `/doctor:sk-skill check` cannot judge these three skills. That is an upstream limitation, not a Product Owner defect

### Alignment with Skilled sk-code

- **Quality gate:** `quality-gate.cjs --files` over the 42 live code files reports comment hygiene, secrets, conflict markers and Python, shell and CJS syntax clean
- **One heuristic hit:** `sk-create-figjam/assets/compose-board.js:156` uses top-level `await`. It is a false positive. The file is a template that runs as the body of a `use_figma` call, and the "board composer self-test" gate proves every shipped model composes
- **Shell:** F18, five wrappers without `-e` or a stated reason
- **JSDoc:** F17, declined with the reason above

### Vendored package sync and the Skilled overlay engine

- **State:** `vendor.json` holds seven entries, five whole packets and two single-file entries. Six were in step. `mcp-code-mode` was three files behind one Skilled commit from the same day, which raised the Node floor to 24.22.1. It is pulled now and all seven are in step
- **Can `/doctor:overlay` and repin replace `vendor-sync.py`:** no. Three independent reads agree (iteration 7, a separate analysis agent that ran the engine on scratch trees, and the orchestrator's read of the engine header)
  - The engine hard-codes one vendored `.skilled` tree (`overlay-engine.cjs:73`). Product Owner has no `.skilled` folder and vendors into seven peer folders
  - One pin for the whole tree against seven per-entry pins
  - No include list, so the two single-file entries have no analog. A staged repin on a two-packet scratch tree exited 2 with 809 refusals
  - No verb that writes a local fix back upstream. `vendor-sync.py push` does that
  - The engine exists to carry a project's own edits across a re-copy. These copies carry none by rule
- **What makes sync easy instead:** a `sync` command that pulls every upstream-ahead entry and prints one line per entry, a `status --local` check that works in a standalone clone where the gate skips today, a `diff` command, and a recipe in `scripts/README.md`
- **What would change the answer:** a package-scoped repin in Skilled, local edits to vendored packets here, or dropping the standalone public clone, at which point Skilled's Link mode removes the need for any sync
- **Settled question from iteration 7:** `pull` refuses when the local copy has edits upstream does not carry (`vendor-sync.py:509`), so there is no data-loss path

## 5. Remediation Workstreams

1. **WS1 hub doc drift:** F01, F04, F05, F06, F07, F21
2. **WS2 browser capture rules, upstream in Skilled then vendored:** F03, F11
3. **WS3 gates and config:** F02 (run reference parity from the Product Owner format harness), F09, F10, F14, F18, and the `.gitignore` half of F03
4. **WS4 Claude Project kernel:** F15, F16, F24, plus the feedback-ticket label the previous packet deferred to the next kernel move
5. **WS5 vendor sync conveniences:** F12, F19, F20, F23 and the three commands above

Not remediated here: F08 (by design), F13 (refuted), F17 (declined), F22 and F25 (owner decisions).

## 6. Traceability Status

- **Core `spec_code`:** partial. The hub prose and the hub gate disagree (F01)
- **Core `checklist_evidence`:** pass. Each surviving finding cites the rule it breaks
- **Overlay `skill_agent`:** not applicable. The surface defines no agent
- **Overlay `feature_catalog_code`:** not applicable to the hub. The vendored catalogs are byte-identical copies
- **Overlay `playbook_capability`:** partial. The hub playbook holds 7 of 7 scenarios. The vendored chrome parallel-instance scenarios name manuals this system does not register (F04)
- **Overlay `agent_cross_runtime`:** not applicable

## 7. Deferred Items

- F22, the always-loaded word count. `AGENTS.md`, the hub and the packet `SKILL.md` load about 11,800 words before task work
- F25, an index for `SYNC.md`
- The `sk-product-owner/SKILL.md` word count warning
- The Skilled checker gap for skills outside `.skilled/skills`

## 8. Search Ledger

- **Ruled out by the reviewer:** a vendored copy carrying local overlays (0 drift across 529 recorded files), `exclude` and `include` on one entry, missing recorded files, `context/` as a packaging leak, a second `manual_call_templates` set, `USER-GUIDE.md` version drift
- **Ruled out by the orchestrator:** a `pull` that overwrites local edits, deprecated changelog placement, an unguarded validator fork

## 9. Audit Appendix

- **Convergence:** stop reason maxIterationsReached (operator-fixed 10). Convergence was telemetry only
- **Claim adjudication:** passed for iterations 1 to 9. Iteration 10 recorded `passed: false` because it re-filed three open P1s as refinement rows without new typed packets. Their packets exist in iterations 1, 2 and 8
- **Parallel lanes:** iterations 3 to 9 shared one run directory. Every lane wrote only its own narrative and delta, every append went through the gateway, and write containment reported no violation in any lane. Lanes derived their iteration number from the dispatcher, since the state log could not order seven concurrent writers
- **Replay depth:** iteration 10 re-read the four P1s in full and carried the 21 P2s on verified anchors
- **Core Protocols:** spec_code partial, checklist_evidence pass
- **Overlay Protocols:** skill_agent not applicable, feature_catalog_code not applicable, playbook_capability partial, agent_cross_runtime not applicable
- **Orchestrator checks run:** `package_skill.py --check --strict` on three skill roots, `quality-gate.cjs --files` on 42 files, `vendor-sync.py status`, `reference-parity.cjs`, and direct reads of `SKILL.md:80-92`, `check_hub.py`, `.utcp_config.json`, `sk-create-changelog/SKILL.md` section 4, `overlay-engine.cjs:1-90` and `vendor-sync.py:450-600`
