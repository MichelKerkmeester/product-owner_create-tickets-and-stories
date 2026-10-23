# Review Iteration 003 — Connector tool names and parameters, and what backs each

**Review target:** `specs/z-staging-po-019r` (Product Owner claude.ai Project packaging)
**Iteration:** 3 of 3
**Focus:** whether the connector tool names and parameters the kernel and knowledge assume are backed by repository documentation, and what iterations 1 and 2 left open.
**Lineage:** `specs/z-staging-po-019r/review/lineages/deepseek` (session `fanout-deepseek-1792598333413-h7kxu3`, generation 1)

## Dimension

Traceability (source-to-claim evidence) and correctness of the transport recipes. The claim set is fixed by `[SOURCE: specs/z-staging-po-019r/spec.md:7]`: `clickup_create_task` with `markdown_description`, `clickup_update_task`, `clickup_get_task` with include description, `clickup_create_document`, `clickup_create_document_page`, `visibility: PRIVATE`, and the Figma connector's `generate_diagram` and its read tool.

## Files Reviewed

| File | What was checked |
| --- | --- |
| `AI Systems/Product Owner/claude project/Custom Instructions.md:239-249, 299` | the ClickUp transport contract and the private-doc offer |
| `AI Systems/Product Owner/claude project/README.md:114-125` | the Project guide's transport summary |
| `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:128, 311-320, 345` | Figma tool names and the tag step |
| `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Hybrid Workflow.md:160` | the tag step |
| `AI Systems/Product Owner/mcp-click-up/SKILL.md:16-30` | the markdown contract and its verification date |
| `AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-medium-priority/create-document.md:14-40` | required document parameters |
| `AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-high-priority/get-task.md:18-37` | the `include` parameter |
| `AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-low-priority/create-doc-page.md:29-39` | `content_format` |
| `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:125, 251-267` | tool and parameter tables |
| `AI Systems/Product Owner/mcp-figma/SKILL.md:1-60` | what surface the Figma packet documents |
| `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:334-338` | the hosted Figma MCP and its unconfirmed prefix |
| `AI Systems/Product Owner/sk-product-owner/SKILL.md:305-310` | the source-side private-doc recipe |

## Findings by Severity

P0: 0 · P1: 2 · P2: 2

### P0 Findings

None. Both P1 findings are missing or unverified fields on a path the runtime can decline; neither fabricates a write.

### P1 Findings

#### 1. R3-P1-001 — The private-doc recipe the Project offers omits two parameters the tool requires, and the source-side rule that resolves them is not mirrored

**Severity:** P1 (incomplete implementation)
**Evidence:** `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:299]` offers "`Where in ClickUp should this go? Send a list link, or I'll upload it as a private doc, which I recommend for now.`" and then defines it: "A private doc is `clickup_create_document` with `visibility: "PRIVATE"` and one page carrying the artifact as `text/md`." `[SOURCE: AI Systems/Product Owner/claude project/README.md:125]` adds `create_page: false` but no other field. The vendored packet states the full requirement: `[SOURCE: AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-medium-priority/create-document.md:38]` says "All four of `name`, `parent`, `visibility` and `create_page` are required. `parent` is `{id, type}`". The source side carries the missing resolution rule: `[SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:307]` names `name`, `parent`, `visibility: "PRIVATE"` and `create_page: false`, then "It goes under `CLICKUP_DOC_PARENT_URL` when that is set, otherwise under the kind's link, otherwise under the space or folder the user names", and `[SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:308]` adds "The container id and its `parent.type` are read from the link. When the link does not show which container it is, `clickup_get_workspace_hierarchy` settles it before the push."

**Why it matters:** The offer's recommended branch ("I'll upload it as a private doc") is the one a user with no link takes, and it is exactly the branch with no container. As written, the Project has no `parent`, no `parent.type` and no `name` for the call the kernel tells it to make, so the recipe cannot be executed without an unstated question. The skill mirrors the required fields and the container-resolution rule; the Project mirror dropped both, which is the parity failure the manual method is supposed to prevent.

**Claim adjudication**

- `type`: missing_required_parameter
- `claim`: the Project's private-doc recipe omits `name` and `parent` plus the container-resolution rule, while the tool requires all four fields and the source skill carries them.
- `evidenceRefs`: `Custom Instructions.md:299`, `claude project/README.md:125`, `mcp-click-up/feature-catalog/mcp-medium-priority/create-document.md:38`, `sk-product-owner/SKILL.md:307-308`
- `counterevidenceSought`: read the whole ClickUp Connector Delivery section (`Custom Instructions.md:239-249`) and the Project guide's transport block (`claude project/README.md:114-125`) for a `parent` or hierarchy rule. Neither names one. Checked whether the offer's "where" question supplies the parent: it does when the user sends a link, and it does not when the user accepts the recommended private doc.
- `alternativeExplanation`: the Project intentionally delegates the container to the connector, which may choose a default parent when one is omitted, and the packet's "required" note may describe the Code Mode manual rather than the connector.
- `finalSeverity`: P1. Not P0, because no write is fabricated and the runtime can still ask a follow-up. Not P2, because the kernel's own recommended path is not executable as documented and two required fields were lost in the mirror.
- `confidence`: high for the omission; medium for the connector's behaviour on a missing `parent` (the repository does not say).
- `downgradeTrigger`: a Project run that accepts the private-doc offer and completes the create with no parent, or a recorded decision that the connector defaults the parent.
- `fix changes`: `AI Systems/Product Owner/claude project/Custom Instructions.md` (line 299 names `name`, `parent`, `visibility`, `create_page: false` and the ask-for-container rule) and `AI Systems/Product Owner/claude project/README.md` (line 125 the same).

#### 2. R3-P1-002 — The Flow knowledge asserts a Figma connector tool set that no repository document evidences for that surface

**Severity:** P1 (traceability / assumed capability)
**Evidence:** `[SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:311]` says "A Figma connector in this Project turns Mermaid text into a FigJam diagram through its diagram tool, `generate_diagram` on Figma's server". `[SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:345]` says "The read is the connector's read tool, `get_figjam` on Figma's server, node by node", `[SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:314]` names a `whoami` tool, and `[SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:45]` names `get_screenshot`. The only repository source for those names is the skill side: `[SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:334]` describes "The hosted Figma MCP", and `[SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:338]` says Figma marks `generate_diagram` remote-only and that the packet "waits for a live session to name the native tool prefix, because no source confirms one". The vendored Figma packet documents a different surface entirely: `[SOURCE: AI Systems/Product Owner/mcp-figma/SKILL.md:38]` is a CLI (verify the binary, choose a connect mode, bring up the daemon), and `mcp-figma/` contains no `generate_diagram`, `get_figjam`, `get_screenshot` or `whoami` line at all.

**Why it matters:** The Project has no hub and no CLI; its whole Figma capability rests on a hosted connector whose tool names the repository cannot confirm, and whose source explicitly says the prefix is unconfirmed. Presenting the names as fact makes the Flow gate's "read calls the write will spend" and the read-back contract depend on an unverified interface. The kernel itself is correctly conditional ("With a Figma connector that writes diagrams"), so the overreach is in the knowledge mirror, which states the surface as settled.

**Claim adjudication**

- `type`: unverified_capability_claim
- `claim`: the Project knowledge names `generate_diagram`, `get_figjam`, `get_screenshot` and `whoami` as the claude.ai Figma connector's tools, and the repository's only supporting source says the native tool prefix is unconfirmed.
- `evidenceRefs`: `knowledge/Product Owner - Templates - Flow Mode.md:311`, `:314`, `:345`, `sk-create-figjam/references/flow-mode.md:334-338`, `mcp-figma/SKILL.md:38`
- `counterevidenceSought`: searched `mcp-figma/` for every one of the four names (zero matches) and searched the Product Owner tree for another Figma-connector source. `claude project/README.md` documents no Figma connector at all (iteration 2). The `SYNC.md` notes describe the Flow mirrors as hand-written in "connector terms", which is a decision to translate, not evidence of the connector's schema.
- `alternativeExplanation`: the connector may be a standard hosted Figma MCP whose server-side tool names are stable enough that the packet's caution concerns only the client prefix; the mirror may have dropped the prefix caveat deliberately as a Project-side mechanic.
- `finalSeverity`: P1. The route cannot be validated from the repository and the claim is stated as fact in the document that gates the write. P2 would fit if the kernel's conditional wording carried into the knowledge file; it does not.
- `confidence`: high that the repository does not evidence the names; medium that the names are wrong.
- `downgradeTrigger`: a connector schema capture for the claude.ai Figma connector, or a Project run that completes a `generate_diagram` write and a `get_figjam` read.
- `fix changes`: `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md` (mark the tool set as reported-by-the-connector with the no-tool fallback) and a `SYNC.md` decision sentence.

### P2 Findings

#### 3. R3-P2-001 — The ClickUp parameters are evidenced for the Code Mode manual, which the packet explicitly says was not the claude.ai connector

**Severity:** P2 (provenance doubt stated)
**Evidence:** `[SOURCE: AI Systems/Product Owner/mcp-click-up/SKILL.md:26]` ends its contract table with "The claude.ai ClickUp connector was not re-checked on 2026-10-08." The same table's evidence is the Code Mode manual: `[SOURCE: AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-high-priority/get-task.md:18]` records the live name as `clickup_official.clickup_official_clickup_get_task` "when the hosted server registered 61 tools on that date", and `[SOURCE: AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:125]` lists `clickup_create_document` with `name`, `parent`, `visibility`, `create_page` from the server schema. The kernel states the result as the connector's own contract: `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:241]` "This Project reaches ClickUp through the claude.ai ClickUp connector … deliver artifacts with the connector's markdown-aware parameters only", then `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:243]` to `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:246]`.

**Why it matters:** The parameter values (`markdown_description`, `include: ["description"]`, `content_format: "text/md"`) are well evidenced for the hosted server the Code Mode manual calls, and the short tool names are the server's own names before the manual's prefix. The one gap is that no repository document confirms the connector exposes them under those short names. Recording it keeps the difference between "documented for a sibling surface" and "verified for this surface" visible, which is what focus question four asks for.

**Doubt stated:** The likely answer is that the connector exposes the same 61 server tools without the `clickup_official.` prefix, so the kernel is probably right. The repository cannot settle it, and the packet says so itself.

**Fix changes:** `AI Systems/Product Owner/claude project/README.md` (one sentence naming the evidence surface and its date), plus the kernel only if a connector schema check contradicts it.

#### 4. R3-P2-002 — The Flow tag step assumes the connector exposes a Figma Plugin API method

**Severity:** P2 (unverified capability claim)
**Evidence:** `[SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:320]` says "tag every node the write created in one more call to the connector's write tool. The call runs `setSharedPluginData` with a fixed namespace of `productowner`". `[SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Hybrid Workflow.md:160]` repeats it as "shared plugin data written with `setSharedPluginData`". `setSharedPluginData` is a Figma Plugin API method, not a tool name, and `mcp-figma/` contains no mention of it.

**Why it matters:** The step is optional ("only when the gate named this write") and the kernel never mentions it, so the blast radius is small. It is still a Project Knowledge instruction that names a callable the runtime may have no way to make, and the fallback (skip the tag) is not written beside it.

**Fix changes:** `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md` (name the connector capability conditionally, with the skip path) and `Product Owner - Templates - Flow Hybrid Workflow.md` (the same).

## Traceability Checks

| Protocol | Status | Evidence |
| --- | --- | --- |
| `spec_code` (core) | partial | Focus question four is answered item by item: three ClickUp parameters evidenced via the Code Mode manual, one private-doc recipe incomplete, four Figma tool names unverified for the connector. |
| `checklist_evidence` (core) | notApplicable | No `checklist.md` in the staging folder. |
| `skill_agent` (overlay) | fail | The Project mirror lost required fields the skill carries (`sk-product-owner/SKILL.md:307-308`), the subject of R3-P1-001. |
| `agent_cross_runtime` (overlay) | notApplicable | No agent definition in scope. |
| `feature_catalog_code` (overlay) | partial | The feature catalog backs the ClickUp names and fields for the hosted server; it does not cover the claude.ai connector or any Figma connector tool. |
| `playbook_capability` (overlay) | deferred | The playbook files under `sk-create-figjam/manual-testing-playbook/` exercise the CLI `fj` route, not a Project connector. |

## Parameters and their evidence

| Assumed by the Project | Where it is assumed | Repository evidence | Verdict |
| --- | --- | --- | --- |
| `clickup_create_task` + `markdown_description` | `Custom Instructions.md:243` | `mcp-click-up/SKILL.md:20-24`, `references/mcp-tools.md:125` (Code Mode manual, 2026-10-08) | evidenced for the manual, not re-checked for the connector (R3-P2-001) |
| `clickup_update_task` + `markdown_description` | `Custom Instructions.md:244` | the same table | evidenced for the manual |
| `clickup_get_task` + `include: ["description"]` | `Custom Instructions.md:246` | `feature-catalog/mcp-high-priority/get-task.md:29-37` | evidenced for the manual |
| `clickup_create_document` + `visibility: "PRIVATE"` + `create_page: false` | `Custom Instructions.md:299`, `claude project/README.md:125` | `feature-catalog/mcp-medium-priority/create-document.md:30-38` | field set incomplete in the Project (R3-P1-001) |
| `clickup_create_document_page` + `content_format: "text/md"` | `Custom Instructions.md:245`, `claude project/README.md:125` | `feature-catalog/mcp-low-priority/create-doc-page.md:32-39` | evidenced for the manual |
| Figma `generate_diagram` | `knowledge/.../Templates - Flow Mode.md:311` | `sk-create-figjam/references/flow-mode.md:334-338` only; `mcp-figma/` has none | unverified for the connector (R3-P1-002) |
| Figma read tool `get_figjam` / `get_screenshot` | `knowledge/.../Templates - Flow Mode.md:345`, `:45` | the same skill source; no packet | unverified (R3-P1-002) |
| Figma `whoami` | `knowledge/.../Templates - Flow Mode.md:314` | the same skill source; no packet | unverified (R3-P1-002) |
| `setSharedPluginData` tag | `knowledge/.../Templates - Flow Mode.md:320` | none | unverified (R3-P2-002) |

## What iterations 1 and 2 left open

- **Iteration 1's open question** (whether a live runtime resolves ALWAYS 1 against Flow Mode in practice) stays open; the repository cannot run the Project. R1-P1-001 still stands on the text.
- **Iteration 2's open question** (which surfaces expose the connectors and where they are added) stays open. This iteration narrows it: the repository's only transport evidence is a Code Mode manual plus a named hosted Figma MCP, so the connector surface is unverified from both ends — setup (iteration 2) and tool names (this iteration).
- **Iteration 1's Quick-energy drift (R1-P1-002)** was re-checked against the final kernel text before synthesis: the `natural_quick` regex at `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:511]` still has no just-do-it branch. It stands.

## Ruled out

- **`clickup_create_task` with `markdown_description`** — searched for a contrary parameter name. `[SOURCE: AI Systems/Product Owner/mcp-click-up/SKILL.md:24]` says the server has no `markdown_content` or plain `description` parameter, so the kernel's choice is the documented one. No finding beyond the surface caveat.
- **`include_markdown_description=true`** — the older API form is documented as a raw-REST behaviour in `[SOURCE: AI Systems/Product Owner/mcp-click-up/SKILL.md:26]`; the kernel uses the MCP `include` array, which matches `[SOURCE: AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-high-priority/get-task.md:29]`. No finding.
- **`visibility: "PRIVATE"`** — valid per `[SOURCE: AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-medium-priority/create-document.md:30]`. No finding.
- **A Figma connector documented in `mcp-figma/`** — the packet has an `INSTALL-GUIDE.md`, an MCP section and a `references/` tree, all CLI. Searched for `generate_diagram`, `get_figjam`, `get_screenshot`, `whoami` and "connector": zero matches. No finding beyond R3-P1-002.

## Open Questions

- **What the claude.ai ClickUp connector exposes and requires.** `[SOURCE: AI Systems/Product Owner/mcp-click-up/SKILL.md:26]` says it was not re-checked. Whether it accepts `parent`-less document creation, and whether it exposes the 61 server tools under unprefixed names, cannot be settled here (R3-P1-001, R3-P2-001).
- **What the claude.ai Figma connector exposes.** The only source names a hosted Figma MCP, marks `generate_diagram` remote-only, and says no source confirms the native tool prefix (`[SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:338]`). The repository cannot answer what the connector's tool names are (R3-P1-002).
- **Whether the Project's Flow intake can run without a Figma connector at all.** The kernel's no-connector bullet is written, but no Project-surface check exercises it (iteration 2's R2-P2-001).

## Next Dimension

None. Iteration 3 of 3 is complete; synthesis follows.

Review verdict: CONDITIONAL
