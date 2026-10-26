#!/bin/bash
# Run every FigJam playbook scenario on one model, one run at a time, in playbook order, to
# collect a board and a reply for each template the skill can draw.
# Usage: run_full.sh <system dir> <run folder> <file key> <label> <model> [ID ...]
set -u
SYS="$1"; OUT="$2"; KEY="$3"; LABEL="$4"; MODEL="$5"; shift 5
HERE="$(cd "$(dirname "$0")" && pwd)"
IDS=("$@")
if [ ${#IDS[@]} -eq 0 ]; then
  while IFS= read -r id; do IDS+=("$id"); done < <(cd "$HERE" && python3 -c '
import sys
import devin_playbook_runner as dv
for r in dv.load_playbook(sys.argv[1], "product-owner"):
    if r["side"] == "skill" and "sk-create-figjam" in r["file"]:
        print(r["id"])' "$SYS" | sort -V)
fi
mkdir -p "$OUT/stdout"
for id in "${IDS[@]}"; do
  # A run that already finished keeps its result, so the batch resumes where it stopped
  if ls "$OUT/skill/$LABEL/$id - "*/meta.json >/dev/null 2>&1; then
    echo "$id $LABEL skipped, already run"
    continue
  fi
  echo "$id $LABEL start $(date -u +%H:%M:%S)"
  python3 "$HERE/adaptive_compare.py" "$SYS" "$OUT" "$LABEL" "$MODEL" "$id" "$KEY" \
    > "$OUT/stdout/$id-$LABEL.txt" 2>&1
  echo "$id $LABEL exit $? $(date -u +%H:%M:%S)"
done
