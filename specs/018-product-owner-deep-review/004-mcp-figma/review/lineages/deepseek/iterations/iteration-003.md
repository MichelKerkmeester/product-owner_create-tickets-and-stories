# Iteration 3 - Traceability

**Dimension:** traceability (spec alignment, cross-reference integrity, version claims)
**Iteration:** 3 of 5
**Target:** `AI Systems/Product Owner/mcp-figma/` (vendored packet), `vendor.json`, `scripts/vendor-sync.py`
**Route:** Resolved route: mode=review target_agent=deep-review, execution=single_review_iteration
**Sources read this iteration:** steer.md (lineage), `spec.md`, all six `changelog/v1.*.md`, `feature-catalog/feature-catalog.md` and its 8 subfiles' headings, `manual-testing-playbook/manual-testing-playbook.md` (index + section map) and the 17 scenario files' IDs, `references/*.md` (link targets), `SKILL.md`, `README.md`, `INSTALL-GUIDE.md`, `hub-router.json`/`leaf-manifest.json`/`mode-registry.json`/`description.json` (read-only, for references INTO the packet).

## Files Reviewed

| File | Traceability question asked |
|---|---|
| `spec.md` | Do the declared in-scope surfaces exist, and does the "byte copy, never edited" claim hold? |
| `README.md`, `SKILL.md`, `references/*.md`, `feature-catalog/feature-catalog.md` | Does every relative link resolve from the file's own depth, in the position the packet actually ships in? |
| `manual-testing-playbook/manual-testing-playbook.md` | Do its declared version, section map and scenario count match the files beside it? |
| `changelog/v1.0.0.0.md` … `v1.1.3.0.md` | Does each released version's record reach the files that claim that version? |
| `references/figma-cli-reference.md`, `INSTALL-GUIDE.md` | Do the two descriptions of `extract` agree on the output's shape? |
| `vendor.json` | Does the manifest's declared upstream path actually hold the copy that shipped? |

## Findings by Severity

### P0 Findings

None.

### P1 Findings

**R3-P1-001 - Seven cross-references resolve only at the upstream nesting depth, so in the position the packet actually ships they point at nothing.**

Every relative link in the packet was resolved from its own file's directory, twice: once inside `.skilled/skills/mcp-tooling/mcp-figma` and once inside `AI Systems/Product Owner/mcp-figma`. Upstream, all links resolve. Vendored, seven do not, because each one climbs to a sibling skill, a catalog file or a repo file that sits above the `.skilled` root and therefore above the copy:

| Broken link | Target it reaches in the vendored position |
|---|---|
| `README.md:203` | `AI Systems/README.txt` |
| `SKILL.md:115` | `AI Systems/sk-doc/sk-create-skill/assets/skill/skill-smart-router.md` |
| `feature-catalog/feature-catalog.md:71` | `AGENTS.md` five levels above `AI Systems/Product Owner` |
| `references/mcp-wiring.md:41` and `:170` | `AI Systems/mcp-code-mode/SKILL.md` |
| `references/troubleshooting.md:477` (two links on one line) | `AI Systems/mcp-code-mode/SKILL.md` and `AI Systems/mcp-chrome-devtools/SKILL.md` |

The cost is concentrated on the optional MCP path: both `mcp-wiring.md` links and one `troubleshooting.md` link point at the Code Mode mechanics the MCP path depends on, and none of them can be followed here. A reader who trusts the packet's navigation loses the one document that explains the naming and prefixed-env rules.

[SOURCE: mcp-figma/README.md:203]
[SOURCE: mcp-figma/SKILL.md:115]
[SOURCE: mcp-figma/feature-catalog/feature-catalog.md:71]
[SOURCE: mcp-figma/references/mcp-wiring.md:41]
[SOURCE: mcp-figma/references/mcp-wiring.md:170]
[SOURCE: mcp-figma/references/troubleshooting.md:477]

- **Claim:** the packet's internal navigation is depth-dependent and does not survive vendoring.
- **evidenceRefs:** the seven links above; a link-resolution sweep over all 58 files in both positions (upstream: 0 broken; vendored: 7 broken); `vendor.json`'s `local_path`/`upstream_path` pair showing the position change.
- **counterevidenceSought:** checked whether Product Owner re-creates any of those targets locally (`sk-doc/`, `mcp-code-mode/`, `mcp-chrome-devtools/`, `README.txt`): none exists. Checked whether a link-rewrite step runs on vendor (there is none in `vendor-sync.py`).
- **alternativeExplanation:** the copy may be intended to be *read* only through its own `references/` set, in which case only the two entry-point links matter. That still leaves `README.md:203` and `SKILL.md:115` broken in the two files a reader is told to start from.
- **finalSeverity:** P1, with the doubt stated: no functional command depends on these links, so the impact is lost navigation rather than a failed operation.
- **downgradeTrigger:** if the vendored copy is formally documented as "resolve links against the upstream tree", this becomes P2 documentation debt.
- **Fix site (upstream):** `.skilled/skills/mcp-tooling/mcp-figma/README.md:203`, `SKILL.md:115`, `feature-catalog/feature-catalog.md:71`, `references/mcp-wiring.md:41`/`:170`, `references/troubleshooting.md:477` - point at repo-root-relative targets that a depth change cannot break, or carry the resolution note in the copy.

### P2 Findings

**R3-P2-001 - The playbook index pins the skill at `1.0.0.0` while the packet declares `1.1.3.0`.**

The root playbook's overview ends "Skill version 1.0.0.0." Three released versions later the packet is `1.1.3.0` (`SKILL.md:6`, `README.md:11`), so the testing document names a skill generation that is three releases behind the one it tests.

[SOURCE: mcp-figma/manual-testing-playbook/manual-testing-playbook.md:9]
[SOURCE: mcp-figma/SKILL.md:6]

- **Fix site (upstream):** `.skilled/skills/mcp-tooling/mcp-figma/manual-testing-playbook/manual-testing-playbook.md:9`.

**R3-P2-002 - Two of the playbook's three pointers to its own cross-reference index name the wrong section.**

The index is Section 13 (`## 13. SCENARIO CROSS-REFERENCE INDEX`). Line 33 points at Section 13 correctly; lines 35 and 135 both say "Section 12", which is the intra-routing category. A reader following either pointer lands one section early.

[SOURCE: mcp-figma/manual-testing-playbook/manual-testing-playbook.md:35]
[SOURCE: mcp-figma/manual-testing-playbook/manual-testing-playbook.md:135]
[SOURCE: mcp-figma/manual-testing-playbook/manual-testing-playbook.md:390]

- **Fix site (upstream):** `manual-testing-playbook/manual-testing-playbook.md:35` and `:135`.

**R3-P2-003 - The install guide describes `extract`'s output as 9 sections; the reference and the catalog say 11.**

`figma-cli-reference.md:221` enumerates the eleven sections by name and tags them as source-confirmed, and `feature-catalog/feature-catalog.md:100` agrees. `INSTALL-GUIDE.md:268` sets the expectation at 9 in the one table an operator uses to decide whether the export worked, so a correct 11-section export could read as a surprise and an incomplete 9-section one as a pass.

[SOURCE: mcp-figma/INSTALL-GUIDE.md:268]
[SOURCE: mcp-figma/references/figma-cli-reference.md:221]
[SOURCE: mcp-figma/feature-catalog/feature-catalog.md:100]

- **Fix site (upstream):** `.skilled/skills/mcp-tooling/mcp-figma/INSTALL-GUIDE.md:268`.

## Traceability Checks

| Protocol | Level | Status | Evidence |
|---|---|---|---|
| `spec_code` | core | pass | `spec.md` declares three in-scope surfaces; all three exist at the declared paths. Its Focus claim ("a byte copy of an upstream skill and never edited in Product Owner") holds: 58/58 hashes match `vendor.json` and the upstream tree, and `vendor.json`'s `upstream_path` names the folder the copy actually came from. The spec's out-of-scope list was honoured: no `specs/`, `export/`, `benchmark/reports/`, `claude-plugin/`, Product Context, screenshot or figma.com URL was opened. |
| `checklist_evidence` | core | not_applicable | No `checklist.md` in the staging folder; nothing to hold evidence against. |
| `skill_agent` | overlay | pending | Iteration 4 covers how a runtime agent consumes the packet. |
| `agent_cross_runtime` | overlay | not_applicable | The packet ships no agent definition in either runtime tree. |
| `feature_catalog_code` | overlay | partial | The catalog's command forms agree with the installed binary (positional `extract [output]`, `arrange` labeled destructive, `init-agent` writes `AGENTS.md`). It disagrees with the front-door docs twice: on `extract --out` (R2-P1-001) and on the 9-vs-11 section count (R3-P2-003). Its only broken link is the `AGENTS.md` target at line 71. |
| `playbook_capability` | overlay | partial | 17 scenario files for 17 declared scenarios, and every ID the two example scripts cite (`DETECT-001`, `CONNECT-001`, `DAEMON-001`, `INSPECT-001`, `EXPORT-001`) exists in the playbook. Its own version and section pointers are stale (R3-P2-001, R3-P2-002); capability-level review is iteration 4. |

## External references into the packet

- `hub-router.json` names `mcp-figma/SKILL.md`; that file exists. `leaf-manifest.json`, `mode-registry.json` and `description.json` name the packet as a `transport` packet and route by mode, but reference no other path inside it, so no router entry points at a file the packet lacks.

## Ruled out this iteration

- **"The manifest's upstream path is wrong"** - `.skilled/skills/mcp-tooling/mcp-figma` is exactly the folder whose 58 hashes the manifest records.
- **"The changelog trail is fabricated"** - the six changelog files are dated v1.0.0.0 through v1.1.3.0, the packet declares 1.1.3.0, and the 1.1.0.0 entry's specific claim (README moved from `1.0.0.2` to `1.1.0.0`) matches the README's current content and its subsequent bump to 1.1.3.0. The trail is real; only INSTALL-GUIDE and the playbook failed to join it.
- **"Scenario IDs drift between the playbook and the examples"** - the five IDs the examples cite are all declared playbook IDs.

## Next Dimension

Iteration 4 (maintainability, and the steer's second focus): how `sk-create-figjam` uses this packet - which of its routes call `fj`, what it assumes about the packet's surface, and whether the transport/consumer contract is stated in one place or inferred - plus the packet's own follow-on change cost (duplication between the several copies of the MCP manual snippet, the 18-file playbook against a 17-scenario index, and the per-file version scheme).

Review verdict: CONDITIONAL
