---
title: "product-owner: Manual Testing Playbook"
description: "Operator-facing index for product-owner hub-routing validation across four modes: three workflow packets, one read-only transport, and the artifact-word and negation boundaries."
version: 1.0.0.0
---

# product-owner: Manual Testing Playbook

> **EXECUTION POLICY**: Every scenario runs against the live `product-owner` routing contract, with no mocks or stubs. Scenarios check the hub's actual `workflowMode` decision, its packet-qualified leaves and its boundary behavior. Acceptable verdicts are `PASS`, `FAIL` or `SKIP`, and every `SKIP` names the specific runtime blocker.

This is the hub-level operator directory for four modes: three workflow packets (`sk-product-owner`, `sk-create-figjam` and `mcp-click-up`) and one read-only transport (`mcp-figma`). It checks hub-level mode resolution only. `sk-product-owner/manual-testing-playbook/` owns the artifact behavior tests, and each vendored packet owns its own.

The source of truth for routing is `hub-router.json`, `mode-registry.json` and the root `ROUTER.md` leaf map. The compiled route returns the legacy sentinel for this hub, and a run records that rather than presenting it as compiled-serving evidence.

---

### Result persistence

<!-- MANUAL_PLAYBOOK_RESULT_PERSISTENCE_CONTRACT -->
A scenario run is complete only after its `PASS`, `FAIL` or `SKIP` outcome and reason are persisted into `benchmark/reports/<dated-run-label>/`. Generated report Markdown is renderer-owned and never hand-authored.

---

## 1. OVERVIEW

The hub routes a request to one advisor identity, then resolves a `workflowMode` through the stage one rules. The root `ROUTER.md` maps the request's intent to the exact packet-local leaves. A request no intent matches loads only the two Human Voice cards in `DEFAULT_RESOURCE`, and the packet's own Section 2 routes it from there.

The `hub-routing/` folder holds **7 scenario files**, one per mode, a FigJam diagram type beyond the user flow and the two boundaries most likely to misroute: a tool named inside an artifact request and a negated tool mention. `benchmark/hub-routing-cases.json` carries 41 machine-replayed gold rows beside them.

---

## 2. SCENARIOS

Scored scenarios live as per-file YAML-frontmatter gold under `hub-routing/`.

| ID | File | Expected `workflowMode` |
|----|------|--------------------------|
| MT-001 | [`hub-routing/task-request.md`](hub-routing/task-request.md) | `sk-product-owner` |
| MT-002 | [`hub-routing/flow-command.md`](hub-routing/flow-command.md) | `sk-create-figjam` |
| MT-003 | [`hub-routing/cupt-command-line.md`](hub-routing/cupt-command-line.md) | `mcp-click-up` |
| MT-004 | [`hub-routing/figma-cli-operation.md`](hub-routing/figma-cli-operation.md) | `mcp-figma` |
| MT-005 | [`hub-routing/tool-inside-artifact.md`](hub-routing/tool-inside-artifact.md) | `sk-product-owner` |
| MT-006 | [`hub-routing/negated-signal.md`](hub-routing/negated-signal.md) | `sk-product-owner` |
| MT-007 | [`hub-routing/figjam-diagram-type.md`](hub-routing/figjam-diagram-type.md) | `sk-create-figjam` |

### Ownership boundaries

- **Artifact words win.** A request that asks for a task, bug, Story, PRD, Epic, Doc or clarification stays in `sk-product-owner` even when it names `figma-ds-cli`, `cupt` or FigJam, unless it opens with the tool the way a command line does
- **Bare figma and clickup are no signal.** The Product Owner router reads figma as UI refinement feedback, and clickup is usually a subject
- **A negation reaches back to the start of its clause.** "do not use figma-ds-cli" starts no packet, while "don't worry, figma-ds-cli fj nodes" still routes to `mcp-figma`

---

## 3. SUCCESS CRITERIA

- All 7 scenarios resolve to their expected `workflowMode` and assemble exactly the expected packet-qualified leaves
- No scenario loads a Product Owner mode reference for a tool request, or a tool reference for an artifact request
- `python3 benchmark/gates/check_hub.py`, run from the repository root, replays the 41 gold rows and passes

---

## 4. EVIDENCE AND REPORTING

For each executed scenario, record the prompt, the selected `workflowMode`, the expected and observed leaf pairs, the command output, its exit status and the verdict. Store current runs under a dated `benchmark/reports/<run-label>/` folder.
