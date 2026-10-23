# Deep Review — Iteration 5

## Dimension

Closing adversarial replay and severity calibration across correctness, security, traceability, and maintainability.

## Files Reviewed

* scripts/vendor-sync.py, scripts/build-plugin.py, vendor.json, and both Claude plugin manifests
* benchmark/gates/check_hub.py, hub-router.json, and root SKILL.md
* sk-product-owner/scripts/flow_check.py, sk-product-owner/scripts/vendored/mermaid_extract.py, Flow Mode, and its templates
* The Change Location flow model in the outer Product Context repository

## Findings by Severity

### P0

None after re-adjudication. R1-P1-001 is P1 because the unsafe path requires an explicit mutating sync command. R2-P0-001 is P2 because its trigger requires a symlinked plugin parent whose external target already supplies a readable plugin manifest and skills directory.

### P1

#### R1-P1-001 — Manifest paths can redirect sync writes outside package roots

~~~json
{
  "findingId": "R1-P1-001",
  "id": 1,
  "severity": "P1",
  "priorSeverity": "P0",
  "cluster": "manifest_path_escape",
  "title": "Manifest paths can redirect sync writes outside package roots",
  "case": "A user runs vendor-sync pull or push with a manifest whose local_path, upstream_path, or include entry escapes its package root.",
  "file": "scripts/vendor-sync.py",
  "line": 164,
  "claim": "Manifest-derived paths are joined to repository roots without rejecting absolute or parent-traversal paths, and copy/delete operations later use those paths.",
  "evidence": "resolve_dirs joins local_path and upstream_path directly; copy_tree deletes an existing target for a full pull and writes included files directly. A manifest-only change can plant the trigger, but a trusted operator must still invoke a mutating command.",
  "evidenceRefs": [
    "scripts/vendor-sync.py:160",
    "scripts/vendor-sync.py:164",
    "scripts/vendor-sync.py:167",
    "scripts/vendor-sync.py:174",
    "scripts/vendor-sync.py:185",
    "scripts/vendor-sync.py:214",
    "scripts/vendor-sync.py:225",
    "scripts/vendor-sync.py:233",
    "scripts/vendor-sync.py:247"
  ],
  "counterevidenceSought": "Checked whether the trigger requires changing the script and whether an automatic privileged caller was established. A data-only manifest change is sufficient after the manifest is tracked; no automatic pull/push caller was established. In this checkout git status reports vendor.json and both sync/build scripts as untracked phase additions, contrary to the prompt's tracked-file premise.",
  "alternativeExplanation": "The manifest is normally maintained with the repository and pull/push are explicit operator actions, so this is a guarded local-tool path error rather than an unattended remote exploit.",
  "finalSeverity": "P1",
  "confidence": "high",
  "downgradeTrigger": "Downgrade to P2 if mutating sync commands are only run on reviewed manifests and no untrusted manifest reaches them; upgrade if privileged CI runs pull/push on untrusted changes.",
  "userImpact": "A malformed or adversarial manifest can overwrite or remove data outside the intended package directories when a mutating sync command runs.",
  "findingClass": "class-of-bug",
  "scopeProof": "Static path review covers resolve_dirs plus both pull and push paths into copy_tree; no path containment check precedes the writes.",
  "affectedSurfaceHints": [
    "vendor manifest",
    "vendor sync pull",
    "vendor sync push"
  ],
  "recommendation": "Reject absolute paths and traversal, resolve local/upstream paths beneath their roots, and validate every include path before any read or write."
}
~~~

#### R2-P1-001 — Hosted rollback can clear unrelated content on the target page

~~~json
{
  "findingId": "R2-P1-001",
  "id": 4,
  "severity": "P1",
  "priorSeverity": "P1",
  "cluster": "hosted_rollback_page_scope",
  "title": "Hosted rollback can clear unrelated content on the target page",
  "case": "A hosted diagram write is incomplete or wrong and the operator follows the documented rollback on a page that already contains unrelated objects.",
  "file": "sk-product-owner/references/flow-mode.md",
  "line": 116,
  "claim": "The rollback instruction clears the whole FigJam page and relies on the unverified claim that nothing else imports that page.",
  "evidence": "The hosted route names the plan but does not require an empty or dedicated page before writes. Its rollback clears the entire page; the general gate requires disclosure and approval but does not establish the page's contents.",
  "evidenceRefs": [
    "sk-product-owner/references/flow-mode.md:63",
    "sk-product-owner/references/flow-mode.md:111",
    "sk-product-owner/references/flow-mode.md:114",
    "sk-product-owner/references/flow-mode.md:116"
  ],
  "counterevidenceSought": "Checked for a dedicated-page or empty-page precondition and item-scoped hosted rollback. Neither appears in the reviewed route.",
  "alternativeExplanation": "If users always choose a newly created empty page, clearing that page removes only the failed diagram; the current instructions do not enforce that condition.",
  "finalSeverity": "P1",
  "confidence": "high",
  "downgradeTrigger": "Downgrade if the hosted route requires and verifies a dedicated empty page or uses item-scoped deletion for rollback.",
  "userImpact": "Following the documented rollback can delete unrelated FigJam content.",
  "findingClass": "class-of-bug",
  "scopeProof": "The hosted rollback is whole-page; the fallback route separately uses page duplication and version history.",
  "affectedSurfaceHints": [
    "hosted FigJam route",
    "rollback instruction",
    "write gate"
  ],
  "recommendation": "Require a verified dedicated empty page before the first hosted write, or make rollback remove only the generated diagram."
}
~~~

#### R3-P1-001 — Flow delivery reply conflicts with the global self-scan rule

~~~json
{
  "findingId": "R3-P1-001",
  "id": 5,
  "severity": "P1",
  "priorSeverity": "P1",
  "cluster": "flow_delivery_reply_conflict",
  "title": "Flow delivery reply conflicts with the global self-scan rule",
  "case": "A Flow Mode response follows the two-line-only delivery instruction while active global Product Owner instructions require an HVR self-scan in every delivery response.",
  "file": "sk-product-owner/references/flow-mode.md",
  "line": 136,
  "claim": "The Flow reply says it carries the board and proof, and nothing else; the root instructions require a separate self-scan line as delivery metadata and do not exempt Flow Mode from it.",
  "evidence": "The Flow section requires board URL and read-back lines and says nothing else. AGENTS.md requires the HVR self-scan beside delivery verification and says the metadata belongs in chat.",
  "evidenceRefs": [
    "sk-product-owner/references/flow-mode.md:136",
    "sk-product-owner/references/flow-mode.md:138",
    "sk-product-owner/references/flow-mode.md:139",
    "AGENTS.md:39",
    "AGENTS.md:50",
    "AGENTS.md:56"
  ],
  "counterevidenceSought": "Checked whether the Flow exemption explicitly waives the self-scan. It waives export/file steps and defines board/read-back output, but the global rule still says every delivery response and its exemption text does not mention the scan.",
  "alternativeExplanation": "The two-line Flow reply might be read as the specialized delivery shape overriding generic response metadata, making the global scan instruction ambiguous rather than impossible.",
  "finalSeverity": "P1",
  "confidence": "high",
  "downgradeTrigger": "Downgrade if the global instructions explicitly exempt Flow Mode from the self-scan, or the Flow reply shape is amended to allow the metadata line.",
  "userImpact": "The agent cannot satisfy both mandatory response contracts for a Flow delivery.",
  "findingClass": "cross-consumer",
  "scopeProof": "The conflict is present in the root instruction surface and routed Flow Mode response section; it is not a one-off response.",
  "affectedSurfaceHints": [
    "global Product Owner delivery contract",
    "Flow Mode delivery",
    "Human Voice self-scan"
  ],
  "recommendation": "Reconcile the Flow reply shape with the global scan metadata rule."
}
~~~

#### R5-P1-001 — Clarification requests can be routed to the Figma tool packet

~~~json
{
  "findingId": "R5-P1-001",
  "id": 6,
  "severity": "P1",
  "cluster": "hub_artifact_word_coverage",
  "title": "Clarification requests can be routed to the Figma tool packet",
  "case": "A request names a figma-ds-cli operation and asks for a clarification without using a listed artifact word or dollar command, such as asking to draft a clarification about Flow output.",
  "file": "hub-router.json",
  "line": 6,
  "claim": "The hub contract says clarification requests use the Product Owner packet, but artifactWords omits clarification; route_stage_one therefore returns the Figma packet when the tool signal is present.",
  "evidence": "The artifact check consults only routerPolicy.artifactWords before collecting tool-signal hits. With no listed artifact word or command, the figma-ds-cli signal is the only hit and routes to mcp-figma. check_hub.py checks only that artifactWords is a non-empty list and its fixed gold rows do not cover clarification.",
  "evidenceRefs": [
    "SKILL.md:18",
    "SKILL.md:31",
    "SKILL.md:33",
    "hub-router.json:6",
    "hub-router.json:28",
    "benchmark/gates/check_hub.py:59",
    "benchmark/gates/check_hub.py:183",
    "benchmark/gates/check_hub.py:201",
    "benchmark/gates/check_hub.py:212"
  ],
  "counterevidenceSought": "Checked the hub's explicit clarification statement, configured artifactWords, routing precedence, and gold-row coverage. Clarification is named in the packet table but absent from words and examples that force the default.",
  "alternativeExplanation": "The author may expect clarification requests to include task/doc/Story vocabulary or a command; the hub promises clarification requests directly, and the packet accepts clarification as an outcome.",
  "finalSeverity": "P1",
  "confidence": "high",
  "downgradeTrigger": "Downgrade only if the hub contract is narrowed so clarification is not independently a Product Owner request; otherwise add the term and a gold row.",
  "userImpact": "A clarification request can start in the tool-only packet, bypassing Product Owner intake and delivery behavior.",
  "findingClass": "class-of-bug",
  "scopeProof": "route_stage_one checks the configured list and returns the sole matching signal; the checker has no parity assertion between the list and documented packet coverage.",
  "affectedSurfaceHints": [
    "hub router",
    "artifactWords policy",
    "hub gold rows"
  ],
  "recommendation": "Add clarification to the artifact vocabulary and a gate row, and make check_hub compare the documented policy inventory with hub-router.json."
}
~~~

### P2

#### R2-P0-001 — Plugin build can delete an external skills directory through a symlinked parent

~~~json
{
  "findingId": "R2-P0-001",
  "id": 2,
  "severity": "P2",
  "priorSeverity": "P0",
  "cluster": "plugin_output_symlink_escape",
  "title": "Plugin build can delete an external skills directory through a symlinked parent",
  "case": "A build runs with claude-plugin resolving through a symlinked parent whose external target already contains .claude-plugin/plugin.json and a skills directory.",
  "file": "scripts/build-plugin.py",
  "line": 117,
  "claim": "shutil.rmtree follows a symlinked parent while removing the skills path, but the trigger requires the parent to resolve to an existing external plugin tree with a readable manifest.",
  "evidence": "build reads plugin.json before computing and removing skills. A symlink at the skills leaf is handled by rmtree's refusal path; the reported case requires a symlink higher in the path and a target satisfying the earlier manifest read.",
  "evidenceRefs": [
    "scripts/build-plugin.py:108",
    "scripts/build-plugin.py:110",
    "scripts/build-plugin.py:113",
    "scripts/build-plugin.py:117",
    "scripts/build-plugin.py:119"
  ],
  "counterevidenceSought": "Checked whether an ordinary tracked-file change can create the required external target and whether the manifest read blocks an absent target. The pre-rmtree read requires a valid plugin.json at the resolved parent; no build workflow that supplies such an external target was established. Current plugin files are untracked additions in this checkout.",
  "alternativeExplanation": "This is primarily a local workspace footgun if a developer deliberately points the plugin directory at another existing plugin tree; a party able to create that filesystem layout can also write broadly in the build workspace.",
  "finalSeverity": "P2",
  "confidence": "high",
  "downgradeTrigger": "Close if the build is restricted to a fresh checkout with a real claude-plugin directory and no externally prepared parent symlink; upgrade if untrusted PR content can make a privileged runner resolve the parent to an existing external plugin tree.",
  "userImpact": "If the filesystem precondition is met, the build can remove the target tree's skills directory.",
  "findingClass": "class-of-bug",
  "scopeProof": "The reviewed sequence is manifest read at line 110, then skills removal at line 119; no normal in-repository data field selects an outside output directory.",
  "affectedSurfaceHints": [
    "plugin build",
    "claude-plugin output"
  ],
  "recommendation": "Resolve and validate the plugin/output paths against the repository root before cleanup, and refuse symlinked parents."
}
~~~

#### R1-P2-002 — Plugin build can package content from a symlinked hub source

~~~json
{
  "findingId": "R1-P2-002",
  "id": 3,
  "severity": "P2",
  "priorSeverity": "P1",
  "cluster": "plugin_source_symlink_leak",
  "title": "Plugin build can package content from a symlinked hub source",
  "case": "A shipped root hub file is replaced by a symlink to a path readable by the process running the plugin build.",
  "file": "scripts/build-plugin.py",
  "line": 71,
  "claim": "The symlink scan runs for packet trees, while HUB_FILES are inserted into the source map without a symlink check; copyfile and hashing follow a hub-source symlink.",
  "evidence": "A contributor can submit a symlinked hub source without changing the builder, but the impact depends on an external sensitive target and a privileged build context. No privileged untrusted-PR build or secret-bearing target was established.",
  "evidenceRefs": [
    "scripts/build-plugin.py:45",
    "scripts/build-plugin.py:68",
    "scripts/build-plugin.py:71",
    "scripts/build-plugin.py:74",
    "scripts/build-plugin.py:77",
    "scripts/build-plugin.py:83",
    "scripts/build-plugin.py:121",
    "scripts/build-plugin.py:124",
    "scripts/build-plugin.py:125"
  ],
  "counterevidenceSought": "Checked whether all shipped source trees share the same symlink scan and whether the copy/hash comparison detects a followed source link. Packet trees are scanned; HUB_FILES are not. The copy/hash comparison reads resolved bytes and does not detect the link itself.",
  "alternativeExplanation": "Most ordinary in-repository symlink targets are public files, and the builder may run only on trusted local content. Secret packaging requires a sensitive target and execution/publishing path not established here.",
  "finalSeverity": "P2",
  "confidence": "medium",
  "downgradeTrigger": "Close if the build rejects or proves containment of every HUB_FILES source before reading; upgrade if privileged automated builds consume untrusted symlink changes and publish output.",
  "userImpact": "A privileged build could include readable external content in the generated plugin package.",
  "findingClass": "class-of-bug",
  "scopeProof": "The scan loop at lines 74-83 covers packet directories only; HUB_FILES are mapped at lines 71-72 then copied at lines 121-125.",
  "affectedSurfaceHints": [
    "plugin build",
    "hub source files",
    "plugin package artifact"
  ],
  "recommendation": "Apply symlink and resolved-root checks to every HUB_FILES source before copying or hashing."
}
~~~

#### R5-P2-001 — Flow color limit has no check before or after the board write

~~~json
{
  "findingId": "R5-P2-001",
  "id": 7,
  "severity": "P2",
  "cluster": "flow_style_rule_enforcement",
  "title": "Flow color limit has no check before or after the board write",
  "case": "A Mermaid model uses several classDef or style directives to assign different accent colors to categories.",
  "file": "sk-product-owner/scripts/vendored/mermaid_extract.py",
  "line": 726,
  "claim": "The extractor drops classDef/style directives before flow_check sees the diagram, and the documented read-back checks counts, labels and connector overlap without checking the one-accent limit.",
  "evidence": "Flow Mode limits the diagram to one accent. The parser discards style directives and flow_check only validates diagram kind, direction, shapes, labels, exits and node count. The read-back checklist does not mention accent count; live generator styling behavior was not tested.",
  "evidenceRefs": [
    "sk-product-owner/references/flow-mode.md:65",
    "sk-product-owner/references/flow-mode.md:95",
    "sk-product-owner/references/flow-mode.md:102",
    "sk-product-owner/scripts/vendored/mermaid_extract.py:726",
    "sk-product-owner/scripts/vendored/mermaid_extract.py:729",
    "sk-product-owner/scripts/vendored/mermaid_extract.py:738",
    "sk-product-owner/scripts/flow_check.py:44",
    "sk-product-owner/scripts/flow_check.py:67"
  ],
  "counterevidenceSought": "Checked static pre-write validation and the written read-back instructions. The parser drops the directives and the read-back list checks counts, labels and connector geometry; no color-count check is stated.",
  "alternativeExplanation": "The hosted generator may ignore Mermaid styling directives, or a human may inspect color as part of screenshot read-back. Neither behavior is established by the reviewed contract.",
  "finalSeverity": "P2",
  "confidence": "medium",
  "downgradeTrigger": "Close if the generator is shown to discard all styles or read-back explicitly verifies the one-accent rule; raise if the generator applies multiple colors and the checker is the sole gate.",
  "userImpact": "A generated board may violate the documented visual constraint and use color as a category scheme.",
  "findingClass": "class-of-bug",
  "scopeProof": "The parser counts and drops style directives and returns without preserving style properties; diagram_problems has no color/style condition.",
  "affectedSurfaceHints": [
    "Flow Mode pre-write check",
    "Mermaid style directives",
    "FigJam read-back"
  ],
  "recommendation": "Reject or inspect style directives before writing, or state an explicit color check in board read-back."
}
~~~

## Traceability Checks

* Core spec_code is partial: the live hub and Flow contracts were compared with their code, while phase 005/006 completion evidence remains open from the prior traceability pass.
* Core checklist_evidence is partial: self-test structure was read statically; no tests or gates were run in this review.
* Overlay skill_agent fails because Flow Mode still conflicts with the global delivery self-scan and the hub omits a documented clarification route.
* Overlay agent_cross_runtime is partial: the hub route function and config were read directly, but no runtime behavior was executed.
* Feature-catalog and playbook capability overlays were not reassessed in this final slice.
* The Flow parser sweep found that full-line comments are removed, subgraphs become rejected container shapes, ampersand endpoint groups expand to concrete edges, and each outgoing edge is counted against its source decision. Self-loops remain explicit edges. Quote-aware masking protects node and operator parsing; an edge label terminator uses the next raw vertical bar, so quoted bars are outside the evidenced input contract.
* Style and class directives are discarded before flow_check. The visual one-accent rule is not checked by the current pre-write or read-back instructions, recorded as R5-P2-001.
* Both plugin manifests parse as JSON; plugin name and version agree, the marketplace points to ./, and no MCP registration is present. The Change Location model has a provenance row for each of its eight nodes; its stated eight connectors and two labelled decision exits match the Mermaid edges. The source screenshots were not in this review scope, so their contents were not independently checked.
* The dispatch summary says vendor.json and claude-plugin are tracked. In this checkout, git status reports vendor.json, both plugin manifests, and both scripts as untracked phase additions. A post-merge data-only contribution can still change the manifest without changing the sync code; the output symlink finding needs a prepared external target and filesystem write capability.
* Static review only. No source or out-of-scope file was modified.

## Verdict

The two former P0 findings were reduced to P1 and P2 after checking their trigger preconditions. The retained P1 findings and the new hub route mismatch require a conditional result.

## Next Dimension

None. This is iteration 5 of 5. Hosted board read-back, the outer validator runtime, and phase closure evidence remain outside this iteration's selected static checks.

Review verdict: CONDITIONAL
