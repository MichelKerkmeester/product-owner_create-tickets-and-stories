# Deep Review — Iteration 2

## Dimension

Security: path containment and symlink handling, plugin manifests, public-repository leakage, and the Flow Mode write gate

## Files Reviewed

* scripts/vendor-sync.py — manifest path resolution and mutating copy/delete paths [SOURCE: scripts/vendor-sync.py:160] [SOURCE: scripts/vendor-sync.py:174] [SOURCE: scripts/vendor-sync.py:214]
* scripts/build-plugin.py — source collection, output deletion and copy paths [SOURCE: scripts/build-plugin.py:68] [SOURCE: scripts/build-plugin.py:108] [SOURCE: scripts/build-plugin.py:117]
* sk-product-owner/scripts/flow_check.py — caller-selected model read path [SOURCE: sk-product-owner/scripts/flow_check.py:70] [SOURCE: sk-product-owner/scripts/flow_check.py:156]
* sk-product-owner/scripts/vendored/mermaid_extract.py — caller-selected input and output paths [SOURCE: sk-product-owner/scripts/vendored/mermaid_extract.py:252] [SOURCE: sk-product-owner/scripts/vendored/mermaid_extract.py:1395]
* vendor.json and both files under claude-plugin/.claude-plugin/
* sk-product-owner/references/flow-mode.md, sk-product-owner/assets/flow-templates.md, AGENTS.md and claude project/Custom Instructions.md
* Three Product Owner worked examples for the public-link scan

## Findings by Severity

### P0

#### R1-P1-001 — Manifest paths can redirect sync writes outside package roots

* Case: A changed checkout supplies an absolute or parent-traversing local_path, upstream_path or include entry, then an operator runs vendor-sync.py pull or push
* File: scripts/vendor-sync.py:160
* Evidence: resolve_dirs joins manifest values without canonical containment checks. The include branch then copies or unlinks through joined paths. The non-include branch recursively removes the target before copying. pull_package skips its drift refusal when the recorded baseline is empty, then reaches the copy and manifest update [SOURCE: scripts/vendor-sync.py:160] [SOURCE: scripts/vendor-sync.py:174] [SOURCE: scripts/vendor-sync.py:185] [SOURCE: scripts/vendor-sync.py:214] [SOURCE: scripts/vendor-sync.py:225]
* User impact: A sync command on a checkout with altered vendor metadata can overwrite or delete files outside the repository or shared-skill package
* Finding class: class-of-bug
* Scope proof: Current vendor.json paths are in-tree, but shared path resolution does not reject absolute paths, traversal, resolved-root escapes or symlinked parent components
* Recommendation: Resolve and reject every package and include path outside its designated root before hashing or mutation; reject unsafe symlink components and cover pull and push escape cases with isolated tests
* Re-verified from iteration 1. Severity is raised from P1 to P0 because the path reaches recursive deletion and file overwrite/unlink operations

~~~json
{
  "findingId": "R1-P1-001",
  "claim": "Manifest-controlled package and include paths can escape their designated roots and reach destructive sync operations.",
  "evidenceRefs": ["scripts/vendor-sync.py:160", "scripts/vendor-sync.py:174", "scripts/vendor-sync.py:185", "scripts/vendor-sync.py:214", "scripts/vendor-sync.py:225", "scripts/vendor-sync.py:247"],
  "counterevidenceSought": "The current manifest uses in-tree paths; pull is explicit; recorded local drift blocks some pulls; push requires a baseline. The empty-baseline branch bypasses the pull conflict check, and none of these conditions validates containment.",
  "alternativeExplanation": "vendor.json may be treated as trusted repository configuration and operators intentionally request pull or push. That narrows the trigger but does not confine the destructive target.",
  "finalSeverity": "P0",
  "confidence": 0.98,
  "downgradeTrigger": "All package and include paths are canonicalized beneath their roots before reads or writes, symlink components are safely contained, and escape cases prove outside paths remain unchanged."
}
~~~

#### R2-P0-001 — Plugin build can delete an external skills directory through a symlinked parent

* Case: A checkout makes claude-plugin a symlink to an outside directory containing skills, then an operator runs the plugin builder
* File: scripts/build-plugin.py:117
* Evidence: The builder forms root/claude-plugin/skills without validating the parent. If the child exists, it calls shutil.rmtree. A symlink at skills itself is rejected by rmtree, but a symlink at claude-plugin is followed while resolving the child [SOURCE: scripts/build-plugin.py:108] [SOURCE: scripts/build-plugin.py:117] [SOURCE: scripts/build-plugin.py:119]
* User impact: A build can recursively delete an outside directory named skills
* Finding class: class-of-bug
* Scope proof: Neither the plugin parent nor the resolved output path is checked against root before deletion
* Recommendation: Reject symlinks in the plugin output path and verify the resolved deletion target is a child of the repository root

~~~json
{
  "findingId": "R2-P0-001",
  "claim": "The plugin builder can recursively delete an outside skills directory when the claude-plugin parent is a symlink.",
  "evidenceRefs": ["scripts/build-plugin.py:108", "scripts/build-plugin.py:117", "scripts/build-plugin.py:119", "scripts/build-plugin.py:124"],
  "counterevidenceSought": "The current plugin is a regular in-repository directory, and rmtree refuses when its direct argument is itself a symlink. That does not protect a regular child reached through a symlinked parent.",
  "alternativeExplanation": "The builder is expected to run on trusted repository contents, so an attacker must first place a symlinked parent in the checkout and induce a build.",
  "finalSeverity": "P0",
  "confidence": 0.95,
  "downgradeTrigger": "The builder rejects symlinked path components and proves the resolved deletion target remains beneath the configured repository root."
}
~~~

### P1

#### R1-P2-002 — Plugin build can package content from a symlinked hub source

* Case: A root hub file such as SKILL.md is a symlink to a file outside the checkout when the plugin build runs
* File: scripts/build-plugin.py:71
* Evidence: Hub files enter the source map without the symlink check used for entries inside packet walks. copyfile follows the hub source, and the later hash comparison accepts the copied external bytes because it hashes the same source target [SOURCE: scripts/build-plugin.py:71] [SOURCE: scripts/build-plugin.py:77] [SOURCE: scripts/build-plugin.py:124] [SOURCE: scripts/build-plugin.py:125]
* User impact: External or secret content can enter a plugin artifact that is later published
* Finding class: class-of-bug
* Scope proof: All four HUB_FILES enter through the unchecked loop; the existing self-test plants a link only inside a packet [SOURCE: scripts/build-plugin.py:45] [SOURCE: scripts/build-plugin.py:71] [SOURCE: scripts/build-plugin.py:144] [SOURCE: scripts/build-plugin.py:163]
* Recommendation: Reject symlinks for every mapped source before copying and add a self-test for each hub-source path
* Re-verified from iteration 1 and escalated from P2 because the bypass can package external secret material

~~~json
{
  "findingId": "R1-P2-002",
  "claim": "A symlinked root hub source bypasses the source scan and can make the plugin package bytes from outside the repository.",
  "evidenceRefs": ["scripts/build-plugin.py:45", "scripts/build-plugin.py:68", "scripts/build-plugin.py:71", "scripts/build-plugin.py:77", "scripts/build-plugin.py:124", "scripts/build-plugin.py:125"],
  "counterevidenceSought": "Packet walks reject discovered symlinks and the output hash proves copied bytes match the source. The source hash follows the symlink too, so byte equality does not prove an in-repository source.",
  "alternativeExplanation": "A hub symlink may be an accidental local state and the built plugin may never be published. Disclosure occurs if the artifact is distributed.",
  "finalSeverity": "P1",
  "confidence": 0.92,
  "downgradeTrigger": "Every source path, including all HUB_FILES and packet roots, is checked before mapping and the self-test refuses a planted hub-source symlink."
}
~~~

#### R2-P1-001 — Hosted rollback can clear unrelated content on the target page

* Case: A hosted diagram write partially succeeds on a page that already contains unrelated nodes, then the operator follows the stated rollback
* File: sk-product-owner/references/flow-mode.md:116
* Evidence: The gate names the target plan, file, page, effect and rollback and waits for yes, but the hosted rollback is to clear the whole page. It does not require that page to be empty or dedicated to the generated diagram [SOURCE: sk-product-owner/references/flow-mode.md:63] [SOURCE: sk-product-owner/references/flow-mode.md:111] [SOURCE: sk-product-owner/references/flow-mode.md:116]
* User impact: A rollback can remove board content unrelated to the attempted flow
* Finding class: class-of-bug
* Scope proof: The fallback route names page duplication and Undo/history; the hosted route instead names page clearing without an empty-page precondition [SOURCE: sk-product-owner/references/flow-mode.md:116] [SOURCE: sk-product-owner/references/flow-mode.md:126]
* Recommendation: Require a dedicated empty page before the hosted write or remove only the nodes created by that call, and name that scoped rollback in the gate

~~~json
{
  "findingId": "R2-P1-001",
  "claim": "The documented hosted rollback clears the entire destination page and can delete content unrelated to the generated flow.",
  "evidenceRefs": ["sk-product-owner/references/flow-mode.md:63", "sk-product-owner/references/flow-mode.md:111", "sk-product-owner/references/flow-mode.md:116", "sk-product-owner/references/flow-mode.md:126"],
  "counterevidenceSought": "The gate discloses rollback before asking for yes and names the page. The note that nothing else imports the page does not establish that it contains no unrelated content.",
  "alternativeExplanation": "The hosted route may be intended for a newly created dedicated page, but the instructions do not require that condition.",
  "finalSeverity": "P1",
  "confidence": 0.86,
  "downgradeTrigger": "The route requires a dedicated empty page or rollback removes only elements created by the attempted diagram."
}
~~~

### P2

#### R2-P2-001 — Fictional examples still contain clickable Figma URLs

* Case: A reader follows a Figma reference from a public Product Owner worked example
* File: sk-product-owner/assets/examples/story/story-example-complete.md:51
* Evidence: The example contains Figma design and board URLs with placeholder-like slugs, and related bug examples contain Figma file URLs. The slugs and .example documentation host appear synthetic; no external link validation was performed [SOURCE: sk-product-owner/assets/examples/story/story-example-complete.md:51] [SOURCE: sk-product-owner/assets/examples/story/story-example-complete.md:57] [SOURCE: sk-product-owner/assets/examples/story/story-example-complete.md:59] [SOURCE: sk-product-owner/assets/examples/bug/bug-example-frontend-visual.md:31]
* User impact: No private board exposure is established, but clickable Figma URLs in a public Product Owner corpus can be mistaken for live approved references and conflict with a strict no-board-URLs boundary
* Finding class: matrix/evidence
* Scope proof: Exact search of the Product Owner tree found these example URLs; focused Flow Mode files contain only the literal board URL placeholder and no board identifier
* Recommendation: Replace example Figma URLs with non-clickable placeholders if the public-repository rule excludes all board URLs

## Traceability Checks

* Core spec_code: partial. Static security paths were reviewed; phase acceptance mapping was not performed
* Core checklist_evidence: partial. No tests were run in this iteration; the existing builder self-test does not cover hub-source or output-parent symlinks
* Overlay skill_agent: partial. Flow Mode gate wording and hosted/fallback routes were read directly
* Overlay agent_cross_runtime: deferred. No cross-runtime execution was part of this security pass
* Overlay feature_catalog_code: deferred. No feature-catalog behavior mapping was performed
* Overlay playbook_capability: deferred. Playbook behavior was not reviewed in this security slice

The Mermaid extractor SHA-256 matches its vendor.json record. Both Claude plugin manifests have no mcpServers key and no secret-like values. The focused Flow Mode, flow-template and Custom Instructions files contain no actual board URL, screenshot, private filesystem path or account/workspace identifier. The public-link advisory concerns placeholder-looking URLs in unrelated worked examples, not evidence of a copied Barter flow.

## Verdict

Two active P0 path-deletion risks require correction before merge. The hosted rollback and hub-source symlink risks also require action.

## Next Dimension

Traceability

Review verdict: FAIL
