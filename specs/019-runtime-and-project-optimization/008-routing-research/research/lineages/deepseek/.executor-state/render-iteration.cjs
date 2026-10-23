#!/usr/bin/env node
'use strict';

// Renders one iteration narrative, its delta stream and its gateway event file
// from a single payload, so the finding text in the markdown, the delta and the
// canonical record cannot disagree.

const fs = require('node:fs');
const path = require('node:path');

const LINEAGE = path.resolve(__dirname, '..');
const payloadPath = process.argv[2];
if (!payloadPath) {
  console.error('usage: render-iteration.cjs <payload.json>');
  process.exit(1);
}

const payload = JSON.parse(fs.readFileSync(payloadPath, 'utf8'));
const config = JSON.parse(fs.readFileSync(path.join(LINEAGE, 'deep-research-config.json'), 'utf8'));
const sessionId = config.lineage.sessionId;
const iteration = Number(payload.iteration);
const pad3 = String(iteration).padStart(3, '0');
const findings = (payload.findings || []).map((finding, index) => ({
  id: `f-iter${pad3}-${String(index + 1).padStart(3, '0')}`,
  severity: finding.severity || 'P2',
  label: String(finding.label).trim(),
  sources: finding.sources || [],
}));

const bullets = (items) => (items && items.length ? items.map((item) => `- ${item}`).join('\n') : '- none');

const markdown = [
  `# Iteration ${iteration}: ${payload.focusTitle}`,
  '',
  '## Focus',
  payload.focus,
  '',
  '## Findings',
  ...findings.map((finding, index) => `${index + 1}. ${finding.label}`),
  '',
  '## Ruled Out',
  bullets(payload.ruledOut),
  '',
  '## Dead Ends',
  bullets(payload.deadEnds),
  '',
  '## Edge Cases',
  `- Ambiguous input: ${payload.edgeCases?.ambiguous || 'none'}`,
  `- Contradictory evidence: ${payload.edgeCases?.contradictory || 'none'}`,
  `- Missing dependencies: ${payload.edgeCases?.missing || 'none'}`,
  `- Partial success: ${payload.edgeCases?.partial || 'none'}`,
  '',
  '## Sources Consulted',
  bullets(payload.sources),
  '',
  '## Assessment',
  `- New information ratio: ${payload.newInfoRatio}`,
  `- Questions addressed: ${(payload.questionsAddressed || []).join('; ')}`,
  `- Questions answered: ${(payload.questionsAnswered || []).join('; ')}`,
  '',
  '## Reflection',
  `- What worked and why: ${payload.reflection.worked}`,
  `- What did not work and why: ${payload.reflection.failed}`,
  `- What I would do differently: ${payload.reflection.differently}`,
  '',
  '## Questions Remaining',
  bullets(payload.questionsRemaining),
  '',
  '## Recommended Next Focus',
  payload.nextFocus,
  '',
].join('\n');

fs.writeFileSync(path.join(LINEAGE, 'iterations', `iteration-${pad3}.md`), markdown, 'utf8');

const record = {
  type: 'iteration',
  iteration,
  run: iteration,
  runId: sessionId,
  sessionId,
  lineageId: sessionId,
  generation: 1,
  mode: 'research',
  target_agent: 'deep-research',
  agent_definition_loaded: true,
  resolved_route: 'Resolved route: mode=research target_agent=deep-research',
  newInfoRatio: Number(payload.newInfoRatio),
  status: payload.status,
  focus: payload.focusTitle,
  findingsCount: findings.length,
  keyFindings: findings.map((finding) => finding.label),
  noveltyJustification: payload.noveltyJustification,
  answeredQuestions: payload.questionsAnswered || [],
  keyQuestions: payload.questionsAddressed || [],
  ruledOut: payload.ruledOut || [],
  sourcesQueried: payload.sources || [],
  edgeCase: payload.edgeCases?.partial || 'none',
  timestamp: payload.timestamp,
  durationMs: Number(payload.durationMs || 0),
  executor: config.executor,
  graphEvents: [],
};

const deltaLines = [JSON.stringify(record)];
for (const finding of findings) {
  deltaLines.push(JSON.stringify({
    type: 'finding',
    id: finding.id,
    severity: finding.severity,
    label: finding.label,
    iteration,
    sources: finding.sources,
  }));
}
for (const direction of payload.ruledOut || []) {
  deltaLines.push(JSON.stringify({ type: 'ruled_out', direction, reason: 'no in-scope evidence produced a route', iteration }));
}

fs.writeFileSync(path.join(LINEAGE, 'deltas', `iter-${pad3}.jsonl`), `${deltaLines.join('\n')}\n`, 'utf8');
fs.writeFileSync(path.join(LINEAGE, '.executor-state', `iter-${pad3}-event.json`), JSON.stringify(record), 'utf8');
process.stdout.write(`${findings.length} findings, iteration ${iteration} written\n`);
