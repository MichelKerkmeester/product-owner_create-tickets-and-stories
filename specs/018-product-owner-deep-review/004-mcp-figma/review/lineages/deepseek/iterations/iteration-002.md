# Iteration 2 - Security

**Dimension:** security
**Iteration:** 2 of 5
**Target:** `AI Systems/Product Owner/mcp-figma/` (vendored packet), `vendor.json`, `scripts/vendor-sync.py`
**Route:** Resolved route: mode=review target_agent=deep-review, execution=single_review_iteration
**Sources read this iteration:** steer.md (lineage), `README.md`, `INSTALL-GUIDE.md`, `references/tool-surface.md`, `references/figma-cli-reference.md`, `references/mcp-wiring.md`, `assets/utcp-figma-manual.md`, `assets/env-template.md`, `scripts/install.sh`, `scripts/_common.sh`, `scripts/doctor.sh`, `scripts/print-utcp-snippets.sh`, `scripts/connect-yolo.sh`, `scripts/unpatch.sh`, `examples/safe-connect-daemon-health.sh`, `examples/inspect-export-readonly.sh`, `mcp-servers/figma-cli/setup.sh`, `mcp-servers/figma-mcp/README.md`, `AI Systems/Product Owner/.gitignore`; oracle: `figma-ds-cli extract --help`, `figma-ds-cli export --help`.

## Files Reviewed

| File | Security question asked |
|---|---|
| `README.md`, `INSTALL-GUIDE.md` | Do the copy-paste commands keep the packet's own no-overwrite and gating promises? |
| `references/tool-surface.md`, `references/figma-cli-reference.md` | Is the gate taxonomy stated consistently with the commands it names? |
| `references/mcp-wiring.md`, `assets/utcp-figma-manual.md`, `assets/env-template.md` | What executes with the Figma token in its environment, and at what version? |
| `scripts/install.sh` | What code does the installer run, from where, at what pin? |
| `scripts/doctor.sh`, `scripts/print-utcp-snippets.sh` | Can any output path print the daemon token or a real credential? |
| `examples/*.sh`, `mcp-servers/figma-cli/setup.sh` | Do the worked examples honour the gates they claim to mirror? |
| `AI Systems/Product Owner/.gitignore` | Is the token file the packet tells users to create actually ignored? |

## Findings by Severity

### P0 Findings

None. The security surface holds where it matters most: no credential-shaped string exists anywhere in the packet (a `figd_`/`sk-`/`ghp_`/AKIA scan across all 58 files returned nothing), the daemon token is only ever referenced by path and `doctor.sh:33` states "(contents NOT shown)", no script uses `sudo`, `chmod`, or a `curl | bash` pipe, yolo connect is consent-flagged and refuses without it (`connect-yolo.sh:13-27`), and `AI Systems/Product Owner/.gitignore:10-12` does ignore `.env` while keeping `.env.example` tracked, so following the packet's token instructions does not stage a secret.

### P1 Findings

**R2-P1-001 - The quick-start and the install-guide checklist invoke `extract` with a flag the binary does not define, at a fixed path that the packet's own no-overwrite rule forbids.**

`figma-ds-cli extract --help` documents `extract [options] [output]` with only `--sections`, `--pages`, `--selection`, `--split`, `--no-split`. There is no `--out`. The packet knows this in two places - `figma-cli-reference.md:217` and `tool-surface.md:78` both record the positional `[output]` form - and its own runnable example uses the positional/`-o` convention (`examples/inspect-export-readonly.sh:62`). Yet the two documents a new user is told to follow hand them `--out DESIGN.md`: a flag that is at best ignored and at worst rejected, aimed at a fixed filename in the working directory. That fixed path is precisely the "silently overwrite an existing file" case `tool-surface.md:50` and the SKILL.md rule set exist to prevent, and the example script that gets it right does so by refusing when the target exists (`examples/inspect-export-readonly.sh:55-59`).

[SOURCE: mcp-figma/README.md:86]
[SOURCE: mcp-figma/INSTALL-GUIDE.md:268]
[SOURCE: mcp-figma/INSTALL-GUIDE.md:291]
[SOURCE: mcp-figma/references/figma-cli-reference.md:217]
[SOURCE: mcp-figma/examples/inspect-export-readonly.sh:62]

- **Claim:** the documented extract invocation is not the invocation the tool accepts, and it defeats the packet's own overwrite guard.
- **evidenceRefs:** the three `--out` sites above; `figma-ds-cli extract --help` (positional `[output]`, no `--out`); `tool-surface.md:78` and `figma-cli-reference.md:217` (positional form); `tool-surface.md:50` and `README.md:89` ("never silently overwrite").
- **counterevidenceSought:** checked whether the CLI defines a hidden global `--out`; the top-level `--help` options are only `-V/--version` and `-h/--help`, so no global flag exists to inherit. Checked whether a second `extract` spelling exists under `export`: `export --help` lists `dtcg`, `screenshot`, `node` and siblings, with their own `-o` flags.
- **alternativeExplanation:** commander may tolerate an unknown option and treat `DESIGN.md` as the positional argument, so the command could still work. That possibility does not rescue the finding: it makes the flag noise rather than an error, and the fixed path still overwrites.
- **finalSeverity:** P1. **confidence:** high on the flag; medium on the runtime consequence, stated as such.
- **downgradeTrigger:** if `extract --out` is accepted as an alias by 1.2.0, only the fixed-path half of this finding survives, at P2.
- **Fix site (upstream):** `.skilled/skills/mcp-tooling/mcp-figma/README.md:86`, `INSTALL-GUIDE.md:268` and `:291` - use `figma-ds-cli extract <fresh-path>/DESIGN.md` and add the refuse-if-exists step the example already implements.

### P2 Findings

**R2-P2-001 - Nothing the packet executes is pinned or integrity-checked, in a packet that pins itself byte-for-byte.**

`install.sh` clones the default branch (`git clone --depth 1`, no tag, no commit) and then runs `npm install -g .` inside that clone, which executes the dependency install lifecycle as the invoking user. The optional MCP path registers `figma-developer-mcp@latest` (or the bare name, which resolves to the same moving tag), and that server runs with the Figma token in its environment. Both the reference and the asset carry the same unpinned arg, and `mcp-wiring.md:95` concedes the surface "can change". `vendor.json` exists because an unpinned copy cannot be trusted; the same argument is not applied to the tool the copy installs.

[SOURCE: mcp-figma/scripts/install.sh:102]
[SOURCE: mcp-figma/scripts/install.sh:104]
[SOURCE: mcp-figma/references/mcp-wiring.md:60]
[SOURCE: mcp-figma/assets/utcp-figma-manual.md:53]

- **confidence:** medium. This is a hardening gap, not a demonstrated vulnerability; the tool is third-party by nature and installing from source is a documented, deliberate choice.
- **Downgrade/upgrade trigger:** becomes P1 the moment the repo starts treating the packet's own integrity discipline as a security requirement for its dependencies.
- **Fix site (upstream):** `scripts/install.sh:102-104` - pin a tag or commit and record it; `references/mcp-wiring.md:60` and `assets/utcp-figma-manual.md:53` - pin a version instead of `@latest`.

**R2-P2-002 - The optional MCP path pipes arbitrary third-party-authored text into the model with no untrusted-content instruction.**

`mcp-wiring.md` teaches the agent to pull file and node data as model input, and the tool's own docs describe that payload as free text authored in a Figma document, which any collaborator can write. Nowhere in `SKILL.md`, `references/mcp-wiring.md` or `assets/utcp-figma-manual.md` is the returned content marked as data rather than instruction, so a node name or text layer reading like an instruction is indistinguishable from the user's request.

[SOURCE: mcp-figma/references/mcp-wiring.md:29]
[SOURCE: mcp-figma/assets/utcp-figma-manual.md:108]

- **confidence:** medium-low, and stated as such: no exploit is demonstrated and no sibling transport packet was compared to establish whether this is packet-specific.
- **Fix site (upstream):** `references/mcp-wiring.md` Section 5 - add a one-line guard that Figma-authored content is untrusted data.

## Traceability Checks

| Protocol | Level | Status | Evidence |
|---|---|---|---|
| `spec_code` | core | pending | Deferred to iteration 3's spec-alignment pass. |
| `checklist_evidence` | core | not_applicable | No `checklist.md` in the staging folder. |
| `skill_agent` | overlay | pending | Iteration 4. |
| `agent_cross_runtime` | overlay | not_applicable | No runtime agent definition shipped. |
| `feature_catalog_code` | overlay | partial | `feature-catalog/feature-catalog.md:104` states the extract invocation correctly (positional form) while `README.md:86` and `INSTALL-GUIDE.md` do not: the catalog agrees with the binary, the front-door docs do not. |
| `playbook_capability` | overlay | pending | Iteration 4. |

## Security checklist walked

| Check | Result |
|---|---|
| Credential-shaped strings in the packet | none found (scan across all 58 files) |
| Daemon token printed anywhere | no: path only, contents never read by a script (`doctor.sh:33`) |
| `sudo` / `chmod` / remote-pipe execution | none in `scripts/`, `examples/`, `mcp-servers/` |
| Destructive verb without consent gate | none: yolo connect refuses without the consent flag, `unpatch.sh` is the stated rollback |
| Arbitrary execution (`eval`/`raw`/`run`) | classified as arbitrary-mutation and gated in `tool-surface.md` and SKILL.md ALWAYS rule 6 |
| `.env` handling | `.gitignore:10-12` ignores `.env`, `.env.*`, keeps `.env.example` |
| Local service binding | daemon and CDP both documented as `127.0.0.1` only |
| Export overwrite protection | documented, implemented in `examples/inspect-export-readonly.sh`, contradicted by README/INSTALL-GUIDE (R2-P1-001) |

## Reconfirmed from iteration 1 (not re-counted)

- **Binary identity is still the weak seam.** `examples/safe-connect-daemon-health.sh:34-38` prints `figma-cli --version` and then assigns `BIN="figma-cli"` whatever the probe says, so even the example that narrates the fail-closed rule does not enforce it. Second site of R1-P1-002's root cause; recorded there, not as a new finding.

## Next Dimension

Iteration 3 (traceability): spec-versus-packet alignment, every cross-reference resolved from its own file's depth, version claims across all six changelogs against the packet version, and the reference graph between `SKILL.md`, `references/`, `feature-catalog/` and the playbook.

Review verdict: CONDITIONAL
