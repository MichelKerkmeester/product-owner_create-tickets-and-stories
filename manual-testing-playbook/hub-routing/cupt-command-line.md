---
id: MT-003
category: hub_routing
stage: routing
title: "A cupt command line routes to mcp-click-up"
expected_intent: mcp-click-up
expected_resources:
  - mcp-click-up/references/cupt-commands.md
  - mcp-click-up/references/mcp-tools.md
expected_workflow_mode: mcp-click-up
expected_leaf_resources:
  - workflow_mode: mcp-click-up
    leaf_resource_id: references/cupt-commands.md
  - workflow_mode: mcp-click-up
    leaf_resource_id: references/mcp-tools.md
created: 2026-10-20
version: 1.0.0.0
---

# MT-003: A cupt command line routes to mcp-click-up

Prompt: cupt list my open tasks

## Expected Behavior

The request opens with `cupt`, a keyword of the `clickup-aliases` class, so the opener rule starts it in `mcp-click-up` although it names tasks.

## Success Criteria

The router resolves `mcp-click-up` and does not fall back to the default packet because of the word tasks.
