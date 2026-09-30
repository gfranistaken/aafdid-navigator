# AAFDID Navigator

A human interface and an AI-agent tool for working through AAFDID, the Adaptive Acquisition Framework Document Identification tool. Describe a Department of War acquisition program once. The navigator tells you:

- which information requirements apply
- when each one is due
- whether each one is statutory or regulatory
- what AAFDID's notes say about it

People and agents use the same rule base, so they get the same answer with the same requirement codes.

**Open the navigator:** [gfranistaken.github.io/aafdid-navigator](https://gfranistaken.github.io/aafdid-navigator/)

**Not a secure system.** Do not enter classified information, CUI, source selection or other procurement-sensitive information, proprietary data, or personal information into the web page or paste it into a profile. The page runs entirely in the browser and sends nothing you enter to a server, but it is an unofficial public website, not a U.S. Government system. A generic program label and rounded dollar figures are all it needs.

**Unofficial.** AAFDID itself is an overview: comply with its tabular notes and the full text of each cited source. This project is not affiliated with or endorsed by WARU, DAU or the Department of War.

| | |
| --- | --- |
| Rules | 1.0.0 · 268 requirement records across all six pathways |
| AAFDID capture | August 22, 2026 (every AAFDID table page, print-to-PDF, parsed in [aafdid-open](https://github.com/gfranistaken/aafdid-open)) |
| Live check | September 30, 2026: every captured row was located on the live AAFDID pages, and the differences found were corrected |
| Acquisition of Services | Drawn from DoDI 5000.74, because AAFDID has no AoS table |

## Pick your entry point

| You are | Use |
| --- | --- |
| A program manager, engineer or analyst | The [web navigator](https://gfranistaken.github.io/aafdid-navigator/), or `web/index.html` opened straight from disk (it works offline) |
| Building an agent in GenAI.mil, Claude, ChatGPT or similar | [`agent/`](agent/README.md): instructions, knowledge files and test scenarios |
| An agent or script that can run code | `node engine/cli.js profile.txt` or `python3 engine/aafdid.py profile.txt` |
| Maintaining the rules | `rules/`, `sources/`, `tools/`, `tests/` (see [docs/RULES.md](docs/RULES.md)) |

## The workflow

The web page and the agent follow the same five steps.

1. **Find the pathway.** Five yes/no questions lead to UCA, MTA, MCA, SWA, DBS or AoS, with the governing paragraph cited for each question.
2. **Describe the program.** Only the questions that change the answer for that pathway are asked, typically three to seven. "Not sure" is always allowed.
3. **See what applies.** Every requirement gets one of these statuses:

   | Status | Meaning |
   | --- | --- |
   | Required | The AAFDID marks match this program. Items are grouped as due at the next event, due at later events, ongoing, as required ("Other" column), or from earlier events. |
   | May apply | The item depends on a condition in its note, or on someone's discretion. The MTA "may be applicable" table and the CSDR plan authority's choices land here. |
   | Also review | UCA only: the MCA milestone and exception entries for the program's ACAT level, which AAFDID's UCA page says to use too. |
   | Only if triggered | Breaches, waivers, deviations, congressional inquiries, bridge contracts. |
   | Needs an answer | A profile answer is missing, so the question that settles it is shown. Unknown is never treated as no. |
   | Reference | APB rules that govern the baseline rather than documents to submit. |
   | Not applicable | The reason is given. |

4. **Tailor and approve.** Statutory items stay unless the statute allows a waiver. The decision authority may tailor regulatory items and records the decision, usually in the ADM.
5. **Hand it off.** Copy the profile block, a checklist, a Markdown report or JSON. An agent built from `agent/` reads the same profile block.

## Coverage

| Pathway | Records | Source tables |
| --- | --- | --- |
| MCA | 135 | Milestone and Phase (80), Recurring (3), Exceptions and Waivers (22), CCA (11), CSDR (6), APB rules (4), Breach definitions (3), plus EVMS (6) |
| MTA | 52 | Table 1 submissions to OSD (11), Statutory and Regulatory "may be applicable" (33), plus EVMS (6) and the two CSDR reports that cover MTA programs |
| UCA | 10 | UCA Unique (4), plus EVMS; also reviews the ACAT II and III entries of the MCA tables, as AAFDID directs |
| SWA | 51 | Application and Embedded SW (34), SWA CCA (11), plus EVMS |
| DBS | 27 | DBS Statutory (16), plus EVMS (6) and the five CSDR reports that cover IS programs |
| AoS | 24 | DoDI 5000.74 (Change 1, 2021) and DFARS 207.103 |

The six EVMS rows are shared by every pathway except AoS, because AAFDID notes that EVM is not specific to any one pathway. The six CSDR rows (`CSDR-01` to `CSDR-06`) carry their own pathway branches, because AAFDID's CSDR table covers ACAT I and II programs, IS programs (including DBS) and MTA programs over $100M.

## Changes since AAFDID's tables

AAFDID's tables predate several changes. Each one is attached to the records it affects:

- **MDAP and major system thresholds rose.** The FY2026 NDAA, sec. 1804, raised them to more than $1.0B RDT&E or $4.5B procurement, and to more than $275M or $1.3B, both in FY2024 dollars. AAFDID and DoDI 5000.85 still use the FY2020 figures.
- **JCIDS was disestablished** by the August 20, 2025 requirements memo.
- **The Warfighting Acquisition System memo** of November 7, 2025, created Portfolio Acquisition Executives and signaled a 5000-series rewrite.
- **EVMS thresholds changed** under DFARS Class Deviation 2026-O0011.
- **MTA rules changed** under DoDI 5000.80 Change 1 (November 2024) and 10 U.S.C. 3602.
- **The CMO position was repealed.** AAFDID's own DBS note already says so.

Details and sources are in [`rules/currency.json`](rules/currency.json).

## Repository layout

```
rules/        pathways.json, questions.json, currency.json (hand-written)
              requirements.json, meta.json, aafdid-rules.json (built)
sources/      aafdid-capture/ (AAFDID tables as captured), corrections-2026-09-30.json,
              aos-dodi-5000-74.json
engine/       aafdid.js (browser and Node), aafdid.py (Python port), cli.js
web/          template.html -> index.html (full page) and artifact.html (the same page as a
              fragment, for hosts that add their own document skeleton)
agent/        AGENT_INSTRUCTIONS.md, knowledge/, knowledge-combined/, tests/
tests/        scenarios/ (30 profiles), expected/ (snapshots), run_tests.py
tools/        build_rules.py, build_web.py, build_agent.py, build_all.sh
docs/         RULES.md (schema and condition language), PROVENANCE.md
```

## Build and test

Python 3.9 or later and Node 18 or later. No packages to install.

```
tools/build_all.sh           # rules -> tests -> web page -> agent pack
python3 tests/run_tests.py   # both engines, all scenarios: identical JSON, Markdown, checklist and profile block
```

`tests/run_tests.py --update` rewrites the snapshots after an intended rule change. Review the diff before you commit it.

## Publish the web page with GitHub Pages

The workflow in `.github/workflows/pages.yml` publishes `web/index.html` and the rules bundle on every push to `main`. To turn it on once, go to Settings > Pages > Build and deployment and set Source to GitHub Actions. The page then lives at `https://gfranistaken.github.io/aafdid-navigator/`, and the bundle at `.../aafdid-rules.json`.

## Limits worth knowing

- **Row-level applicability is automated; most note-level conditions are not.** Program type, system size, event, contract value, IT type and DOT&E oversight are evaluated; the DOT&E oversight gates come from AAFDID's own notes. Other notes add conditions this tool does not ask about, for example "if the program has international partners". Those rows are flagged "Conditions in note", and the note is shown verbatim.
- **Unrecognized input is reported, not guessed.** A field the rules don't use, or a value that matches no option, is listed as ignored and the field stays unknown.
- **Dollar thresholds stay as AAFDID prints them.** Where law or policy has since changed a threshold, a "Changed since" note says so rather than silently rewriting AAFDID.
- **AoS records come from DoDI 5000.74, not AAFDID,** and cite their paragraphs.
- **Requirement codes such as `MCA-M06` are tied to a release.** The `id` fields in the JSON stay stable across releases.

See [docs/PROVENANCE.md](docs/PROVENANCE.md) for how every record was captured and checked.

## License

Data and documentation: CC0-1.0, derived from U.S. Government works. Code (`engine/`, `tools/`, `tests/`, `web/`): MIT. See [LICENSE](LICENSE).
