#!/usr/bin/env bash
# Print every line the playbook cites by number, labelled by file and line.
# The Interactive Mode mirror is matched by stem so the snapshot survives its rename.
cd "$(git rev-parse --show-toplevel)/AI Systems/Product Owner" || exit 1
show() { local f="$1"; shift; for n in "$@"; do printf '%s:%s: ' "$(echo "$f" | sed -E 's/ - v[0-9.]+\.md$//')" "$n"; sed -n "${n}p" "$f"; done; }
show sk-product-owner/SKILL.md 207 208 217 283
show "claude project/Custom Instructions.md" 58 76 79 85 89 104 130 217 223 224 225 226 227 228 233
show sk-product-owner/references/interactive-mode.md 85 93 124
show "$(ls "claude project/knowledge/"*"System - Interactive Mode"*.md)" 62 70
