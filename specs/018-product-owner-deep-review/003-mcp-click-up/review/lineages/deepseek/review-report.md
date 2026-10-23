# Deep Review Report — Product Owner `mcp-click-up`

> Verdict source: findings registry (`deep-review-findings-registry.json`). Final line of every iteration is a self-report; this report recomputes from the registry: 0 P0, 4 P1, 12 P2 active.
>
> Review scope: `AI Systems/Product Owner/mcp-click-up/` (178 files, byte-copied upstream skill), `AI Systems/Product Owner/vendor.json`, `AI Systems/Product Owner/scripts/vendor-sync.py`, and the hub surfaces that route to and hand off through the packet (`AGENTS.md`, `SKILL.md`, `ROUTER.md`, `hub-router.json`, `mode-registry.json`, `leaf-manifest.json`, `sk-product-owner/SKILL.md`).
>
> Lineage: sessionId `fanout-deepseek-1792580454700-vajsq8`, generation 1, lineageMode `new`, 5 of 5 iterations, stop reason `maxIterationsReached`.

## 1. Executive Summary

- **Overall verdict: CONDITIONAL**
- **hasAdvisories: true** — twelve active P2 advisories accompany the four P1 findings.
- **P0: 0 · P1: 4 · P2: 12** (active; none resolved, none repeated).
- **Dimension coverage: 4 of 4** — correctness, security, traceability, maintainability.
- Review scope summary: the vendored packet was audited as a byte copy of `.skilled/skills/mcp-tooling/mcp-click-up`, together with the manifest that pins it, the tool that keeps it in step, and the six hub surfaces that describe how it is reached.

What holds up:

- The copy is faithful. `vendor-sync.py status` reports all three packages in step, `diff -rq` against the upstream tree is empty, and all 178 manifest hashes match both trees.
- The invariant is gated twice: `benchmark/gates/run_gates.sh:46-47` runs the sync check and its test suite, and `scripts/build-plugin.py:104-117` refuses to ship a packet that differs from the manifest.
- Navigation is clean: 0 broken relative links across the packet's 171 Markdown files, and no broken hub link outside template placeholders.
- The transport contract (markdown-aware parameters), the push-target variable names and the routing vocabulary agree across the hub, `sk-product-owner`, `.env.example` and the packet.

What does not:

- The hub's ClickUp handoff promises pushes on a `cupt`-only runtime that the packet says have no route there, and its private-doc recipe omits a required parameter.
- `doctor.sh` cannot see the Code Mode config from the vendored location, so its only MCP check is a false negative in the copy that ships here.
- The packet contradicts itself on whether `cupt` can create a task.

## 2. Planning Trigger

- `/speckit:plan` is required: four active P1 findings, three of them in Product Owner source (hub and `sk-product-owner`) and one upstream-only in the packet.
- No implementation was performed. This report is observation-only.

```json
{
  "triggered": true,
  "verdict": "CONDITIONAL",
  "hasAdvisories": true,
  "activeFindings": {
    "P0": 0,
    "P1": 4,
    "P2": 12,
    "ids": [
      "R2-P1-001", "R3-P1-001", "R3-P1-002", "R4-P1-001",
      "R1-P2-001", "R1-P2-002", "R1-P2-003",
      "R2-P2-001", "R2-P2-002",
      "R3-P2-001", "R3-P2-002",
      "R4-P2-001", "R4-P2-002",
      "R5-P2-001", "R5-P2-002", "R5-P2-003"
    ]
  },
  "remediationWorkstreams": [
    {
      "id": "W1",
      "severity": "P1",
      "findings": ["R2-P1-001"],
      "title": "Make the packet's diagnostic find the Code Mode config in any layout",
      "fixSite": "mcp-click-up/scripts/doctor.sh (upstream)",
      "surface": "vendored packet"
    },
    {
      "id": "W2",
      "severity": "P1",
      "findings": ["R3-P1-001"],
      "title": "Align the hub's handoff trigger with the surface that can actually push",
      "fixSite": "AI Systems/Product Owner/AGENTS.md:117",
      "surface": "hub bootstrap"
    },
    {
      "id": "W3",
      "severity": "P1",
      "findings": ["R3-P1-002"],
      "title": "Correct the private-doc push recipe to the packet's required parameters",
      "fixSite": "AI Systems/Product Owner/sk-product-owner/SKILL.md:306",
      "surface": "workflow packet"
    },
    {
      "id": "W4",
      "severity": "P1",
      "findings": ["R4-P1-001"],
      "title": "Resolve the cupt create contradiction one way",
      "fixSite": "mcp-click-up/feature-catalog/cupt-global-flags/json-flag.md:19 (upstream)",
      "surface": "vendored packet"
    },
    {
      "id": "W5",
      "severity": "P2",
      "findings": ["R1-P2-001", "R1-P2-002", "R1-P2-003"],
      "title": "Vendor tooling robustness: verified commit pin, atomic pull, guarded hash_tree",
      "fixSite": "scripts/vendor-sync.py, scripts/build-plugin.py",
      "surface": "hub tooling"
    },
    {
      "id": "W6",
      "severity": "P2",
      "findings": ["R2-P2-001", "R2-P2-002"],
      "title": "Credential and supply-chain hygiene in the packet's guidance",
      "fixSite": "mcp-click-up/INSTALL-GUIDE.md, mcp-click-up/references/mcp-tools.md (upstream)",
      "surface": "vendored packet"
    },
    {
      "id": "W7",
      "severity": "P2",
      "findings": ["R3-P2-001", "R3-P2-002"],
      "title": "Hub pointers: transport owner name and the unrepresentable install leaf",
      "fixSite": "sk-product-owner/references/doc-mode.md:416, ROUTER.md:19",
      "surface": "hub routing"
    },
    {
      "id": "W8",
      "severity": "P2",
      "findings": ["R4-P2-001", "R4-P2-002"],
      "title": "Packet document hygiene: one version per document, copy-relative run commands",
      "fixSite": "mcp-click-up/INSTALL-GUIDE.md (upstream)",
      "surface": "vendored packet"
    },
    {
      "id": "W9",
      "severity": "P2",
      "findings": ["R5-P2-001", "R5-P2-002", "R5-P2-003"],
      "title": "Ownership: one owner per restated fact",
      "fixSite": "mcp-click-up/feature-catalog/FEATURE-CATALOG.md upstream, AGENTS.md:117, mcp-click-up/SKILL.md:105",
      "surface": "hub and packet"
    }
  ],
  "specSeed": [
    "Record the vendoring contract as: byte copy plus manifest plus gate plus plugin re-check, with the packet never edited in Product Owner.",
    "Record that a vendored packet's diagnostic and run commands must resolve in both layouts, or state which layout is supported.",
    "Record the ClickUp handoff trigger set once, in sk-product-owner Section 7, and make AGENTS.md point at it.",
    "Record the private-doc push as two calls: clickup_create_document with create_page, then the page write with content_format text/md.",
    "Record whether cupt has a create command; if it does not, remove every cupt add claim from the packet."
  ],
  "planSeed": [
    "Edit AGENTS.md:117 to drop the bare cupt CLI from the offer trigger, or add the cupt-only branch that offers a comment or tag handoff instead of a task or doc push.",
    "Edit sk-product-owner/SKILL.md:306 to name create_page and split the create call from the page write, citing mcp-click-up/references/mcp-tools.md:251.",
    "Open an upstream change to mcp-click-up/scripts/doctor.sh: replace the fixed five-level walk with an upward search for .utcp_config.json.",
    "Open an upstream change to mcp-click-up/feature-catalog/cupt-global-flags/json-flag.md:19 and FEATURE-CATALOG.md:17,326 to remove cupt add from the --json list, or document the command in cupt-commands.md.",
    "Edit sk-product-owner/references/doc-mode.md:416 to name mcp-click-up/SKILL.md instead of mcp-tooling.",
    "Widen ROUTER.md:19's leaf contract to admit the packet-root INSTALL-GUIDE.md, or record it as an explicit non-leaf resource.",
    "Harden scripts/vendor-sync.py (verify base_commit, stage pull into a sibling directory) and guard hash_tree in scripts/build-plugin.py:114.",
    "Pin mcp-remote in the three snippets that launch it, and add the shell-history warning beside cupt config --api-token."
  ],
  "findingClasses": [
    "verification-gap",
    "non-atomic-write",
    "error-path",
    "incorrect-path-resolution",
    "credential-hygiene",
    "supply-chain",
    "capability-contract-mismatch",
    "parameter-contract-drift",
    "stale-reference",
    "unrepresentable-leaf",
    "version-header-drift",
    "layout-dependent-path",
    "contradictory-reference",
    "duplicated-fact",
    "unowned-duplication",
    "dead-vocabulary"
  ],
  "affectedSurfacesSeed": [
    "AI Systems/Product Owner/AGENTS.md",
    "AI Systems/Product Owner/sk-product-owner/SKILL.md",
    "AI Systems/Product Owner/sk-product-owner/references/doc-mode.md",
    "AI Systems/Product Owner/ROUTER.md",
    "AI Systems/Product Owner/leaf-manifest.json",
    "AI Systems/Product Owner/scripts/vendor-sync.py",
    "AI Systems/Product Owner/scripts/build-plugin.py",
    "AI Systems/Product Owner/mcp-click-up/scripts/doctor.sh (upstream)",
    "AI Systems/Product Owner/mcp-click-up/INSTALL-GUIDE.md (upstream)",
    "AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md (upstream)",
    "AI Systems/Product Owner/mcp-click-up/feature-catalog/FEATURE-CATALOG.md (upstream)",
    "AI Systems/Product Owner/mcp-click-up/feature-catalog/cupt-global-flags/json-flag.md (upstream)",
    "AI Systems/Product Owner/mcp-click-up/SKILL.md (upstream)"
  ],
  "fixCompletenessRequired": true
}
```

## 3. Active Finding Registry

### P0 — 0 active

None.

### P1 — 4 active

| ID | Title | Dimension | File:line | Evidence | Fix recommendation | Disposition |
|----|-------|-----------|-----------|----------|--------------------|-------------|
| R2-P1-001 | `doctor.sh` cannot find `.utcp_config.json` from the vendored copy | security | `AI Systems/Product Owner/mcp-click-up/scripts/doctor.sh:71` | Fixed five-level walk; live run printed "not found at expected repo root" while `AI Systems/.utcp_config.json` registers `clickup_official` | Upstream: search upward for the nearest `.utcp_config.json` | active |
| R3-P1-001 | The hub counts a cupt-only runtime as ClickUp tooling, promising a push the packet cannot perform | traceability | `AI Systems/Product Owner/AGENTS.md:117` | Trigger list includes the `cupt` CLI; packet marks task creation and documents MCP-only (`SKILL.md:91-92`); Section 7 excludes cupt (`sk-product-owner/SKILL.md:283`) | Align the trigger with the surface, or state the cupt-only branch | active |
| R3-P1-002 | The private-doc recipe omits `create_page` and folds the page write into the create call | traceability | `AI Systems/Product Owner/sk-product-owner/SKILL.md:306` | Packet marks `create_page` required and states the tool takes no content (`create-document.md:31,38`; `mcp-tools.md:251`) | Name `create_page`; split create from the page write | active |
| R4-P1-001 | Two packet documents say `cupt add` creates a task; four say cupt has no create command | traceability | `AI Systems/Product Owner/mcp-click-up/feature-catalog/cupt-global-flags/json-flag.md:19` | Contradicted at `mcp-tools.md:59,304`, `SKILL.md:353`, `create-task.md:49`; no `add` section in `cupt-commands.md` | Remove the `add` claim, or document the command in the reference | active |

Adjudication notes (adversarial self-check, replayed at synthesis):

- R2-P1-001 — Hunter: re-read `doctor.sh:71` and re-derived all three candidate depths; ran the script and reproduced the not-found line. Skeptic: could the packet be upstream-only by contract? No — the packet ships the script and a README that tells a reader to run it. Referee: **confirmed P1**.
- R3-P1-001 — Hunter: re-read `AGENTS.md:117`, `sk-product-owner/SKILL.md:283`, `mcp-click-up/SKILL.md:91`. Skeptic: if Section 7 governs, this is wording. But no document declares precedence and `AGENTS.md` is the bootstrap. Referee: **confirmed P1**; interacts with R4-P1-001 — if the CLI really has a create command, the trigger would be partly valid and W2/W4 must be settled together.
- R3-P1-002 — Hunter: re-read `SKILL.md:306` and the card's required-parameter row. Skeptic: the schema might default `create_page`; even then the recipe misdescribes the call and produces an empty doc first. Referee: **confirmed P1**.
- R4-P1-001 — Hunter: re-read all six statements. Skeptic: the CLI could not be executed here, so the reference is being trusted over a feature card. Referee: **confirmed P1** as an internal contradiction regardless of the CLI's truth.

### P2 — 12 active

| ID | Title | Dimension | File:line | Fix site |
|----|-------|-----------|-----------|----------|
| R1-P2-001 | The recorded upstream commit is never checked, so a mis-pin reports "in step" | correctness | `AI Systems/Product Owner/scripts/vendor-sync.py:236` | `scripts/vendor-sync.py` |
| R1-P2-002 | `pull` deletes the local copy before copying, so an interrupted pull truncates the packet | correctness | `AI Systems/Product Owner/scripts/vendor-sync.py:221` | `scripts/vendor-sync.py` |
| R1-P2-003 | A symlink inside a packet escapes the plugin build's refusal path as an uncaught exception | correctness | `AI Systems/Product Owner/scripts/build-plugin.py:114` | `scripts/build-plugin.py` |
| R2-P2-001 | Token guidance puts a ClickUp token on the command line with no history warning | security | `AI Systems/Product Owner/mcp-click-up/INSTALL-GUIDE.md:120` | upstream `INSTALL-GUIDE.md` |
| R2-P2-002 | The Code Mode bridge runs an unpinned third-party package on every launch | security | `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:20` | upstream `references/mcp-tools.md` |
| R3-P2-001 | `doc-mode.md` names `mcp-tooling`, a packet that does not exist here | traceability | `AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:416` | `sk-product-owner/references/doc-mode.md` |
| R3-P2-002 | The packet's INSTALL route loads a packet-root file the leaf contract cannot register | traceability | `AI Systems/Product Owner/ROUTER.md:19` | `ROUTER.md` / `leaf-manifest.json` |
| R4-P2-001 | `INSTALL-GUIDE.md` states two versions of itself and dates content before its own source | maintainability | `AI Systems/Product Owner/mcp-click-up/INSTALL-GUIDE.md:14` | upstream `INSTALL-GUIDE.md` |
| R4-P2-002 | Run commands use the upstream `.skilled/...` path, available here only through an untracked symlink | maintainability | `AI Systems/Product Owner/mcp-click-up/INSTALL-GUIDE.md:24` | upstream `INSTALL-GUIDE.md` |
| R5-P2-001 | Command surface and counts are hand-restated in three layers; the validator did not catch the drift | maintainability | `AI Systems/Product Owner/mcp-click-up/feature-catalog/FEATURE-CATALOG.md:17` | upstream `FEATURE-CATALOG.md` |
| R5-P2-002 | The ClickUp handoff has three independent authors and no stated owner | maintainability | `AI Systems/Product Owner/AGENTS.md:117` | `AGENTS.md` |
| R5-P2-003 | The packet router declares an `assets` base that does not exist | maintainability | `AI Systems/Product Owner/mcp-click-up/SKILL.md:105` | upstream `SKILL.md` |

## 4. Remediation Workstreams

**P0 — none.**

**P1, in order:**

1. **W2 — settle the handoff trigger (R3-P1-001).** One edit in `AGENTS.md:117` (drop the bare `cupt` CLI from the trigger, or add the cupt-only branch) closes the divergence with `sk-product-owner/SKILL.md:283`. This is the finding a user meets first.
2. **W4 — settle `cupt add` (R4-P1-001).** The answer to W4 changes W2's cost: if cupt can create tasks, `AGENTS.md` is right and the reference is wrong; if it cannot, the packet's four denials stand and the feature card and two catalog lines must change. Settle this before W2's wording.
3. **W3 — correct the private-doc recipe (R3-P1-002).** One edit in `sk-product-owner/SKILL.md:306`, mirroring `mcp-click-up/references/mcp-tools.md:251`.
4. **W1 — make the diagnostic layout-independent (R2-P1-001).** An upstream change in `mcp-click-up/scripts/doctor.sh`; until it lands, Product Owner's diagnostic cannot verify a Code Mode registration.

**P2 advisories, separated:**

- **W5 vendor tooling (R1-P2-001..003).** Verify `base_commit`; stage `pull`; guard `hash_tree` in the plugin build.
- **W6 credential and supply chain (R2-P2-001..002).** Prefer `cupt auth` and warn about `--api-token`; pin `mcp-remote`.
- **W7 hub pointers (R3-P2-001..002).** Fix the `mcp-tooling` name; decide the install leaf's contract status.
- **W8 packet documents (R4-P2-001..002).** One version per document; copy-relative run commands.
- **W9 ownership (R5-P2-001..003).** One owner per restated fact; drop the enumerated `--json` list; retire or create the `assets` base.

## 5. Spec Seed

- The vendoring contract is: byte copy, manifest with per-file hashes and a commit pin, a release gate, and a plugin re-check; nothing inside the packet is edited in Product Owner.
- A packet that ships scripts must document run paths that work wherever the packet is vendored, or name the one layout it supports.
- The ClickUp handoff has one owner (`sk-product-owner/SKILL.md` Section 7); every other document points at it.
- A private ClickUp doc is two calls: `clickup_create_document` (with `create_page`) then the page write with `content_format: "text/md"`.
- Whether `cupt` can create tasks or documents is a single fact that must appear in one place and be denied nowhere.

## 6. Plan Seed

- `AGENTS.md:117`: remove the bare `cupt` CLI from the offer trigger, or state the cupt-only branch (comment, tag, time, attach).
- `sk-product-owner/SKILL.md:306`: add `create_page`; split the create and page writes.
- `sk-product-owner/references/doc-mode.md:416`: name `mcp-click-up/SKILL.md`.
- `mcp-click-up/scripts/doctor.sh` (upstream): upward search for `.utcp_config.json`.
- `mcp-click-up/feature-catalog/cupt-global-flags/json-flag.md:19` and `FEATURE-CATALOG.md:17,326` (upstream): resolve `cupt add`.
- `mcp-click-up/INSTALL-GUIDE.md` (upstream): one version statement; copy-relative run commands.
- `mcp-click-up/references/mcp-tools.md:20` (upstream): pin `mcp-remote` in every snippet.
- `ROUTER.md:19`: admit the packet-root install guide as a leaf, or record it as a named exception.
- `scripts/vendor-sync.py`: verify the commit pin; stage `pull`.
- `scripts/build-plugin.py:114`: guard `hash_tree`.

## 7. Traceability Status

**Core protocols**

| Protocol | Status | Evidence | Drift |
|----------|--------|----------|-------|
| `spec_code` | pass | The spec's three in-scope entries were read in full; each finding names the file a fix changes, upstream where the packet owns the text | none |
| `checklist_evidence` | pass (notApplicable for a checklist) | The staging wrapper carries no `checklist.md`; the steer file's rulings supplied the acceptance rules and each was applied | none |

**AC_COVERAGE:** exempt — the staging folder has neither `checklist.md` nor an in-progress `implementation-summary.md`, so the lifecycle predicate for the advisory signal is inactive.

**Overlay protocols**

| Protocol | Status | Evidence | Drift |
|----------|--------|----------|-------|
| `skill_agent` | pass | `hub-router.json:70-78` declares `mcp-click-up/SKILL.md`; hub `SKILL.md:26` names the packet; the packet's Section 2 owns intra-packet routing | none |
| `agent_cross_runtime` | pass | `AGENTS.md:166` and hub `SKILL.md:26` agree on routing; `AGENTS.md:117` is the one divergent statement (R3-P1-001) | recorded |
| `feature_catalog_code` | partial | 50 cupt cards / 61 MCP tool cards reconcile to the tree; the claim layer contradicts itself on `cupt add` (R4-P1-001, R5-P2-001) | recorded |
| `playbook_capability` | pass (narrative), machine summary empty | Ownership is assigned at hub level (`manual-testing-playbook/manual-testing-playbook.md:11`); the packet's 43 scenario files and their `../../references/...` links resolve. The registry's `traceability.summary` reads `required: 0, executed: 0` because the iteration 4 and 5 check rows carried no `evidence` array, so the reducer could not count them; the strategy table correspondingly prints `pending` | recorded |

**Resource Map Coverage Gate:** skipped — `specs/product-owner/018-product-owner-deep-review/003-mcp-click-up/resource-map.md` does not exist, so `resource_map_present` is false and the gate has no map to converge.

## 8. Deferred Items

- Live ClickUp verification of the 61-tool inventory: the packet's inventory is a dated 2026-10-08 capture; checking it against the live server needs credentials this review does not have.
- The `claude project/` mirror: hand-written from the skill sources, outside the spec's declared scope; it may carry the same `cupt`-create contradiction and should be re-synced after W2–W4.
- The plugin output under `claude-plugin/`: generated by `scripts/build-plugin.py`; only the builder was reviewed.
- Turning `benchmark/gates/run_gates.sh` from a release step into a commit-time hook: the repository has no hooks today, and the gate's own README documents the release-step contract.

## Dimension Expansion Map

- Reducer-owned sweep state: 0 completed pivots, 0 failed pivots, 0 audited overrides, no saturated directions, no remaining frontier. This lineage spent its five iterations on four dimensions plus one closing maintainability pass rather than on pivot expansion.
- Selected review directions by iteration: (1) manifest and sync-tool correctness, (2) the executable and credential surface, (3) the hub's push-target and handoff contract, (4) navigation, versions and layout-dependent paths, (5) ownership of restated facts.
- Remaining frontier: none recorded; breadth was capped by `stopPolicy: max-iterations`, not by saturation.
- This section records breadth only and does not alter the verdict, `hasAdvisories`, the registry or the adversarial self-check.

## 9. Search Ledger

- **Search coverage (cumulative, registry `candidateCoverage`):** 19 bug classes covered by evidence, 10 ruled out, 0 deferred, 0 blocked; 15 classes produced at least one finding. `graphCoverageMode: graphless_fallback` (the coverage graph was not seeded in this fan-out lineage, so convergence remained telemetry under `max-iterations`).
- **Ruled-out ledger (7 entries, registry `ruledOutCandidates`):** `manifest_hash_drift` (iteration 1; verified byte-identical and hash-consistent); `command_injection` (iteration 2; arrays plus quoted expansion, no eval); `supply_chain` (iteration 2; documented design, not drift); `version_drift` (iteration 3; all four read 1.0.0.0); `stale_reference` (iteration 3; identical across three files); `broken_link` (iteration 4; 0 broken links); `playbook_duplication` (iteration 5; ownership is assigned in the hub playbook).
- **Clean search proof (7 entries, registry `cleanSearchProof`):** each ruled-out class was closed by a direct read or a read-only command whose result is recorded in the iteration narrative and its delta, so the disposition is evidence-backed rather than an assumption.
- **Search debt:** none (`searchDebtCount: 0`, `hasSearchDebt: false`).
- **Per-iteration ledgers:** `deltas/iter-001.jsonl` … `deltas/iter-005.jsonl`, one `ruled_out` row per closed class and one `finding` row per finding.

## 10. Audit Appendix

**Convergence summary**

| # | Focus | Ratio | P0/P1/P2 | Status | Verdict line |
|---|-------|-------|----------|--------|--------------|
| 1 | correctness | 1.00 | 0/0/3 | complete | PASS |
| 2 | security | 0.70 | 0/1/2 | complete | CONDITIONAL |
| 3 | traceability | 0.55 | 0/2/2 | complete | CONDITIONAL |
| 4 | references and paths | 0.24 | 0/1/2 | complete | CONDITIONAL |
| 5 | maintainability | 0.09 | 0/0/3 | complete | CONDITIONAL |

- Stop reason: `maxIterationsReached` (hard stop at the cap; `stopPolicy: max-iterations`, `convergenceMode: off`). Convergence before the cap was treated as telemetry, as the dispatch required.
- Registry convergence score after iteration 5: 0.906; no blocked stops, no repeated findings, no severity changes.
- Claim adjudication: typed packets exist for all four P1 findings and were replayed at synthesis (see §3 notes).

**Coverage summary:** 4 of 4 dimensions; 171 packet Markdown files plus 178 manifest entries, the three vendored packages, six hub documents, and the plugin builder.

**Ruled-out claims:** listed in §9; each names the command or read that closed it.

**Sources reviewed (read-only):** `spec.md` and `steer.md` in the staging folder; `AI Systems/Product Owner` — `AGENTS.md`, `SKILL.md`, `ROUTER.md`, `hub-router.json`, `mode-registry.json`, `leaf-manifest.json`, `description.json`, `.env.example`, `.gitignore`, `vendor.json`, `scripts/vendor-sync.py`, `scripts/build-plugin.py`, `scripts/tests/test_vendor_sync.py`, `benchmark/gates/run_gates.sh`, `benchmark/gates/README.md`, `manual-testing-playbook/manual-testing-playbook.md`, `sk-product-owner/SKILL.md`, `sk-product-owner/references/doc-mode.md`, `sk-product-owner/assets/interactive-response-templates.md`, and the `mcp-click-up/` packet (skill, install guide, four references, 111 feature cards, 43 playbook files, scripts, examples, changelog).
Read-only commands executed: `python3 scripts/vendor-sync.py status`, `diff -rq` against the upstream packet, `git log`/`git cat-file` in the resolved upstream repository, `git status --porcelain`, `bash mcp-click-up/scripts/doctor.sh`, plus link and hash sweeps over the trees. Nothing under review was modified; no test suite was run.

**Cross-reference appendix:** Core — `spec_code`, `checklist_evidence`. Overlay — `skill_agent`, `agent_cross_runtime`, `feature_catalog_code`, `playbook_capability`.

**Machine-owned artifact state:** config `status` flips to `complete` at synthesis; findings registry, dashboard and strategy are reducer-owned and were refreshed after every iteration.

## Source Tags

Every active finding's evidence line, as a resolvable repository-relative tag.

- R1-P2-001 — [SOURCE: scripts/vendor-sync.py:236]
- R1-P2-002 — [SOURCE: scripts/vendor-sync.py:221]
- R1-P2-003 — [SOURCE: scripts/build-plugin.py:114]
- R2-P1-001 — [SOURCE: mcp-click-up/scripts/doctor.sh:71]
- R2-P2-001 — [SOURCE: mcp-click-up/INSTALL-GUIDE.md:120]
- R2-P2-002 — [SOURCE: mcp-click-up/references/mcp-tools.md:20]
- R3-P1-001 — [SOURCE: AGENTS.md:117]
- R3-P1-002 — [SOURCE: sk-product-owner/SKILL.md:306]
- R3-P2-001 — [SOURCE: sk-product-owner/references/doc-mode.md:416]
- R3-P2-002 — [SOURCE: ROUTER.md:19]
- R4-P1-001 — [SOURCE: mcp-click-up/feature-catalog/cupt-global-flags/json-flag.md:19]
- R4-P2-001 — [SOURCE: mcp-click-up/INSTALL-GUIDE.md:14]
- R4-P2-002 — [SOURCE: mcp-click-up/INSTALL-GUIDE.md:24]
- R5-P2-001 — [SOURCE: mcp-click-up/feature-catalog/FEATURE-CATALOG.md:17]
- R5-P2-002 — [SOURCE: AGENTS.md:117]
- R5-P2-003 — [SOURCE: mcp-click-up/SKILL.md:105]

---

**Final verdict: CONDITIONAL** — 0 P0, 4 P1, 12 P2 active. No blocker, four fixes before release: settle the handoff trigger and the private-doc recipe in the hub, settle whether `cupt` can create, and make the packet's diagnostic work where it ships.
