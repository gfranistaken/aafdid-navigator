# Provenance

This page explains where every record came from and how it was checked. Nothing in the rules was written from memory.

## 1. AAFDID capture (August 22–27, 2026)

The AAFDID site (`www.waru.edu/aafdid/...`) refuses automated clients, so each table page was printed to PDF from a browser and parsed. The capture is by the aafdid-open project ([aafdid-open](https://github.com/gfranistaken/aafdid-open), `aafdid-raw/`). The MTA table was printed again in landscape on August 27 to recover its right-hand columns.

The capture has 18 files: 17 tables and overview pages, plus the Title 10 crosswalk. They are copied unchanged into `sources/aafdid-capture/`, with the original `EXTRACTION_REPORT.md`.

## 2. Live check against AAFDID (September 30, 2026)

Every live table page was read through a fetch tool and compared row by row with the capture. For the long MCA milestone page, the site's `?search=` filter was used to reach every row.

| Table | Live rows | Result |
| --- | --- | --- |
| MCA Milestone and Phase | 80 | 78 rows exact; the OTP and SEP rows also list ACAT IAM/IAC (MAIS), which the capture missed (corrected) |
| MCA Recurring, Exceptions, CCA, CSDR, EVMS (2 tables), APB, Breach | 3, 22, 11, 6, 3 + 3, 4, 3 | Names, marks and thresholds match. CCA action text and footnotes were cleaned from the live page (corrected). |
| MTA Statutory/Regulatory | 33 | Marks, type and approval match. One note is missing a memo citation (added as an addendum). |
| MTA Program Information (Table 1) | 11 | Capture had an extra header row (dropped). The TYPE column (all Regulatory) and footnotes were taken from the live page. |
| SWA Application and Embedded SW | 34 | Capture was missing "Information Support Plan" (added). Cybersecurity TYPE and SOURCE and Market Research SOURCE were completed. |
| SWA CCA | 11 | One action's truncated text was completed. |
| DBS Statutory | 17 | Match. The Auditability source was completed, and the closing "None" row was dropped. |
| UCA Unique | 4 | Match |

Every correction, with the live text as evidence, is in `sources/corrections-2026-09-30.json`. `tools/build_rules.py` applies them, and each record's `provenance.check` says whether it matched or was corrected.

AAFDID's What's New page lists one entry (February 2023). Its Excel exports are filed under January 2025, and no table page shows a last-updated date.

## 3. Acquisition of Services (September 30, 2026)

AAFDID has no AoS requirements table. The 24 AoS records come from these sources, and each cites its paragraph:

- DoDI 5000.74, *Defense Acquisition of Services* (January 10, 2020, Change 1 effective June 24, 2021)
- the AAF services pages
- DFARS 207.103(d)(i)(B), which sets the written acquisition plan threshold: $50M for all years or $25M in any fiscal year, as shown on acquisition.gov with effective date May 7, 2026

The DoDI still uses pre-2022 Title 10 numbers. Renumbered sections are added only where AAFDID's own Title 10 crosswalk gives them.

## 4. Pathway finder

Each finder question cites the paragraph it rests on:

- DoDI 5000.02, para 4.2 (the pathway descriptions) and para 4.1.a (combining pathways)
- DoDI 5000.80, paras 1.2.c and 1.2.d
- DoDI 5000.87, paras 1.2.b and 3.1.b
- DoDI 5000.74, paras 1.1.b and 1.2.a

The UCA question uses the MDAP thresholds as amended in December 2025 (10 U.S.C. 4201).

## 5. Changes since AAFDID

`rules/currency.json` records changes made after AAFDID's tables were last updated. Each has primary or reliable sources:

| Change | Source |
| --- | --- |
| MDAP and major system thresholds | 10 U.S.C. 4201 and 3041 as amended by Pub. L. 119-60, sec. 1804 (uscode.house.gov) |
| JCIDS disestablished | The August 20, 2025 memo, as reported and archived in the WARU library |
| Warfighting Acquisition System | The November 7, 2025 memo |
| EVMS thresholds | DFARS Class Deviation 2026-O0011, checked on September 29–30, 2026 for the companion work-statement templates |
| MTA | DoDI 5000.80 Change 1 through the WARU comparison briefing (the posted DoDI PDF still showed the 2019 original); 10 U.S.C. 3602 |

## Known gaps

- The AAFDID Excel exports were not read directly, because the site blocks downloads from this environment. A browser-saved copy would allow a byte-level re-check.
- DoDI 5000.81 (UCA) and DoDI 5000.75 (DBS) could not be fetched during the check. UCA and DBS records rest on AAFDID's tables, which were checked live.
- Conditions stated only inside AAFDID notes are shown, not evaluated. Rows whose notes contain conditional wording are flagged.
- The EVMS and CSDR rows keep AAFDID's thresholds. The deviation note says where the EVMS thresholds have changed.
