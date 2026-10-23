# Iteration 001 — What a vision model can and cannot read from a UI screenshot

## Focus

Iteration 1 opens the input-to-model half of Flow Mode with the weakest link in the chain: the screenshot read. It asks what a vision-capable model reliably returns from a UI screenshot, which reads are cheap and certain, which are approximate, and therefore which reads Flow Mode may trust, which it must re-read, and which it must refuse to draw. Sources read: the repo's local vision skill and its per-tool catalog, Figma's own `figma-generate-diagram` skill text as the generator contract, and Flow Mode's screenshot intake as the baseline.

## Actions Taken

- Read `.skilled/skills/sk-vision/SKILL.md` in full: routes, the 13-tool surface, model lifecycle, OCR checkpoint requirement, troubleshooting.
- Read the per-tool catalog pages for the four tools a screenshot read actually uses: `inspect`, `ocr` (scene-understanding), `zoom` and `diff` (pixel-analysis).
- Read `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 and Section 5 as the baseline the finding would change.
- Searched the 22-repo corpus for screenshot-reading material. The hit that matters is Figma's own `workflow-skills/video-interaction-mapper`, which reads a recording frame by frame and carries an explicit uncertainty vocabulary; phase 009 and phase 016 never cite it as a source for the intake side.
- Did not read any screenshot or image file, any `figma.com` board URL, or anything under a containment folder.

## Findings

1. **The default local vision checkpoint cannot read text at all, and the OCR-capable one is labelled approximate.** `sk_vision_ocr` "requires a Moondream 3.x checkpoint. The default `moondream2` cannot transcribe text and fails loudly", and its output must be treated "as approximately correct because a preview checkpoint can repeat tokens. Verify against ground truth when exactness matters" [SOURCE: .skilled/skills/sk-vision/SKILL.md:204]. The tool exists and is honest about its own error mode; Flow Mode's screenshot intake never names a read tool, a checkpoint or a verification step, and instead states that a click target "is read off the image" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:113]. A node label retyped from a screenshot is therefore a transcription of an approximate read, and nothing in the packet records that. What the packet already does well and must keep: labels must use "the product's or the source's own terms" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:169], so the fix is a verification route, not a looser label rule.

2. **The scene read classifies; it does not measure.** `sk_vision_inspect` without a question runs caption, scene and OCR and returns "the scene read classifies image type, layout, elements, and state" from "a fixed prompt that asks for a type classification (UI screenshot, terminal, code, error dialog, document, chart/diagram, photo, or other), a layout description, notable elements, and current state" [SOURCE: .skilled/skills/sk-vision/feature-catalog/scene-understanding/inspect.md:32]. Coordinates come from other tools, `sk_vision_point` returning "normalized (0-1) center coordinates for a target" [SOURCE: .skilled/skills/sk-vision/SKILL.md:172]. So "the row under the cursor" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:113] is available only as a description unless a `point` or `detect` call is made, and Flow Mode names neither. The consequence is concrete: the label for the node that starts the next step is the least certain text in the model and is the one thing a user checks first.

3. **Small text fails at full-image scale, and the repair is a second read on an upscale.** `sk_vision_zoom` exists because it "makes small text and fine details readable when the vision model misses them at full-image scale", and "this second-pass analysis is where zoomed text actually becomes readable" [SOURCE: .skilled/skills/sk-vision/feature-catalog/pixel-analysis/zoom.md:18], [SOURCE: .skilled/skills/sk-vision/feature-catalog/pixel-analysis/zoom.md:26]. A dense dashboard screenshot read once at full size is therefore the worst case, and a node label drawn from it is the failure mode Figma names as a stretched shape: "long labels stretch shapes" [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:320]. No packet rule says a label read from a screenshot is re-read on a crop before it is written.

4. **Two screenshots can be compared by measurement, which settles "new screen or new state" without a caption.** `sk_vision_diff` "answers 'what changed' for before/after screenshots, render regressions, and UI iterations"; it returns "the changed pixel percentage, up to 12 changed-region boxes in normalized coordinates", and anti-aliasing is blurred out so it "does not count as change" [SOURCE: .skilled/skills/sk-vision/feature-catalog/pixel-analysis/diff.md:18], [SOURCE: .skilled/skills/sk-vision/feature-catalog/pixel-analysis/diff.md:22]. A pair with a small changed area inside one region reads as a state of the same screen; a pair whose changed area is the whole viewport reads as a different screen. Flow Mode has no such test today: it orders screenshots by filename grammar and asks one question when two orders fit [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:111], and never checks whether two supplied images are two screens or one screen in two states.

5. **Figma's own screenshot-reading workflow carries a named uncertainty vocabulary that Flow Mode lacks.** It separates the visible change from the trigger and allows "unknown trigger when the cause is ambiguous" [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:102]. It requires an inferred target to be marked "`inferred: true`, `uncertain: true`, `visible: false`, or `confidence: \"medium\"`/`\"low\"`", and it suppresses such a marker by default "so the canvas does not show a confident pulse over empty UI" [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:111]. Its edge case is blunt: "Missing trigger evidence: use `Unknown trigger` instead of guessing" [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:317]. Flow Mode's equivalent rule is prose, "A missing step ... is asked about or left as a named gap" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:144], with no per-item marker and no confidence channel inside the model. This is the single largest transferable idea found so far: a per-edge confidence label that the provenance table can carry.

6. **The before/after pair, not the screenshot, is the unit that carries a trigger.** Figma's workflow maps "the important before/after states, infer what triggered each change" [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:20] and records, per moment, a `trigger`, a `short_label`, an `annotation` and the before and after targets [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:130]. Flow Mode orders a flat list of files and then infers each move [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:111], which forces one order and one trigger per adjacent pair. Naming `(from, to, trigger, confidence)` as the intake record instead separates the two uncertainties — which screen follows which, and what moved between them — and is the change finding 4 and finding 5 both need.

## Questions Answered

- What can a vision-capable model reliably read from a UI screenshot, and which reads must Flow Mode re-check or refuse?

## Questions Remaining

- Ordering a screenshot set that carries no step numbers.
- Screen versus state, and how loading, empty and error states enter a model.
- Finding the action between two screens when it is only implied.
- Figma prototype links, frame names and the read tools behind them.
- Prose rules and acceptance criteria into decisions and branches.
- Merging sources, resolving conflicts, provenance per node and marking gaps.
- Type choice from what the input holds, and chunking a large input.
- The pre-gate check of a model against its sources.

## Next Focus

Ordering: how a screenshot set becomes a sequence when the filenames carry no step number, and how a screen is told apart from a state, building on findings 4 and 6.
