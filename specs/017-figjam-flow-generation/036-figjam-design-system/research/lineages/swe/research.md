# FigJam board design quality, cross-type consistency and a user-editable design spec

**Lineage:** swe (cli-devin, model swe-2-max) · **Session:** fanout-swe-1792955293904-icey00 · **Iterations:** 2 of 2 · **Stop reason:** maxIterationsReached · **Written:** 2026-10-25T19:26Z

Every item here is a finding or a proposal from the `swe` lineage. Nothing in `AI Systems/Product Owner/sk-create-figjam/` was modified; this lineage writes only inside `AI Systems/Product Owner/specs/017-figjam-flow-generation/036-figjam-design-system/research/lineages/swe`.

## 1. Run notes the merge should know

- Iteration 1 read `compose-board.js` end to end (all 1,230 lines), `references/style-guide.md`, `references/quality-rubric.md` §6-7 and the screenshots README, and viewed seven rendered boards as images: `user-flow-board.png`, `process-board.png`, `architecture-board.png`, `sequence-board.png`, `state-board.png`, `er-board.png`, `gantt-board.png`. Iteration 2 read `scripts/compose_board.py`, `scripts/figjam_checks/common.py`, `references/types/sequence.md` and `state.md`, the `sk-design-md-generator` SKILL.md and its `design-md-format.md`, plus public sources (Google Labs `DESIGN.md` spec, `@google/design.md` on npm, W3C DTCG Format Module 2025.10, getdesign.md/Stitch notes).
- **Skipped by write boundary (recorded, not executed):** the bounded `spec.md` pre-init mutation and `step_writeback_spec_findings` (root `spec.md` is outside the lineage), `step_graph_upsert` (coverage-graph DB outside the lineage; `graphEvents` carried as `[]`), `step_validate_post_synthesis_spec_doc` (validate.sh is prohibited by dispatch), and the terminal observability row (fan-out lineage; `skip_when: config.fanout` applies by intent).
- **Gateway note:** the `type:"iteration"` record's `status` must be one of `complete|error|insight|stuck|thought|timeout`; an initial `completed` was refused by the payload validator and corrected.
- `steer.md` never existed in this lineage; no lead rulings were received.

## 2. What the current boards already do well (keep all of it)

1. **One framed board with real furniture on every type** — white section, 64 px Bold title, 28 px Regular subtitle wrapped to a 960-1440 band, gray `Key` section, 16 px source line, 80 px margins [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1123-1202]. Identical on all seven screenshots — the strongest consistency asset.
2. **Colour by kind, enforced semantically.** Each of ~30 kinds fixes shape and colour together, so a colour means the same thing on every board [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:51-83] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:32].
3. **A first glance that works.** The pink `#F849C1` accent (8 px node outline / 4 px message) is a hue no kind uses, clears the 3:1 mark gate, and outweighs every other mark at 25.0 vs 12.6 weight×contrast [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:135-152]. It reads first on every viewed board: Return confirmed (`user-flow-board.png`), Authorise the card (`sequence-board.png`), the critical bar (`gantt-board.png`), Booking (`er-board.png`), sync-service (`architecture-board.png`), Approve the claim (`process-board.png`).
4. **A key generated from what the board actually draws** — every kind, line and arrow in use, and nothing else [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1142-1194] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:136].
5. **Algorithmic connector legibility.** A port-pricing solver (6 seeded restarts, pair-wise sweeps, BLOCKED/CLASH/NEAR costs) keeps labels mid-connector and clear of boxes, titles, zones and each other [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:600-840]. Visible as clean mid-run labels on `user-flow-board.png` and `er-board.png`.
6. **FigJam-native palette pairs with measured contrast** — every kind draws a swatch pair the check accepts and the self-test re-measures, so boards stay recolourable from the FigJam picker [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:103-120] [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/common.py:43-61].
7. **One Inter ramp at 64/28/24/20/16 (14-16 for fields/pins/bars),** weight carrying hierarchy, on an 8 px grid with one size per shape class [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:191-202] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:568-579].
8. **A source line that names sources and what was left out** on every board — provenance visible at a glance.

## 3. How the seven types read side by side

- **Hierarchy and first glance:** title → accent → spine/first rank, in that order, on all seven. The accent is the single focal mechanism and it is uniform — one thing in pink, never more.
- **Alignment and spacing rhythm:** 8 px grid, fixed composer steps (80 cross / 136 rank / 48-96 zone / 80 board / 64 key) hold everywhere; flows read as one spine with exits beside it. Sequence is the exception in feel — fixed `ROW=72` spreads seven messages over a tall, mostly empty column.
- **Type scale and weight:** identical ramp everywhere; the only per-type variation is deliberate (entity field lines, gantt bar length text, sequence pins).
- **Colour harmony and contrast:** pastel fill/stroke pairs are harmonious and restrained; the risk is not harmony but *signal distance* — zone tints are near-white and planned gantt bars are hollow.
- **Connector routing and label legibility:** solver-owned and uniformly good; sequence self-message loops are the one cramped element (`SELF_DROP=40`).
- **Zone tints:** `TINT_CYCLE` alternates warm/cool so neighbours never merge, but at overview zoom the six tints are only just separable (`architecture-board.png`); `state-board.png`'s composite zone reads through its label more than its tint.
- **Key:** correct-by-construction everywhere; the architecture key is the widest (9 entries) and approaches board width.
- **Density:** flows and ER are balanced; sequence is airy-right, gantt airy-between-bars, state has a hollow middle-right region — three of seven boards lean sparse.
- **Cross-type similarity:** family resemblance is real and high — same furniture, same palette grammar, same accent. Divergence lives in kind vocabulary and layout mode (deliberate), not in style (no drift observed). Scores 19-22/22 corroborate.

## 4. Ranked design changes

Rank weighs how much a change shows on the board, how many of the seven types it reaches, and how cheap it is. **[C]** marks changes about consistency across diagram types — there are five: 1, 2, 5, 10, 11.

1. **[C] Take `pink` out of `TINT_CYCLE`, and add a tint check to the self-test.** `TINT_CYCLE` ends in `'pink'` [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:48] while the light pink pair "belongs to the accent alone" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:139]. A sixth zone tint can therefore visually collide with the one mechanism that marks the first glance. The self-test inspects kinds but never tints [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:712-727]. Changes `assets/compose-board.js` (line 48) and `scripts/compose_board.py` (accent check), plus the cycle recorded in `references/style-guide.md` §2.
2. **[C] Single-source the palette/kind table into a spec file that composer, check and mirror all derive from.** Today the same truth lives in `compose-board.js` constants, `ACCENT_PAIRS`/`PAIRED_FILL`/`LANE_PAIR` in `scripts/figjam_checks/common.py:47-61`, and the mirrored knowledge copy at `claude project/knowledge/Product Owner - Assets - Flow Board Composer.md` [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:71-73]. Three stores agreeing by convention is the top cross-type consistency risk and the spec file's core justification (see §5).
3. **Make sequence rows adaptive and deepen self-loops.** `ROW` is fixed at 72 px and `SELF_DROP` at 40 px [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:939,957]; `sequence-board.png` shows the result — the sparsest board at 19/22 [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/screenshots/README.md]. Scale row height to the tallest label on the row and give self-loops enough drop to carry their label clear of the lifeline.
4. **Give gantt `planned` bars a real fill.** `planned` is white with a thin gray stroke [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:78], so on `gantt-board.png` bars read as unfilled outlines and the chart is hollow until the critical bar. A light fill (e.g. light blue or a soft gray fill) restores weight without breaking the status grammar; keep critical's heavier outline and milestone's diamond.
5. **[C] Codify the accent as a spec token with locked semantics** — pink pair, 8 px on nodes and bars, 4 px on sequence messages, hue ≥45° from every kind, ≥3:1 on canvas [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:161-169] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:921-927]. It is uniform across all seven types today; making it a named token keeps it uniform under user theming.
6. **Deepen zone tints a step (a few points more chroma), still near-white.** `TINT` values like `#F5FBFF`/`#FFF7F0` [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:42-47] are only just separable at overview on `architecture-board.png` and `state-board.png`. Keep the alternating warm/cool cycle; raise tint presence so grouping is visible before the label is read. Alternatively ship current values as spec defaults and let users deepen them — either way the tokens must be named.
7. **Lighten sequence participant foot labels.** Heads and feet are identical full-weight boxes [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:970-978]; on `sequence-board.png` the duplicated labels double the type weight of the participant column. A reduced fill or smaller label on the foot keeps the UML idiom at half the weight.
8. **Let the key wrap to two rows past a width budget.** The architecture key draws nine entries in one row [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/screenshots/architecture-board.png] from a single `kx` cursor [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1158-1194]. Wrapping keeps wide keys inside the diagram's width band.
9. **Lift ER entity cards with a faint title rule or header band.** Cards are all-white with hierarchy resting on the bold title and field list [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/screenshots/er-board.png]; ER is the chromatically flattest type [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:76]. A hairline under the title (or a near-white tinted header inside the card) adds structure without inventing colour meaning.
10. **[C] Publish the full type ramp as tokens.** 64/28/24/20/16 plus 14-16 field/pin/bar sizes, weight per role [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:191-200] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:89] — identical across all seven types by convention; a `type` token section makes it identical by construction.
11. **[C] Tokenise connector grammar** — stroke `#757575`, weight 2, dash `[10,6]`, `ARROW_LINES`/`ARROW_EQUILATERAL`/`NONE` caps, label type [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:210-228] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:921-927]. Routing stays algorithmic (finding: the solver is not a token surface), but stroke/weight/dash/caps are tokens shared by every type.
12. **Write a density note into the spec, not the composer.** Three of seven boards lean sparse (sequence rows, gantt between bars, state's hollow middle-right — `state-board.png`). The rubric's Proportion criterion already catches it [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:137]; the fix is model-side (split or re-flow), so the spec should carry a `density` guidance section rather than a padding knob.

## 5. Recommendation: the design spec file

**Yes — the packet should read a user-editable design spec, and the strongest form is a packet-level `DESIGN.md`-style file with a YAML token layer, seeded verbatim from today's constants.**

### 5.1 Where it lives

- **Packet level first:** a new file under `AI Systems/Product Owner/sk-create-figjam/` — e.g. `references/board-style.md` (sits beside `style-guide.md`, which stays the *rationale* document) or a packet-root `DESIGN.md`. The spec describes one packet's drawing surface; a repository-root `DESIGN.md` collides with `sk-design`'s artifact name and overreaches [SOURCE: .skilled/skills/sk-design/sk-design-md-generator/references/design-md-format.md:49-64].
- **Optional user override:** resolved by walking up from the model file's directory (project → packet), so a repo user can restyle without touching the packet.
- **The claude.ai Project mirror** has no Python and fills MODEL by hand inside a copied composer [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:71-73]; the mirror ships the *resolved* constants inside its knowledge copy via the existing SYNC.md mirror contract [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:240-242]. It does not read the spec at runtime — a knowledge-file copy of the spec is documentation for mirror users, not an input.

### 5.2 Schema

Borrow Google's `DESIGN.md` shape — a markdown file whose normative values live in YAML (front matter or interleaved fenced blocks), prose explains rationale, unknown sections are tolerated [SOURCE: https://github.com/google-labs-code/design.md/ ; https://cdn.jsdelivr.net/gh/google-labs-code/design.md@main/docs/spec.md]. Token typing follows the W3C DTCG model (typed groups, `{path}` aliases) at YAML scale rather than raw DTCG JSON, which is tool-interchange, not hand-editing [SOURCE: https://www.w3.org/community/design-tokens/].

Sections — every one optional, each defaulting to the current constant:

```yaml
meta:    { name, extends }            # extends: another spec path for layering
colors:
  pairs: { lightBlue: {fill: "#C2E5FF", stroke: "#3DADFF", text: "#1E1E1E"}, ... }
  kinds: { start: lightBlue, screen: white, decision: lightYellow, ... }
accent:  { pair: lightPink, nodeWeight: 8, messageWeight: 4 }
zones:   { tints: {...}, cycle: [blue, orange, teal, yellow, violet], labelType: {size: 24, weight: SemiBold} }
type:    { family: Inter, ramp: {title: [64,Bold], subtitle: [28,Regular], zone: [24,SemiBold], node: [20,Medium], label: [16], field: [14]} }
spacing: { grid: 8, cross: 80, rank: 136, zonePad: 48, zoneHead: 96, zoneGap: 48, boardPad: 80, keyOffset: 64 }
shapes:  { kind -> FigJam shape + cornerRadius }       # e.g. pin radius 14
connectors: { color: "#757575", weight: 2, dash: [10,6], endCap: ARROW_LINES, label: {size: 16, weight: Medium} }
key:     { fill: "#F9F9F9", title: "Key", sample: {w: 88, h: 48} }
title:   { type: title, wrap: [960, 1440] }
subtitle:{ type: subtitle }
source:  { type: label }
density: { guidance-only prose, no knobs }
```

Out of scope for the file (hard boundary): routing-solver costs, layout algorithms, key membership, and the judgment spacing bands [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:600-840] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:221-234].

### 5.3 How each reader reads it

- **`compose_board.py`:** parse the YAML layer, resolve aliases, validate, then inject the resolved constants into the template as a second substitution (`__STYLE__`) beside `__MODEL__` — same single `use_figma` call, same 50,000-char ceiling [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:70-76,595-596].
- **`compose-board.js`:** constants block becomes `const SPEC = __STYLE__;` with reads through it; defaults compiled in so a missing block still composes identically.
- **`figjam_checks/common.py` / self-test:** `ACCENT_PAIRS`, `PAIRED_FILL`, `LANE_PAIR` and the accent checks (hue ≥45°, mark ≥3:1, text ≥4.5:1) re-run against the loaded spec — the existing machinery is the validator [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:700-727] [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/common.py:157-158].
- **Mirror:** ships resolved constants, spec file mirrored as documentation only.

### 5.4 Safe defaults under bad edits

Following the packet's own rule — model errors refuse, style degrades gracefully [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:176-185]:

- Unparseable file → warn, compose with built-in defaults (never refuse).
- Unknown key / unknown kind → warn, ignore the key.
- Colour not a recognised FigJam pair → warn that picker recolouring is lost for it (the recorded trade-off), accept only if floors pass [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:156,206].
- Contrast floor failures (text <4.5:1 on fill, mark <3:0:1 on canvas, accent <45° from every kind hue) → reject that token to its default with a named warning; never fail the board [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:702-726] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:170-174].
- Non-8-multiple spacing → snap to grid with a warning, preserving the grid invariant.

### 5.5 How the rubric and scorecard check a board against it

Section 7's criteria stay; their referent changes from the hardcoded palette to the loaded spec [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:126-139]:

- "Colour by meaning" scores "every colour names a kind the loaded spec declares, and the key explains it."
- "Key and source" adds "key samples match the spec's pairs" — the generated key is already spec-faithful by construction.
- A `Spec conformance:` line joins the finding format, naming any spec token the board deviates from and why (e.g. a floor rejection that fell back).
- The scorecard's scale and per-criterion 0/1/2 semantics are untouched — comparability across boards survives.

## Eliminated Alternatives

- **Raw DTCG `tokens.json` as the spec file** — machine-interchange format, hostile to hand-editing; the question asks for a user-editable file. Typed groups and alias syntax are borrowed inside markdown+YAML instead.
- **Repository-root `DESIGN.md` only** — collides with `sk-design`'s artifact naming and asserts style over surfaces it does not own; packet-level with an optional upward override is the scoped answer.
- **Per-type theme sections in the spec** — type divergence is kind vocabulary and layout mode, not styling (iteration 1 finding 15, iteration 2 finding 9); one shared kind-token table is both simpler and the consistency guarantee.
- **Exposing solver/layout constants in the spec** — invites boards that violate routing invariants a user cannot see.
- **Fail-closed on malformed spec** — contradicts the packet's degrade-gracefully posture for style; validation rejects tokens, not boards.
- **Reading the spec at runtime in the mirror** — the mirror has no Python; resolved constants ship inside its copied composer.

## Divergence Map

- **Saturated directions:** none — both iterations answered all five key questions (registry: `resolvedQuestions: 5`, `iterationsCompleted: 2`).
- **Pivots taken:** none required; iteration 2 consolidated iteration 1 finding 15 via the type references rather than pivoting.
- **Evidence and Council artifacts:** 30 registered findings (`f-iter001-*`, `f-iter002-*`) with per-finding sources in `deltas/iter-001.jsonl` and `deltas/iter-002.jsonl`; no Council artifacts.
- **Pivot failures / audited overrides:** none.
- **Remaining frontier:** `references/types/{architecture,er,gantt,process,user-flow}.md`, `references/flow-mode.md`, `assets/flow-templates.md`, `assets/templates/*.md`, `assets/examples/*.md` and the remaining screenshots (`dense-flow-board.png`, `state-on-existing-board.png`) were not exhaustively read — the synthesis stands on composer, check, self-test, rubric, style-guide and seven rendered boards, which cover the spec-relevant surface. The Barter product surface was intentionally untouched per dispatch.

## Open Questions (for the merge)

- Should the spec's colour tokens permit non-FigJam-native pairs at all, or should the file restrict itself to the native set so recolourability is never at risk? (§5.4 recommends warn-and-accept with floors; a stricter alternative is refuse.)
- Does the merge want the spec consumed by the generator path only, or also offered as a user-facing template (`assets/`) authors can copy?

## Convergence Report

- Stop reason: maxIterationsReached
- Total iterations: 2
- Questions answered: 5 / 5
- Remaining questions: none blocking; merge-level open questions listed above
- Iteration summaries: (1) composer design-surface inventory + seven-board visual audit — 15 findings; (2) DESIGN.md/DTCG conventions, consumption path, schema, safe defaults, rubric integration — 15 findings
- Convergence threshold: 0.05 (telemetry only; `convergenceMode: off`, `stopPolicy: max-iterations`)
- Divergence summary: no pivots, no failures, frontier = unexhausted type references and examples noted above

## Sources

Primary packet sources: `AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js`, `scripts/compose_board.py`, `scripts/figjam_checks/common.py`, `references/style-guide.md`, `references/quality-rubric.md`, `references/types/{sequence,state}.md`, `SKILL.md`, `assets/screenshots/{README.md,user-flow,process,architecture,sequence,state,er,gantt}-board.png` (as rendered images). Design-spec sources: `.skilled/skills/sk-design/sk-design-md-generator/SKILL.md` and `references/design-md-format.md`; https://github.com/google-labs-code/design.md/ ; https://cdn.jsdelivr.net/gh/google-labs-code/design.md@main/docs/spec.md ; https://www.npmjs.com/package/@google/design.md ; https://www.w3.org/community/design-tokens/ ; https://www.designtokens.org/tr/third-editors-draft/format/ ; https://github.com/VoltAgent/design-md . Full provenance: `resource-map.md` in this lineage directory.
