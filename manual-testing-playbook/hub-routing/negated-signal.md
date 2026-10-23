---
id: MT-006
category: hub_routing
stage: routing
title: "A negated tool mention starts no packet"
expected_intent: sk-product-owner
expected_resources:
  - sk-product-owner/references/hvr-core.md
  - sk-product-owner/references/conciseness.md
expected_workflow_mode: sk-product-owner
expected_leaf_resources:
  - workflow_mode: sk-product-owner
    leaf_resource_id: references/hvr-core.md
  - workflow_mode: sk-product-owner
    leaf_resource_id: references/conciseness.md
created: 2026-10-20
version: 1.0.0.0
---

# MT-006: A negated tool mention starts no packet

Prompt: do not use figma-ds-cli, the empty state padding is off

## Expected Behavior

The only signal has a negation earlier in its clause, so it starts no packet and the request stays in the default mode. No root `ROUTER.md` intent matches, so only the two Human Voice cards load and the packet's Section 2 scores its semantic topics.

## Success Criteria

The router resolves `sk-product-owner`, never `mcp-figma`, and assembles only the two `DEFAULT_RESOURCE` cards at the hub.
