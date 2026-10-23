---
id: MT-002
category: hub_routing
stage: routing
title: "The Flow command routes to sk-create-figjam"
expected_intent: sk-create-figjam
expected_resources:
  - sk-create-figjam/references/flow-mode.md
  - sk-create-figjam/assets/flow-templates.md
expected_workflow_mode: sk-create-figjam
expected_leaf_resources:
  - workflow_mode: sk-create-figjam
    leaf_resource_id: references/flow-mode.md
  - workflow_mode: sk-create-figjam
    leaf_resource_id: assets/flow-templates.md
created: 2026-10-20
version: 1.0.0.0
---

# MT-002: The Flow command routes to sk-create-figjam

Prompt: $flow the location change from these screenshots

## Expected Behavior

`$flow` is the only `$` command and it belongs to `routerPolicy.packetCommands` for `sk-create-figjam`, so stage one starts the request there, and the FLOW intent maps it to the Flow pair.

## Success Criteria

The router resolves `sk-create-figjam` and loads no Product Owner mode reference.
