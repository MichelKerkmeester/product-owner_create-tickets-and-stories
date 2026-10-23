# Iteration 003 — Deep Review

## Dispatcher

- Mode: review; target_agent: deep-review; execution: inline lineage executor (no nested dispatch)
- Iteration: 3 of 5; Dimension: traceability (contract consistency)
- Lineage: sessionId=fanout-deepseek-1792580454700-vajsq8, generation=1, lineageMode=new
- Sources read this iteration: `specs/product-owner/018-product-owner-deep-review/003-mcp-click-up/spec.md`, `specs/product-owner/018-product-owner-deep-review/003-mcp-click-up/review/lineages/deepseek/steer.md`, `deep-review-strategy.md`, `AI Systems/Product Owner/AGENTS.md`, `AI Systems/Product Owner/SKILL.md`, `AI Systems/Product Owner/ROUTER.md`, `AI Systems/Product Owner/hub-router.json`, `AI Systems/Product Owner/mode-registry.json`, `AI Systems/Product Owner/leaf-manifest.json`, `AI Systems/Product Owner/description.json`, `AI Systems/Product Owner/sk-product-owner/SKILL.md`, `AI Systems/Product Owner/sk-product-owner/references/doc-mode.md`, `AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md`, `AI Systems/Product Owner/mcp-click-up/SKILL.md`, `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md`, `AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-medium-priority/create-document.md`

## Dimension

Traceability — does the hub and `sk-product-owner` description of the packet match what the packet can actually do, at the three points the steer names: routing, push targets, and the ClickUp handoff.

## Files Reviewed

- `AI Systems/Product Owner/AGENTS.md:104-125, 160-170`
- `AI Systems/Product Owner/SKILL.md:1-60, 100-140`
- `AI Systems/Product Owner/ROUTER.md:1-121`
- `AI Systems/Product Owner/hub-router.json` (full)
- `AI Systems/Product Owner/mode-registry.json` (full)
- `AI Systems/Product Owner/leaf-manifest.json` (mcp-click-up entry and header)
- `AI Systems/Product Owner/description.json` (full)
- `AI Systems/Product Owner/sk-product-owner/SKILL.md:279-312`
- `AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:414-418`
- `AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md:190-200`
- `AI Systems/Product Owner/mcp-click-up/SKILL.md:100-180`
- `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:120-135, 245-270`
- `AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-medium-priority/create-document.md:15-60`

## Findings by Severity

### P0 Findings

None.

### P1 Findings

1. **The hub counts a `cupt`-only runtime as ClickUp tooling, so it promises a push the packet cannot perform** -- AI Systems/Product Owner/AGENTS.md:117 -- the ClickUp Handoff trigger list is "native ClickUp MCP, or the vendored `mcp-click-up/` packet's `cupt` CLI or ClickUp MCP via Code Mode". `cupt` has no create command and no document command: the packet's own routing table marks task creation and every document operation "**MCP only** / n/a" (`mcp-click-up/SKILL.md:91-92`), and the whole cupt surface is listing, details, completion, notes, time, tags, attachments and workspace (`mcp-click-up/references/cupt-commands.md:74-262`). An offer to "push this to {link}" for a Task, Bug, Story or Doc therefore has no route on a cupt-only runtime, yet the hub's list arms it.
Finding class: capability-contract-mismatch
Scope proof: both halves are shipped in this repository — the trigger list in `AGENTS.md:117` and the packet's own "MCP only" table it routes to; no external fact is needed to see the gap.
Affected surface hints: `AGENTS.md` (fix site, hub), `sk-product-owner/SKILL.md:279-286` (Section 7's narrower trigger list), `mcp-click-up/SKILL.md:91-92` (the surface that decides)
Case: a runtime has `cupt` installed and no ClickUp MCP. A finished Task artifact triggers the ClickUp offer, the user answers "yes, push it", and the agent has no create-task call to make; it must reverse the offer after asking for approval, which is the one moment the handoff exists to avoid.
Fix site: `AI Systems/Product Owner/AGENTS.md:117` — either drop the bare `cupt` CLI from the offer trigger and keep it for the operations it can perform (comment, tag, time, attach), or state the cupt-only branch: offer a comment or tag handoff, and say a task or doc push needs the MCP.
Claim adjudication:
```json
{
  "claim": "The hub's ClickUp handoff trigger includes a cupt-only runtime, while the packet it delegates to documents task creation and document operations as MCP-only, so the offered push cannot be completed there.",
  "evidenceRefs": [
    "AI Systems/Product Owner/AGENTS.md:117",
    "AI Systems/Product Owner/sk-product-owner/SKILL.md:283",
    "AI Systems/Product Owner/mcp-click-up/SKILL.md:91",
    "AI Systems/Product Owner/mcp-click-up/references/cupt-commands.md:74"
  ],
  "counterevidenceSought": "Searched the whole cupt reference and the ten cupt feature-catalog areas for a create or document command and found none; checked whether Section 7's narrower trigger list could be read as governing AGENTS.md and found it cannot, because AGENTS.md states the trigger set in its own words before pointing at Section 7 only for the offer's content.",
  "alternativeExplanation": "A cupt-only runtime could still push by posting the artifact as a comment on an existing task. That is a real route, but it is not the push the offer names: the offer names a list link for a new task or a private doc, and neither exists on cupt.",
  "finalSeverity": "P1",
  "confidence": "high",
  "downgradeTrigger": "If AGENTS.md is read as descriptive of the general case and Section 7 as the operative rule, the divergence becomes a wording defect and the severity drops to P2. The two documents do not say which governs, so P1 stands."
}
```

2. **The private-doc push recipe omits a required parameter and folds page creation into the create call** -- AI Systems/Product Owner/sk-product-owner/SKILL.md:306 -- Section 7 says "A private doc is `clickup_create_document` with `visibility: "PRIVATE"` and one page carrying the artifact through `content_format: "text/md"`". The packet's card and tool reference both make `create_page` a required parameter, and both state that the call takes no content: text is added afterwards with `clickup_create_document_page` or `clickup_update_document_page` (`mcp-click-up/feature-catalog/mcp-medium-priority/create-document.md:31-38`, `mcp-click-up/references/mcp-tools.md:251-266`). A reader of Section 7 alone writes a call the server schema rejects or a document with no page.
Finding class: parameter-contract-drift
Scope proof: the recipe, the required-parameter table and the "takes no content" sentence are all inside this repository; the packet is the delegated owner of the mechanics and disagrees with the hub's summary.
Affected surface hints: `sk-product-owner/SKILL.md:306` (fix site), `sk-product-owner/references/doc-mode.md:416` (the doc-side repetition), `mcp-click-up/references/mcp-tools.md:251` (the authority)
Case: a user approves "upload it as a private ClickUp doc instead" on a runtime with only Code Mode; an agent that follows Section 7 calls `clickup_create_document` with `name`, `parent`, `visibility` and page content, omits `create_page`, and the first push of the session fails on a required parameter the packet documents one folder away.
Fix site: `AI Systems/Product Owner/sk-product-owner/SKILL.md:306` — name `create_page` and split the recipe into the create call and the page write, keeping the packet as the authority for the field list.
Claim adjudication:
```json
{
  "claim": "Section 7's private-doc recipe omits create_page, which the packet marks required, and describes content going into a call the packet says takes no content.",
  "evidenceRefs": [
    "AI Systems/Product Owner/sk-product-owner/SKILL.md:306",
    "AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-medium-priority/create-document.md:31",
    "AI Systems/Product Owner/mcp-click-up/feature-catalog/mcp-medium-priority/create-document.md:38",
    "AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:251"
  ],
  "counterevidenceSought": "Read the packet's create-document card and the tool reference's document section for any variant where create_page is optional or content is accepted; found none, and found an explicit sentence that the tool takes no content.",
  "alternativeExplanation": "The schema may default create_page when omitted. Even then the recipe produces an empty document before the page write and still misdescribes the call, so the finding survives with a smaller blast radius.",
  "finalSeverity": "P1",
  "confidence": "high",
  "downgradeTrigger": "If a live call shows create_page is optional and the server accepts content on create, the finding drops to P2 (wording) rather than P1 (failed call)."
}
```

### P2 Findings

1. **`doc-mode.md` names `mcp-tooling` as the transport owner, a packet that does not exist in this repository** -- AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:416 -- "An approved push follows the `mcp-tooling` ClickUp transport contract". Product Owner has no `mcp-tooling` packet: the vendored folder is `mcp-click-up/`, and every other pointer in the hub names `mcp-click-up/SKILL.md` (`AGENTS.md:117`, `SKILL.md:26`, `hub-router.json:70-78`). `mcp-tooling` is the shared skill repo's parent folder, so the name is true upstream and stale here.
Finding class: stale-reference
Scope proof: a directory listing of the hub root shows the packet set, and the same file's sibling references already use the vendored name, so the fix is a rename rather than a new concept.
Affected surface hints: `sk-product-owner/references/doc-mode.md:416` (fix site), `AGENTS.md:117` (the naming the rest of the hub uses)
Case: an agent writing a Doc reads Doc Mode, looks for an `mcp-tooling` packet to load, finds none in this repository, and either falls back to the shared tree or skips the contract entirely.
Fix site: `AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:416` — name `mcp-click-up/SKILL.md`, the way `AGENTS.md` and the hub router do.

2. **The packet's INSTALL route loads a packet-root file the hub's leaf contract cannot register** -- AI Systems/Product Owner/ROUTER.md:19 -- the leaf contract is stated as `<packet>/references|assets/...`, and `leaf-manifest.json` accordingly registers three `references/` leaves for `mcp-click-up` (`cupt-commands.md`, `mcp-tools.md`, `troubleshooting.md`). The packet's own router has four intents, and its `INSTALL` intent loads `INSTALL-GUIDE.md` at the packet root together with `references/troubleshooting.md` (`mcp-click-up/SKILL.md:146,176`). That leaf is unrepresentable: it is neither under `references/` nor under `assets/`, so it has no `leafResourceId` and no canonical pair.
Finding class: unrepresentable-leaf
Scope proof: the restriction and the manifest are both hub files; the disagreeing route is the packet's own `RESOURCE_MAP`, inside the same repository.
Affected surface hints: `ROUTER.md:19` and `leaf-manifest.json` (fix sites, hub) or the packet's `RESOURCE_MAP` (upstream)
Case: a benchmark replay or a checker that projects `RESOURCE_MAP` entries to `(workflowMode, leafResourceId)` pairs reaches the INSTALL leaf, finds no manifest entry, and either drops the leaf or fails the packet; a hub-routed "how do I install cupt" request is described as loading two references while the packet would load the install guide first.
Fix site: `AI Systems/Product Owner/ROUTER.md:19` — widen the leaf contract to the packet root, or record the install guide as an explicit non-leaf resource with its reason.

## Traceability Checks

- `Core: spec_code` — the spec's three entries plus the steer's named hub surfaces (routing, push targets, ClickUp handoff) were read; the two P1s sit exactly on those surfaces. Status: pass.
- `Core: checklist_evidence` — no checklist exists in the staging wrapper; the review rulings in `steer.md:1-11` were applied, including "every finding inside mcp-click-up/ names the upstream file as the fix site" (both packet-side findings here are named that way). Status: pass.
- `Overlay: skill_agent` — hub `SKILL.md` to packet `SKILL.md` handoff: `hub-router.json` declares `mcp-click-up/SKILL.md` as the mode resource, `SKILL.md:26` calls the packet "Vendored", and the packet's Section 2 owns the intra-packet routing. Status: pass.
- `Overlay: agent_cross_runtime` — `AGENTS.md` is the only runtime bootstrap in this repository and it agrees with `SKILL.md` on routing. Status: pass, with the handoff finding above.

## Integration Evidence

- `hub-router.json:70-78` routes `mcp-click-up` on the three signals `mcp-click-up`, `cupt`, `clickup mcp`; `SKILL.md:56` and `ROUTER.md:62` list the same three, so routing vocabulary is one source of truth across three files.
- `mode-registry.json:25-31` places `mcp-click-up` and `mcp-figma` in the `vendored-packets` extension and names `vendor.json` plus `scripts/vendor-sync.py status, pull and push` as the mechanism, which is the same mechanism iterations 1 and 2 verified.
- `SKILL.md:14` version authority ("This file's `version` frontmatter ... `description.json`, `mode-registry.json` and `hub-router.json` carry the same value") holds: all four read `1.0.0.0`.
- `sk-product-owner/assets/interactive-response-templates.md:193-194` reproduce the two closing lines from Section 7 verbatim, so the reply shape is consistent with the push-target rules.
- `.env.example` declares exactly the four variables Section 7 reads (`CLICKUP_TASK_LIST_URL`, `CLICKUP_BUG_LIST_URL`, `CLICKUP_STORY_LIST_URL`, `CLICKUP_DOC_PARENT_URL`) and `.gitignore:10-12` keeps `.env` out of git while tracking the example.

## Edge Cases

- The hub never states which document governs when `AGENTS.md:117` and Section 7 differ; that ambiguity is why finding 1 is recorded at P1 with the downgrade path written out rather than silently normalised.
- `claude project/` mirrors the skill by hand and is outside the spec's declared scope, so the divergence between it and this review's fix sites was not audited here.

## Confirmed-Clean Surfaces

- Push-target variable names, their meaning, and the two closing lines are identical in `sk-product-owner/SKILL.md:293-308`, `.env.example`, and `sk-product-owner/assets/interactive-response-templates.md:193-194`.
- The transport parameter table in Section 7 (`markdown_description`, `content_format: "text/md"`, `include: ["description"]`) matches `AGENTS.md:117` and the packet's Markdown Transport Contract (`mcp-click-up/SKILL.md:20-26`, `references/mcp-tools.md:205`).
- Mode identity: `description.json`, `mode-registry.json`, `hub-router.json` and hub `SKILL.md` all read version `1.0.0.0`, as the hub's own version-authority paragraph requires.
- `ROUTER.md`'s CLICK_UP leaf set (`references/cupt-commands.md`, `references/mcp-tools.md`) resolves on disk and both are registered in `leaf-manifest.json`.

## Ruled Out

- "The hub and the packet disagree about how to reach ClickUp in markdown": all three transport sites agree.
- "Push-target names drifted between the skill, the env example and the reply templates": they match exactly.
- "The four hub documents carry different versions": all read 1.0.0.0.

## Next Dimension

- Dimension: references and paths
- Focus area: every relative link, repository-relative path and version header in the packet and in the hub surfaces that point into it, including the install-guide invocation, the `scripts/README.md` commands, and the changelog to `SKILL.md` version line
- Reason: the P2s this iteration found are both stale pointers, so the dimension deserves a systematic sweep rather than another spot check
- Rotation status: correctness, security and traceability complete; references next

## Source Tags

- R3-P1-001 — [SOURCE: AGENTS.md:117]
- R3-P1-002 — [SOURCE: sk-product-owner/SKILL.md:306]
- R3-P2-001 — [SOURCE: sk-product-owner/references/doc-mode.md:416]
- R3-P2-002 — [SOURCE: ROUTER.md:19]

## Verdict

Two P1 and two P2 findings this iteration, no P0. The hub's handoff is well built where it is specified — transport parameters, push-target names and routing vocabulary are consistent — but two of its pointers are wrong in ways that fail at the moment of use: a cupt-only offer that cannot be kept, and a private-doc recipe that omits a required parameter. Release-blocking: no, conditional on the two hub fixes.

Review verdict: CONDITIONAL
