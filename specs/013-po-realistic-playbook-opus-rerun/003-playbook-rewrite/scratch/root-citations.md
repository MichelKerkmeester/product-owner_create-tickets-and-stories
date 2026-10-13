# Root citations, re-read on the post-001 tree

Read on 2026-09-25 against the committed tree: Product Owner repo `ff5c80f` (phase 001 at `ab846b4`), Barter `37591a16` (phase 001 at `1bb25170`). Paths are relative to `AI Systems/Product Owner/`. `CI.md` is `claude project/Custom Instructions.md`. The Interactive Mode knowledge file is now `claude project/knowledge/Product Owner - System - Interactive Mode - v0.405.md`, renamed from v0.404 by phase 001. The root names it by title only, so the rename breaks no citation.

## Citations the old root carries

| Root section | Cited file | Old line | New line | Rule text on the new line | Moved? |
|---|---|---:|---:|---|---|
| Clarification turns | `sk-product-owner/references/interactive-mode.md` | 85 | 85 | "A clarification is exported like any other deliverable." | No |
| Clarification turns | `sk-product-owner/references/interactive-mode.md` | 93 | 93 | "Read the file back and report its path exactly as an artifact delivery does." The line now also holds the D2 sentence: a Story asked for with its tasks asks in the Story lane at the top of `export/`, outside the bundle folder | No, text grew inside the line |
| Clarification turns | Interactive Mode knowledge file | 62 | 62 | "A clarification is delivered like any other deliverable." | No |
| Clarification turns | Interactive Mode knowledge file | 70 | 70 | "Report its export-equivalent path exactly as" an artifact delivery does. The line now also holds the Story lane sentence | No, text grew inside the line |
| Clarification turns | `sk-product-owner/SKILL.md` | 217 | 217 | "Every delivery response carries this line, in this exact shape, next to the export path and the read-back confirmation:" | No |
| Clarification turns | `CI.md` | 89 | 89 | "8. Emit the `HVR self-scan:` line in every delivery response" | No |
| Clarification turns | `AGENTS.md` Section 2 | section | section | Deliverable Export Protocol, "Do not paste the full artifact into chat" | Section cite, no line |
| Rendering without a Canvas panel | `CI.md` | 76 | 76 | "1. Always deliver the output as a Canvas Artifact, rendered in the side Canvas panel" | No |
| Rendering without a Canvas panel | `CI.md` | 85 | 85 | "5. Render the Deliverable Block before any commentary" | No |
| Export names | `sk-product-owner/SKILL.md` | 207 | 207 | New task, bug, Doc, Story and Epic patterns, `Story-` now. The line also holds the bundle folder and its reply | No, text grew inside the line |
| Export names | `sk-product-owner/SKILL.md` | 208 | 208 | Clarification in the lane `{task\|bug\|doc\|Story\|Epic}`, `intake` when no artifact was resolved | No, lane word changed |
| Export names | `CI.md` | 223 to 228 | 223 to 228 | New Task, Bug, Doc, Story (now with the bundle folder and one Deliverable Block per file), Epic and Clarification labels | No, 226 grew |
| Export names | `CI.md` | 233 | 233 | "The human reconciles `NNN` when saving outside the Project." | No |
| Defect severity | `sk-product-owner/SKILL.md` | 283 | 283 | "4. Never expand scope beyond the request ... allowed only when the chat response names it as an addition" | No |
| Defect severity | `CI.md` | 104 | 104 | "6. Never expand scope beyond the request ... allowed only when the chat response names it as an addition" | No |

Phase 001 edited these rules inside their existing lines, so no line number moved. The root's old citations all still point at the rule they name.

## The four identity greps

Run from the repository root on the committed tree.

| Grep | Old count, exit | New count, exit | Lines matched now |
|---|---|---|---|
| `grep -c "read-back succeeded" "AI Systems/Product Owner/AGENTS.md"` | `1`, `0` | `2`, `0` | 47 (step 7) and 91 (the D2 bundle reply) |
| `grep -c "read-back succeeded" "AI Systems/Product Owner/claude project/Custom Instructions.md"` | `0`, `1` | `0`, `1` | none |
| `grep -c "Canvas Artifact" "AI Systems/Product Owner/AGENTS.md"` | `0`, `1` | `0`, `1` | none |
| `grep -c "Canvas Artifact" "AI Systems/Product Owner/claude project/Custom Instructions.md"` | `4`, `0` | `4`, `0` | 76, 181, 221, 235 |

The first count moved from `1` to `2`. The D2 bundle paragraph at `AGENTS.md` line 91 added a second `read-back succeeded`. The split still holds: each proof string appears only in its own runtime's identity file. `SID-001` and `PID-001` must state `2` for the first grep.

## Citations the new root adds (T013)

| Root section | Cited file | Line | Rule text |
|---|---|---:|---|
| Export names | `sk-product-owner/SKILL.md` | 209 | "Refinement of an existing task, Doc or PRD: keep the original source basename and never overwrite the supplied source" |
| Export names | `CI.md` | 229 to 231 | The `PRD refinement`, task source sync and Doc refinement labels, each `export/[original-source-filename].md` or the retained task filename |
| Export names | `AGENTS.md` | 70 to 73 | "Refined artifact or document:" and its `export/[original-source-filename].md` block |
| Identity handover rule | `AGENTS.md` | 287 | "An explicit command routes the request and does not supply that direction. `$task`, `$bug`, `$doc` and `$story` still ask their mode's context-specific question and wait for the answer before drafting." This is why the new two-turn handover chain opens on a clarification |
| Export names | `AGENTS.md` | 84 to 91 | "Story with its tasks:" block, the two bundle paths and the bundle paragraph with its reply |
| Export names | `sk-product-owner/references/story-mode.md` | 392 to 409 | "Story With Nested Tasks": folder, `n` order, Story lane clarification outside the folder, `#### **Tasks**` block, `**Story**` block |
| Export names | `CI.md` | 226 | Bundle label and one Deliverable Block per file, Story first, each with its own `Export-equivalent path:` |
| Clarification turns | `sk-product-owner/references/interactive-mode.md` | 93 | The Story lane sentence for a Story asked for with its tasks |
| Clarification turns | Interactive Mode knowledge file | 70 | The same Story lane sentence, Project wording |
