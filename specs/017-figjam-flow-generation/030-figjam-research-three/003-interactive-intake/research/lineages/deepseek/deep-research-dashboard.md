---
title: Deep Research Dashboard
description: Auto-generated reducer view over the research packet.
---

# Deep Research Dashboard - Session Overview

Auto-generated from JSONL state log, iteration files, findings registry, and strategy state. Never manually edited.

<!-- ANCHOR:overview -->
## 1. OVERVIEW

Reducer-generated observability surface for the active research packet.

<!-- /ANCHOR:overview -->
<!-- ANCHOR:status -->
## 2. STATUS
- Topic: Design an interactive intake for both sk-product-owner and sk-create-figjam that keeps asking the user questions until it is confident it understands the feature well enough to produce the FigJam output, and that spars with the user on what the board should convey and how it should look. Study the current behaviour first: sk-product-owner's Interactive Mode and its question templates, the router's clarification path, sk-create-figjam's gate and its ambiguity recovery, and the kernel's Interactive Mode. Then research: a confidence model with named facts the intake must know before drawing (the reader, the question the board answers, scope, entry and exit, actors, decisions, states, sources) and a threshold, a stop rule and a round cap so it never interrogates without end, how to ask few high-value questions per round, how to propose rather than only ask (a draft outline, two alternative framings, a Mermaid sketch before the board), how to challenge a brief that asks for too much or the wrong diagram type, how to record answers so later turns build on them, how this works when the user says just do it, how energy levels such as Quick and Standard change it, and how the Claude Project kernel would carry it. Use public sources on clarifying questions, requirements elicitation and design critique, Figma's own skills that ask before acting, and the repo's .skilled/skills/sk-prompt/ for its question-asking method. Earlier research to build on, read first: AI Systems/Product Owner/specs/017-figjam-flow-generation/009-figjam-skill-research/research/research.md and AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md (sections 1 to 9). Their changes are implemented, so do not re-propose them. Packet sources: AI Systems/Product Owner/sk-create-figjam/ (SKILL.md, references/flow-mode.md, references/style-guide.md, references/quality-rubric.md, references/hybrid-workflow.md, references/types/*.md, assets/flow-templates.md, assets/templates/*.md, assets/examples/*.md, scripts/flow_check.py, scripts/figjam_checks/*.py, manual-testing-playbook/), AI Systems/Product Owner/sk-product-owner/ (SKILL.md, references/interactive-mode.md, references/routing.md, references/router-contract.md, references/story-mode.md, references/doc-mode.md, assets/interactive-response-templates.md), the hub AI Systems/Product Owner/SKILL.md, AI Systems/Product Owner/AGENTS.md, the claude.ai kernel AI Systems/Product Owner/claude project/Custom Instructions.md and the vendored AI Systems/Product Owner/mcp-figma/. The corpus is 22 public repos under research/corpus/ (Figma's own figma__mcp-server-guide skills among them). Every iteration either widens the sources (a new file, a new repo found with gh search, a public web page) or deepens an earlier finding, and names the earlier iteration it builds on. Never stop early. Cite every claim as [SOURCE: path:line] or [SOURCE: URL]. Name what the packets already do well, so nothing good is removed. Each ranked change names the Product Owner file it changes and the source it comes from. Never open AI Systems/Product Context, any screenshot or image file, any figma.com board URL or anything under a containment folder, and never quote Barter product flows. Examples use fictional companies such as Fernhouse, Loomlist and Roamstay. The synthesis proposes the intake loop as concrete changes: its confidence rule, stop rule, question bank, sparring step and where each lands in which Product Owner file, at least 8 ranked.
- Started: 2026-10-21T08:30:00Z
- Status: COMPLETE
- Iteration: 5 of 5
- Session ID: fanout-deepseek-1792563734045-t20sb9
- Parent Session: none
- Lifecycle Mode: new
- Generation: 1
- continuedFromRun: none
- stopReason: maxIterationsReached

<!-- /ANCHOR:status -->
<!-- ANCHOR:progress -->
## 3. PROGRESS

| # | Focus | Track | Ratio | Findings | Status |
|---|-------|-------|-------|----------|--------|
| 1 | Audit the current intake behaviour in sk-product-owner Interactive Mode, the router clarification path, sk-create-figjam's type choice, intake and gate, and the kernel | - | 0.85 | 9 | complete |
| 2 | Widen to the corpus: how Figma's own skills, Adobe and community FigJam builders decide they know enough to act before drawing | - | 0.70 | 10 | complete |
| 3 | Public elicitation and design-critique practice: confidence via named-dimension coverage, stop rules, recommended answers and critique questions | - | 0.75 | 13 | complete |
| 4 | Answer persistence, energy levels and the just-do-it path across sk-prompt, Interactive Mode, Flow Mode and the kernel | - | 0.60 | 12 | complete |
| 5 | Challenge rules for an over-broad brief or a wrong type, kernel placement, and the test contract a loop must change | - | 0.55 | 11 | complete |

- iterationsCompleted: 5
- keyFindings: 55
- openQuestions: 0
- resolvedQuestions: 5

<!-- /ANCHOR:progress -->
<!-- ANCHOR:questions -->
## 4. QUESTIONS
- Answered: 5/5
- [x] What do sk-product-owner Interactive Mode, the router clarification path, sk-create-figjam's gate and the kernel do today, and where does the flow stop short of a board?
- [x] Which named facts must a board intake establish before drawing, and what confidence model, threshold and stop rule make it confident enough to draw?
- [x] How should the intake spar with the user through proposals - a draft outline, two alternative framings, a Mermaid sketch - instead of only asking questions?
- [x] How should intake answers persist across turns, and what changes when the user says just do it or selects Quick energy?
- [x] How should the intake challenge an over-broad brief or the wrong diagram type, and how does the Claude Project kernel carry the loop?

<!-- /ANCHOR:questions -->
<!-- ANCHOR:uncovered-questions -->
## Uncovered Questions
- Count: 0
- None

<!-- /ANCHOR:uncovered-questions -->
<!-- ANCHOR:trend -->
## 5. TREND
- newInfoRatio sparkline: █▇▇▆▅▅▅▅▅▆▅▅▄▃▂▂▂▁▁▁
- score sparkline: █▇▇▆▅▅▅▅▅▆▅▅▄▃▂▂▂▁▁▁
- Last 3 ratios: 0.75 -> 0.60 -> 0.55
- Stuck count: 0
- Guard violations: none recorded by the reducer pass
- convergenceScore: 0.55
- coverageBySources: {"assets.ctfassets.net":1,"design.google":1,"github.com":1,"other":43,"pages.graphics.cs.wisc.edu":1,"raw.githubusercontent.com":1,"thecrit.co":1}
- Advisory events: none

<!-- /ANCHOR:trend -->
<!-- ANCHOR:dead-ends -->
## 6. DEAD ENDS
- **Reading the router's 0.85 band as an intake confidence.** It scores artifact intent from keywords, so a request can route to FLOW at HIGH confidence with a one-line brief [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:38]. Routing confidence and board confidence are different scales. (iteration 1)
- **Treating Interactive Mode's five quality dimensions as the confidence model.** They score the question's phrasing, and each can be 8+ while the reader, scope and board message stay unknown [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:431]. The confidence model has to score understanding of the feature, not the question text. (iteration 1)
- Searching `sk-create-figjam` for an existing intake questionnaire found only the type/order/plan questions listed in finding 5. The packet's intake is source reading (Section 4), not interviewing. (iteration 1)
- **Copying `approved_sections` as a literal mechanism.** It stores a set of board sections; the intake needs a set of facts with a status each. The precedent is the stored answer object, not its schema. (iteration 2)
- **Treating the four-questions-per-call limit as the round cap.** It caps one message's width, and the project-plan skill loops without a round bound [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:255]. (iteration 2)
- Adobe's Spectrum diagram material is a house-style critic, not an intake. It adds no question structure beyond the two-attempt stop [SOURCE: research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:161]. (iteration 2)
- Search for a confidence score or numeric threshold in the corpus. The only numbers are node, edge and attempt budgets; no skill scores its own understanding. Corpus-wide search returned no match. (iteration 2)
- **Adopting a fixed 15-question budget as the round cap.** The figure counts questions, and the brief's unit is a round; a round may carry one to three questions, so the budget has to be expressed in rounds and in no-new-information answers [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md]. (iteration 3)
- **Copying the seven-dimension checklist wholesale.** Its dimensions are requirement-shaped (glossary, ADR rationale). The board model needs its own nine facts, borrowing the coverage rule rather than the rows [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md]. (iteration 3)
- **Treating Google's stage list as a schema.** It describes a review conversation's focus, not the intake's stored state [SOURCE: https://design.google/library/reviewing-the-design-review]. (iteration 3)
- A search for a numeric confidence threshold on clarification in requirements engineering returned no authoritative number. Practice states completeness and stop conditions, not a calibrated score. (iteration 3)
- The Gause–Weinberg context-free-question extract returned an image-only PDF of 148 characters, so its examples could not be quoted directly; the secondary descriptions of context-free questions were read from the search index instead and are not used as evidence here. (iteration 3)
- **Mapping "just do it" to Raw energy.** Raw is reachable only by explicit "skip depth" language and skips the phase flow, which would skip the check and the gate that Flow Mode protects [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:75], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:51]. (iteration 4)
- **Putting the brief on the board as a sticky or a section.** It is a write outside the diagram and needs its own yes, because an extension the gate did not name is not covered by the first yes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:168]. (iteration 4)
- **Reusing the clarification export file as the intake record.** The contract forbids the file holding anything but the question, and a project-side run cannot write it at all [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:97], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:234]. (iteration 4)
- Search for a state file in `sk-create-figjam`. The packet has no persistent state outside the model and the provenance table, by design. (iteration 4)
- Search for an existing per-turn recap in the packet. Section 8 lists the reply's lines from the board URL to the HVR self-scan, and none of them is a brief [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:235], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:240]. (iteration 4)
- **A script rule in `flow_check.py` for brief completeness.** The check's input is the model, and the brief is settled before the model [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:170]. (iteration 5)
- **Adding a new packet or a new Knowledge file for the loop.** The loop is a step inside Flow Mode, and the kernel's Knowledge table already names Flow Mode as owning "intake" [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:207]. A new file would double the parity surface for no gain. (iteration 5)
- **Putting the intake in `sk-product-owner/references/interactive-mode.md`.** A Flow route does not load it, and the hub starts `$flow` in the other packet [SOURCE: AI Systems/Product Owner/SKILL.md:53], [SOURCE: AI Systems/Product Owner/ROUTER.md:37]. (iteration 5)
- Search for an existing intake test in the playbook: all 25 scenario files cover routing, board creation, board quality, board writes and boundaries; none covers an under-specified brief. (iteration 5)
- Search for any state file or cache in `sk-create-figjam`: none exists, by design. (iteration 5)

<!-- /ANCHOR:dead-ends -->
<!-- ANCHOR:divergent-pivots -->
## 6A. DIVERGENT PIVOTS
- Completed pivots: 0
- Failed pivots: 0
- Audited overrides: 0
- Saturated: none yet
- Pivot lineage: none yet
- Remaining frontier: none recorded

<!-- /ANCHOR:divergent-pivots -->
<!-- ANCHOR:next-focus -->
## 7. NEXT FOCUS
[All tracked questions are resolved]

<!-- /ANCHOR:next-focus -->
<!-- ANCHOR:active-risks -->
## 8. ACTIVE RISKS
- None active beyond normal research uncertainty.

<!-- /ANCHOR:active-risks -->
<!-- ANCHOR:blocked-stops -->
## 9. BLOCKED STOPS
No blocked-stop events recorded.

<!-- /ANCHOR:blocked-stops -->
<!-- ANCHOR:graph-convergence -->
## 10. GRAPH CONVERGENCE
- graphConvergenceScore: 0.00
- graphDecision: [Not recorded]
- graphBlockers: none recorded

<!-- /ANCHOR:graph-convergence -->
