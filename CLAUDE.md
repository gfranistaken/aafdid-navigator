# AAFDID Navigator

Rule base, engines, web page and agent pack for AAFDID information requirements.

- Hand-written sources: `rules/pathways.json`, `rules/questions.json`, `rules/currency.json`, `sources/*.json`.
- Generated (do not edit by hand): `rules/requirements.json`, `rules/meta.json`, `rules/aafdid-rules.json`, the `gates` lists and the dollar-range `options` in `rules/questions.json`, `web/index.html`, `web/artifact.html`, `agent/**` (except `agent/README.md`), `tests/expected/*`.
- The published site (llms.txt, answer files, knowledge copies) is built at deploy time by `tools/build_site.py`; nothing in `_site/` is committed.
- Rebuild and test: `tools/build_all.sh`. Both engines must pass `python3 tests/run_tests.py` with identical output. After an intended rule change, run `python3 tests/run_tests.py --update` and review the snapshot diff.
- `engine/aafdid.js` and `engine/aafdid.py` implement the same logic; change both together.
- Never add a requirement without a source; AAFDID wording stays verbatim. Corrections go in a corrections file under `sources/`.
