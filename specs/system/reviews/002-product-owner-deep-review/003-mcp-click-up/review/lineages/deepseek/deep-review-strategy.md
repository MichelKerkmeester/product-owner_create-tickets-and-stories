# Deep Review Strategy - Product Owner mcp-click-up

## 1. REVIEW CHARTER

- Target: Product Owner vendored ClickUp packet (`AI Systems/Product Owner/mcp-click-up/`), its manifest `AI Systems/Product Owner/vendor.json`, its sync tool `AI Systems/Product Owner/scripts/vendor-sync.py`, and the hub surfaces that route to and hand off through it (`SKILL.md`, `ROUTER.md`, `hub-router.json`, `mode-registry.json`, `leaf-manifest.json`, `AGENTS.md`, `sk-product-owner/SKILL.md`).
- Dimensions: correctness, contract consistency (traceability), references and paths, maintainability.
- Stop conditions: `max-iterations` policy; this lineage runs the full 5-iteration cap and records convergence as telemetry only.
- Success criteria: no active P0; every finding carries `[SOURCE: path:line]` plus the file a fix changes; no dimension left uncovered.

## 2. TOPIC

Read-only audit of a byte-copied upstream skill (`.skilled/skills/mcp-tooling/mcp-click-up`) as it is vendored into Product Owner, of the manifest that pins it, of the sync tool that moves changes both ways, and of how the Product Owner hub and `sk-product-owner` use it for routing, push targets and the ClickUp handoff. The vendored packet is never edited in Product Owner, so every finding inside it names the upstream file as the fix site.

<!-- ANCHOR:review-dimensions -->
## 3. REVIEW DIMENSIONS (remaining)
[All dimensions complete]

<!-- /ANCHOR:review-dimensions -->
## 4. NON-GOALS

- Re-deriving ClickUp server behaviour. The packet's tool inventory was captured live; this review checks internal consistency and consistency with the hub, not the live server.
- Reviewing `export/`, `benchmark/reports/`, `specs/` or `claude-plugin/` run output.
- Implementation. No fix is applied during review; findings name the fix site only.

## 5. STOP CONDITIONS

- The 5-iteration cap (`stopPolicy: max-iterations`); convergence signals are telemetry inside this lineage.
- An active P0 would force `FAIL` and block release regardless of iteration count.

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
- P1 (Required): 4
- P2 (Suggestions): 12
- Resolved: 0

<!-- /ANCHOR:running-findings -->
## 8. WHAT WORKED
- Running the sync tool's own `status` and a byte-level `diff -rq` before reading its code: drift was ruled out with evidence in one call, so the iteration could spend its budget on failure modes instead of on the drift hypothesis (iteration 1).
- Reconciling every manifest entry against the on-disk tree in both directions: it turned "the manifest looks complete" into a counted 178/178 result (iteration 1).
- Counting the packet's own claims (50 cupt features, 61 MCP tools) against the tree: cheap, and it either confirms a claim or finds an inflated one (iteration 1).

## 9. WHAT FAILED
- Trying to prove the vendored packet's upstream-relative install paths are broken from Product Owner: `AI Systems/Product Owner/.skilled` is a symlink to the shared skill folder, so `.skilled/skills/mcp-tooling/mcp-click-up/scripts/install.sh` resolves locally. The hypothesis was dropped rather than written up (iteration 1).

<!-- ANCHOR:exhausted-approaches -->
## 9. EXHAUSTED APPROACHES (do not retry)
### "`doctor.sh` prints secrets": it prints no credential value. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: "`doctor.sh` prints secrets": it prints no credential value.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "`doctor.sh` prints secrets": it prints no credential value.

### "`vendor.json` is incomplete or carries stale entries": file-by-file reconciliation showed 178/178 in both directions. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: "`vendor.json` is incomplete or carries stale entries": file-by-file reconciliation showed 178/178 in both directions.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "`vendor.json` is incomplete or carries stale entries": file-by-file reconciliation showed 178/178 in both directions.

### "A reference file carries a stale version of the packet release": each sub-document carries its own version and only `INSTALL-GUIDE.md` states two for itself. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: "A reference file carries a stale version of the packet release": each sub-document carries its own version and only `INSTALL-GUIDE.md` states two for itself.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "A reference file carries a stale version of the packet release": each sub-document carries its own version and only `INSTALL-GUIDE.md` states two for itself.

### "Placeholder targets in the example artifacts are defects": they are `{figma-url}`-style samples by design. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: "Placeholder targets in the example artifacts are defects": they are `{figma-url}`-style samples by design.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "Placeholder targets in the example artifacts are defects": they are `{figma-url}`-style samples by design.

### "Push-target names drifted between the skill, the env example and the reply templates": they match exactly. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: "Push-target names drifted between the skill, the env example and the reply templates": they match exactly.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "Push-target names drifted between the skill, the env example and the reply templates": they match exactly.

### "The drift gate does not exist": `benchmark/gates/run_gates.sh:47` runs `vendor-sync.py status`. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: "The drift gate does not exist": `benchmark/gates/run_gates.sh:47` runs `vendor-sync.py status`.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "The drift gate does not exist": `benchmark/gates/run_gates.sh:47` runs `vendor-sync.py status`.

### "The example queue scripts are command-injection sinks for task names": ids and names are read into arrays and passed quoted; no `eval`, `xargs` or `sh -c` exists in either script. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: "The example queue scripts are command-injection sinks for task names": ids and names are read into arrays and passed quoted; no `eval`, `xargs` or `sh -c` exists in either script.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "The example queue scripts are command-injection sinks for task names": ids and names are read into arrays and passed quoted; no `eval`, `xargs` or `sh -c` exists in either script.

### "The four hub documents carry different versions": all read 1.0.0.0. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: "The four hub documents carry different versions": all read 1.0.0.0.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "The four hub documents carry different versions": all read 1.0.0.0.

### "The hub and the packet disagree about how to reach ClickUp in markdown": all three transport sites agree. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: "The hub and the packet disagree about how to reach ClickUp in markdown": all three transport sites agree.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "The hub and the packet disagree about how to reach ClickUp in markdown": all three transport sites agree.

### "The hub has no version discipline": all four hub documents read 1.0.0.0, as its own version-authority paragraph requires. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: "The hub has no version discipline": all four hub documents read 1.0.0.0, as its own version-authority paragraph requires.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "The hub has no version discipline": all four hub documents read 1.0.0.0, as its own version-authority paragraph requires.

### "The hub's links into the packet are broken": every non-placeholder link resolves. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: "The hub's links into the packet are broken": every non-placeholder link resolves.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "The hub's links into the packet are broken": every non-placeholder link resolves.

### "The install scripts modify MCP or editor configuration": they print snippets only (`install.sh:5`, `scripts/README.md:13`). -- BLOCKED (iteration 2, 1 attempts)
- What was tried: "The install scripts modify MCP or editor configuration": they print snippets only (`install.sh:5`, `scripts/README.md:13`).
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "The install scripts modify MCP or editor configuration": they print snippets only (`install.sh:5`, `scripts/README.md:13`).

### "The installer ignores the shipped `requirements.txt` floor, so installs drift": the split is documented on purpose (`mcp-servers/clickup-cli/README.md:37`), so the unpinned install is intended behaviour for the embedded path; only the `mcp-remote` bridge is unpinned without such a note. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: "The installer ignores the shipped `requirements.txt` floor, so installs drift": the split is documented on purpose (`mcp-servers/clickup-cli/README.md:37`), so the unpinned install is intended behaviour for the embedded path; only the `mcp-remote` bridge is unpinned without such a note.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "The installer ignores the shipped `requirements.txt` floor, so installs drift": the split is documented on purpose (`mcp-servers/clickup-cli/README.md:37`), so the unpinned install is intended behaviour for the embedded path; only the `mcp-remote` bridge is unpinned without such a note.

### "The packet is an unmaintained fork": it is a byte copy with a manifest, a gate and a test suite. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: "The packet is an unmaintained fork": it is a byte copy with a manifest, a gate and a test suite.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "The packet is an unmaintained fork": it is a byte copy with a manifest, a gate and a test suite.

### "The packet's feature counts are inflated": counts reconcile exactly to the tree. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: "The packet's feature counts are inflated": counts reconcile exactly to the tree.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "The packet's feature counts are inflated": counts reconcile exactly to the tree.

### "The packet's relative links are broken after vendoring": 0 broken links in 171 files. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: "The packet's relative links are broken after vendoring": 0 broken links in 171 files.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "The packet's relative links are broken after vendoring": 0 broken links in 171 files.

### "The repo-local `.skilled` symlink redirects the upstream to a different tree": both links resolve to the same target directory. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: "The repo-local `.skilled` symlink redirects the upstream to a different tree": both links resolve to the same target directory.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "The repo-local `.skilled` symlink redirects the upstream to a different tree": both links resolve to the same target directory.

### "The two manual-testing-playbooks duplicate each other": the hub playbook states the split, and the hub file set is 8 files against the packet's 43. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: "The two manual-testing-playbooks duplicate each other": the hub playbook states the split, and the hub file set is 8 files against the packet's 43.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "The two manual-testing-playbooks duplicate each other": the hub playbook states the split, and the hub file set is 8 files against the packet's 43.

### "The vendored packet has silently drifted": `diff -rq` and `vendor-sync.py status` both show byte-identity, so no drift finding was recorded. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: "The vendored packet has silently drifted": `diff -rq` and `vendor-sync.py status` both show byte-identity, so no drift finding was recorded.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: "The vendored packet has silently drifted": `diff -rq` and `vendor-sync.py status` both show byte-identity, so no drift finding was recorded.

### `Core: checklist_evidence` — no checklist exists in the staging wrapper; the four prior iterations' evidence lines were re-opened where this iteration depends on them (`AGENTS.md:117`, `sk-product-owner/SKILL.md:283`, `SKILL.md:105`, `FEATURE-CATALOG.md:17`). Status: pass. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: `Core: checklist_evidence` — no checklist exists in the staging wrapper; the four prior iterations' evidence lines were re-opened where this iteration depends on them (`AGENTS.md:117`, `sk-product-owner/SKILL.md:283`, `SKILL.md:105`, `FEATURE-CATALOG.md:17`). Status: pass.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Core: checklist_evidence` — no checklist exists in the staging wrapper; the four prior iterations' evidence lines were re-opened where this iteration depends on them (`AGENTS.md:117`, `sk-product-owner/SKILL.md:283`, `SKILL.md:105`, `FEATURE-CATALOG.md:17`). Status: pass.

### `Core: checklist_evidence` — no checklist exists in the staging wrapper; the review rulings in `steer.md:1-11` were applied, including "every finding inside mcp-click-up/ names the upstream file as the fix site" (both packet-side findings here are named that way). Status: pass. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: `Core: checklist_evidence` — no checklist exists in the staging wrapper; the review rulings in `steer.md:1-11` were applied, including "every finding inside mcp-click-up/ names the upstream file as the fix site" (both packet-side findings here are named that way). Status: pass.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Core: checklist_evidence` — no checklist exists in the staging wrapper; the review rulings in `steer.md:1-11` were applied, including "every finding inside mcp-click-up/ names the upstream file as the fix site" (both packet-side findings here are named that way). Status: pass.

### `Core: checklist_evidence` — no checklist exists in the staging wrapper; the steer file's security-relevant rulings (read-only, never open Product Context or screenshots) were followed. Status: pass. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: `Core: checklist_evidence` — no checklist exists in the staging wrapper; the steer file's security-relevant rulings (read-only, never open Product Context or screenshots) were followed. Status: pass.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Core: checklist_evidence` — no checklist exists in the staging wrapper; the steer file's security-relevant rulings (read-only, never open Product Context or screenshots) were followed. Status: pass.

### `Core: checklist_evidence` — no checklist exists in the staging wrapper; the steer's citation rule 5 ("a repository-relative path that resolves") was applied to every finding and every `[SOURCE:]`-style path in this narrative. Status: pass. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: `Core: checklist_evidence` — no checklist exists in the staging wrapper; the steer's citation rule 5 ("a repository-relative path that resolves") was applied to every finding and every `[SOURCE:]`-style path in this narrative. Status: pass.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Core: checklist_evidence` — no checklist exists in the staging wrapper; the steer's citation rule 5 ("a repository-relative path that resolves") was applied to every finding and every `[SOURCE:]`-style path in this narrative. Status: pass.

### `Core: checklist_evidence` — the staging spec folder carries no `checklist.md` or `implementation-summary.md` (read-only review wrapper); the acceptance evidence for this iteration is the spec's own scope table plus the steer file's review rulings. Status: notApplicable for the missing checklist, pass for the scope table as the governing evidence. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: `Core: checklist_evidence` — the staging spec folder carries no `checklist.md` or `implementation-summary.md` (read-only review wrapper); the acceptance evidence for this iteration is the spec's own scope table plus the steer file's review rulings. Status: notApplicable for the missing checklist, pass for the scope table as the governing evidence.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Core: checklist_evidence` — the staging spec folder carries no `checklist.md` or `implementation-summary.md` (read-only review wrapper); the acceptance evidence for this iteration is the spec's own scope table plus the steer file's review rulings. Status: notApplicable for the missing checklist, pass for the scope table as the governing evidence.

### `Core: spec_code` — the security dimension read every executable file under `mcp-click-up/scripts/`, `mcp-click-up/mcp-servers/`, and `mcp-click-up/examples/`, which is the whole shell surface of the packet the spec names. Status: pass. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: `Core: spec_code` — the security dimension read every executable file under `mcp-click-up/scripts/`, `mcp-click-up/mcp-servers/`, and `mcp-click-up/examples/`, which is the whole shell surface of the packet the spec names. Status: pass.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Core: spec_code` — the security dimension read every executable file under `mcp-click-up/scripts/`, `mcp-click-up/mcp-servers/`, and `mcp-click-up/examples/`, which is the whole shell surface of the packet the spec names. Status: pass.

### `Core: spec_code` — the spec names a byte-copied packet; a packet may not be corrected here, so each finding above names the upstream file as the fix site, per the steer's rule 3. Status: pass. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: `Core: spec_code` — the spec names a byte-copied packet; a packet may not be corrected here, so each finding above names the upstream file as the fix site, per the steer's rule 3. Status: pass.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Core: spec_code` — the spec names a byte-copied packet; a packet may not be corrected here, so each finding above names the upstream file as the fix site, per the steer's rule 3. Status: pass.

### `Core: spec_code` — the spec's three entries plus the steer's named hub surfaces (routing, push targets, ClickUp handoff) were read; the two P1s sit exactly on those surfaces. Status: pass. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: `Core: spec_code` — the spec's three entries plus the steer's named hub surfaces (routing, push targets, ClickUp handoff) were read; the two P1s sit exactly on those surfaces. Status: pass.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Core: spec_code` — the spec's three entries plus the steer's named hub surfaces (routing, push targets, ClickUp handoff) were read; the two P1s sit exactly on those surfaces. Status: pass.

### `Core: spec_code` — the staging spec names three in-scope entries (`mcp-click-up/`, `vendor.json`, `scripts/vendor-sync.py`). All three were opened and read; the manifest was additionally reconciled against both trees. Status: pass for the three named entries. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: `Core: spec_code` — the staging spec names three in-scope entries (`mcp-click-up/`, `vendor.json`, `scripts/vendor-sync.py`). All three were opened and read; the manifest was additionally reconciled against both trees. Status: pass for the three named entries.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Core: spec_code` — the staging spec names three in-scope entries (`mcp-click-up/`, `vendor.json`, `scripts/vendor-sync.py`). All three were opened and read; the manifest was additionally reconciled against both trees. Status: pass for the three named entries.

### `Core: spec_code` — the staging spec's three named entries and the steer's focus list were re-read against the four earlier iterations' findings; every finding names a fix site in the file its steer rule requires. Status: pass. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: `Core: spec_code` — the staging spec's three named entries and the steer's focus list were re-read against the four earlier iterations' findings; every finding names a fix site in the file its steer rule requires. Status: pass.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Core: spec_code` — the staging spec's three named entries and the steer's focus list were re-read against the four earlier iterations' findings; every finding names a fix site in the file its steer rule requires. Status: pass.

### `Overlay: agent_cross_runtime` — `AGENTS.md` is the only runtime bootstrap in this repository and it agrees with `SKILL.md` on routing. Status: pass, with the handoff finding above. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: `Overlay: agent_cross_runtime` — `AGENTS.md` is the only runtime bootstrap in this repository and it agrees with `SKILL.md` on routing. Status: pass, with the handoff finding above.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Overlay: agent_cross_runtime` — `AGENTS.md` is the only runtime bootstrap in this repository and it agrees with `SKILL.md` on routing. Status: pass, with the handoff finding above.

### `Overlay: feature_catalog_code` — the catalog reconciliation stands at 50 cupt cards and 61 MCP tool cards; the unresolved part is the claim layer, not the counts. Status: partial, carried from iteration 4. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: `Overlay: feature_catalog_code` — the catalog reconciliation stands at 50 cupt cards and 61 MCP tool cards; the unresolved part is the claim layer, not the counts. Status: partial, carried from iteration 4.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Overlay: feature_catalog_code` — the catalog reconciliation stands at 50 cupt cards and 61 MCP tool cards; the unresolved part is the claim layer, not the counts. Status: partial, carried from iteration 4.

### `Overlay: feature_catalog_code` — the catalog's counts still reconcile to the tree (50 cupt cards, 61 MCP tool cards), and the only catalog contradiction is the `--json`/`add` claim recorded above. Status: partial. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: `Overlay: feature_catalog_code` — the catalog's counts still reconcile to the tree (50 cupt cards, 61 MCP tool cards), and the only catalog contradiction is the `--json`/`add` claim recorded above. Status: partial.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Overlay: feature_catalog_code` — the catalog's counts still reconcile to the tree (50 cupt cards, 61 MCP tool cards), and the only catalog contradiction is the `--json`/`add` claim recorded above. Status: partial.

### `Overlay: feature_catalog_code` — the packet's feature catalog counts were reconciled against the tree: 50 `cupt-*` feature cards across 10 areas and 61 `mcp-*` cards, matching `feature-catalog/FEATURE-CATALOG.md:17` and `references/mcp-tools.md:74` (61 tools, plus 61 unique tool rows in section 5). Status: pass. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: `Overlay: feature_catalog_code` — the packet's feature catalog counts were reconciled against the tree: 50 `cupt-*` feature cards across 10 areas and 61 `mcp-*` cards, matching `feature-catalog/FEATURE-CATALOG.md:17` and `references/mcp-tools.md:74` (61 tools, plus 61 unique tool rows in section 5). Status: pass.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Overlay: feature_catalog_code` — the packet's feature catalog counts were reconciled against the tree: 50 `cupt-*` feature cards across 10 areas and 61 `mcp-*` cards, matching `feature-catalog/FEATURE-CATALOG.md:17` and `references/mcp-tools.md:74` (61 tools, plus 61 unique tool rows in section 5). Status: pass.

### `Overlay: feature_catalog_code` — the two credential-bearing feature cards (`cupt-authentication/direct-token.md`, `cupt-authentication/interactive-auth.md`) were read against the guide: the guide's two options match the two cards. Status: pass with the hygiene gap recorded above. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: `Overlay: feature_catalog_code` — the two credential-bearing feature cards (`cupt-authentication/direct-token.md`, `cupt-authentication/interactive-auth.md`) were read against the guide: the guide's two options match the two cards. Status: pass with the hygiene gap recorded above.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Overlay: feature_catalog_code` — the two credential-bearing feature cards (`cupt-authentication/direct-token.md`, `cupt-authentication/interactive-auth.md`) were read against the guide: the guide's two options match the two cards. Status: pass with the hygiene gap recorded above.

### `Overlay: playbook_capability` — the hub-level playbook states that "each vendored packet owns its own" playbook (`Product Owner/manual-testing-playbook/manual-testing-playbook.md:11`), so the two playbooks are a documented split rather than duplication. Status: pass. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: `Overlay: playbook_capability` — the hub-level playbook states that "each vendored packet owns its own" playbook (`Product Owner/manual-testing-playbook/manual-testing-playbook.md:11`), so the two playbooks are a documented split rather than duplication. Status: pass.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Overlay: playbook_capability` — the hub-level playbook states that "each vendored packet owns its own" playbook (`Product Owner/manual-testing-playbook/manual-testing-playbook.md:11`), so the two playbooks are a documented split rather than duplication. Status: pass.

### `Overlay: playbook_capability` — the manual-testing-playbook's own cross-links resolve, and its recovery scenario for missing auth exercises the documented `cupt config --api-token` path consistently. Status: pass. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: `Overlay: playbook_capability` — the manual-testing-playbook's own cross-links resolve, and its recovery scenario for missing auth exercises the documented `cupt config --api-token` path consistently. Status: pass.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Overlay: playbook_capability` — the manual-testing-playbook's own cross-links resolve, and its recovery scenario for missing auth exercises the documented `cupt config --api-token` path consistently. Status: pass.

### `Overlay: playbook_capability`, `Overlay: skill_agent`, `Overlay: agent_cross_runtime` — deferred to iterations 3 and 5 (hub usage and structural sweep). -- BLOCKED (iteration 1, 1 attempts)
- What was tried: `Overlay: playbook_capability`, `Overlay: skill_agent`, `Overlay: agent_cross_runtime` — deferred to iterations 3 and 5 (hub usage and structural sweep).
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Overlay: playbook_capability`, `Overlay: skill_agent`, `Overlay: agent_cross_runtime` — deferred to iterations 3 and 5 (hub usage and structural sweep).

### `Overlay: skill_agent` — hub `SKILL.md` to packet `SKILL.md` handoff: `hub-router.json` declares `mcp-click-up/SKILL.md` as the mode resource, `SKILL.md:26` calls the packet "Vendored", and the packet's Section 2 owns the intra-packet routing. Status: pass. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: `Overlay: skill_agent` — hub `SKILL.md` to packet `SKILL.md` handoff: `hub-router.json` declares `mcp-click-up/SKILL.md` as the mode resource, `SKILL.md:26` calls the packet "Vendored", and the packet's Section 2 owns the intra-packet routing. Status: pass.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: `Overlay: skill_agent` — hub `SKILL.md` to packet `SKILL.md` handoff: `hub-router.json` declares `mcp-click-up/SKILL.md` as the mode resource, `SKILL.md:26` calls the packet "Vendored", and the packet's Section 2 owns the intra-packet routing. Status: pass.

<!-- /ANCHOR:exhausted-approaches -->
## 10A. SATURATED / SWEPT DIMENSIONS AND EXPANSION FRONTIER
- Completed pivots: 0
- Failed pivots: 0
- Audited overrides: 0
- Swept: none yet
- Pivot lineage: none yet
- Remaining frontier: none recorded

## 11. RULED OUT DIRECTIONS

- Vendor drift hypothesis: `vendor-sync.py status` reports mcp-click-up in step at `325ebb22`, 178 files; `diff -rq` against the upstream tree is empty and all 178 on-disk files match the manifest (iteration 1).
- Repo-local `.skilled` resolving to a different upstream tree: both Product Owner `.skilled` and the repository `.skilled` resolve to the same target, so `find_upstream_root` cannot pick a divergent tree here (iteration 1).
- Command injection through ClickUp task names in the two example scripts: ids and names land in arrays and are expanded quoted; no `eval`, `xargs` or `sh -c` exists (iteration 2).
- The packet's scripts modifying MCP or editor configuration: `install.sh` and `doctor.sh` print and report only (iteration 2).
- A destructive-command hazard: no `rm -rf` of an unvalidated variable exists anywhere in the packet's shell surface (iteration 2).

<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
[All dimensions covered]

<!-- /ANCHOR:next-focus -->
## 13. KNOWN CONTEXT

### Bounded Context Snapshot

- Target pointers: `AI Systems/Product Owner/mcp-click-up/**` (178 files), `vendor.json`, `scripts/vendor-sync.py`, `scripts/tests/test_vendor_sync.py`; hub surfaces `SKILL.md`, `ROUTER.md`, `hub-router.json`, `mode-registry.json`, `leaf-manifest.json`, `AGENTS.md`, `sk-product-owner/SKILL.md`.
- Behaviour claims to verify: byte-identity of the vendored copy; `vendor.json` hashes and `base_commit`; the hub's claim that `mcp-click-up` routes inside its own `SKILL.md`; `sk-product-owner` Section 7 push-target rules matching `AGENTS.md` and `.env.example`; leaf registration of the packet's resources.
- Reuse and conventions: Product Owner marks generated or vendored surfaces (`.skilled` symlink, `claude-plugin/`, `export/`) and expects the hub to own routing while the packet owns transport mechanics.
- Review risks and gaps: `.skilled` is a workspace symlink, so upstream-relative paths in the packet resolve locally but say nothing about a standalone clone; live ClickUp server behaviour is unverifiable from the repository; no `resource-map.md` exists in the staging spec folder, so the Resource Map Coverage Gate is skipped.

## 14. CROSS-REFERENCE STATUS
<!-- MACHINE-OWNED: START -->
| Protocol | Level | Status | Iteration | Notes |
|----------|-------|--------|-----------|-------|
| `spec_code` | core | pass | 1 | all three entries the spec names were read; manifest reconciled against both trees |
| `checklist_evidence` | core | pass | 1 | no checklist exists in the staging wrapper; the spec scope table is the governing evidence |
| `skill_agent` | overlay | pending | 1 | hub to packet routing is iteration 3 |
| `agent_cross_runtime` | overlay | pending | 1 | not yet attempted |
| `feature_catalog_code` | overlay | pass | 1 | 50 cupt cards across 10 areas, 61 MCP tool cards, both match the catalog and tool reference |
| `playbook_capability` | overlay | pending | 1 | deferred to the maintainability sweep |
<!-- MACHINE-OWNED: END -->

## 15. FILES UNDER REVIEW
<!-- MACHINE-OWNED: START -->
| File | Dimensions Reviewed | Last Iteration | Findings | Status |
|------|-------------------|----------------|----------|--------|
| `scripts/vendor-sync.py` | D1 | 1 | 0 P0, 0 P1, 2 P2 | complete |
| `vendor.json` | D1 | 1 | none (178/178 hashes match) | complete |
| `scripts/build-plugin.py` | D1 | 1 | 0 P0, 0 P1, 1 P2 | partial |
| `benchmark/gates/run_gates.sh` | D1 (context) | 1 | none | complete |
| `mcp-click-up/SKILL.md` | D1 (routing table, pseudocode) | 1 | none yet | partial |
| `mcp-click-up/references/cupt-commands.md` | D1 (command surface) | 1 | none | partial |
| `mcp-click-up/feature-catalog/FEATURE-CATALOG.md` | D1 (counts) | 1 | none | complete |
| `mcp-click-up/scripts/doctor.sh` | D2 | 2 | 0 P0, 1 P1, 0 P2 | complete |
| `mcp-click-up/scripts/install.sh` | D2 | 2 | 0 P0, 0 P1, 0 P2 (snippet pinning noted under R2-P2-002) | complete |
| `mcp-click-up/scripts/README.md` | D2 | 2 | 0 P0, 1 P1, 0 P2 (same finding) | complete |
| `mcp-click-up/mcp-servers/clickup-cli/` | D2 | 2 | none | complete |
| `mcp-click-up/examples/*.sh` | D2 | 2 | none | complete |
| `mcp-click-up/INSTALL-GUIDE.md` | D2 | 2 | 0 P0, 0 P1, 1 P2 | complete |
| `mcp-click-up/references/troubleshooting.md` | D2 | 2 | 0 P0, 0 P1, 0 P2 (same hygiene finding) | complete |
<!-- MACHINE-OWNED: END -->

## 16. REVIEW BOUNDARIES
<!-- MACHINE-OWNED: START -->
- Max iterations: 5
- Convergence threshold: 0.1
- Rolling STOP threshold: 0.08
- No-progress threshold: 0.05
- Coverage stabilization passes required: 1
- Session lineage: sessionId=fanout-deepseek-1792580454700-vajsq8, parentSessionId=null, generation=1, lineageMode=new
- Findings registry: `deep-review-findings-registry.json`
- Release-readiness states: in-progress | converged | release-blocking
- Per-iteration budget: 12 tool calls, 10 minutes
- Severity threshold: P2
- Review target type: spec-folder (staging wrapper over the Product Owner files the spec names)
- Cross-reference checks: core=[spec_code, checklist_evidence], overlay=[skill_agent, agent_cross_runtime, feature_catalog_code, playbook_capability]
- Started: 2026-10-21T11:04:14Z
<!-- MACHINE-OWNED: END -->
