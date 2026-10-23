# Iteration 11: What a parent hub is, in files

## Focus

Read the Moneybird Accountant hub files to establish the structural minimum of a parent hub, so the Product Owner conversion can be described as concrete edits instead of an aspiration. This opens the hub precedent, one of the two the topic names.

## Findings

1. A parent hub is two small registries: `hub-router.json` carries a version, `routerPolicy` with `defaultMode`, `handoff` and `fallback`, plus per-mode keyword signals, and `mode-registry.json` carries the hub name and one row per mode with `workflowMode`, `packet`, `packetSkillName`, `packetKind` (workflow or tool), `router` and `default`. [SOURCE: AI Systems/Moneybird Accountant/hub-router.json:1] [SOURCE: AI Systems/Moneybird Accountant/mode-registry.json:1]
2. The hub's own `SKILL.md` is a packet picker, not a capability: it states that the repository root is a parent hub over three packets, that this file picks the packet, that the packet's `ROUTER.md` routes inside it, and that the packet's `SKILL.md` holds the contract. [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:10]
3. Routing is explicitly two-stage and bounded: stage one picks the packet from the registry and signals, stage two is the packet's own router, so a request reads only the routing of the packets it actually uses. [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:30]
4. The default mode is the workflow packet, and a request starts there unless it names a CLI operation; a strictly CLI-named request starts in the named tool packet, and a CLI name matches whole words only. [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:32]
5. A hub ships its own consistency checkers: `check-route-table.py` proves the hub files, the registry packets and their routers agree and that no packet `SKILL.md` embeds a router again, while `route-replay.py` scores packet chains against the routing rules. [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:38]
6. Each packet under the hub is itself a full package with its own `ROUTER.md`, `SKILL.md`, `graph-metadata.json`, leaf manifests, changelog, benchmark and playbook, so hub conversion composes packages rather than flattening them. [SOURCE: AI Systems/Moneybird Accountant/cli-moneybird/ROUTER.md:1]

## Ruled Out

- Treating "parent hub" as a large single skill. The hub is a router plus independent packets, and the packet boundary is the unit of loading.
- Making a tool packet the default. The registry defaults to the workflow packet so a bare request cannot fall into a CLI execution.

## Dead Ends

- Looking for a hub-level mode reference file. The hub has no mode docs of its own; all stage-two routing lives in packets.

## Edge Cases

- Ambiguous input: "parent hub" could mean the registry files or the routing behavior. Selected both, since they are one mechanism.
- Contradictory evidence: none.
- Missing dependencies: the two checker scripts were not run, so their enforcement is documented rather than observed.
- Partial success: none.

## Sources Consulted

- `AI Systems/Moneybird Accountant/hub-router.json:1-12`
- `AI Systems/Moneybird Accountant/mode-registry.json:1-30`
- `AI Systems/Moneybird Accountant/SKILL.md:10,30,32,38`
- `AI Systems/Moneybird Accountant/cli-moneybird/ROUTER.md:1-20`

## Assessment

- New information ratio: 1.0
- Questions addressed: what a parent hub is structurally.
- Questions answered: none fully; the hub anatomy is answered, the conversion of Product Owner and the hub's own mistakes remain.

## Reflection

- What worked and why: reading the 13-line router before the 291-line Product Owner bootstrap made the hub's minimality obvious, which reframes the conversion as a small registry plus packaging, not a rewrite.
- What did not work and why: expecting a hub-level mode reference wasted a step; the hub intentionally owns no modes.
- What I would do differently: read the hub's SKILL.md routing section immediately after the JSON, since it explains why the JSON has so few fields.

## Recommended Next Focus

Iteration 12: read the Moneybird hub's spec and changelog record for what the conversion cost and what broke, so the Product Owner hub plan inherits the corrections the way iteration 10 did for the plugin.
