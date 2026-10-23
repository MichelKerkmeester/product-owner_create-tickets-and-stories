---
title: "Implementation Summary"
description: "Product Owner is now a parent hub: a root SKILL.md picks the Product Owner packet or the vendored figma packet, and the prose router moved into ROUTER.md with every gate held to its baseline."
trigger_phrases:
  - "parent hub conversion implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/004-parent-hub-conversion"
    last_updated_at: "2026-10-20T07:10:00Z"
    last_updated_by: "claude-code"
    recent_action: "Applied the hub conversion as one patch and closed the phase"
    next_safe_action: "Start 005-flow-mode; its board criteria wait on the hosted Figma MCP"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "scaffold-004-parent-hub-conversion"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.2 -->
# Implementation Summary

<!-- SPECKIT_LEVEL: 2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 004-parent-hub-conversion |
| **Completed** | 2026-10-20 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Product Owner is now a parent hub on the Moneybird Accountant pattern. A request reads the root `SKILL.md` first, which picks the Product Owner packet by default or the vendored `mcp-figma/` packet for a request that names only a figma tool operation. Existing requests route exactly as before: the router fixtures and the differential hold their counts.

### Phase 4: parent-hub-conversion

The prose router left `sk-product-owner/SKILL.md` Section 2 for `sk-product-owner/ROUTER.md`, and a one-line pointer stays behind, so every "SKILL.md Section 2" pointer still lands. `benchmark/gates/check_hub.py` holds the hub together: it checks the hub files, the registry, each router and its pointer, exempts the vendored packet only when `vendor.json` lists it, and replays 11 stage one gold rows. Both format validators now lint the hub `SKILL.md` and `ROUTER.md`.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| SKILL.md, mode-registry.json, hub-router.json | Created | Hub stage one: packets, default, signals, artifact and negation words |
| sk-product-owner/ROUTER.md | Created | The prose router moved out of SKILL.md |
| sk-product-owner/SKILL.md | Modified | Section 2 becomes a pointer, stale router mentions repointed |
| AGENTS.md | Modified | Read order hub first, then the packet the hub picks, and the DAG |
| benchmark/gates/check_hub.py, run_gates.sh | Created, Modified | Hub gate and its self-test in the runner |
| benchmark/router/differential.py | Modified | Reads the topic table and contract pointer from ROUTER.md |
| benchmark/format/validate-output-format.cjs | Modified | Lints the hub SKILL.md and ROUTER.md |
| z — Claude Project Sync Loop/systems.cjs, validate-output-format.cjs | Modified | The same perimeter through an `extraSources` entry, `[]` for other systems |
| 23 playbook files, router-contract.md, READMEs, SYNC.md, leaf-manifest.config.json | Modified | Citations remapped, routing mentions repointed, gate counts, a maintenance record |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The baseline was captured first, then `scratch/convert.py` and `scratch/fixes.py` built the change in a scratch systems tree that also held the three other format-gated systems and the Sync Loop folder. All gates ran there, then the scratch was applied to the live trees as `scratch/hub.patch` (40 files) and `scratch/sync-loop.patch` (4 files). A fresh Sonnet reviewer read the first patch and found no P0 and three P1. The live patch was reversed, both scripts were corrected, and the result was applied again as one patch, so the live tree only ever took a single change. Nothing is committed.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| The token allowance is the hub SKILL.md plus 286 tokens | The Moneybird shape costs a router head, a pointer and a read order. The operator amended the criterion on 2026-10-20 after the structural cuts brought the overhead from 432 to 286 |
| `interactive-mode.md` keeps its "SKILL.md Section 2" pointers | It is a Sync Loop pair source whose mirror carries an adapted Section 2 wording, and the SKILL.md pointer still forwards to ROUTER.md |
| A `$` command or an artifact word keeps a tool mention in Product Owner | The review showed `$d figma-ds-cli fj nodes` and "write a PRD for the figma-ds-cli rollout" otherwise reached the tool packet |
| The shared validator gained `extraSources` rather than a Product Owner special case | Other systems resolve it to `[]`, so their perimeters and fixtures stay unchanged |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| Router fixtures | PASS, 117/117 and 189/189 differential, same as baseline |
| Format fixtures | PASS, Product Owner 59 cases, Sales, Deal Templates and Copywriter 155 PASS lines each, same as baseline |
| check_hub.py and --self-test | PASS, 2 packets and 11 gold rows. Each of 5 planted defects fails with its own message |
| Default Task read set, o200k | 26,358 to 27,685: a rise of 1,327 against an allowance of 1,049 + 286 = 1,335 |
| reference-parity.cjs | PASS, identical in all three modes, perimeter 40 to 42 source files |
| run_gates.sh | PASS, all 9 gates, exit 0 |
| run_parity.sh, run_residency.sh | PASS, 37/37 pairs, exit 0, and residency exit 0 |
| Planted em dash in the hub SKILL.md and in ROUTER.md | Both validators exit 1 naming the file |
| Fresh review | No P0. Three P1 and the P2 set fixed, see the goal log |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **The router contract's ALWAYS list still names only `sk-product-owner/SKILL.md`.** Its Python is held equal to the kernel's Router Code by copy parity, so adding the hub there is a kernel change for phase 007.
2. **run_receipts.sh exits 1.** SYNC.md has carried no dated upload receipt since before this phase. That needs a real upload by the operator.
3. **Versions are unchanged.** The skill version and changelog move in the release step, phase 008.
<!-- /ANCHOR:limitations -->
