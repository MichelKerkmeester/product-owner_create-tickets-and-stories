# Iteration 3: Three public distributions of Figma's diagram skill, and the packet's type grammar against Figma's own

## Focus

Read `openai__plugins` (Figma's skills as OpenAI ships them) and the `lightspeedwp__.github` `figma-generate-diagram` copy, then compare their per-type references — starting with `flowchart.md` — against the packet's `references/types/user-flow.md` and the rules `scripts/figjam_checks/flowchart.py` enforces. Builds on iteration 2's finding that the newer commit adds no diagram type, and on iteration 1's shared-rule baseline.

## Actions Taken

1. Located the Figma plugin inside `openai__plugins` and recursively diffed its `figma-generate-diagram` against `figma__mcp-server-guide/skills/figma-generate-diagram`.
2. Diffed `lightspeedwp__.github/plugins/figma/figma-generate-diagram` against the same guide copy.
3. Read `figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md` in full (shape table, edge semantics, ELK survival, palette, density, validation checklist, tool call).
4. Read the packet's `references/types/user-flow.md` and the rule constants and checks in `scripts/figjam_checks/flowchart.py`.

## Findings

1. The three public distributions are one rule set, not three opinions: `openai__plugins` differs from the Figma guide only in `references/workflow.md`, and `lightspeedwp__.github` is an older, shorter copy carrying repository badges at the top of its references [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:1], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-diagram/references/flowchart.md:3]. Any difference between the packet and "public FigJam work" is therefore mostly a difference from Figma's own vendor guidance.
2. The corpus documents eighteen Mermaid shapes that render as distinct FigJam shapes and three stroke types with four end caps [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:35], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:56], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:75]. The packet deliberately restricts a user flow to four shapes and solid one-way arrows [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:40], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:47], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:55]. The restriction buys one meaning per shape but costs the dotted "happens later" and thick "critical path" semantics the generator supports [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:78], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:79].
3. Shape semantics converge: Figma's "shape carries the label" principle and the packet's judged-by-hand rule are the same instruction — never repeat in text what the shape already says [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:60], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:66], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:71]. Nothing is lost by keeping the packet rule.
4. The nine light fill/stroke pairs in the packet's palette are exactly Figma's built-in pairs [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:285], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:63]. Figma additionally permits saturated fills for strong emphasis while warning that Mermaid cannot set text colour [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:295]; the packet refuses those fills because white text on a saturated fill measures 1.85:1 [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:118]. The packet's refusal is better grounded than the vendor's permission.
5. Direction is a direct conflict: Figma defaults to `flowchart LR` and switches to `TD` for hierarchies and wide sibling sets [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:26], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:27]; the packet defaults user flows to top-to-bottom and reserves left-to-right for short sequential flows [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:60]. The packet gives a reason (fan-out and platform splits), the corpus does not, but neither ties the choice to a measured layout outcome.
6. Density is the widest gap: Figma's soft caps are about 20 nodes, 20–30 "consider subgraphs", 30+ split, and its checklist allows about 25 [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:329], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:350]; the packet hard-caps a user flow at 9 nodes and a process or architecture at 9 nodes and 12 connectors, with a lane exception of 12/16 [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:64], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:44], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:45]. The packet's cap protects the manual scorecard's 100%-zoom legibility, but it forces a split of an ordinary 12-step flow that Figma's own layout is documented to hold.
7. The packet's checker already automates most of Figma's eight-item pre-call checklist: orphan nodes, decision exits and missing exit labels, merge-dot words, and node/connector budgets are code rules [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:127], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:143], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:148], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:221], against Figma's model-executed checklist [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:343]. The two Figma items with no packet counterpart are the generic cycle audit and the subgraph audit, and the packet answers both by forbidding subgraphs in a user flow and by checking cycles only for architecture [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:319].
8. The packet's architecture type is machine-checked further than the corpus's placement guidance: it fixes six lanes and an allowed-edge table with dotted lanes [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:50], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:52], while the corpus documents that the architecture layout promotes only some subgraphs to sections and inlines the rest, which is why reparenting must wrap every new node [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:68], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:69]. The packet's lane table is the stronger model; the corpus's note is the stronger warning about what the board actually contains.
9. Per-type read-back is a packet-only capability: every packet type ends with counts measured on the board against the model, with an example line [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:93], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:98], while the corpus's flowchart reference ends at the tool call and has no post-write comparison [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:400], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:405].
10. The merge dot is a packet invention with no counterpart in the corpus's shape vocabulary: a wordless circle where branches rejoin, which solves the platform-split rejoin that Figma handles with subgraphs or duplicated nodes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:45], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:58], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:35]. It is one of the packet's clear advantages and must not be removed.
11. The architecture layout code rule matches exactly: only an architecture passes `useArchitectureLayoutCode`, and a generic flowchart must not [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:407], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:182].

## Questions Answered

None fully. Q1 now has the vendor baseline and its two public redistributions; it still needs the community diagram tools (ERD plugin, Mermaid converters) before it can claim the corpus exposes no additional kind.

## Questions Remaining

- Q1: type/kind and model-rule coverage.
- Q2: layout, colour, density and board-quality measurement.
- Q3: read-back, revision, fileKey reuse, failure/retry, delivery.
- Q4: request routing and artifact handoff.
- Q5: claude.ai kernel without a Figma connector, and ClickUp.

## Ruled Out

- Counting `openai__plugins` and `lightspeedwp__.github` as independent evidence: one is identical apart from the hybrid workflow reference, the other an older truncated copy, so citing all three as separate sources would inflate the evidence base.
- Adopting Figma's eighteen-shape vocabulary for a user flow: the packet's four-shape rule is what lets the check assign one meaning per shape, and the corpus itself warns that most Mermaid shapes silently fall back to rectangles.

## Dead Ends

- Looking for a per-type read-back in the corpus's type references: none exists; the corpus validates before the call and stops at the tool call.

## Edge Cases

- Contradictory evidence: direction defaults conflict (LR vs TD) and density caps differ by a factor of two to three. Both are recorded with citations; neither is resolved into a single recommendation this iteration.
- Ambiguous input: none.
- Missing dependencies: none.
- Partial success: none.

## Sources Consulted

- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/openai__plugins/plugins/figma/skills/figma-generate-diagram/ (diff)
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-diagram/ (diff)
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md
- AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md
- AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py

## Assessment

- New information ratio: 0.85
- Questions addressed: Q1, Q2, Q3
- Questions answered: none

## Reflection

- What worked and why: diffing the three distributions first prevented a false sense of three independent sources. Reading the checker's constants (`BUDGET`, lane table, decision-exit cap) next to the corpus's prose checklist showed that the packet already automates six of Figma's eight pre-call checks, which reframed the density gap as the main open trade-off rather than a missing rule.
- What did not work and why: the first draft treated shape breadth as a packet weakness. The corpus's own warning that most Mermaid shapes fall back to rectangles shows the packet's four-shape rule is a deliberate defence, not an oversight.
- What I would do differently: read `figjam_checks/flowchart.py` before the type reference, because the enforced constants are the real contract and the prose is their explanation.

## Recommended Next Focus

Iteration 4: read the board-as-context and read-back projects — `ecestnrkl__figjam-mcp`, `ulasbilgen__mcp-skills-plugins` (`get_figjam`), `rrichardsonv__parse-figjam`, `southleft__figma-console-mcp-skills` and `atezer__FMCP` — and compare their read-back and revision models with the packet's `get_figjam`/`fj nodes -l` read-back and its fileKey reuse rule. Builds on iteration 1 finding 8 (read-back honesty) and iteration 2 finding 6 (reparenting changes what a read-back sees).
