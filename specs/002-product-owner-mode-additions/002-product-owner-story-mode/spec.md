---
title: "Spec: Product Owner Story Mode"
description: "Story Mode for the Product Owner system: research-grounded story formats, a three-tier template family, and a routed STORY intent with interactive tier intelligence across both packagings."
trigger_phrases:
  - "product owner story mode"
  - "story mode routing"
  - "story templates"
  - "user story examples"
importance_tier: "high"
contextType: "specification"
_memory:
  continuity:
    packet_pointer: "002-product-owner-mode-additions/002-product-owner-story-mode"
    last_updated_at: "2026-07-15T16:52:12Z"
    last_updated_by: "claude"
    recent_action: "Implemented Story Mode across the Product Owner skill and Claude packagings with routing, tier intelligence, and a rebuilt thirteen-mirror manifest"
    next_safe_action: "Upload the synchronized thirteen-mirror Claude package when deployment access is available"
---
<!-- SPECKIT_LEVEL: 1 -->
# Spec: Product Owner Story Mode

## 0. FEATURE SUMMARY (grown from the research packet below)

This packet began as story-format research and grew, by operator direction, into the full Story Mode feature:

1. **Research** (sections below): cited story-format evidence and example files, produced by a GLM-5.2 dispatch.
2. **House format**: the Fv2.5 Feed Function Rulesets story rewritten with light conventional elements (Connextra Story lines, Given/When/Then scenario bullets, DoR/DoD gates) after a full ticket-block restructure was rejected in review; generalized into a three-tier template family (Simple / Medium / Complex) plus a chooser, hardened by a GPT-5.6-Sol review triage.
3. **Story Mode**: a fifth artifact intent in the Product Owner system. `$story`/`$s` commands with token-boundary rules, story framing and tie-breaks ("create a task to write a story" stays Task), semantic scoring, a story intake gate with tier inference in Interactive Mode, a `story_mode.md` reference (v0.100) and `story_templates.md` asset (v0.100), and parity across AGENTS.md, the Claude kernel (v0.3.0, aligned with Skill v0.4.0), both READMEs and SYNC.md. Versions bumped for the new feature: Skill 0.4.0, Interactive Mode 0.404, Interactive Response Templates 0.102; the mirror set grew to thirteen files with a fourteen-row checksum manifest.

## Original research spec: User Story Examples Research

## 1. PROBLEM & PURPOSE

The Product Owner system writes tasks, bugs, and documents, and one retained export (`022 - story-chat.md`) shows story-shaped work already arriving. There is no curated reference for how the industry actually formats user stories and project-management stories that developers turn into tickets. This packet collects that reference material from public online sources so future Product Owner work (for example a dedicated story capability) starts from evidence rather than memory.

## 2. SCOPE

### In Scope

- Online research of user-story and PM-story formats used to derive development tickets: the Connextra "As a / I want / so that" form, job stories, Gherkin-style acceptance criteria, INVEST, story splitting, epic-to-story breakdown, and real ticket anatomy from mainstream trackers.
- A cited `research.md` summarizing findings and sources.
- Three to five self-contained example/template markdown files under `examples/`, each grounded in the researched sources.

### Out of Scope

- Any change to the Barter `Product Owner/` package, its skill, kernel, mirrors, or checksums.
- Choosing or approving a future Product Owner story mode; this packet only gathers evidence.
- Copying long verbatim passages from sources; findings are synthesized with short attributed quotes only.

## 3. REQUIREMENTS

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | Research real, reachable online sources. | Every cited URL was actually fetched during the run; unreachable or paywalled sources are marked as such; no fabricated links. |
| REQ-002 | Produce a cited research summary. | `research.md` records the story formats found, where each comes from, and how tickets are typically derived from stories. |
| REQ-003 | Produce ticket-ready example files. | Three to five markdown files in `examples/`, each self-contained with frontmatter, at least one filled example per format, and its sources listed. |
| REQ-004 | Follow repository documentation style. | Files use markdown tables only at two columns or fewer; wider data becomes lists. |
| REQ-005 | Independent verification. | The dispatching session verifies files exist, citations are plausible and reachable-marked, and style rules hold before closing the packet. |

## 4. EXECUTION MODEL

Research and file authoring are delegated to one `opencode run` dispatch of `zai-coding-plan/glm-5.2` at variant `max` (operator-selected), working in this repository so the files land directly in this packet. The dispatching session (Claude Code) owns the packet, verifies the deliverables, and closes the tasks.
