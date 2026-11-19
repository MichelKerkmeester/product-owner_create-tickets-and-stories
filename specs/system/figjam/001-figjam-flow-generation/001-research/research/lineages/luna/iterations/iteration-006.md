# Iteration 6: Moneybird’s parent hub structure

## Focus
Map Moneybird Accountant’s two-stage packet routing to Product Owner’s current single-mode package.

## Actions Taken
- Read the Moneybird bootstrap, root hub skill, hub-router.json, mode-registry.json, and route checker.
- Compared the hub’s packet roles with Product Owner’s current router and single-mode manifest configuration.
- Traced the appropriate boundary for a FigJam workflow that handles mixed source inputs but uses mcp-figma for board operations.

## Findings
1. Moneybird separates packet selection from packet behavior: root SKILL.md is stage one, mode-registry.json maps each packet folder, skill name, kind, and router, hub-router.json supplies the default and stage-one signals, and each packet’s ROUTER.md and SKILL.md own stage two and its contract. [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:10] [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:30] [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:44] [SOURCE: AI Systems/Moneybird Accountant/mode-registry.json:4] [SOURCE: AI Systems/Moneybird Accountant/hub-router.json:2] [SOURCE: AI Systems/Moneybird Accountant/hub-router.json:8]
2. The current Moneybird checker encodes one default workflow packet and classifies every non-default packet as a tool packet; it also verifies packet names, routers, default agreement, and that hub signals name the registry modes. [SOURCE: AI Systems/Moneybird Accountant/mode-registry.json:5] [SOURCE: AI Systems/Moneybird Accountant/mode-registry.json:13] [SOURCE: AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/check-route-table.py:201] [SOURCE: AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/check-route-table.py:903] [SOURCE: AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/check-route-table.py:944] [SOURCE: AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/check-route-table.py:947]
3. The cleanest fit is to keep Product Owner’s existing backlog and documentation workflow as the default workflow packet and model embedded mcp-figma as a tool packet; mixed screenshot, Figma, or product-document requests remain Product Owner work, which classifies sources and governs the FigJam-only result before handing board operations to the tool packet. [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:44] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:54] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:64] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:67] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:79] [INFERENCE: the FigJam tool packet should own board calls while Product Owner retains input classification and final-output policy]
4. Product Owner is explicitly a standalone single-mode skill today, with one workflowMode and references/assets/playbook roots; parent-hub conversion therefore needs a root hub contract plus the two hub JSON files and a bootstrap load-order change, while retaining the existing skill as the default packet instead of trying to make its current manifest behave like a registry. [SOURCE: AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:2] [SOURCE: AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:4] [SOURCE: AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:11] [SOURCE: AI Systems/Moneybird Accountant/AGENTS.md:36] [SOURCE: AI Systems/Moneybird Accountant/AGENTS.md:42] [SOURCE: AI Systems/Moneybird Accountant/AGENTS.md:44]
5. A FigJam flow-generation experience is more than a CLI packet: Moneybird’s hub makes its default accountant packet own real workflow rules and only hands off concrete Moneybird or Jortt operations, so Product Owner should keep source authority, conflict resolution, diagram quality, and FigJam-only delivery in its workflow packet and hand off only named board operations to mcp-figma. [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:32] [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:34] [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:55] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:73] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:79] [INFERENCE: workflow policy belongs in the default product workflow rather than the low-level CLI packet]

## Questions Answered
- How does Moneybird’s parent hub divide stage-one packet selection from packet-level routing, and what maps cleanly to Product Owner?

## Questions Remaining
- Which routing mistakes did Moneybird’s reviews uncover, and which of its controls should Product Owner adopt?
- Which combined architecture risks should sequence the build phases?

## Next Focus
Use Moneybird’s hub-review findings and gold-route cases to identify concrete misrouting failures and derive Product Owner-specific guards.

## Sources Consulted
- AI Systems/Moneybird Accountant/AGENTS.md:36-50
- AI Systems/Moneybird Accountant/SKILL.md:8-55
- AI Systems/Moneybird Accountant/hub-router.json:1-13
- AI Systems/Moneybird Accountant/mode-registry.json:1-30
- AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/check-route-table.py:201,868-952
- AI Systems/Moneybird Accountant/sk-moneybird-accountant/feature-catalog/reference-and-state/hub-and-packet-routers.md:32-57
- AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:1-11
- AI Systems/Product Owner/sk-product-owner/SKILL.md:42-74
- AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:64-84
