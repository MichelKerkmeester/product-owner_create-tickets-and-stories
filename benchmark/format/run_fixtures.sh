#!/usr/bin/env bash
# Regression gate for the output-format validator's own mechanics.
#
# Each case pins behavior that regressed once already: a path mask that
# blanked every em dash downstream of a slash, a sanctioned-definition pattern
# anchored at column zero, and a directory argument that crashed instead of
# taking the clean missing-file exit. The conciseness cases at the bottom pin
# the four checks that turned blocking once their vocabulary was written into
# the always-loaded instruction surface.
set -uo pipefail
cd "$(dirname "$0")"

VALIDATOR="./validate-output-format.cjs"
FIXTURES="./fixtures"
failures=0

check() {
  local name="$1" expected_exit="$2" pattern="$3" antipattern="$4"
  shift 4
  local output status
  output="$(node "$VALIDATOR" "$@" 2>&1)"
  status=$?
  if [ "$status" -ne "$expected_exit" ]; then
    echo "FAIL ${name}: expected exit ${expected_exit}, got ${status}"
    echo "${output}" | sed 's/^/     /'
    failures=$((failures + 1))
    return
  fi
  # A herestring, not a pipe: `grep -q` exits on the first match, which sends
  # SIGPIPE back to a writer still streaming, and `pipefail` then reports the
  # pipeline as failed even though the pattern matched. That turned every large
  # advisory report into a false fixture failure.
  if [ -n "$pattern" ] && ! grep -q -- "$pattern" <<< "$output"; then
    echo "FAIL ${name}: output missing ${pattern}"
    echo "${output}" | sed 's/^/     /'
    failures=$((failures + 1))
    return
  fi
  if [ -n "$antipattern" ] && grep -q -- "$antipattern" <<< "$output"; then
    echo "FAIL ${name}: output unexpectedly contains ${antipattern}"
    echo "${output}" | sed 's/^/     /'
    failures=$((failures + 1))
    return
  fi
  echo "PASS ${name}"
}

# A prose em dash after a slash-bearing token stays visible.
check "path mask keeps a real violation" 1 "mask-paths-violation.md:6: prose em dash" "" \
  "${FIXTURES}/mask-paths-violation.md"
check "path mask keeps the second violation" 1 "mask-paths-violation.md:8: prose em dash" "" \
  "${FIXTURES}/mask-paths-violation.md"
check "path mask keeps a dash with slashes on both sides" 1 "mask-paths-violation.md:10: prose em dash" "" \
  "${FIXTURES}/mask-paths-violation.md"

# A dash between two path components is structural and stays exempt.
check "path mask exempts a dash inside a path" 0 "validation passed" "prose em dash" \
  "${FIXTURES}/mask-paths-exempt.md"

# The definition delimiter is sanctioned at any indentation.
check "indented definition bullets are sanctioned" 0 "validation passed" "prose em dash" \
  "${FIXTURES}/sanctioned-definition-nested.md"

# Every shape the card grants an exemption for must clear the gate, or the
# writer is told one thing by the always-loaded rules and another by the gate.
check "card-sanctioned shapes clear the gate" 0 "validation passed" "prose em dash" \
  "${FIXTURES}/sanctioned-shapes.md"

# A directory argument takes the clean missing-target exit, never a stack trace.
check "directory argument exits cleanly" 66 "not a regular file" "EISDIR" "${FIXTURES}"

# The four conciseness checks block, so each needs a case proving it fires and
# a case proving it does not. The silent half matters more: a gate that fires
# on a quoted mention, a single hedge or an informative lead-in gets switched
# off within a week, and then it guards nothing.
check "opener check fires" 1 "conciseness-violation.md:8: sentence opens with" "" \
  "${FIXTURES}/conciseness-violation.md"
check "heading echo check fires" 1 "conciseness-violation.md:12: first sentence restates its heading" "" \
  "${FIXTURES}/conciseness-violation.md"
check "hedge stack check fires" 1 "conciseness-violation.md:16: hedge stack in one sentence" "" \
  "${FIXTURES}/conciseness-violation.md"
check "terminal recap check fires" 1 "conciseness-violation.md:22: section closes on a recap opener" "" \
  "${FIXTURES}/conciseness-violation.md"

# The Delivery section is opt-in, so an all-placeholder one reads as a delivery
# view nobody took. Advice, not a block: the mode reference grants three TBD
# slots for a Delivery the requester asked for, the refinement rule keeps a
# source section's slots untouched, and both scaffolds ship the exact form, so a
# blocking check here fails correct work.
check "all-TBD delivery section advises without blocking" 0 "delivery-placeholder-violation.md:20: Delivery section carries only TBD placeholders" "" \
  "${FIXTURES}/delivery-placeholder-violation.md"
check "a populated delivery slot stays silent" 0 "validation passed" "only TBD placeholders" \
  "${FIXTURES}/delivery-placeholder-exempt.md"

# The Requirements narration check and the Mark-as-done divider rule were both
# pinned by nothing here, and the narration fixtures had sat unused in this
# directory since the commit that created them. A regression that deleted either
# check outright would have printed PASSED.
check "requirements narration fires on the first bullet" 1 "requirements-narration-violation.md:7: Requirements bullet reports what a screen says" "" \
  "${FIXTURES}/requirements-narration-violation.md"
check "requirements narration fires on the second bullet" 1 "requirements-narration-violation.md:8: Requirements bullet reports what a screen says" "" \
  "${FIXTURES}/requirements-narration-violation.md"
check "a quoted string and real constraints stay silent" 0 "validation passed" "reports what a screen says" \
  "${FIXTURES}/requirements-narration-exempt.md"
check "mark-as-done divider fires" 1 "markasdone-divider-violation.md:16: divider follows a Mark-as-done checkbox" "" \
  "${FIXTURES}/markasdone-divider-violation.md"
check "the sanctioned section close above a spacer stays silent" 1 "failed with 1 error(s)" "markasdone-divider-violation.md:24" \
  "${FIXTURES}/markasdone-divider-violation.md"

# The Barter house shape rules, gated on the `* * *` divider so a deliverable in
# another grammar never meets them. The silent half matters more than the loud
# one: a compliant house Story carries a divider under every heading, three
# `TBD...` tokens the ellipsis cap must not count, one `← PRIO` and one emoji.
check "house grammar: a heading with no divider under it fires" 1 "house-grammar-violation.md:5: a content heading with no" "" \
  "${FIXTURES}/house-grammar-violation.md"
check "house grammar: a hyphen rule fires" 1 "house-grammar-violation.md:9: a \`---\` divider in a house-grammar deliverable" "" \
  "${FIXTURES}/house-grammar-violation.md"
check "house grammar: a heading deeper than H4 fires" 1 "house-grammar-violation.md:32: a heading deeper than H4" "" \
  "${FIXTURES}/house-grammar-violation.md"
check "house grammar: a Checklist sub-block in Requirements fires" 1 "house-grammar-violation.md:19: a ..Checklist.. sub-block inside Requirements" "" \
  "${FIXTURES}/house-grammar-violation.md"
check "house grammar: a checkbox in Requirements fires" 1 "house-grammar-violation.md:21: a checkbox item inside Requirements" "" \
  "${FIXTURES}/house-grammar-violation.md"
check "house grammar: asterisk emphasis fires" 1 "house-grammar-violation.md:34: asterisk emphasis" "" \
  "${FIXTURES}/house-grammar-violation.md"
check "house grammar: the ellipsis cap fires" 1 "house-grammar-violation.md: 3 ellipses" "" \
  "${FIXTURES}/house-grammar-violation.md"
check "house grammar: the emoji cap fires" 1 "house-grammar-violation.md: 2 emoji" "" \
  "${FIXTURES}/house-grammar-violation.md"
check "house grammar: a second PRIO marker fires" 1 "house-grammar-violation.md: 2 \`← PRIO\` markers" "" \
  "${FIXTURES}/house-grammar-violation.md"
check "house grammar: a compliant house Story stays silent" 0 "validation passed" "house-grammar" \
  "${FIXTURES}/house-grammar-silent.md"
check "house grammar: the TBD token never counts against the ellipsis cap" 0 "validation passed" "ellipses" \
  "${FIXTURES}/house-grammar-silent.md"
check "house grammar: the rules stay off a deliverable in another grammar" 0 "validation passed" "house-grammar deliverable" \
  "${FIXTURES}/conciseness-silent.md"

check "near-miss prose passes" 0 "validation passed" "" "${FIXTURES}/conciseness-silent.md"
check "opener check stays silent" 0 "validation passed" "sentence opens with" \
  "${FIXTURES}/conciseness-silent.md"
check "heading echo check stays silent" 0 "validation passed" "restates its heading" \
  "${FIXTURES}/conciseness-silent.md"
check "one hedge stays silent" 0 "validation passed" "hedge stack" \
  "${FIXTURES}/conciseness-silent.md"
check "terminal recap check stays silent" 0 "validation passed" "recap opener" \
  "${FIXTURES}/conciseness-silent.md"

# The length caps advise on a deliverable and never block, so the violation
# fixture still exits 0 and the near-miss fixture prints no advice at all.
check "length caps: a third About paragraph warns" 0 "length-caps-violation.md:3: About opening holds 3 paragraphs" "" \
  "${FIXTURES}/length-caps-violation.md"
check "length caps: a bullet over 25 words warns" 0 "length-caps-violation.md:13: bullet runs 28 words" "" \
  "${FIXTURES}/length-caps-violation.md"
check "length caps: a two-sentence bullet warns" 0 "length-caps-violation.md:14: bullet holds 2 sentences" "" \
  "${FIXTURES}/length-caps-violation.md"
check "length caps: a paragraph over 60 words warns" 0 "length-caps-violation.md:18: paragraph runs 61 words" "" \
  "${FIXTURES}/length-caps-violation.md"
check "length caps: a four-sentence paragraph warns" 0 "length-caps-violation.md:20: paragraph holds 4 sentences" "" \
  "${FIXTURES}/length-caps-violation.md"
check "length caps: a requirement opening on a plain When is no Given/When/Then line" 0 "length-caps-violation.md:24: bullet runs 31 words" "" \
  "${FIXTURES}/length-caps-violation.md"
check "length caps: lines at the caps, code, tables, quotes and Given/When/Then stay silent" 0 "validation passed" "over the" \
  "${FIXTURES}/length-caps-silent.md"
check "length caps: a References block inside About is not counted as its opening" 0 "validation passed" "About opening" \
  "${FIXTURES}/length-caps-silent.md"

if [ "$failures" -ne 0 ]; then
  echo "${failures} format-validator fixture(s) failed"
  exit 1
fi
echo "PASSED all format-validator fixtures"
