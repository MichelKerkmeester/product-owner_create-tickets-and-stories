---
title: "Tasks: Package Rewiring"
description: "Wire the example libraries into both Product Owner packagings and verify."
importance_tier: "high"
contextType: "implementation"
---
<!-- SPECKIT_LEVEL: 1 -->
# Tasks: Package Rewiring

- [x] T001 SKILL.md: extend the resource model so each routed mode may load its example folder ON_DEMAND (never bulk), with the example libraries listed in the references section. (`Product Owner/skill/SKILL.md`)
- [x] T002 AGENTS.md, user guide and SYNC.md: describe the example libraries, extend the DAG and the mirror inventory. (`Product Owner/`)
- [x] T003 Claude project: mirror every example byte-identically, rebuild the checksum manifest, extend the kernel knowledge table and the upload inventory/smoke matrix. (`Product Owner/claude project/`)
- [x] T004 Verify: mirror parity and checksums fully green, router fixture suite passes, per-mode grammar scans clean; record evidence here. (`Product Owner/`)

Evidence: SKILL.md ON_DEMAND row and references extended with one-example-max loading; AGENTS.md load-on-demand rule and DAG entry; user guide feature bullet and routed-resources note; SYNC.md example-mirror convention with the twenty-eight-file inventory and drift-check counts; kernel knowledge table gained four Examples rows plus the one-example consultation rule; fifteen example mirrors written under their frontmatter titles; checksum manifest rebuilt to twenty-nine rows. Verified: 28/28 mirrors byte-identical (one interim SKILL.md drift caught and resynced), 29/29 checksums match, 43 router fixtures pass.
