#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const systemRoot = path.resolve(__dirname, '../..');
const skillRoot = path.join(systemRoot, 'sk-product-owner');

const args = process.argv.slice(2);
const write = args.includes('--write');
const flags = new Set(args.filter((arg) => arg.startsWith('--')));
const targets = args.filter((arg) => !arg.startsWith('--'));

const unknownFlag = [...flags].find((flag) => flag !== '--write');
if (unknownFlag) {
  console.error(`Unknown flag: ${unknownFlag}`);
  console.error('Usage: validate-output-format.cjs [--write] [file ...]');
  process.exit(64);
}
if (write && targets.length) {
  console.error('--write reformats the skill sources and cannot be combined with an explicit file list.');
  process.exit(64);
}

function markdownFiles(directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const target = path.join(directory, entry.name);
    if (entry.isSymbolicLink()) return [];
    if (entry.isDirectory()) return markdownFiles(target);
    return entry.isFile() && entry.name.endsWith('.md') ? [target] : [];
  });
}

// The four shared rule files are regular-file copies of cards governed once at
// the shared knowledge hub, carried as copies so this system works as its own
// repository. The walk leaves all four out, and the two always-loaded cards are
// named here explicitly instead. They are the strictest-enforced files in the
// system and the ones the whole fleet reads, so dropping either from the lint
// would remove the check exactly where it matters most.
const sharedCopies = new Set(
  ['conciseness-rationale.md', 'conciseness.md', 'human-voice-rules.md', 'hvr-core.md'].map((name) =>
    path.join(skillRoot, 'references', name),
  ),
);
const sourceFiles = [
  path.join(systemRoot, 'AGENTS.md'),
  path.join(skillRoot, 'SKILL.md'),
  path.join(skillRoot, 'README.md'),
  path.join(skillRoot, 'references', 'hvr-core.md'),
  path.join(skillRoot, 'references', 'conciseness.md'),
  ...[
    ...markdownFiles(path.join(skillRoot, 'references')),
    ...markdownFiles(path.join(skillRoot, 'assets')),
  ].filter((file) => !sharedCopies.has(file)),
  path.join(systemRoot, 'claude project', 'Custom Instructions.md'),
];

// An explicit path argument lints that artifact instead of the skill's own
// sources, so a produced deliverable can be checked before it ships.
const lintingArtifacts = targets.length > 0;
const files = lintingArtifacts ? targets.map((target) => path.resolve(process.cwd(), target)) : sourceFiles;

// A path that is absent, or that exists but is not a regular file (a
// directory being the common slip), fails here with the same clean exit
// instead of throwing an unhandled EISDIR out of the read loop below.
const describeUnreadable = (file) => {
  if (!fs.existsSync(file)) return `${file}: no such file`;
  return `${file}: not a regular file`;
};
const unreadable = files.filter((file) => !fs.existsSync(file) || !fs.statSync(file).isFile());
if (unreadable.length) {
  console.error(unreadable.map(describeUnreadable).join('\n'));
  process.exit(66);
}

// The Human Voice punctuation pass blocks on the files that teach the voice,
// and reports advice everywhere else. The bullet punctuation and
// acceptance-spacing rules block on every file, since both are contracts the
// artifact templates state outright. The four conciseness checks below that
// pass (opener, hedge stack, terminal recap, heading echo) now block on every
// file too: the always-loaded conciseness layer states their vocabulary
// outright, so a writer is never failed for wording no instruction file gave
// them. A guard near the bottom of this file fails if a term drifts into a
// list here without being written into that layer. The bullet-ratio and
// heading-density statistics raise nothing at all, because a ratio over a whole
// file is evidence rather than a rule, and both were measured against sanctioned
// house output that sits outside their bands. Four checks apply to a deliverable alone:
// artifact purity, the two cut rules that resolve without judgement, the two
// over-compression floors that hold the keep side at the same strength, and the
// three deal artifact rules, which reach a document carrying the deal export's
// own two section headings and nothing else. The card's blocker vocabulary runs
// in both modes, read out of the card itself rather than retyped, so the list
// the writer is given and the list the gate holds cannot drift apart.
const hvrEnforced = new Set([
  path.join(systemRoot, 'AGENTS.md'),
  path.join(skillRoot, 'SKILL.md'),
  path.join(skillRoot, 'references', 'hvr-core.md'),
  path.join(skillRoot, 'references', 'conciseness.md'),
  path.join(skillRoot, 'references', 'story-mode.md'),
  path.join(skillRoot, 'references', 'doc-mode.md'),
  path.join(systemRoot, 'claude project', 'Custom Instructions.md'),
]);

const hvrCard = path.join(skillRoot, 'references', 'hvr-core.md');

// The full standard the card names as its authority. The card carries a subset
// of it, so this is the file a card term is checked against.
const hvrStandard = path.join(skillRoot, 'references', 'human-voice-rules.md');

// This system measures zero blocker terms across its whole source perimeter once
// the card itself is set aside, so the vocabulary pass blocks in both modes,
// exactly as the bullet punctuation rule does and for the same reason.
const vocabularyBlocks = true;

const errors = [];
const advisories = [];
// The Mark-as-done line in either checkbox form, so the divider rule and the
// stripper still hold on an artifact written before the house dropped the space.
const MARK_AS_DONE = /^- \[ ?\] _Mark as done, if the criteria are met_$/;

// A divider sitting directly above a same-level empty spacer heading closes the
// whole H2 section, which is what the Barter house PRDs do at the end of
// Acceptance criteria, Scope and Requirements. The banned divider is the one
// that separates a criterion's Mark-as-done line from the next criterion, so
// only that case is an error. A spacer heading is hashes plus whitespace, whose
// trim is the hashes, which keeps it visible to the same non-empty content scan.
const SPACER_HEADING = /^#{2,4}[ \t]+$/;
const closesSection = (lines, dividerIndex) => {
  const nextIndex = lines.findIndex((line, index) => index > dividerIndex && line.trim() !== '');
  return nextIndex >= 0 && SPACER_HEADING.test(lines[nextIndex]);
};

// --- masking -----------------------------------------------------------
// Quoted spans hold cited material, so a document naming a banned phrase is
// not using it. Path-like spans carry structural punctuation that no voice
// rule governs. Both are blanked before any prose rule runs.
const maskInlineCode = (line) => line.replace(/`[^`]*`/g, (match) => ' '.repeat(match.length));
const maskQuoted = (line) => line.replace(/"[^"]*"/g, (match) => ' '.repeat(match.length));

// An HTML comment renders as nothing, so a metadata header written as one is
// addressed to the toolchain rather than to the reader. Comment spans are
// blanked before the artifact-purity pass below, which is what keeps the
// sanctioned line-1 score header silent. Blanking rather than dropping keeps
// every finding pointing at the line it came from.
function withoutHtmlComments(lines) {
  let open = false;
  return lines.map((line) => {
    let out = '';
    let rest = line;
    while (rest.length) {
      if (open) {
        const close = rest.indexOf('-->');
        if (close === -1) {
          out += ' '.repeat(rest.length);
          break;
        }
        out += ' '.repeat(close + 3);
        rest = rest.slice(close + 3);
        open = false;
        continue;
      }
      const start = rest.indexOf('<!--');
      if (start === -1) {
        out += rest;
        break;
      }
      out += rest.slice(0, start);
      rest = rest.slice(start);
      open = true;
    }
    return out;
  });
}

// A spaced dash is exempt only when it sits between two path components: the
// text touching it on the left ends in a slash segment with no space in it,
// and the text on the right continues into another slash. That is what a
// directory named `z — Product Owner` needs. The earlier form exempted any
// dash downstream of any slash-bearing token, which silently swallowed real
// violations such as `docs/guide — this` and `and/or — missed`.
const PATH_INTERNAL_DASH = /(?<=\/[A-Za-z0-9_.~$#%+-]+)\s[—–]\s(?=[A-Za-z0-9_.~$#%+ -]*\/)/g;
const PATH_RUN = /[A-Za-z0-9_.~$#%+/-]*\/[A-Za-z0-9_.~$#%+/-]*/g;
const blank = (match) => ' '.repeat(match.length);
const maskPaths = (line) =>
  line
    .replace(/https?:\/\/\S+/g, blank)
    .replace(PATH_INTERNAL_DASH, blank)
    .replace(PATH_RUN, blank);

// A sanctioned shape stays sanctioned wherever it sits. Indentation, a
// blockquote marker and a checkbox are all containers, not content, so strip
// them before testing rather than teaching every pattern about each one.
const stripContainers = (line) =>
  line.replace(/^\s*(?:>\s?)*\s*/, '').replace(/^(\* {3})(?:\[[ xX]?\] )/, '$1');

// A leaked process line arrives wrapped in whatever container it sat in: an
// indent, a blockquote marker, a list marker, a bold run. Stripping the wrapper
// before the anchored purity patterns run is what lets one pattern match the
// line whether it shipped bare or as a bullet.
const stripLeadIn = (line) =>
  line
    .replace(/^\s*(?:>\s?)*\s*/, '')
    .replace(/^(?:[-*+]\s+|\d+[.)]\s+)/, '')
    .replace(/^(?:\*\*|__|\*|_)\s*/, '');
const stripEmphasis = (text) => text.replace(/[*_]+/g, '');

// The definition delimiter names a term and then defines it.
const SANCTIONED_DEFINITION = /^\* {3}\*\*.+?\*\* — /;

// A status notice carries a source class and then the scope it covers. The
// qualifier routinely contains its own commas, so a comma delimiter would
// hide where the label ends and the scope begins.
const SANCTIONED_STATUS = /^(?:\* {3})?(?:\*\*)?Status:(?:\*\*)?\s.+ — /;

// --- word lists --------------------------------------------------------
// The first three lists drive blocking checks. Every term in them is stated
// verbatim in the always-loaded conciseness layer, which is what earns them
// the right to block: the writer is given the same list the gate holds. The
// STATED_VOCABULARY guard below keeps the two halves identical, so a term
// added here without being written into that file fails the run instead of
// silently punishing wording nobody was told about.
const SENTENCE_OPENERS = [
  'in conclusion', 'in summary', 'to summarize', 'to summarise', 'to recap', 'to sum up',
  "it's worth noting", 'it is worth noting', "it's important to note", 'it is important to note',
  "let's explore", "let's dive in", "let's take a look", 'at the end of the day',
  'without further ado', 'as we all know', 'it goes without saying', 'first and foremost',
  'last but not least', 'with that in mind', 'on that note', 'that said', 'needless to say',
  'simply put', 'in essence', 'at its core', 'in the world of', 'when it comes to',
  // Widened once each term was verified absent from every export and every
  // instruction source in the fleet. A cross-reference that names its target
  // stays legitimate, which is why only the forms pointing at nothing are here.
  'at a high level', 'as you can see', 'as mentioned above', 'as noted above',
  'as previously noted', 'as we have seen', 'as discussed above', 'in this section',
  'put simply', 'generally speaking', 'broadly speaking', 'the key takeaway',
  'the fact of the matter is', 'it should be noted', 'it must be noted',
  'by way of background',
];

const RECAP_OPENERS = [
  'in summary', 'in conclusion', 'to summarize', 'to summarise', 'to recap', 'to sum up',
  'in short', 'all in all', 'overall', 'ultimately', 'in closing',
  'to conclude', 'to wrap up', 'the takeaway', 'net net', 'in a nutshell',
  'long story short', 'to put it simply', 'on the whole',
];

const HEDGES = [
  'might', 'may', 'could', 'perhaps', 'maybe', 'possibly', 'potentially', 'probably',
  'seems', 'appears', 'arguably', 'somewhat', 'relatively', 'presumably', 'likely',
  'generally', 'typically', 'i think', 'i believe', 'tends to',
  // Uncertainty markers with no content of their own. A rate, a proportion or a
  // degree on a quantity is deliberately absent: the scope qualifier and the
  // specific number are keep rules, so banning "often" or "roughly" would fail
  // correct writing.
  'to some extent', 'in some cases', 'apparently', 'conceivably', 'ostensibly',
  'seemingly', 'in theory', 'i suspect', 'my sense is',
];

const STOPWORDS = new Set([
  'a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for', 'from', 'how', 'in', 'into',
  'is', 'it', 'its', 'no', 'not', 'of', 'on', 'or', 'per', 'so', 'than', 'that', 'the', 'then',
  'these', 'this', 'those', 'to', 'use', 'used', 'uses', 'was', 'were', 'what', 'when', 'which',
  'who', 'why', 'with', 'all', 'any', 'new', 'do', 'does', 'if', 'you', 'your',
]);

// Words a restating sentence leans on while adding no information of its own.
const FILLER_WORDS = new Set([
  'section', 'describe', 'describes', 'explain', 'explains', 'cover', 'covers', 'outline',
  'outlines', 'provide', 'provides', 'define', 'defines', 'detail', 'details', 'overview',
  'following', 'below', 'above', 'here', 'important', 'key', 'essential', 'critical',
  'various', 'several', 'help', 'helps', 'ensure', 'ensures', 'about', 'discuss', 'discusses',
  'introduce', 'introduces', 'present', 'presents', 'summarise', 'summarize', 'part',
]);

// Semantic connectives carry the logic of a sentence. A count near zero in
// explanatory prose is the mechanical signature of over-compression, which is
// why this statistic guards the keep side rather than the cut side.
const SEMANTIC_CONNECTIVES = [
  'because', 'so that', 'unless', 'which means', 'while', 'although', 'though', 'since',
  'whereas', 'in order to', 'rather than', 'instead of', 'when', 'if', 'until', 'before',
  'after', 'so',
];

const contentWords = (text) =>
  text
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, ' ')
    .split(/\s+/)
    .filter((word) => word.length >= 3 && !STOPWORDS.has(word))
    .map((word) => word.replace(/s$/, ''))
    .filter((word) => word.length >= 3 && !STOPWORDS.has(word));

const startsWithAny = (sentence, openers) => {
  const normalised = sentence.trim().toLowerCase().replace(/^[*_#>\s-]+/, '');
  return openers.find((opener) => normalised.startsWith(opener));
};

// --- the Human Voice blocker vocabulary --------------------------------
// The always-loaded card carries the whole blocker list inline, so the gate
// reads that list out of the card rather than keeping a second copy of it. A
// second copy is how the card and the gate come to disagree, and the writer is
// the one who pays for the disagreement. Sections 3 to 7 hold the blocking
// material: the hard blocker words as one bare comma list, then a quoted phrase
// list each for blocker phrases, banned metaphors, setup language and
// generalisations.
//
// Three things the card states stay out of the blocking list on purpose. The
// terms on the card's own "allowed when literal" line, because the card itself
// withholds them from unconditional blocking. A term carrying a bracketed
// placeholder, because that is a shape rather than a string to match. And the
// inflections of the six words named below.
const CARD_SECTION_NUMBERS = [3, 4, 5, 6, 7];
const CARD_WORD_SECTION = 3;
const CARD_LITERAL_NOTE = /^Blocked as metaphor, allowed when literal:/;
const CARD_HEADING = /^##\s+\d+\./;
const CARD_CONTRAST_STATEMENT = 'Not just X, but Y';

// A word whose literal reading is ordinary English reports as advice in both
// modes rather than blocking, because the past and progressive forms are
// precisely where the literal reading lives: a test harness, a curated set, an
// elevated surface. A check that fails a build over "test harness" is switched
// off inside a week, and the other ninety-six terms go unguarded with it, so
// advice that stays visible buys more than a rule nobody leaves turned on. The
// inflections are still matched. Demoting the severity is the whole grant, and
// dropping the inflected forms on top of it removed six card-declared blockers
// from enforcement altogether: "harness" reported and "fosters" reported
// nothing at all. Each consuming system states this demotion on its own
// surfaces, and the guard at the bottom of this file fails the run when the
// statement is gone.
const LITERAL_SENSE = ['harness', 'foster', 'nurture', 'curate', 'elevate', 'resonate'];

// The card enumerates two of its own inflected pairs, so a stated form alone
// would let "leveraging" and "delving" through a gate that stops at "leverage"
// and "delve". Regular inflection closes that without inventing vocabulary: an
// inflection of a banned word is the banned word.
function inflections(word) {
  const forms = new Set([word]);
  if (word.endsWith('e')) {
    forms.add(`${word}s`);
    forms.add(`${word}d`);
    forms.add(`${word.slice(0, -1)}ing`);
  } else if (/(?:[sxz]|ch|sh)$/.test(word)) {
    forms.add(`${word}es`);
    forms.add(`${word}ed`);
    forms.add(`${word}ing`);
  } else {
    forms.add(`${word}s`);
    forms.add(`${word}ed`);
    forms.add(`${word}ing`);
  }
  return [...forms];
}

const escapeTerm = (term) => term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/\s+/g, '\\s+');

// A hyphen is part of "game-changer" and a boundary nowhere else here, so the
// fences are letter-and-digit lookarounds rather than a word boundary.
const termPattern = (forms) =>
  new RegExp(`(?<![A-Za-z0-9])(?:${forms.map(escapeTerm).join('|')})(?![A-Za-z0-9])`, 'i');

// "Not just X, but Y" is a shape rather than a term, so it needs its own
// pattern. The card states it, which is what earns it the right to block.
const CONTRAST_BAN = /(?<![A-Za-z0-9])not just(?![A-Za-z0-9])[^.!?]{0,80}?,\s+but(?![A-Za-z0-9])|(?<![A-Za-z0-9])not only(?![A-Za-z0-9])[^.!?]{0,80}?(?<![A-Za-z0-9])but(?![A-Za-z0-9])/i;

function cardSection(lines, number) {
  const start = lines.findIndex((line) => new RegExp(`^##\\s+${number}\\.\\s`).test(line));
  if (start === -1) return [];
  const after = lines.findIndex((line, index) => index > start && CARD_HEADING.test(line));
  return lines.slice(start + 1, after === -1 ? lines.length : after);
}

function readCardVocabulary(cardPath) {
  if (!fs.existsSync(cardPath) || !fs.statSync(cardPath).isFile()) {
    return { missing: true, sections: {}, terms: [], contrastStated: false };
  }
  const lines = fs.readFileSync(cardPath, 'utf8').split(/\r?\n/);
  const sections = {};
  for (const number of CARD_SECTION_NUMBERS) {
    const body = cardSection(lines, number);
    if (number === CARD_WORD_SECTION) {
      const listLine = body.find(
        (line) => line.trim() && !CARD_LITERAL_NOTE.test(line.trim()) && !/^-{3,}$/.test(line.trim()),
      );
      sections[number] = listLine ? listLine.split(',').map((word) => word.trim()).filter(Boolean) : [];
      continue;
    }
    sections[number] = body.flatMap((line) => (line.match(/"[^"]+"/g) || []).map((span) => span.slice(1, -1)));
  }
  const stated = CARD_SECTION_NUMBERS.flatMap((number) => sections[number]);
  const literalNote = lines.find((line) => CARD_LITERAL_NOTE.test(line.trim())) || '';
  const granted = new Set(
    literalNote
      .replace(/^.*allowed when literal:\s*/, '')
      .replace(/\.\s*$/, '')
      .split(',')
      .map((word) => word.trim().toLowerCase())
      .filter(Boolean),
  );
  const single = new Set(sections[CARD_WORD_SECTION].map((word) => word.toLowerCase()));
  const literal = new Set(LITERAL_SENSE);
  const terms = [];
  const seen = new Set();
  // The metaphor lists spell one granted term with an article in front of it, so
  // the grant is matched against the bare term. Reading the grant narrowly would
  // put the same words back under an unconditional ban one section later, which
  // is the card contradicting itself through the gate.
  const bare = (term) => term.replace(/^(?:a|an|the)\s+/, '');
  for (const raw of stated) {
    const term = raw.toLowerCase();
    if (term.includes('[') || granted.has(term) || granted.has(bare(term)) || seen.has(term)) continue;
    seen.add(term);
    const literalSense = literal.has(term);
    const forms = single.has(term) && !/\s/.test(term) ? inflections(term) : [term];
    terms.push({ term, literalSense, pattern: termPattern(forms) });
  }
  return {
    missing: false,
    sections,
    granted: [...granted],
    terms,
    contrastStated: lines.some((line) => line.includes(CARD_CONTRAST_STATEMENT)),
  };
}

// The blocker list comes out of the always-loaded card, so the card is read once
// per run rather than once per file. A card the run cannot read leaves the
// vocabulary pass guarding nothing, which has to be loud in both modes rather
// than only in the source-mode absence check further down.
const vocabulary = readCardVocabulary(hvrCard);
if (vocabulary.missing && lintingArtifacts) {
  errors.push(`${hvrCard}: the ALWAYS-loaded Human Voice card is absent, so its blocker list cannot be read`);
}

// --- artifact purity ---------------------------------------------------
// A deliverable carries the deliverable. A score, a dimension breakdown, a
// voice self-scan, a hard blocker count and an assumption ledger are delivery
// metadata: they belong in the reply, and inside the file only in the line-1
// HTML comment, which renders as nothing and is the one place a reader never
// sees. These patterns run on a produced artifact and never on an instruction
// file, which has to be able to state each shape in order to teach it.
//
// Precision comes from anchoring, not from vocabulary. "Score", "scores" and
// "rating" are ordinary words in a ratings requirement, and the corpus holds a
// real one reading "which scores strongest and which weakest", so the ban
// reaches a heading whose own leading word is the report label and a body line
// whose own opening is the report. It never reaches the word wherever it falls.
const PROCESS_ACRONYM = /\b(?:MEQT|HVR)\b/i;
const PROCESS_DEAL_SCORE = /\bDEAL\s+(?:scoring|score)\b|\bDEAL\s+\d{1,2}\s*\/\s*\d{1,2}\b/;
const PROCESS_HEADING_LABEL = /^(?:Scoring|Self-scan|Hard blockers?|Weakest|Quality Score|Validation checklist|Gate roster|Template compliance|Compliance report)\b/i;
const SELF_SCAN_LINE = /^HVR self-scan\s*:/i;
const HARD_BLOCKER_REPORT = /\bhard blockers?\s*:|\b(?:no|zero|passes|fails|failed|\d+)\s+(?:HVR\s+)?hard blockers?\b|\bHVR\s+hard blockers?\b/i;
const SCORE_DIMENSION_LINE = /\bM\s*\d+\s*[^\w\s]{0,2}\s*E\s*\d+\s*[^\w\s]{0,2}\s*Q\s*\d+|\bD\s*\d+\s*[^\w\s]{0,2}\s*E\s*\d+\s*[^\w\s]{0,2}\s*A\s*\d+\s*[^\w\s]{0,2}\s*L\s*\d+/;
const SCORE_COMMENTARY = /^(?:(?:Two|Three)\s+)?Weakest(?:\s+two)?\s*:/i;
const ASSUMPTION_TAG = /\[Assumes\s*:/i;

// The rest of the delivery-metadata enumeration, each anchored to a label the
// process owns rather than to a word a deliverable might use. "Mode:" alone is
// an ordinary field label in product copy, a dark mode row or a payment mode, so
// the value has to name the router's own vocabulary before the line reads as
// metadata. The same reasoning runs through every pattern here: a total is a
// total only over a denominator, a verdict is one of the two house band labels
// and nothing else, and an attestation names the artifact it vouches for. All of
// them are matched against the line with its lead-in and emphasis runs removed,
// so a bolded label is the same finding as a bare one.
const METADATA_MODE_LINE = /^Mode\s*:\s*\$?(?:task|subtask|bug|doc|story|epic|prd|interactive|quick|raw|standard|deep)\b/i;
const METADATA_TEMPLATE_LINE = /^Template\s*:\s*(?:v\d|version\s*\d|task|bug|doc|story|epic)\b/i;
const METADATA_ENERGY_LINE = /^Energy\s*:\s*(?:raw|quick|standard|deep)\b/i;
const METADATA_PERSPECTIVES_LINE = /^Perspectives\s*:\s*(?:user|business|technical|risk|delivery)\b/i;
const SCORE_TOTAL_LINE = /^Total\s*:\s*\d+(?:\.\d+)?\s*\/\s*\d+/i;
const FLOOR_STATUS_LINE = /^Floor status\s*:/i;
const BAND_VERDICT_LINE = /^(?:REVISION NEEDED|REJECTED)\s*[.:]?\s*$/;
const REVISION_CYCLE_LINE = /^(?:Round|Cycle|Iteration)\s+\d+\s+of\s+\d+\b/i;
const RESCORE_REPORT = /\bre-?scor(?:e|ed|es|ing)\b|\b(?:applied|ran|took)\s+\d+\s+(?:revision\s+)?cycles?\b/i;
const PHASE_FLOW_TRACE = /\bD\s*->\s*(?:E\s*->\s*)?P\s*->\s*(?:T\s*->\s*)?H\b/;
const ATTESTATION = /\b(?:I|we)\s+(?:hereby\s+)?attest\b|\battest(?:s|ed)?\s+(?:that\s+)?(?:this|the)\s+(?:artifact|document|deliverable|story|epic|doc|output|export)\b/i;

// A Quality or Score heading cannot be banned on its own words: "Quality checks"
// opens a real review section and a ratings requirement legitimately reads
// "which scores strongest and which weakest". The section body settles it. A
// Quality or Score heading whose own section then carries a score line is the
// report shape the ban exists to keep out, and the same heading over ordinary
// content is not.
const SCORE_SECTION_HEADING = /^(?:Quality|Scores?)\b/i;

// The house divider. A deliverable carrying `* * *` is written in the Barter
// house grammar, which is what earns it the three shape rules below: the `---`
// substitution ban, the divider that follows every content heading, and the H4
// depth cap. A deliverable in any other grammar never meets them, exactly as a
// document that is not a deal export never meets the deal rules above.
const HOUSE_DIVIDER = /^\* \* \*$/;
const HYPHEN_RULE = /^-{3,}$/;
const CONTENT_HEADING = /^#{2,6}[ \t]+\S/;
const DEEP_HEADING = /^#{5,6}[ \t]+\S/;
const REQUIREMENTS_CHECKLIST = /^\*{2}Checklist\*{2}/;
// A checkbox in either form, `[]` as the house writes it or `[ ]` as older
// artifacts do, capturing the item text.
const CHECKBOX_ITEM = /^(?:\*\s{3}|[-*+]\s)\[[ xX]?\]\s+(.*\S)\s*$/;
const SPACED_CHECKBOX = /^\s*(?:\*\s{3}|[-*+]\s)\[ \]/;
const PRIO_MARKER = /← PRIO/g;

// The card's two per-piece caps and its asterisk-emphasis ban. `TBD...` is the
// one named ellipsis exemption, so it is subtracted before the count. The
// emphasis span is a single asterisk pair that is not half of a `**` run, read
// after the list marker is removed so the house bullet `*   ` and the divider
// `* * *` are not read as one.
const LIST_MARKER = /^\s*(?:\*\s{3}|[-*+]\s|\d+[.)]\s)/;
const EMPHASIS_SPAN = /(?<![\\*])\*(?![*\s])[^*\n]*[^*\s]\*(?!\*)/;
// A pictograph, not every non-Latin glyph: the arrow block stays out because
// `←` is a house priority marker, and the dash and quote ranges stay out
// because the punctuation pass already owns them.
const PICTOGRAPH = /[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}\u{2B00}-\u{2BFF}]/gu;
const ELLIPSIS = /\.\.\./g;
const TBD_TOKEN = /TBD\.\.\./g;

// One finding per line, named for the shape it is, so a leaked block reports
// what it is rather than every pattern it happens to touch.
function processShape(visible) {
  const heading = visible.match(/^\s*#{1,6}\s+(\S.*?)\s*$/);
  if (heading) {
    const text = stripEmphasis(heading[1]);
    if (PROCESS_ACRONYM.test(text) || PROCESS_DEAL_SCORE.test(text) || PROCESS_HEADING_LABEL.test(text)) {
      return 'a scoring section heading';
    }
  }
  const bare = stripLeadIn(visible);
  const label = stripEmphasis(bare);
  if (SELF_SCAN_LINE.test(bare)) return 'a voice self-scan line';
  if (HARD_BLOCKER_REPORT.test(visible)) return 'a hard blocker report';
  if (SCORE_DIMENSION_LINE.test(visible)) return 'a score dimension line';
  if (SCORE_COMMENTARY.test(bare)) return 'score commentary';
  if (ASSUMPTION_TAG.test(visible)) return 'an assumption tag';
  if (SCORE_TOTAL_LINE.test(label)) return 'a score total';
  if (FLOOR_STATUS_LINE.test(label)) return 'a floor status line';
  if (BAND_VERDICT_LINE.test(label)) return 'a score band verdict';
  if (
    METADATA_MODE_LINE.test(label)
    || METADATA_TEMPLATE_LINE.test(label)
    || METADATA_ENERGY_LINE.test(label)
    || METADATA_PERSPECTIVES_LINE.test(label)
  ) {
    return 'a process metadata header';
  }
  if (REVISION_CYCLE_LINE.test(label) || RESCORE_REPORT.test(visible)) return 'an improvement-cycle note';
  if (PHASE_FLOW_TRACE.test(visible)) return 'a phase-flow trace';
  if (ATTESTATION.test(visible)) return 'an attestation footer';
  return null;
}

// Three rules the card and the mode references state that no check here holds,
// each with the measurement that settled it. A gate that fires on compliant work
// gets switched off, and then the rules it did hold go unguarded with it.
//
// The Oxford comma needs a list parser with quote masking. A bare regex reads the
// clause-level "the count is five, and the floor is fifty" as a serial list, and
// that construction is ordinary in every Requirements section in the tree.
//
// Title-case headings are heuristic in the general case. The rule at
// doc-mode.md:95 exempts proper nouns, acronyms and literal identifiers, so a
// stop-word pass would flag `### Instagram ReAuth on iOS`, and the card grants
// two all-caps Bug Mode labels and the deal export's own two headings outright.
// The all-caps form alone is safely catchable and is what those grants cover, so
// there is nothing left to check once they are honoured.
//
// The wider Requirements narration class, a bullet saying a screen shows,
// displays, contains or presents something, is not mechanically separable from a
// constraint. Measured across the worked examples and the numbered export drafts:
// the narrow four-verb set hits zero compliant bullets and the wider set hits
// sixteen, among them "The control bar shows rotate left, crop and rotate right,
// in that order", which is a constraint a build can fail. Requirements still
// needs a reader.
//
// The Story presence rules, the verbatim preamble, the required heading set and
// `1\.` numbering on acceptance criteria, stay out for a different reason than the
// three above. They are create-time shape checks, and story-mode.md exempts a
// source-preserving refinement from every one of them by name, so a refinement of
// a Story written before the preamble rule keeps its own opening and is correct
// output. Nothing in the file says whether it was created or refined. The divider
// rules below survive that problem because a refinement that preserves a
// non-house source carries no house divider and never meets them, which is not
// true of a rule that fires on something being absent. Measured for the record:
// 21 of the 22 deliverables carrying `## Acceptance criteria` carry the verbatim
// preamble, the one that does not is an Epic and correctly omits it, and none has
// an unnumbered criteria block.

// --- the house grammar shape -------------------------------------------
// Gated on the house divider, the same way the deal rules are gated on the deal
// export's headings, so a deliverable in another grammar never meets them.
// Measured across the twenty-nine house-grammar worked examples, scaffold
// instances and numbered exports in the tree: zero findings on all three rules,
// and sixty-six `---` rules in the fourteen plain-grammar deliverables the rules
// correctly leave alone.
function houseGrammarFindings(prose, lines) {
  if (!prose.some(({ visible }) => HOUSE_DIVIDER.test(visible.trim()))) return [];
  const findings = [];
  const proseStart = frontmatterEnd(lines);
  for (const { index, visible } of prose) {
    if (index < proseStart) continue;
    const text = visible.trim();
    if (HYPHEN_RULE.test(text)) {
      findings.push({ index, message: 'a `---` divider in a house-grammar deliverable, where `* * *` is the divider' });
      continue;
    }
    if (DEEP_HEADING.test(text)) {
      findings.push({ index, message: 'a heading deeper than H4, where a bold paragraph lead carries the level below it' });
      continue;
    }
    if (!CONTENT_HEADING.test(text)) continue;
    const next = lines.slice(index + 1).find((line) => line.trim() !== '');
    if (next === undefined || !HOUSE_DIVIDER.test(next.trim())) {
      findings.push({ index, message: 'a content heading with no `* * *` divider on the line below it' });
    }
  }
  return findings;
}

// --- the score section shape -------------------------------------------
// One pass rather than one line, because the heading and the body decide this
// together. The section runs to the next heading at the same level or above.
function scoreSectionFindings(prose) {
  const findings = [];
  const rows = prose.map(({ index, visible }) => ({ index, text: visible.trim() }));
  rows.forEach(({ index, text }, position) => {
    const heading = text.match(/^(#{1,6})\s+(\S.*?)\s*$/);
    if (!heading) return;
    if (!SCORE_SECTION_HEADING.test(stripEmphasis(heading[2]))) return;
    const depth = heading[1].length;
    const body = [];
    for (let cursor = position + 1; cursor < rows.length; cursor += 1) {
      const later = rows[cursor].text.match(/^(#{1,6})\s+/);
      if (later && later[1].length <= depth) break;
      body.push(rows[cursor].text);
    }
    const scored = body.find((line) => {
      const bare = stripEmphasis(stripLeadIn(line));
      return (
        SCORE_DIMENSION_LINE.test(line)
        || SCORE_TOTAL_LINE.test(bare)
        || FLOOR_STATUS_LINE.test(bare)
        || BAND_VERDICT_LINE.test(bare)
        || HARD_BLOCKER_REPORT.test(line)
      );
    });
    if (scored !== undefined) {
      findings.push({ index, message: 'a scoring section heading' });
    }
  });
  return findings;
}

// --- the deal artifact shape -------------------------------------------
// Three rules a deal export carries, each with a fixed string behind it, so all
// three settle without judgement. They run on a deliverable that carries the
// export's own two section headings, which is what keeps them off a voice
// snippet, a score reply, a self-scan reply and every instruction file that has
// to state the same strings in order to teach them.
//
// The creator-fit label is one Barter app field, so its wording never varies. No
// other field label in the format ends in the word "for:", which is what makes a
// bold label line of that shape and not reading the fixed label a defect with no
// legitimate case behind it. Verified across the whole source perimeter: the
// only line of that shape is the fixed label, twenty-four times, no collisions.
const DEAL_HEADLINE_HEADING = /^##\s+HEADLINE OPTIONS\s*$/;
const DEAL_ABOUT_HEADING = /^##\s+ABOUT\s*$/;
const CREATOR_FIT_LABEL = '**Perfect for:**';
const CREATOR_FIT_LABEL_SHAPE = /^\*\*[A-Za-z][A-Za-z' ]*? for:\*\*$/;
// The creator-fit lead names the creator, not the deal. The deal Standards allow
// five shapes, and in each the name sits in a short slot that closes the
// sentence: one to three words after "If you're a", "If you're already a" and
// "For anyone who's into", one to three before the closing "content" of "If you
// create", and one to four after "For anyone who likes to", the length of the
// longest worked example. A slot that short leaves no room for the offer, the
// quantity, the value or a tone note to be restated, so a clause about what this
// deal hands over cannot fit one. The slot admits no digit for the same reason,
// so a euro amount or a pack size cannot enter it. A bracketed placeholder counts
// as one word, because the scaffold files teach the shapes with a slot still in
// it. Whether a name is one creators already use is the name test, which stays a
// reader's judgement.
const LEAD_PROFILE_WORD = "(?:\\[[^\\]]+\\]|[A-Za-z][A-Za-z'-]*)";
const leadSlot = (most) => `${LEAD_PROFILE_WORD}(?: ${LEAD_PROFILE_WORD}){0,${most - 1}}`;
const CREATOR_FIT_LEAD_PROFILE = new RegExp(
  `^(?:If you're (?:already )?an? ${leadSlot(3)}`
  + `|If you create ${leadSlot(3)} content`
  + `|For anyone who's into ${leadSlot(3)}`
  + `|For anyone who likes to ${leadSlot(4)})\\.$`,
);
const CREATOR_FIT_LEAD_SHAPES = 'one line in a Standards shape: "If you\'re a [name].", "If you create [name] content.", "For anyone who\'s into [name].", "For anyone who likes to [something they already do]." or "If you\'re already a [label]."';
const CONTENT_IDEAS_LABEL = '**Content ideas:**';
const CONCISE_VARIATION = '**Most concise**';
const VARIATION_LABEL = /^\*\*Most (?:valuable|authentic|concise)\*\*/;
const DEAL_BULLET = /^[-*+]\s+\S/;

// The Content ideas lead has no fixed wording and should have none, because the
// rule tells the writer to match the deal's voice and the three worked examples
// carry three different sentences. Structure is the whole of what a machine can
// settle here: one prose line, never a bullet, present under every label in the
// file, and the same bytes in each of them.
function dealArtifactFindings(prose) {
  const rows = prose.map(({ index, raw, visible }) => ({ index, raw: raw.trim(), text: visible.trim() }));
  const carries = (heading) => rows.some(({ text }) => heading.test(text));
  if (!carries(DEAL_HEADLINE_HEADING) || !carries(DEAL_ABOUT_HEADING)) return [];

  const nextContent = (position) => rows.slice(position + 1).find(({ text }) => text !== '') || null;
  const secondContent = (position) => {
    const rest = rows.slice(position + 1).filter(({ text }) => text !== '');
    return rest[1] || null;
  };
  const inConciseVariation = (position) => {
    for (let cursor = position; cursor >= 0; cursor -= 1) {
      if (VARIATION_LABEL.test(rows[cursor].text)) return rows[cursor].text.startsWith(CONCISE_VARIATION);
    }
    return false;
  };

  const findings = [];
  const leads = [];
  rows.forEach(({ index, text }, position) => {
    if (CREATOR_FIT_LABEL_SHAPE.test(text) && text !== CREATOR_FIT_LABEL) {
      findings.push({
        index,
        message: `creator-fit label reads ${text} rather than the one fixed label ${CREATOR_FIT_LABEL}`,
      });
    }
    if (text === CREATOR_FIT_LABEL) {
      const next = nextContent(position);
      const concise = inConciseVariation(position);
      if (!next) {
        findings.push({ index, message: 'creator-fit label carries nothing below it' });
      } else if (concise && !DEAL_BULLET.test(next.text)) {
        findings.push({
          index,
          message: 'creator-fit lead sentence in the concise variation, which carries the label and its bullets alone',
        });
      } else if (!concise && DEAL_BULLET.test(next.text)) {
        findings.push({
          index,
          message: `creator-fit lead sentence missing, the label is followed by ${CREATOR_FIT_LEAD_SHAPES}`,
        });
      } else if (!concise && !CREATOR_FIT_LEAD_PROFILE.test(next.text)) {
        findings.push({
          index: next.index,
          message: `creator-fit lead restates the deal rather than naming a general creator profile, ${CREATOR_FIT_LEAD_SHAPES}`,
        });
      }
    }
    if (text === CONTENT_IDEAS_LABEL) {
      const next = nextContent(position);
      if (!next || DEAL_BULLET.test(next.text)) {
        findings.push({ index, message: 'Content ideas lead sentence missing, the label is followed by one prose line' });
        return;
      }
      const second = secondContent(position);
      if (second && !DEAL_BULLET.test(second.text)) {
        findings.push({ index, message: 'Content ideas lead runs past one line before its bullets' });
        return;
      }
      leads.push(next);
    }
  });

  const [first, ...rest] = leads;
  if (first) {
    for (const lead of rest) {
      if (lead.raw !== first.raw) {
        findings.push({
          index: lead.index,
          message: 'Content ideas lead differs from the one this deal already uses, it is the same sentence in every variation',
        });
      }
    }
  }
  return findings.sort((left, right) => left.index - right.index);
}

// --- the cut side that a machine can settle ----------------------------
// Two of the layer's named cut rules resolve deterministically, so both block
// on a deliverable. Precision uses the same trick the heading echo uses: the
// sentence has to carry no content of its own beyond the marker, which leaves a
// claim that says why something matters alone and catches only the sentence
// whose whole content is that it matters.
const IMPORTANCE_MARKERS = [
  'important', 'critical', 'essential', 'crucial', 'vital', 'matters', 'significant',
  'noteworthy', 'fundamental',
];
const IMPORTANCE_STEMS = new Set(IMPORTANCE_MARKERS.map((word) => word.replace(/s$/, '')));
const IMPORTANCE_ASSERTION = new RegExp(`\\b(?:${IMPORTANCE_MARKERS.join('|')})\\b`, 'i');

const EFFORT_VERBS = [
  'analysed', 'analyzed', 'reviewed', 'checked', 'scored', 'scanned', 'verified',
  'examined', 'evaluated', 'assessed', 'investigated', 'audited',
];
const EFFORT_REPORT = new RegExp(
  `^(?:i|i'(?:ve|ll|m)|we|we'(?:ve|ll|re))\\b[^.!?]{0,40}?\\b(?:${EFFORT_VERBS.join('|')})\\b`,
  'i',
);

// --- the keep side, and the perimeter that makes it mean something -----
// Connective inventory and article rate are the two over-compression
// signatures a machine can count, and both mean something only where sentences
// carry the reasoning. A headline list, a field block, a hashtag run and a
// variation label say nothing about compression, which is why a deal template
// scoring zero connectives across its whole file is correct rather than
// telegraphic. Measuring paragraph prose alone, and only once there is enough
// of it for a ratio to be evidence, is what stops the counterweight from
// crying wolf on a structured artifact and getting switched off. A counterweight
// nobody trusts leaves the cut side running unopposed.
const STRUCTURAL_LINE_SHAPE = /^\s*(?:[-*+]\s|\d+[.)]\s|\||>|#{1,6}\s|!\[|\* \* \*|-{3,}|={3,}|<)/;
const FIELD_LINE_SHAPE = /^\s*(?:\*\*|__)?[A-Z][^.!?]{0,40}(?:\*\*|__)?\s*:\s*\S/;
const TAG_RUN_SHAPE = /^\s*[#@]\S/;
const LABEL_LINE_SHAPE = /^\s*(?:\*\*|__)[^*_]+(?:\*\*|__)[.,:;!?]?\s*$/;
const PROSE_WORD_FLOOR = 200;
const CONNECTIVE_FLOOR_PER_1000 = 5;
const ARTICLE_FLOOR_PER_1000 = 30;

// Frontmatter is machine-readable metadata whose description field is one long
// line, so counting it as prose would swamp the ratio it feeds.
function frontmatterEnd(lines) {
  if (!lines.length || lines[0].trim() !== '---') return 0;
  const close = lines.findIndex((line, index) => index > 0 && line.trim() === '---');
  return close > 0 ? close + 1 : 0;
}

const isProseLine = (line) =>
  Boolean(line)
  && !STRUCTURAL_LINE_SHAPE.test(line)
  && !FIELD_LINE_SHAPE.test(line)
  && !TAG_RUN_SHAPE.test(line)
  && !LABEL_LINE_SHAPE.test(line);

// --- the length caps ---------------------------------------------------
// The caps a deliverable's writing is held to: a bullet is one sentence of 25
// words or fewer, a paragraph at most three sentences and 60 words, and an
// About or Overview opening at most two paragraphs. The opening is the prose
// before the section's first heading or bold label, since a task template keeps
// its References block inside About and those lines are not the opening. They
// advise and never block, because a long line that carries a supplied value is
// still correct, and a scenario grades what an artifact says before how long it
// takes to say it. Code, tables, blockquotes and Given/When/Then lines are
// exempt, and a backticked or double-quoted span counts as one word, since copy
// carried verbatim from a source is the writer's to keep rather than to shorten.
const BULLET_WORD_CAP = 25;
const PARAGRAPH_WORD_CAP = 60;
const PARAGRAPH_SENTENCE_CAP = 3;
const OPENING_PARAGRAPH_CAP = 2;
const LIST_ITEM = /^\s*(?:[-*+]|\d+[.)])\s+(.*)$/;
// The house writes a scenario step's keyword in bold, which is what separates
// `**When** they sign in` from a requirement that happens to open on "When".
const GIVEN_WHEN_THEN = /^(?:\*\*(?:Given|When|Then|And|But)\*\*|Given\b)/;
const OPENING_HEADING = /^(?:About|Overview)$/i;
const SENTENCE_BREAK = /(?<=[.!?])\s+(?=["'(]?[A-Z0-9])/;

const capText = (line) =>
  line
    .replace(/`[^`]*`/g, 'CODE')
    .replace(/"[^"]*"/g, 'QUOTE')
    .replace(/[*_]+/g, '')
    .trim();
const capWords = (text) => text.split(/\s+/).filter((word) => /[A-Za-z0-9]/.test(word)).length;
const capSentences = (text) => text.split(SENTENCE_BREAK).filter((sentence) => /[A-Za-z0-9]/.test(sentence)).length;

function lengthCapFindings(lines, uncommented, proseStart) {
  const findings = [];
  let inFence = false;
  let paragraph = null;
  let opening = null;

  const closeParagraph = () => {
    if (!paragraph) return;
    const words = capWords(paragraph.text);
    const sentences = capSentences(paragraph.text);
    if (words > PARAGRAPH_WORD_CAP) {
      findings.push({ index: paragraph.index, message: `paragraph runs ${words} words, over the 60-word cap` });
    }
    if (sentences > PARAGRAPH_SENTENCE_CAP) {
      findings.push({ index: paragraph.index, message: `paragraph holds ${sentences} sentences, over the three-sentence cap` });
    }
    if (opening) opening.paragraphs += 1;
    paragraph = null;
  };
  const closeOpening = () => {
    if (opening && opening.paragraphs > OPENING_PARAGRAPH_CAP) {
      findings.push({
        index: opening.index,
        message: `${opening.name} opening holds ${opening.paragraphs} paragraphs, over the two-paragraph cap`,
      });
    }
    opening = null;
  };

  lines.forEach((line, index) => {
    if (/^\s*(```|~~~)/.test(line)) {
      closeParagraph();
      inFence = !inFence;
      return;
    }
    if (inFence || index < proseStart) return;
    const text = uncommented[index];
    const trimmed = text.trim();

    const heading = trimmed.match(/^#{1,6}(?:\s+(.*))?$/);
    if (heading) {
      closeParagraph();
      closeOpening();
      const name = capText(heading[1] || '');
      if (OPENING_HEADING.test(name)) opening = { index, name, paragraphs: 0 };
      return;
    }
    if (!trimmed || HOUSE_DIVIDER.test(trimmed) || HYPHEN_RULE.test(trimmed)) {
      closeParagraph();
      return;
    }

    const item = text.match(LIST_ITEM);
    if (item) {
      closeParagraph();
      const raw = item[1].replace(/^\[[ xX]?\]\s*/, '').trim();
      const body = capText(raw);
      if (!body || GIVEN_WHEN_THEN.test(raw)) return;
      const words = capWords(body);
      const sentences = capSentences(body);
      if (words > BULLET_WORD_CAP) {
        findings.push({ index, message: `bullet runs ${words} words, over the 25-word cap` });
      }
      if (sentences > 1) {
        findings.push({ index, message: `bullet holds ${sentences} sentences, over the one-sentence cap` });
      }
      return;
    }

    if (LABEL_LINE_SHAPE.test(text)) {
      closeParagraph();
      closeOpening();
      return;
    }
    if (STRUCTURAL_LINE_SHAPE.test(text) || TAG_RUN_SHAPE.test(text)) {
      closeParagraph();
      return;
    }
    const body = capText(trimmed);
    if (GIVEN_WHEN_THEN.test(trimmed)) {
      closeParagraph();
      return;
    }
    if (paragraph) paragraph.text += ` ${body}`;
    else paragraph = { index, text: body };
  });
  closeParagraph();
  closeOpening();

  return findings.sort((left, right) => left.index - right.index);
}

// --- per-file analysis -------------------------------------------------
function analyse(file, source) {
  const relative = lintingArtifacts ? file : path.relative(systemRoot, file);
  const enforceHvr = hvrEnforced.has(file) || lintingArtifacts;
  const report = (message, blocking) => (blocking ? errors : advisories).push(message);

  const lines = source.split(/\r?\n/);
  const uncommented = withoutHtmlComments(lines);
  let inFence = false;
  const prose = []; // { index, raw, masked, visible }

  lines.forEach((line, index) => {
    if (/^\s*(```|~~~)/.test(line)) {
      inFence = !inFence;
      return;
    }
    if (inFence) return;
    prose.push({
      index,
      raw: line,
      masked: maskPaths(maskInlineCode(line)),
      visible: maskInlineCode(uncommented[index]),
    });
  });

  // 0. artifact purity. A deliverable carries final content only, so the score,
  // the voice scan and the assumption ledger stay in the reply. Quoted spans are
  // masked here for the same reason every other check masks them: a document
  // naming a shape is not using it.
  if (lintingArtifacts) {
    prose.forEach(({ index, visible }) => {
      const shape = processShape(maskQuoted(visible));
      if (shape) {
        errors.push(`${relative}:${index + 1}: ${shape} inside the deliverable, which carries final content only`);
      }
    });

    // 0b. the deal artifact shape. Gated on the export's own two section
    // headings rather than on the system running the gate, so a document that
    // is not a deal export never sees these three rules at all.
    dealArtifactFindings(prose).forEach(({ index, message }) => {
      errors.push(`${relative}:${index + 1}: ${message}`);
    });

    // 0c. the Delivery section is opt-in, and an all-placeholder one reads as a
    // delivery view nobody took. Advice rather than a block, because asked-ness
    // lives in the request and never in the artifact: the mode reference grants
    // three `TBD...` slots as correct output for a Delivery the requester asked
// for and nothing was estimated in, the refinement rule keeps a source
// section's `TBD...` slots untouched, and both scaffolds ship the exact
// all-placeholder form. A gate that fails those is a gate that gets switched
// off. A populated slot anywhere in the section clears it either way.
    const deliveryIndex = lines.findIndex((line) => line.trim() === '## Delivery');
    if (deliveryIndex >= 0) {
      const slots = lines.slice(deliveryIndex + 1).filter((line) => /^\*   \S/.test(line));
      if (slots.length >= 3 && slots.every((line) => line.trim() === '*   TBD...')) {
        advisories.push(
          `${relative}:${deliveryIndex + 1}: Delivery section carries only TBD placeholders, so an unasked one reads as a delivery view nobody took`,
        );
      }
    }

    // 0e. the house grammar shape, the score-section report shape, the two card
    // caps and the asterisk-emphasis ban. Each is gated on something the
    // deliverable carries rather than on the system that ran the gate.
    houseGrammarFindings(prose, lines).forEach(({ index, message }) => {
      errors.push(`${relative}:${index + 1}: ${message}`);
    });
    scoreSectionFindings(prose).forEach(({ index, message }) => {
      errors.push(`${relative}:${index + 1}: ${message} inside the deliverable, which carries final content only`);
    });

    // The two per-piece caps the card states, counted over the whole deliverable
    // because the rule is per piece rather than per line. `TBD...` is the one
    // named ellipsis exemption, so it comes off the count first.
    const pieceText = prose.map(({ visible }) => visible).join('\n');
    const ellipses = (pieceText.match(ELLIPSIS) || []).length - (pieceText.match(TBD_TOKEN) || []).length;
    if (ellipses > 1) {
      errors.push(`${relative}: ${ellipses} ellipses, where the card caps a piece at one`);
    }
    const pictographs = (pieceText.match(PICTOGRAPH) || []).length;
    if (pictographs > 1) {
      errors.push(`${relative}: ${pictographs} emoji, where the card caps a piece at one`);
    }
    const prios = (pieceText.match(PRIO_MARKER) || []).length;
    if (prios > 1) {
      errors.push(`${relative}: ${prios} `+'`← PRIO`'+` markers, where the house grammar allows one`);
    }
    prose.forEach(({ index, visible }) => {
      const text = visible.trim();
      if (HOUSE_DIVIDER.test(text)) return;
      if (EMPHASIS_SPAN.test(text.replace(LIST_MARKER, ''))) {
        errors.push(`${relative}:${index + 1}: asterisk emphasis, which the card bans in delivered output`);
      }
    });

    // 0d. Requirements hold constraints a build can fail, each one a `- []`
    // checklist item under its group name. A plain bullet there is the retired
    // shape and a `**Checklist**` label is build tracking, so both settle without
    // reading the wording. The per-criterion Mark-as-done checkbox lives in
    // Acceptance criteria and never inside Requirements.
    //
    // An item saying a screen explains, states, tells or informs, while quoting
    // none of the copy, reports that a string exists without carrying the
    // string. The design already holds what the screen says, so the item fixes
    // nothing a build could get wrong, and the repair is to quote the copy in
    // backticks or drop the item. Deliberately narrow, and a copy-paraphrase
    // check rather than a description check: third-person verb forms only, so
    // the noun "state" never matches, and any backtick in the item is an
    // exemption because an item that quotes the copy has carried the value.
    // Measured at one hit across 261 Requirements bullets in the story corpus
    // and zero across 67 in the worked examples, mirrors and numbered exports.
    // The wider "describes a screen" class is not mechanically separable, so
    // Requirements still needs a reader.
    const requirementsIndex = lines.findIndex((line) => line.trim() === '## Requirements');
    if (requirementsIndex >= 0) {
      const nextSection = lines.findIndex((line, i) => i > requirementsIndex && /^## /.test(line));
      const last = nextSection === -1 ? lines.length : nextSection;
      for (let i = requirementsIndex + 1; i < last; i += 1) {
        const line = lines[i].trim();
        if (REQUIREMENTS_CHECKLIST.test(line)) {
          errors.push(`${relative}:${i + 1}: a **Checklist** label inside Requirements, where each constraint is its own checklist item`);
          continue;
        }
        if (/^\*   \S/.test(lines[i])) {
          errors.push(`${relative}:${i + 1}: a plain bullet inside Requirements, where each constraint is a \`- []\` checklist item`);
          continue;
        }
        const item = lines[i].match(CHECKBOX_ITEM);
        if (!item || item[1].includes('`')) continue;
        if (!/\b(?:explains|states|tells|informs)\b/.test(item[1])) continue;
        errors.push(
          `${relative}:${i + 1}: Requirements item reports what a screen says without quoting the copy`,
        );
      }
    }
  }

  // 0f. the house writes every checkbox `[]`, with no space between the
  // brackets. The checkbox rules above read both forms, so this is the one
  // check that holds a deliverable to the house form.
  if (lintingArtifacts) {
    prose.forEach(({ index, raw }) => {
      if (!SPACED_CHECKBOX.test(raw)) return;
      errors.push(`${relative}:${index + 1}: a checkbox written \`[ ]\`, where the house form is \`[]\` with no space`);
    });
  }
  // 1. bullet punctuation and the acceptance-block spacing rule (unchanged)
  lines.forEach((line, index) => {
    const bullet = line.match(/^\s*[-*]\s+(.*\S)\s*$/);
    if (bullet && !bullet[1].endsWith('...') && /\.(?:[*_]+)?$/.test(bullet[1])) {
      errors.push(`${relative}:${index + 1}: bullet item ends with a full stop`);
    }

    if (!MARK_AS_DONE.test(line.trim())) return;
    const nextContentIndex = lines.findIndex((candidate, candidateIndex) => candidateIndex > index && candidate.trim() !== '');
    if (nextContentIndex >= 0 && lines[nextContentIndex].trim() === '* * *' && !closesSection(lines, nextContentIndex)) {
      errors.push(`${relative}:${nextContentIndex + 1}: divider follows a Mark-as-done checkbox`);
    }
  });

  // 2. Human Voice punctuation, so a cleaned instruction surface cannot rot.
  // Quoted spans are masked here for the same reason they are masked in the
  // checks below: a quoted literal is material the document is showing, such
  // as an example of an output line, not punctuation the document is using.
  // Frontmatter is skipped for the same reason the keep side skips it below:
  // it is machine-readable metadata, so a semicolon separating two clauses of
  // an Assumes field is a field separator and never reaches a reader as prose.
  const proseStart = frontmatterEnd(lines);
  prose.filter(({ index }) => index >= proseStart).forEach(({ index, raw, masked }) => {
    const text = maskQuoted(masked);
    if (text.includes(';')) {
      report(`${relative}:${index + 1}: prose semicolon (HVR bans it, use two sentences)`, enforceHvr);
    }
    const curly = text.match(/[‘’“”]/g);
    if (curly) {
      report(`${relative}:${index + 1}: curly quote (HVR requires straight quotes)`, enforceHvr);
    }
    let emDashes = (text.match(/—/g) || []).length;
    const bare = stripContainers(raw);
    if (emDashes && SANCTIONED_DEFINITION.test(bare)) emDashes -= 1;
    if (emDashes && SANCTIONED_STATUS.test(bare)) emDashes -= 1;
    if (emDashes > 0) {
      report(`${relative}:${index + 1}: prose em dash (HVR bans it, use a comma, colon or full stop)`, enforceHvr);
    }
  });

  // 2b. the Human Voice blocker vocabulary, which is the other half of the
  // same always-loaded card. The card is the one file the pass never reads
  // itself against: it holds every banned term by design, and a list cannot
  // judge the page it was read from.
  //
  // Masking runs in the order the purity pass established. An HTML comment
  // renders as nothing, inline code is a literal being shown, a quoted span is
  // material the document cites, and a blockquote line is a whole cited
  // passage, which is what a file listing the banned vocabulary verbatim uses.
  // A curly apostrophe is normalised to a straight one so a term is not missed
  // by punctuation the card bans anyway.
  if (file !== hvrCard) {
    prose.forEach(({ index, raw, visible }) => {
      if (/^\s*>/.test(raw)) return;
      const text = maskQuoted(visible).replace(/[‘’]/g, "'");
      if (!text.trim()) return;
      const blocking = [];
      const literal = [];
      for (const entry of vocabulary.terms) {
        if (!entry.pattern.test(text)) continue;
        (entry.literalSense ? literal : blocking).push(entry.term);
      }
      if (blocking.length) {
        report(
          `${relative}:${index + 1}: Human Voice hard blocker (${blocking.join(', ')}), the ALWAYS-loaded card bans it`,
          vocabularyBlocks,
        );
      }
      if (literal.length) {
        advisories.push(
          `${relative}:${index + 1}: Human Voice blocker with a literal reading (${literal.join(', ')}), banned as a figure and fine as the plain word`,
        );
      }
      if (vocabulary.contrastStated && CONTRAST_BAN.test(text)) {
        report(
          `${relative}:${index + 1}: "not just X, but Y" contrast, state X and state Y separately`,
          vocabularyBlocks,
        );
      }
    });
  }

  // 3. conciseness: sentence-initial openers and hedge stacks (blocking)
  prose.forEach(({ index, masked }) => {
    const text = maskQuoted(masked);
    if (!text.trim()) return;
    const sentences = text.split(/(?<=[.!?])\s+/);
    sentences.forEach((sentence) => {
      const opener = startsWithAny(sentence, SENTENCE_OPENERS);
      if (opener) {
        errors.push(`${relative}:${index + 1}: sentence opens with "${opener}", which announces instead of stating`);
      }
      const lower = ` ${sentence.toLowerCase()} `;
      const found = HEDGES.filter((hedge) => lower.includes(` ${hedge} `) || lower.includes(` ${hedge},`));
      if (found.length >= 2) {
        errors.push(`${relative}:${index + 1}: hedge stack in one sentence (${found.join(', ')}), keep the one that is true`);
      }
      // Importance assertion and effort reporting, the two cut rules that
      // resolve without judgement. Blocking on a deliverable, advisory on an
      // instruction file, which states both shapes in order to ban them.
      if (IMPORTANCE_ASSERTION.test(sentence) && sentence.trim().split(/\s+/).filter(Boolean).length <= 12) {
        const carried = contentWords(sentence).filter(
          (word) => !FILLER_WORDS.has(word) && !IMPORTANCE_STEMS.has(word),
        );
        if (!carried.length) {
          report(`${relative}:${index + 1}: importance assertion, the sentence says only that something matters`, lintingArtifacts);
        }
      }
      if (EFFORT_REPORT.test(sentence.trim().replace(/^[*_#>\s-]+/, ''))) {
        report(`${relative}:${index + 1}: effort reporting, the sentence narrates the work instead of the finding`, lintingArtifacts);
      }
    });
  });

  // 4. conciseness: terminal recap and heading echo (blocking)
  const headingIndexes = prose.filter(({ raw }) => /^#{1,6}\s+\S/.test(raw)).map(({ index }) => index);
  const isStructural = (line) => /^\s*([-*+]\s|\d+[.)]\s|\||>|#{1,6}\s|!\[|\* \* \*|---)/.test(line) || !line.trim();

  headingIndexes.forEach((headingIndex, position) => {
    const nextHeading = headingIndexes[position + 1] ?? lines.length;
    const body = prose.filter(({ index }) => index > headingIndex && index < nextHeading);

    // Heading echo. Precision comes from the second condition: the sentence
    // must add no content word of its own beyond generic filler, so a lead-in
    // that carries real information is left alone. An H1 is the document
    // title, whose description line legitimately names the document.
    const firstProse = /^#\s/.test(lines[headingIndex]) ? null : body.find(({ raw }) => !isStructural(raw));
    if (firstProse) {
      const headingWords = contentWords(lines[headingIndex].replace(/^#+\s*/, ''));
      if (headingWords.length >= 2) {
        const sentence = maskQuoted(firstProse.masked).split(/(?<=[.!?])\s+/)[0] || '';
        const sentenceWords = contentWords(sentence);
        const headingSet = new Set(headingWords);
        const shared = headingWords.filter((word) => sentenceWords.includes(word));
        const added = sentenceWords.filter((word) => !headingSet.has(word) && !FILLER_WORDS.has(word));
        if (sentenceWords.length && shared.length >= 2 && shared.length / headingWords.length >= 0.7 && added.length === 0) {
          errors.push(`${relative}:${firstProse.index + 1}: first sentence restates its heading and adds nothing (${shared.join(', ')})`);
        }
      }
    }

    // terminal recap: the section's closing paragraph opening on a summary move
    const lastProse = [...body].reverse().find(({ raw }) => !isStructural(raw));
    if (lastProse && lastProse !== firstProse) {
      const opener = startsWithAny(maskQuoted(lastProse.masked), RECAP_OPENERS);
      if (opener) {
        errors.push(`${relative}:${lastProse.index + 1}: section closes on a recap opener ("${opener}")`);
      }
    }
  });

  // 5. advisory statistics, never blocking
  const body = prose.map(({ raw }) => raw);
  const bullets = body.filter((line) => /^\s*[-*+]\s/.test(line)).length;
  const headings = headingIndexes.length;
  const contentLines = body.filter((line) => line.trim()).length || 1;
  const words = body.join(' ').split(/\s+/).filter(Boolean).length || 1;
  const connectives = SEMANTIC_CONNECTIVES.reduce(
    (total, connective) => total + (body.join(' ').toLowerCase().match(new RegExp(`\\b${connective}\\b`, 'g')) || []).length,
    0,
  );
  const articles = (body.join(' ').toLowerCase().match(/\b(?:the|a|an)\b/g) || []).length;
  const copulas = (body.join(' ').toLowerCase().match(/\b(?:is|are|was|were|be|been)\b/g) || []).length;

  const stats = [
    `bullet ratio ${(bullets / contentLines).toFixed(2)}`,
    `heading density ${(headings / contentLines).toFixed(2)}`,
    `connectives per 1000 words ${((connectives / words) * 1000).toFixed(1)}`,
    `article rate ${((articles / words) * 1000).toFixed(1)}`,
    `copula rate ${((copulas / words) * 1000).toFixed(1)}`,
  ];
  // The two ratios above stay statistics and raise nothing. Both were measured
  // against the house output before that was settled. A 0.6 bullet-ratio
  // advisory flagged six of the thirty-nine sanctioned sources every run,
  // including all four story examples at 0.61 to 0.65, and the conciseness
  // layer's heading band, one heading per 150 to 400 words, is outside the
  // house grammar's range on thirty-four of thirty-seven sanctioned
  // deliverables, because a Doc and a Story put a divider under every heading
  // and a spacer heading between sections. The layer states over-bulleting by
  // its tells rather than by a ratio, so the tells are what a reader applies
  // and the ratios are what a reviewer reads under PO_FORMAT_STATS.
  // 6. the keep side, measured over paragraph prose alone so a structured
  // artifact is never read as telegraphic. Blocking on a deliverable, advisory
  // on an instruction file, which is the same strength the two cut rules above
  // carry. Hardening one side alone produces the failure this layer exists to
  // prevent.
  const proseText = prose
    .filter(({ index }) => index >= proseStart)
    .map(({ visible }) => visible.trim())
    .filter(isProseLine)
    .join(' ');
  const proseWords = proseText.split(/\s+/).filter(Boolean).length;
  if (proseWords >= PROSE_WORD_FLOOR) {
    const proseLower = proseText.toLowerCase();
    const proseConnectives = SEMANTIC_CONNECTIVES.reduce(
      (total, connective) => total + (proseLower.match(new RegExp(`\\b${connective}\\b`, 'g')) || []).length,
      0,
    );
    const proseArticles = (proseLower.match(/\b(?:the|a|an)\b/g) || []).length;
    const per1000 = (count) => ((count / proseWords) * 1000).toFixed(1);
    if ((proseConnectives / proseWords) * 1000 < CONNECTIVE_FLOOR_PER_1000) {
      report(
        `${relative}: prose connectives ${per1000(proseConnectives)} per 1000 across ${proseWords} prose words, connective stripping leaves the reader guessing the relation`,
        lintingArtifacts,
      );
    }
    if ((proseArticles / proseWords) * 1000 < ARTICLE_FLOOR_PER_1000) {
      report(
        `${relative}: prose articles ${per1000(proseArticles)} per 1000 across ${proseWords} prose words, telegraphese is compression past the line`,
        lintingArtifacts,
      );
    }
  }

  // 7. the length caps, advice on a deliverable only
  if (lintingArtifacts) {
    lengthCapFindings(lines, uncommented, proseStart).forEach(({ index, message }) => {
      advisories.push(`${relative}:${index + 1}: ${message}`);
    });
  }

  return `${relative}: ${stats.join(', ')}`;
}

const statLines = [];

for (const file of files) {
  const source = fs.readFileSync(file, 'utf8');

  if (write) {
    let previousContent = '';
    const sourceLines = source.split(/\r?\n/);
    const formatted = sourceLines.flatMap((line, index) => {
      // The section-closing divider above a spacer heading is sanctioned, so
      // the stripper leaves it where the checker leaves it.
      if (line.trim() === '* * *' && MARK_AS_DONE.test(previousContent) && !closesSection(sourceLines, index)) return [];

      const bullet = line.match(/^(\s*[-*]\s+)(.*\S)(\s*)$/);
      let nextLine = line;
      if (bullet && !bullet[2].endsWith('...') && /\.(?:[*_]+)?$/.test(bullet[2])) {
        nextLine = `${bullet[1]}${bullet[2].replace(/\.(?=[*_]*$)/, '')}${bullet[3]}`;
      }
      if (nextLine.trim() !== '') previousContent = nextLine.trim();
      return [nextLine];
    });
    const output = formatted.join('\n');
    if (output !== source) fs.writeFileSync(file, output);
  }

  statLines.push(analyse(file, write ? fs.readFileSync(file, 'utf8') : source));
}

if (!lintingArtifacts) {
  const skill = fs.readFileSync(path.join(skillRoot, 'SKILL.md'), 'utf8');
  // The two acceptance-block contracts below moved out of the per-shape
  // scaffolds and into the mode reference, which is now the single authority
  // for everything the Story and Epic shapes share. Checking them here is
  // what stops a split from quietly dropping a shared rule.
  const storyMode = fs.readFileSync(path.join(skillRoot, 'references', 'story-mode.md'), 'utf8');
  const card = path.join(skillRoot, 'references', 'hvr-core.md');
  const layer = path.join(skillRoot, 'references', 'conciseness.md');
  if (!skill.includes('Bullet items never end with a full stop')) {
    errors.push('sk-product-owner/SKILL.md: missing the bullet punctuation contract');
  }
  if (!storyMode.includes('No divider separates a Mark-as-done line from the next criterion')) {
    errors.push('sk-product-owner/references/story-mode.md: missing the acceptance spacing contract');
  }
  if (!storyMode.includes('the one sanctioned divider after a Mark-as-done checkbox')) {
    errors.push('sk-product-owner/references/story-mode.md: missing the section-close divider contract');
  }
  if (!storyMode.includes('`## Delivery` is optional and opt-in')) {
    errors.push('sk-product-owner/references/story-mode.md: missing the opt-in Delivery contract');
  }
  if (!storyMode.includes('Supplied hard values travel into Requirements verbatim')) {
    errors.push('sk-product-owner/references/story-mode.md: missing the supplied-hard-value contract');
  }
  if (!skill.includes('HVR self-scan: N hard blockers.')) {
    errors.push('sk-product-owner/SKILL.md: missing the HVR self-scan response contract');
  }
  // The gate demotes six card-declared hard blockers to advice because each
  // carries an everyday literal reading. A leniency stated only in code is a
  // leniency the writer never learns, so this system states it on its own
  // surface and this contract fails the run when the statement goes.
  const wrapper = fs.readFileSync(path.join(systemRoot, 'AGENTS.md'), 'utf8');
  if (!wrapper.includes('reports them as advice rather than blocking')) {
    errors.push('AGENTS.md: missing the literal-sense demotion notice the gate relies on');
  }
  if (!fs.existsSync(card)) {
    errors.push('sk-product-owner/references/hvr-core.md: the ALWAYS-loaded Human Voice card is absent');
  } else {
    // The blocker vocabulary is read out of the card, so the guard the
    // conciseness list needs by hand holds here by construction. What still
    // needs guarding is the reading itself: a card reshaped so a section no
    // longer parses would disarm the pass without a word, and a silent gate is
    // worse than no gate, so an empty section fails the run.
    const emptySections = CARD_SECTION_NUMBERS.filter((number) => !(vocabulary.sections[number] || []).length);
    if (emptySections.length) {
      errors.push(
        `sk-product-owner/references/hvr-core.md: section(s) ${emptySections.join(', ')} yielded no blocker terms, so the vocabulary pass guards nothing`,
      );
    }
    // The comparison that can fail is the upstream one. Filtering the parsed
    // vocabulary against the card it was parsed from can never fire, because
    // every term is by construction a substring of that file. The card names
    // the shared EN standard as its authority and itself as a carried subset,
    // so a term the card enforces and the standard does not hold is a rule one
    // system invented for the whole fleet, which is the drift worth a gate.
    if (!fs.existsSync(hvrStandard)) {
      errors.push(
        `sk-product-owner/references/human-voice-rules.md: the Human Voice standard the card names as its authority is absent, so the carried subset is checked against nothing`,
      );
    } else {
      const standardText = fs.readFileSync(hvrStandard, 'utf8').toLowerCase();
      const unstated = vocabulary.terms.filter((entry) => !standardText.includes(entry.term));
      if (unstated.length) {
        errors.push(
          `sk-product-owner/references/human-voice-rules.md: ${unstated.length} card term(s) the authority standard does not state (${unstated.map((entry) => entry.term).join(', ')})`,
        );
      }
    }
    const held = new Set(vocabulary.terms.map((entry) => entry.term));
    const orphaned = LITERAL_SENSE.filter((term) => !held.has(term));
    if (orphaned.length) {
      errors.push(
        `sk-product-owner/references/hvr-core.md: literal-sense term(s) named by the gate and absent from the card (${orphaned.join(', ')})`,
      );
    }
    if (!vocabulary.contrastStated) {
      errors.push(`sk-product-owner/references/hvr-core.md: missing the ${CARD_CONTRAST_STATEMENT} contrast ban`);
    }
  }

  // The gate and the instructions have to hold the same list. A blocking
  // check whose vocabulary the writer was never given is the defect this
  // guard exists to stop from coming back, so a term present here and absent
  // there fails the run rather than the next writer.
  if (!fs.existsSync(layer)) {
    errors.push('sk-product-owner/references/conciseness.md: the ALWAYS-loaded conciseness layer is absent');
  } else {
    const stated = fs.readFileSync(layer, 'utf8').toLowerCase();
    const vocabulary = [...new Set([
        ...SENTENCE_OPENERS, ...RECAP_OPENERS, ...HEDGES, ...IMPORTANCE_MARKERS, ...EFFORT_VERBS,
      ])];
    const unstated = vocabulary.filter((term) => !stated.includes(term));
    if (unstated.length) {
      errors.push(
        `sk-product-owner/references/conciseness.md: ${unstated.length} blocking term(s) not stated in the layer (${unstated.join(', ')})`,
      );
    }
  }
}

if (advisories.length) {
  console.log('Advisory:');
  console.log(advisories.map((line) => `  ${line}`).join('\n'));
}
if (process.env.PO_FORMAT_STATS === '1') {
  console.log('Statistics:');
  console.log(statLines.map((line) => `  ${line}`).join('\n'));
}

if (errors.length) {
  console.error(errors.join('\n'));
  console.error(`Product Owner output format validation failed with ${errors.length} error(s)`);
  process.exit(1);
}

const scope = lintingArtifacts ? `${files.length} artifact file(s)` : `${files.length} source files`;
console.log(`Product Owner output format validation passed across ${scope}${write ? ' after formatting' : ''}`);
