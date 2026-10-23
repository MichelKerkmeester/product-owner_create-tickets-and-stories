---
id: MT-005
category: hub_routing
stage: routing
title: "A tool named inside a document request stays with sk-product-owner"
expected_intent: sk-product-owner
expected_resources:
  - sk-product-owner/references/doc-mode.md
  - sk-product-owner/assets/doc-templates.md
expected_workflow_mode: sk-product-owner
expected_leaf_resources:
  - workflow_mode: sk-product-owner
    leaf_resource_id: references/doc-mode.md
  - workflow_mode: sk-product-owner
    leaf_resource_id: assets/doc-templates.md
created: 2026-10-20
version: 1.0.0.0
---

# MT-005: A tool named inside a document request stays with sk-product-owner

Prompt: document how figma-ds-cli handles auth

## Expected Behavior

The request names `figma-ds-cli` but does not open with it, and it asks for a document, so the artifact rule keeps it in `sk-product-owner` and the DOC intent maps it to the Doc pair.

## Success Criteria

The router resolves `sk-product-owner`, and the Doc source gate in the packet still runs before any draft.
