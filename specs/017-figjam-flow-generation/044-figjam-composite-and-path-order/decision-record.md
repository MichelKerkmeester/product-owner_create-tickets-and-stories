---
title: "Decision Record: Phase 44: FigJam composite placement and path order"
description: "The launcher's node pin did not reach the runs, so the label trace moves to a Homebrew node reinstall the operator chose, carried into phase 045."
trigger_phrases:
  - "figjam node pin decision"
importance_tier: "normal"
contextType: "decision"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/044-figjam-composite-and-path-order"
    last_updated_at: "2026-10-27T16:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Recorded why the node pin is superseded"
    next_safe_action: "Reinstall Homebrew node on the operator's yes in phase 045"
---
# Decision Record: Phase 44: FigJam composite placement and path order

<!-- SPECKIT_LEVEL: 2 -->
<!-- SPECKIT_TEMPLATE_SOURCE: decision-record | v2.2 -->

---

<!-- ANCHOR:adr-001 -->
## ADR-001: Replace the launcher's node pin with a Homebrew node reinstall

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-27 |
| **Deciders** | The operator, on Claude Code's question after the rerun |

---

<!-- ANCHOR:adr-001-context -->
### Context

Homebrew's node 26.11.1 cannot load its `simdutf` library, so `flow_check.py` printed `Label: skipped` on every v1.0.9.0 run. Phase 044 put a working nvm node first on the launcher's PATH. In the v1.0.10.0 rerun every check still printed `Label: skipped` with the same load error, because the Bash tool inside each Claude Code run rebuilds PATH from the shell profile, where Homebrew's node comes first.

### Constraints
- The label trace runs inside the model's own Bash tool, which the launcher cannot reach through the environment.
- An install changes the operator's machine and waits for the operator's yes with its rollback stated.

<!-- /ANCHOR:adr-001-context -->

---

<!-- ANCHOR:adr-001-decision -->
### Decision

**Summary**: AC-006 is superseded. The working node comes from reinstalling Homebrew's node, which relinks it to the installed `simdutf`, and phase 045 proves the trace after that reinstall.

**Details**: The operator chose the reinstall over a skill change that falls back to another node and over leaving the trace skipped. The reinstall runs only after Claude Code states its rollback and the operator says yes.

<!-- /ANCHOR:adr-001-decision -->

---

<!-- ANCHOR:adr-001-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Reinstall Homebrew node** | Fixes the cause on this machine, with no skill change | An install, so it waits for a yes | 8/10 |
| `flow_check.py` falls back to the next node | Works whatever PATH the run gets | A shipped skill change that works around one machine's fault | 5/10 |
| Accept the skip | Nothing changes | Label wraps stay a by-eye check in every run | 2/10 |

**Why Chosen**: The fault is a broken local install, and fixing it at its source keeps the skill unchanged.

<!-- /ANCHOR:adr-001-alternatives -->

---

<!-- ANCHOR:adr-001-consequences -->
### Consequences

**Positive**:
- The launcher's pin is no longer needed once Homebrew's node loads.

**Negative**:
- The v1.0.10.0 rerun had no label trace. Mitigation: graders counted the orphan wraps by eye from the full-size renders.

**Risks**: A reinstall can pull a newer node. Mitigation: the composer and flow check self-tests run on it before any further rerun.

<!-- /ANCHOR:adr-001-consequences -->

---

<!-- ANCHOR:adr-001-impl -->
### Implementation

**What changes**: Nothing in the package. The reinstall changes the machine only.

**How to roll back**: `brew uninstall node`, after which the launcher's pinned nvm node is the one left.

<!-- /ANCHOR:adr-001-impl -->
<!-- /ANCHOR:adr-001 -->
