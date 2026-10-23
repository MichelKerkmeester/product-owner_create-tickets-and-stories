---
id: MT-007
category: hub_routing
stage: routing
title: "A FigJam sequence diagram routes to sk-create-figjam"
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

# MT-007: A FigJam sequence diagram routes to sk-create-figjam

Prompt: draw the checkout payment as a sequence diagram in FigJam

## Expected Behavior

The request carries no `$` command and no artifact word, and `figjam` is the one packet signal, so stage one starts it in `sk-create-figjam`. The FLOW intent maps it to the Flow pair, and the packet's own Section 2 then adds the sequence reference and template.

## Success Criteria

The router resolves `sk-create-figjam` and loads no Product Owner mode reference.
