# FigJam board design quality, cross-type consistency and a user-editable design spec

**Lineage:** opus (claude-opus-5-5) · **Session:** fanout-opus-1792955293904-icey00 · **Iterations:** 3 of 3 · **Stop reason:** maxIterationsReached · **Written:** 2026-10-25T19:14:10Z

Every item here is a proposal. Phase decision D1 freezes the work as findings only [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/036-figjam-design-system/goal.md:44].

## 1. Run notes the merge should know

- Iterations 1 and 2 read the packet's own files and all nine screenshots as images. Iteration 3 read the DESIGN.md Style Reference contract as this repository's `mcp-figma` packet records it.
- **Not read:** `.skilled/skills/sk-design/sk-design-md-generator/` and `.skilled/skills/system-deep-loop/` (the symlink resolves outside the session's allowed directories). Web search and fetch were also refused. The public token-format claims (W3C Design Tokens Community Group shape) are marked as not fetched and should be confirmed by a lineage with web access.
- **Not run:** `append-mode-event.cjs` and `reduce-state.cjs` both returned "requires approval". Each iteration record, and the synthesis record with `stopReason: "maxIterationsReached"`, is kept in `deltas/` for the lead to replay through the gateway. `deep-research-state.jsonl` was never written.

## 2. What the current boards already do well (keep all of it)

1. **One entry for every type.** A white framed section, a 64 px Bold title, a 28 px subtitle and 80 px margins [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1125-1137]. You can see it on all nine screenshots.
2. **Colour by kind, and a key generated from what the board actually draws** [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:50-83] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1142-1193].
3. **One accent that carries weight as well as hue,** so it wins in greyscale [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:135-143]. It reads first on `user-flow-board.png`, `process-board.png`, `er-board.png`, `gantt-board.png` and `dense-flow-board.png`.
4. **A straight spine with exits beside it** [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:318-327]. Both flows on `user-flow-board.png` and `dense-flow-board.png` read left to right with no backtracking.
5. **FigJam swatches written as hex/255,** so anyone on the board can still recolour it from the picker [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:156].
6. **An 8 px grid,** with one size per shape class on a board [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:568-579].
7. **A source line that names its sources and what was left out,** on every board.
8. **A measured palette.** The self-test re-measures every contrast ratio and the accent's hue distance and mark gate [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:702-727].

## 3. Ranked design changes

Rank weighs how much a fix shows on the board, how many types it reaches and how cheap it is. **[C]** marks a change about consistency across diagram types. There are six of them: 2, 3, 4, 5, 9 and 12.

1. **Take pink out of the zone tint cycle, and make the self-test check tints.** Change `assets/compose-board.js` line 48, the accent check in `scripts/compose_board.py` lines 712-727, and the allowed tint cycle in `manual-testing-playbook/manual-testing-playbook.md` line 97.
   - Evidence: `TINT_CYCLE` ends in `'pink'` [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:48], but the guide says the light pink pair "belongs to the accent alone" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:139].
   - The self-test inspects kinds only, never tints [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:712-727].
   - On `architecture-board.png`, the External lane is pink on the same board as the pink sync-service accent.
2. **[C] Tint zones and gantt sections by one rule: use a hue no member kind draws, and never the accent's.** Change `assets/compose-board.js` lines 593 and 1087, using the `tint` hook that already exists and is never set.
   - Evidence: positional tints clash with kind hues. On `user-flow-board.png` an orange exit sits in an orange zone. On `architecture-board.png` a violet store sits in a violet lane.
   - The tint is positional [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:593], while the rubric asks that nothing be coloured by position [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:132].
   - Gantt section bands use the same cycle [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1087].
3. **[C] Give each colour one role across all seven types.** Change `assets/compose-board.js` lines 51-83 and `references/style-guide.md` Section 2.
   - Evidence: light blue currently means start, gateway, first state, participant and in progress [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:52] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:65] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:70] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:77] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:79]. That contradicts "a colour means the same thing on every board" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:32].
   - On `sequence-board.png`, eight light-blue participant pills crowd the first glance.
   - Proposal: keep light blue as the `entry` role for start and first state only. Draw participants white with the neutral stroke, and record gateway and active as named roles.
4. **[C] Give the key one fixed order per type.** Change `assets/compose-board.js` lines 851-853 to sort kinds by a canonical role order, the way gantt already does at line 1059.
   - Evidence: `state-board.png` keys "Final state, State, Start, First state, End", while `state-on-existing-board.png` keys "Start, First state, State, End, Final state" [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:851-853] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1059].
5. **[C] Use one connector language, defined once.** Change `assets/compose-board.js` lines 218-220 and 921-927 and the lines table in `references/style-guide.md` Section 2.
   - Evidence: sequence requests are charcoal with closed heads, while every graph edge is gray with open heads [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:921-927] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:218-220]. Side by side, `sequence-board.png` reads heavier than `user-flow-board.png`.
   - Proposal: name connector roles once (`line.default`, `line.emphasis`, `line.reply`, `line.async`) and let each type pick from them.
6. **Line up zone tops on group-mode boards.** Change `assets/compose-board.js` lines 496-509 so zones in one row share their top edge, and their bottom edge in LR mode.
   - Evidence: ragged tops on `user-flow-board.png` (about 30 px), `dense-flow-board.png` (about 90 px) and `architecture-board.png` (five lanes at five heights).
7. **Make edge labels and key text readable at overview zoom.** Change `assets/compose-board.js` line 90: `label` from 16 to 18, or scale it with board width past 1600 px. Add a `small` step for the 14 px gantt and pin text.
   - Evidence: 16 px labels against 20 px nodes and a 64 px title are the smallest text on `dense-flow-board.png` and `user-flow-board.png` [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:90].
   - Gantt and pin text are magic 14 px values [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1101-1102].
   - The rubric judges legibility at overview zoom [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:134].
8. **Keep routed edges clear of the title block.** In `assets/compose-board.js`, add a routing level floor under the subtitle near the route constants at line 610, using the offset at line 1139.
   - Evidence: "check out" runs about 50 px under the subtitle on `state-board.png`. "Writes Blocks" climbs over Events on `architecture-board.png`.
   - The spacing rules protect zone borders but not the title [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:234].
9. **[C] Give the key the diagram's width, or align it to the grid.** Change `assets/compose-board.js` lines 1147-1148 and 1194.
   - Evidence: the content-width key leaves a large empty region on `er-board.png`, `state-board.png`, `gantt-board.png` and `dense-flow-board.png` [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1194]. The rubric penalises that [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:137].
   - The key is the one element every type shares, so its width rule is a consistency rule.
10. **Top-align ER cards within a rank.** Change `assets/compose-board.js` lines 451-456 for `entity` items.
    - Evidence: on `er-board.png`, Guest, Booking and Payment sit on three different top lines, and "makes (1 to 0..n)" jogs up into Booking [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:547-555].
11. **Wrap the subtitle so it leaves no single-word last line.** Change `assets/compose-board.js` line 1131.
    - Evidence: "Engineering" sits alone on `architecture-board.png` and "engineers" on `sequence-board.png` [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1131].
12. **[C] Score consistency and conformance to the spec.** Change `references/quality-rubric.md` Section 7 and the scorecard in `manual-testing-playbook/manual-testing-playbook.md`.
    - Proposal: add a ninth design criterion, "Matches the design spec: key order, title block, line roles and tint rule as the active spec sets them". Add a gallery scenario that composes all seven types under one spec and compares them.
    - Evidence: nothing grades cross-type drift today [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:81-93] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:126-139].
13. **Cut the colour prose in the type references down to role mappings and a pointer.** Change Section 5 and the board paragraph of `references/types/*.md`.
    - Evidence: each file restates colours the style guide owns, and the architecture file says "colours it by that lane", which the code does not do [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/architecture.md:16] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/process.md:97] [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/common.py:59-61].
14. **Give sequence step pins their own `marker` role.** Change `assets/compose-board.js` lines 1009-1012 and 1174-1177.
    - Evidence: the pin hard-codes the data-store violet [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1009-1012]. That colour was chosen for its 4.57:1 white digit [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:174], and that floor should travel with the role.

## 4. Recommendation: the design spec file

**Verdict:** yes, the packet should read one design spec file. The file should sit at one packet default with one optional user override. It should be the only home of the values the composer holds as literals today, not a fourth copy of them.

### 4.1 Where it lives

| Layer | Path | Role |
|---|---|---|
| Default | `AI Systems/Product Owner/sk-create-figjam/assets/board-design.md` | Shipped and complete. It replaces the `SHAPE`, `TINT`, `TINT_CYCLE`, `KINDS`, `TYPE`, spacing and `ARROWS` literals in `compose-board.js`. `style-guide.md` keeps the reasoning and points to it, and its `FIGJAM_PALETTE` table is checked against it |
| User override | `AI Systems/Product Owner/figjam-design.md`, at the system root beside `AGENTS.md`, optional | Holds only the tokens a user changes, with `extends: default`. The repository user restyles every board here without touching the packet |
| Per run | `compose_board.py --design <path>` | One-off override, for example for a talk deck |

The order of precedence is: per run, then the user override, then the default.

The two-layer shape follows the repository's Style Reference: prose sections for a person, plus one fenced, machine-readable token block for the tool [SOURCE: AI Systems/Product Owner/mcp-figma/feature-catalog/design-system-extract-and-import/design-system-extract-and-import.md:27].

### 4.2 Schema

The prose comes first, in sections that mirror the style guide: Overview, Colour by meaning, The accent, Zones, Type, Spacing, Shapes, Connectors, Key, Title block and source, What the validator enforces.

The token block follows, in W3C Design Tokens Community Group shape: `$value`, `$type` and `$description`, with `{alias}` references. (This format detail was not fetched in this session.)

```jsonc
{
  "meta": { "name": "FigJam default", "extends": null, "version": "1.0.0" },
  "swatch": {                                   // FigJam's own pairs; fixed, read-only
    "lightBlue": { "$type": "pair", "$value": { "fill": "#C2E5FF", "stroke": "#3DADFF", "text": "#1E1E1E" } }
    // ... lightGreen, lightTeal, lightViolet, lightPink, lightRed, lightOrange, lightYellow, lightGray, white, black, darkGray, violet
  },
  "role": {                                     // what a user restyles
    "entry":    { "$value": "{swatch.lightBlue}" },
    "neutral":  { "$value": "{swatch.white}" },
    "goal":     { "$value": "{swatch.lightGreen}" },
    "exit":     { "$value": "{swatch.lightOrange}" },
    "error":    { "$value": "{swatch.lightRed}" },
    "decision": { "$value": "{swatch.lightYellow}" },
    "store":    { "$value": "{swatch.lightViolet}" },
    "io":       { "$value": "{swatch.lightTeal}" },
    "client":   { "$value": "{swatch.lightTeal}" },
    "external": { "$value": "{swatch.lightGray}" },
    "done":     { "$value": "{swatch.lightGray}" },
    "marker":   { "$value": "{swatch.violet}" },
    "accent":   { "$value": "{swatch.lightPink}", "weight": { "node": 8, "message": 4 } }
  },
  "kind": {                                     // structural; shape + role, validated for distinctness
    "start":       { "shape": "ROUNDED_RECTANGLE", "role": "entry", "key": "Where it starts" },
    "participant": { "shape": "ROUNDED_RECTANGLE", "role": "neutral", "key": "Participant" }
    // ... every kind in KINDS today
  },
  "ink":   { "text": "#1E1E1E", "line": "#757575", "lifeline": "#B3B3B3", "faint": "#D9D9D9" },
  "line":  { "default":  { "color": "{ink.line}", "weight": 2, "cap": "ARROW_LINES" },
             "emphasis": { "color": "{ink.text}", "weight": 2, "cap": "ARROW_EQUILATERAL" },
             "reply":    { "dash": [10, 6] }, "async": { "color": "{swatch.lightBlue.stroke}", "cap": "ARROW_LINES" } },
  "zone":  { "tintPolicy": "avoid-member-hues", "tints": ["blue", "orange", "teal", "yellow", "violet", "green"],
             "head": 96, "pad": 48, "gap": 48, "align": "row-top" },
  "type":  { "family": "Inter", "title": 64, "subtitle": 28, "zone": 24, "node": 20, "label": 18, "small": 14,
             "weights": { "title": "Bold", "zone": "Semi Bold", "node": "Medium", "body": "Regular" } },
  "space": { "grid": 8, "rankGap": 136, "crossGap": 80, "boardPad": 80, "keyGap": 64, "titleClear": 48 },
  "stroke": { "node": 2, "heavy": 4, "ring": 6 },
  "rhythm": { "sequenceRow": 72, "ganttRow": 56, "ganttBar": 32 },
  "key":   { "width": "diagram", "order": "canonical" },
  "titleBlock": { "subtitleMeasure": [960, 1440], "noOrphan": true },
  "source": { "size": "{type.label}" }
}
```

### 4.3 How each reader reads it

- **`compose_board.py`** resolves the three layers and checks the result (Section 4.4). It writes the measured ratios into a resolved theme. It fills a new `__THEME__` placeholder with only the values that differ from the default, beside `__MODEL__` [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:569-571]. Sending only the differences protects the 50,000-character call [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:347] and the under-6,400 characters left for the model [SOURCE: AI Systems/Product Owner/SYNC.md:100].
  - The `COMPOSED` line names the active spec and its hash.
  - The self-test regexes [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:700-701] read the token block instead of the JavaScript source.
- **`compose-board.js`** keeps today's values as built-in defaults and deep-merges `THEME` over them. A board drawn with no theme is therefore identical to today's board.
  - It also writes the spec hash into the shared plugin data it already sets [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1211-1214], so a revision can tell which spec drew a board.
- **`flow_check.py` / `common.py`** derive `ACCENT_PAIRS` from the resolved swatches and roles [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/common.py:47-57] instead of keeping a separate list.
- **claude.ai Project.** A Project cannot read a local file [SOURCE: AI Systems/Product Owner/SYNC.md:82].
  - Ship a Knowledge file, `Product Owner - Assets - Flow Board Design.md`, mirrored by hand from `board-design.md`.
  - The agent fills `__THEME__` by hand from any overrides the user pastes, the same way it fills `__MODEL__`.
  - The composer mirror stays byte-equal to `--template`, because only the placeholder lives in the code [SOURCE: AI Systems/Product Owner/SYNC.md:92].

### 4.4 Safe defaults when a user edits it badly

1. **Schema.** Unknown keys, wrong types and broken aliases each fall back to the default for that token only, with a warning.
2. **Palette.** A role takes a swatch by name. A raw hex is accepted only with `"offPalette": true`. The board then reports it, because a custom colour is no longer recolourable from FigJam's picker [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:206].
3. **Floors.** The existing measures are rerun on the resolved theme [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:702-727]:
   - text on every fill at 4.5:1 or better
   - the accent stroke at 3:1 or better on white
   - the accent at least 45 degrees from every role's hue and every tint's hue
   - the accent weight above every other stroke
   - the `marker` digit at 4.5:1 or better
   - type sizes within bounds: label at least 14, node 16 to 28, title at least twice the node size
   - every space and size on the grid
4. **Distinctness.** No two kinds a type can draw may share both shape and role. If they do, the change to the kind mapping is refused and the default is used.
5. **Fallback.** A role that fails reverts to its default role while the rest of the theme stands. Each reverted token is named in the `COMPOSED` line and in the reply's `Finding:` line. A theme can never ship a board that fails the greyscale or first-glance rules [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:92].

### 4.5 How the rubric and the scorecard check a board against it

- **Rubric.** Add the ninth criterion from change 12 to Section 7 of the quality rubric: the board matches the active spec's key order, title block, line roles and tint rule. Add Section 6 checklist lines:
  - every fill on the board resolves to a spec role
  - no tint shares a hue with a kind inside it or with the accent
- **Scorecard.** Signal scores against the active spec's roles instead of the fixed palette text. Its allowed tint list comes from the spec [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:95-101].
- **New playbook scenarios:**
  1. a family scenario that composes the seven example models under the default spec and checks that key order, title block and line roles match
  2. a broken-override scenario (pink tint, white text on a light fill, unknown key) that expects named fallbacks and an unchanged first glance
- **Self-test.** It composes every shipped example under the default spec and under a sample override, and fails if a floor is crossed.

## 5. Open questions for the merge

- Whether a lineage with access confirms the sk-design-md-generator section list and the DTCG field names. The recommendation depends only on the two-layer shape, which the in-repo `mcp-figma` docs confirm.
- Whether the user override belongs at the system root or in a gitignored local folder, as the ClickUp push targets do. That depends on whether restyling is a team choice or a personal one.
