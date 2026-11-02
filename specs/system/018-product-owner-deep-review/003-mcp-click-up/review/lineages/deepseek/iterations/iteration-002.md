# Iteration 002 — Deep Review

## Dispatcher

- Mode: review; target_agent: deep-review; execution: inline lineage executor (no nested dispatch)
- Iteration: 2 of 5; Dimension: security
- Lineage: sessionId=fanout-deepseek-1792580454700-vajsq8, generation=1, lineageMode=new
- Sources read this iteration: `specs/product-owner/018-product-owner-deep-review/003-mcp-click-up/spec.md`, `specs/product-owner/018-product-owner-deep-review/003-mcp-click-up/review/lineages/deepseek/steer.md`, `deep-review-strategy.md`, `AI Systems/Product Owner/mcp-click-up/scripts/install.sh`, `AI Systems/Product Owner/mcp-click-up/scripts/doctor.sh`, `AI Systems/Product Owner/mcp-click-up/scripts/README.md`, `AI Systems/Product Owner/mcp-click-up/mcp-servers/clickup-cli/setup.sh`, `AI Systems/Product Owner/mcp-click-up/mcp-servers/clickup-cli/requirements.txt`, `AI Systems/Product Owner/mcp-click-up/mcp-servers/clickup-cli/README.md`, `AI Systems/Product Owner/mcp-click-up/examples/task-queue-workflow.sh`, `AI Systems/Product Owner/mcp-click-up/examples/time-tracking-workflow.sh`, `AI Systems/Product Owner/mcp-click-up/INSTALL-GUIDE.md`, `AI Systems/Product Owner/mcp-click-up/references/troubleshooting.md`
- Live read-only evidence: `bash scripts/doctor.sh` executed once from the vendored packet; it installs nothing and writes nothing (`scripts/README.md:13`)

## Dimension

Security — the packet's executable surface and the credential guidance a reader follows, judged as a trust boundary: what the packet runs, what it asks the user to paste, and what it claims to have checked.

## Files Reviewed

- `AI Systems/Product Owner/mcp-click-up/scripts/install.sh:1-255`
- `AI Systems/Product Owner/mcp-click-up/scripts/doctor.sh:1-91`
- `AI Systems/Product Owner/mcp-click-up/scripts/README.md`
- `AI Systems/Product Owner/mcp-click-up/mcp-servers/clickup-cli/setup.sh:1-16`
- `AI Systems/Product Owner/mcp-click-up/mcp-servers/clickup-cli/requirements.txt`
- `AI Systems/Product Owner/mcp-click-up/mcp-servers/clickup-cli/README.md:30-80`
- `AI Systems/Product Owner/mcp-click-up/examples/task-queue-workflow.sh:1-214`
- `AI Systems/Product Owner/mcp-click-up/examples/time-tracking-workflow.sh:1-175`
- `AI Systems/Product Owner/mcp-click-up/INSTALL-GUIDE.md:28-200`
- `AI Systems/Product Owner/mcp-click-up/references/troubleshooting.md:60-140`

## Findings by Severity

### P0 Findings

None.

### P1 Findings

1. **`doctor.sh` hard-codes a five-level walk to `.utcp_config.json`, so in the vendored packet its only Code Mode check is a guaranteed false negative** -- AI Systems/Product Owner/mcp-click-up/scripts/doctor.sh:71 -- `UTCP="$HERE/../../../../../.utcp_config.json"` is correct only in the upstream layout, where the script sits five levels under the repository root that holds `.skilled`. In the Product Owner copy the same expression lands one directory above the workspace, and `doctor.sh:81` then prints ".utcp_config.json not found at expected repo root" even though the file exists and registers `clickup_official`.
Finding class: incorrect-path-resolution
Scope proof: the depth is a literal in this file; every invocation available in this repository was enumerated (vendored path, and the `.skilled`-relative path that `scripts/README.md:31` documents) and none reaches the directory that holds the file.
Affected surface hints: `mcp-click-up/scripts/doctor.sh` (fix upstream), `mcp-click-up/scripts/README.md:22` (the promise it fails to keep), every Product Owner reader who runs the diagnostic
Case: a Product Owner reader with a working Code Mode ClickUp manual runs `bash mcp-click-up/scripts/doctor.sh`; the diagnostic prints ".utcp_config.json not found at expected repo root" although `/Users/michelkerkmeester/MEGA/Development/AI Systems/.utcp_config.json` exists and contains `mcp.clickup.com` plus a `clickup_official` manual, so the reader is pushed to re-add a manual that is already correct.
Fix site: `mcp-click-up/scripts/doctor.sh` upstream — search upward for the nearest `.utcp_config.json` (the same walk `vendor-sync.py` uses for `.skilled`) instead of counting directories.
Claim adjudication:
```json
{
  "claim": "doctor.sh resolves .utcp_config.json at a fixed depth that matches only the upstream skill layout, so its MCP registration check cannot see the workspace config in the vendored copy.",
  "evidenceRefs": [
    "AI Systems/Product Owner/mcp-click-up/scripts/doctor.sh:71",
    "AI Systems/Product Owner/mcp-click-up/scripts/doctor.sh:81",
    "AI Systems/Product Owner/mcp-click-up/scripts/README.md:22",
    "AI Systems/.utcp_config.json:1"
  ],
  "counterevidenceSought": "Checked all three candidate depths from the script directory: three up is the Product Owner root (no file), four up is the workspace root (file present, registers clickup_official), five up, the coded value, is /Users/michelkerkmeester/MEGA/Development (no file). Also ran the script: it printed the not-found line.",
  "alternativeExplanation": "The packet is only ever executed from the upstream layout, where five up is correct, and Product Owner never runs scripts/. Rejected as complete mitigation: the packet ships scripts/README.md, which tells a reader to run it, and the byte-copy contract makes this copy the only one a Product Owner reader has.",
  "finalSeverity": "P1",
  "confidence": "high",
  "downgradeTrigger": "If Product Owner documents that these scripts must only be run from the shared skill repository, the impact becomes a documentation note and the severity drops to P2."
}
```

### P2 Findings

1. **The token guidance puts a ClickUp API token on the command line with no shell-history warning** -- AI Systems/Product Owner/mcp-click-up/INSTALL-GUIDE.md:120 -- the recommended individual path is `cupt config --api-token pk_YOUR_TOKEN_HERE`, repeated in `README.md:64` and `references/troubleshooting.md:132`. A token passed as an argument is written to shell history and is visible in the process table while the command runs. The packet states its own hygiene stance in `scripts/doctor.sh:2-3` ("it never prints secrets"), so the omission is inconsistent with the packet's own standard, not merely absent.
Finding class: credential-hygiene
Scope proof: the four instruction sites are all inside the reviewed packet; the interactive alternative (`cupt auth`) is documented beside each of them.
Affected surface hints: `mcp-click-up/INSTALL-GUIDE.md` (fix upstream), `mcp-click-up/README.md`, `mcp-click-up/references/troubleshooting.md`, `mcp-click-up/feature-catalog/cupt-authentication/direct-token.md`
Case: a user follows the recommended option on a shared machine; the `pk_` token is now in `~/.zsh_history` and in any terminal-session recording, and nothing in the packet told them to prefer `cupt auth` or to clear the history entry.
Fix site: `mcp-click-up/INSTALL-GUIDE.md` upstream — label `cupt auth` the default and note that `--api-token` leaves the token in shell history.

2. **The Code Mode bridge runs an unpinned third-party package on every launch** -- AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:20 -- the manual launches `npx -y mcp-remote https://mcp.clickup.com/mcp`, with `-y` suppressing the install prompt. Every launch therefore executes whatever version npm currently serves, and the packet's own verification section documents how the *server* tool set can change (`mcp-tools.md:24`) without ever pinning the *client* that carries the OAuth token.
Finding class: supply-chain
Scope proof: the launch string is identical in the three sites that document it (`mcp-tools.md:20`, `INSTALL-GUIDE.md:156`, `install.sh:185`); no version constraint appears in any of them.
Affected surface hints: `mcp-click-up/references/mcp-tools.md` (fix upstream), `mcp-click-up/INSTALL-GUIDE.md`, `mcp-click-up/scripts/install.sh` (the snippet it prints)
Case: a compromised or broken `mcp-remote` release lands on npm; the next launch of the ClickUp manual runs it with the user's OAuth session, and the packet offers no pinned alternative to compare against.
Fix site: `mcp-click-up/references/mcp-tools.md` upstream — pin a version range in every snippet and say what to do when the pinned range stops working.

## Traceability Checks

- `Core: spec_code` — the security dimension read every executable file under `mcp-click-up/scripts/`, `mcp-click-up/mcp-servers/`, and `mcp-click-up/examples/`, which is the whole shell surface of the packet the spec names. Status: pass.
- `Core: checklist_evidence` — no checklist exists in the staging wrapper; the steer file's security-relevant rulings (read-only, never open Product Context or screenshots) were followed. Status: pass.
- `Overlay: feature_catalog_code` — the two credential-bearing feature cards (`cupt-authentication/direct-token.md`, `cupt-authentication/interactive-auth.md`) were read against the guide: the guide's two options match the two cards. Status: pass with the hygiene gap recorded above.

## Integration Evidence

- `mcp-click-up/scripts/README.md:31` documents the upstream invocation `bash .skilled/skills/mcp-tooling/mcp-click-up/scripts/doctor.sh`; in Product Owner that path resolves through the `.skilled` symlink, so the script's `$HERE` becomes `<Product Owner>/.skilled/skills/mcp-tooling/mcp-click-up/scripts`, whose five-level parent is the Product Owner root — which holds no `.utcp_config.json`. The direct vendored invocation was also exercised and printed the same not-found line.

## Edge Cases

- `install.sh` never writes `opencode.json` or `.utcp_config.json`; it prints snippets (`install.sh:5`, `scripts/README.md:13`). That is the right trust posture and is recorded as clean, not as a gap.
- `npx -y` is the only way the packet documents reaching the hosted server, so the unpinned bridge is a design choice, not a slip; the finding asks for a pin, not for the removal of the route.
- A token pasted into a chat or a spec would be the worse exposure; the packet never asks for that, and `Product Owner/AGENTS.md:117` keeps the push targets in the shell or `.env`.

## Confirmed-Clean Surfaces

- No `eval`, no `sh -c`, no `xargs`, and no unquoted interpolation of ClickUp-supplied task ids or names in the two example scripts: both read ids and names into arrays with `IFS= read -r` and pass them quoted (`examples/task-queue-workflow.sh:157-176`).
- No `rm -rf` of an unvalidated variable anywhere in the packet's shell surface; the `cleanup` traps only print (`examples/task-queue-workflow.sh:24-30`, `examples/time-tracking-workflow.sh:9-16`).
- `doctor.sh` is genuinely read-only and prints no secret: it reports presence and version strings only (`doctor.sh:2-3`, `:37-67`).
- `install.sh` refuses unknown options and exits non-zero rather than guessing (`install.sh:47-55`), and verifies the install before claiming success (`install.sh:119-134`).
- `mcp-servers/clickup-cli/setup.sh` no-ops when `cupt` is already on `PATH`; `requirements.txt` carries the `cupt>=0.7.1` floor for the `pip install -r` path, and the README documents that split deliberately (`mcp-servers/clickup-cli/README.md:37`), so the split is not recorded as a defect.

## Ruled Out

- "The install scripts modify MCP or editor configuration": they print snippets only (`install.sh:5`, `scripts/README.md:13`).
- "The example queue scripts are command-injection sinks for task names": ids and names are read into arrays and passed quoted; no `eval`, `xargs` or `sh -c` exists in either script.
- "The installer ignores the shipped `requirements.txt` floor, so installs drift": the split is documented on purpose (`mcp-servers/clickup-cli/README.md:37`), so the unpinned install is intended behaviour for the embedded path; only the `mcp-remote` bridge is unpinned without such a note.
- "`doctor.sh` prints secrets": it prints no credential value.

## Next Dimension

- Dimension: traceability (contract consistency)
- Focus area: how `AGENTS.md`, `sk-product-owner/SKILL.md` Section 7, `hub-router.json`, `mode-registry.json`, `ROUTER.md` and `leaf-manifest.json` describe the packet's routing, push targets and ClickUp handoff, including the cupt-only runtime case
- Reason: the first two iterations read the packet from inside; the hub's promises about it are the remaining half of the review, and one contradiction is already visible between `AGENTS.md:117` and Section 7
- Rotation status: correctness and security complete; traceability next

## Source Tags

- R2-P1-001 — [SOURCE: mcp-click-up/scripts/doctor.sh:71]
- R2-P2-001 — [SOURCE: mcp-click-up/INSTALL-GUIDE.md:120]
- R2-P2-002 — [SOURCE: mcp-click-up/references/mcp-tools.md:20]

## Verdict

One P1 and two P2 findings this iteration, no P0. The packet's write surface is careful and its scripts are disciplined; the P1 is a diagnostic that cannot succeed in the copy that ships to Product Owner, and the P2s are credential and supply-chain hygiene in the instructions a user follows. Release-blocking: no, but the P1 needs an upstream fix before the packet's verification story can be trusted here.

Review verdict: CONDITIONAL
