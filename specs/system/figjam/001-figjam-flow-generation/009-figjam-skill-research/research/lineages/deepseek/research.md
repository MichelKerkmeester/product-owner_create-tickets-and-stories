# Flow Mode × public FigJam diagram skills — research synthesis

**Run:** `fanout-deepseek-1792482040367-nu2bmb` · 20 iterations · stop reason `maxIterationsReached`
**Scope:** Flow Mode's Mermaid → FigJam pipeline against eight pinned public diagram-skill repositories, plus one repo found by `gh search` during the run.
**Limits of the evidence:** every write-route finding is a rule read against a corpus source. No board was written during this research, so nothing here claims observed generator behaviour on a live FigJam file.

---

## 1. Executive summary

Flow Mode's strongest asset is its executable pre-write check. No corpus skill has a deterministic model checker with planted self-tests, and the official skill leaves most of its rules to prose that the model must remember at call time. Its weakest asset is the page rule: it tells the run to write into a new or confirmed-empty page and to roll back by clearing that page, while the vendor API cannot create a page in a FigJam file and a shared board can hold other people's work.

The research produced **thirteen changes**: twelve ranked below and one route-specific batch. It also settled Flow Mode's five deliberate limits: three survive unchanged or with an added obligation, one changes unit only if a palette is ever defined, and one should stop being a rule.

The highest-value fix is not the page rule. It is the **unchecked edge operator**: `flow_check.py` validates node shapes, exits, counts, labels and colour, but never looks at `Edge.style`, `undirected` or `bidirectional`, so `A --- B`, `A <--> B`, `A -.-> B` and `A ==> B` all pass and the board renders a connector that means something the model did not intend [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:77] [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:181].

---

## 2. Verdicts on the four known gaps

| Gap | Verdict | Reason |
|---|---|---|
| New-page rule and page rollback | **Reject the rule; adopt a file + optional section target** | `figma.createPage()` throws in FigJam; the vendor tells hybrid extensions to organise with sections instead [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:13]. The official generator creates a new file without `fileKey`, adds to an existing file with it, and replaces an old diagram by deleting its nodes first [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:102] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:110]. The page rule appears in **eight statements across three files**, including both error-recovery sections [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:159] [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:127]. |
| Emoji | **Adopt rejection** | The official skill states the generator's universal constraint [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:49]; ompug errors on emoji with a published range [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/sanitize.py:173]. Flow Mode has no emoji rule, so a model can pass the check and be rejected by the tool. |
| Reserved IDs (`end`, `subgraph`, `graph`) | **Adopt rejection** | The official skill names them as breaking the model [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:52]; ompug errors on both its reserved set and Mermaid keywords, lowercasing the ID first [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:520]. Match case-insensitively. |
| Underscored IDs | **Adopt rejection** | Official guidance ties underscores to broken edge routing [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:53]; ompug makes it an error [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:525]. |

---

## 3. Verdicts on the five deliberate limits

| Limit | Verdict | Evidence |
|---|---|---|
| **TD only** | **Keep as house default; stop stating it as a generator requirement** | The official default is LR; rocket-path uses LR and TD for decision trees; ompug's linter and Mermaid Jam accept five directions. No corpus source mandates TD [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:26] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:211]. |
| **9 nodes** | **Keep; add a naming obligation when splitting** | Official soft cap ~20, ompug ~25, FMCP times out at 7–12 nodes per write, and rocket-path's densest example is exactly 9 [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:329] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/references/diagram-types.md:31] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/references/examples.md:22]. Anything omitted by a split must be named, never dropped silently [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/references/diagram-types.md:32]. |
| **3 decision exits** | **Keep unchanged** | Official decision trees and rocket-path's examples use three labelled exits [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:26] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/references/examples.md:92]. |
| **One accent colour** | **Keep one hex** — "accent family" withdrawn | A family has no membership rule without a palette, so the check would be arbitrary; one hex is exact and self-testable [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:45]. The official semantic-colour guidance and IamTheLime's MAIN/note/warning palette justify a role palette only if `flow-templates.md` ever defines one [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/themes.md:26]. |
| **Four shapes** | **Keep; cite the vendor table** | Rectangle, stadium, ellipse-circle and diamond all render distinctly, while most other Mermaid shapes fall back to rectangles [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:35]. rocket-path's "full range" claim is the counterexample that proves the limit's value [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:52]. |

Subgraph support is **rejected**, not left open: the official recipe couples subgraphs to tinted fills, per-subgraph direction and node-to-node edges, each colliding with an existing Flow Mode rule [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:157] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:161]; Mermaid Jam rejects them outright [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:23].

---

## 4. The ranked changes

| # | Change | Flow Mode target | Corpus source | Proof |
|---|---|---|---|---|
| 1 | Reject undirected, bidirectional, dashed and thick edges; the message names the label or loop-back alternative | `sk-product-owner/scripts/flow_check.py` | [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:50] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/references/figjam-snippets.md:221] | self-test planted `---`, `<-->`, `-.->`, `==>` |
| 2 | Replace page language with a file + optional section target in all eight statements | `sk-product-owner/references/flow-mode.md` (63, 115, 117, 159), `claude project/knowledge/Product Owner - Templates - Flow Mode.md` (41, 93, 95, 127), `claude project/Custom Instructions.md:249` | [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:13] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:674] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/README.md:30] | 8/8 paragraph count; parity read after commit |
| 3 | Reuse `fileKey` on revision; delete the previous diagram's nodes before regenerating | `flow-mode.md` Section 5, Section 7 | [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:102] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:110] | recovery scenario read-through |
| 4 | Emoji error using ompug's published ranges | `flow_check.py` | [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/sanitize.py:173] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:49] | self-test planted emoji |
| 5 | Reserved-ID error, case-insensitive | `flow_check.py` | [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:52] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:37] | self-test planted `end` |
| 6 | Underscore-ID error | `flow_check.py` | [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:53] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:525] | self-test planted underscore |
| 7 | Read-back v2: section scope, endpoint direction, missing/extra names | `flow-mode.md` Section 6, `assets/flow-templates.md:122`, mirror Section 6 | [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md:50] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:1191] | worked passing and failing lines |
| 8 | Raw-text markup scan for HTML tags and emphasis | `flow_check.py` | [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:242] [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:44] | self-test planted `<b>` |
| 9 | 80-character label cap, measured after cleaning | `flow_check.py` | [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/build.py:25] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/shared/reviser.ts:138] | self-test planted 81 chars |
| 10 | Uncertain-call reconciliation before retry | `flow-mode.md` Section 5 | [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:5] | failed-call scenario read |
| 11 | One section per diagram; one legend per board when colour carries meaning | `flow-mode.md` Sections 5–6 | [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py:26] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/themes.md:26] | multi-diagram scenario |
| 12 | Reject subgraphs explicitly | `flow-mode.md` Section 4, `flow_check.py` | [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:157] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:23] | self-test planted subgraph |
| 13 | Route hygiene on `fj` plus the pre-load rule | `flow-mode.md` Section 5 | [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/SKILL.md:24] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:59] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:139] | route read-through |

### Why this order

- Rank 1 is the most frequent silent failure: an undirected or reversed connector needs only a habitual `---`, and nothing catches it today [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:77].
- Rank 2 is the most destructive: clearing a shared page loses work no read-back can restore, and the API cannot create the replacement page the rule assumes [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:13].
- Rank 3 is the mechanism that makes revision possible and stops every regeneration creating a draft file [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:102].
- Ranks 4–6 are three one-line rules with the strongest corpus consensus and the cheapest proof [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:520].
- Ranks 7–9 turn the board from "looks done" into "proven done" and close checks that cannot fire.
- Ranks 10–13 are write-safety and route-specific rules whose proof is a scenario read, not a self-test.

---

## 5. What the research changed its mind about

1. **Accent family** — proposed in iteration 10, withdrawn in iteration 12: no palette exists, so a family check is unfalsifiable.
2. **Exact-match reserved IDs** — proposed in iteration 14, withdrawn in iteration 19: the corpus linter lowercases IDs before comparing.
3. **Subgraph support** — considered open in iteration 8, rejected in iteration 12: it cascades into three rule changes.
4. **`fileKey` reuse** — ranked 10 in iteration 18, promoted to 3 in iteration 19: without it, every regeneration creates a draft file.

Keeping these reversals visible is deliberate. Each one came from reading the target file or a corpus implementation rather than a corpus claim.

---

## 6. Implementation batches

| Batch | Contents | Proof |
|---|---|---|
| **A — checker** | six rules: edge operators, emoji, reserved IDs, underscores, raw-text markup, label cap; eight planted models; updated docstring | `python3 sk-product-owner/scripts/flow_check.py --self-test` exits 0; every planted model exits 1 |
| **B — model rules and asset** | nine-bullet rule list, reworded label rule, recalculated check/read-back split, v2 `Read-back:` line in `flow-templates.md` | Batch A plus a read of the five shipped patterns against the new rules |
| **C — Project mirror** | Section 4 rules, Section 5 write routes, Section 6 read-back, Section 7 recovery, hand-written with recorded adaptations (no script, no `fj` route) | paragraph-by-paragraph diff against the skill |
| **D — kernel** | one Flow Mode Delivery line; H1 minor bump v1.2.2 → v1.3.0; skill 1.2.1.0 → 1.2.2.0 | kernel line stays one line; version moves in the same change |

Order is A → B → C → D. Each batch's proof exists when it runs; D last because the kernel summarises the mirror.

---

## 7. External preconditions (not performed here)

1. **Commit the untracked Flow Mode files.** `flow-mode.md`, the mirror and `flow_check.py` are untracked, so the drift comparison has no timestamps until they are committed once [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:1].
2. **Clean the declaration.** `validate_parity.py product-owner` currently exits 2 because `systems.py` differs from HEAD and checks nothing [SOURCE: AI Systems/z — Claude Project Sync Loop/validate_parity.py:90]. The gate cannot certify any batch until the declaration matches a commit.
3. **Run the parity read after the batch lands**, then the read-only drift comparison [SOURCE: AI Systems/Product Owner/SYNC.md:12].
4. **Record the kernel review only after a named human confirms it**, as a dated sentence with the reviewer and content key [SOURCE: AI Systems/Product Owner/SYNC.md:13].
5. **Do not apply the output-format gate to Flow Mode.** Its deliverable is a board and no artifact file is written [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:143].

---

## 8. Evidence base and limits

- 20 iteration files, 20 matching state records, 235 deduplicated findings in the registry, 5/5 key questions resolved.
- Eight pinned repositories plus `rrichardsonv/parse-figjam`, read through the GitHub API and cited by URL. The pinned corpus supplied the write and read rules; `parse-figjam` supplied the inverse, board-as-data read.
- The research read `flow_check.py` and `mermaid_extract.py` directly and probed the parser with five edge operators and a markup label. Those probes are the source of the edge-operator gap and the dead-markup finding.
- **Not established:** live generator behaviour, section placement on a hosted route, and whether a thick edge renders distinctly in FigJam. Any plan that depends on those should verify them on a scratch board first.

---

## 9. Sources

**Flow Mode surfaces**
- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`
- `AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md`
- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py`
- `AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py`
- `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md`
- `AI Systems/Product Owner/claude project/knowledge/Product Owner - Assets - Flow Templates.md`
- `AI Systems/Product Owner/claude project/Custom Instructions.md`
- `AI Systems/Product Owner/SYNC.md`

**Corpus (pinned under `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/`)**
- `figma__mcp-server-guide` — official `figma-generate-diagram`, `figma-use-figjam`, `references/flowchart.md`
- `IamTheLime__dotfiles` — `figjam-diagrams`
- `southleft__figma-console-mcp-skills` — `figjam-create-content`
- `mkaralevich__pi-figma-labor` — `figjam-create`
- `amo-tech-ai__rocket-path-ai` — `figjam-diagrams`
- `atezer__FMCP` — `figjam-diagram-builder`
- `ompug__diagram-codebase` — linter, builder, sanitizer, Figma driver
- `memi-design__mermaid-jam` — parser, reviser, placement

**Widened**
- `https://github.com/rrichardsonv/parse-figjam/blob/HEAD/SKILL.md`
