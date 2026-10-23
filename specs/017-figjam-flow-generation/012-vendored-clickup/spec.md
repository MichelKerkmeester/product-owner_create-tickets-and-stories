---
title: "Feature Specification: Phase 12: Vendored ClickUp packet"
description: "Product Owner writes ClickUp artifacts but carries no ClickUp skill. This phase vendors mcp-click-up into the hub as a byte copy kept in step with .skilled by vendor-sync.py, the same way mcp-figma is."
trigger_phrases:
  - "vendored clickup"
  - "mcp-click-up vendored"
  - "phase 12 vendored clickup"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 12: Vendored ClickUp packet

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-20 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 12 of 12 |
| **Predecessor** | 011-figjam-packet-split |
| **Successor** | 013-skilled-hub-alignment |
| **Handoff Criteria** | vendor-sync.py status reports both packages in step, the hub check and run_gates.sh pass |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 12** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: A byte copy of `.skilled/skills/mcp-tooling/mcp-click-up` at `mcp-click-up/`, its manifest entry, its hub registration and the docs that count the packets.

**Dependencies**:
- The vendor sync from phase 003, which already handles whole-folder packages.
- The operator chose on 2026-10-20: a real copy, not a symlink, under the upstream folder name `mcp-click-up`, kept in step like `mcp-figma`.

**Deliverables**:
- `mcp-click-up/` and its `vendor.json` entry.
- The hub registry, stage one signals and gold rows for it.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Product Owner writes ClickUp tasks and docs, but the ClickUp skill lives only in `.skilled`. A Product Owner clone, or the plugin, has no ClickUp contract with it, and a symlink would point at a path a clone does not have.

### Purpose
Vendor the ClickUp skill as a byte copy that `vendor-sync.py status`, `pull` and `push` keep in step with `.skilled`.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- `vendor.json` entry `mcp-click-up`, then `vendor-sync.py pull`.
- `mode-registry.json` tool row marked vendored, `hub-router.json` signals, hub `SKILL.md` row and rule.
- `check_hub.py` gold rows for the signals, a negation and a ClickUp word inside an artifact request.
- `build-plugin.py` ships the packet. READMEs, AGENTS.md and SYNC.md name it.

### Out of Scope
- Any edit inside `mcp-click-up/`. It is upstream-owned, so a change goes through `push`.
- A Claude Project mirror. A Project reaches ClickUp through its own connector.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| mcp-click-up/ | Create | Byte copy of the upstream skill |
| vendor.json | Modify | The package entry and its file hashes |
| SKILL.md, mode-registry.json, hub-router.json | Modify | Fourth packet and its signals |
| benchmark/gates/check_hub.py | Modify | Gold rows |
| scripts/build-plugin.py, claude-plugin/ | Modify | Packet shipped |
| README.md, AGENTS.md, SYNC.md | Modify | Layout and counts |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | `mcp-click-up/` matches upstream byte for byte and holds no symlink. |
| REQ-002 | `vendor-sync.py status` reports both whole-folder packages and the extractor in step. |
| REQ-003 | The hub sends a request that names only `mcp-click-up`, `cupt` or `clickup mcp` to the packet, and keeps an artifact request with Product Owner. |
| REQ-004 | run_gates.sh and the hub check self-test pass. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-005 | The plugin ships the packet and the docs count four packets. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: An upstream ClickUp fix reaches Product Owner with one `pull`.
- **SC-002**: "write a task for the ClickUp import" still routes to Task Mode.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | Private data enters the public repo | High | The upstream is already a public GitHub repo, and a scan found no token or workspace id |
| Risk | Bare "clickup" captures Product Owner requests | Med | Bare "clickup" is no signal, because Product Owner writes ClickUp-native docs |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Reliability
- **NFR-R01**: The copy fails `status` the moment either side changes.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- "don't use cupt, the export drops rows" routes to Product Owner, because the negation reaches the signal.
- A request naming both `cupt` and `figma-ds-cli` names two tool packets and stays with the default.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 8/25 | One copied folder and its registration |
| Risk | 6/25 | The sync path is proven on mcp-figma |
| Research | 2/20 | None |
| **Total** | **16/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator chose the folder name and a real copy on 2026-10-20.
<!-- /ANCHOR:questions -->
