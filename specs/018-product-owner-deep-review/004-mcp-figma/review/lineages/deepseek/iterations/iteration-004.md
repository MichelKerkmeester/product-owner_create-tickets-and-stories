# Iteration 4 - Maintainability (and the consumer contract with sk-create-figjam)

**Dimension:** maintainability
**Iteration:** 4 of 5
**Target:** `AI Systems/Product Owner/mcp-figma/` (vendored packet), plus its only in-repo consumer `AI Systems/Product Owner/sk-create-figjam/` (read-only)
**Route:** Resolved route: mode=review target_agent=deep-review, execution=single_review_iteration
**Sources read this iteration:** steer.md (lineage), `sk-create-figjam/SKILL.md`, `sk-create-figjam/references/flow-mode.md`, `mcp-figma/references/tool-surface.md` (FigJam rows + §6/§7), `mcp-figma/references/figma-cli-reference.md` §FigJam, `mcp-figma/references/mcp-wiring.md`, `mcp-figma/assets/utcp-figma-manual.md`, `mcp-figma/scripts/print-utcp-snippets.sh`, `mcp-figma/mcp-servers/figma-mcp/README.md`, `mcp-figma/scripts/_common.sh`, `mcp-figma/scripts/doctor.sh`, `mcp-figma/references/troubleshooting.md`; oracle: `figma-ds-cli fj --help`, `figma-ds-cli --version`.

## Files Reviewed

| File | Maintainability question asked |
|---|---|
| `sk-create-figjam/SKILL.md`, `sk-create-figjam/references/flow-mode.md` | Does the consumer state its contract with the transport packet in one place, and do its `fj` claims survive the binary? |
| `mcp-figma/references/tool-surface.md`, `references/figma-cli-reference.md` | Does the packet classify every verb its only in-repo consumer actually runs? |
| `mcp-figma/references/mcp-wiring.md`, `assets/utcp-figma-manual.md`, `scripts/print-utcp-snippets.sh`, `mcp-servers/figma-mcp/README.md`, `references/troubleshooting.md` | How many copies of the Code Mode manual snippet exist, and have they drifted? |
| `mcp-figma/scripts/_common.sh`, `scripts/doctor.sh` | Do the diagnostic constants match the names the packet itself warns are ambiguous? |

## Findings by Severity

### P0 Findings

None.

### P1 Findings

None this iteration. Every issue found here is a maintenance-cost or precision issue: none of them changes what a command does.

### P2 Findings

**R4-P2-001 - The same Code Mode manual entry is copied in five places and the copies have already diverged on the version pin.**

The manual's `args` array appears as `["-y", "figma-developer-mcp@latest", "--stdio"]` in `references/mcp-wiring.md:60`, `scripts/print-utcp-snippets.sh:22`, `references/troubleshooting.md:406` and `mcp-servers/figma-mcp/README.md:44`, and as `["-y", "figma-developer-mcp", "--stdio"]` (no pin, which npm resolves to the same moving tag) in `assets/utcp-figma-manual.md:53`. The packet already designates the asset as the "paste-ready" copy, so four hand-maintained duplicates of one JSON object now disagree with the designated source, and any future pin change has to land in five files or the drift grows.

[SOURCE: mcp-figma/assets/utcp-figma-manual.md:53]
[SOURCE: mcp-figma/references/mcp-wiring.md:60]
[SOURCE: mcp-figma/scripts/print-utcp-snippets.sh:22]
[SOURCE: mcp-figma/references/troubleshooting.md:406]
[SOURCE: mcp-figma/mcp-servers/figma-mcp/README.md:44]

- **Fix site (upstream):** `assets/utcp-figma-manual.md` stays the single source; `mcp-wiring.md:51-66` and `print-utcp-snippets.sh:14-27` should link or print from it rather than restate the object.

**R4-P2-002 - The diagnostic constants re-introduce the very name collision the packet spends a section warning about.**

The packet's central warning is that `figma-cli` names two different tools, so the token directory is the unambiguous `~/.figma-ds-cli/.daemon-token`. The PID file it documents and reads is `~/.figma-cli-daemon.pid` - the ambiguous name, in `$HOME`, right beside the unrelated tool's namespace. `doctor.sh:34` then reports that file's contents as "the daemon PID" with no check that the process it names is this daemon, so a stale or foreign PID file reads as a healthy local daemon in the report-only diagnostic that operators are told to trust.

[SOURCE: mcp-figma/scripts/_common.sh:49]
[SOURCE: mcp-figma/scripts/doctor.sh:34]
[SOURCE: mcp-figma/references/troubleshooting.md:310]

- **Doubt stated:** the filename is the upstream tool's own convention, so the packet cannot rename it. The fix is a note plus a validation, not a rename.
- **Fix site (upstream):** `scripts/_common.sh:49` (comment why the two namespaces differ) and `scripts/doctor.sh:34` (verify the PID's process name before reporting it as the daemon).

**R4-P2-003 - "The official Figma Dev Mode MCP is not a supported path in this release" reads repo-wide, while the sibling packet ships that route as its primary one.**

`mcp-wiring.md` §6 confines the sentence by its section heading, but the sentence itself carries no "through Code Mode" qualifier; the qualifier only arrives in the following bullet. `sk-create-figjam/SKILL.md:216` and `references/flow-mode.md:334` describe the same hosted MCP (`generate_diagram`, `use_figma`, `get_figjam`) as the primary route through Figma's own plugin or the client's connector, explicitly outside Code Mode. An agent that reads the transport packet first can therefore refuse a route its own consumer treats as first-class.

[SOURCE: mcp-figma/references/mcp-wiring.md:154]
[SOURCE: sk-create-figjam/SKILL.md:216]
[SOURCE: sk-create-figjam/references/flow-mode.md:334]

- **Fix site (upstream):** `references/mcp-wiring.md:154` - scope the sentence to "not a supported path *through Code Mode* in this release".

## The consumer contract, reviewed (no finding)

This is the steer's stated second focus, so the result is recorded even though it produced no defect:

- **The handoff is stated once and points at the right owner.** `sk-create-figjam/SKILL.md:26` excludes a bare `figma-ds-cli` operation from its own scope and names the packet; `:65` loads `../mcp-figma/SKILL.md` for the `fj` route; `:199` names it as "`figma-ds-cli` mechanics for the `fj` route and its mutating gate"; `references/flow-mode.md:26` repeats the handoff as the route's "Hands Off To". The consumer never restates the gating taxonomy, so the transport packet remains the single authority for it.
- **Every `fj` verb the consumer relies on exists, and the packet already classifies it.** `figma-ds-cli fj --help` under 1.2.0 lists exactly `list`, `info`, `nodes`, `sticky`, `shape`, `text`, `connect`, `delete`, `move`, `update`, `eval`. The consumer uses `fj info` (read-back before the first write), `fj shape`, `fj connect`, `fj text`, `fj nodes -l`, and keeps `fj delete` / `fj eval` off its path (flow-mode.md:357-361). `tool-surface.md:149-152` classifies all of them: `list|info|nodes` READ-ONLY, `sticky|shape|text|connect|move|update` MUTATING, `fj delete` DESTRUCTIVE, `fj eval` ARBITRARY, with the destructive rollback row at `:222` and the arbitrary-mutation rule at `:233`. Nothing the consumer does is unclassified.
- **The version precondition the consumer states is the one the packet states.** flow-mode.md:354 requires 1.2.0 from the silships repo "because the npm build has no `fj` group"; the installed 1.2.0 has the group, and the packet's own version trap (`SKILL.md:18`) says the same thing in the same terms.

## Traceability Checks

| Protocol | Level | Status | Evidence |
|---|---|---|---|
| `spec_code` | core | pass | Carried forward from iteration 3; the consumer's `fj` assumptions are satisfied by the packet's documented surface and by the installed binary. |
| `checklist_evidence` | core | not_applicable | No `checklist.md` in the staging folder. |
| `skill_agent` | overlay | pass | The consumer-side contract is explicit (exclusion at SKILL.md:26, on-demand load at :65, reference at :199, "Hands Off To" at flow-mode.md:26), delegates the gate rather than duplicating it, and every route it names exists. |
| `agent_cross_runtime` | overlay | not_applicable | The packet ships no runtime agent definition; the consumer does not require one. |
| `feature_catalog_code` | overlay | partial | Unchanged from iteration 3. |
| `playbook_capability` | overlay | partial | Scenario structure and IDs align (17 files / 17 declared, five cited IDs resolve) and the spot-checked command forms (`export screenshot -o`, `daemon status|diagnose`, `connect --safe`) match the installed 1.2.0. Twelve of the seventeen scenarios were not audited line by line, so this stays partial rather than pass. |

## Ruled out this iteration

- **"The consumer depends on `fj` behaviour the transport packet never documents"** - every verb used is classified at `tool-surface.md:149-152`, including the destructive rollback.
- **"The consumer's `fj` route is stale relative to 1.2.0"** - all eleven `fj` subcommands the binary exposes are the ones the packet records; the consumer uses a subset and uses it the way the binary defines it (for example `fj connect <startId> <endId>` takes no label, which both documents say).
- **"`sk-create-figjam` duplicates the gating taxonomy"** - it does not; it names the packet as the owner in four places.

## Next Dimension

Iteration 5 (close-out pass): re-replay each confirmed P1 against its cited line, check whether any finding has been silently resolved or superseded by another iteration's evidence, audit the two surfaces no iteration has yet opened end to end (`feature-catalog/` subfiles beyond the index, `changelog/` claims against file content, `mcp-servers/`), and confirm the vendor manifest and sync tool hold under the same scrutiny as the packet they carry.

Review verdict: PASS
