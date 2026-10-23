# Iteration 7: Moneybird’s routing failures and Product Owner guards

## Focus
Identify the hub’s confirmed prior misroutes and review gaps, then translate them into FigJam-specific route behavior and validation cases.

## Actions Taken
- Read the Moneybird hub review reports, phase 18 and 19 implementation summaries, route gold rows, and hub packet-selection scenario.
- Compared those defects with Product Owner’s existing Figma-related routing signal and FigJam-only output requirement.
- Separated historical defects that were later fixed from the residual regex and live-agent limits still documented.

## Findings
1. The first Moneybird hub resolver had confirmed false routes: prefix matching made the CLI signal catch “Jortt clients,” and naming a CLI could send a Jortt-to-Moneybird migration request to the CLI packet alone, bypassing the accountant workflow; later gold rows now pin whole-word matching and the migration chain. [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:78] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/spec.md:68] [SOURCE: AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/route-replay/routing-gold.json:4943] [SOURCE: AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/route-replay/routing-gold.json:4964] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/scratch/verification/review-parent.md:14] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/scratch/verification/review-parent.md:25]
2. Product Owner currently scores the word Figma as a UI-refinement Task signal, while its new specification makes FigJam the requested output; route by explicit output intent such as a dedicated FigJam command or “make a FigJam flow,” keep ordinary Figma feedback in Task Mode, and let mixed source requests begin in Product Owner before any tool handoff. [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:44] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:51] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:59] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:71] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:97] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:79] [INFERENCE: output intent is a more stable routing signal than whether an input mentions Figma]
3. The first filing-gate repair exposed a second defect: testing raw text for a refusal let “Don’t submit anything” suppress a valid purchase-invoice handoff; Product Owner should test negated, quoted, and contextual Figma/CLI mentions so mentions alone never authorize or trigger board writes, which remain gated mutating commands. [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:78] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:90] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:179] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:184] [INFERENCE: Figma tool names inside negation or explanation should not be treated as a request to mutate a board]
4. Moneybird’s initial route suite was green despite four untested mutants, then fresh reviews found more stage-one and negation gaps; the recorded process adds one gold row or failing case per fix and checks that old gold routes do not regress, so Product Owner needs the same build-time route replay and a live plugin/CLI smoke pass as separate checks. [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:78] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:103] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/implementation-summary.md:78] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/implementation-summary.md:105]
5. The current Moneybird review still reports 46 misses in 741 reviewer prompts and 128 in 5,920 generated combinations, and its audit states that resolver results do not prove a live model follows the route; keep Product Owner’s natural-language router small, use exact commands for high-confidence FigJam intent, and verify representative live routing instead of treating a passing fixture corpus as runtime proof. [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/implementation-summary.md:109] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/implementation-summary.md:122] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/scratch/verification/review-parent.md:98] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:59] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:60] [INFERENCE: static route fixtures and live agent behavior require separate evidence]

## Questions Answered
- Which routing mistakes did Moneybird’s reviews uncover, and which controls should Product Owner adopt for FigJam?

## Questions Remaining
- What integrated risks and ordered implementation phases best fit the findings so far?

## Next Focus
Synthesize capability limits, input paths, diagram rules, cross-repository sync, plugin packaging, hub routing, precedent mistakes, and risks into a staged recommendation.

## Sources Consulted
- AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:78-105, 116-119
- AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/spec.md:64-70
- AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/implementation-summary.md:76-80, 103-123
- AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/019-review-findings-fixes/scratch/verification/review-parent.md:14-40, 63-69, 84-98
- AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/route-replay/routing-gold.json:4943-4969
- AI Systems/Product Owner/sk-product-owner/SKILL.md:44-74, 89-100
- AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:77-84
- .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:179-191
