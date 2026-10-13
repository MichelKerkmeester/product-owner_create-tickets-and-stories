---
title: "Spec: Product Owner ClickUp Handoff"
description: "Consent-gated ClickUp delivery for Product Owner artifacts with markdown-preserving transport."
trigger_phrases:
  - "clickup handoff"
  - "clickup consent gate"
  - "clickup markdown transport"
  - "markdown_description"
importance_tier: "high"
contextType: "specification"
_memory:
  continuity:
    packet_pointer: "002-product-owner-mode-additions/003-product-owner-clickup-handoff"
    last_updated_at: "2026-07-15T12:16:28Z"
    last_updated_by: "claude"
    recent_action: "Implemented and verified the consent gate and markdown transport contract"
    next_safe_action: "Re-upload the synchronized Claude package and re-run the live smoke matrix when deployment access is available"
---
<!-- SPECKIT_LEVEL: 1 -->
# Spec: Product Owner ClickUp Handoff

## 1. INCIDENT & PURPOSE

An AI session running the Product Owner system with ClickUp tooling created workspace tickets DEV-3354 and DEV-3355 without being asked, and both rendered as raw markdown (literal `### About`, `**Checklist**`, `- [ ]` in the description). Two root causes:

1. The Product Owner package had no ClickUp handoff rule at all — every ClickUp mention was the markdown grammar contract for document bodies, so a runtime with ClickUp tools had nothing telling it to ask first.
2. The `mcp-tooling` ClickUp packet documented task creation with only a plain `description` parameter. ClickUp stores that field literally; the markdown-aware parameters (`markdown_description` on create, `markdown_content` on update, `content` + `content_format` markdown for documents/pages) were documented only for documents — the fix from an earlier live document session had never been generalized to tasks.

By the time of this packet's live check, the two broken tickets had already been replaced with clean content, so no in-place repair was needed.

## 2. REQUIREMENTS

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | Consent gate on every ClickUp write. | Whenever the runtime exposes ClickUp tooling, the Product Owner export response offers ClickUp delivery and waits; no create, update or delete happens without explicit user approval in the current conversation. The file export itself never waits for permission. |
| REQ-002 | Markdown-preserving transport. | Approved pushes send markdown through `markdown_description` (task create), `markdown_content` (task update) or `content` + markdown `content_format` (documents/pages), never the plain `description` field. |
| REQ-003 | Product Owner references the ClickUp skill. | The Product Owner package names the `mcp-tooling` ClickUp packet as the owner of transport mechanics rather than duplicating tool syntax. |
| REQ-004 | ClickUp skill documents the contract. | The `mcp-click-up` packet carries the markdown transport contract in its SKILL rules, tool reference and the create/update task catalog entries, with live-verification evidence. |
| REQ-005 | Package parity and sync. | The rule appears in SKILL.md, AGENTS.md, doc_mode.md, Custom Instructions, the user guide and the SYNC required-parity list; mirrors stay byte-identical and all checksums are rebuilt. |

## 3. LIVE VERIFICATION EVIDENCE (2026-07-15)

Executed against the Barter workspace (team 90151466006, Task Tracker list 901519108524) with the operator's own `cupt` token after the claude.ai ClickUp connector disconnected mid-session:

- Scratch task created with `markdown_description` (headings, bold, checklist): fetched back, plain description showed converted text with no literal markup; `markdown_description` round-tripped intact; task deleted.
- Second scratch task: `PUT /task` accepted BOTH `markdown_content` and `markdown_description`, each rendering correctly; task deleted.
- DEV-3354 / DEV-3355 fetched: current descriptions are clean replacements (no raw markdown), so in-place repair was unnecessary.
