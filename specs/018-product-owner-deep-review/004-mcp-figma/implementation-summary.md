---
title: "Implementation Summary"
description: "17 review findings, 6 of them P1, with each P1 checked against its cited line."
trigger_phrases:
  - "mcp figma deep review implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "018-product-owner-deep-review/004-mcp-figma"
    last_updated_at: "2026-10-21T13:45:00Z"
    last_updated_by: "claude-code"
    recent_action: "Checked every P1 finding against its cited line"
    next_safe_action: "The operator chooses which findings to fix"
    blockers: []
    key_files:
      - "review/lineages/deepseek/review-report.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
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
| **Spec Folder** | 004-mcp-figma |
| **Status** | Complete |
| **Completed** | 2026-10-21 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

A five-iteration deep review with 17 findings: 0 P0, 6 P1 and 11 P2. The orchestrator opened the cited line of every P1, and 6 of 6 hold.

### P1 findings, checked

| ID | Finding | Cited line | Verdict | What the line shows |
|----|---------|------------|---------|---------------------|
| R1-P1-001 | tool-surface.md inverts the truth about the primitive verbs: declares them top-level aliases and calls the real create-subcommand form drift | `mcp-figma/references/tool-surface.md:98` | Holds | tool-surface.md:98 calls rect, ellipse and the rest top-level aliases and the create form drift. figma-ds-cli 1.2.0 lists only create, create --help lists rect, and figma-ds-cli rect prints the top-level usage. Fix upstream |
| R1-P1-002 | _common.sh resolves figma-cli without the silships identity check SKILL.md makes mandatory | `mcp-figma/scripts/_common.sh:21` | Holds | _common.sh:21 picks figma-cli with no check that it is the silships build, which mcp-figma/SKILL.md:72 says to verify. Fix upstream |
| R1-P1-003 | connect-safe.sh exits 0 after doing nothing whenever stdin is not a TTY | `mcp-figma/scripts/connect-safe.sh:20` | Holds | connect-safe.sh:20 prints an info line and exits 0 on a non-TTY stdin, so an automated caller reads success when nothing connected. Fix upstream |
| R1-P1-004 | doctor.sh resolves .utcp_config.json one level above the repo root once vendored, so the optional-MCP check false-negatives | `mcp-figma/scripts/doctor.sh:48` | Holds | doctor.sh:48 uses the same five-level walk as the ClickUp doctor and misses .utcp_config.json in the vendored position. Fix upstream |
| R2-P1-001 | README and INSTALL-GUIDE invoke extract with a --out flag the binary does not define, at a fixed path the packet's own no-overwrite rule forbids | `mcp-figma/README.md:86` | Holds | README.md:86 runs extract --out DESIGN.md, and figma-ds-cli extract --help takes a positional output and has no --out. Fix upstream |
| R3-P1-001 | seven cross-references resolve only at the upstream nesting depth, so they are dangling in the position the packet ships in | `mcp-figma/references/mcp-wiring.md:41` | Holds | references/mcp-wiring.md:41 links ../../../mcp-code-mode/SKILL.md, which does not exist from the vendored position. Fix upstream, or accept it as a vendoring limit |

### P2 findings, unchecked

| ID | Finding | Cited line |
|----|---------|------------|
| R1-P2-001 | install.sh --verbose test can never be false, so the quiet branch is dead | `mcp-figma/scripts/install.sh:95` |
| R1-P2-002 | INSTALL-GUIDE version metadata trails the packet at 1.0.0.0 while SKILL.md and README declare 1.1.3.0 | `mcp-figma/INSTALL-GUIDE.md:4` |
| R1-P2-003 | vendor-sync.py can write a null base_commit and then report in step at None | `scripts/vendor-sync.py:135` |
| R2-P2-001 | nothing the packet executes is pinned or integrity-checked: install.sh clones the default branch and runs npm install -g, the MCP manual uses figma-developer-mcp@latest | `mcp-figma/scripts/install.sh:102` |
| R2-P2-002 | the optional MCP path pipes arbitrary Figma-authored text into the model with no untrusted-content instruction | `mcp-figma/references/mcp-wiring.md:29` |
| R3-P2-001 | playbook index pins the skill at 1.0.0.0 while the packet declares 1.1.3.0 | `mcp-figma/manual-testing-playbook/manual-testing-playbook.md:9` |
| R3-P2-002 | two of the playbook's three pointers to its own scenario cross-reference index name Section 12 instead of Section 13 | `mcp-figma/manual-testing-playbook/manual-testing-playbook.md:35` |
| R3-P2-003 | INSTALL-GUIDE describes extract output as 9 sections while the reference and catalog say 11 | `mcp-figma/INSTALL-GUIDE.md:268` |
| R4-P2-001 | the Code Mode manual entry is copied in five places and the copies have already diverged on the version pin | `mcp-figma/assets/utcp-figma-manual.md:53` |
| R4-P2-002 | the daemon PID constant re-introduces the figma-cli name collision the packet warns about, and doctor reports its contents unvalidated | `mcp-figma/scripts/_common.sh:49` |
| R4-P2-003 | the official Dev Mode MCP out-of-scope sentence reads repo-wide while sk-create-figjam ships that route as its primary one | `mcp-figma/references/mcp-wiring.md:154` |

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| review/ | Created | The lineage, the merged registry and the review report |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The run was staged in the outer repository with a scope spec and a steer file, the copy kept here as `review/staging-scope.md`, and ran in parallel with the other four reviews. `fanout-run.cjs --loop-type review` ran one DeepSeek V4.1 Flash max lineage of 5 iterations through cli-pi and llmgateway, with the stop policy at max-iterations and convergence off, and `fanout-merge.cjs` merged it. The review folder was copied here without the runner's containment snapshots and with its containment log lines removed, since both list files from the private outer tree. Nothing is committed.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Check every P1, list every P2 unchecked | A reviewer's severity is a claim until its cited line is read, and the P1s are the ones that would change what the operator fixes first |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| State log, `grep -c '"type":"iteration"' review/lineages/deepseek/deep-review-state.jsonl` | 5 iteration records, stopReason maxIterationsReached, every record routed to deep-review, fanout exit 0 |
| Citations, `python3` over `review/lineages/deepseek/deep-review-findings-registry.json` testing each file exists | All 17 findings carry a file and line, and every cited file exists |
| P1 verdicts, `sed -n` on each cited line | 6 of 6 hold on the cited line |
| Write containment, `find` for files newer than the launch outside the lineage | No file changed outside the lineage during the run |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **The P2 findings are unchecked.** They are the reviewer's claims until a fix opens each line.
2. **Nothing is fixed.** The findings wait for the operator's choice.
3. **Fixes go upstream.** The packet is vendored and hashed in vendor.json, so a fix lands in the shared skill and comes back through scripts/vendor-sync.py pull.
<!-- /ANCHOR:limitations -->
