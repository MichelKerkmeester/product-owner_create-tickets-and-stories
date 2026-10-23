#!/usr/bin/env node
// ───────────────────────────────────────────────────────────────────
// MODULE: Code Mode Launcher
// ───────────────────────────────────────────────────────────────────
'use strict';

// ─────────────────────────────────────────────────────────────────────────────
// 1. IMPORTS
// ─────────────────────────────────────────────────────────────────────────────

const { spawn } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');

const { resolveNodeInterpreter } = require(
  './vendored/code-mode/lib/node-engine-resolver.cjs',
);
const { runServer } = require('./vendored/code-mode/mcp-code-mode-launcher.cjs');

// ─────────────────────────────────────────────────────────────────────────────
// 2. CONFIGURATION
// ─────────────────────────────────────────────────────────────────────────────

const SERVER_DIRECTORY = path.resolve(__dirname, '..', 'mcp-code-mode', 'mcp-server');
const SERVER_MANIFEST_PATH = path.join(SERVER_DIRECTORY, 'package.json');
const SERVER_ENTRYPOINT_PATH = path.join(SERVER_DIRECTORY, 'dist', 'index.js');

// ─────────────────────────────────────────────────────────────────────────────
// 3. ERROR HELPER
// ─────────────────────────────────────────────────────────────────────────────

function fail(message) {
  process.stderr.write(`[code-mode] ${message}\n`);
  return 1;
}

// ─────────────────────────────────────────────────────────────────────────────
// 4. LAUNCH FLOW
// ─────────────────────────────────────────────────────────────────────────────

/**
 * Start the MCP server with a Node interpreter that satisfies its manifest.
 *
 * @returns {Promise<number>} Server process exit status.
 */
async function main() {
  if (!fs.existsSync(SERVER_ENTRYPOINT_PATH)) {
    return fail(
      'the server is not built yet. Under Node 24, run: ' +
      'cd mcp-code-mode/mcp-server && npm ci && npm run build',
    );
  }
  const resolution = resolveNodeInterpreter({ manifestPath: SERVER_MANIFEST_PATH });
  if (!resolution?.path) {
    return fail(
      `no installed Node satisfies ${resolution?.range ?? 'the server manifest'} ` +
      `(${resolution?.reason ?? 'unknown'}). Install Node 24, for example with nvm install 24.`,
    );
  }
  return runServer({
    nodePath: resolution.path,
    entrypointPath: SERVER_ENTRYPOINT_PATH,
    serverArguments: process.argv.slice(2),
    spawnProcess: spawn,
    terminateOnSignal: true,
  });
}

// ─────────────────────────────────────────────────────────────────────────────
// 5. CLI ENTRYPOINT
// ─────────────────────────────────────────────────────────────────────────────

main()
  .then((exitCode) => {
    process.exitCode = exitCode;
  })
  .catch((error) => {
    process.exitCode = fail(error.stack || error.message);
  });
