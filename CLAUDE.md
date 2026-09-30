# AAFDID Navigator

Rule base, engines, web page and agent pack for AAFDID information requirements.

- Hand-written sources: `rules/pathways.json`, `rules/questions.json`, `rules/currency.json`, `sources/*.json`.
- Generated (do not edit by hand): `rules/requirements.json`, `rules/meta.json`, `rules/aafdid-rules.json`, `web/index.html`, `agent/**`, `tests/expected/*`.
- Rebuild and test: `tools/build_all.sh`. Both engines must pass `python3 tests/run_tests.py` with identical output.
- `engine/aafdid.js` and `engine/aafdid.py` implement the same logic; change both together.
- Never add a requirement without a source; AAFDID wording stays verbatim. Corrections go in a corrections file under `sources/`.
