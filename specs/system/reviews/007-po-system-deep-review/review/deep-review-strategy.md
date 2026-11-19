---
title: Deep Review Strategy Template
description: Runtime template copied to review/ during initialization to track review progress, dimension coverage, findings, and outcomes across iterations.
trigger_phrases:
  - "deep review strategy template"
  - "review dimension tracking"
  - "exhausted review approaches"
  - "review session tracking"
importance_tier: normal
contextType: planning
version: 1.11.0.13
---

# Deep Review Strategy - Session Tracking Template

Runtime template copied into the resolved `specs/054-po-system-deep-review/review/` during initialization. Tracks review progress across iterations.

## 1. OVERVIEW

### Purpose

Serves as the "persistent brain" for a deep review session. Records which dimensions remain, what was found (P0/P1/P2), what review approaches worked or failed, and where to focus next. Read by the orchestrator and agents at every iteration.

### Usage

- **Init:** Orchestrator copies this template to `specs/054-po-system-deep-review/review/deep-review-strategy.md` and populates Topic, Review Dimensions, Known Context, and Review Boundaries from config and memory context.
- **Per iteration:** Agent reads Next Focus, reviews the assigned dimension/files, updates findings, marks dimensions complete, and sets new Next Focus.
- **Mutability:** Mutable, updated by both orchestrator and agents throughout the session.
- **Protection:** None (shared mutable state). Orchestrator validates consistency on resume.
- **Ownership:** Machine-managed metrics and coverage blocks are wrapped in explicit ownership markers. Human commentary and operator overrides live outside those markers.

---

## 2. TOPIC
The whole Product Owner system and its nested skills in AI Systems/Product Owner: hub SKILL.md, ROUTER.md and AGENTS.md, sk-product-owner, sk-create-figjam, the vendored mcp-click-up, mcp-aside-devtools, mcp-chrome-devtools, mcp-code-mode and mcp-figma packages, vendor.json and scripts/vendor-sync.py, claude project/, benchmark/ gates and fixtures, manual-testing-playbook/, SYNC.md, READMEs, USER-GUIDE.md and changelogs

Operator focus: Find drift, bugs and refinement or improvement opportunities across the whole Product Owner system. Check alignment with Skilled sk-doc (sk-create-skill package shape, README, changelog, frontmatter, playbook and catalog modes) and with sk-code for scripts and validators. Analyze how easily the vendored mcp and browser packages sync from Skilled, and whether Skilled overlay and repinning support for external repos (doctor:overlay, system-skilled-doctor) could replace or simplify scripts/vendor-sync.py. Never open or quote AI Systems/Product Owner/.env, it holds secrets. Skip specs/, export/ and z_archive/ except as evidence.

---

<!-- ANCHOR:review-dimensions -->
## 3. REVIEW DIMENSIONS (remaining)
[All dimensions complete]

<!-- /ANCHOR:review-dimensions -->
## 4. NON-GOALS
Product Owner deliverables in export/, archived packets, the .env file and upstream Skilled internals beyond the overlay, repin and sk-doc and sk-code contracts.

---

## 5. STOP CONDITIONS
Stop policy max-iterations: all 10 iterations run. Convergence is telemetry only.

---

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
- P1 (Required): 7
- P2 (Suggestions): 21
- Resolved: 0

<!-- /ANCHOR:running-findings -->
## 8. WHAT WORKED
- **Disk-existence sweep before reading contracts**: probing all 18 `RESOURCE_MAP` paths and all 88 `leaf-manifest.json` leaves first turned "does every routed file exist" into a 0-miss fact instead of an inference, which freed the rest of the budget for contract-vs-contract comparison. (iteration 1)
- **Cross-file parity reads in one batch**: reading `SKILL.md`, `ROUTER.md`, `hub-router.json`, `mode-registry.json` and `leaf-manifest.json` together exposed the `SKILL.md:87` vs three-on-disk-`ROUTER.md` contradiction immediately; read one at a time it reads as compliant. (iteration 1)
- **Deliberate hunt for documented non-drift**: checking `DEFAULT_RESOURCE` vs `routerPolicy.defaultResource` and the `mcp-code-mode` leaf-manifest exception against their own justification text ruled both out cheaply and kept them out of the findings. (iteration 1)
- **Byte-comparing the two copies of a gated artifact before reading either**: `cmp -s` plus `wc -l` on the Product Owner and Sync Loop `validate-output-format.cjs` turned a vague "these look duplicated" suspicion into a 145-line divergence with two incompatible runner contracts in one call. Comparing artifacts beats reading both bodies. (iteration 2)
- **Following the exit-code contract from the header to the implementation**: reading the documented exit table first, then the result block, proved `run_gates.sh` faithful on three of four claims and isolated the one silent exclusion (finding 6) instead of re-auditing every gate. (iteration 2)
- **Checking that every `--self-test` gate is wired to a script that implements the flag**: four greps ruled out the whole "check that cannot fail" family, including the `unittest.main` guard on `test_vendor_sync.py`. (iteration 2)
- **Letting the git index answer the ignore question instead of reading the ignore file**: `git ls-files` plus `git check-ignore -v` turned ".env and click-up-links.md are ignored, so they are safe" into a checked fact, and it covered the case ignore rules cannot — a file committed before its rule existed. (iteration 3)
- **Grepping the sibling packet to test whether a rule gap is a fleet gap or a packet gap**: one search of `mcp-aside-devtools/SKILL.md` turned "maybe no packet has one" into "the sibling has it and this one does not", which makes R3-P1-001 a rule gap rather than a preference. (iteration 3)
- **Reading the docstring before reporting the containment gap**: `vendor-sync.py:316-318` explains why a resolved-path check would refuse the `.skilled` link, which killed the traversal finding and left only the narrower override-root asymmetry. (iteration 3)
- **Testing the guide's claims against the directory instead of against each other**: `README.md` says 67 knowledge files, the kernel says twenty-eight example documents and the directory holds 30. Counting the directory once turned "these prose numbers might be stale" into one precise finding and one clean pass, because the README and the directory could then be adjudicated separately from the README and the kernel. (iteration 5)
- **Resolving a tracked/untracked claim with `git check-ignore -v` rather than `cat .gitignore`**: the guide claims `local/` holds a gitignored filled copy while `templates/` holds the blank scaffold. Reading the ignore rule alone leaves open whether the filled file is actually untracked; `git ls-files` plus `git check-ignore -v` proved the split in one call and retired a would-be privacy finding. (iteration 5)
- **Treating a dated note's number as history, not drift**: the 2026-09-17 note says thirty-eight files against a live 67. `SYNC.md`'s own 2026-09-18 entry establishes that a dated entry records what was true when written, which settles the contradiction from inside the document instead of charging it as a defect. (iteration 5)
- **Diffing the authoring rule owner before the authored artifact**: reading `sk-create-skill`'s required shape and `sk-create-changelog`'s placement rules first turned "does this system follow sk-doc" into a line-by-line comparison with a citable rule number per deviation, and surfaced a conflict *inside* sk-doc (`sk-create-skill/SKILL.md:165` still mandates the per-packet `changelog/` that `sk-create-changelog/SKILL.md:10` deprecates) that no Product Owner read could have exposed. (iteration 4)
- **Counting the tree before trusting a deprecation**: `ls`+`wc -l` on the three `changelog/` folders (29 + 44 + 19) plus a listing of `.skilled/changelog/` (15 components, none named `product-owner`) settled placement drift as a measured fact in one call instead of an inference from one sample file. (iteration 4)
- **Prevalence checks as a phantom-finding filter**: counting how many installed skills ship a top-level `references/README.md` (0 of 8) killed a plausible sk-doc deviation before it reached the narrative. A rule quoted in one packet is not a rule imposed on all packets. (iteration 4)

- **Measuring entry cost instead of guessing at it**: `wc -w` on the four files the bootstrap chain names turned "the hub feels big" into 11,801 words (4,214 + 927 + 1,660 + 5,000) in one call, making the cost evidence rather than opinion. (iteration 9)
- **Answering the operator's vendoring question from the two lock schemas**: `vendor.json`'s per-file SHA plus `overlay.md:2`'s stated purpose settled "can overlay replace vendor-sync" as no (no byte parity, no `push`) and exposed the real gap in the same comparison, the absent local-edit affordance. (iteration 9)
- **Counting headings and longest line before criticising a document**: `SYNC.md` at 136 lines / 22,351 words / 2 ATX headings / 4,364-char longest line made the finding falsifiable, and scanning ATX headings only is what the downgrade trigger honestly records. (iteration 9)
- **Answering the operator focus with a table instead of prose opinions**: reading `vendor.json`, the overlay engine's constants and both router documents before forming a view turned "could overlay replace this" into four blockers with file:line each, instead of the plausible-sounding "overlay is the newer mechanism". The `VENDOR_ROOT = '.skilled'` constant alone decided it. (iteration 7)
- **Hashing the manifest instead of trusting a status run**: a 15-line read-only script recomputed all 529 recorded sha256 values and returned 0 drift, 0 missing across 7 packages. That one fact — no local overlays exist today — deleted a suspected class of findings and made the overlay analysis affordable. (iteration 7)
- **Checking whether `.skilled` is git-tracked before calling an excluded file "upstream content"**: `git ls-files .skilled` returning 0 entries and `check-ignore` reporting "beyond a symbolic link" is what kept finding 8 at P2 instead of a P1 claim about lost upstream files. (iteration 7)

---

## 9. WHAT FAILED
- Iteration 6 marginal note: **rule-line-first reading produced two bounded findings and eight clean rulings in one pass.** Reading the sk-code standard's own line (JS :228/:202, shell :68) before judging the code kept two suspected defects (`set -e` omission, missing JSDoc) from being filed as correctness bugs and turned the rest into ruled-out evidence. (iteration 6)

- **Relative-path probing from the packet folder**: resolving `.skilled/...` as `../../../` produced three false misses (`compiled-route.cjs`, `leaf-resource-contract.cjs`, `generate-leaf-manifest.cjs`) that would have been reported as dead paths. Re-probing from the repository root corrected it; always resolve workspace-relative tool paths from the repo root, never from the review target. (iteration 1)
- **Reading only the `### NEVER` block as authority**: the first pass treated `SKILL.md:87` as current policy until `check_hub.py:23` was cross-read. Authority files need the gate cross-read before any rule is called authoritative. (iteration 1)
- **Estimating drift direction from line counts alone**: `wc -l` says the Product Owner validator is the smaller copy, and it is tempting to write "stale fork". Line count proves divergence, not direction. Finding 5 was refiled as drift with a named downgrade trigger rather than a claim about which copy is newer. (iteration 2)
- **Budgeting the whole Sync Loop script surface in one iteration**: 13 Python scripts, 2 CJS scripts and 5 shell runners cannot be read in a correctness pass that also covers the gate runner. Filed as deferred (SL-014) instead of half-read, which keeps the security pass honest. (iteration 2)
- **Not loading review doctrine because the budget ran out**: `sk-code-review/references/review-core.md` was never read in iteration 3, so severity was carried over from iterations 1-2 and the dispatch restatement. That is a gap in the pass, not a clean one; iteration 4 carries it as required evidence. (iteration 3)
- **A pathspec grep that could not match**: `git ls-files | grep '/context/'` requires a leading slash, so a repo-relative `context/...` path can never match and the empty result reads like "untracked" when it is "asked wrongly". Re-run as `git ls-files context`. (iteration 3)
- **Running-findings totals move underneath a concurrent iteration**: iterations 1-3 raised 3 P1 and 7 P2, while the reducer-derived block read P2=10 by the time iteration 3 finished, because iterations 3-9 run in parallel and sibling records landed during this pass. The count is reducer-owned and was left alone; a per-iteration agent must read its own findings from its own delta, never from the shared totals. (iteration 3)
- **Reading a registration as data before trusting the docs that describe it**: dumping the four `manual_call_templates` keys out of `.utcp_config.json` with `node -e` and comparing the *name set* against the vendored README's claim ("the `chrome_devtools_1` and `chrome_devtools_2` manuals in `.utcp_config.json`") found the P1 in one call. Registry-vs-prose comparison on the name set is far cheaper than reading the vendored docs first and believing them. (iteration 8)
- **Counting a claim against disk instead of reasoning about it**: `find … -name '*.md' | wc -l` returned 69 for `sk-product-owner/manual-testing-playbook/`, so "the 68 artifact scenarios" was ruled out in one command instead of argued about. (iteration 8)
- **Scanning `manual-testing-playbook/` for the uppercase word only**: the first probe used `"smoke matrix\|Smoke"`, which is enough to prove the phrase is absent but not enough to name what the guide meant. A stored `SMOKE` heading or a `smoke-matrix.sh` would have been missed, so finding 2 is filed with an alternative explanation and a downgrade trigger rather than as a settled capability gap. (iteration 5)
- **Reading the kernel-review record as a live claim before reading its note**: the 0.8.0-versus-1.2.18 gap looks like an eleven-release drift until `kernel-review.json`'s own `note` and the fleet episode record are read. Read control files' self-descriptions before measuring them against live state. (iteration 5)
- **Assuming the state log's iteration count is authoritative under parallel fan-out**: the JSONL holds 2 records against a dispatched iteration 5. The parallel dispatch contract, not the log, decides the number, and the mismatch now costs an edge-case entry in every concurrent iteration. (iteration 5)
- **Reading `sk-create-skill`'s packet shape as current policy**: its `changelog/`-per-packet line at `:165` is stale against `sk-create-changelog`'s deprecation. Two `sk-doc` packets disagree, so a shape claim needs the owning packet read too, not just the shape packet. (iteration 4)
- **Nearly filing a conditional rule as a violation**: `procedures/` is required only for packets with multiple distinct triggered processes, and the reference implementation `sk-create-skill` has none, so filing it would have been a phantom finding. (iteration 4)

- **Letting one probe dump a whole manifest**: `cat vendor.json` consumed the output budget and truncated the four probe sections before it, losing verified anchors that had to be re-probed. Query manifests with `grep`/`jq` projections. (iteration 9)
- **Trusting an `&&` chain around `grep -c`**: a zero count exits 1 and silently killed the rest of the probe mid-chain. Use `;` separators when a probe has independent sections. (iteration 9)
- **Asserting against a concurrently edited strategy**: an exact-match strategy patch aborted because parallel iterations had already rewritten the section, so iteration 9 fell back to additive inserts. Shared mutable state must be patched additively, never asserted. (iteration 9)
---

- **Assuming an excluded manifest path was build output**: the first reading of `mcp-code-mode.exclude` treated `graph-metadata.json` as generated and nearly dropped the observation. It exists in the upstream tree and is absent from the copy, so the honest form is a P2 with a downgrade trigger — not silence, and not a P1. (iteration 7)
- **Reading `vendor.json` as raw JSON without a structure digest**: 614 lines of hash table hid that `include`/`exclude`/`base_commit` appear on different packages. A computed per-package key summary is what exposed the four different `base_commit` values behind the overlay blocker. (iteration 7)

---

<!-- ANCHOR:exhausted-approaches -->
## 9. EXHAUSTED APPROACHES (do not retry)
### **`benchmark/` shape deviation**: ruled out. `benchmark/README.md` is present and `reports/` uses the contracted dated folder grammar. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: **`benchmark/` shape deviation**: ruled out. `benchmark/README.md` is present and `reports/` uses the contracted dated folder grammar.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`benchmark/` shape deviation**: ruled out. `benchmark/README.md` is present and `reports/` uses the contracted dated folder grammar.

### **`claude project/local/` as a private-data leak into the tracked package.** Ignored at `.gitignore:15`, filled copy untracked, only the blank `templates/` copy tracked. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: **`claude project/local/` as a private-data leak into the tracked package.** Ignored at `.gitignore:15`, filled copy untracked, only the blank `templates/` copy tracked.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`claude project/local/` as a private-data leak into the tracked package.** Ignored at `.gitignore:15`, filled copy untracked, only the blank `templates/` copy tracked.

### **`context/.gitkeep` and `context/README.md` as an untracked-but-claimed pair** -- ruled out; both are tracked and both are negated back in by `!` rules at `.gitignore:36-37`. -- BLOCKED (iteration 10, 1 attempts)
- What was tried: **`context/.gitkeep` and `context/README.md` as an untracked-but-claimed pair** -- ruled out; both are tracked and both are negated back in by `!` rules at `.gitignore:36-37`.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`context/.gitkeep` and `context/README.md` as an untracked-but-claimed pair** -- ruled out; both are tracked and both are negated back in by `!` rules at `.gitignore:36-37`.

### **`DEFAULT_RESOURCE` vs `routerPolicy.defaultResource` collision as drift.** Distinguished on purpose at `ROUTER.md:37` with `defaultResourceSemantics: fallback-only`. Not a finding. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: **`DEFAULT_RESOURCE` vs `routerPolicy.defaultResource` collision as drift.** Distinguished on purpose at `ROUTER.md:37` with `defaultResourceSemantics: fallback-only`. Not a finding.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`DEFAULT_RESOURCE` vs `routerPolicy.defaultResource` collision as drift.** Distinguished on purpose at `ROUTER.md:37` with `defaultResourceSemantics: fallback-only`. Not a finding.

### **`documentation`/`clarify` missing from `vocabularyClasses.artifact-request-nouns`** while present in `product-owner-artifacts`. Examined as a possible rule-2 gap: a request such as "write documentation for X" misses the artifact-request rule and lands on the single-signal rule instead, but both resolve to `defaultMode` `sk-product-owner`, so the outcome is identical. Cosmetic redundancy, not actionable at any severity. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: **`documentation`/`clarify` missing from `vocabularyClasses.artifact-request-nouns`** while present in `product-owner-artifacts`. Examined as a possible rule-2 gap: a request such as "write documentation for X" misses the artifact-request rule and lands on the single-signal rule instead, but both resolve to `defaultMode` `sk-product-owner`, so the outcome is identical. Cosmetic redundancy, not actionable at any severity.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`documentation`/`clarify` missing from `vocabularyClasses.artifact-request-nouns`** while present in `product-owner-artifacts`. Examined as a possible rule-2 gap: a request such as "write documentation for X" misses the artifact-request rule and lands on the single-signal rule instead, but both resolve to `defaultMode` `sk-product-owner`, so the outcome is identical. Cosmetic redundancy, not actionable at any severity.

### **`exclude` and `include` set on the same package** (which the script refuses): ruled out — `vendor.json` respects the mutual exclusion at [`AI Systems/Product Owner/scripts/vendor-sync.py:357`. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: **`exclude` and `include` set on the same package** (which the script refuses): ruled out — `vendor.json` respects the mutual exclusion at [`AI Systems/Product Owner/scripts/vendor-sync.py:357`.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`exclude` and `include` set on the same package** (which the script refuses): ruled out — `vendor.json` respects the mutual exclusion at [`AI Systems/Product Owner/scripts/vendor-sync.py:357`.

### **`feature_catalog_code` gap.** No catalog exists for this system to drift from; the fleet catalog covers the gate, not this source. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: **`feature_catalog_code` gap.** No catalog exists for this system to drift from; the fleet catalog covers the gate, not this source.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`feature_catalog_code` gap.** No catalog exists for this system to drift from; the fleet catalog covers the gate, not this source.

### **`graph-metadata.json` as a duplicate hub identity** -- ruled out; `SKILL.md:72` and the manifest agree that only the hub carries one. -- BLOCKED (iteration 10, 1 attempts)
- What was tried: **`graph-metadata.json` as a duplicate hub identity** -- ruled out; `SKILL.md:72` and the manifest agree that only the hub carries one.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`graph-metadata.json` as a duplicate hub identity** -- ruled out; `SKILL.md:72` and the manifest agree that only the hub carries one.

### **`kernel-review.json` version mismatch as drift**: ruled out. The record's `note` states it is a dated point-in-time record at the version named, and that nothing reads it. The finding filed (11) is the unanswerable comparison, not a claim that the record is wrong. -- BLOCKED (iteration 9, 1 attempts)
- What was tried: **`kernel-review.json` version mismatch as drift**: ruled out. The record's `note` states it is a dated point-in-time record at the version named, and that nothing reads it. The finding filed (11) is the unanswerable comparison, not a claim that the record is wrong.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`kernel-review.json` version mismatch as drift**: ruled out. The record's `note` states it is a dated point-in-time record at the version named, and that nothing reads it. The finding filed (11) is the unanswerable comparison, not a claim that the record is wrong.

### **`leaf-manifest.config.json` missing at the hub root**: ruled out. The parent-hub shape at `sk-create-skill/SKILL.md:203-215` does not list it; only a class-S standalone skill authors one. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: **`leaf-manifest.config.json` missing at the hub root**: ruled out. The parent-hub shape at `sk-create-skill/SKILL.md:203-215` does not list it; only a class-S standalone skill authors one.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`leaf-manifest.config.json` missing at the hub root**: ruled out. The parent-hub shape at `sk-create-skill/SKILL.md:203-215` does not list it; only a class-S standalone skill authors one.

### **`leaf-manifest.json` mode ordering differing from `hub-router.json.tieBreak`.** The manifest sorts by packet name because it is generated; `tieBreak` is a routing policy. Different purposes, no behavioral consequence. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: **`leaf-manifest.json` mode ordering differing from `hub-router.json.tieBreak`.** The manifest sorts by packet name because it is generated; `tieBreak` is a routing policy. Different purposes, no behavioral consequence.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`leaf-manifest.json` mode ordering differing from `hub-router.json.tieBreak`.** The manifest sorts by packet name because it is generated; `tieBreak` is a routing policy. Different purposes, no behavioral consequence.

### **`mcp-code-mode` as an incomplete packet**: ruled out. It is exempted in the hub, carries its own leaf manifest by design and is excluded from `graph-metadata.json` in `vendor.json`, which is consistent with being the shipped server rather than a packet. -- BLOCKED (iteration 9, 1 attempts)
- What was tried: **`mcp-code-mode` as an incomplete packet**: ruled out. It is exempted in the hub, carries its own leaf manifest by design and is excluded from `graph-metadata.json` in `vendor.json`, which is consistent with being the shipped server rather than a packet.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`mcp-code-mode` as an incomplete packet**: ruled out. It is exempted in the hub, carries its own leaf manifest by design and is excluded from `graph-metadata.json` in `vendor.json`, which is consistent with being the shipped server rather than a packet.

### **`mcp-code-mode` leaf-manifest as a rule violation.** Exempted twice in the hub and genuinely not a packet. Not a finding. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: **`mcp-code-mode` leaf-manifest as a rule violation.** Exempted twice in the hub and genuinely not a packet. Not a finding.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`mcp-code-mode` leaf-manifest as a rule violation.** Exempted twice in the hub and genuinely not a packet. Not a finding.

### **`mermaid-extract` pointing at a nonexistent tree.** Its `local_path` is `sk-create-figjam/scripts/vendored`, not `scripts/vendored`; the assumption that every vendored package lives under `scripts/` was wrong, not the manifest. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: **`mermaid-extract` pointing at a nonexistent tree.** Its `local_path` is `sk-create-figjam/scripts/vendored`, not `scripts/vendored`; the assumption that every vendored package lives under `scripts/` was wrong, not the manifest.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`mermaid-extract` pointing at a nonexistent tree.** Its `local_path` is `sk-create-figjam/scripts/vendored`, not `scripts/vendored`; the assumption that every vendored package lives under `scripts/` was wrong, not the manifest.

### **`norm()` duplicated across the five document programs.** Copy-paste REPL snippets cannot import; the duplication is stated in-line at `mcp-tools.md:644` and the alternative (a runtime-injected prelude) does not exist here. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: **`norm()` duplicated across the five document programs.** Copy-paste REPL snippets cannot import; the duplication is stated in-line at `mcp-tools.md:644` and the alternative (a runtime-injected prelude) does not exist here.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`norm()` duplicated across the five document programs.** Copy-paste REPL snippets cannot import; the duplication is stated in-line at `mcp-tools.md:644` and the alternative (a runtime-injected prelude) does not exist here.

### **`overlay-manifest.json` / `.skilled-overlays.json` present in Product Owner and pointing nowhere**: ruled out — neither file exists in the target, consistent with the engine being unused here. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: **`overlay-manifest.json` / `.skilled-overlays.json` present in Product Owner and pointing nowhere**: ruled out — neither file exists in the target, consistent with the engine being unused here.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`overlay-manifest.json` / `.skilled-overlays.json` present in Product Owner and pointing nowhere**: ruled out — neither file exists in the target, consistent with the engine being unused here.

### **`procedures/` missing from the workflow packets**: ruled out. The rule at `sk-create-skill/SKILL.md:167` is conditional, and the reference implementation `sk-create-skill` itself carries no `procedures/` folder. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: **`procedures/` missing from the workflow packets**: ruled out. The rule at `sk-create-skill/SKILL.md:167` is conditional, and the reference implementation `sk-create-skill` itself carries no `procedures/` folder.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`procedures/` missing from the workflow packets**: ruled out. The rule at `sk-create-skill/SKILL.md:167` is conditional, and the reference implementation `sk-create-skill` itself carries no `procedures/` folder.

### **`references/README.md` missing from both packets**: ruled out. All eight installed skills that carry a top-level `references/` folder also lack one, and `sk-create-skill/SKILL.md:48` describes that packet's own route map rather than a rule imposed on every package. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: **`references/README.md` missing from both packets**: ruled out. All eight installed skills that carry a top-level `references/` folder also lack one, and `sk-create-skill/SKILL.md:48` describes that packet's own route map rather than a rule imposed on every package.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`references/README.md` missing from both packets**: ruled out. All eight installed skills that carry a top-level `references/` folder also lack one, and `sk-create-skill/SKILL.md:48` describes that packet's own route map rather than a rule imposed on every package.

### **`rmtree` on `*.pull-old` / `*.pull-new` escaping the repository.** Ruled out — both names derive from `target = repo_root/local_rel`, which `resolve_dirs` has already resolved inside the root and refused when equal to it. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: **`rmtree` on `*.pull-old` / `*.pull-new` escaping the repository.** Ruled out — both names derive from `target = repo_root/local_rel`, which `resolve_dirs` has already resolved inside the root and refused when equal to it.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`rmtree` on `*.pull-old` / `*.pull-new` escaping the repository.** Ruled out — both names derive from `target = repo_root/local_rel`, which `resolve_dirs` has already resolved inside the root and refused when equal to it.

### **`run_gates.sh` skip guard resolving a different Sync Loop folder than `rule_parity.py`**: ruled out. Both resolve to `dirname(Product Owner)/z — Claude Project Sync Loop`. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: **`run_gates.sh` skip guard resolving a different Sync Loop folder than `rule_parity.py`**: ruled out. Both resolve to `dirname(Product Owner)/z — Claude Project Sync Loop`.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`run_gates.sh` skip guard resolving a different Sync Loop folder than `rule_parity.py`**: ruled out. Both resolve to `dirname(Product Owner)/z — Claude Project Sync Loop`.

### **`scripts/vendored/code-mode` and `sk-create-figjam/scripts/vendored` as undocumented drop points**: ruled out — both are `include`-scoped manifest packages with recorded commits. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: **`scripts/vendored/code-mode` and `sk-create-figjam/scripts/vendored` as undocumented drop points**: ruled out — both are `include`-scoped manifest packages with recorded commits.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`scripts/vendored/code-mode` and `sk-create-figjam/scripts/vendored` as undocumented drop points**: ruled out — both are `include`-scoped manifest packages with recorded commits.

### **`set -e` omission as a correctness defect.** The four counting runners stay abort-free on purpose and the five parity wrappers `exec` a single delegated checker, so a mid-script failure cannot be skipped silently. Only the doctrine-recording gap survives (finding 2). -- BLOCKED (iteration 6, 1 attempts)
- What was tried: **`set -e` omission as a correctness defect.** The four counting runners stay abort-free on purpose and the five parity wrappers `exec` a single delegated checker, so a mid-script failure cannot be skipped silently. Only the doctrine-recording gap survives (finding 2).
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`set -e` omission as a correctness defect.** The four counting runners stay abort-free on purpose and the five parity wrappers `exec` a single delegated checker, so a mid-script failure cannot be skipped silently. Only the doctrine-recording gap survives (finding 2).

### **`sk-create-figjam` registering a competing figma manual** — ruled out; the package carries no manual registration. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: **`sk-create-figjam` registering a competing figma manual** — ruled out; the package carries no manual registration.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`sk-create-figjam` registering a competing figma manual** — ruled out; the package carries no manual registration.

### **`sk-product-owner/SKILL.md:290` "68 scenarios" as a stale count** — ruled out; 69 files minus the index is 68. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: **`sk-product-owner/SKILL.md:290` "68 scenarios" as a stale count** — ruled out; 69 files minus the index is 68.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`sk-product-owner/SKILL.md:290` "68 scenarios" as a stale count** — ruled out; 69 files minus the index is 68.

### **`USER-GUIDE.md` version drift** -- ruled out; it states no version and no count. -- BLOCKED (iteration 10, 1 attempts)
- What was tried: **`USER-GUIDE.md` version drift** -- ruled out; it states no version and no count.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`USER-GUIDE.md` version drift** -- ruled out; it states no version and no count.

### **`vendor sync tests` gate that cannot fail**: ruled out. `scripts/tests/test_vendor_sync.py:352` runs `unittest.main(verbosity=2)` and the suite asserts real exit codes 0/1/2 across eight cases. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: **`vendor sync tests` gate that cannot fail**: ruled out. `scripts/tests/test_vendor_sync.py:352` runs `unittest.main(verbosity=2)` and the suite asserts real exit codes 0/1/2 across eight cases.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`vendor sync tests` gate that cannot fail**: ruled out. `scripts/tests/test_vendor_sync.py:352` runs `unittest.main(verbosity=2)` and the suite asserts real exit codes 0/1/2 across eight cases.

### **`vendor sync` guard reading a different environment variable than the script**: ruled out. `run_gates.sh:80` tests `VENDOR_UPSTREAM_ROOT`, `vendor-sync.py:103` reads the same name. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: **`vendor sync` guard reading a different environment variable than the script**: ruled out. `run_gates.sh:80` tests `VENDOR_UPSTREAM_ROOT`, `vendor-sync.py:103` reads the same name.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`vendor sync` guard reading a different environment variable than the script**: ruled out. `run_gates.sh:80` tests `VENDOR_UPSTREAM_ROOT`, `vendor-sync.py:103` reads the same name.

### **`vendor.json` `exclude`/`include` keys as an undocumented escape hatch**: ruled out. Both keys appear with explicit file lists (including `node_modules`, `dist` for Code Mode), so the copy contract is stated per package. -- BLOCKED (iteration 9, 1 attempts)
- What was tried: **`vendor.json` `exclude`/`include` keys as an undocumented escape hatch**: ruled out. Both keys appear with explicit file lists (including `node_modules`, `dist` for Code Mode), so the copy contract is stated per package.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`vendor.json` `exclude`/`include` keys as an undocumented escape hatch**: ruled out. Both keys appear with explicit file lists (including `node_modules`, `dist` for Code Mode), so the copy contract is stated per package.

### **`vendor.json` missing the vendored `scripts/vendored/` tree.** It is registered as `code-mode-launcher` with `upstream_path: .skilled/bin` and both files hashed. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: **`vendor.json` missing the vendored `scripts/vendored/` tree.** It is registered as `code-mode-launcher` with `upstream_path: .skilled/bin` and both files hashed.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **`vendor.json` missing the vendored `scripts/vendored/` tree.** It is registered as `code-mode-launcher` with `upstream_path: .skilled/bin` and both files hashed.

### **A previously-committed secret surviving an ignore rule.** Ruled out for `.env`, `click-up-links.md` and `claude project/local/`: none appears in `git ls-files`. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: **A previously-committed secret surviving an ignore rule.** Ruled out for `.env`, `click-up-links.md` and `claude project/local/`: none appears in `git ls-files`.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **A previously-committed secret surviving an ignore rule.** Ruled out for `.env`, `click-up-links.md` and `claude project/local/`: none appears in `git ls-files`.

### **A second `.utcp_config.json` in the target carrying the isolated chrome manuals** — ruled out; the target has exactly one, with four templates. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: **A second `.utcp_config.json` in the target carrying the isolated chrome manuals** — ruled out; the target has exactly one, with four templates.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **A second `.utcp_config.json` in the target carrying the isolated chrome manuals** — ruled out; the target has exactly one, with four templates.

### **A second `manual_call_templates` set somewhere in the target** -- ruled out again at the terminal pass; exactly four templates in exactly one `.utcp_config.json`. -- BLOCKED (iteration 10, 1 attempts)
- What was tried: **A second `manual_call_templates` set somewhere in the target** -- ruled out again at the terminal pass; exactly four templates in exactly one `.utcp_config.json`.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **A second `manual_call_templates` set somewhere in the target** -- ruled out again at the terminal pass; exactly four templates in exactly one `.utcp_config.json`.

### **A vendored copy currently carrying local overlays**: ruled out — 0 drift and 0 missing across 529 files in all 7 packages. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: **A vendored copy currently carrying local overlays**: ruled out — 0 drift and 0 missing across 529 files in all 7 packages.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **A vendored copy currently carrying local overlays**: ruled out — 0 drift and 0 missing across 529 files in all 7 packages.

### **Absolute temporary paths in `benchmark/reports/**` as a disclosure.** Ruled out — the matches are harness paths (`/var/folders/.../devin-compare-bench`) and base64 diagram payloads, not user data or credentials. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: **Absolute temporary paths in `benchmark/reports/**` as a disclosure.** Ruled out — the matches are harness paths (`/var/folders/.../devin-compare-bench`) and base64 diagram payloads, not user data or credentials.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Absolute temporary paths in `benchmark/reports/**` as a disclosure.** Ruled out — the matches are harness paths (`/var/folders/.../devin-compare-bench`) and base64 diagram payloads, not user data or credentials.

### **agent_cross_runtime** — no runtime-mirror file was read as authority or edited; `.skilled/commands/doctor/overlay.md` and the `system-skilled-doctor` packet were read as upstream contracts only. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: **agent_cross_runtime** — no runtime-mirror file was read as authority or edited; `.skilled/commands/doctor/overlay.md` and the `system-skilled-doctor` packet were read as upstream contracts only.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **agent_cross_runtime** — no runtime-mirror file was read as authority or edited; `.skilled/commands/doctor/overlay.md` and the `system-skilled-doctor` packet were read as upstream contracts only.

### **Archived gate snapshots as live drift**: ruled out as a defect source; they are recorded run output under `benchmark/reports/`. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: **Archived gate snapshots as live drift**: ruled out as a defect source; they are recorded run output under `benchmark/reports/`.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Archived gate snapshots as live drift**: ruled out as a defect source; they are recorded run output under `benchmark/reports/`.

### **Bare `FIGMA_API_KEY` in `.utcp_config.json` as a credential-resolution defect.** Ruled out. `.utcp_config.json:79` references `${FIGMA_API_KEY}` while `.env.example:15` declares `figma_FIGMA_API_KEY`, which reads as a split; the split is documented in four places — `mcp-figma/references/mcp-wiring.md:82-95` carries an explicit mapping table, `references/troubleshooting.md:396-398` names the symptom and cause, `INSTALL-GUIDE.md:330` says a bare name fails, and `.env.example:8-9` states the prefix rule. The pairing is deliberate. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: **Bare `FIGMA_API_KEY` in `.utcp_config.json` as a credential-resolution defect.** Ruled out. `.utcp_config.json:79` references `${FIGMA_API_KEY}` while `.env.example:15` declares `figma_FIGMA_API_KEY`, which reads as a split; the split is documented in four places — `mcp-figma/references/mcp-wiring.md:82-95` carries an explicit mapping table, `references/troubleshooting.md:396-398` names the symptom and cause, `INSTALL-GUIDE.md:330` says a bare name fails, and `.env.example:8-9` states the prefix rule. The pairing is deliberate.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Bare `FIGMA_API_KEY` in `.utcp_config.json` as a credential-resolution defect.** Ruled out. `.utcp_config.json:79` references `${FIGMA_API_KEY}` while `.env.example:15` declares `figma_FIGMA_API_KEY`, which reads as a split; the split is documented in four places — `mcp-figma/references/mcp-wiring.md:82-95` carries an explicit mapping table, `references/troubleshooting.md:396-398` names the symptom and cause, `INSTALL-GUIDE.md:330` says a bare name fails, and `.env.example:8-9` states the prefix rule. The pairing is deliberate.

### **checklist_evidence** — the vendored-package sync question in the operator focus is answered above with four named blockers, each tied to a file and line; the "zero overlays today" claim rests on a computed hash comparison over all 529 recorded files, not on prose. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: **checklist_evidence** — the vendored-package sync question in the operator focus is answered above with four named blockers, each tied to a file and line; the "zero overlays today" claim rests on a computed hash comparison over all 529 recorded files, not on prose.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **checklist_evidence** — the vendored-package sync question in the operator focus is answered above with four named blockers, each tied to a file and line; the "zero overlays today" claim rests on a computed hash comparison over all 529 recorded files, not on prose.

### **Chrome version pin drift as the defect** — ruled out; `chrome-devtools-mcp@0.26.0` in `.utcp_config.json:57` matches every pinned reference in `INSTALL-GUIDE.md` and `assets/utcp-chrome-devtools-manuals.md`. The drift is the *manual set*, not the version (finding 1). -- BLOCKED (iteration 8, 1 attempts)
- What was tried: **Chrome version pin drift as the defect** — ruled out; `chrome-devtools-mcp@0.26.0` in `.utcp_config.json:57` matches every pinned reference in `INSTALL-GUIDE.md` and `assets/utcp-chrome-devtools-manuals.md`. The drift is the *manual set*, not the version (finding 1).
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Chrome version pin drift as the defect** — ruled out; `chrome-devtools-mcp@0.26.0` in `.utcp_config.json:57` matches every pinned reference in `INSTALL-GUIDE.md` and `assets/utcp-chrome-devtools-manuals.md`. The drift is the *manual set*, not the version (finding 1).

### **Compiled-routing directive as dead prose**: ruled out. `ROUTER.md:135-145` documents that no compiled activation manifest ships and that a clone without `.skilled/bin/` takes the same legacy path, so the directive has a stated fallback. -- BLOCKED (iteration 9, 1 attempts)
- What was tried: **Compiled-routing directive as dead prose**: ruled out. `ROUTER.md:135-145` documents that no compiled activation manifest ships and that a clone without `.skilled/bin/` takes the same legacy path, so the directive has a stated fallback.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Compiled-routing directive as dead prose**: ruled out. `ROUTER.md:135-145` documents that no compiled activation manifest ships and that a clone without `.skilled/bin/` takes the same legacy path, so the directive has a stated fallback.

### **core `checklist_evidence`** — partial. Playbook execution policy at `manual-testing-playbook/manual-testing-playbook.md:9` ("every scenario runs against the live `product-owner` routing contract, with no mocks") is honoured by the 7 hub-routing scenarios; it is *not* satisfied for the vendored packages' scenarios once their manuals are unregistered (finding 1). -- BLOCKED (iteration 8, 1 attempts)
- What was tried: **core `checklist_evidence`** — partial. Playbook execution policy at `manual-testing-playbook/manual-testing-playbook.md:9` ("every scenario runs against the live `product-owner` routing contract, with no mocks") is honoured by the 7 hub-routing scenarios; it is *not* satisfied for the vendored packages' scenarios once their manuals are unregistered (finding 1).
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **core `checklist_evidence`** — partial. Playbook execution policy at `manual-testing-playbook/manual-testing-playbook.md:9` ("every scenario runs against the live `product-owner` routing contract, with no mocks") is honoured by the 7 hub-routing scenarios; it is *not* satisfied for the vendored packages' scenarios once their manuals are unregistered (finding 1).

### **core `spec_code`** — partial. The hub's declared companion set at `SKILL.md:59` and `:103` names `changelog/`, `manual-testing-playbook/` and `benchmark/`; all three exist. Within this pass the spec-to-code check is limited to the playbook and the vendored registration surface. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: **core `spec_code`** — partial. The hub's declared companion set at `SKILL.md:59` and `:103` names `changelog/`, `manual-testing-playbook/` and `benchmark/`; all three exist. Within this pass the spec-to-code check is limited to the playbook and the vendored registration surface.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **core `spec_code`** — partial. The hub's declared companion set at `SKILL.md:59` and `:103` names `changelog/`, `manual-testing-playbook/` and `benchmark/`; all three exist. Within this pass the spec-to-code check is limited to the playbook and the vendored registration surface.

### **Duplicate `Local - Push Targets` title as package drift.** Two declared surfaces with different purposes, one ignored by Git. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: **Duplicate `Local - Push Targets` title as package drift.** Two declared surfaces with different purposes, one ignored by Git.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Duplicate `Local - Push Targets` title as package drift.** Two declared surfaces with different purposes, one ignored by Git.

### **feature_catalog_code** — not exercised this iteration; the vendored `feature-catalog/` trees are byte-identical copies and were covered by the hash comparison rather than re-read. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: **feature_catalog_code** — not exercised this iteration; the vendored `feature-catalog/` trees are byte-identical copies and were covered by the hash comparison rather than re-read.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **feature_catalog_code** — not exercised this iteration; the vendored `feature-catalog/` trees are byte-identical copies and were covered by the hash comparison rather than re-read.

### **Feature-catalog asymmetry across packets as a package-shape defect**: ruled out. Four vendored MCP/tool packets carry `feature-catalog/`, `mcp-code-mode` and the two workflow packets do not; tool-surface catalogs have no workflow counterpart to describe. -- BLOCKED (iteration 9, 1 attempts)
- What was tried: **Feature-catalog asymmetry across packets as a package-shape defect**: ruled out. Four vendored MCP/tool packets carry `feature-catalog/`, `mcp-code-mode` and the two workflow packets do not; tool-surface catalogs have no workflow counterpart to describe.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Feature-catalog asymmetry across packets as a package-shape defect**: ruled out. Four vendored MCP/tool packets carry `feature-catalog/`, `mcp-code-mode` and the two workflow packets do not; tool-surface catalogs have no workflow counterpart to describe.

### **FigJam mirror table drift between the README and `systems.py`.** Six rows to six declared pairs. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: **FigJam mirror table drift between the README and `systems.py`.** Six rows to six declared pairs.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **FigJam mirror table drift between the README and `systems.py`.** Six rows to six declared pairs.

### **Format `check()` degrading into a match-everything assertion on an empty antipattern**: ruled out. Both pattern branches are guarded by `[ -n ... ]`. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: **Format `check()` degrading into a match-everything assertion on an empty antipattern**: ruled out. Both pattern branches are guarded by `[ -n ... ]`.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Format `check()` degrading into a match-everything assertion on an empty antipattern**: ruled out. Both pattern branches are guarded by `[ -n ... ]`.

### **Hardcoded credentials in tracked runtime config.** Ruled out — see Confirmed-Clean Surfaces. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: **Hardcoded credentials in tracked runtime config.** Ruled out — see Confirmed-Clean Surfaces.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Hardcoded credentials in tracked runtime config.** Ruled out — see Confirmed-Clean Surfaces.

### **Kernel / skill / hub version drift.** All three schemes internally consistent and cross-cited; see the `skill_agent` row. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: **Kernel / skill / hub version drift.** All three schemes internally consistent and cross-cited; see the `skill_agent` row.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Kernel / skill / hub version drift.** All three schemes internally consistent and cross-cited; see the `skill_agent` row.

### **Knowledge-count drift in the Project README.** 67 claimed, 67 present. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: **Knowledge-count drift in the Project README.** 67 claimed, 67 present.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Knowledge-count drift in the Project README.** 67 claimed, 67 present.

### **Manual-name drift between `.utcp_config.json` and the clickup package** — ruled out; `clickup_official` is used consistently, 268 times. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: **Manual-name drift between `.utcp_config.json` and the clickup package** — ruled out; `clickup_official` is used consistently, 268 times.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Manual-name drift between `.utcp_config.json` and the clickup package** — ruled out; `clickup_official` is used consistently, 268 times.

### **Manual-name drift for figma** — ruled out; the `figma` namespace matches the `figma_*` tool vocabulary. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: **Manual-name drift for figma** — ruled out; the `figma` namespace matches the `figma_*` tool vocabulary.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Manual-name drift for figma** — ruled out; the `figma` namespace matches the `figma_*` tool vocabulary.

### **Missing shebang and banner in `benchmark/reports/**`.** Recorded run output; iteration 2 ruling honored (edge case 3). -- BLOCKED (iteration 6, 1 attempts)
- What was tried: **Missing shebang and banner in `benchmark/reports/**`.** Recorded run output; iteration 2 ruling honored (edge case 3).
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Missing shebang and banner in `benchmark/reports/**`.** Recorded run output; iteration 2 ruling honored (edge case 3).

### **Mode/packet kind mismatch.** `packetKind`, `backendKind`, `transport-axis` and the `SKILL.md` mode table agree across four modes. Not a finding. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: **Mode/packet kind mismatch.** `packetKind`, `backendKind`, `transport-axis` and the `SKILL.md` mode table agree across four modes. Not a finding.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Mode/packet kind mismatch.** `packetKind`, `backendKind`, `transport-axis` and the `SKILL.md` mode table agree across four modes. Not a finding.

### **overlay `agent_cross_runtime`** — notApplicable; no agent definition in this surface. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: **overlay `agent_cross_runtime`** — notApplicable; no agent definition in this surface.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **overlay `agent_cross_runtime`** — notApplicable; no agent definition in this surface.

### **overlay `feature_catalog_code`** — partial. `mcp-chrome-devtools/feature-catalog/mcp-parallel-instances/*.md` (6 entries) documents capabilities whose backing manuals are unregistered; `mcp-chrome-devtools/feature-catalog/dom-and-screenshot/`, `console-and-network/` and `protocol-discovery/` map onto the single live manual and are unaffected. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: **overlay `feature_catalog_code`** — partial. `mcp-chrome-devtools/feature-catalog/mcp-parallel-instances/*.md` (6 entries) documents capabilities whose backing manuals are unregistered; `mcp-chrome-devtools/feature-catalog/dom-and-screenshot/`, `console-and-network/` and `protocol-discovery/` map onto the single live manual and are unaffected.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **overlay `feature_catalog_code`** — partial. `mcp-chrome-devtools/feature-catalog/mcp-parallel-instances/*.md` (6 entries) documents capabilities whose backing manuals are unregistered; `mcp-chrome-devtools/feature-catalog/dom-and-screenshot/`, `console-and-network/` and `protocol-discovery/` map onto the single live manual and are unaffected.

### **overlay `playbook_capability`** — partial, and the source of finding 1. Playbook capability claims were checked against the registration that backs them: the hub's own 7 scenarios (MT-001..MT-007, `manual-testing-playbook.md:36-44`) map one-to-one onto the 7 files on disk, while `mcp-chrome-devtools/manual-testing-playbook/mcp-parallel-instances/` maps onto manuals absent from `.utcp_config.json`. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: **overlay `playbook_capability`** — partial, and the source of finding 1. Playbook capability claims were checked against the registration that backs them: the hub's own 7 scenarios (MT-001..MT-007, `manual-testing-playbook.md:36-44`) map one-to-one onto the 7 files on disk, while `mcp-chrome-devtools/manual-testing-playbook/mcp-parallel-instances/` maps onto manuals absent from `.utcp_config.json`.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **overlay `playbook_capability`** — partial, and the source of finding 1. Playbook capability claims were checked against the registration that backs them: the hub's own 7 scenarios (MT-001..MT-007, `manual-testing-playbook.md:36-44`) map one-to-one onto the 7 files on disk, while `mcp-chrome-devtools/manual-testing-playbook/mcp-parallel-instances/` maps onto manuals absent from `.utcp_config.json`.

### **overlay `skill_agent`** — unchanged from iteration 1; no agent definition in this surface. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: **overlay `skill_agent`** — unchanged from iteration 1; no agent definition in this surface.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **overlay `skill_agent`** — unchanged from iteration 1; no agent definition in this surface.

### **playbook_capability** — not exercised; `manual-testing-playbook/` copies are also covered by the 529-file hash comparison. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: **playbook_capability** — not exercised; `manual-testing-playbook/` copies are also covered by the 529-file hash comparison.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **playbook_capability** — not exercised; `manual-testing-playbook/` copies are also covered by the 529-file hash comparison.

### **Python script quality as a deviation source.** Fully compliant on the P0 list; no action. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: **Python script quality as a deviation source.** Fully compliant on the P0 list; no action.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Python script quality as a deviation source.** Fully compliant on the P0 list; no action.

### **Replacing `vendor-sync.py` with `/doctor:overlay` + `repin`**: ruled out with four named blockers (tree model, one-pin-vs-seven-pins, include-list packages, missing upstream-write verb). Not an effort question. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: **Replacing `vendor-sync.py` with `/doctor:overlay` + `repin`**: ruled out with four named blockers (tree model, one-pin-vs-seven-pins, include-list packages, missing upstream-write verb). Not an effort question.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Replacing `vendor-sync.py` with `/doctor:overlay` + `repin`**: ruled out with four named blockers (tree model, one-pin-vs-seven-pins, include-list packages, missing upstream-write verb). Not an effort question.

### **Routed-file existence as a defect source.** 18/18 `RESOURCE_MAP` paths and 88/88 manifest leaves resolve; no dangling leaf, no phantom reference. Not a finding. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: **Routed-file existence as a defect source.** 18/18 `RESOURCE_MAP` paths and 88/88 manifest leaves resolve; no dangling leaf, no phantom reference. Not a finding.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Routed-file existence as a defect source.** 18/18 `RESOURCE_MAP` paths and 88/88 manifest leaves resolve; no dangling leaf, no phantom reference. Not a finding.

### **Router fixture gate masking the first failure with `|| status=1`**: ruled out. Both checks run unconditionally and the combined status is 1 if either failed. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: **Router fixture gate masking the first failure with `|| status=1`**: ruled out. Both checks run unconditionally and the combined status is 1 if either failed.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Router fixture gate masking the first failure with `|| status=1`**: ruled out. Both checks run unconditionally and the combined status is 1 if either failed.

### **Self-test gates wired to scripts that do not implement `--self-test`**: ruled out. `check_hub.py`, `example_lint.py`, `flow_check.py` and `compose_board.py` each parse `--self-test` and return a non-zero count when a planted defect does not fire. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: **Self-test gates wired to scripts that do not implement `--self-test`**: ruled out. `check_hub.py`, `example_lint.py`, `flow_check.py` and `compose_board.py` each parse `--self-test` and return a non-zero count when a planted defect does not fire.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Self-test gates wired to scripts that do not implement `--self-test`**: ruled out. `check_hub.py`, `example_lint.py`, `flow_check.py` and `compose_board.py` each parse `--self-test` and return a non-zero count when a planted defect does not fire.

### **Self-tests missing from `benchmark/grader/*.py` and `benchmark/router/*.py`.** Observed but not filed: no rules line for a test requirement was verified inside this lane's budget, and the router pair is exercised by `run_fixtures.sh` against `fixtures.json` and `differential_corpus.json`. Deferred with evidence, not converted into a pass. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: **Self-tests missing from `benchmark/grader/*.py` and `benchmark/router/*.py`.** Observed but not filed: no rules line for a test requirement was verified inside this lane's budget, and the router pair is exercised by `run_fixtures.sh` against `fixtures.json` and `differential_corpus.json`. Deferred with evidence, not converted into a pass.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Self-tests missing from `benchmark/grader/*.py` and `benchmark/router/*.py`.** Observed but not filed: no rules line for a test requirement was verified inside this lane's budget, and the router pair is exercised by `run_fixtures.sh` against `fixtures.json` and `differential_corpus.json`. Deferred with evidence, not converted into a pass.

### **Shell interpolation of untrusted values on the vendor-sync write path.** Ruled out for the functions read: the write path is `shutil.copytree` / `rename` / `rmtree` over `pathlib` values, with no shell call in `copy_tree`, `carry_excluded` or `resolve_dirs`. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: **Shell interpolation of untrusted values on the vendor-sync write path.** Ruled out for the functions read: the write path is `shutil.copytree` / `rename` / `rmtree` over `pathlib` values, with no shell call in `copy_tree`, `carry_excluded` or `resolve_dirs`.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Shell interpolation of untrusted values on the vendor-sync write path.** Ruled out for the functions read: the write path is `shutil.copytree` / `rename` / `rmtree` over `pathlib` values, with no shell call in `copy_tree`, `carry_excluded` or `resolve_dirs`.

### **skill_agent** — `@deep-review` LEAF boundary held: no sub-agent, no Task tool, no delegation. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: **skill_agent** — `@deep-review` LEAF boundary held: no sub-agent, no Task tool, no delegation.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **skill_agent** — `@deep-review` LEAF boundary held: no sub-agent, no Task tool, no delegation.

### **spec_code** — `vendor.json` is a hand-authored contract with no spec carrying it; the review target names it explicitly, and `scripts/vendor-sync.py` is the only implementation that reads it. No spec-side drift found in scope. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: **spec_code** — `vendor.json` is a hand-authored contract with no spec carrying it; the review target names it explicitly, and `scripts/vendor-sync.py` is the only implementation that reads it. No spec-side drift found in scope.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **spec_code** — `vendor.json` is a hand-authored contract with no spec carrying it; the review target names it explicitly, and `scripts/vendor-sync.py` is the only implementation that reads it. No spec-side drift found in scope.

### **Stale `kernel-review.json` as a live claim.** Declared a dated record in its own text and corroborated by its `note`; no live tooling reads the filename. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: **Stale `kernel-review.json` as a live claim.** Declared a dated record in its own text and corroborated by its `note`; no live tooling reads the filename.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Stale `kernel-review.json` as a live claim.** Declared a dated record in its own text and corroborated by its `note`; no live tooling reads the filename.

### **Swallowed error in probe-tab cleanup.** `mcp-tools.md:110` ignores a failed close in `finally`; the resource is best-effort and the outer state already records the outcome. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: **Swallowed error in probe-tab cleanup.** `mcp-tools.md:110` ignores a failed close in `finally`; the resource is best-effort and the outer state already records the outcome.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Swallowed error in probe-tab cleanup.** `mcp-tools.md:110` ignores a failed close in `finally`; the resource is best-effort and the outer state already records the outcome.

### **The "38 files" SYNC note as live drift.** A dated historical entry, adjudicated in Edge Cases. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: **The "38 files" SYNC note as live drift.** A dated historical entry, adjudicated in Edge Cases.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **The "38 files" SYNC note as live drift.** A dated historical entry, adjudicated in Edge Cases.

### **The `-e` omission being one author's oversight.** The same WHY comment appears in four files, so it is a shared, deliberate convention. -- BLOCKED (iteration 6, 1 attempts)
- What was tried: **The `-e` omission being one author's oversight.** The same WHY comment appears in four files, so it is a shared, deliberate convention.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **The `-e` omission being one author's oversight.** The same WHY comment appears in four files, so it is a shared, deliberate convention.

### **The 60 KB Notion export in `context/` as a packaging leak** -- ruled out; `/context/*` ignores it and it is absent from `git ls-files context`. -- BLOCKED (iteration 10, 1 attempts)
- What was tried: **The 60 KB Notion export in `context/` as a packaging leak** -- ruled out; `/context/*` ignores it and it is absent from `git ls-files context`.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **The 60 KB Notion export in `context/` as a packaging leak** -- ruled out; `/context/*` ignores it and it is absent from `git ls-files context`.

### **The hub playbook claiming scenarios it does not ship** — ruled out; 7 declared, 7 on disk. -- BLOCKED (iteration 8, 1 attempts)
- What was tried: **The hub playbook claiming scenarios it does not ship** — ruled out; 7 declared, 7 on disk.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **The hub playbook claiming scenarios it does not ship** — ruled out; 7 declared, 7 on disk.

### **Vendored copies missing recorded files**: ruled out — every one of the 529 manifest entries resolves on disk. -- BLOCKED (iteration 7, 1 attempts)
- What was tried: **Vendored copies missing recorded files**: ruled out — every one of the 529 manifest entries resolves on disk.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Vendored copies missing recorded files**: ruled out — every one of the 529 manifest entries resolves on disk.

### **Version drift between hub authority files.** All four `1.0.28.0` carriers agree and the newest changelog matches. Not a finding. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: **Version drift between hub authority files.** All four `1.0.28.0` carriers agree and the newest changelog matches. Not a finding.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Version drift between hub authority files.** All four `1.0.28.0` carriers agree and the newest changelog matches. Not a finding.

<!-- /ANCHOR:exhausted-approaches -->
- **Batching two large `cat`s to answer two questions at once**: reading `.utcp_config.json` and `vendor.json` in a single call spent the whole 50KB output budget on `vendor.json`'s per-file sha256 map and truncated the config that was the actual subject. One artifact per call when either can exceed the cap. (iteration 8)

---

## 10A. SATURATED / SWEPT DIMENSIONS AND EXPANSION FRONTIER
- Completed pivots: 0
- Failed pivots: 0
- Audited overrides: 0
- Swept: none yet
- Pivot lineage: none yet
- Remaining frontier: none recorded

## 11. RULED OUT DIRECTIONS
- **UNVERIFIED item closed at iteration 10:** the `.gitignore:34-37` claim that `context/.gitkeep` and `context/README.md` stay tracked was re-run as `git ls-files context`. Both are tracked, `git ls-files --error-unmatch` accepts both, and the 60 KB reference file beside them is ignored by `/context/*`. Clean; not a finding.
- **USER-GUIDE.md numeric drift:** ruled out (iteration 10, evidence: no version string and no `N files|scenarios|entries|documents|modes|packets` claim present)
- **graph-metadata.json as a duplicate hub identity:** ruled out (iteration 10, evidence: one `skill_id` `product-owner`, empty `depends_on` and `conflicts_with`, agreeing with `SKILL.md:72`)
[Review angles that were investigated and definitively eliminated -- consolidated from iteration dead-end data]
- Dangling routed leaf: ruled out (iteration 1, evidence: 18/18 `AI Systems/Product Owner/ROUTER.md:96-132` paths and 88/88 `AI Systems/Product Owner/leaf-manifest.json` leaves present on disk)
- Hub version drift: ruled out (iteration 1, evidence: `AI Systems/Product Owner/SKILL.md:5`, `hub-router.json:3`, `mode-registry.json:3`, `description.json:4` all `1.0.28.0`; `changelog/v1.0.28.0.md:9` newest)
- `DEFAULT_RESOURCE` vs `routerPolicy.defaultResource` collision: ruled out as drift (iteration 1, evidence: `AI Systems/Product Owner/ROUTER.md:37` distinguishes them; `hub-router.json:22` sets `fallback-only`)
- Mode / `packetKind` / `transport-axis` mismatch: ruled out (iteration 1, evidence: `SKILL.md:22-27` vs `mode-registry.json:56/90/119/150`)
- `mcp-code-mode/leaf-manifest.json` as a violation of `SKILL.md:87`: ruled out (iteration 1, evidence: `SKILL.md:72` exempts it; it is a vendored server, not a packet)
- `leaf-manifest.json` mode ordering vs `hub-router.json` `tieBreak`: ruled out (iteration 1, evidence: generated ordering vs routing policy, no behavioural path)
- `documentation`/`clarify` absent from `vocabularyClasses.artifact-request-nouns`: ruled out (iteration 1, evidence: both the artifact-request rule and the single-signal rule resolve to `defaultMode` `sk-product-owner`, identical outcome)
- Self-test gate wired to a script without `--self-test`: ruled out (iteration 2, evidence: `check_hub.py:701`, `example_lint.py:337`, `flow_check.py:636`, `compose_board.py:1761`)
- `vendor sync tests` gate that cannot fail: ruled out (iteration 2, evidence: `scripts/tests/test_vendor_sync.py:352` runs `unittest.main(verbosity=2)`)
- Runner exit-code mishandling: ruled out (iteration 2, evidence: `run_gates.sh:99-108`, `benchmark/router/run_fixtures.sh:28`, `benchmark/format/run_fixtures.sh:250`)
- Skip guard vs script path or env-var drift: ruled out (iteration 2, evidence: `run_gates.sh:66` == `rule_parity.py:68`; `VENDOR_UPSTREAM_ROOT` matches `vendor-sync.py:103`)
- Format fixture assertion that can never fire: ruled out (iteration 2, evidence: `benchmark/format/run_fixtures.sh:52` guards both pattern branches with `[ -n ... ]`)
- Archived gate snapshots under `benchmark/reports/**` as live drift: ruled out (iteration 2, evidence: recorded run output, not the live gate)
- Hardcoded credential in committed runtime config: ruled out (iteration 3, evidence: `AI Systems/Product Owner/.utcp_config.json:79` is `${FIGMA_API_KEY}`, `.env.example:15` is empty, `.mcp.json` and `opencode.json` only set `UTCP_CONFIG_FILE`)
- Ignored private files surviving in git history: ruled out (iteration 3, evidence: `git ls-files` has no entry for `.env`, `click-up-links.md` or `claude project/local/`; `git check-ignore -v` maps them to `.gitignore:10/16/15`)
- Bare-versus-prefixed `FIGMA_API_KEY` as a defect: ruled out (iteration 3, evidence: `AI Systems/Product Owner/mcp-figma/references/mcp-wiring.md:82-95` mapping table, `references/troubleshooting.md:396-398` symptom entry)
- Shell interpolation on the vendor-sync write path: ruled out (iteration 3, evidence: `AI Systems/Product Owner/scripts/vendor-sync.py:403-447` uses `shutil.copytree`/`rename`/`rmtree` over `pathlib` values)
- Manifest path traversal in `vendor-sync.py`: ruled out (iteration 3, evidence: `:322` refuses `..`, absolute and backslash; `:363-367` resolve-checks `local_dir` and refuses the repo root)
- Absolute temp paths under `benchmark/reports/**` as disclosure: ruled out (iteration 3, evidence: harness paths such as `/var/folders/.../devin-compare-bench` and base64 diagram payloads)
- **UNVERIFIED, carried forward:** the `.gitignore:34-37` claim that `context/.gitkeep` and `context/README.md` stay tracked — the check used a `/context/` pattern that cannot match a repo-relative path. Re-run as `git ls-files context`.
- `sk-product-owner/SKILL.md:290` "the 68 artifact scenarios" as a stale count: ruled out (iteration 8, evidence: 69 markdown files under `sk-product-owner/manual-testing-playbook/` = 1 index + 68 scenarios)
- Hub playbook claiming scenarios it does not ship: ruled out (iteration 8, evidence: `manual-testing-playbook/manual-testing-playbook.md:28` declares 7, `hub-routing/` holds 7 files, table at `:36-44` lists MT-001..MT-007)
- Clickup manual-name drift between `.utcp_config.json` and `mcp-click-up`: ruled out (iteration 8, evidence: `clickup_official` appears 268 times across `mcp-click-up/**/*.md`, matching `.utcp_config.json:16`)
- Figma manual-name drift: ruled out (iteration 8, evidence: `figma_*` tool vocabulary resolves under the registered `figma` manual at `.utcp_config.json:66`)
- A second `.utcp_config.json` in the target carrying the isolated chrome manuals: ruled out (iteration 8, evidence: exactly one config, four `manual_call_templates`, none named `chrome_devtools_1`/`_2`/`_3`)
- Chrome version-pin drift as the defect: ruled out (iteration 8, evidence: `chrome-devtools-mcp@0.26.0` consistent at `.utcp_config.json:57`, `INSTALL-GUIDE.md:933` and `assets/utcp-chrome-devtools-manuals.md:69`; the drift is the manual set, not the version)
- Kernel / skill / hub version drift: ruled out (iteration 5, evidence: kernel H1 `v1.2.18` matches `SYNC.md` bullet and `claude project/README.md:11,63`; skill `1.2.16.0` matches `sk-product-owner/SKILL.md:5`, `sk-product-owner/changelog/v1.2.16.0.md` and `README.md:63`; hub `1.0.28.0` matches `changelog/v1.0.28.0.md`)
- Stale `claude project/kernel-review.json` (0.8.0 against a live 1.2.18) as a live claim: ruled out (iteration 5, evidence: the file's own `note` declares it a dated record, and no live tooling references the filename outside `SYNC.md` prose and archived `feature-catalog/` and `episodes/` documents)
- `claude project/local/` as a private-data leak into the tracked package: ruled out (iteration 5, evidence: `.gitignore:15` ignores the folder, `git ls-files` returns only the blank `claude project/templates/` copy)
- Knowledge-count drift between the Project upload guide and `claude project/knowledge/`: ruled out (iteration 5, evidence: `README.md:16,146` claim 67, directory holds 67, arithmetic 37 core + 30 Examples reconciles)
- Duplicate `Local - Push Targets` document title across `claude project/local/` and `claude project/templates/`: ruled out (iteration 5, evidence: `README.md:14-15` declares scaffold versus filled copy, and the diff is placeholder-to-value only)
- FigJam mirror-table drift between `claude project/README.md:97-102` and `systems.py:1831-1841`: ruled out (iteration 5, evidence: six README rows against six declared `../sk-create-figjam/assets/templates/` pairs)
- `feature_catalog_code` gap for this system: ruled out as notApplicable (iteration 5, evidence: no Product Owner feature catalog exists; the fleet catalog under `z — Claude Project Sync Loop/feature-catalog/` documents the gate, not this source)
- The 2026-09-17 SYNC note's "thirty-eight files" as live drift: ruled out (iteration 5, evidence: a dated entry records what was true when written, per `SYNC.md`'s own 2026-09-18 entry)
- `references/README.md` absent from both packets: ruled out (iteration 4, evidence: 0 of 8 installed skills with a top-level `references/` folder ship one; `sk-create-skill/SKILL.md:48` describes that packet's own route map)
- `procedures/` absent from the workflow packets: ruled out (iteration 4, evidence: conditional rule at `sk-create-skill/SKILL.md:167`; the reference packet `sk-create-skill` has no `procedures/`)
- `benchmark/` shape deviation: ruled out (iteration 4, evidence: `benchmark/README.md` present; `benchmark/reports/` folders follow `<YYYY-MM-DD>--<subject>--<variant>`)
- `leaf-manifest.config.json` absent at the hub root: ruled out (iteration 4, evidence: the parent-hub shape at `sk-create-skill/SKILL.md:203-215` lists no such file; only class-S standalone skills author one)
- `SKILL.md` frontmatter contract: ruled out (iteration 4, evidence: `SKILL.md:2-5`, `sk-product-owner/SKILL.md:2-5`, `sk-create-figjam/SKILL.md:2-5` all carry name/description/allowed-tools/four-part version; names match folders)

- Two independent sync mechanisms (`vendor-sync.py` and `/doctor:overlay`) with disjoint verbs and no cross-reference in `scripts/README.md`, `README.md`, `AGENTS.md`, `SYNC.md` or `USER-GUIDE.md`: finding 9 (iteration 7)
- `/doctor:overlay` + `repin` as a replacement for `vendor-sync.py`: ruled out (iteration 7, evidence: `overlay-engine.cjs:73` `VENDOR_ROOT`, `:2606` repin diff scope, four differing `base_commit` values, two `include`-scoped packages, no upstream-write verb)
- Local overlays already carried by the vendored packages: ruled out (iteration 7, evidence: 529/529 recorded files match their sha256, 0 drift, 0 missing across 7 packages)
- `exclude` and `include` both set on one package: ruled out (iteration 7, evidence: `vendor-sync.py:357` refuses it and `vendor.json` respects it)
- Recorded manifest file absent from the vendored copy: ruled out (iteration 7, evidence: all 529 entries resolve on disk)
- `overlay-manifest.json` / `.skilled-overlays.json` present but orphaned in Product Owner: ruled out (iteration 7, evidence: neither exists in the target)

---

<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
- **Dimension:** terminal -- all four dimensions are complete (correctness replayed here, security at iteration 3, traceability at iteration 4, maintainability at iteration 9). - **Focus area:** none; the loop reached `max-iterations` with 4 P1 and 21 P2 active. - **Reason:** `stopPolicy: max-iterations` -- all 10 iterations run and convergence is telemetry only. Hand-off is to `/speckit:plan` for the four P1s, in the order R10-REF-001, R10-REF-002, R10-REF-003, then R3-P1-001. - **Rotation status:** closed. - **Blocked/productive carry-forward:** productive -- the three refinements are remediation-ready and each names the exact edit surface. - **Required evidence:** none outstanding. - **Recovery note:** budget edge case 4 above is the one process deviation; it did not change a finding. Review verdict: CONDITIONAL

<!-- /ANCHOR:next-focus -->
## 13. KNOWN CONTEXT
[Populated during initialization from the continuity ladder and ripgrep recipes, if any prior work exists]

### Bounded Context Snapshot

Populate during initialization before the first review dimension runs. Keep this pointer-based and scoped to the declared review target:

- Target pointers: files, specs, symbols, or resource-map entries under review.
- Behavior claims: acceptance criteria, public contracts, or docs to verify.
- Reuse and conventions: existing patterns that define expected implementation shape.
- Review risks and gaps: stale graph or memory caveats, missing files, and out-of-scope areas.

Do not inline full source bodies. Do not dispatch the retired standalone context loop. Use this snapshot only to seed review dimensions and final traceability.

---

## 14. CROSS-REFERENCE STATUS
<!-- MACHINE-OWNED: START -->
[Alignment checks completed across core and overlay protocols]

| Protocol | Level | Status | Iteration | Notes |
|----------|-------|--------|-----------|-------|
| `spec_code` | core | partial | 4 | `sk-create-skill/SKILL.md:98-121` standalone shape and `:203-231` parent-hub shape diffed against both packet trees and the hub root; shape elements match except the changelog placement recorded as R4-P2-001 |
| `checklist_evidence` | core | partial | 4 | every finding cites the exact rule line it breaks: `sk-create-changelog/SKILL.md:10` for R4-P2-001, `sk-create-skill/SKILL.md:95` for R4-P2-002 |
| `skill_agent` | overlay | partial | 4 | three `SKILL.md` frontmatters satisfy `sk-create-skill/SKILL.md:144-149`; names match folders; versions `1.0.28.0`, `1.2.16.0`, `1.0.18.0` |
| `agent_cross_runtime` | overlay | notApplicable | 4 | no agent definition in this surface |
| `feature_catalog_code` | overlay | notApplicable | 4 | no feature catalog under the hub and no Product Owner artifact routes to `sk-create-feature-catalog`; the `feature-catalog` playbook pages exist only on the Sync Loop side |
| `playbook_capability` | overlay | pass | 4 | hub index declares the four-mode scope and result persistence, `hub-routing/` holds 7 scenario files, `benchmark/reports/` folders follow the contracted dated grammar |
<!-- MACHINE-OWNED: END -->

---

## 15. FILES UNDER REVIEW
<!-- MACHINE-OWNED: START -->
[Per-file coverage state table -- populated during initialization from scope discovery]

| File | Dimensions Reviewed | Last Iteration | Findings | Status |
|------|-------------------|----------------|----------|--------|
| `SKILL.md` | D1 | 1 | 0 P0, 1 P1, 1 P2 | partial |
| `ROUTER.md` | D1 | 1 | 0 P0, 0 P1, 2 P2 | partial |
| `hub-router.json` | D1 | 1 | 0 P0, 0 P1, 0 P2 | partial |
| `mode-registry.json` | D1 | 1 | 0 P0, 0 P1, 1 P2 (jointly with `SKILL.md:69`) | partial |
| `leaf-manifest.json` | D1 | 1 | none (88/88 leaves resolve) | complete |
| `description.json` | D1 | 1 | none (version parity holds) | complete |
| `sk-product-owner/SKILL.md` | D1 | 1 | none at frontmatter/version level | partial (Section 2 unread) |
| `sk-product-owner/ROUTER.md` | D1 | 1 | none at heading level; shape is finding 1 evidence | partial |
| `benchmark/gates/check_hub.py` | D1 | 1 | none (its contract is the corroborating evidence for finding 1) | partial |
| `benchmark/hub-routing-cases.json` | D1 | 1 | none checked (present, not replayed) | not started |
| `changelog/v1.0.28.0.md` | D1 | 1 | none | complete |
| `benchmark/gates/run_gates.sh` | D1 | 2 | 0 P0, 0 P1, 2 P2 (findings 6, 7) | partial |
| `benchmark/format/run_fixtures.sh` | D1 | 2 | none directly; its hard-coded validator path is finding 5 evidence | partial |
| `benchmark/format/validate-output-format.cjs` | D1 | 2 | 0 P0, 1 P1 (finding 5, jointly with the Sync Loop copy) | partial |
| `z — Claude Project Sync Loop/validate-output-format.cjs` | D1 | 2 | 0 P0, 1 P1 (finding 5, jointly) | partial |
| `z — Claude Project Sync Loop/run_fixtures.sh` | D1 | 2 | none (argument contract is finding 5 evidence) | partial |
| `benchmark/router/run_fixtures.sh` | D1 | 2 | none (exit combination verified) | complete |
| `scripts/vendor-sync.py` | D1 | 2 | none (setup and exit paths verified) | partial (containment unread) |
| `scripts/tests/test_vendor_sync.py` | D1 | 2 | none (`__main__` guard and exit assertions present) | complete |
| `benchmark/gates/rule_parity.py` | D1 | 2 | none (path derivation agrees with the runner) | partial (body unread) |
| `benchmark/parity/*.sh` | D1 | 2 | 0 P0, 0 P1, 1 P2 (finding 6: never invoked) | partial (bodies unread) |
| `.gitignore` | D2 | 3 | 0 P0, 1 P1 (R3-P1-001, no artifact boundary) | partial (context/ claim unverified) |
| `.env.example`, `.mcp.json`, `opencode.json`, `.utcp_config.json` | D2 | 3 | none (placeholders only) | complete |
| `mcp-chrome-devtools/SKILL.md`, `references/cdp-patterns.md` | D2 | 3 | 0 P0, 1 P1 (R3-P1-001) | partial (other references unread) |
| `mcp-aside-devtools/SKILL.md` | D2 | 3 | 0 P0, 0 P1, 1 P2 (R3-P2-002) | partial |
| `scripts/vendor-sync.py` | D1, D2 | 3 | 0 P0, 0 P1, 1 P2 (R3-P2-003) | partial (CLI tail unread) |
| `changelog/` (hub) | D3 | 4 | 0 P0, 0 P1, 1 P2 (R4-P2-001) | partial (29 entries, all packet-local) |
| `sk-product-owner/changelog/` | D3 | 4 | 0 P0, 0 P1, 1 P2 (R4-P2-001, jointly) | partial (44 entries) |
| `sk-create-figjam/changelog/` | D3 | 4 | 0 P0, 0 P1, 1 P2 (R4-P2-001, jointly) | partial (19 entries) |
| `.gitignore` | D3 | 4 | 0 P0, 0 P1, 1 P2 (R4-P2-002) | partial |
| `SKILL.md` (hub frontmatter) | D3 | 4 | none (four-field contract satisfied) | complete |
| `sk-product-owner/SKILL.md` (frontmatter) | D3 | 4 | none | complete |
| `sk-create-figjam/SKILL.md` (frontmatter) | D3 | 4 | none | complete |
| `manual-testing-playbook/manual-testing-playbook.md` | D3 | 4 | none (index, persistence contract and 7 scenario files present) | complete |
| `benchmark/README.md` + `benchmark/reports/` | D3 | 4 | none (shape matches contract) | complete |
| `sk-product-owner/{references,assets}/` | D3 | 4 | none at shape level | partial (bodies unread) |
| `sk-create-figjam/{references,assets,scripts}/` | D3 | 4 | 0 P0, 0 P1, 1 P2 (R4-P2-002, joint) | partial (bodies unread) |
<!-- MACHINE-OWNED: END -->

---

## 16. REVIEW BOUNDARIES
<!-- MACHINE-OWNED: START -->
- Max iterations: 10
- Convergence threshold: 0.1
- Rolling STOP threshold: 0.08
- No-progress threshold: 0.05
- Coverage stabilization passes required: 1
- Session lineage: sessionId=2026-11-10T20:08:17Z, parentSessionId=null, generation=1, lineageMode=new
- Findings registry: `deep-review-findings-registry.json`
- Release-readiness states: in-progress | converged | release-blocking
- Per-iteration budget: 12 tool calls, 10 minutes
- Severity threshold: P2
- Review target type: directory
- Cross-reference checks: core=spec_code, checklist_evidence; overlay=skill_agent, agent_cross_runtime, feature_catalog_code, playbook_capability
- Stop policy: max-iterations (all 10 run; convergence is telemetry only)
- Client-side write exclusion: `AI Systems/Product Owner/.env` is never opened or quoted (operator instruction)
- Started: 2026-11-10T20:08:17Z
| `SKILL.md:66` layout gloss | D4 | 9 | 1 P2 (finding 8) | reviewed |
| `AGENTS.md:190-274` | D4 | 9 | 1 P2 (finding 9) | partial (gate coverage unverified) |
| `vendor.json` | D4 | 9 | 1 P2 (finding 10) | partial (hashes read, no sync run) |
| `SYNC.md` | D4 | 9 | 1 P2 (finding 12) | partial (shape measured, rows unread) |
| `claude project/kernel-review.json` | D4 | 9 | 1 P2 (finding 11) | reviewed |
| `/doctor:overlay` command | D4 | 9 | none (comparison surface for finding 10) | partial |
<!-- MACHINE-OWNED: END -->

---

## 17. EXAMPLE (POPULATED)

Reference snippet showing a partially populated strategy file mid-review. Use this as a visual anchor when opening a live strategy doc.

```markdown
## 1. REVIEW CHARTER
- Target: .skilled/skills/system-deep-loop/deep-research (skill, v1.4.0)
- Dimensions: correctness, test-coverage, cross-runtime-parity, observability
- Stop conditions: rolling newInfoRatio < 0.08 for 2 iterations OR all dimensions converged OR max=7 reached
- Success criteria: zero P0 in correctness; test-coverage P0 resolved or deferred with rationale

## 4. NEXT FOCUS
- Dimension: test-coverage
- Files: .skilled/skills/system-deep-loop/deep-research/scripts/reduce-state.cjs, .skilled/skills/system-spec-kit/runtime/cli/tests/deep-research-contract-parity.vitest.ts
- Why: Iteration 2 surfaced a P0 (convergence-path coverage gap); needs a focused follow-up before correctness can terminate PASS.

## 9. COVERAGE MATRIX
| Dimension            | Status     | Iterations touched |
|----------------------|------------|--------------------|
| correctness          | converged  | 1                  |
| test-coverage        | converging | 2, 4               |
| cross-runtime-parity | converging | 3                  |
| observability        | converging | 4                  |
```
