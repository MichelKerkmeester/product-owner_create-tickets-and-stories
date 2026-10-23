---
id: MT-001
category: hub_routing
stage: routing
title: "A task request routes to sk-product-owner"
expected_intent: sk-product-owner
expected_resources:
  - sk-product-owner/references/task-mode.md
  - sk-product-owner/assets/task-templates.md
expected_workflow_mode: sk-product-owner
expected_leaf_resources:
  - workflow_mode: sk-product-owner
    leaf_resource_id: references/task-mode.md
  - workflow_mode: sk-product-owner
    leaf_resource_id: assets/task-templates.md
created: 2026-10-20
version: 1.0.0.0
---

# MT-001: A task request routes to sk-product-owner

Prompt: write a task for the onboarding checklist, step two is skipped for new creators

## Expected Behavior

The artifact word task is a keyword of the default mode's `product-owner-artifacts` class, so stage one keeps the request in `sk-product-owner`, and the root `ROUTER.md` TASK intent maps it to the Task pair.

## Success Criteria

The router resolves `sk-product-owner` and assembles exactly the Task pair beside the two Human Voice cards.
