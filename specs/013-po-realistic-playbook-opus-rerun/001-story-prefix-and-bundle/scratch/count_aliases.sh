#!/usr/bin/env bash
# Count the $prd and $p aliases and the H1 ban on a PRD - prefix, per file.
# Mirrors are matched by stem so the count survives the version renames.
cd "$(git rev-parse --show-toplevel)/AI Systems/Product Owner" || exit 1
files=(AGENTS.md sk-product-owner/SKILL.md sk-product-owner/references/story-mode.md
  sk-product-owner/references/interactive-mode.md sk-product-owner/assets/story-template.md
  sk-product-owner/assets/epic-template.md sk-product-owner/assets/task-templates.md
  "claude project/Custom Instructions.md")
for f in "claude project/knowledge/"*"Story Mode"*.md "claude project/knowledge/"*"Interactive Mode"*.md \
  "claude project/knowledge/"*"Task Templates"*.md "claude project/knowledge/"*"Story Template"*.md \
  "claude project/knowledge/"*"Epic Template"*.md; do files+=("$f"); done
printf '%-8s %-6s %-8s %s\n' '$prd' '$p' 'no-PRD-' 'file (stem)'
tp=0; tq=0; tn=0
for f in "${files[@]}"; do
  a=$(grep -oF '$prd' "$f" | wc -l | tr -d ' ')
  b=$(grep -oE '\$p([^a-zA-Z0-9_]|$)' "$f" | wc -l | tr -d ' ')
  c=$(grep -oiF 'no `PRD -` prefix' "$f" | wc -l | tr -d ' ')
  stem=$(echo "$f" | sed -E 's/ - v[0-9.]+\.md$//')
  printf '%-8s %-6s %-8s %s\n' "$a" "$b" "$c" "$stem"
  tp=$((tp+a)); tq=$((tq+b)); tn=$((tn+c))
done
printf '%-8s %-6s %-8s %s\n' "$tp" "$tq" "$tn" TOTAL
