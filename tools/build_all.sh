#!/usr/bin/env bash
# Rebuild everything from the sources, then test. Run from the repository root.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/build_rules.py
python3 tests/run_tests.py
python3 tools/build_web.py
python3 tools/build_agent.py
