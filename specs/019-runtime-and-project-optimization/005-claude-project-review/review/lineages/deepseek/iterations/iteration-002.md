# Review Iteration 002 — End-user setup UX for the ClickUp and Figma connectors

**Review target:** `specs/z-staging-po-019r` (Product Owner claude.ai Project packaging)
**Iteration:** 2 of 3
**Focus:** whether a Claude Desktop or claude.ai user is told, step by step, how to add the claude.ai ClickUp and Figma connectors, open the Product Owner Project, enable the connectors in a chat, check that they work and troubleshoot — compared with `AI Systems/Media Editor/USER-GUIDE.md`, which does this for its own extension.
**Lineage:** `specs/z-staging-po-019r/review/lineages/deepseek` (session `fanout-deepseek-1792598333413-h7kxu3`, generation 1)

## Dimension

Traceability and maintainability of the operator-facing path. The requirement is stated in `[SOURCE: specs/z-staging-po-019r/spec.md:7]`; the benchmark is the Media Editor guide's five-part shape: pick by surface, install, open the Project and switch the connector on, check that it works, troubleshoot.

## Files Reviewed

| File | What was checked |
| --- | --- |
| `AI Systems/Media Editor/USER-GUIDE.md:1-106` | benchmark structure: surface table, install, enable, check, troubleshooting |
| `AI Systems/Product Owner/README.md:149-199` | Quick Start, the "Connect ClickUp and Figma (optional)" section, the claude.ai Project steps |
| `AI Systems/Product Owner/README.md:860-897` | troubleshooting section |
| `AI Systems/Product Owner/claude project/README.md:1-194` | the Project upload guide, the ClickUp Connector Delivery section, Set Up the Live Project, Smoke Matrix |
| `AI Systems/Product Owner/claude project/Custom Instructions.md:243-259` | ClickUp Connector Delivery and Flow Mode Delivery as the runtime's assumptions |
| `AI Systems/Product Owner/mcp-click-up/SKILL.md:16-30`, `mcp-click-up/INSTALL-GUIDE.md:1-210` | whether the ClickUp setup text covers the Project connector or the CLI |
| `AI Systems/Product Owner/mcp-figma/SKILL.md:1-60` | whether the Figma setup text covers the Project connector or the CLI |

## Findings by Severity

P0: 0 · P1: 2 · P2: 2

### P0 Findings

None. Missing setup text cannot corrupt a delivered artifact; it leaves a documented capability unreachable until the user finds the connector UI alone.

### P1 Findings

#### 1. R2-P1-001 — The only "Connect ClickUp and Figma" instructions are the CLI Code Mode install, so a Project user is never told how to add or enable either connector

**Severity:** P1 (incomplete implementation / traceability)
**Evidence:** `[SOURCE: AI Systems/Product Owner/README.md:173]` opens "### Connect ClickUp and Figma (optional)" and `[SOURCE: AI Systems/Product Owner/README.md:178]` to `[SOURCE: AI Systems/Product Owner/README.md:180]` install the repository's Code Mode stack: `.utcp_config.json`, `.mcp.json`, Node 24, `cd mcp-code-mode/mcp-server && nvm exec 24 npm ci && nvm exec 24 npm run build`. `[SOURCE: AI Systems/Product Owner/README.md:193]` to `[SOURCE: AI Systems/Product Owner/README.md:197]` is the only Project path and has three steps: paste the kernel, upload 62 files, run the smoke matrix. `[SOURCE: AI Systems/Product Owner/claude project/README.md:127]` to `[SOURCE: AI Systems/Product Owner/claude project/README.md:134]` is the Project's own upload guide and has six steps, none of them a connector. `[SOURCE: AI Systems/Product Owner/claude project/README.md:114]` is a ClickUp parameter section that presumes the connector already exists. The benchmark does the opposite: `[SOURCE: AI Systems/Media Editor/USER-GUIDE.md:20]` to `[SOURCE: AI Systems/Media Editor/USER-GUIDE.md:27]` is a "where you chat → what to install" table, `[SOURCE: AI Systems/Media Editor/USER-GUIDE.md:72]` to `[SOURCE: AI Systems/Media Editor/USER-GUIDE.md:74]` opens the Project and then says "Under **+ > Connectors**, switch Media Editor on", and `[SOURCE: AI Systems/Media Editor/USER-GUIDE.md:61]` to `[SOURCE: AI Systems/Media Editor/USER-GUIDE.md:66]` is the install with the exact menu path.

**Why it matters:** A Project user who wants ClickUp delivery follows the only heading that names ClickUp and Figma together and lands on a Node 24 build of a local MCP server the Project cannot use. Neither the product README nor the Project README ever says how a connector is added to a Claude account, how it is switched on inside a chat, or that the seller connector and the Figma connector are separate. The capability the kernel's whole ClickUp section depends on is therefore undocumented for the surface it is written for.

**Claim adjudication**

- `type`: missing_surface_instructions
- `claim`: the packaging documents the CLI Code Mode transport for ClickUp and Figma but gives a Claude Desktop or claude.ai user no add-or-enable step for either connector.
- `evidenceRefs`: `README.md:173`, `README.md:178-180`, `README.md:193-197`, `claude project/README.md:114`, `claude project/README.md:128-134`, `Media Editor/USER-GUIDE.md:20-27`, `Media Editor/USER-GUIDE.md:61-66`, `Media Editor/USER-GUIDE.md:72-74`
- `counterevidenceSought`: searched both READMEs, the kernel and `SYNC.md` for "Desktop", "Connectors", "Settings > Connectors" and "add connector". The word "Desktop" appears zero times in `AI Systems/Product Owner/README.md` and zero times in `claude project/README.md`. `mcp-click-up/INSTALL-GUIDE.md` documents a CLI install (sections 2-5) and never the Project connector.
- `alternativeExplanation`: the connectors may be considered an account-level setting the operator configures once and the package need not document, with the kernel's phrase "when the connector is present" treated as the whole contract.
- `finalSeverity`: P1. Not P0, because every artifact path works without a connector and the kernel degrades to "no connector, nothing to offer". Not P2, because the spec's third focus asks for exactly this path and the review-benchmark in the same repository shows the expected shape, so the omission is a missing implementation rather than a wording preference.
- `confidence`: high
- `downgradeTrigger`: a Project-surface setup section elsewhere that a Project user can reach, or a playbook scenario that completes a connector setup from the documentation alone.
- `fix changes`: `AI Systems/Product Owner/README.md` (replace or retitle the CLI-only section and add a Project-surface path) and `AI Systems/Product Owner/claude project/README.md` (extend Set Up the Live Project).

#### 2. R2-P1-002 — The Figma connector has no setup, enablement or no-connector statement for a Project user, although Flow Mode Delivery is built on it

**Severity:** P1 (incomplete implementation)
**Evidence:** `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:255]` says the board write "depends on the Figma connector", `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:257]` tells the runtime to check the model and wait for a yes "With a Figma connector that writes diagrams", and `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:257]` names "the connector's read tool". `[SOURCE: AI Systems/Product Owner/claude project/README.md:114]` to `[SOURCE: AI Systems/Product Owner/claude project/README.md:127]` is the only connector section in the Project upload guide and it is ClickUp-only. `[SOURCE: AI Systems/Product Owner/mcp-figma/SKILL.md:38]` is the repository's Figma setup text and it is a CLI path ("Verify the binary, choose a connect mode (safe plugin vs yolo patch), bring up the daemon"), which is a different surface from a claude.ai connector. No file in `AI Systems/Product Owner/` names a Figma connector add-or-enable step.

**Why it matters:** Flow Mode is the newest route in the kernel and its happy path is unreachable without a connector nobody is told how to add. A user who follows the docs can install `figma-ds-cli` and a daemon, then find that the Project's Flow Mode still reports no Figma connector, because the CLI and the connector are unrelated transports. The kernel handles the no-connector case correctly (`[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:258]`), which makes the missing setup the only gap between a user with the connector and a user without it.

**Claim adjudication**

- `type`: missing_surface_instructions
- `claim`: the package's only Figma setup text is the CLI daemon path, and no Project-facing document says how to add or enable a Figma connector for Flow Mode.
- `evidenceRefs`: `Custom Instructions.md:255-258`, `claude project/README.md:114-127`, `mcp-figma/SKILL.md:38`, `Media Editor/USER-GUIDE.md:74`
- `counterevidenceSought`: read `claude project/README.md` in full and searched the whole Product Owner tree for "figma connector" (case-insensitive). The kernel's own three Flow bullets are the only Project-facing mentions, and each assumes the connector exists. The Media Editor benchmark's `+ > Connectors` line is the only in-repo description of the enable step.
- `alternativeExplanation`: the Figma connector may be new enough that the operator intends Field users to rely on its presence without written setup, and the kernel's no-connector branch may be the intended documented path.
- `finalSeverity`: P1 for the same reason as R2-P1-001: a shipped route depends on a setup step the package never states. Not P0, because Flow Mode refuses safely and never fabricates a board.
- `confidence`: high
- `downgradeTrigger`: a documented Figma connector setup step for the Project surface, or a decision record that Flow Mode is CLI-only.
- `fix changes`: `AI Systems/Product Owner/claude project/README.md` (a Figma connector section beside the ClickUp one) and `AI Systems/Product Owner/README.md` (say which surface the connector belongs to).

### P2 Findings

#### 3. R2-P2-001 — Neither connector has a "check that it works" step with an expected result

**Severity:** P2 (missing validation)
**Evidence:** The Project guide's verification is `[SOURCE: AI Systems/Product Owner/claude project/README.md:133]` ("Run the smoke matrix below") and the matrix at `[SOURCE: AI Systems/Product Owner/claude project/README.md:138]` to `[SOURCE: AI Systems/Product Owner/claude project/README.md:173]`, whose only connector-adjacent bullets are `[SOURCE: AI Systems/Product Owner/claude project/README.md:166]` ("With the ClickUp connector present, every export response offers ClickUp delivery") and `[SOURCE: AI Systems/Product Owner/claude project/README.md:173]` (the read-back parameter). Neither is a probe a user runs to prove the connector is live, and no bullet covers Figma at all. The benchmark gives three: `[SOURCE: AI Systems/Media Editor/USER-GUIDE.md:80]` a health call with the expected finding, `[SOURCE: AI Systems/Media Editor/USER-GUIDE.md:81]` a real task, `[SOURCE: AI Systems/Media Editor/USER-GUIDE.md:82]` the approval step and the "a command instead of a saved file means the tools did not run" interpretation.

**Why it matters:** The smoke matrix proves routing, not reachability. A user whose connector is off sees the same kernel fallback as a user who has no connector, and nothing in the docs distinguishes "connector not enabled" from "no connector available", which is the first question the troubleshooting section would need to answer.

**Fix changes:** `AI Systems/Product Owner/claude project/README.md` (one ClickUp probe and one Figma probe with expected output, in the smoke matrix or a Check That It Works section).

#### 4. R2-P2-002 — There is no troubleshooting entry for a missing or disabled connector, and the one ClickUp symptom is written for the CLI

**Severity:** P2 (documentation gap)
**Evidence:** `[SOURCE: AI Systems/Product Owner/README.md:860]` to `[SOURCE: AI Systems/Product Owner/README.md:897]` is the only troubleshooting section, and its ClickUp entry `[SOURCE: AI Systems/Product Owner/README.md:882]` to `[SOURCE: AI Systems/Product Owner/README.md:884]` reads "The push used the plain `description` field. Push again with `markdown_description`" — a CLI push symptom with no Project counterpart. The same section's `[SOURCE: AI Systems/Product Owner/README.md:874]` to `[SOURCE: AI Systems/Product Owner/README.md:876]` entry ("No `Path:` or `Verified:` line") is also CLI-only, since a Project reports `Export-equivalent path:` instead. `[SOURCE: AI Systems/Product Owner/claude project/README.md:194]` is the Project guide's last line and closes on a deployment caveat, with no troubleshooting section. The benchmark's table `[SOURCE: AI Systems/Media Editor/USER-GUIDE.md:86]` to `[SOURCE: AI Systems/Media Editor/USER-GUIDE.md:97]` carries seven symptom rows, two of which are exactly the "tools are off" and "missing from + > Connectors" cases a Project user hits.

**Why it matters:** A Project user follows the troubleshooting section and is told to look for a `Path:`/`Verified:` pair their surface never produces, or to "push again" through a transport they have not set up. Missing rows are cheap to add and are the difference between a support loop and a self-serve fix.

**Fix changes:** `AI Systems/Product Owner/README.md` (add connector rows: connector off, connector absent from the chat's + menu, board read-back not possible) and `AI Systems/Product Owner/claude project/README.md` (a short Troubleshooting section).

## Traceability Checks

| Protocol | Status | Evidence |
| --- | --- | --- |
| `spec_code` (core) | partial | Focus question 3 of the spec is answered: the setup UX does not exist on the Project surface, while the benchmark shows the expected five-part shape. |
| `checklist_evidence` (core) | notApplicable | No `checklist.md` in the staging folder. |
| `skill_agent` (overlay) | pass | The kernel's connector assumptions match the skill's parameter table (`sk-product-owner/SKILL.md:291`), which is iteration 3's subject; here only the setup path is judged. |
| `agent_cross_runtime` (overlay) | notApplicable | No agent definition in scope. |
| `feature_catalog_code` (overlay) | notApplicable | No feature catalog in scope. |
| `playbook_capability` (overlay) | deferred | The playbook grades the CLI packaging; it cannot exercise a live connector. |

## Ruled out

- **"The benchmark's advise-only row applies to the Product Owner Project."** `[SOURCE: AI Systems/Media Editor/USER-GUIDE.md:27]` says a claude.ai browser or mobile user gets advice only, because the Media Editor runtime runs on the user's computer. The Product Owner's two connectors are account-level and the repository records no such local requirement, so the Media Editor row is not evidence that claude.ai web lacks the Product Owner connectors. No finding either way; see Open Questions.
- **"The kernel's connector text is wrong."** `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:243]` to `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:249]` describes parameters and the approval gate, not setup, and iteration 3 tests whether those parameters are evidenced. No setup finding lands on the kernel.
- **"The smoke matrix is the setup test."** It was read in full (`claude project/README.md:138-173`): every bullet tests routing, format or delivery wording. No bullet tests that a connector answers. No finding about coverage of the matrix itself beyond R2-P2-001.

## Open Questions

- **Which surfaces expose the claude.ai ClickUp and Figma connectors, and where in each surface they are added.** The repository's only enablement evidence is the Desktop chat's `+ > Connectors` (`Media Editor/USER-GUIDE.md:74`), which belongs to a locally installed extension. Whether claude.ai in a browser reaches the same connectors, and whether adding them happens in account Settings or in the chat, cannot be settled from this repository. The fix for R2-P1-001 and R2-P1-002 needs an operator-supplied statement before it is written as fact.
- **Whether the claude.ai ClickUp connector exposes the same tool names and parameters as the Code Mode manual.** `[SOURCE: AI Systems/Product Owner/mcp-click-up/SKILL.md:26]` says the connector "was not re-checked on 2026-10-08", which leaves iteration 3's evidence question open at the connector and closed at the manual.

## Next Dimension

Iteration 3: the connector tool names and parameters the kernel and knowledge assume, the documentation that backs each, and anything iterations 1 and 2 left open.

Review verdict: CONDITIONAL
