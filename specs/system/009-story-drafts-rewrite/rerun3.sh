#!/usr/bin/env bash
# Second pass on the three stories whose first pass turned UI mechanics into
# acceptance criteria. Same model, same router, one extra sentence of steer.
ROOT="/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems"
OUT="$(dirname "$0")"; R="$OUT/rerun3.tsv"; printf "seconds\texit\tfile\n" > "$R"
one() {
  local f="$1" tag="$2" s e secs rc
  s=$(perl -MTime::HiRes=time -e 'print time')
  ( cd "$ROOT" && pi -p --provider llmgateway --model deepseek-v4-flash:max -- \
    "/agent-router product owner \$story the Story at \"$f\" has too many acceptance criteria and several of them describe UI mechanics rather than outcomes. Rewrite it in place at that exact path from the same source, keeping the criteria to the few outcomes a user relies on per surface, moving any fixed mechanic such as gesture, angle, ratio or column behaviour into Requirements as a hard constraint, and letting the prose carry the reasoning. No numbered export, and no reference to the screenshots in that folder, they get embedded in ClickUp." \
    < /dev/null ) > "$OUT/rerun-$tag.txt" 2>&1
  rc=$?; e=$(perl -MTime::HiRes=time -e 'print time'); secs=$(perl -e "printf '%.1f', $e-$s")
  printf "%s\t%s\t%s\n" "$secs" "$rc" "$f" >> "$R"; echo "[$tag] ${secs}s exit=$rc"
}
one "/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/Product Owner/export/Story Drafts/Content Gallery - Highlights - Edit Reel UX/Content Gallery - Highlights - Edit Reel UX.md" edit-reel &
one "/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/Product Owner/export/Story Drafts/Creator - Media Editor/Creator - Media Editor.md" media-editor &
one "/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/Product Owner/export/Story Drafts/Onboarding - Birthday/Onboarding - Birthday.md" birthday &
wait; echo complete
