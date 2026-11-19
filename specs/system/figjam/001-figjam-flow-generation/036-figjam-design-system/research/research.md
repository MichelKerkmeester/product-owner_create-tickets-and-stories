# FigJam Board Design and a User-Editable Design Spec: Research Synthesis

This synthesis merges the three lineages of fan-out run 1792955293904-icey00 on one question: how the boards `sk-create-figjam` composes can look better and stay consistent across all seven diagram types, and whether the packet should read a design spec file a repository user can edit. Every item is a proposal. Phase decision D1 freezes this phase as findings only [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/036-figjam-design-system/goal.md:44].

Every iteration claim used below was checked against its cited line before use, and every visual claim against the PNG it names. Claimed absences were searched for first. Section 2 gives the counts and Section 8 lists each correction and drop.

---

## 1. Summary

### What the boards do well today (keep all of it)

- **One entry for every type.** A white framed section, a 64 px Bold title, a 28 px Regular subtitle and 80 px margins open every board [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1125-1139]. All nine screenshots show it, and it is the main reason the seven types read as one family.
- **Colour by kind, never by hand.** A kind fixes shape and colour together [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:50-83], and a `style` line is read as meaning, not paint [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:122-133]. The process example styles its focus step with the orange pair, and `process-board.png` still draws it light pink, which is that rule working.
- **A key built from what the board draws** and nothing else [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:851-854] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1142-1194].
- **One accent that wins by weight as well as hue.** An 8 px pink outline against 2 px elsewhere, 3.13:1 on white, 25.0 weight times contrast against 12.6 for the next mark [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:137-143]. It reads first on `user-flow-board.png`, `process-board.png`, `architecture-board.png`, `er-board.png`, `gantt-board.png`, `dense-flow-board.png` and `state-on-existing-board.png`, and as a 4 px message on `sequence-board.png`.
- **A straight spine with exits beside it** [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:318-327]. `user-flow-board.png` and `dense-flow-board.png` read left to right with no backtracking.
- **FigJam swatches written as hex/255,** so anyone on the board can recolour from the picker [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:26] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:156].
- **An 8 px grid with one size per shape class,** so a rank reads as one row [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:568-579].
- **A port-pricing router** that keeps labels mid-run and clear of boxes and zone titles on almost every board [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:600-610].
- **A measured palette.** The self-test re-measures contrast and the accent's hue distance and mark gate [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:712-727]. It ran 815 of 815 passed during this synthesis.
- **A source line that names its sources and what was left out,** on every screenshot.

### The main weaknesses

1. **The accent's hue leaks into zone tints.** `TINT_CYCLE` ends in `pink` [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:48]. The pink tint `#FFF0FA` sits at about 320 degrees, one degree from the accent stroke's 319. `architecture-board.png` draws the External lane pink beside the pink sync-service. The self-test passes with it, because it checks kinds and never tints.
2. **Zone tints are positional, so they collide with kind hues.** An orange exit sits in an orange zone on `user-flow-board.png`, a violet store in a violet lane on `architecture-board.png` and a light blue start in a blue lane on `process-board.png`.
3. **Light blue means five things across types:** start, gateway, first state, participant and in progress. On `sequence-board.png` eight light blue pills outweigh the pink focus message.
4. **The seven types drift where they should match.** Key order, key width, connector colour and head, zone top lines and the smallest text size each follow a different rule per type or per model.
5. **Small text and loose geometry.** 16 px edge labels and 14 px bar and pin text are hard to read on wide boards. Routes can climb into the subtitle band and the board margin. Zone tops are ragged on group-mode boards.
6. **The design lives in three hand-kept copies:** the composer literals, the check's pairs in `common.py` and the style guide's palette table, plus the Project mirror. Nothing grades a board against a declared style or against its siblings.

### Headline recommendation

Fix the four cross-type defects first (pink out of the tints, one tint rule, one meaning per colour, one key order), because each is a few lines and shows on every board. Then add one packet-level design spec, `sk-create-figjam/assets/figjam-design.md`, written as a smaller FigJam form of the DESIGN.md Style Reference: Style Reference prose sections plus one strict JSON token block. Its default holds today's values exactly, so adding it changes no board. A user restyles through an optional override at `AI Systems/Product Owner/figjam-design.md`. `compose_board.py` validates the merge and sends only the changed tokens to the composer through a `__THEME__` placeholder, and the self-test pins the composer's built-in defaults to the spec. Section 6 has the full design.

---

## 2. Method

| Lineage | Executor and model | Iterations | What it covered |
|---|---|---|---|
| opus | Claude Code, Claude Opus 5.5 at medium effort | 3 | Iteration 1 audited the composer tokens and all nine PNGs. Iteration 2 traced the design into `compose_board.py`, `common.py`, the type references, the scorecard and the Project mirror. Iteration 3 read the Style Reference as `mcp-figma` describes it and the gantt and sequence code. It could not read `sk-design-md-generator` or the web, and wrote no findings registry |
| swe | Devin, SWE 2 max | 2 | Iteration 1 inventoried the composer surface and viewed seven PNGs. Iteration 2 read `sk-design-md-generator`, `compose_board.py` and `common.py`, and fetched Google's DESIGN.md spec and the W3C Design Tokens report |
| luna | Codex, GPT-6 Luna at max effort on the fast tier | 2 | Iteration 1 set the shared visual grammar and the score scopes. Iteration 2 designed the Style Reference contract, the parity path and spec grading, and read public DESIGN.md examples |

[SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/036-figjam-design-system/research/fanout-attribution.md:5-9] lists opus with 0 iterations because it wrote no registry. Its three iteration files exist and were used. The merged registry holds 45 findings from swe and luna only [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/036-figjam-design-system/research/findings-registry.json].

**Verification.** The seven iterations carry 75 numbered findings: opus 30, swe 30, luna 15. Each was checked against its cited line, a grep for any claimed absence, the PNG it names or, for two outside sources, a fetch.

| Result | Count | Meaning |
|---|---|---|
| Verified | 58 | The cited line or image shows what the claim says |
| Corrected | 15 | The core holds and a detail, a cause or a citation was wrong. Each is fixed below and listed in Section 8 |
| Dropped | 2 | The core does not hold. Listed in Section 8 |

This synthesis also added eight observations of its own, marked **(synthesis)**. Checks run here: `compose_board.py --self-test`, 815 of 815 passed, exit 0. `compose_board.py --template` measures 43,624 characters, which leaves about 6,376 of the 50,000 one `use_figma` call takes [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:75-76]. The W3C Design Tokens Community Group final report and Google's `design.md` repository were fetched. No packet file was edited.

---

## 3. Visual audit

Read at the rendered size each PNG ships at, as an overview. Pixel figures are on the render and scale with it.

### Per screenshot

**`user-flow-board.png`** (21 of 22)
- Hierarchy holds: title, then the pink Return confirmed, then the light blue Order list. The spine runs straight through two decisions.
- Zone tops are ragged: Request the return starts about 30 px above Find the order and Done. The orange Contact support exit sits inside the orange-tinted Request the return zone, so orange says "this zone" and "leaves the flow" at once.
- Edge labels (Yes, No, Courier pickup, Drop-off point) and key entries are the smallest text on the board, a 4 to 1 drop from the title. The key spans about 60% of the width and leaves an empty block to its right.

**`process-board.png`** (21 of 22)
- Three full-width lanes give a clear structure. The light blue start sits in the light blue Customer lane, so the entry colour is muted by its own tint.
- Density is uneven: the left half of the Warehouse operator lane and the right half of the CS agent lane are empty, while Claim queued runs one long vertical trunk across a lane boundary.
- Two edges into Damage clear? arrive side by side on the left magnet about 80 px apart, which reads as a double line.

**`architecture-board.png`** (21 of 22)
- Six lanes start at five different top lines (Clients, Edge and Services, Events, Stores, External), so the board reads as scattered boxes rather than columns.
- The External lane is pink-tinted with a pink border on the same board as the pink-outlined sync-service, which dilutes the one accent. The violet Blocks Database sits in a violet Stores lane.
- The subtitle leaves "Engineering" alone on its second line. The key holds nine entries in one row and runs almost the full board width. Writes Blocks climbs over the Events lane and drops into Stores.

**`sequence-board.png`** (19 of 22, the lowest)
- Eight identical light blue participant pills, head and foot, are the heaviest marks on the board and compete with the 4 px pink Authorise the card.
- The violet step pins sit at the left edge about 150 px from the first lifeline, so the eye jumps between the number and its message **(synthesis)**.
- PartnerHub's lifeline carries one message, so the right quarter is empty. Requests are near-black with closed heads, unlike the gray open-head connectors on every other type. The subtitle leaves "engineers" alone on line 2.

**`state-board.png`** (22 of 22)
- No accent is set, so the first glance falls on the light blue Pending and the Confirmed zone. That is allowed, since focus is optional for state [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:148].
- check out runs above the Confirmed zone about 43 px under the subtitle. card authorised leaves the 80 px board margin and runs about 25 px from the board's left edge **(synthesis)**.
- missed check-in sits on the Confirmed zone's bottom-right corner **(synthesis)**. The key reads Final state, State, Start, First state, End and spans just over half the width.

**`er-board.png`** (22 of 22)
- The flattest type: white cards with gray strokes, so hierarchy rests on the bold card title and the pink Booking. That restraint reads well.
- Card tops are ragged in the Guest side row: Guest, Booking and Payment start at three heights because each is centred on its rank. makes (1 to 0..n) jogs up and over into Booking's top, because Booking's left magnet is taken by is reserved by.
- The three-entry key leaves more than half the key row empty, and relationships carry cardinality only as label text.

**`gantt-board.png`** (21 of 22)
- Planned bars are white with a thin gray stroke, so the chart reads hollow until the critical bar.
- Section bands are tinted blue, orange and teal by position, and mean nothing [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:97]. "1 week, critical" at 14 px is the smallest text on the board.
- The key's In focus sample is light pink while the marked bar is light red under the pink outline. The code draws the sample as the marked task's own kind [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1061] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1164], so this screenshot likely predates that code **(synthesis, inferred)**.

**`dense-flow-board.png`** (21 of 22)
- The pink decision diamond reads first and the spine stays straight through nine nodes.
- Settle the price starts about 90 px above Find a room. Yes climbs out over its decision and back down into the next zone.
- Seven edge labels at 16 px render tiny on this 2048 px export. The key covers about 40% of the width with empty space to its right and below Find a room.

**`state-on-existing-board.png`** (22 of 22)
- The pink Completed reads first, and the board placed itself beside existing content without overlap.
- Its key order is Start, First state, State, End, Final state, In focus. That is the same type as `state-board.png` in a different order.
- card authorised and guest cancels run long perimeter loops, one about 43 px under the subtitle and one down the right edge.

### Cross-type consistency

Where the seven types differ when they should not:

| Aspect | User flow | Process | Architecture | Sequence | State | ER | Gantt |
|---|---|---|---|---|---|---|---|
| Light blue means | Start | Start | Edge or gateway | Participant | First state | Not used | In progress |
| Zone or band tint | Position in cycle | Position in cycle | Position in cycle, sixth is pink | No zones | Position in cycle | Position in cycle | Position in cycle |
| Key order | Model order | Model order | Model order | Participant, arrows used, pin | Model order | Model order | Fixed order |
| Connector look | Gray 2 px, open head | Gray 2 px, open head | Gray 2 px, open head | Near-black, closed head | Gray 2 px, open head | Gray 2 px, no head | No connectors |
| Smallest text | 16 px label | 16 px label | 16 px label | 14 px pin | 16 px label | 16 px field | 14 px bar text |
| Zone top line | Fit to members | Shared lane | Fit to members | No zones | Fit to members | Fit to members | Shared band |
| Key width | Content | Content | Content | Content | Content | Content | Content |

Sources for the rows: [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:52] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:65] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:70] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:77] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:79] for light blue, [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:593] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1087] for tints, [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:851-853] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:966] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1059] for key order, [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:218-220] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:921-927] for connectors, [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:90] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1008] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1101-1102] for type, [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:496-509] for zone tops and [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1194] for key width.

What is rightly different and should stay: sequence's dashed lifelines and numbered pins, gantt's time axis and grid rules, state's ringed end dots and composite zones, ER's field cards and headless relationship lines and architecture's fixed lane order. Those are each type's vocabulary. The furniture, the meaning of a colour, the key's order rule and width, the line language and the type steps are not, and they are where the drift sits.

---

## 4. Ranked design changes

Rank weighs how much a change shows on the board, how many types it reaches, its risk and its cost. **[C]** marks a change about consistency across diagram types. Eight of the eighteen carry it. Lineage letters: O is opus, S is swe and L is luna.

### Rank 1. Take pink out of the zone tints and make the self-test check tints [C]

- **Change:** drop `pink` from `TINT_CYCLE`, change the tint row of the style guide and the graders' allowed cycle and add a tint hue check beside the accent checks
- **Files:** `assets/compose-board.js` line 48, `references/style-guide.md` Section 2 line 93, `manual-testing-playbook/manual-testing-playbook.md` line 97, `scripts/compose_board.py` lines 712-727
- **Evidence:** [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:48] against "The only pink and the only heavy line on a board" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:91]. The guide's own zone row lists pink in the cycle [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:93], so the record contradicts itself. The self-test reads kinds only and passed 815 of 815 with the pink tint present. `architecture-board.png`
- **Visible effect:** the sixth zone or gantt section takes a non-pink tint, and pink again means the first glance only
- **Risk:** low. The cycle gets five tints, so a sixth zone repeats the first. Neighbours still differ
- **Raised by:** O, S

### Rank 2. Tint zones and gantt bands by one rule: a hue no member kind draws, never the accent's [C]

- **Change:** pick each zone's tint from the cycle skipping any hue a node inside it draws, using the `tint` field the composer already reads and nothing sets
- **Files:** `assets/compose-board.js` lines 593 and 1087, `references/style-guide.md` Section 2, `references/quality-rubric.md` line 133
- **Evidence:** the tint is positional [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:593] and `compose_board.py` never writes `tint` (grep finds it only in the docstring). Gantt reuses the cycle [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1087]. `user-flow-board.png`, `architecture-board.png`, `process-board.png`
- **Visible effect:** no orange exit in an orange zone and no violet store in a violet lane, so hue keeps one job
- **Risk:** low. Tints still alternate, and the rubric's "neighbouring tints differ" holds
- **Raised by:** O

### Rank 3. Give each colour one meaning across all seven types [C]

- **Change:** keep light blue as `entry` (start and first state). Draw participants white with the neutral stroke. Record gateway and in progress as named roles in the style guide, or move in progress to a pair no other entry kind uses
- **Files:** `assets/compose-board.js` lines 51-83, `references/style-guide.md` Section 2 lines 70-79, `references/types/sequence.md` line 54
- **Evidence:** five kinds draw light blue [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:52] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:65] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:70] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:77] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:79] against "a colour means the same thing on every board" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:32]. `sequence-board.png`
- **Visible effect:** the sequence board's first glance moves to the pink message, and light blue reads as "start here" everywhere
- **Risk:** medium. It changes the look of every sequence board and the gallery
- **Raised by:** O

### Rank 4. Make one design spec the single source of the board's style [C]

- **Change:** add `assets/figjam-design.md` holding today's values, pin the composer's literals to it in the self-test, derive the check's accepted pairs from it and send a user override through `__THEME__` (Section 6)
- **Files:** new `sk-create-figjam/assets/figjam-design.md`, `scripts/compose_board.py` lines 69-76, 569-571 and 700-727, `scripts/figjam_checks/common.py` lines 47-61, `assets/compose-board.js` line 15, `references/style-guide.md` lines 18 and 210-215
- **Evidence:** the guide calls itself "The one source" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:18] while naming two other holders [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:212-213]. The self-test regex-parses the JavaScript [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:700-701]. The check keeps its own pairs [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/common.py:47-61]
- **Visible effect:** none at first, by design. Ranks 1 to 3 and 5 then stay fixed because a drift fails the self-test, and a user can restyle every board in one place
- **Risk:** medium. It adds a file to the Project mirror and one step to the kernel's composer instructions
- **Raised by:** O, S, L

### Rank 5. Give the key one fixed order per type [C]

- **Change:** sort key entries by a canonical role order per type (entry, steps, decision, goal, exit, error, stores, then lines, then In focus), as gantt already does
- **Files:** `assets/compose-board.js` lines 851-854 and 966
- **Evidence:** first-use order [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:851-853] against gantt's fixed list [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1059]. `state-board.png` and `state-on-existing-board.png` key one type in two orders
- **Visible effect:** two boards of one type have identical keys, and the key reads in the order a reader meets the diagram
- **Risk:** low
- **Raised by:** O

### Rank 6. Line up zone tops on group-mode boards

- **Change:** zones that sit in one row share their top edge in LR mode and their left edge in TB mode
- **Files:** `assets/compose-board.js` lines 496-509
- **Evidence:** each zone box fits its own members [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:496-509]. `user-flow-board.png` about 30 px, `dense-flow-board.png` about 90 px, `architecture-board.png` five top lines
- **Visible effect:** zones read as one row of columns, and the grid the rest of the board keeps holds at the top
- **Risk:** low to medium. Taller zones may widen the routing gaps the router prices
- **Raised by:** O

### Rank 7. Raise edge label, key and source text to 18 px and add a `small` step

- **Change:** `TYPE.label` from 16 to 18, a `TYPE.small` of 14 for bar text and pins in place of the literal 14s and label size scaled up past a 1,600 px wide body if 18 still reads small
- **Files:** `assets/compose-board.js` lines 90, 1008, 1101-1102 and 1174, `references/style-guide.md` Section 5 lines 193-200
- **Evidence:** [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:90] and the magic 14s [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1101-1102]. The rubric judges legibility at overview zoom [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:134]. `user-flow-board.png`, `dense-flow-board.png`, `gantt-board.png`
- **Visible effect:** Yes, No and branch labels survive the overview zoom on wide boards
- **Risk:** medium. Wider labels widen rank gaps [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:434-435], so dense boards grow and the layout budgets need a re-check
- **Raised by:** O

### Rank 8. Keep every route inside the diagram's box

- **Change:** add the subtitle band and the board margin as blocked regions the router prices, using the offset above the body
- **Files:** `assets/compose-board.js` lines 609-627 and 1138-1139, `references/style-guide.md` line 234
- **Evidence:** the router knows zone heads and rims but not the board title [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:617-627], and the body starts 64 px under the subtitle [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1139]. `state-board.png` (check out under the subtitle, card authorised inside the margin), `state-on-existing-board.png`, `architecture-board.png`
- **Visible effect:** the title block stands clear and the 80 px margin is even on all four sides
- **Risk:** low to medium. Some back edges take a longer path
- **Raised by:** O, L (long perimeter returns), synthesis (margin)

### Rank 9. Give the key the diagram's width and wrap it there [C]

- **Change:** the key section spans the body width, and entries wrap to a second row past it instead of running on
- **Files:** `assets/compose-board.js` lines 1147-1148 and 1158-1194
- **Evidence:** the key is sized to its content [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1194] from one cursor [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1158]. Empty regions on `state-board.png`, `er-board.png`, `gantt-board.png` and `dense-flow-board.png`, and a near board-wide key on `architecture-board.png`. The rubric penalises a large empty region [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:137]
- **Visible effect:** the key aligns with the diagram's edges on every type
- **Risk:** low
- **Raised by:** O, S

### Rank 10. Define the connector language once [C]

- **Change:** name connector roles (`default`, `emphasis`, `reply`, `async`, `relationship`, `lifeline`) with colour, weight, dash and caps, and let each type pick from them. Sequence requests take `default` gray with a closed head, so the head carries the request and reply difference and the colour stops changing family
- **Files:** `assets/compose-board.js` lines 210-229, 921-927 and 1151-1157, `references/style-guide.md` Section 2 lines 85-92
- **Evidence:** graph edges default to gray with open heads [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:218-220], sequence requests are near-black with closed heads [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:921-927]. `sequence-board.png` beside `user-flow-board.png`
- **Visible effect:** the sequence board stops reading darker and heavier than its siblings
- **Risk:** low. Head shape and dash still tell request, reply and async apart
- **Raised by:** O, S, L

### Rank 11. Lighten the sequence board

- **Change:** draw participant feet as a lighter, smaller echo of the head, set step pins beside the first lifeline rather than at the board's left edge and size rows to the tallest label instead of a fixed 72 px
- **Files:** `assets/compose-board.js` lines 933-962, 970-978 and 1008
- **Evidence:** head and foot are identical shapes [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:972-973], pins sit at `ox + 8` [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1008] and `ROW` is fixed [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:957]. `sequence-board.png`, the gallery's lowest score [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/screenshots/README.md:28]
- **Visible effect:** half the participant weight, numbers next to the messages they number and a shorter board
- **Risk:** low. The read-back counts heads by `node:` name, and feet are named `foot:` [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:973]
- **Raised by:** S, L, synthesis (pins)

### Rank 12. Give gantt planned bars a visible stroke

- **Change:** draw planned bars with the `#757575` line gray as their stroke, keeping the white fill that means planned
- **Files:** `assets/compose-board.js` line 78 and the planned row of `references/style-guide.md` line 78
- **Evidence:** planned is white with the `#B3B3B3` stroke [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:28] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:78]. `gantt-board.png` reads hollow
- **Visible effect:** bars read as scheduled work at overview zoom
- **Risk:** low. It needs its own pair entry, since the white pair's stroke serves every white node
- **Raised by:** S (who proposed a fill, see Section 7)

### Rank 13. Top-align ER cards within a rank

- **Change:** place entity cards in one rank on a shared top line rather than a shared centre
- **Files:** `assets/compose-board.js` lines 451-456
- **Evidence:** every box is centred on its rank [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:453-455] and card height follows field count [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:547-555]. `er-board.png`
- **Visible effect:** card titles align across a row. The makes jog stays, because its cause is the taken magnet, not the alignment
- **Risk:** low
- **Raised by:** O

### Rank 14. Wrap the subtitle with no one-word last line

- **Change:** when the last line holds one word, rewrap at a narrower measure inside the 960 to 1440 band
- **Files:** `assets/compose-board.js` line 1131
- **Evidence:** [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1131]. "Engineering" on `architecture-board.png`, "engineers" on `sequence-board.png`
- **Visible effect:** a balanced two-line subtitle
- **Risk:** low. It costs one extra text measurement
- **Raised by:** O

### Rank 15. Grade family consistency and spec conformance [C]

- **Change:** add a ninth rubric criterion, "Matches the active design": key order, title block, line roles and tint rule as the spec sets them. Point the scorecard's Signal at the resolved spec, and add one board-quality scenario that composes all seven examples under one spec and compares their furniture
- **Files:** `references/quality-rubric.md` Section 7 lines 126-139, `manual-testing-playbook/manual-testing-playbook.md` lines 81-114, a new scenario under `manual-testing-playbook/board-quality/`
- **Evidence:** the eight criteria score one board at a time [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:126] and the scorecard's dimensions hold no cross-type check [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:81-93]
- **Visible effect:** none on a board. Drift such as Rank 5's becomes a lost point
- **Risk:** low. The rubric total moves from 16 to 18
- **Raised by:** O, L

### Rank 16. Cut the colour prose in the type references to role mappings and a pointer

- **Change:** each type's board paragraph names which roles it draws and points to the style guide for the colours
- **Files:** `references/types/user-flow.md` line 49, `state.md` line 54, `gantt.md` line 53, `sequence.md` line 54, `architecture.md` lines 16 and 53, `process.md` line 97, plus their Project mirrors
- **Evidence:** each restates colours the style guide owns. The zone wording differs three ways: "colours it by that lane" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/architecture.md:16], "each lane gets its own tint" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/process.md:97] and "one neutral tint" for the check's lane pair [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/common.py:59-61]
- **Visible effect:** none. A restyle then edits one file
- **Risk:** low
- **Raised by:** O

### Rank 17. Give the sequence step pin its own `marker` role

- **Change:** name the pin pair as a role so remapping `store` never recolours pins, and keep the 4.5:1 white digit floor on that role
- **Files:** `assets/compose-board.js` lines 1009-1012 and 1174-1177
- **Evidence:** the pin draws the saturated violet pair [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1009-1012], whose fill is the data store's stroke [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:37]. It was chosen for its 4.57:1 white digit [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:174]
- **Visible effect:** none today
- **Risk:** low
- **Raised by:** O

### Rank 18. Measure the gantt section name at the size it is drawn, and re-render the gantt screenshot

- **Change:** measure section labels with `SEMI` at `TYPE.zone`, which is how `zoneSection` draws them, and re-render `gantt-board.png` from the current composer
- **Files:** `assets/compose-board.js` line 1030, `assets/screenshots/gantt-board.png`
- **Evidence:** the name column measures at `TYPE.node` [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1030] while the label is drawn at `TYPE.zone` [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:239], so a long section name can run 20% past its column. The gallery's key sample disagrees with the code, as Section 3 notes
- **Visible effect:** no section name crowds the first bar, and the gallery shows what the composer draws
- **Risk:** low
- **Raised by:** synthesis

---

## 5. What the iterations disagreed on, and how this synthesis settled it

- **Bad edits: fall back per token or refuse.** Opus and swe fall back per token and never fail a board. Luna fails closed on any invalid file. Settled as two tiers in Section 6.6: a malformed or unknown override refuses before the call, and a value that only misses a floor reverts that one token and names it.
- **Location.** Opus puts the default under `assets/` with a system-root override. Swe and luna put it at the packet root, luna as `DESIGN.md`. Settled for `assets/figjam-design.md` plus the system-root override, because a packet-root `DESIGN.md` borrows the name of an artifact `sk-design-md-generator` owns and validates as measured.
- **Token syntax.** Swe prefers YAML. Opus and luna prefer one JSON block. Settled for JSON: the packet's scripts import only the Python standard library, which has `json` and no YAML parser [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:45-53].
- **Score totals.** Luna adds fidelity to both the rubric and the scorecard (18 and 24). Settled for the rubric only (Rank 15), with Signal on the scorecard reading the spec, so the 22-point gallery stays comparable. Open question 3 asks the operator.

---

## 6. Design spec file recommendation

### 6.1 Name, location and precedence

| Layer | Path | Holds |
|---|---|---|
| Packet default | `AI Systems/Product Owner/sk-create-figjam/assets/figjam-design.md` | Every token at today's value. Shipped, complete and tracked. The self-test pins the composer's literals to it |
| System override | `AI Systems/Product Owner/figjam-design.md`, beside `AGENTS.md`, optional | Only the tokens a team changes, with `"extends": "default"` |
| Per run | `compose_board.py <model.md> --design <path>` | A one-off override, such as a talk deck |

Precedence is per run, then the system override, then the packet default, resolved token by token. Repository level is out: the repository holds many systems, and a root `DESIGN.md` would collide with the artifact `sk-design-md-generator` owns. `style-guide.md` keeps the reasons, and its `FIGJAM_PALETTE` table stays as the measured record the self-test checks against the spec.

### 6.2 Relation to the DESIGN.md Style Reference

D5 models this file on the Style Reference [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/036-figjam-design-system/goal.md:48]. Reuse its shape, not its whole format:

- **Keep:** the header with a one-line tagline and theme, the intro paragraph, the named-token tables for colours, typography and spacing and shapes, Components (here node kinds, connectors, zones, key and title block), Do's and Don'ts, Surfaces (frame, zone, key) and Elevation, which is "flat" here.
- **Replace:** the Quick Start CSS and Tailwind blocks [SOURCE: .skilled/skills/sk-design/sk-design-md-generator/references/design-md-format.md:311-356] with one fenced `json` block the scripts read. A FigJam board has no CSS.
- **Drop:** Imagery, Motion, Similar Brands and the Agent Prompt Guide's component prompts.
- **Why a smaller form:** the v3 format's first cardinal rule copies every value verbatim from a measured `tokens.json` [SOURCE: .skilled/skills/sk-design/sk-design-md-generator/references/design-md-format.md:30-31], and the generator refuses to author from a brief [SOURCE: .skilled/skills/sk-design/sk-design-md-generator/SKILL.md:46]. This file is authored defaults for a drawing surface, so running it through that validator would fail by design. The Style Reference's "measured" property carries over as the self-test re-measuring every colour token on each run.
- **Token shape:** each token follows the Design Tokens Community Group format, `$value` with optional `$type` and `$description`, and aliases in curly braces. Its final report dates from 28 October 2025 and says it "is not a W3C Standard". The packet borrows the shape and validates its own bounded schema.

### 6.3 Schema

Three colour tiers. **Swatches** are FigJam's own fill, stroke and text pairs and are read-only. **Roles** say what a colour means and alias a swatch. That is the layer a user restyles. **Kinds** fix shape and role and are structural. Every group below is optional in an override, and a missing token falls back to the default.

| Group | Tokens |
|---|---|
| `meta` | `name`, `schemaVersion`, `extends` |
| `swatch` | each FigJam pair as `{ fill, stroke, text }`, the light tint as `fill` and the dark as `stroke`. Read-only |
| `role` | `entry`, `neutral`, `goal`, `exit`, `error`, `decision`, `store`, `io`, `client`, `gateway`, `external`, `inProgress`, `done`, `terminal`, `junction`, `marker`, each aliasing a swatch |
| `accent` | the first-glance pair, `nodeWeight`, `messageWeight` |
| `kind` | each composer kind with `shape`, `role`, `fixed` size where set, `stroke` override (`heavy`, `ring`) and its key words |
| `ink` | `text`, `line`, `lifeline`, `faint`, `canvas` |
| `type` | `family`, a size and weight per step: `title`, `subtitle`, `zone`, `node`, `label`, `field`, `small` |
| `space` | `grid`, `rankGap`, `crossGap`, `zoneGap`, `zoneHead`, `zonePad`, `boardPad`, `titleGap`, `bodyGap`, `keyGap`, `sourceGap`, `para` |
| `rhythm` | `sequenceRow`, `sequenceSelfDrop`, `ganttRow`, `ganttBar`, `ganttHead`, `ganttAxis` |
| `stroke` | `node`, `heavy`, `ring`, `connector`, `accentNode`, `accentMessage` |
| `radius` | `node`, documented as FigJam-native and fixed, since the composer sets no radius today |
| `connector` | per role: `color`, `weight`, `dash`, `startCap`, `endCap`, plus `label` with its size and weight. Labels use FigJam's own chip, so no chip colour is set |
| `zone` | `tints`, `tintPolicy` (`cycle` or `avoid-member-hues`), `align` (`fit` or `row-top`), `label` type step |
| `key` | `fill`, `title`, `width` (`content` or `diagram`), `order` (`first-use` or `canonical`), `sample` sizes |
| `titleBlock` | `title` and `subtitle` type steps, `measure` as `[960, 1440]`, `noOrphan` |
| `source` | type step and its gap above |
| `frame` | `fill`, `margin` |

Out of scope by design: the router's cost constants, the layout algorithm, which kinds the key includes and the spacing bands for people and notes [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:609-611] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:221-234]. Exposing them would let a user break invariants they cannot see.

### 6.4 Filled example at today's values

Every value below is today's, so a board composed under this file is identical to today's board. Ranks 1, 5 and 9 each become a one-token change: drop `pink` from `zone.tints`, `key.order` to `canonical` and `key.width` to `diagram`.

```json
{
  "meta": { "name": "FigJam default", "schemaVersion": 1, "extends": null },
  "swatch": {
    "white":       { "$type": "pair", "$value": { "fill": "#FFFFFF", "stroke": "#B3B3B3", "text": "#1E1E1E" } },
    "black":       { "$type": "pair", "$value": { "fill": "#1E1E1E", "stroke": "#B3B3B3", "text": "#FFFFFF" } },
    "darkGray":    { "$type": "pair", "$value": { "fill": "#757575", "stroke": "#5E5E5E", "text": "#FFFFFF" } },
    "violet":      { "$type": "pair", "$value": { "fill": "#874FFF", "stroke": "#5427B4", "text": "#FFFFFF" } },
    "lightBlue":   { "$type": "pair", "$value": { "fill": "#C2E5FF", "stroke": "#3DADFF", "text": "#1E1E1E" } },
    "lightGreen":  { "$type": "pair", "$value": { "fill": "#CDF4D3", "stroke": "#66D575", "text": "#1E1E1E" } },
    "lightYellow": { "$type": "pair", "$value": { "fill": "#FFECBD", "stroke": "#FFC943", "text": "#1E1E1E" } },
    "lightOrange": { "$type": "pair", "$value": { "fill": "#FFE0C2", "stroke": "#FF9E42", "text": "#1E1E1E" } },
    "lightRed":    { "$type": "pair", "$value": { "fill": "#FFCDC2", "stroke": "#FF7556", "text": "#1E1E1E" } },
    "lightViolet": { "$type": "pair", "$value": { "fill": "#DCCCFF", "stroke": "#874FFF", "text": "#1E1E1E" } },
    "lightPink":   { "$type": "pair", "$value": { "fill": "#FFC2EC", "stroke": "#F849C1", "text": "#1E1E1E" } },
    "lightTeal":   { "$type": "pair", "$value": { "fill": "#C6FAF6", "stroke": "#5AD8CC", "text": "#1E1E1E" } },
    "lightGray":   { "$type": "pair", "$value": { "fill": "#D9D9D9", "stroke": "#B3B3B3", "text": "#1E1E1E" } }
  },
  "role": {
    "entry":      { "$value": "{swatch.lightBlue}", "$description": "Where a reader starts" },
    "neutral":    { "$value": "{swatch.white}" },
    "goal":       { "$value": "{swatch.lightGreen}" },
    "exit":       { "$value": "{swatch.lightOrange}" },
    "error":      { "$value": "{swatch.lightRed}" },
    "decision":   { "$value": "{swatch.lightYellow}" },
    "store":      { "$value": "{swatch.lightViolet}" },
    "io":         { "$value": "{swatch.lightTeal}" },
    "client":     { "$value": "{swatch.lightTeal}" },
    "gateway":    { "$value": "{swatch.lightBlue}" },
    "external":   { "$value": "{swatch.lightGray}" },
    "inProgress": { "$value": "{swatch.lightBlue}" },
    "done":       { "$value": "{swatch.lightGray}" },
    "terminal":   { "$value": "{swatch.black}" },
    "junction":   { "$value": "{swatch.darkGray}" },
    "marker":     { "$value": "{swatch.violet}", "$description": "Sequence step pins, white digit at 4.57:1" }
  },
  "accent": { "pair": "{swatch.lightPink}", "nodeWeight": 8, "messageWeight": 4 },
  "kind": {
    "start":       { "shape": "ROUNDED_RECTANGLE", "role": "entry", "key": "Where it starts" },
    "screen":      { "shape": "ROUNDED_RECTANGLE", "role": "neutral", "key": "Screen or step" },
    "decision":    { "shape": "DIAMOND", "role": "decision", "key": "Decision" },
    "success":     { "shape": "ROUNDED_RECTANGLE", "role": "goal", "key": "Goal reached" },
    "exit":        { "shape": "ROUNDED_RECTANGLE", "role": "exit", "key": "Leaves the flow" },
    "datastore":   { "shape": "ENG_DATABASE", "role": "store", "key": "Data store" },
    "final":       { "shape": "ELLIPSE", "role": "terminal", "key": "End", "fixed": [32, 32], "stroke": "ring" },
    "participant": { "shape": "ROUNDED_RECTANGLE", "role": "entry", "key": "Participant" },
    "crit":        { "shape": "ROUNDED_RECTANGLE", "role": "error", "key": "Critical, heavy outline", "stroke": "heavy" },
    "...":         "every other kind in compose-board.js lines 51-83, each with its shape, role and key words"
  },
  "ink": { "text": "#1E1E1E", "line": "#757575", "lifeline": "#B3B3B3", "faint": "#D9D9D9", "canvas": "#FFFFFF" },
  "type": {
    "family": "Inter",
    "title":    { "size": 64, "weight": "Bold" },
    "subtitle": { "size": 28, "weight": "Regular" },
    "zone":     { "size": 24, "weight": "Semi Bold" },
    "node":     { "size": 20, "weight": "Medium" },
    "label":    { "size": 16, "weight": "Medium" },
    "field":    { "size": 16, "weight": "Regular" },
    "small":    { "size": 14, "weight": "Medium" }
  },
  "space": { "grid": 8, "rankGap": 136, "crossGap": 80, "zoneGap": 48, "zoneHead": 96, "zonePad": 48,
             "boardPad": 80, "titleGap": 16, "bodyGap": 64, "keyGap": 64, "sourceGap": 32, "para": 4 },
  "rhythm": { "sequenceRow": 72, "sequenceSelfDrop": 40, "ganttRow": 56, "ganttBar": 32, "ganttHead": 72, "ganttAxis": 56 },
  "stroke": { "node": 2, "heavy": 4, "ring": 6, "connector": 2, "accentNode": 8, "accentMessage": 4 },
  "radius": { "node": "figjam-native" },
  "connector": {
    "default":      { "color": "{ink.line}", "weight": 2, "dash": [], "startCap": "NONE", "endCap": "ARROW_LINES" },
    "optional":     { "color": "{ink.line}", "weight": 2, "dash": [10, 6], "endCap": "ARROW_LINES" },
    "relationship": { "color": "{ink.line}", "weight": 2, "endCap": "NONE" },
    "request":      { "color": "{ink.text}", "weight": 2, "endCap": "ARROW_EQUILATERAL" },
    "reply":        { "color": "{ink.line}", "weight": 2, "dash": [10, 6], "endCap": "ARROW_EQUILATERAL" },
    "async":        { "color": "{swatch.lightBlue.stroke}", "weight": 2, "endCap": "ARROW_LINES" },
    "lifeline":     { "color": "{ink.lifeline}", "weight": 2, "dash": [6, 6], "endCap": "NONE" },
    "label":        { "type": "label" }
  },
  "zone": {
    "tints": { "blue": "#F5FBFF", "orange": "#FFF7F0", "teal": "#F1FEFD", "yellow": "#FFFBF0", "violet": "#F8F5FF", "pink": "#FFF0FA" },
    "cycle": ["blue", "orange", "teal", "yellow", "violet", "pink"],
    "tintPolicy": "cycle", "align": "fit", "label": "zone"
  },
  "key": { "fill": "#F9F9F9", "title": "Key", "width": "content", "order": "first-use", "sample": { "w": 88, "h": 48 } },
  "titleBlock": { "title": "title", "subtitle": "subtitle", "measure": [960, 1440], "noOrphan": false },
  "source": { "type": "label" },
  "frame": { "fill": "#FFFFFF", "margin": "{space.boardPad}" }
}
```

The `"..."` entry stands for the remaining kinds, which the shipped file lists in full. Sources for the values: [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:19-102] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:921-927] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:933-957] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1031] [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1131-1197].

### 6.5 How the scripts load and validate it

- **`compose_board.py`** reads the one fenced `json` block from each layer and merges them token by token. It resolves aliases, validates (6.6) and writes the measured ratios beside each colour role, so the user never types a ratio. It then fills a new `__THEME__` placeholder beside `__MODEL__` [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:569-571] with only the tokens that differ from the packet default, compact and resolved to hex and numbers. The `COMPOSED` line names the spec layers used, a short hash of the resolved theme and any reverted token.
- **Size budget.** The code leaves about 6,376 characters for model and theme together. A full resolved theme would cost about 4,000 of them, so only the differences travel, under a 1,500-character theme cap that refuses with "split the override" past it. The existing 50,000-character check still runs on the filled code [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:595-597].
- **`compose-board.js`** keeps today's literals as built-in defaults and deep-merges `const THEME = __THEME__` over them. An empty `{}` draws today's board. It writes the theme hash into the shared plugin data it already sets [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/compose-board.js:1214], so a revision knows which style drew the board.
- **Single source by test, not by build step.** The self-test parses the packet default and fails when any composer literal differs from it, replacing today's regex read of the JavaScript [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:700-701]. The style guide's `FIGJAM_PALETTE` rows and `common.py`'s `ACCENT_PAIRS` are checked against the spec's swatches the same way. No generator runs and the Project's code block stays byte-equal to `--template` [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:925-929].
- **`flow_check.py` and `common.py`** keep accepting the swatch pairs in Mermaid `style` lines. The hex in templates and examples marks meaning, not paint [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:124], so a theme never requires a template change.

### 6.6 Safe defaults when a user edits it badly

1. **Refuse before the call** when the override's block is missing, duplicated or unparseable, names an unknown `schemaVersion`, has an unknown top-level group or breaks an alias. The script exits 1 with the field path, as it does for a model that fails the check. A board silently drawn in defaults after a user edit would be a false success.
2. **Revert one token, keep the rest,** when a value is well formed but misses a floor. The reverted token is named on the `COMPOSED` line and in the reply's `Finding:` line. The floors reuse the existing measures [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:702-727] [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/common.py:157-160]:
   - text on every role's fill at 4.5:1 or better, and the `marker` digit at 4.5:1 [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:170-174]
   - the accent stroke at 3:1 on the canvas and at least 45 degrees from every role's hue and every tint's hue
   - the accent stroke heavier than any other stroke
   - no two kinds one type draws share both shape and role
   - type sizes inside bounds: `small` at least 14, `label` at least 14, `node` 16 to 28, `title` at least twice `node`
   - every space, rhythm and size a multiple of `grid`
3. **Palette by name.** A role aliases a swatch. A raw hex is accepted only with `"offPalette": true` and is reported, because a custom colour drops out of FigJam's picker [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:156] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:206].

### 6.7 How the claude.ai Project carries it

A Project cannot read a local file [SOURCE: AI Systems/Product Owner/SYNC.md:82] and runs no script, so its agent already fills `__MODEL__` by hand [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/compose_board.py:71-72].

- A new Knowledge file, `Product Owner - Assets - Flow Board Design.md`, mirrors the packet default by hand under the `SYNC.md` method.
- The composer Knowledge file's steps gain one line: replace `__THEME__` with `{}`, or with the override tokens the user pastes, written compact.
- The Project has no validator, so its override is limited to role aliases and the `key`, `zone` and `titleBlock` switches, each named in the Knowledge file. Contrast floors cannot be measured there, so any raw hex is refused in the Project.
- The kernel's Flow composer instruction changes by one clause, which is a kernel edit under the parity method.

### 6.8 How a user edits it safely

- Copy only the tokens to change into `AI Systems/Product Owner/figjam-design.md`, never edit the packet default, which the self-test pins.
- Run `compose_board.py --design-check`, a new read-only command that prints the resolved theme, the measured ratios, any reverted token and the theme's character cost.
- The prose sections above the block say what each role means, which tokens are safe to change and which floors apply, in the Style Reference's Do's and Don'ts form.

### 6.9 How the rubric and the scorecard check a board against it

- **Rubric Section 7** gains "Matches the active design": 2 when key order, title block, line roles and tint rule match the resolved spec, 1 with one named exception, 0 with two. The total becomes 18.
- **Rubric Section 6** gains two checklist lines: every fill on the board resolves to a spec role, and no zone tint shares a hue with a kind inside it or with the accent.
- **Scorecard Signal** scores against the resolved spec instead of the fixed palette text, and its allowed tint list comes from the spec [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:95-101].
- **New scenarios:** a family scenario composing the seven examples under the default spec and comparing furniture, and a broken-override scenario (pink tint, low-contrast text, an unknown group) that expects one refusal and named reversions with an unchanged first glance.
- **Self-test** composes every shipped example under the default and under a sample override and fails on any crossed floor.

---

## 7. Rejected or deferred ideas

- **Brand skins and arbitrary hex by default.** Rejected. A brand palette turns every swatch into a custom colour [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:206]. Kept only as the reported `offPalette` opt-in.
- **Deeper zone tints (swe).** Rejected. The tints already separate at the 2048 px render, helped by their borders, and stronger tints would compete with the kind fills inside them.
- **A light fill on gantt planned bars (swe).** Rejected in favour of Rank 12. Every light fill already means a status (in progress, done, critical), so a filled planned bar would read as one of them.
- **Removing hex pairs from templates and examples (luna).** Rejected. A `style` line marks meaning and the composer ignores its paint [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:124-133].
- **Fail closed on every token error (luna).** Narrowed to structural errors (6.6), because one low-contrast role should not block a board the rest of the theme draws well.
- **Per-type themes (swe).** Rejected. The types differ by kind vocabulary and layout, not style, so one role table is simpler and is the consistency guarantee.
- **Exposing router and layout constants.** Rejected. They hold invariants a user cannot see.
- **The full v3 Style Reference with Quick Start CSS.** Rejected. Section 6.2 gives the reasons.
- **A raw DTCG `tokens.json` file as the user surface.** Rejected for hand editing. Its token shape is kept inside the Markdown file.
- **A repository-root `DESIGN.md`.** Rejected. Section 6.1 gives the reasons.
- **Shipping the full theme in every call.** Rejected by the code budget (6.5).
- **A numeric corner radius token.** Deferred. The composer sets no radius today (grep finds none in `compose-board.js`), so the token is documented as fixed until the composer can set and verify one.
- **A tinted header band on ER cards (swe).** Deferred. A FigJam shape with text takes one fill, so a band means a second node per card, which the read-back counts.
- **Crow's-foot ends on ER relationships.** Deferred. Whether a FigJam connector cap can draw one was not checked.

---

## 8. Corrections and drops

### Corrected (15)

1. **Opus 1.1, pink tint.** The code does not merely contradict the guide. The guide contradicts itself: line 91 calls the accent the only pink while line 93 lists pink in the tint cycle.
2. **Opus 1.3, tint and kind collision.** Holds visually. Its framing as a breach of "nothing coloured by position" is softened: the rubric also asks that neighbouring tints differ [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:133] and the scorecard says a tint means nothing [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:97]. The orange stream in a yellow lane is an adjacent hue, not a match, and was dropped from the evidence.
3. **Opus 1.10, ER jog.** Card tops are ragged, but Guest and Booking share a centre line. makes jogs because Booking's left magnet is taken, so top alignment will not remove the jog.
4. **Opus 2.3, architecture wording.** "colours it by that lane" is loosely true, because the lane fixes the kind and the kind fixes the colour [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:66]. It is ambiguous, not wrong.
5. **Opus 3.1, Style Reference shape.** The "11 sections with a design-tokens JSON block" describes `figma-ds-cli extract` [SOURCE: AI Systems/Product Owner/mcp-figma/feature-catalog/design-system-extract-and-import/design-system-extract-and-import.md:27], not the v3 Style Reference, whose machine layer is the Quick Start CSS built from a separate `tokens.json`.
6. **Opus 3.5, gantt pink band.** Pink is the sixth tint, so a sixth section would be pink, not a fifth.
7. **Opus 3.7, pin colour.** The pin draws the saturated violet pair. Its fill equals the data store's stroke, but the store draws the light violet pair.
8. **Swe 1.1, one constants block.** Most values sit in lines 17-102, but `ARROWS`, the key `LINES`, gantt rhythm and the 14 px literals live elsewhere.
9. **Swe 1.8, label legibility everywhere.** The router does own it, but `state-board.png` sets missed check-in on a zone corner.
10. **Swe 1.15, no drift observed.** Key order and the sequence line language drift in ways no type needs (Section 3).
11. **Swe 2.1, Google DESIGN.md.** Format, YAML tokens and tolerance of unknown sections confirmed on the repository page. "Counterpart to AGENTS.md" was not found there, and the weekly download count was not checked. Both are left out.
12. **Swe 2.10, graceful degrade as house philosophy.** The packet states no such rule. The cited lines list palette departures. The fallback design here stands on its own reasons.
13. **Luna 1.3, gallery count.** Eight boards besides the sequence board score 21 or 22, as luna's own iteration 2 corrected.
14. **Luna 1.4, conflicting totals.** The 16 and 22 point totals score different scopes, as luna's iteration 2 corrected.
15. **Luna 2.3, public examples.** The DTCG facts were confirmed by fetch. The two GitHub DESIGN.md examples were not fetched and are not used.

### Dropped (2)

1. **Swe 1.7, zone tints barely separate.** The tints read apart on every PNG with zones, helped by their borders.
2. **Luna 2.5, template hex as theme authority.** A `style` line is meaning, not paint, so templates hold no colour authority to remove.

---

## 9. Open questions for the operator

1. Should the override sit at the system root and be tracked, so restyling is a team choice, or in a gitignored local file, so it is a personal one?
2. Should a malformed override refuse the board, as recommended, or compose in defaults with a warning?
3. Keep the scorecard at 22 points with Signal reading the spec, or add a fidelity dimension and re-score the gallery at 24?
4. Rank 3 changes every sequence board's look. Accept white participants, or keep light blue and record participant as its own named role?
5. Should an `offPalette` raw hex be allowed at all, or should themes stay inside FigJam's swatches?
6. The design spec needs one new Knowledge file and one kernel clause. Accept that kernel change now or hold the Project at defaults until the kernel review?

---

## 10. Sources

### Packet sources read

- `AI Systems/Product Owner/sk-create-figjam/`: `assets/compose-board.js` (whole file), `scripts/compose_board.py`, `scripts/figjam_checks/common.py`, `references/style-guide.md`, `references/quality-rubric.md`, `references/types/*.md`, `references/flow-mode.md`, `assets/flow-templates.md`, `assets/templates/*.md` and `assets/examples/*.md` (style lines), `manual-testing-playbook/manual-testing-playbook.md` (scorecard), `manual-testing-playbook/boundaries/restyle-is-a-hand-edit.md`, `SKILL.md`, `assets/screenshots/README.md` and all nine PNGs, viewed as images and cropped where a detail needed it
- `AI Systems/Product Owner/SYNC.md`, `AI Systems/Product Owner/claude project/knowledge/Product Owner - Assets - Flow Board Composer.md` and `AI Systems/Product Owner/specs/017-figjam-flow-generation/036-figjam-design-system/goal.md`
- `.skilled/skills/sk-design/sk-design-md-generator/SKILL.md`, `references/design-md-format.md` and `references/authoring-boundary.md`

### Outside sources fetched

- W3C Design Tokens Community Group, Format, Final Report of 28 October 2025: https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/
- Google Labs `design.md`: https://github.com/google-labs-code/design.md

### Lineage inputs

- `AI Systems/Product Owner/specs/017-figjam-flow-generation/036-figjam-design-system/research/lineages/opus/iterations/iteration-001.md` to `iteration-003.md` and `lineages/opus/research.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/036-figjam-design-system/research/lineages/swe/iterations/iteration-001.md` to `iteration-002.md` and `lineages/swe/research.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/036-figjam-design-system/research/lineages/luna/iterations/iteration-001.md` to `iteration-002.md` and `lineages/luna/research.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/036-figjam-design-system/research/findings-registry.json` (45 findings, swe and luna) and `fanout-attribution.md`

### Checks run during this synthesis

- `compose_board.py --self-test`: 815 of 815 passed, exit 0
- `compose_board.py --template`: 43,624 characters on 1,088 lines
- Greps for `tint` in `compose_board.py`, `radius` in `compose-board.js`, YAML imports in `scripts/` and hex `style` lines in templates and examples
