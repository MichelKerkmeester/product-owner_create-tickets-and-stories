# Review Iteration 009

BINDING: target=AI Systems/Product Owner
BINDING: maxIterations=10
BINDING: convergence=0.1
BINDING: mode=review
BINDING: dimensions=maintainability
BINDING: specFolder=specs/054-po-system-deep-review

## Dispatcher

- Mode: `review`; target agent `@deep-review`; execution = one iteration.
- Dimension this pass: **maintainability**.
- Budget profile: `scan` (9 analysis calls used, 12 soft / 13 hard).
- Operator focus addressed: this pass is the operator's refinement question — always-loaded token cost, duplicated rules between hub, references and kernel, prose-only requirements with no gate, README/USER-GUIDE usefulness, and whether `doctor:overlay` plus re-pinning can replace or simplify `scripts/vendor-sync.py`. Both halves of that question (the duplication cost and the vendoring-mechanism comparison) produced findings below.
- Parallel-work note: iterations 3 to 9 run concurrently, each on its own focus. Only iteration 9's number is used in ids and file names; no other worker's artifacts were read or written.

## Files Reviewed

- `AI Systems/Product Owner/SKILL.md:66` — hub layout gloss for the two browser trees
- `AI Systems/Product Owner/SKILL.md:5` — hub release version `1.0.28.0`
- `AI Systems/Product Owner/AGENTS.md:190` — Command Registry (prose command table)
- `AI Systems/Product Owner/AGENTS.md:205` — Routing Compatibility (prose precedence list)
- `AI Systems/Product Owner/AGENTS.md:226`, `AGENTS.md:240`, `AGENTS.md:274` — loading order, full DAG, DAG rule
- `AI Systems/Product Owner/ROUTER.md:76`, `ROUTER.md:135` — per-request Human Voice cards, compiled-routing directive
- `AI Systems/Product Owner/hub-router.json:24` — `stageOneOrder` (machine precedence)
- `AI Systems/Product Owner/vendor.json:1` — per-file SHA-256 pinning, `base_commit`, `exclude`, `include`
- `AI Systems/Product Owner/mcp-click-up/` (directory listing) — no `.skilled` directory, no overlay lock
- `AI Systems/Product Owner/SYNC.md:6`, `SYNC.md:20`, `SYNC.md:108` — parity-note shape and longest line
- `AI Systems/Product Owner/claude project/Custom Instructions.md:1` — kernel H1 `v1.2.18`
- `AI Systems/Product Owner/claude project/kernel-review.json:1` — review record, version fields, self-description
- `.skilled/commands/doctor/overlay.md:2` — `/doctor:overlay` purpose statement (`status`, `apply`, `repin`)

Word-count measurements (all from the files the bootstrap chain loads): `AGENTS.md` 4,214 · `SKILL.md` 927 · `ROUTER.md` 1,660 · `sk-product-owner/SKILL.md` 5,000 · `sk-create-figjam/SKILL.md` 1,777 · `mcp-figma/SKILL.md` 2,548 · kernel 8,959 · `SYNC.md` 22,351.

## Findings

### P0 Findings

None. No exploitable, destructive or auth-bypassing defect surfaced in the maintainability surfaces read this pass.

### P1 Findings

None **new** this pass. Two P1s raised by earlier iterations remain active in the findings registry and are neither re-reported, extended nor refuted here:

- the hub `NEVER` rule forbidding a packet-local `ROUTER.md` that three packets carry and the gate requires;
- the Product Owner release gate running a diverged fork of the output-format validator the Sync Loop owns.

Per the verdict mapping in force for this loop, those carried P1s are what keep this iteration at CONDITIONAL rather than PASS; the verdict is not a statement about this pass's own yield.

### P2 Findings

8. **The hub layout block calls the two browser trees "packets" and "no packets" eighteen words apart** — `AI Systems/Product Owner/SKILL.md:66` — The Section 3 layout gloss reads "vendored browser packets the ClickUp page routines drive, no packets". The same noun is asserted and denied in one line, inside the paragraph whose only job is telling a maintainer what is and is not a routable packet.
   - Finding class: documentation accuracy / ambiguous ownership
   - Scope proof: one prose line in the hub; `mode-registry.json` lists four modes and `leaf-manifest.json` 88 leaves, neither of which contains these two trees, so this line is the only place their status is stated.
   - Affected surface hints: `SKILL.md` Section 3 layout block; any future `mode-registry.json` or `leaf-manifest.json` edit; `manual-testing-playbook/` links that name the browser trees.
   - Case: a maintainer adding a fifth browser-facing mode reads `SKILL.md:66`, concludes the two trees are packets that lost their manifests, and edits `mode-registry.json` — the edit then disagrees with the generated `leaf-manifest.json` and with the hub's packet-file rule.
   - Counterevidence: the surrounding sentences do say the Code Mode server is "a repository file and no packet", so a careful reader can recover the intent; that is why this stays P2, not P1.

9. **About 11,800 words load before any task work, and `AGENTS.md` keeps a second prose copy of the precedence the registry owns** — `AI Systems/Product Owner/AGENTS.md:205` — The bootstrap chain is `AGENTS.md` → hub `SKILL.md` → `ROUTER.md` → packet `SKILL.md`, which measures 4,214 + 927 + 1,660 + 5,000 = 11,801 words (roughly 16k tokens) before a single artifact step, and `ROUTER.md:76` records that two Human Voice cards also load on every request. Inside that cost, `AGENTS.md:205-224` restates routing precedence — extract `$quick` before intent, check `$task --subtask` before `$task`, one explicit command beats natural-language wording — that `hub-router.json:24` `stageOneOrder` also encodes, and `AGENTS.md:190` restates the command table the router consumes.
   - Finding class: duplicated authority / entry-token cost
   - Scope proof: counts are measured on the four files the bootstrap chain names; the precedence rules are present in both `AGENTS.md:205` and `hub-router.json:24`; no reviewed file compares the two copies.
   - Affected surface hints: `AGENTS.md:190-274`; `hub-router.json` `stageOneOrder` and `vocabularyClasses`; `ROUTER.md` stage-one table; `benchmark/hub-routing-cases.json` (replays outcomes, not prose).
   - Case: `$epic` stops forcing the Story shape in `hub-router.json`. The routing fixtures pass because they replay the registry, while `AGENTS.md:205` still states the old precedence to every CLI session, and that stale copy is read first.
   - Counterevidence: `check_hub.py` is the hub's gate and could compare the two; iterations 1 and 2 read its contract for packet-file and version rules, not for prose-versus-registry comparison, so the comparison is unverified. Unverified gate coverage is the reason this is P2.
   - Downgrade trigger: a read of `check_hub.py` showing it does compare `AGENTS.md` precedence prose to `hub-router.json` collapses this to a pure token-cost note.

10. **Two incompatible vendoring models coexist, and the vendored packets have no local-edit path** — `AI Systems/Product Owner/vendor.json:1` — `vendor.json` pins every vendored file by SHA-256 plus a `base_commit` per package (the ClickUp packet alone pins more than a hundred files), and `scripts/vendor-sync.py` verifies and re-copies them byte for byte, with a local edit treated as drift and sent upstream through `push`. The tree it copies from uses a different model: `/doctor:overlay` describes itself as "Check whether a vendored Skilled tree still carries its overlays, put them back, or re-pin it" (`overlay.md:2`), and its `apply --capture` exists to adopt one live local edit as an overlay. The copies carry no overlay artifacts — the `mcp-click-up/` listing is twelve entries with no dotfiles and no `.skilled` directory — so `--capture` has no analogue here and there is no way to keep a local fix and still sync.
   - Finding class: divergent mechanism / missing local-edit affordance
   - Scope proof: `vendor.json` hash-pins each vendored file; the copied trees contain no overlay lock; the hub sends every vendored change upstream.
   - Affected surface hints: `vendor.json` (`exclude`, `include`, `base_commit`), `scripts/vendor-sync.py`, `.skilled/commands/doctor/overlay.md`, `SKILL.md` "When NOT to Use".
   - Case: an operator needs a one-line fix in `mcp-click-up/references/troubleshooting.md` for a demo. `vendor-sync.py` reports drift on the next run, `push` needs upstream commit rights the demo does not have, and `--capture` never reaches outside `.skilled`; the operator either edits upstream or keeps a tree the sync tool calls broken.
   - Operator-question answer: overlay and re-pin **cannot** replace `scripts/vendor-sync.py` — overlay has no whole-packet byte parity, no per-file manifest and no `push` verb. The part worth closing is the missing local-edit affordance: either state the no-local-edits rule as a checkable gate or adopt overlay for the two workflow packets.
   - Counterevidence: `push` is a real capability `doctor:overlay` lacks, and byte parity is the stronger guarantee for a vendored third-party tool; a straight replacement would be a regression, which is why this is P2 and the recommendation is narrow.

11. **The kernel review record cannot answer "is the Project kernel current?" — three version vocabularies with no stated relation** — `AI Systems/Product Owner/claude project/kernel-review.json:1` — The record carries `kernelVersion: 0.8.0` and `alignedSkillVersion: 0.8.0`; the live kernel's H1 is `# Product Owner - Custom Instructions - v1.2.18` (`Custom Instructions.md:1`); the hub release is `1.0.28.0` (`SKILL.md:5`). The record's own note calls it a dated point-in-time record and states that "Nothing reads this file", so the one structured artifact that could show kernel-review recency reports 0.8.0 against a 1.2.18 kernel and a 1.0.28.0 hub, with no field stating which is newer.
   - Finding class: unverifiable governance record
   - Scope proof: the three version strings are read directly; the record is the only structured kernel-review artifact in the reviewed surface.
   - Affected surface hints: `claude project/kernel-review.json`; `claude project/Custom Instructions.md` H1; `SYNC.md` review notes; hub `changelog/`.
   - Case: a release reviewer asks whether the kernel was reviewed after the last skill change. The record says 0.8.0 / 0.8.0, the kernel says v1.2.18, the hub says 1.0.28.0, and no field maps them; the answer exists only by hand-reading `SYNC.md`.
   - Counterevidence: the record disclaims itself as historical, so it is honest rather than wrong. The defect is the unanswerable comparison, not a false claim, which keeps it P2.
   - Downgrade trigger: a stated mapping (for example a `kernelVersion` that copies the kernel H1 and an `alignedSkillVersion` that copies the hub version) removes the finding.

12. **The parity note is 22,351 words in 136 lines with two headings, so the hand-parity method has no index** — `AI Systems/Product Owner/SYNC.md:6` — `SYNC.md` measures 136 lines and 22,351 words, with ATX headings only at `:6` (`# Product Owner Parity Note`) and `:20` (`## Review notes`), and its longest line is 4,364 characters at line 108. That is 2.5× the 8,959-word kernel it documents, in the file whose entire job is mapping skill paragraphs to Project counterparts, and it is the hand-authored authority the parity method depends on.
   - Finding class: unusable maintenance artifact / unreadable diff surface
   - Scope proof: counts and heading positions measured on the file; no other parity map exists for the Claude Project package.
   - Affected surface hints: `SYNC.md:6-136`; `SYNC.md:108`; the 70 files under `claude project/knowledge/`; the root parity method in the repository `AGENTS.md` §5.
   - Case: one paragraph changes in `sk-product-owner/SKILL.md`. The maintainer must locate that paragraph's row in a 22k-word, two-heading file to decide whether the Project counterpart needs the same edit; the row is not addressable by heading, and the resulting edit sits inside a 4.3 KB line, so review cannot see it.
   - Counterevidence: the file may carry non-ATX structure (bold rows, fenced lists) that a heading scan does not count, and iteration 2 did read parts of it successfully; the finding is about navigability at this size, not absence of content. That is why it is P2.
   - Downgrade trigger: a section per packet or per Project file (heading-addressable rows) at any size, or evidence that the parity workflow already greps a stable key.

## Traceability Checks

| Protocol | Level | Status | Evidence |
|---|---|---|---|
| `spec_code` | core | partial | `SKILL.md:66` prose denies and asserts packet status for the same two trees; the machine registries (`mode-registry.json` four modes, `leaf-manifest.json` 88 leaves) agree with each other and disagree with the prose. Finding 8. |
| `checklist_evidence` | core | partial | Hub `ALWAYS`/`NEVER` items read against disk this pass: the `vendor.json` + `vendor-sync.py` item resolves (`vendor.json:1`), the "no packet-local logic in the hub" item holds. The packet-file rule remains finding 1's subject and was not re-examined. |
| `skill_agent` | overlay | pass | One advisor identity holds: hub `product-owner`, `description.json`, single `graph-metadata.json`, kernel H1 `v1.2.18` naming the same system. |
| `agent_cross_runtime` | overlay | notApplicable | No agent definition inside this surface. |
| `feature_catalog_code` | overlay | partial | Four vendored packets carry `feature-catalog/`; `mcp-code-mode` and the two workflow packets carry none. Asymmetry is explainable (tool packets catalog tool surfaces) and was ruled out as a defect, not filed. |
| `playbook_capability` | overlay | partial | Every packet carries `manual-testing-playbook/`, plus one at the hub root; playbook bodies were not read this pass — deferred to the traceability iteration. |

## Integration Evidence

- `/doctor:overlay` command contract: `.skilled/commands/doctor/overlay.md:2` (purpose), with `apply --capture` named in its argument table — read as the comparison surface for finding 10. The engine and workflow YAML were not executed.
- `scripts/vendor-sync.py` was read at contract level only in this pass; its verb and pin behaviour came from `vendor.json` and iteration 2's verification, not from a rerun.
- `benchmark/parity/run_parity.sh` is named by `kernel-review.json` as the parity checker; iteration 2 established that the release runner never invokes the checked-in parity scripts (open finding 6). This pass used that only as context for finding 11 and did not re-litigate it.

## Edge Cases

- **Iteration-number disagreement (recorded, resolved by dispatch).** The state log derives three from `type:"iteration"` records (iterations 1 and 2 complete, iteration 3 not yet recorded), while dispatch assigns 9 and pre-registers `iteration_start` rows for 3 through 9 because those workers run concurrently. Deriving would collide with a parallel worker, so the dispatch-assigned 9 was used. This is the one place the contract's derive-from-JSONL rule is knowingly not applied.
- **Racing projection.** `deep-review-state.jsonl` is written by other workers during this pass, so counts read from it (P0=0, P1=2, P2=5 at start) are a snapshot, not a fixed fact. Findings 8-12 were deduplicated against the seven registry titles given in dispatch, not against a live registry re-read late in the pass.
- **Word-count scope.** Counts are for the four files the bootstrap chain itself names; whether a runtime actually loads all four before the first user turn is environment-dependent, so the token figure is an upper bound stated as such.
- **Heading scan limit.** `SYNC.md` was scanned for ATX headings only; non-ATX structure inside it is unmeasured, which is written into finding 12's downgrade trigger rather than hidden.

## Confirmed-Clean Surfaces

- Package shape: all seven vendored and workflow packages carry `SKILL.md`, `ROUTER.md`, `README.md`, `changelog/`, `manual-testing-playbook/` and `references/`; changelog counts are non-trivial everywhere (44, 19, 25, 12, 20, 16, 18), so no package is missing its release line.
- Single advisor identity: no duplicate `graph-metadata.json` outside the hub.
- `vendor.json` internal consistency: every package declares `local_path`, `upstream_path` and either a `base_commit` with per-file hashes or an `include`/`exclude` pair; the two `include` packages (`code-mode-launcher`, `mermaid-extract`) pin their upstreams to the same commit.
- `ROUTER.md` structure: five headed sections plus the compiled-routing directive, and the directive itself documents the legacy sentinel path for a clone with no `.skilled/bin/`, so the fallback is stated rather than implied.

## Ruled Out

- **`kernel-review.json` version mismatch as drift**: ruled out. The record's `note` states it is a dated point-in-time record at the version named, and that nothing reads it. The finding filed (11) is the unanswerable comparison, not a claim that the record is wrong.
- **Feature-catalog asymmetry across packets as a package-shape defect**: ruled out. Four vendored MCP/tool packets carry `feature-catalog/`, `mcp-code-mode` and the two workflow packets do not; tool-surface catalogs have no workflow counterpart to describe.
- **`mcp-code-mode` as an incomplete packet**: ruled out. It is exempted in the hub, carries its own leaf manifest by design and is excluded from `graph-metadata.json` in `vendor.json`, which is consistent with being the shipped server rather than a packet.
- **Compiled-routing directive as dead prose**: ruled out. `ROUTER.md:135-145` documents that no compiled activation manifest ships and that a clone without `.skilled/bin/` takes the same legacy path, so the directive has a stated fallback.
- **`vendor.json` `exclude`/`include` keys as an undocumented escape hatch**: ruled out. Both keys appear with explicit file lists (including `node_modules`, `dist` for Code Mode), so the copy contract is stated per package.

## Next Focus

- **Dimension:** security.
- **Focus area:** `AI Systems/Product Owner/scripts/` (path containment in `vendor-sync.py`, `code-mode.cjs`), `benchmark/gates/check_markdown_links.py`, the fixture harnesses for shell quoting and path handling, and `AI Systems/z — Claude Project Sync Loop/*.py` argument handling.
- **Reason:** correctness and maintainability are now covered on the hub contract and packaging surface; the executable surface is where operator input, file paths and shell interpolation meet, which is the security dimension's reach. `AI Systems/Product Owner/.env` remains a hard non-target.
- **Rotation status:** `maintainability` completed its first pass this iteration; `security` becomes the active dimension with `traceability` still queued. Parallel workers cover their own focuses and are not counted here.
- **Blocked/productive carry-forward:** productive — finding 10's narrow question (is the no-local-edit rule gated anywhere?) needs one read of `benchmark/gates/` wiring; deferred, not exhausted.
- **Required evidence:** `scripts/vendor-sync.py` containment helpers, `scripts/code-mode.cjs`, `check_markdown_links.py` path resolution, and the Sync Loop Python entry points, each checked for traversal, shell interpolation of untrusted values and secret exposure.
- **Recovery note:** not applicable; this iteration ran inside budget.

## Verdict

No P0 and no new P1. Five new P2 findings, all in maintainability: contradictory hub prose (8), entry cost with duplicated precedence prose (9), two vendoring models with no local-edit path (10), an unanswerable kernel-review version comparison (11), and a parity note too large to navigate (12).

Two P1 findings remain active from earlier iterations (registered, not raised here). Per the loop's mapping over findings active at this iteration, that keeps the verdict at CONDITIONAL rather than PASS; `hasAdvisories=true` because five P2s are also open.

Review verdict: CONDITIONAL
