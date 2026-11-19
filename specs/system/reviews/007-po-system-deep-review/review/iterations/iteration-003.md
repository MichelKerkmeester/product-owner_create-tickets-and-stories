# Review Iteration 003 — Security

## Dispatcher
- Resolved route: `mode=review`, `target_agent=deep-review`, iteration 3 of 10, dimension `security`.
- Budget profile: `verify` — 13 tool calls used of a hard max of 13.
- Lineage: sessionId `2026-11-10T20:08:17Z`, generation 1, lineageMode `new`, run `054-po-system-deep-review`.
- Packet root: `specs/054-po-system-deep-review/review/`. Target `AI Systems/Product Owner` was read-only for this pass.

## Dimension
security — secrets and trust boundaries. This pass covered the committed runtime configuration
(`.mcp.json`, `.utcp_config.json`, `opencode.json`, `.env.example`, `.gitignore`, `click-up-links.md`), the
private-material boundary of the public Product Owner repository, browser automation and its evidence artifacts in
`mcp-aside-devtools` and `mcp-chrome-devtools`, and the whole-tree write path in `scripts/vendor-sync.py`.
`AI Systems/Product Owner/.env` was never opened, per the operator instruction recorded in strategy section 16.

## Files Reviewed
- `AI Systems/Product Owner/.gitignore:1-46` — ignore rules for `.env`, `click-up-links.md`, `claude project/local/`, `context/`, containment snapshots.
- `AI Systems/Product Owner/.env.example:1-16` — the tracked key list; empty assignments only.
- `AI Systems/Product Owner/.mcp.json:1-13`, `AI Systems/Product Owner/opencode.json:1-15` — both only set `UTCP_CONFIG_FILE` and run `node scripts/code-mode.cjs`.
- `AI Systems/Product Owner/.utcp_config.json` (manual_call_templates) — one credential reference at `:79`, three manuals with `env: {}`.
- `AI Systems/Product Owner/mcp-chrome-devtools/SKILL.md`, `AI Systems/Product Owner/mcp-chrome-devtools/references/cdp-patterns.md:63-63,191-210,412-460,570-573`.
- `AI Systems/Product Owner/mcp-aside-devtools/SKILL.md:126-142,186-206`, `AI Systems/Product Owner/mcp-aside-devtools/feature-catalog/devtools-parity/cookies-and-storage.md:19`, `AI Systems/Product Owner/mcp-aside-devtools/references/session-management.md:54`.
- `AI Systems/Product Owner/mcp-figma/references/mcp-wiring.md:67-95`, `AI Systems/Product Owner/mcp-figma/references/troubleshooting.md:396-407`.
- `AI Systems/Product Owner/scripts/vendor-sync.py:296-465` — `contained_path`, `resolve_dirs`, `carry_excluded`, `copy_tree`.
- Repository tracking state via `git rev-parse --show-toplevel`, `git ls-files`, `git check-ignore -v`.

## Findings - New

### P0 Findings

None. No active blocker was found in this pass.

### P1 Findings

1. **Browser evidence artifacts carry live session secrets with no redaction rule and no ignore boundary** -- `AI Systems/Product Owner/mcp-chrome-devtools/references/cdp-patterns.md:412` -- The packet teaches `bdg network har output.har` followed by a `jq` analysis step, `bdg network getCookies`, a cookie-set example whose literal value is `"secret-token-123"` (`:445-448`), and a "Batch cookie extraction" loop (`:570-573`). A HAR export carries request and response headers by format, so it carries `Cookie` and `Authorization` verbatim. The packet's own `SKILL.md` states no redaction rule: a grep for `redact|credential|secret|cookie` across it returns only `:3`, `:10`, `:19`, `:21` and `:190`, where `:21` offers "cookie manipulation" as a supported use case. The hub carries no such rule either — `SKILL.md` and `ROUTER.md` match only Figma design-token vocabulary. `.gitignore` has no rule for `*.har`, images or captured artifacts (a pattern grep exits 1), and the export command writes the relative filename `output.har`, so the artifact lands in the repository that was opened, which is the public Product Owner repo. The sibling packet proves the fleet does have the convention: `mcp-aside-devtools/SKILL.md:135` states it as ALWAYS rule 6.
   Finding class: rule-gap in a vendored packet's trust boundary
   Scope proof: `mcp-chrome-devtools/`, `mcp-aside-devtools/SKILL.md` and the root `.gitignore` are all inside the declared review scope; no evidence was drawn from outside the target.
   Affected surface hints: `AI Systems/Product Owner/mcp-chrome-devtools/SKILL.md` (rule block), `AI Systems/Product Owner/mcp-chrome-devtools/references/cdp-patterns.md` (artifact-writing recipes), `AI Systems/Product Owner/.gitignore` (artifact ignore boundary).
   Case: An operator asks why a logged-in page returns 401; the agent runs `bdg network har output.har` in the repository root, the HAR lands as an untracked file holding the session cookie and bearer header, and a later `git add -A` in the public Product Owner repo commits it.

   Claim adjudication:
   ```json
   {"type":"rule_gap","claim":"A reviewed packet teaches HAR and cookie export into the working tree while neither the packet, the hub, nor .gitignore provides a redaction or ignore boundary for the resulting secret-bearing artifact.","evidenceRefs":["AI Systems/Product Owner/mcp-chrome-devtools/references/cdp-patterns.md:412","AI Systems/Product Owner/mcp-chrome-devtools/references/cdp-patterns.md:445","AI Systems/Product Owner/mcp-chrome-devtools/references/cdp-patterns.md:570","AI Systems/Product Owner/mcp-chrome-devtools/SKILL.md:21","AI Systems/Product Owner/mcp-aside-devtools/SKILL.md:135","AI Systems/Product Owner/.gitignore:1-46"],"counterevidenceSought":"searched the packet SKILL.md for a redaction rule (4 hits, none a rule), searched hub SKILL.md and ROUTER.md for secret/credential/redact/cookie (only Figma design-token hits), searched .gitignore for har/png/cookie patterns (no match)","alternativeExplanation":"the operator is expected to route artifacts under export/, which is gitignored, so the leak requires the agent to write into the tree root","finalSeverity":"P1","confidence":"medium-high","downgradeTrigger":"downgrade to P2 if the hub SKILL.md ALWAYS rules are shown to forbid persisting secret-bearing artifacts, or if .gitignore gains a *.har and captured-artifact rule"}
   ```

### P2 Findings

2. **The one redaction rule the fleet does have is scoped to an undefined term and weaker than its own leaf** -- `AI Systems/Product Owner/mcp-aside-devtools/SKILL.md:135` -- ALWAYS rule 6 reads "Redact cookies, credentials, private DOM, and request headers/bodies from default logs". "Default logs" is never defined in the packet: a grep across both browser packets finds the phrase only in restatements (`SKILL.md:135`, `references/troubleshooting.md:33`, `references/session-management.md:54`) and once in a strict form, in a catalog leaf two routing hops below the skill — `feature-catalog/devtools-parity/cookies-and-storage.md:19` says "redact values from any saved evidence". The skill body permits what its leaf forbids, and the capability that produces saved evidence is documented in the same body at `:205` (`page.context().cookies()` / `page.evaluate(localStorage)`).
   Finding class: rule-scope ambiguity against a documented capability
   Scope proof: read within `mcp-aside-devtools/`; the leaf cited is inside the declared scope; no claim is made about unread leaves.
   Affected surface hints: `AI Systems/Product Owner/mcp-aside-devtools/SKILL.md:135`, `AI Systems/Product Owner/mcp-aside-devtools/feature-catalog/devtools-parity/cookies-and-storage.md:19`.
   Case: An agent captures `page.context().cookies()` as evidence and saves the JSON beside the transcript; rule 6 forbids only "default logs", so a saved evidence file sits outside its letter while the catalog leaf forbids exactly that.
   Claim adjudication:
   ```json
   {"type":"rule_scope","claim":"ALWAYS rule 6 governs an undefined artifact class, and a stricter sibling rule lives outside the skill body.","evidenceRefs":["AI Systems/Product Owner/mcp-aside-devtools/SKILL.md:135","AI Systems/Product Owner/mcp-aside-devtools/feature-catalog/devtools-parity/cookies-and-storage.md:19","AI Systems/Product Owner/mcp-aside-devtools/references/session-management.md:54"],"counterevidenceSought":"grepped for an explicit definition of 'default logs' in both browser packets; found restatements only","alternativeExplanation":"'default logs' may be an operator-vernacular phrase understood to include saved evidence, making the leaf a clarification rather than a contradiction","finalSeverity":"P2","confidence":"medium","downgradeTrigger":"not applicable; already at the lowest tier"}
   ```

3. **`vendor-sync.py` validates its discovered upstream root but not its override root** -- `AI Systems/Product Owner/scripts/vendor-sync.py:105` -- `find_upstream_root` accepts `VENDOR_UPSTREAM_ROOT` with `return Path(override)` and no marker, resolve or containment check, while the auto-discovery branch resolves candidates before accepting them (`:213`, `:234`). `resolve_dirs` then joins `upstream_rel` onto that unchecked root and validates only `is_dir()` (`:371-374`); `contained_path` guards the spelling of the relative path, and its own docstring at `:316-318` claims an escape is "refused on any side", which is true of the manifest value but not of the root it is joined to. A mistyped override still fails loudly when the joined path is absent, so this is a validation asymmetry rather than an exploit path: the risk is syncing a wrong-but-real tree over a package directory.
   Finding class: unvalidated environment input on a whole-tree write path
   Scope proof: `scripts/vendor-sync.py` is a named review-scope file; only the read and write paths named in the dispatch focus were examined.
   Affected surface hints: `AI Systems/Product Owner/scripts/vendor-sync.py:105`, `:213-234`, `:359-374`, `:428-447` (the pull/retire swap that acts on the resolved tree).
   Case: An operator exports `VENDOR_UPSTREAM_ROOT` to a shared volume that happens to contain the same relative package paths; `is_dir()` passes, and `copy_tree` replaces the vendored package with that volume's content, whose recorded hashes then differ from `vendor.json`.
   Claim adjudication:
   ```json
   {"type":"input_validation","claim":"The override branch of upstream discovery performs fewer checks than the discovery branch it overrides.","evidenceRefs":["AI Systems/Product Owner/scripts/vendor-sync.py:105","AI Systems/Product Owner/scripts/vendor-sync.py:213","AI Systems/Product Owner/scripts/vendor-sync.py:371","AI Systems/Product Owner/scripts/vendor-sync.py:303"],"counterevidenceSought":"read the docstring at :316-318 to test whether the gap is deliberate; it justifies spelling-only containment for the manifest value, not for the root","alternativeExplanation":"the override is an operator escape hatch and the operator is trusted, so validating it is redundant","finalSeverity":"P2","confidence":"high","downgradeTrigger":"not applicable; already at the lowest tier"}
   ```

## Traceability Checks

| Protocol | Level | Result |
|----------|-------|--------|
| `spec_code` | core | partial — the `.gitignore` claims at `:9-12`, `:14-16`, `:34-37` were checked against `git check-ignore -v` and `git ls-files`; two of the three claims verified, the `context/` claim was not verified (see Edge Cases). |
| `checklist_evidence` | core | partial — `mcp-aside-devtools/SKILL.md:128-142` ALWAYS/NEVER read line by line against the packet's references; ALWAYS 6 is narrower than its own catalog leaf (finding 2). |
| `skill_agent` | overlay | notApplicable — no agent definition in this surface; the two browser packets are skills, checked as skill bodies. |
| `agent_cross_runtime` | overlay | notApplicable — no runtime mirror is in scope for the browser packets. |
| `feature_catalog_code` | overlay | partial — `feature-catalog/devtools-parity/cookies-and-storage.md:19` was read as the contradicting side of finding 2 and as corroboration for finding 1's convention claim. |
| `playbook_capability` | overlay | notApplicable this pass — no playbook body was read in the security dimension; carried to a later iteration. |

## Integration Evidence
- Hub routing surface: `AI Systems/Product Owner/SKILL.md` and `AI Systems/Product Owner/ROUTER.md` were grepped, not assumed — they carry no secret-handling rule, which is the negative evidence finding 1 needs.
- Sibling-packet convention: `mcp-aside-devtools/SKILL.md:135` is named as the exact surface that has the rule `mcp-chrome-devtools` lacks.
- Credential wiring chain: `.env.example:8-15` → `.utcp_config.json:79` → `mcp-figma/references/mcp-wiring.md:82-95` → `mcp-figma/references/troubleshooting.md:396-398`, read as a chain, which is why the bare-name reference is ruled out rather than reported.
- Repository boundary: `git rev-parse --show-toplevel` returns `AI Systems/Product Owner`, so the ignore rules audited govern every vendored packet at once; no nested repository was found.

## Edge Cases
- **Review doctrine not re-read.** `sk-code-review/references/review-core.md` was not loaded this iteration: the 13-call budget was exhausted on the target surface. Severity was assigned with the P0/P1/P2 discipline already applied in iterations 1 and 2 and restated in the dispatch prompt. Recorded as unverified, not as a pass; iteration 4 carries it as required evidence.
- **`context/` tracking state unestablished.** The `git ls-files` check used a `/context/` pattern that requires a leading slash, so a repo-relative `context/...` path could not match. The `.gitignore:34-37` claim that `context/.gitkeep` and `context/README.md` stay tracked is therefore neither confirmed nor refuted. Deferred, not passed.
- **`.env` contents unknown by design.** The operator prohibition means nothing in this iteration asserts what the local `.env` holds. What was verified is narrower and stated as such: `.env` exists with mode `-rw-------`, and is untracked.
- **HAR severity rests on format semantics.** The claim that a HAR carries cookies and auth headers is a property of the HAR format, not a file read in this repo; it is stated as format semantics and is the reason the finding is about the missing boundary rather than about a specific leaked file.
- **Secret-pattern sweep is lexical.** The sweep cannot see a secret that matches none of its patterns; "no credential found" means no match, not "no credential present".

## Confirmed-Clean Surfaces
- `.env` — present on disk, mode `-rw-------`, untracked (`git check-ignore -v` → `.gitignore:10`; `git ls-files` no hit). Contents not read.
- `click-up-links.md` — present (813 B), untracked, ignored by `.gitignore:16`. Never committed, so the ignore rule was not bypassed.
- `claude project/local/Product Owner - Local - Push Targets.md` — present, untracked, ignored by `.gitignore:15`.
- `.env.example` — tracked, 16 lines, every assignment empty. No value to leak.
- `.mcp.json` and `opencode.json` — hold no secret; both only set `UTCP_CONFIG_FILE` and run `node scripts/code-mode.cjs`.
- `.utcp_config.json` — one credential reference (`:79`), three manuals with `env: {}`; the clickup, aside and chrome transports declare no token field.
- Secret-pattern sweep over tracked `.json/.md/.py/.cjs/.js/.sh` — matches only in `mcp-code-mode/` documentation as placeholders (`pk_your_api_key_here`, `pk_1234567890_ACTUAL_KEY_HERE`, `ghp_1234567890abcdefghijklmnopqrstuvwxyz`).
- `scripts/vendor-sync.py:303-324` — `contained_path` refuses empty, absolute, backslash and `..` values; the refusal is total for the manifest value.
- `scripts/vendor-sync.py:359-367` — `local_dir` is resolve-checked against the repository root and refused when it IS the root, which is the correct check for the tree that gets written and deleted.

## Ruled Out
- **Bare `FIGMA_API_KEY` in `.utcp_config.json` as a credential-resolution defect.** Ruled out. `.utcp_config.json:79` references `${FIGMA_API_KEY}` while `.env.example:15` declares `figma_FIGMA_API_KEY`, which reads as a split; the split is documented in four places — `mcp-figma/references/mcp-wiring.md:82-95` carries an explicit mapping table, `references/troubleshooting.md:396-398` names the symptom and cause, `INSTALL-GUIDE.md:330` says a bare name fails, and `.env.example:8-9` states the prefix rule. The pairing is deliberate.
- **Hardcoded credentials in tracked runtime config.** Ruled out — see Confirmed-Clean Surfaces.
- **A previously-committed secret surviving an ignore rule.** Ruled out for `.env`, `click-up-links.md` and `claude project/local/`: none appears in `git ls-files`.
- **Absolute temporary paths in `benchmark/reports/**` as a disclosure.** Ruled out — the matches are harness paths (`/var/folders/.../devin-compare-bench`) and base64 diagram payloads, not user data or credentials.
- **Shell interpolation of untrusted values on the vendor-sync write path.** Ruled out for the functions read: the write path is `shutil.copytree` / `rename` / `rmtree` over `pathlib` values, with no shell call in `copy_tree`, `carry_excluded` or `resolve_dirs`.
- **`rmtree` on `*.pull-old` / `*.pull-new` escaping the repository.** Ruled out — both names derive from `target = repo_root/local_rel`, which `resolve_dirs` has already resolved inside the root and refused when equal to it.

## Next Focus
- **Dimension:** traceability
- **Focus area:** `AI Systems/Product Owner/SYNC.md` against `claude project/`, the hub's `feature_catalog_code` and `playbook_capability` protocols, and `manual-testing-playbook/` capability claims against the listed playbooks.
- **Reason:** security now has one productive finding family (browser artifacts) and two ruled-out families; traceability has the largest untouched surface and four queued overlay protocols with two still `notApplicable`-by-non-review.
- **Rotation status:** `security` completed its first pass; `traceability` becomes active while `maintainability` stays queued.
- **Blocked/productive carry-forward:** carry the browser-artifact family (finding 1) — its downgrade trigger needs one read of the hub ALWAYS block, which is the same read that settles whether the hub has any secret rule at all.
- **Required evidence:** `sk-code-review/references/review-core.md` (not read this iteration), `git ls-files context` (deferred check), hub `SKILL.md:78-89` ALWAYS/NEVER block, `SYNC.md` parity method against `claude project/`.
- **Recovery note:** budget-bound, not evidence-bound; nothing in this pass was abandoned mid-read.

## Verdict
**CONDITIONAL** — 1 new P1, 2 new P2, no P0. The two carried P1 findings from iterations 1 and 2 remain active, so the iteration cannot reach PASS.

Review verdict: CONDITIONAL
