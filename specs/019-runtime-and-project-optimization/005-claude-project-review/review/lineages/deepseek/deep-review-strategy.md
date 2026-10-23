# Deep Review Strategy - Product Owner Claude Project packaging

## 1. REVIEW CHARTER

- Target: the Product Owner claude.ai Project packaging under `AI Systems/Product Owner/claude project/` (kernel, 62 knowledge files, package README), read against the skill sources in `sk-product-owner/` and `sk-create-figjam/`.
- Anchor: `specs/z-staging-po-019r/spec.md` (review scope) and `specs/z-staging-po-019r/review/lineages/deepseek/steer.md` (lead rulings).
- Dimensions: correctness, security, traceability, maintainability.
- Stop conditions: 3 iterations (`stopPolicy: max-iterations`); convergence is telemetry only.
- Success criteria: every finding carries P0/P1/P2, a resolvable `[SOURCE: path:line]`, and the file a fix changes; questions the repository cannot settle are recorded as open questions, not facts.

## 2. TOPIC

Review: specs/z-staging-po-019r

<!-- ANCHOR:review-dimensions -->
## 3. REVIEW DIMENSIONS (remaining)
- [ ] security

<!-- /ANCHOR:review-dimensions -->
## 4. NON-GOALS

- `AI Systems/Product Owner/specs/`, `export/`, `benchmark/reports/`, `claude-plugin/` are out of scope.
- `AI Systems/Product Context`, any screenshot and any `figma.com` URL are never opened.
- No fix is implemented; the review is read-only and reports findings only.

## 5. STOP CONDITIONS

- Three executed iterations, then synthesis, with `stopReason: maxIterationsReached`.
- A blocker that stops an iteration from producing markdown plus a delta.

<!-- ANCHOR:completed-dimensions -->
## 4. COMPLETED DIMENSIONS
- [x] correctness
- [x] traceability
- [x] maintainability

<!-- /ANCHOR:completed-dimensions -->
<!-- ANCHOR:running-findings -->
## 5. RUNNING FINDINGS
- P0 (Blockers): 0
- P1 (Required): 6
- P2 (Suggestions): 7
- Resolved: 0

<!-- /ANCHOR:running-findings -->
## 8. WHAT WORKED
- **Sentence-level rule-loss audit** — deleting each removed kernel sentence against the union of the kernel and all 62 knowledge files proved the 2026-10-21 dedupe lost no rule, and turned a suspected P0 into a recorded negative (iteration 1).
- **Benchmark-shaped comparison** — reading the Media Editor guide's five parts (surface table, install, enable, check, troubleshoot) against the package made the missing setup path a concrete per-part finding instead of a general "docs are thin" claim (iteration 2).
- **Parameter-by-parameter evidence table** — tabulating each assumed connector field against `mcp-click-up/` and `mcp-figma/` separated the values that are backed from the surface that is not (iteration 3).

## 9. WHAT FAILED
- **Reading the reducers as proof** — the first gateway call was recorded against the repository root because the run directory was taken from the shell's working directory instead of the workflow's relative path. The mistake was caught by the projection, disclosed in iteration 1, and the record was re-appended in the lineage. Write the run directory as the workflow writes it, never from `pwd`.
- **Seeding the coverage graph** — `upsert.cjs` writes the shared graph outside the lineage directory, so graph convergence stayed at zero. The cost is a missing signal, not a missing review.

<!-- ANCHOR:exhausted-approaches -->
## 9. EXHAUSTED APPROACHES (do not retry)
### **"The benchmark's advise-only row applies to the Product Owner Project."** `[SOURCE: AI Systems/Media Editor/USER-GUIDE.md:27]` says a claude.ai browser or mobile user gets advice only, because the Media Editor runtime runs on the user's computer. The Product Owner's two connectors are account-level and the repository records no such local requirement, so the Media Editor row is not evidence that claude.ai web lacks the Product Owner connectors. No finding either way; see Open Questions. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: **"The benchmark's advise-only row applies to the Product Owner Project."** `[SOURCE: AI Systems/Media Editor/USER-GUIDE.md:27]` says a claude.ai browser or mobile user gets advice only, because the Media Editor runtime runs on the user's computer. The Product Owner's two connectors are account-level and the repository records no such local requirement, so the Media Editor row is not evidence that claude.ai web lacks the Product Owner connectors. No finding either way; see Open Questions.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **"The benchmark's advise-only row applies to the Product Owner Project."** `[SOURCE: AI Systems/Media Editor/USER-GUIDE.md:27]` says a claude.ai browser or mobile user gets advice only, because the Media Editor runtime runs on the user's computer. The Product Owner's two connectors are account-level and the repository records no such local requirement, so the Media Editor row is not evidence that claude.ai web lacks the Product Owner connectors. No finding either way; see Open Questions.

### **"The kernel's connector text is wrong."** `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:243]` to `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:249]` describes parameters and the approval gate, not setup, and iteration 3 tests whether those parameters are evidenced. No setup finding lands on the kernel. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: **"The kernel's connector text is wrong."** `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:243]` to `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:249]` describes parameters and the approval gate, not setup, and iteration 3 tests whether those parameters are evidenced. No setup finding lands on the kernel.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **"The kernel's connector text is wrong."** `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:243]` to `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:249]` describes parameters and the approval gate, not setup, and iteration 3 tests whether those parameters are evidenced. No setup finding lands on the kernel.

### **"The smoke matrix is the setup test."** It was read in full (`claude project/README.md:138-173`): every bullet tests routing, format or delivery wording. No bullet tests that a connector answers. No finding about coverage of the matrix itself beyond R2-P2-001. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: **"The smoke matrix is the setup test."** It was read in full (`claude project/README.md:138-173`): every bullet tests routing, format or delivery wording. No bullet tests that a connector answers. No finding about coverage of the matrix itself beyond R2-P2-001.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **"The smoke matrix is the setup test."** It was read in full (`claude project/README.md:138-173`): every bullet tests routing, format or delivery wording. No bullet tests that a connector answers. No finding about coverage of the matrix itself beyond R2-P2-001.

### **`clickup_create_task` with `markdown_description`** — searched for a contrary parameter name. `[SOURCE: AI Systems/Product Owner/mcp-click-up/SKILL.md:24]` says the server has no `markdown_content` or plain `description` parameter, so the kernel's choice is the documented one. No finding beyond the surface caveat. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: **`clickup_create_task` with `markdown_description`** — searched for a contrary parameter name. `[SOURCE: AI Systems/Product Owner/mcp-click-up/SKILL.md:24]` says the server has no `markdown_content` or plain `description` parameter, so the kernel's choice is the documented one. No finding beyond the surface caveat.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`clickup_create_task` with `markdown_description`** — searched for a contrary parameter name. `[SOURCE: AI Systems/Product Owner/mcp-click-up/SKILL.md:24]` says the server has no `markdown_content` or plain `description` parameter, so the kernel's choice is the documented one. No finding beyond the surface caveat.

### **`include_markdown_description=true`** — the older API form is documented as a raw-REST behaviour in `[SOURCE: AI Systems/Product Owner/mcp-click-up/SKILL.md:26]`; the kernel uses the MCP `include` array, which matches `[SOURCE: AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-high-priority/get-task.md:29]`. No finding. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: **`include_markdown_description=true`** — the older API form is documented as a raw-REST behaviour in `[SOURCE: AI Systems/Product Owner/mcp-click-up/SKILL.md:26]`; the kernel uses the MCP `include` array, which matches `[SOURCE: AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-high-priority/get-task.md:29]`. No finding.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`include_markdown_description=true`** — the older API form is documented as a raw-REST behaviour in `[SOURCE: AI Systems/Product Owner/mcp-click-up/SKILL.md:26]`; the kernel uses the MCP `include` array, which matches `[SOURCE: AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-high-priority/get-task.md:29]`. No finding.

### **`visibility: "PRIVATE"`** — valid per `[SOURCE: AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-medium-priority/create-document.md:30]`. No finding. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: **`visibility: "PRIVATE"`** — valid per `[SOURCE: AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-medium-priority/create-document.md:30]`. No finding.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`visibility: "PRIVATE"`** — valid per `[SOURCE: AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-medium-priority/create-document.md:30]`. No finding.

### **A deleted rule in the 2026-10-21 cut.** Every deleted sentence was matched against the current kernel plus all knowledge files; the survivors are reformulations (above). No finding. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: **A deleted rule in the 2026-10-21 cut.** Every deleted sentence was matched against the current kernel plus all knowledge files; the survivors are reformulations (above). No finding.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **A deleted rule in the 2026-10-21 cut.** Every deleted sentence was matched against the current kernel plus all knowledge files; the survivors are reformulations (above). No finding.

### **A Figma connector documented in `mcp-figma/`** — the packet has an `INSTALL-GUIDE.md`, an MCP section and a `references/` tree, all CLI. Searched for `generate_diagram`, `get_figjam`, `get_screenshot`, `whoami` and "connector": zero matches. No finding beyond R3-P1-002. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: **A Figma connector documented in `mcp-figma/`** — the packet has an `INSTALL-GUIDE.md`, an MCP section and a `references/` tree, all CLI. Searched for `generate_diagram`, `get_figjam`, `get_screenshot`, `whoami` and "connector": zero matches. No finding beyond R3-P1-002.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **A Figma connector documented in `mcp-figma/`** — the packet has an `INSTALL-GUIDE.md`, an MCP section and a `references/` tree, all CLI. Searched for `generate_diagram`, `get_figjam`, `get_screenshot`, `whoami` and "connector": zero matches. No finding beyond R3-P1-002.

### **Example count of 28.** Counted the knowledge directory: 5 Task, 4 Bug, 7 Doc, 5 Story, 7 Flow. The kernel's "twenty-eight" is correct; only the README bullet is stale (R1-P2-002). -- BLOCKED (iteration 1, 1 attempts)
- What was tried: **Example count of 28.** Counted the knowledge directory: 5 Task, 4 Bug, 7 Doc, 5 Story, 7 Flow. The kernel's "twenty-eight" is correct; only the README bullet is stale (R1-P2-002).
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Example count of 28.** Counted the knowledge directory: 5 Task, 4 Bug, 7 Doc, 5 Story, 7 Flow. The kernel's "twenty-eight" is correct; only the README bullet is stale (R1-P2-002).

### **Story versus Epic shape drift.** The kernel's Story paragraph (`Custom Instructions.md:159`) and Template - Story Mode now agree that a Story opens on `## Problem` and an Epic on `## About`; checked against `sk-create-figjam` and `sk-product-owner` sources. No finding. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: **Story versus Epic shape drift.** The kernel's Story paragraph (`Custom Instructions.md:159`) and Template - Story Mode now agree that a Story opens on `## Problem` and an Epic on `## About`; checked against `sk-create-figjam` and `sk-product-owner` sources. No finding.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Story versus Epic shape drift.** The kernel's Story paragraph (`Custom Instructions.md:159`) and Template - Story Mode now agree that a Story opens on `## Problem` and an Epic on `## About`; checked against `sk-create-figjam` and `sk-product-owner` sources. No finding.

### **The four shared rule files drill.** `[SOURCE: AI Systems/Product Owner/claude project/README.md:107]` declares the four shared rule files byte copies of their cards in the shared knowledge folder, so their Project-side filesystem wording is the declared state, not drift. No finding. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: **The four shared rule files drill.** `[SOURCE: AI Systems/Product Owner/claude project/README.md:107]` declares the four shared rule files byte copies of their cards in the shared knowledge folder, so their Project-side filesystem wording is the declared state, not drift. No finding.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **The four shared rule files drill.** `[SOURCE: AI Systems/Product Owner/claude project/README.md:107]` declares the four shared rule files byte copies of their cards in the shared knowledge folder, so their Project-side filesystem wording is the declared state, not drift. No finding.

<!-- /ANCHOR:exhausted-approaches -->
## 10A. SATURATED / SWEPT DIMENSIONS AND EXPANSION FRONTIER
- Completed pivots: 0
- Failed pivots: 0
- Audited overrides: 0
- Swept: none yet
- Pivot lineage: none yet
- Remaining frontier: none recorded

## 11. RULED OUT DIRECTIONS
[Review angles that were investigated and definitively eliminated -- consolidated from iteration dead-end data]

<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
security

<!-- /ANCHOR:next-focus -->
## 13. KNOWN CONTEXT

### Bounded Context Snapshot

- Target pointers: `AI Systems/Product Owner/claude project/Custom Instructions.md` (906 lines, H1 v1.2.2), `claude project/knowledge/` (62 files), `claude project/README.md`, `AI Systems/Product Owner/README.md`, `AI Systems/Product Owner/SYNC.md`.
- Claimed behavior to verify: kernel and each knowledge file hold the same decision rules as their `sk-product-owner/` and `sk-create-figjam/` sources; the 2026-10-21 kernel cut moved eight duplicated rules into one place without losing one; a Project user is told how to connect ClickUp and Figma and check them; connector tool names and parameters the package assumes are backed by `mcp-click-up/` and `mcp-figma/`.
- Reuse and conventions: the manual parity method in `SYNC.md` Sections 1-4; the source-to-mirror map in `claude project/README.md`.
- Review risks and gaps: the live claude.ai Project is not readable from the repository, so connector capability questions that the vendored packets cannot settle are open questions. `resource-map.md` is absent, so the coverage gate is skipped. Step `step_seed_coverage_graph` was not run because `upsert.cjs` writes outside this lineage's artifact directory; iteration records therefore omit `graphEvents`.

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

| File | Dimensions Reviewed | Last Iteration | Findings | Status |
|------|-------------------|----------------|----------|--------|
| `AI Systems/Product Owner/claude project/Custom Instructions.md` | pending | - | - | pending |
| `AI Systems/Product Owner/claude project/knowledge/` | pending | - | - | pending |
| `AI Systems/Product Owner/claude project/README.md` | pending | - | - | pending |
| `AI Systems/Product Owner/README.md` | pending | - | - | pending |
| `AI Systems/Product Owner/SYNC.md` | pending | - | - | pending |
| `AI Systems/Media Editor/USER-GUIDE.md` | pending | - | - | pending |
| `AI Systems/Product Owner/mcp-click-up/` | pending | - | - | pending |
| `AI Systems/Product Owner/mcp-figma/` | pending | - | - | pending |
<!-- MACHINE-OWNED: END -->

## 16. REVIEW BOUNDARIES
<!-- MACHINE-OWNED: START -->
- Max iterations: 3
- Convergence threshold: 0.1
- Rolling STOP threshold: 0.08
- No-progress threshold: 0.05
- Coverage stabilization passes required: 1
- Session lineage: sessionId=fanout-deepseek-1792598333413-h7kxu3, parentSessionId=null, generation=1, lineageMode=new
- Findings registry: `deep-review-findings-registry.json`
- Release-readiness states: in-progress | converged | release-blocking
- Per-iteration budget: 12 tool calls, 10 minutes
- Severity threshold: P2
- Review target type: spec-folder
- Cross-reference checks: core=[spec_code, checklist_evidence], overlay=[skill_agent, agent_cross_runtime, feature_catalog_code, playbook_capability]
- Started: 2026-10-21T16:04:17Z
<!-- MACHINE-OWNED: END -->
