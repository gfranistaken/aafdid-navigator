#!/usr/bin/env node
/*
 * AAFDID Navigator command line.
 *   node engine/cli.js profile.txt            Markdown report
 *   node engine/cli.js profile.json --json    JSON result
 *   node engine/cli.js - --checklist < p.txt  Checklist from stdin
 *   node engine/cli.js profile.txt --block    Normalized profile block
 * A profile is JSON or an "AAFDID PROFILE v1" block of "field: value" lines.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const A = require('./aafdid.js');

const args = process.argv.slice(2);
const file = args.find(a => !a.startsWith('--'));
if (!file) {
  console.error('Usage: node engine/cli.js <profile file or -> [--json|--block|--checklist]');
  process.exit(2);
}
const bundle = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'rules', 'aafdid-rules.json'), 'utf8'));
const text = file === '-' ? fs.readFileSync(0, 'utf8') : fs.readFileSync(file, 'utf8');
let input;
try { input = JSON.parse(text); } catch (e) { input = A.parseProfileBlock(text); }
const result = A.evaluate(bundle, input);
if (args.includes('--json')) console.log(JSON.stringify(result, null, 2));
else if (args.includes('--block')) console.log(A.toProfileBlock(bundle, input));
else if (args.includes('--checklist')) console.log(A.toChecklist(result));
else console.log(A.toMarkdown(result));
