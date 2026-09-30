# AAFDID extraction report — 2026-08-22

Source: browser print-to-PDF of every waru.edu/aafdid table page (waru.edu returns 403 to non-browser clients; Claude in Chrome is server-blocked on /aafdid/*).
Parsers: `tools/parse_mca.py` (dot/check grid), `tools/parse_cols.py` (column tables; `--gap-rows`, `--header=`) — moved into `tools/` as the documented re-extraction path (README.md Phase 1 runbook, Option B). Four prose-definition tables and two overview pages were transcribed verbatim from the PDF text layer and carry `extraction_method: manual_transcription_from_pdf_text`.

The 18 JSON files in this directory were then modeled into `data/` by
`tools/ingest_local_json.py` (README.md Phase 1 runbook, Option C). See
`data/DATASET_CARD.md` for the modeling conventions applied (event-name
expansion, source-citation parsing, `mta.json` truncation handling, excluded
parser-artifact rows).

| File | Table | Rows | Method |
|---|---|---|---|
| mca_milestone_phase.json | MCA — Milestone and Phase Information Requirements | 80 | geometry |
| mca_recurring.json | MCA — Recurring Program Reports | 3 | geometry |
| mca_exceptions.json | MCA — Exceptions, Waivers, and Alternative Management/Reporting | 22 | geometry |
| mca_apb.json | MCA — Acquisition Program Baselines | 4 | manual_transcription_from_pdf_text |
| mca_breach.json | MCA — Statutory Program Breach Definitions | 3 | manual_transcription_from_pdf_text |
| mca_csdr.json | MCA — Cost Data Reporting Requirements (CSDR) | 6 | manual_transcription_from_pdf_text |
| mca_evms_application.json | MCA — EVMS Application Requirements | 3 | geometry |
| mca_evms_reporting.json | MCA — EVMS Reporting Requirements | 3 | manual_transcription_from_pdf_text |
| mca_cca.json | MCA — CCA Compliance | 11 | geometry |
| mta.json | MTA — Statutory/Regulatory Requirements | 33 | geometry |
| mta_program_info.json | MTA — Submission Deliverables and Timelines to OSD | 12 | geometry |
| swa.json | SWA — Application and Embedded SW Information Requirements | 33 | geometry |
| swa_cca.json | SWA — Clinger-Cohen Act Compliance | 11 | geometry |
| swa_overview.json | SWA — Overview page | — | manual_transcription_from_pdf_text |
| dbs.json | DBS — Statutory Requirements | 17 | geometry |
| uca.json | UCA — Unique Information Requirements | 4 | geometry |
| aos_overview.json | AoS — Overview page (requirements table not yet published) | — | manual_transcription_from_pdf_text |
| title10_crosswalk.json | Title 10 Changes Summary Table (legacy → current section crosswalk) | 88 | geometry |

**Total rows: 333**

## Known gaps and caveats

- **mta.json — right-edge truncation: FIXED 2026-08-27.** Re-printed landscape (`raw_local/mta.pdf`) and re-parsed with `parse_cols.py`; approval authority and note text now complete for all 33 rows, same row set and marks as the portrait extraction. `parse_cols.py` now also merges rows wrapped across page breaks (including the `Test Strategy/Assessment of Test results` name split) and filters repeated page-header words out of note text.
- **mca_cca.json — footnote superscripts.** The CCA table carries footnote refs (3, 4, 5, 6, 7) per row; these are captured as `footnote_refs` where they were superscripts in the PDF text, but positional mapping to rows was not verified against the page image.
- **dbs.json** — 17 rows incl. the closing `None / Capability Support / N/A` row.
- **AoS** — AAFDID has no requirements table yet; overview only.
- **Whats-New / aafdid-background / AIR-Overview / title-10-overview / UCA, MTA, MCA, DBS overview pages** — not yet printed.
- Every row carries `provenance.source_url`, `pdf_page`, and a SHA-256 prefix of the source PDF. Nothing was generated from model memory.