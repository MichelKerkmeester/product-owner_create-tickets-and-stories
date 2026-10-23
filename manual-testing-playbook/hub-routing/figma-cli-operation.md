---
id: MT-004
category: hub_routing
stage: routing
title: "A figma-ds-cli operation routes to mcp-figma"
expected_intent: mcp-figma
expected_resources:
  - mcp-figma/references/figma-cli-reference.md
  - mcp-figma/references/mcp-wiring.md
expected_workflow_mode: mcp-figma
expected_leaf_resources:
  - workflow_mode: mcp-figma
    leaf_resource_id: references/figma-cli-reference.md
  - workflow_mode: mcp-figma
    leaf_resource_id: references/mcp-wiring.md
created: 2026-10-20
version: 1.0.0.0
---

# MT-004: A figma-ds-cli operation routes to mcp-figma

Prompt: figma-ds-cli fj nodes

## Expected Behavior

The request opens with `figma-ds-cli`, a keyword of the `figma-aliases` class, so stage one starts it in the `mcp-figma` transport.

## Success Criteria

The router resolves `mcp-figma`, whose tool surface stays read-only in this workspace.
