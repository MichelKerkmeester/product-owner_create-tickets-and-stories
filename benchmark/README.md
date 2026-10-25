---
title: "product-owner Hub Routing Benchmark"
description: "The hub routing baseline for product-owner: the stage one gold rows and the gate that replays them."
trigger_phrases:
  - "product-owner benchmark"
  - "hub routing gold rows"
  - "hub routing baseline"
version: 1.0.0.0
---

# product-owner Hub Routing Benchmark

## 1. OVERVIEW

This folder is the hub's routing baseline. [`hub-routing-cases.json`](hub-routing-cases.json) holds 51 gold rows, the requests most likely to be misrouted when packets sit beside the default one: a bare request, the existing figma Task fixture, requests that name only one tool or the Flow commands, FigJam requests for every diagram type with one in plain words, board links and notes on a board, tickets and bugs about a FigJam board, negated mentions, a command conflict, and tool mentions inside an artifact request or beside another `$` command. Each row names the `workflowMode` stage one must pick.

The system gates beside this file own the packet's own routing. `router/` replays the Product Owner router against its fixtures and the kernel copy, so stage two inside a packet is never scored here. The two vendored packets' own intents are left to their upstream tests, and this folder only proves which packet each request reaches and which leaves the hub lane loads.

---

## 2. HOW TO RUN

```bash
python3 benchmark/gates/check_hub.py
python3 benchmark/gates/check_hub.py --self-test
```

Run both from the repository root. The first replays every row against `../hub-router.json` and checks that the hub files, the registry, the root `ROUTER.md` and the packets agree. The second plants one defect per rule in a scratch copy and requires each to fail. `gates/run_gates.sh` runs both among the system gates.

---

## 3. STRUCTURE

| Path | Purpose |
|---|---|
| [`hub-routing-cases.json`](hub-routing-cases.json) | The gold rows: label, request and expected `workflowMode` |
| `README.md` | This index |
| `fixtures/companies/` | The three fictional company folders the manual testing playbook attaches: Fernhouse, Loomlist and Roamstay |
| [`format/`](format/README.md) | The output format validator and its fixture runner |
| [`gates/`](gates/README.md) | Rule parity, example lint, the hub and leaf map checks, the Markdown link check and `run_gates.sh` |
| [`grader/`](grader/README.md) | The reply linter and twin comparison over a finished playbook report |
| [`parity/`](parity/README.md) | The wrappers into the shared Sync Loop parity gate |
| `reports/` | The dated run folders |
| [`router/`](router/README.md) | The executable route contract, its fixtures and the differential gate |

A dated run that records more than a pass belongs in a `reports/<run-label>/` folder beside these files.
