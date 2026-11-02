# Deep Review Strategy - Product Owner mcp-figma (vendored transport packet)

Session: `fanout-deepseek-1792580474713-m4jej7` | target: `specs/product-owner/018-product-owner-deep-review/004-mcp-figma` | reviewer: cli-pi / deepseek-v4.1-flash

## 1. REVIEW CHARTER

- Target: the three in-scope surfaces named by `specs/product-owner/018-product-owner-deep-review/004-mcp-figma/spec.md`:
  `AI Systems/Product Owner/mcp-figma/` (58 vendored files), `AI Systems/Product Owner/vendor.json`,
  `AI Systems/Product Owner/scripts/vendor-sync.py`.
- The packet is a byte copy of `.skilled/skills/mcp-tooling/mcp-figma` at upstream commit
  `293caa90a865400557e1fd13af27ae785a3bd429`. It is never edited in Product Owner, so every
  finding inside `mcp-figma/` names the UPSTREAM file as its fix site.
- Dimensions: correctness, security, traceability, maintainability (all four; `review_dimensions: all`).
- Stop conditions: `stopPolicy: max-iterations` with 5 iterations; convergence mode off, so a low
  newInfoRatio is telemetry that widens the next angle instead of ending the loop.
- Success criteria: every in-scope surface read at least once, every finding carrying
  `[SOURCE: path:line]` and a named fix site, and one final verdict line per iteration.

## 2. TOPIC

Read-only review of the Product Owner Figma transport packet, its vendor manifest and its sync tool.

<!-- ANCHOR:review-dimensions -->
## 3. REVIEW DIMENSIONS (remaining)
[All dimensions complete]

<!-- /ANCHOR:review-dimensions -->
## 4. NON-GOALS

- Not the staging spec folder itself (`specs/product-owner/018-product-owner-deep-review/004-mcp-figma/` holds only the review scope note).
- Not `AI Systems/Product Owner/specs/`, `export/`, `benchmark/reports/` or `claude-plugin/`
  (run output and generated mirrors), per steer ruling 4.
- Not `AI Systems/Product Context`, any screenshot, or any figma.com URL: never opened.
- No fixes are implemented. This loop reports only.

## 5. STOP CONDITIONS

- 5 dispatched iterations (config.maxIterations), then synthesis.
- Escalate instead of guessing if the upstream copy of a cited line cannot be read.

<!-- ANCHOR:completed-dimensions -->
## 4. COMPLETED DIMENSIONS
- [x] correctness
- [x] security
- [x] traceability
- [x] maintainability

<!-- /ANCHOR:completed-dimensions -->
<!-- ANCHOR:running-findings -->
## 5. RUNNING FINDINGS
- P0 (Blockers): 0
- P1 (Required): 6
- P2 (Suggestions): 11
- Resolved: 0

<!-- /ANCHOR:running-findings -->
## 8. WHAT WORKED

- Reading the packet against the ACTUALLY INSTALLED `figma-ds-cli` 1.2.0 (`--version`, `--help`,
  per-command `--help`) instead of trusting the packet's own account of the command surface. The
  installed binary is the only oracle that can falsify a command-table row, and it did.
- Recomputing every `vendor.json` sha256 and diffing the vendored tree against the upstream tree:
  one command proved in-step status instead of arguing from the manifest alone.
- Resolving every markdown link from its own file's depth, both inside the vendored copy and inside
  the upstream tree, which separated "always broken" links from "broken only because of vendoring depth".

## 9. WHAT FAILED

- `vendor-sync.py status` was NOT executed: it needs an upstream tree walk that is safe, but the
  lineage write surface forbids any command whose side effects leave the lineage, and the hash
  comparison reproduced its three-tree logic in Python instead. Recorded as a method limit, not a defect.

<!-- ANCHOR:exhausted-approaches -->
## 9. EXHAUSTED APPROACHES (do not retry)
[No exhausted approach categories yet]

<!-- /ANCHOR:exhausted-approaches -->
## 10A. SATURATED / SWEPT DIMENSIONS AND EXPANSION FRONTIER
- Completed pivots: 0
- Failed pivots: 0
- Audited overrides: 0
- Swept: none yet
- Pivot lineage: none yet
- Remaining frontier: none recorded

## 11. RULED OUT DIRECTIONS

- "The vendored copy has drifted from upstream": ruled out by sha256 comparison of all 58 recorded
  files against the upstream tree (0 changed, 0 added, 0 removed) and by `base_commit` being the
  last commit that touched the upstream folder (iteration 1, evidence: vendor.json + git log).
- "`vendor.json` records files that no longer exist locally": ruled out, 58 recorded = 58 present.

<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
[All dimensions covered]

<!-- /ANCHOR:next-focus -->
## 13. KNOWN CONTEXT

### Bounded Context Snapshot

- Target pointers: `AI Systems/Product Owner/mcp-figma/SKILL.md` (routing + rules),
  `references/` (4 refs), `assets/` (2), `scripts/` (8 bash), `examples/` (2),
  `feature-catalog/` (8 + index), `manual-testing-playbook/` (28 + index), `changelog/` (6),
  `mcp-servers/` (3), `INSTALL-GUIDE.md`, `README.md`.
- Behavior claims to verify: canonical binary is `figma-ds-cli` and npm `figma-cli` is unrelated;
  full surface needs >= 1.2.0 from the silships repo; daemon on `127.0.0.1:3456`; safe connect is
  the default; every destructive verb is gated; exports never silently overwrite; the optional
  Framelink MCP is already registered in `.utcp_config.json` as `figma` and needs
  `figma_FIGMA_API_KEY`.
- Reuse and conventions: sibling vendored packet `mcp-click-up` uses the same manifest/sync pattern;
  `hub-router.json`, `mode-registry.json`, `leaf-manifest.json` route `mcp-figma` as a transport.
- Review risks and gaps: the packet is a byte copy, so any defect here is also upstream; runtime
  behaviour cannot be observed (no Figma session); `AI Systems/Product Owner/claude-plugin/` holds a
  generated mirror that must NOT be treated as a second source of truth.
- Out of scope areas: Product Context, screenshots, figma.com URLs, `specs/`, `export/`,
  `benchmark/reports/`, `claude-plugin/`.

## 14. CROSS-REFERENCE STATUS
<!-- MACHINE-OWNED: START -->
[Alignment checks completed across core and overlay protocols]

| Protocol | Level | Status | Iteration | Notes |
|----------|-------|--------|-----------|-------|
| `spec_code` | core | [pending/pass/partial/fail/blocked] | [N] | [details] |
| `checklist_evidence` | core | [pending/pass/partial/fail/blocked] | [N] | [details] |
| `skill_agent` | overlay | [pending/pass/partial/fail/blocked/notApplicable] | [N] | [details] |
| `agent_cross_runtime` | overlay | [pending/pass/partial/fail/blocked/notApplicable] | [N] | [details] |
| `feature_catalog_code` | overlay | [pending/pass/partial/fail/blocked/notApplicable] | [N] | [details] |
| `playbook_capability` | overlay | [pending/pass/partial/fail/blocked/notApplicable] | [N] | [details] |
<!-- MACHINE-OWNED: END -->

## 15. FILES UNDER REVIEW
<!-- MACHINE-OWNED: START -->
[Per-file coverage state table -- populated during initialization from scope discovery]

| File | Dimensions Reviewed | Last Iteration | Findings | Status |
|------|-------------------|----------------|----------|--------|
| `AI Systems/Product Owner/mcp-figma/SKILL.md` | [D1, D3] | [1] | [0 P0, 1 P1, 0 P2] | partial |
| `AI Systems/Product Owner/mcp-figma/README.md` | [D1, D3] | [1] | [0 P0, 0 P1, 1 P2] | partial |
| `AI Systems/Product Owner/mcp-figma/INSTALL-GUIDE.md` | [D1, D3] | [1] | [0 P0, 0 P1, 1 P2] | partial |
| `AI Systems/Product Owner/mcp-figma/references/tool-surface.md` | [D1] | [1] | [0 P0, 1 P1, 0 P2] | partial |
| `AI Systems/Product Owner/mcp-figma/scripts/_common.sh` | [D1] | [1] | [0 P0, 1 P1, 0 P2] | partial |
| `AI Systems/Product Owner/vendor.json` | [D1] | [1] | [0 P0, 0 P1, 0 P2] | complete |
| `AI Systems/Product Owner/scripts/vendor-sync.py` | [D1] | [1] | [0 P0, 0 P1, 1 P2] | partial |
<!-- MACHINE-OWNED: END -->

## 16. REVIEW BOUNDARIES
<!-- MACHINE-OWNED: START -->
- Max iterations: 5
- Convergence threshold: 0.1
- Rolling STOP threshold: 0.08
- No-progress threshold: 0.05
- Coverage stabilization passes required: 1
- Session lineage: sessionId=fanout-deepseek-1792580474713-m4jej7, parentSessionId=null, generation=1, lineageMode=new
- Findings registry: `deep-review-findings-registry.json`
- Release-readiness states: in-progress | converged | release-blocking
- Per-iteration budget: 12 tool calls, 10 minutes
- Severity threshold: P2
- Review target type: spec-folder (staging binding; the reviewed files are the Product Owner surfaces)
- Cross-reference checks: core=[spec_code, checklist_evidence], overlay=[skill_agent, agent_cross_runtime, feature_catalog_code, playbook_capability]
- Started: 2026-10-21T11:05:54.000Z
<!-- MACHINE-OWNED: END -->
