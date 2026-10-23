# Iteration 004 — Deep Review

## Dispatcher

- Mode: review; target_agent: deep-review; execution: inline lineage executor (no nested dispatch)
- Iteration: 4 of 5; Dimension: references and paths
- Lineage: sessionId=fanout-deepseek-1792580454700-vajsq8, generation=1, lineageMode=new
- Sources read this iteration: `specs/product-owner/018-product-owner-deep-review/003-mcp-click-up/spec.md`, `specs/product-owner/018-product-owner-deep-review/003-mcp-click-up/review/lineages/deepseek/steer.md`, `deep-review-strategy.md`, every Markdown file under `AI Systems/Product Owner/mcp-click-up/` (link and path sweep), every Markdown file under `AI Systems/Product Owner/sk-product-owner/` plus `AGENTS.md`, `SKILL.md`, `ROUTER.md` (hub link sweep), `AI Systems/Product Owner/mcp-click-up/INSTALL-GUIDE.md`, `references/cupt-commands.md`, `references/troubleshooting.md`, `feature-catalog/FEATURE-CATALOG.md`, `feature-catalog/cupt-global-flags/json-flag.md`, `changelog/v1.2.0.0.md`, `scripts/README.md`, `examples/task-queue-workflow.sh`

## Dimension

References and paths — whether every pointer a reader or an agent follows lands on something that exists in the repository as shipped, and whether the version headers agree with the content they describe.

## Files Reviewed

- All 171 Markdown files under `AI Systems/Product Owner/mcp-click-up/` (link audit)
- `AI Systems/Product Owner/mcp-click-up/INSTALL-GUIDE.md:1-160`
- `AI Systems/Product Owner/mcp-click-up/references/cupt-commands.md:252-262`
- `AI Systems/Product Owner/mcp-click-up/references/troubleshooting.md:245-260`
- `AI Systems/Product Owner/mcp-click-up/feature-catalog/FEATURE-CATALOG.md:15-19, 320-330`
- `AI Systems/Product Owner/mcp-click-up/feature-catalog/cupt-global-flags/json-flag.md:15-25`
- `AI Systems/Product Owner/mcp-click-up/changelog/v1.2.0.0.md:20-30`
- `AI Systems/Product Owner/mcp-click-up/scripts/README.md:10-35`
- `AI Systems/Product Owner/mcp-click-up/examples/task-queue-workflow.sh:35-45`
- `AI Systems/Product Owner/sk-product-owner/**` and the three hub documents (link audit)

## Findings by Severity

### P0 Findings

None.

### P1 Findings

1. **Two packet documents say `cupt add` creates a task; four others say cupt has no create command** -- AI Systems/Product Owner/mcp-click-up/feature-catalog/cupt-global-flags/json-flag.md:19 -- the JSON-flag card states "`--json` ... exists on five commands: `cupt add --json` (prints the created task), `cupt list --json`, ...", and `feature-catalog/FEATURE-CATALOG.md:17,326` repeats it. Against that, `references/mcp-tools.md:59` and `:304`, `SKILL.md:353` and `feature-catalog/mcp-high-priority/create-task.md:49` all state that cupt has no create command and that task creation is MCP-only. The authoritative command reference documents no `add` command at all: its list, details, completion, notes, time, tag, attachment and workspace sections contain only `time add`, `tag add` and `attach add` (`references/cupt-commands.md:74-262`).
Finding class: contradictory-reference
Scope proof: all six statements are inside the vendored packet; the command reference that would settle them is in the same folder and was read end to end.
Affected surface hints: `feature-catalog/cupt-global-flags/json-flag.md` (fix site, upstream), `feature-catalog/FEATURE-CATALOG.md:17,326`, `SKILL.md:353`, `references/mcp-tools.md:59`
Case: an agent routing a "create a task" request reads the JSON-flag card first, concludes cupt can create tasks, and runs `cupt add --json`; on a cupt-only runtime that either fails as an unknown command or creates a task the packet says cannot exist, while the MCP-only routing rule in the same packet says the opposite.
Fix site: `mcp-click-up/feature-catalog/cupt-global-flags/json-flag.md:19` upstream — drop `add` from the `--json` command list (and the two catalog summary lines) unless the command is documented in `references/cupt-commands.md`.
Claim adjudication:
```json
{
  "claim": "The packet contradicts itself on whether cupt can create a task, so the JSON-flag card and catalog describe a command the command reference does not document.",
  "evidenceRefs": [
    "AI Systems/Product Owner/mcp-click-up/feature-catalog/cupt-global-flags/json-flag.md:19",
    "AI Systems/Product Owner/mcp-click-up/feature-catalog/FEATURE-CATALOG.md:326",
    "AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:59",
    "AI Systems/Product Owner/mcp-click-up/SKILL.md:353",
    "AI Systems/Product Owner/mcp-click-up/references/cupt-commands.md:74",
    "AI Systems/Product Owner/mcp-click-up/references/cupt-commands.md:252"
  ],
  "counterevidenceSought": "Searched the whole packet for an `add` command section or card: found only time add, tag add and attach add, plus three MCP-only create cards. Checked §13 Global Flags, which lists --json for read commands and never mentions add.",
  "alternativeExplanation": "Older cupt releases may have had an `add` command that the reference dropped while the flag card kept it. That is drift, not correctness of the current packet, and the contradiction stands either way.",
  "finalSeverity": "P1",
  "confidence": "high",
  "downgradeTrigger": "If `cupt add` is confirmed to exist in the installed CLI, the finding moves to the four documents that deny it (P1 there instead) rather than disappearing."
}
```

### P2 Findings

1. **`INSTALL-GUIDE.md` states two different versions of itself and dates its own content before the server state it describes** -- AI Systems/Product Owner/mcp-click-up/INSTALL-GUIDE.md:14 -- the frontmatter reads `version: 1.0.0.0` (`:4`) while the body reads "**Version:** 1.0.1.0 | **Updated:** 2026-07-16". The guide's content is the hosted-server OAuth route with the 61-tool inventory, which `changelog/v1.2.0.0.md:25` dates to the 2026-10-08 capture, and `changelog/v1.2.0.0.md:27` records that setup routing changed in that release. So the guide was edited after the date it advertises and no longer matches its own frontmatter.
Finding class: version-header-drift
Scope proof: both version statements are in the same file, and the changelog entry that dates the content is two folders away in the same packet.
Affected surface hints: `INSTALL-GUIDE.md` (fix site, upstream), `changelog/v1.2.0.0.md`
Case: an operator checks whether the guide is current by reading "Updated: 2026-07-16", concludes it predates the hosted-server migration, and follows the older API-key route it no longer recommends — or a validator comparing frontmatter to body finds two versions for one document.
Fix site: `mcp-click-up/INSTALL-GUIDE.md` — one version statement, one date, both refreshed with the hosted-server change.

2. **Every run command the packet documents uses the upstream `.skilled/...` path, which exists in Product Owner only through an untracked symlink** -- AI Systems/Product Owner/mcp-click-up/INSTALL-GUIDE.md:24 -- the guide's AI-first block, `references/troubleshooting.md:253`, `scripts/README.md:31-32` and even the example script's error hint (`examples/task-queue-workflow.sh:41`) all say `bash .skilled/skills/mcp-tooling/mcp-click-up/scripts/install.sh`. In Product Owner that path resolves only because `AI Systems/Product Owner/.skilled` is a symlink (`git status --porcelain` reports it untracked), so a clone of Product Owner has no such path; the packet's own `scripts/` folder is the only copy that ships with the repository.
Finding class: layout-dependent-path
Scope proof: the symlink's tracking state and the four call sites were checked in this repository; the packet copy carries the same scripts.
Affected surface hints: `INSTALL-GUIDE.md` (fix site, upstream), `references/troubleshooting.md`, `scripts/README.md`, `examples/task-queue-workflow.sh`
Case: a Product Owner clone without the shared skill folder present — a fresh checkout, a contributor on another machine, or CI — follows the guide's install line and gets "No such file or directory" for the packet's own installer, which is sitting at `mcp-click-up/scripts/install.sh`.
Fix site: `mcp-click-up/INSTALL-GUIDE.md` upstream — use a copy-relative path (`bash mcp-click-up/scripts/install.sh`, and the `$(dirname "$0")` form inside the scripts), keeping the `.skilled/...` form only where the packet is documented as living in the shared tree.

## Traceability Checks

- `Core: spec_code` — the spec names a byte-copied packet; a packet may not be corrected here, so each finding above names the upstream file as the fix site, per the steer's rule 3. Status: pass.
- `Core: checklist_evidence` — no checklist exists in the staging wrapper; the steer's citation rule 5 ("a repository-relative path that resolves") was applied to every finding and every `[SOURCE:]`-style path in this narrative. Status: pass.
- `Overlay: feature_catalog_code` — the catalog's counts still reconcile to the tree (50 cupt cards, 61 MCP tool cards), and the only catalog contradiction is the `--json`/`add` claim recorded above. Status: partial.
- `Overlay: playbook_capability` — the manual-testing-playbook's own cross-links resolve, and its recovery scenario for missing auth exercises the documented `cupt config --api-token` path consistently. Status: pass.

## Integration Evidence

- `changelog/v1.2.0.0.md:27` confirms from inside the packet that `INSTALL-GUIDE.md` "sits at the packet root", which is the same fact that makes iteration 3's leaf finding (R3-P2-002) real: the hub's `<packet>/references|assets/...` leaf contract cannot express it, and the packet's own history says the router had to be changed to find it.
- Link sweep, executed read-only: all relative Markdown links in the 171 packet files resolve (0 broken), including the cross-folder links from `manual-testing-playbook/*/*.md` back to `references/troubleshooting.md` and the `feature-catalog` links into `REFERENCES` sections.
- Hub link sweep: `AGENTS.md`, `SKILL.md`, `ROUTER.md` and `sk-product-owner/**` resolve every non-placeholder link; the only unresolved targets are template placeholders (`{figma-url}`, `{url}`, `{relative-path}`) and illustrative links inside the rendered example artifacts under `sk-product-owner/assets/examples/`, which are sample documents rather than navigation.

## Edge Cases

- The `.skilled/...` form is correct in the shared skill repository, so the finding is not that the path is wrong there; it is that the packet is now also shipped somewhere the path does not resolve, and the packet's scripts are present in that second place.
- `cupt add` cannot be settled from the repository alone. The adjudication treats the packet's own command reference and its three "no create command" statements as the authority, and the downgrade trigger records what would move the finding if the CLI disagrees.

## Confirmed-Clean Surfaces

- Relative-link integrity inside the packet: 0 broken out of every link in 171 Markdown files.
- Reference versions are internally consistent where they are stated once: `cupt-commands.md` 1.0.0.3, `mcp-tools.md` 1.1.0.0, `troubleshooting.md` 1.0.0.3, `README.md` 1.1.0.0, `FEATURE-CATALOG.md` 1.1.0.0, `manual-testing-playbook.md` 1.1.1.0, `SKILL.md` 1.2.2.0 matching `changelog/v1.2.2.0.md`'s `version: 1.2.2.0`.
- The playbook's scenario files sit one folder deeper than the catalog cards and their `../../references/...` links are correct for that depth.
- `.env.example` and `.gitignore` agree: the four push-target keys are listed empty and `.env` is ignored while `.env.example` is exempted.

## Ruled Out

- "The packet's relative links are broken after vendoring": 0 broken links in 171 files.
- "The hub's links into the packet are broken": every non-placeholder link resolves.
- "Placeholder targets in the example artifacts are defects": they are `{figma-url}`-style samples by design.
- "A reference file carries a stale version of the packet release": each sub-document carries its own version and only `INSTALL-GUIDE.md` states two for itself.

## Next Dimension

- Dimension: maintainability
- Focus area: structure and duplication across the 111 feature cards and the four reference documents, the dead `assets` base in the packet router, changelog hygiene, and the cost of keeping a byte-copy consistent with a hub that describes it in six places
- Reason: the remaining risk after four dimensions is not a broken pointer but the maintenance surface that produced the pointers; the maintainability pass should name the drift sources, not re-list the findings
- Rotation status: all four dimensions touched; maintainability closes the loop

## Source Tags

- R4-P1-001 — [SOURCE: mcp-click-up/feature-catalog/cupt-global-flags/json-flag.md:19]
- R4-P2-001 — [SOURCE: mcp-click-up/INSTALL-GUIDE.md:14]
- R4-P2-002 — [SOURCE: mcp-click-up/INSTALL-GUIDE.md:24]

## Verdict

One P1 and two P2 findings this iteration, no P0. The packet's own navigation is clean — no broken relative link in 171 files — but it ships two mutually exclusive statements about whether cupt can create a task, a self-contradicting version header, and run commands that only work where the shared skill folder happens to be linked in.

Review verdict: CONDITIONAL
