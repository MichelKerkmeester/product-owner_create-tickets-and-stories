# Iteration 10: Mistakes the Media Editor plugin already paid for

## Focus

Read the plugin phase's decision record, acceptance criteria and implementation summary for the failures, supersessions and operator decisions it produced. This deepens the packaging precedent from a description into a set of corrections the Product Owner plugin should inherit.

## Findings

1. Claude Code supplies no Node for a bundle and does not expand a bundle's folder settings, so the plugin's `plugin.json` must run `node` and the README must document Node as an external requirement; the original Node 18 claim was superseded by the package's own 20.9.0 engines floor. [SOURCE: AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/implementation-summary.md:55] [SOURCE: AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/acceptance-criteria.md:63]
2. The plugin build resolves a skill's linked rule files into real files and fails when any copied file differs from its source or when the unpacked server holds a link; Product Owner had already replaced four shared rule symlinks with regular-file copies for the same standalone-clone reason. [SOURCE: AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/implementation-summary.md:55] [SOURCE: AI Systems/Product Owner/SYNC.md:44]
3. A safety rule that treated any download redirect as a failure made installs impossible on eight of ten pinned platform URLs, because GitHub serves release assets through a signed redirect; the rule was amended the same day to allow exactly one host-checked redirect. A protective rule can silently reduce platform coverage. [SOURCE: AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/decision-record.md:163] [SOURCE: AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/decision-record.md:179]
4. The test suite resolved a development binary while the shipped plugin carried a different pinned build, and running against the shipped pair produced 45 failures unrelated to capability. Shipped-payload parity needs its own test pass, not the development dependency's word. [SOURCE: AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/implementation-summary.md:122]
5. A skill rename propagated into every packaging surface at once: the plugin copy path, the Project knowledge names and the re-upload and rebuild steps all had to move in the same release, and the build's whole-folder replacement exists so an old-name copy cannot ship beside the new one. [SOURCE: AI Systems/Media Editor/sk-media-editor/changelog/v0.8.0.0.md:83] [SOURCE: AI Systems/Media Editor/sk-media-editor/changelog/v0.8.0.0.md:121]
6. Bundled-tool behavior differences become operator decisions rather than test outcomes: when the shipped ffmpeg changed how it copies audio into MP4, the phase recorded the trade-off and left the choice to the operator instead of silently re-encoding. [SOURCE: AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/implementation-summary.md:122]

## Ruled Out

- Assuming the runtime supplies a Node runtime or expands bundle settings. The spike disproved both, and the manifest was rebuilt around that.
- Treating the development dependency as the shipped binary. The 45-failure run shows that shortcut fails silently.

## Dead Ends

- Looking for a plugin-specific parity tool in the PO repo. The parity lesson is transferable, but there is no shared checker to reuse.

## Edge Cases

- Ambiguous input: "mistakes" could mean defects or wrong design choices. Selected both, since the redirect rule and the Node assumption were design errors while the test mismatch was a defect-class miss.
- Contradictory evidence: none; the acceptance criterion records its own supersession.
- Missing dependencies: the plugin build script itself was not read, so the exact link resolution is documented rather than inspected.
- Partial success: none.

## Sources Consulted

- `AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/implementation-summary.md:55,122,132`
- `AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/acceptance-criteria.md:63`
- `AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/decision-record.md:163,179`
- `AI Systems/Media Editor/sk-media-editor/changelog/v0.8.0.0.md:83,121`
- `AI Systems/Product Owner/SYNC.md:44`

## Assessment

- New information ratio: 1.0
- Questions addressed: Media Editor lessons and mistakes.
- Questions answered: the Media Editor half of the lessons question, and it feeds the sync-path question directly.

## Reflection

- What worked and why: reading the acceptance criteria for the word "superseded" found the Node assumption faster than reading the plan, because a supersession marks a belief that failed in practice.
- What did not work and why: expecting the changelog to carry defects was wrong; the phase documents carry them and the changelog carries the propagation steps.
- What I would do differently: read `implementation-summary.md` first in any completed phase, since it collects the corrections the other documents describe as intended behavior.

## Recommended Next Focus

Iteration 11: turn to the Moneybird Accountant hub precedent and read `hub-router.json` and `mode-registry.json` to establish what a parent hub is in file terms, so the Media Editor lessons can be compared against a second, structurally different precedent.
