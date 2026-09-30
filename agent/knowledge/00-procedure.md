# How to work: AAFDID Navigator procedure

Knowledge file 00 of the AAFDID Navigator agent pack. Read this first.

## What this is

A rule base for finding which AAFDID information requirements apply to a DoW acquisition program. It has 268 records across six pathways.
- AAFDID capture: 2026-08-22 (browser print-to-PDF of every AAFDID table page, parsed in the aafdid-open project).
- Live check: 2026-09-30: every captured row located on the live AAFDID pages; differences corrected (sources/corrections-2026-09-30.json).
- Acquisition of Services: DoDI 5000.74, Change 1 (2021-06-24); AAFDID has no AoS table.

## Program profile block

The profile is the program's answers. Read it when pasted, and print it exactly like this when asked:

```
AAFDID PROFILE v1
program: <name>
pathway: <mca|mta|uca|swa|dbs|aos>
event: <the next event's id from the pathway file, or omit>
<field>: <value>
unknown: <comma-separated fields not answered yet>
```

Only fields asked for the pathway appear (see 01-intake.md). Booleans are `yes` or `no`, and dollar amounts are plain numbers.

When reading a pasted profile, match values to the options in 01-intake.md, including the listed synonyms ("ACAT IC" is `mdap`; "Milestone B" is `ms_b`). If a field is not an intake field for the pathway, or a value matches no option, say which ones you could not use and treat those fields as unknown.

## Pathway finder

Answer in order. The first yes points to a pathway. The decision authority approves the choice, and programs may combine pathways (DoDI 5000.02, para 4.1.a). Ask in this order and stop at the first yes.

1. Are you buying services, meaning work performed by a contractor, rather than a product, system or software? Yes: AoS. No: next question.
   - Services at or above the simplified acquisition threshold follow DoDI 5000.74. Services managed as part of another pathway's program stay with that program. (DoDI 5000.02, para 4.2.f; DoDI 5000.74, paras 1.1.b and 1.2.a)
2. Is it a business system that supports business operations such as finance, contracting, logistics, budgeting, installations or human resources? Yes: DBS. No: next question.
   - Covered defense business system software uses the DBS pathway, though it may use the software pathway for custom-built parts (DoDI 5000.87, para 1.2.b). (DoDI 5000.02, para 4.2.e)
3. Does it answer a validated urgent operational need, fieldable in less than 2 years, at a cost below the MDAP thresholds? Yes: UCA. No: next question.
   - Urgent needs are designated under DoDD 5000.71 and DoDI 5000.81. The MDAP thresholds rose in December 2025, to more than $1.0B RDT&E or $4.5B procurement in FY2024 dollars (10 U.S.C. 4201). (DoDI 5000.02, para 4.2.a)
4. Is the effort mainly software: applications, or upgrades to software embedded in a weapon system? Yes: SWA. No: next question.
   - The application path covers software on commercial or modified hardware or cloud platforms. The embedded path covers upgrades to software in weapon systems, while the host system may stay on another pathway. (DoDI 5000.87, paras 1.2.b and 3.1.b; 10 U.S.C. 3603)
5. Can it be fielded within 5 years using mature technology, either as prototypes demonstrated in an operational environment or by starting production of a proven item within 6 months? Yes: MTA. No: MCA.
   - Rapid Prototyping: residual operational capability within 5 years. Rapid Fielding: production within 6 months and fielding within 5 years. Neither may be planned past those limits. (DoDI 5000.80, paras 1.2.c and 1.2.d)

## Procedure for "which requirements apply?"

1. Confirm the pathway. If the profile has none, run the pathway finder.
2. Note the next event (`event`). If it is missing, list requirements by event instead of splitting them.
3. Open the pathway's knowledge file. Use only records whose Pathway line names that pathway. The one exception is UCA, which also reviews some MCA rows (see 12-uca.md).
4. For each record, test its Condition code against the profile. `always` holds for every program on the pathway. A field the profile does not answer is unknown. `AND` is false if any part is false, and unknown if any part is unknown. `OR` is true if any part is true, and unknown if any part is unknown.
5. Assign a status:
   - The condition holds: use the record's "Status when the condition holds". Required, May apply, Only if triggered, or Reference rule.
   - The condition is false but the "May apply instead when" code holds: May apply.
   - The condition, or the "May apply instead when" code, is unknown: Needs an answer. Name only the fields that keep it unknown (skip parts of an `OR` that are already false), and ask their questions from 01-intake.md.
   - Otherwise: Not applicable. Give the Applies-when text as the reason.
6. Work out the type. If the record gives a type rule (Statutory if ..., otherwise ...), apply it to the profile. If its field is unknown, use the type the record gives for that case, or say the type depends on that answer, and ask the question. A "Type by event" rule gives each event its own type: show it beside each event (for example `MS B (update, statutory)`), and give the record the type at the next event when it is due there, otherwise Statutory and regulatory if its events differ.
7. Group the Required items when a next event is given:
   - Due at the next event: the When-due line includes the next event. SWA records due at "Each decision point" are due at every decision point, so they always go here.
   - Due at later events: it includes an event after the next one.
   - Ongoing: no event, such as recurring reports, contract-level items and compliance actions.
   - As required: its only events are AAFDID's "Other" column, not a numbered decision point.
   - From earlier events: all its numbered events come before the next one (it may also be due at Other). It should already exist; check for updates.
   Without a next event, list Required items under Due by event (with their events) and Ongoing.
   When the next event is Other, list the items due at Other first (Due at Other), then the rest under Due by event.
8. Then list, in this order: May apply, Also review (UCA only, see 12-uca.md), Only if triggered, Needs an answer, Reference rules, then Not applicable.
9. After the lists, add the questions that would settle more of the list: the ones behind Needs-an-answer items, types that depend on an answer, and for UCA the ACAT question.
10. Then add the "Changed since AAFDID" notes attached to listed records, and the notes in 20-changes-since-aafdid.md that change the answer. Then Not applicable, then the caveat below.

## Output format

Use this layout. Code, name, type, when, approval and source come from the record.

```
# AAFDID requirements: <program name>
- Pathway: <name> (<code>), <instruction>
- Next event: <event name, or 'not given; all events listed'>
- Counts: <n> required, <n> may apply, <n> also review, <n> triggered, <n> need an answer, <n> not applicable
  (leave out "also review" when there are none)

## Due at <event name> (<n>)
| Code | Requirement | Type | When | Approval | Source |
...
## Due by event (<n>)  (when no next event is given, or the next event is Other)
## Due at later events (<n>)
## Ongoing, contract-level and compliance items (<n>)
## As required (<n>)
## From earlier events (<n>)
## May apply: check the condition (<n>)
| Code | Requirement | Type | Condition | Source |
## Also review: MCA entries AAFDID points UCA programs to (<n>)  (UCA only)
## Only if triggered (<n>)
## Needs an answer (<n>)
| Code | Requirement | Missing answer |
## Reference rules (<n>)
## Questions that would settle more of the list
## Changes since AAFDID that affect this list
## Not applicable (<n>)  (list codes and reasons; may be shortened if asked)

Unofficial. AAFDID is an overview: comply with its tabular notes and the full text of each cited source.
```

## Tailoring

- Statutory requirements stay unless the statute itself allows a waiver (AAFDID MCA overview).
- The decision authority can tailor regulatory requirements. Record the decisions in writing, usually in the ADM or the approved acquisition strategy.
- Items marked "Part of Acquisition Strategy" belong inside the strategy, not in separate documents.
- Never call a statutory item tailorable, and never invent a waiver authority.

## Rules that prevent wrong answers

- Never add a requirement that is not a record in the knowledge files. If the user asks about one, say it is not in the AAFDID knowledge files.
- Never treat unknown as no. Unknown means Needs an answer.
- Keep dollar thresholds as written, with their dollar basis. Do not convert them.
- Cite by code and name, for example `MCA-M06 ACQUISITION PROGRAM BASELINE (APB)`.
- Record codes belong to this rules release. Record ids in the JSON (`rules/aafdid-rules.json`) stay stable across releases.

## Worked example

Profile:

```
AAFDID PROFILE v1
program: F3 replacement power supply (example)
pathway: mta
event: entrance
mta_path: rf
mta_size: non_major
contract_value: 45000000
contract_cost_type: no
```

Correct result (the not-applicable list is left out):

# AAFDID requirements: F3 replacement power supply (example)

- Pathway: Middle Tier of Acquisition (MTA), DoDI 5000.80 (Change 1, November 2024); 10 U.S.C. 3602
- Next event: Program entrance: the ADM starts the MTA clock
- Counts: 6 required, 23 may apply, 0 triggered, 0 need an answer, 23 not applicable
- Rules 1.0.0: AAFDID capture 2026-08-22, checked live 2026-09-30

## Due at Program entrance: the ADM starts the MTA clock (2)

| Code | Requirement | Type | When | Approval | Source |
| --- | --- | --- | --- | --- | --- |
| MTA-T02 | ADM signed by the DA | Regulatory | Entrance |  | DoDI 5000.80 |
| MTA-T05 | Initial PID Entry | Regulatory | Entrance |  | DoDI 5000.80 |

## Due at later events (4)

| Code | Requirement | Type | When | Approval | Source |
| --- | --- | --- | --- | --- | --- |
| MTA-T08 | Updated PID Entry | Regulatory | Execution |  | DoDI 5000.80 |
| MTA-T09 | An assessment of test results | Regulatory | Exit |  | DoDI 5000.80 |
| MTA-T10 | Final PID capturing updated entries, to include the outcome, sustainment, and final budget of the MTA program | Regulatory | Exit |  | DoDI 5000.80 |
| MTA-T11 | Outcome determination ADM signed by the DA | Regulatory | Exit |  | DoDI 5000.80 |

## May apply: check the condition (23)

| Code | Requirement | Type | Condition or trigger | Source |
| --- | --- | --- | --- | --- |
| CSDR-02 | Contractor Cost Data Report | Regulatory | ACAT I and II programs: contracts over $50M, or $20M to $50M at the CSDR plan authority's discretion. MTA programs over $100M: contracts over $20M. IS programs over $100M, including DBS: contracts over $50M. All then-year dollars. | DoDI 5000.73 |
| CSDR-05 | Software Resources Data Report | Regulatory | Software development, production or maintenance efforts over $20M then-year for ACAT I and II programs, IS programs over $100M (including DBS) and MTA programs over $100M. | DoDI 5000.73 |
| MTA-S01 | Acquisition Decision Memorandum (ADM) | Regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | DoDI 5000.80 |
| MTA-S02 | ACQUISITION STRATEGY | Regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | DoDi 5000.80 10 U.S.C. 4211 {formerly 2431a} |
| MTA-S09 | INTELLECTUAL PROPERTY (IP) STRATEGY (Part of Acquisition Strategy) | Statutory and regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | DoDI 5010.44 10 U.S.C. 3771- 3775 {formerly 2320} 10 U.S.C. 4211 {formerly 2431a} |
| MTA-S10 | International Involvement (Part of Acquisition Strategy) | Regulatory | AAFDID marks no size column for this row. Its note ties it to the statutory requirement to consider cooperative opportunities, which applies to every program; DoDI 5000.80 Change 1 adds exportability when international partners are involved. | DoDI 5000.80 |
| MTA-S15 | RELIABILITY AND MAINTAINABILITY (Part of Acquisition Strategy) | Statutory and regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | 10 U.S.C. 4328 {formerly 2443} January 31, 2019 USD(A&S) Policy Memo, "Implementation of Title 10, United States Code, Section 2443, Sustainment Factors in Weapon System Design." DoDI 5000.88 |
| MTA-S17 | Test Strategy/Assessment of Test results (Part of Acquisition Strategy) | Regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | DoDI 5000.80 DoDI 5000.89 |
| MTA-S18 | Transition Plan (Part of Acquisition Strategy) | Regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | DoDI 5000.80 |
| MTA-S19 | CLINGER-COHEN ACT (CCA) COMPLIANCE | Statutory and regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | DoDi 5000.82 SUBTITLE III, TITLE 40 §811, P.L. 106-398 |
| MTA-S20 | CYBERSECURITY STRATEGY | Statutory and regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | DoDi 8500.01 DoDi 5000.82 §811, P.L. 106-398 40 U.S.C. 11313 |
| MTA-S21 | DoD Component Cost Estimate | Regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | DoDI 5000.73 DoDI 5000.80 |
| MTA-S22 | Exit Criteria | Regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | This Table |
| MTA-S23 | FREQUENCY ALLOCATION APPLICATION (DD FORM 1494) | Statutory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | §104, P.L. 102-538 47 U.S.C. 305, 901-904 |
| MTA-S24 | Full Funding Certification Memorandum | Regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | DoDI 5000.73 |
| MTA-S25 | Independent Cost Estimate (ICE) | Statutory and regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | 10 U.S.C. 4323 {formerly 2441} DoDI 5000.73 |
| MTA-S26 | Information Support Plan (ISP) | Regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | DoDI 8330.01 DoDI 8320.02 DoDI 8410.03 |
| MTA-S27 | Information Technology and National Security System Interoperability Certification | Regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | DoDI 5000.80 DoDI 8330.01 |
| MTA-S28 | LIFECYCLE SUSTAINMENT PLAN (LCSP)/PRODUCT SUPPORT STRATEGY (PSS) | Statutory and regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | 10 U.S.C 4324 {formerly 2337} DoDI 5000.80 DoDI 5000.91 |
| MTA-S29 | PESHE AND NEPA/E.O. 12114 COMPLIANCE SCHEDULE (Part of LCSP/PSS) | Statutory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | 42 U.S.C. 4321-4347 E.O. 12114 |
| MTA-S30 | Program Protection Plan (PPP) | Regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | DoDI 5200.39 DoDI 5200.44 |
| MTA-S31 | Request for Proposal (RFP) | Regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | Federal Acquisition Regulation (FAR) Subpart 15.203 |
| MTA-S33 | Systems Engineering Plan (SEP) | Regulatory | For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items. | DoDI 5000.88 This Table |

## Changes since AAFDID that affect this list

- **MDAP and major system thresholds raised** (2025-12-18). The FY2026 NDAA (Pub. L. 119-60, sec. 1804) raised the statutory MDAP threshold to more than $1.0B RDT&E or $4.5B procurement, and the major system threshold to more than $275M RDT&E or $1.3B procurement, both in FY2024 constant dollars. DoDI 5000.85 Table 1 and AAFDID still use the older FY2020 figures ($525M / $3.065B and $200M / $920M). Confirm your program's category against the current statute and your component's direction. Source: [10 U.S.C. 4201 (MDAP definition)](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title10-section4201&num=0&edition=prelim); [10 U.S.C. 3041 (major system definition)](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title10-section3041&num=0&edition=prelim)
- **DoDI 5000.80 Change 1 and 10 U.S.C. 3602** (2024-11-25). DoDI 5000.80 Change 1 changed several MTA rules: - The transition plan goes to OUSD(A&S) through AIR within 2 years of program start. - Transition documentation must be complete 3 months before completion. - A termination is reported to OUSD(A&S) within 7 days and to Congress within 30 days. - Requirement approval may be delegated no lower than the PM. - Test strategies cover non-kinetic threats. - Exportability applies when international partners are involved. 10 U.S.C. 3602 (December 2024) codified MTA, and lets the service acquisition executive permit further 5-year periods. AAFDID's MTA notes cite the October 2022 policy update. Source: [DoDI 5000.80 Original vs Change 1 briefing (Feb 2025)](https://www.waru.edu/sites/default/files/2025-02/DODI%205000_80%20Original%20vs%20Change1%20Webinar%20202502%20no%20notes.pdf); [10 U.S.C. 3602](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title10-section3602&num=0&edition=prelim)

_Unofficial. AAFDID is itself an overview: comply with its tabular notes and the full text of each cited source. Not affiliated with or endorsed by WARU, DAU or the Department of War._
