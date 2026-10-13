---
title: "Feature Specification: Router Coverage, Skill Slimming and Template Parity"
description: "Sixteen of twenty realistic requests fall through to a clarifying question. SKILL.md carries a 608-line pseudocode fence that a model does not need inline. DEPTH is always loaded and is being retired. The three new shape templates skipped the asset convention every other template follows."
trigger_phrases:
  - "optimize product owner routing"
  - "reduce skill.md size"
  - "deprecate depth framework"
  - "template overview section parity"
  - "router falls back too often"
importance_tier: "high"
contextType: "specification"
_memory:
  continuity:
    packet_pointer: "008-router-and-skill-slimming"
    last_updated_at: "2026-09-03T00:00:00Z"
    last_updated_by: "claude"
    recent_action: "Measured the fallback rate, the SKILL.md line budget and the template divergence"
    next_safe_action: "Implement R1 through R5 in one pass, since all five land on SKILL.md"
    blockers: []
    key_files:
      - "sk-product-owner/SKILL.md"
      - "sk-product-owner/references/depth-framework.md"
      - "benchmark/router/route_contract.py"
      - "benchmark/router/differential.py"
    completion_pct: 5
    open_questions:
      - "Does anything downstream depend on DEPTH energy levels once the framework is retired"
    answered_questions:
      - "The 608-line pseudocode fence is what makes SKILL.md 962 lines"
      - "The differential harness lifts that fence from SKILL.md, so moving it means repointing the harness"
      - "Sixteen of twenty uncommanded realistic requests currently reach INTERACTIVE"
---
# Feature Specification: Router Coverage, Skill Slimming and Template Parity

<!-- SPECKIT_LEVEL: 2 -->
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->

---

## 1. METADATA

| Field | Value |
| --- | --- |
| Spec ID | 041 |
| Level | 2 |
| Status | Planned |
| Created | 2026-09-03 |
| Related to | 007-story-mode-and-shape-templates |
| Systems touched | Product Owner only |

---

## 2. PROBLEM & PURPOSE

### 2.1 Measured problems

**The router asks a question for most real requests.** Twenty realistic PM phrasings, none using a command token, were run through the route contract. Sixteen reached INTERACTIVE, eleven of those at confidence `0.0`:

| Request | Route |
| --- | --- |
| add a deadline badge to the collab card | INTERACTIVE 0.25 |
| the app crashes on rotate during upload | INTERACTIVE 0.25 |
| the follower count shows `--` for tiktok | INTERACTIVE 0.0 |
| build a toggle row component for notification prefs | INTERACTIVE 0.0 |
| search results are slow, need pagination | INTERACTIVE 0.0 |
| give the PM a draft on read receipts | INTERACTIVE 0.0 |
| brands want analytics, whole dashboard thing | INTERACTIVE 0.0 |

These are ordinary backlog intake. A crash report scoring 0.25 and a component request scoring 0.0 mean the semantic tables cover the vocabulary of the command tokens rather than the vocabulary people use.

**SKILL.md is 962 lines and one fence is 608 of them.** Section 2 alone is 689 lines. The fence is executable Python that the benchmark needs and a model does not, since the model needs the routing rules, not their reference implementation.

**DEPTH is always loaded at 556 lines** and is being retired outright.

**The three shape templates skipped the asset convention.** Every other template asset opens `## 1. OVERVIEW` with Purpose and Usage, then numbered template sections. `story-template.md`, `epic-template.md` and `story-draft-template.md` jump straight into scaffold content, and the draft template has no structural sections at all.

### 2.2 Purpose

Route the requests people actually type, carry the routing rules in a form a model can use, retire DEPTH, and make the three new templates look like every other template.

### 2.3 Non-goals

- Changing which shape any currently-correct input resolves to
- Changing any artifact's house format
- Touching the other eight systems

---

## 3. REQUIREMENTS

### R1 — Route what people type

* * *

Extend the semantic tables so ordinary phrasing reaches the right mode without a command token.

The measured gaps cluster by intent:

- **Task**: component and build requests, "add a badge", "build a toggle row", "need pagination", "tidy up the copy"
- **Bug**: symptom reports with no defect noun, "the app crashes", "shows `--`", "this is broken", "X is slow" where slow means regression rather than a feature
- **Story**: capability requests framed as user need, "creators cannot X, we should let them"
- **Epic**: initiative framing, "whole dashboard thing", "the whole X", multi-surface scope
- **Story Draft**: handoff framing, "give the PM a draft", "turn my notes into something the devs can pick up"
- **Doc**: explanation framing, "something for the team explaining X", "write up the comparison"

Target: no more than four of the twenty probe requests reach INTERACTIVE, and none of the four for a reason other than genuine ambiguity.

**Guard against over-matching.** Every existing fixture must still pass. `create a task to write a PRD` stays TASK. A word that appears in both a defect report and a feature request must not tip a whole intent, which is why "redesign", "rework" and "overhaul" were deliberately excluded before. State the reasoning for any borderline term in a code comment.

### R2 — Move the pseudocode out of SKILL.md

* * *

Target: **SKILL.md under 600 lines.**

- Move the 608-line pseudocode fence to a new reference, `references/router-contract.md`
- SKILL.md keeps a compact prose routing section: the command table, the framing rules, the confidence thresholds, the resource map and the shape resolution. Rules a model can follow, not an implementation it must parse
- `benchmark/router/differential.py` lifts the fence from SKILL.md today. Repoint it at the new file
- The new reference is not ALWAYS-loaded. It is the executable contract for the benchmark, and ON_DEMAND for a reader who needs the exact algorithm

### R3 — Retire DEPTH

* * *

Delete `references/depth-framework.md` and remove DEPTH from the system.

Seventeen files reference it: `SYNC.md`, `AGENTS.md`, `claude-project.sync.json`, `graph-metadata.json`, `description.json`, `sk-product-owner/README.md`, `SKILL.md`, all five mode references, `interactive-response-templates.md`, `claude project/README.md`, `Custom Instructions.md` and the lock file.

Anything DEPTH currently carries that the system still needs must be identified before deletion and rehomed, not dropped silently. Energy levels are the likely case, since Quick energy is a routing output. Report what was rehomed and where.

### R4 — Template parity

* * *

Give `story-template.md`, `epic-template.md` and `story-draft-template.md` the structure every other template asset uses:

```
## 1. OVERVIEW
### Purpose
### Usage
---
## 2. {SHAPE} TEMPLATE
```

Match `task-templates.md` and `bug-report-template.md` for tone and depth. Usage says which mode loads the asset and what to do with it. This is packaging only, and no scaffold content changes.

### R5 — Check AGENTS.md

* * *

`AGENTS.md` is 256 lines and is the CLI bootstrap. Verify it still describes the system accurately after the Story Mode rename, the template split, the pseudocode move and the DEPTH retirement. Fix what has gone stale.

---

## 4. SEQUENCING

All five land on `SKILL.md`, so they go in one pass. Within it: R3 first, since retiring DEPTH shrinks what R2 has to rewrite. Then R2, then R1, then R4 and R5.

---

## 5. RISKS

| Risk | Mitigation |
| --- | --- |
| R1 over-matches and breaks existing routing | Every fixture passes, plus the differential harness, plus explicit negative fixtures for the excluded terms |
| Moving the fence breaks the differential harness | Repoint it in the same commit, run it before anything else |
| Retiring DEPTH drops a rule the system needs | Identify and rehome before deleting, and report what moved |
| SKILL.md and Custom Instructions.md drift | Both are contract inputs. Edit each once, all changes together |

---

## 6. VERIFICATION

- `bash benchmark/router/run_fixtures.sh`, fixtures and differential both green
- The twenty-request probe rerun, with the fallback count reported before and after
- `node benchmark/format/validate-output-format.cjs` and `bash benchmark/format/run_fixtures.sh`
- The 91 artifacts under `export/z — Test Exports*/` still pass
- `wc -l sk-product-owner/SKILL.md` under 600
- No DEPTH reference outside changelogs
- Sync compiler run, knowledge count correct
