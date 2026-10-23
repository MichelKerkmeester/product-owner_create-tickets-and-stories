#!/usr/bin/env node
// Records one research iteration for this lineage: writes the delta artifact and
// hands the single canonical iteration record to the append gateway.
'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { spawnSync } = require('node:child_process');

const repoRoot = path.resolve(__dirname, '../../../../../..');
const lineageDir = path.resolve(__dirname, '..');
const config = JSON.parse(fs.readFileSync(path.join(lineageDir, 'deep-research-config.json'), 'utf8'));
const sessionId = config.lineage.sessionId;
const gateway = path.join(repoRoot, '.skilled/skills/system-deep-loop/runtime/scripts/append-mode-event.cjs');

const payloadPath = process.argv[2];
if (!payloadPath) {
  console.error('usage: record.cjs <payload.json>');
  process.exit(1);
}
const payload = JSON.parse(fs.readFileSync(path.resolve(payloadPath), 'utf8'));
const n = Number(payload.iteration);
const pad = String(n).padStart(3, '0');

const record = {
  type: 'iteration',
  iteration: n,
  runId: sessionId,
  sessionId,
  lineageId: sessionId,
  mode: 'research',
  target_agent: 'deep-research',
  agent_definition_loaded: true,
  resolved_route: 'Resolved route: mode=research target_agent=deep-research',
  newInfoRatio: payload.newInfoRatio,
  status: payload.status,
  focus: payload.focus,
  findingsCount: payload.findings.length,
  noveltyJustification: payload.noveltyJustification,
  answeredQuestions: payload.answeredQuestions || [],
  ruledOut: payload.ruledOut || [],
  toolsUsed: payload.toolsUsed || ['read', 'bash'],
  sourcesQueried: payload.sourcesQueried || [],
  timestamp: new Date().toISOString(),
  durationMs: payload.durationMs || 60000,
  executor: { kind: 'cli-pi', model: 'deepseek-v4.1-flash' },
};
if (payload.graphEvents) record.graphEvents = payload.graphEvents;

const deltaLines = [JSON.stringify(record)];
for (const finding of payload.findings) {
  deltaLines.push(JSON.stringify({
    type: 'finding',
    id: finding.id,
    label: finding.label,
    iteration: n,
    sources: finding.sources,
  }));
}
fs.writeFileSync(path.join(lineageDir, 'deltas', `iter-${pad}.jsonl`), `${deltaLines.join('\n')}\n`);

const eventPath = path.join(lineageDir, '.executor-state', `event-iter-${pad}.json`);
fs.writeFileSync(eventPath, JSON.stringify(record));

const result = spawnSync(process.execPath, [
  gateway,
  '--mode', 'research',
  '--run-directory', lineageDir,
  '--event-json', eventPath,
], { cwd: repoRoot, encoding: 'utf8' });

let receipt = null;
try { receipt = JSON.parse(result.stdout.trim().split('\n').at(-1)); } catch { receipt = null; }
console.log(JSON.stringify({
  iteration: n,
  deltaRows: deltaLines.length,
  findings: payload.findings.length,
  gatewayExit: result.status,
  ok: receipt && receipt.ok,
  projectionRefreshed: receipt && receipt.projectionRefreshed,
  reason: receipt && receipt.reason,
  code: receipt && receipt.code,
  sequence: receipt && receipt.receipt && receipt.receipt.sequence,
}));
if (result.status !== 0) process.exit(result.status || 1);
