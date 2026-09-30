# AAFDID Navigator knowledge, all files combined

Use this single file when a platform limits the number of knowledge files. It is the nine files in agent/knowledge joined in order.

---

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


---

# Intake questions

Knowledge file 01 of the AAFDID Navigator agent pack.

Ask only the questions shown for the program's pathway, one at a time. If the answer is not known, leave it blank. Requirements that depend on it are reported as undetermined, together with the question that settles them.

Ask the questions for the program's pathway in the order below, one per message. Always offer "not sure". Record each answer under its field name using the value in the left column of its options table.

## MCA: Major Capability Acquisition

1. `pathway`: Which acquisition pathway is the program on?
   - Answer `mca` for this section.
   - Why it matters: Every requirement belongs to a pathway, so this answer scopes everything else.
   - Affects: CSDR-01, CSDR-02, CSDR-03, CSDR-05, CSDR-06
2. `event`: Which decision point or phase comes next?
   - Values: `mdd` = Materiel Development Decision; `ms_a` = Milestone A; `cdd_val` = Capability Development Document validation (also: CDD Validation, CDD); `dev_rfp_rel` = Development RFP Release Decision (also: Dev RFP Release, Development RFP Release, Development RFP Release Decision Point, DRFPRD, RFP Release); `ms_b` = Milestone B; `ms_c` = Milestone C; `frp_dec` = Full-Rate Production or Full Deployment Decision (also: FRP, FD, FRP Decision, FDD, Full-Rate Production, Full Deployment, Full-Rate Production Decision, Full Deployment Decision); `other` = Other, as required. Leave blank to list every event.
   - Why it matters: Requirements due at that event are listed first, then later ones, then recurring and triggered items.
3. `mca_program_type`: What is the program's acquisition category?
   - Values: `mdap` = ACAT IB, IC or ID (MDAP) (also: MDAP, ACAT I, ACAT IB, ACAT IC, ACAT ID, ACAT IC or ID, ACAT IC or ID (MDAP)); `mais` = ACAT IAM or IAC (MAIS), legacy (also: MAIS, ACAT IAM, ACAT IAC, ACAT IAM or IAC); `acat_ii` = ACAT II (major system) (also: ACAT II, II, major system); `acat_iii` = ACAT III and below (also: ACAT III, III, ACAT III and below, ACAT III or below, ACAT IV)
     - `mdap`: AAFDID label: ACAT IC or ID (MDAP). The statutory MDAP threshold is more than $1.0B RDT&E or $4.5B procurement in FY2024 dollars (10 U.S.C. 4201, amended December 2025). DoDI 5000.85 Table 1 still shows $525M and $3.065B in FY2020 dollars.
     - `mais`: Only two AAFDID rows still list MAIS: the Systems Engineering Plan and the Operational Test Plan.
     - `acat_ii`: The statutory major system threshold is more than $275M RDT&E or $1.3B procurement in FY2024 dollars (10 U.S.C. 3041(c), amended December 2025). DoDI 5000.85 Table 1 still shows $200M and $920M in FY2020 dollars.
   - Why it matters: AAFDID's MCA tables mark each requirement by program type.
   - Affects: CSDR-01, CSDR-02, CSDR-03, CSDR-04, CSDR-05, CSDR-06, MCA-B01, MCA-B02, MCA-B03, MCA-B04, MCA-M01, MCA-M02, MCA-M03, MCA-M04, MCA-M05, MCA-M06, MCA-M07, MCA-M08, MCA-M09, MCA-M10, MCA-M11, MCA-M12, MCA-M13, MCA-M14, MCA-M15, MCA-M16, MCA-M17, MCA-M18, MCA-M19, MCA-M20, MCA-M21, MCA-M22, MCA-M23, MCA-M24, MCA-M25, MCA-M26, MCA-M27, MCA-M28, MCA-M29, MCA-M30, MCA-M31, MCA-M32, MCA-M33, MCA-M34, MCA-M35, MCA-M36, MCA-M37, MCA-M38, MCA-M39, MCA-M40, MCA-M41, MCA-M42, MCA-M43, MCA-M44, MCA-M45, MCA-M46, MCA-M47, MCA-M48, MCA-M49, MCA-M50, MCA-M51, MCA-M52, MCA-M53, MCA-M54, MCA-M55, MCA-M57, MCA-M58, MCA-M59, MCA-M60, MCA-M61, MCA-M62, MCA-M63, MCA-M64, MCA-M65, MCA-M66, MCA-M67, MCA-M68, MCA-M69, MCA-M70, MCA-M71, MCA-M72, MCA-M73, MCA-M75, MCA-M76, MCA-M77, MCA-M78, MCA-M79, MCA-M80, MCA-N01, MCA-N02, MCA-N03, MCA-R01, MCA-R02, MCA-R03, MCA-X01, MCA-X02, MCA-X03, MCA-X04, MCA-X05, MCA-X06, MCA-X07, MCA-X08, MCA-X09, MCA-X10, MCA-X11, MCA-X12, MCA-X13, MCA-X14, MCA-X15, MCA-X16, MCA-X17, MCA-X18, MCA-X19, MCA-X20, MCA-X21, MCA-X22
4. `dote_oversight`: Is the program on the DOT&E oversight list (including LFT&E oversight)?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: IOT&E reports, live fire reports and waivers apply only to oversight programs, and DOT&E approval of the operational test plan is statutory for them.
   - Affects: MCA-M28, MCA-M29, MCA-M56, MCA-X01, MCA-X16, MCA-X22
5. `it_type`: Does the system include information technology?
   - Values: `it_system` = Yes, it is an IT system, including a national security system (also: IT, IT system, NSS, national security system, yes); `embedded_it` = Only IT embedded in a weapon system, or a command and control system that is not itself IT (also: embedded, embedded IT, weapon system); `none` = No IT (also: no IT, no)
   - Why it matters: Decides the Clinger-Cohen Act entries. AAFDID presumes the first three CCA actions are satisfied for weapon systems with embedded IT.
   - Affects: MCA-C01, MCA-C02, MCA-C03, MCA-C04, MCA-C05, MCA-C06, MCA-C07, MCA-C08, MCA-C09, MCA-C10, MCA-C11, MCA-M15
6. `contract_value`: What is the largest planned contract or agreement value, including options, in then-year dollars?
   - Value: a dollar amount such as `45000000`, `45M` or `1.2B`. A rounded figure is enough, because the rules only compare it with thresholds.
   - Why it matters: EVMS and cost data reporting thresholds are set by contract value.
   - Affects: CSDR-02, CSDR-03, CSDR-04, CSDR-05, CSDR-06, EVM-01, EVM-02, EVM-03, EVM-04, EVM-05, EVM-06
7. `contract_cost_type`: Is that contract cost-reimbursable or incentive-type, with 18 months or more of performance?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: AAFDID applies EVMS to cost-reimbursable or incentive contracts of 18 months or more.
   - Affects: EVM-01, EVM-02, EVM-03, EVM-05, EVM-06

## MTA: Middle Tier of Acquisition

1. `pathway`: Which acquisition pathway is the program on?
   - Answer `mta` for this section.
   - Why it matters: Every requirement belongs to a pathway, so this answer scopes everything else.
   - Affects: CSDR-02, CSDR-05
2. `event`: Which decision point or phase comes next?
   - Values: `entrance` = Program entrance: the ADM starts the MTA clock (also: program start, start, program entrance, entry, MTA start); `execution` = Throughout program execution (also: during execution, throughout execution); `exit` = Program exit: the outcome ADM (also: program exit, outcome, completion, transition). Leave blank to list every event.
   - Why it matters: Requirements due at that event are listed first, then later ones, then recurring and triggered items.
3. `mta_path`: Is it Rapid Prototyping or Rapid Fielding?
   - Values: `rp` = Rapid Prototyping (also: RP, rapid prototyping, prototyping); `rf` = Rapid Fielding (also: RF, rapid fielding, fielding)
   - Why it matters: AAFDID's tables do not split the two paths, but CAPE's cost-estimate threshold differs, and DoDI 5000.80 asks for a lifecycle sustainment plan for Rapid Fielding.
   - Affects: MTA-T06
4. `mta_size`: Where does the program sit against the major system and MDAP thresholds?
   - Values: `non_major` = Not a major system (also: non-major, nonmajor, non major, not major, not a major system); `major` = Major system, below MDAP thresholds (also: major, major system); `exceeds_mdap` = Above MDAP thresholds (also: exceeds MDAP, above MDAP, MDAP, above MDAP thresholds, exceeds MDAP threshold)
     - `non_major`: At or below 10 U.S.C. 3041(c): $275M RDT&E or $1.3B procurement in FY2024 dollars.
     - `exceeds_mdap`: More than $1.0B RDT&E or $4.5B procurement in FY2024 dollars (10 U.S.C. 4201). Needs USD(A&S) written approval to use MTA.
   - Why it matters: AAFDID's MTA tables mark each requirement for major systems, non-major systems, or programs above MDAP thresholds.
   - Affects: CSDR-02, MTA-S02, MTA-S03, MTA-S04, MTA-S05, MTA-S06, MTA-S07, MTA-S08, MTA-S11, MTA-S12, MTA-S13, MTA-S14, MTA-S16, MTA-S32, MTA-T01, MTA-T03, MTA-T04, MTA-T06, MTA-T07
5. `contract_value`: What is the largest planned contract or agreement value, including options, in then-year dollars?
   - Value: a dollar amount such as `45000000`, `45M` or `1.2B`. A rounded figure is enough, because the rules only compare it with thresholds.
   - Why it matters: EVMS and cost data reporting thresholds are set by contract value.
   - Affects: CSDR-02, CSDR-05, EVM-01, EVM-02, EVM-03, EVM-04, EVM-05, EVM-06
6. `contract_cost_type`: Is that contract cost-reimbursable or incentive-type, with 18 months or more of performance?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: AAFDID applies EVMS to cost-reimbursable or incentive contracts of 18 months or more.
   - Affects: EVM-01, EVM-02, EVM-03, EVM-05, EVM-06

## UCA: Urgent Capability Acquisition

1. `pathway`: Which acquisition pathway is the program on?
   - Answer `uca` for this section.
   - Why it matters: Every requirement belongs to a pathway, so this answer scopes everything else.
   - Also affects these MCA entries to review (12-uca.md): CSDR-01, CSDR-02, CSDR-03, CSDR-05, CSDR-06
2. `event`: Which decision point or phase comes next?
   - Values: `development` = Development Milestone (also: dev); `production` = Production and Deployment Milestone (also: production and deployment); `other` = Other, including disposition (also: disposition). Leave blank to list every event.
   - Why it matters: Requirements due at that event are listed first, then later ones, then recurring and triggered items.
3. `uca_acat`: What ACAT level would the program be?
   - Values: `acat_ii` = ACAT II (also: ACAT II, II); `acat_iii` = ACAT III or below (also: ACAT III, III, ACAT III and below, ACAT III or below)
   - Why it matters: The UCA table, and the MCA entries AAFDID points UCA programs to, are marked by ACAT level.
   - Also affects these MCA entries to review (12-uca.md): MCA-M04, MCA-M05, MCA-M06, MCA-M07, MCA-M08, MCA-M09, MCA-M10, MCA-M11, MCA-M12, MCA-M13, MCA-M14, MCA-M15, MCA-M16, MCA-M18, MCA-M19, MCA-M20, MCA-M23, MCA-M24, MCA-M28, MCA-M29, MCA-M32, MCA-M33, MCA-M35, MCA-M39, MCA-M40, MCA-M41, MCA-M42, MCA-M43, MCA-M44, MCA-M45, MCA-M46, MCA-M47, MCA-M48, MCA-M49, MCA-M51, MCA-M52, MCA-M53, MCA-M54, MCA-M55, MCA-M56, MCA-M57, MCA-M58, MCA-M61, MCA-M62, MCA-M65, MCA-M66, MCA-M68, MCA-M69, MCA-M70, MCA-M71, MCA-M72, MCA-M74, MCA-M76, MCA-M78, MCA-M79, MCA-M80, MCA-X01, MCA-X03, MCA-X05, MCA-X06, MCA-X10, MCA-X11, MCA-X15, MCA-X16, MCA-X17, MCA-X20, MCA-X22
4. `dote_oversight`: Is the program on the DOT&E oversight list (including LFT&E oversight)?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: IOT&E reports, live fire reports and waivers apply only to oversight programs, and DOT&E approval of the operational test plan is statutory for them.
   - Also affects these MCA entries to review (12-uca.md): DBS-14, DBS-15, DBS-16, MCA-M28, MCA-M29, MCA-M56, MCA-X01, MCA-X16, MCA-X22, SWA-21, SWA-23
5. `it_type`: Does the system include information technology?
   - Values: `it_system` = Yes, it is an IT system, including a national security system (also: IT, IT system, NSS, national security system, yes); `embedded_it` = Only IT embedded in a weapon system, or a command and control system that is not itself IT (also: embedded, embedded IT, weapon system); `none` = No IT (also: no IT, no)
   - Why it matters: Decides the Clinger-Cohen Act entries. AAFDID presumes the first three CCA actions are satisfied for weapon systems with embedded IT.
   - Also affects these MCA entries to review (12-uca.md): MCA-C01, MCA-C02, MCA-C03, MCA-C04, MCA-C05, MCA-C06, MCA-C07, MCA-C08, MCA-C09, MCA-C10, MCA-C11, MCA-M15
6. `contract_value`: What is the largest planned contract or agreement value, including options, in then-year dollars?
   - Value: a dollar amount such as `45000000`, `45M` or `1.2B`. A rounded figure is enough, because the rules only compare it with thresholds.
   - Why it matters: EVMS and cost data reporting thresholds are set by contract value.
   - Affects: EVM-01, EVM-02, EVM-03, EVM-04, EVM-05, EVM-06
   - Also affects these MCA entries to review (12-uca.md): CSDR-02, CSDR-03, CSDR-04, CSDR-05, CSDR-06, SWA-19
7. `contract_cost_type`: Is that contract cost-reimbursable or incentive-type, with 18 months or more of performance?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: AAFDID applies EVMS to cost-reimbursable or incentive contracts of 18 months or more.
   - Affects: EVM-01, EVM-02, EVM-03, EVM-05, EVM-06

## SWA: Software Acquisition

1. `pathway`: Which acquisition pathway is the program on?
   - Answer `swa` for this section.
   - Why it matters: Every requirement belongs to a pathway, so this answer scopes everything else.
2. `event`: Which decision point or phase comes next?
   - Values: `planning` = Entering the planning phase (also: planning phase, entering planning); `execution_entry` = Entering the execution phase (also: entering execution, execution phase entry); `execution` = During the execution phase (also: during execution). Leave blank to list every event.
   - Why it matters: Requirements due at that event are listed first, then later ones, then recurring and triggered items.
3. `swa_above_acat_ii`: Would the program's cost exceed the ACAT II thresholds?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: AAFDID makes the acquisition strategy and bandwidth review statutory above ACAT II, and CAPE prepares the independent cost estimate above ACAT II unless it delegates.
   - Affects: SWA-04, SWA-05
4. `mission_critical_it`: Is it mission-critical or mission-essential IT?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: The cybersecurity strategy is statutory for mission-critical and mission-essential IT (40 U.S.C. 11313).
   - Affects: SWA-09
5. `dote_oversight`: Is the program on the DOT&E oversight list (including LFT&E oversight)?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: IOT&E reports, live fire reports and waivers apply only to oversight programs, and DOT&E approval of the operational test plan is statutory for them.
   - Affects: SWA-21, SWA-23
6. `software_maintenance`: Will the program need government software maintenance that counts toward core logistics?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: The Core Logistics Determination is statutory for programs with software maintenance (10 U.S.C. 2464).
   - Affects: SWA-20
7. `contract_value`: What is the largest planned contract or agreement value, including options, in then-year dollars?
   - Value: a dollar amount such as `45000000`, `45M` or `1.2B`. A rounded figure is enough, because the rules only compare it with thresholds.
   - Why it matters: EVMS and cost data reporting thresholds are set by contract value.
   - Affects: EVM-01, EVM-02, EVM-03, EVM-04, EVM-05, EVM-06, SWA-19
8. `contract_cost_type`: Is that contract cost-reimbursable or incentive-type, with 18 months or more of performance?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: AAFDID applies EVMS to cost-reimbursable or incentive contracts of 18 months or more.
   - Affects: EVM-01, EVM-02, EVM-03, EVM-05, EVM-06

## DBS: Defense Business Systems

1. `pathway`: Which acquisition pathway is the program on?
   - Answer `dbs` for this section.
   - Why it matters: Every requirement belongs to a pathway, so this answer scopes everything else.
   - Affects: CSDR-01, CSDR-02, CSDR-03, CSDR-05, CSDR-06
2. `event`: Which decision point or phase comes next?
   - Values: `solution_analysis_atp` = Solution Analysis ATP (also: solution analysis); `functional_requirements_atp` = Functional Requirements ATP (also: functional requirements); `acquisition_atp` = Acquisition ATP (also: acquisition); `contract_award` = Contract award; `limited_deployment_atp` = Limited Deployment ATP(s) (also: limited deployment); `full_deployment_atp` = Full Deployment ATP (also: full deployment); `capability_support_atp` = Capability Support ATP (also: capability support). Leave blank to list every event.
   - Why it matters: Requirements due at that event are listed first, then later ones, then recurring and triggered items.
3. `mission_critical_it`: Is it mission-critical or mission-essential IT?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: The cybersecurity strategy is statutory for mission-critical and mission-essential IT (40 U.S.C. 11313).
   - Affects: DBS-06
4. `dote_oversight`: Is the program on the DOT&E oversight list (including LFT&E oversight)?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: IOT&E reports, live fire reports and waivers apply only to oversight programs, and DOT&E approval of the operational test plan is statutory for them.
   - Affects: DBS-14, DBS-15, DBS-16
5. `contract_value`: What is the largest planned contract or agreement value, including options, in then-year dollars?
   - Value: a dollar amount such as `45000000`, `45M` or `1.2B`. A rounded figure is enough, because the rules only compare it with thresholds.
   - Why it matters: EVMS and cost data reporting thresholds are set by contract value.
   - Affects: CSDR-02, CSDR-03, CSDR-05, CSDR-06, EVM-01, EVM-02, EVM-03, EVM-04, EVM-05, EVM-06
6. `contract_cost_type`: Is that contract cost-reimbursable or incentive-type, with 18 months or more of performance?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: AAFDID applies EVMS to cost-reimbursable or incentive contracts of 18 months or more.
   - Affects: EVM-01, EVM-02, EVM-03, EVM-05, EVM-06

## AoS: Acquisition of Services

1. `pathway`: Which acquisition pathway is the program on?
   - Answer `aos` for this section.
   - Why it matters: Every requirement belongs to a pathway, so this answer scopes everything else.
2. `event`: Which decision point or phase comes next?
   - Values: `plan` = Plan: form the team, review the current strategy, market research (also: planning, plan phase); `develop` = Develop: define requirements, SRRB, acquisition strategy (also: development, develop phase); `execute` = Execute: award and manage performance (also: execution, execute phase). Leave blank to list every event.
   - Why it matters: Requirements due at that event are listed first, then later ones, then recurring and triggered items.
3. `svc_total_value`: What is the total estimated value of the services, all years, in current-year dollars?
   - Value: a dollar amount such as `45000000`, `45M` or `1.2B`. A rounded figure is enough, because the rules only compare it with thresholds.
   - Why it matters: Sets the services category (S-CAT), the decision authority and most thresholds (DoDI 5000.74, Table 1).
   - Affects: AOS-05, AOS-06, AOS-08, AOS-09, AOS-10, AOS-11, AOS-21, AOS-22
4. `svc_annual_value`: What is the highest estimated value in any single year?
   - Value: a dollar amount such as `45000000`, `45M` or `1.2B`. A rounded figure is enough, because the rules only compare it with thresholds.
   - Why it matters: S-CAT I applies above $300M in any year. A Services Acquisition Workshop is required at $250M a year, and a written acquisition plan at $25M in any fiscal year.
   - Affects: AOS-08, AOS-10, AOS-11
5. `svc_special_interest`: Has ASD(A) designated it a Special Interest services acquisition?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: Makes USD(A&S) or designee the decision authority.
6. `svc_vehicle`: How will the services be bought?
   - Values: `standalone` = A standalone contract, or a single-award IDIQ (also: standalone, contract, single-award IDIQ, single award); `idiq_base` = The base award of a multiple-award IDIQ (also: IDIQ base, MA-IDIQ base, MAC base, multiple-award IDIQ, base award); `task_order` = A task order under an IDIQ (enter the order's value above) (also: task order, TO, order, delivery order)
   - Why it matters: A Services Acquisition Workshop is not required for a multiple-award IDIQ base, but it is required for any task order of $100M or more (DoDI 5000.74, para 4.2.d).
   - Affects: AOS-08
7. `svc_overlap`: Could it significantly overlap an existing contract, a DoD or government-wide vehicle, or a best-in-class contract?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: Triggers a business case analysis at $50M or more (DoDI 5000.74, para 3.3.d(9)).
   - Affects: AOS-09
8. `svc_sensitive_functions`: Will contractors perform critical functions, or functions closely associated with inherently governmental functions?
   - Values: `yes`, `no`, or leave blank if not sure.
   - Why it matters: Those functions must be reviewed, justified and reduced where practicable (DoDI 5000.74, para 1.2.c).
   - Affects: AOS-07


---

# MCA requirements: Major Capability Acquisition

Knowledge file 10 of the AAFDID Navigator agent pack, rules 1.0.0. Every record below belongs to the MCA pathway only.

- Governing instruction: DoDI 5000.85
- Summary: Milestone-based pathway for MDAPs, major systems and other complex acquisitions. The milestone decision authority sets the entry point: MDD, Milestone A, B or C.
- Decision authority: ACAT ID: the Defense Acquisition Executive. ACAT IB: the service acquisition executive. ACAT IC and II: the component acquisition executive or designee. ACAT III: as the component acquisition executive designates (DoDI 5000.85, Table 1).
- Events, in order: `mdd` = Materiel Development Decision; `ms_a` = Milestone A; `cdd_val` = Capability Development Document validation; `dev_rfp_rel` = Development RFP Release Decision; `ms_b` = Milestone B; `ms_c` = Milestone C; `frp_dec` = Full-Rate Production or Full Deployment Decision; `other` = Other, as required
- Note: AAFDID's MCA overview: statutory requirements in the MCA tables may not be waived unless the relevant statute permits it.
- Note: Programs may combine pathways; for example, an MCA program may use the software pathway for its software (DoDI 5000.02, para 4.1.a).
- AAFDID page: https://www.waru.edu/aafdid/mca

## Lookup matrix: Milestone and Phase Information Requirements

● = applies to that program type. I = initial submission at that event; U = update. Read the program type column and the next-event column together. A row marked (DOT&E oversight only) also needs `dote_oversight` = yes; the record's Condition code is the full rule.

| Code | Requirement | MDAP | MAIS | II | III | MDD | MS A | CDD Val | Dev RFP Rel | MS B | MS C | FRP/FD | Other |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MCA-M01 | 10 U.S.C. 4251 MILESTONE A COMPLIANCE | ● |  |  |  |  | I |  |  |  |  |  |  |
| MCA-M02 | 10 U.S.C. 4252 MILESTONE B COMPLIANCE | ● |  |  |  |  |  |  |  | I |  |  |  |
| MCA-M03 | 10 U.S.C. 4253 MILESTONE C COMPLIANCE | ● |  |  |  |  |  |  |  |  | I |  |  |
| MCA-M04 | ACQUISITION APPROACH (Part of Acquisition Strategy) | ● |  | ● | ● |  | I |  | I | U | U | U |  |
| MCA-M05 | Acquisition Decision Memorandum (ADM) | ● |  | ● | ● | I | I |  | I | I | I | I | I |
| MCA-M06 | ACQUISITION PROGRAM BASELINE (APB) | ● |  | ● | ● |  |  |  | I | U | U | U | U |
| MCA-M07 | ACQUISITION STRATEGY | ● |  | ● | ● |  | I |  | I | U | U | U |  |
| MCA-M08 | Affordability Analysis | ● |  | ● | ● | I | U |  | U | U | U | U |  |
| MCA-M09 | ANALYSIS OF ALTERNATIVES (AoA) | ● |  | ● | ● |  | I |  | U |  | U |  | U |
| MCA-M10 | AoA Study Guidance and AoA Study Plan | ● |  | ● | ● | I |  |  |  |  |  |  |  |
| MCA-M11 | BANDWIDTH REQUIREMENTS REVIEW | ● |  | ● | ● |  |  |  | I | U | U |  |  |
| MCA-M12 | BENEFITS ANALYSIS AND DETERMINATION (Part of Acquisition Strategy) | ● |  | ● | ● |  | I |  | I | U | U |  |  |
| MCA-M13 | BUSINESS STRATEGY (Part of Acquisition Strategy) | ● |  | ● | ● |  | I |  | I | U | U | U |  |
| MCA-M14 | Capability Development Document (CDD) | ● |  | ● | ● |  | I | U | U |  | U |  | U |
| MCA-M15 | CLINGER-COHEN ACT (CCA) COMPLIANCE | ● |  | ● | ● |  | I |  |  | I | I | I | I |
| MCA-M16 | Concept of Operations/Operational Mode Summary/Mission Profile (CONOPS/OMS/MP) | ● |  | ● | ● |  | I |  | U |  | U |  |  |
| MCA-M17 | CONTRACT-TYPE DETERMINATION (Part of Acquisition Strategy) | ● |  |  |  |  |  |  | I | I | I |  |  |
| MCA-M18 | CONTRACTING STRATEGY (Part of Acquisition Strategy) | ● |  | ● | ● |  | I |  | I | U | U | U |  |
| MCA-M19 | COOPERATIVE OPPORTUNITIES (Part of Acquisition Strategy) | ● |  | ● | ● |  | I |  | I | U | U | U |  |
| MCA-M20 | CORE LOGISTICS DETERMINATION / CORE LOGISTICS AND SUSTAINING WORKLOADS ESTIMATE | ● |  | ● | ● |  |  |  | I | U | I |  |  |
| MCA-M21 | Cost Analysis Requirements Description (CARD) | ● |  |  |  |  | I |  | U | I | U | U | U |
| MCA-M22 | Critical Design Review (CDR) Assessment | ● |  |  |  |  |  |  |  |  |  |  | I |
| MCA-M23 | CYBERSECURITY STRATEGY | ● |  | ● | ● | I | U |  | U | U | U | U |  |
| MCA-M24 | Depot Source of Repair (DSOR) Determination | ● |  | ● | ● |  |  |  |  | U | U |  |  |
| MCA-M25 | Development RFP Release Cost Assessment | ● |  |  |  |  |  |  | I |  |  |  |  |
| MCA-M26 | DoD Component Cost Estimate | ● |  |  |  |  | I |  |  | I | I | I | I |
| MCA-M27 | DoD Component Cost Position | ● |  |  |  |  | I |  |  | I | I | I | I |
| MCA-M28 | DoD Component Live Fire Test and Evaluation (LFT&E) Report (DOT&E oversight only) | ● |  | ● | ● |  |  |  |  |  |  | I | I |
| MCA-M29 | DOT&E REPORT ON INITIAL OPERATIONAL TEST AND EVALUATION (IOT&E) (DOT&E oversight only) | ● |  | ● | ● |  |  |  |  |  |  | I |  |
| MCA-M30 | DT&E Program Assessment | ● |  |  |  |  |  |  | I | U | U |  | U |
| MCA-M31 | DT&E SUFFICIENCY ASSESSMENT | ● |  |  |  |  |  |  |  | I | I |  |  |
| MCA-M32 | Exit Criteria | ● |  | ● | ● |  | I |  | I | U | I |  |  |
| MCA-M33 | FREQUENCY ALLOCATION APPLICATION (DD FORM 1494) | ● |  | ● | ● |  | I |  |  | I | I |  |  |
| MCA-M34 | Full Funding Certification Memorandum | ● |  |  |  |  | I |  | I | I | I | I |  |
| MCA-M35 | GENERAL EQUIPMENT VALUATION (Part of Acquisition Strategy) | ● |  | ● | ● |  |  |  |  |  | I | U |  |
| MCA-M36 | INDEPENDENT COST ESTIMATE (ICE) | ● |  |  |  |  | I |  |  | I | I | I | I |
| MCA-M37 | INDEPENDENT LOGISTICS ASSESSMENT | ● |  |  |  |  |  |  |  | I | I | I | I |
| MCA-M38 | INDEPENDENT TECHNICAL RISK ASSESSMENT (ITRA) | ● |  |  |  |  |  |  |  | I |  | I | I |
| MCA-M39 | INDUSTRIAL BASE CAPABILITY CONSIDERATIONS (Part of Acquisition Strategy) | ● |  | ● | ● |  | I |  | I | U | U | U |  |
| MCA-M40 | Information Support Plan (ISP) | ● |  | ● | ● |  |  |  | I |  | U |  | U |
| MCA-M41 | Information Technology and National Security System Interoperability Certification | ● |  | ● | ● |  |  |  |  |  |  | I |  |
| MCA-M42 | Initial Capabilities Document (ICD) | ● |  | ● | ● | I |  |  |  |  |  |  |  |
| MCA-M43 | INTELLECTUAL PROPERTY (IP) STRATEGY (Part of Acquisition Strategy) | ● |  | ● | ● |  | I |  | I | U | U | U |  |
| MCA-M44 | Item Unique Identification Implementation Plan | ● |  | ● | ● |  | I |  | U | U | U |  |  |
| MCA-M45 | LFT&E REPORT | ● |  | ● | ● |  |  |  |  |  |  | I | I |
| MCA-M46 | Life-Cycle Mission Data Plan | ● |  | ● | ● |  | I |  | U | U | U | U |  |
| MCA-M47 | LIFE-CYCLE SUSTAINMENT PLAN | ● |  | ● | ● |  | I |  |  | U | U | U | U |
| MCA-M48 | LOW-RATE INITIAL PRODUCTION (LRIP) QUANTITY | ● |  | ● | ● |  |  |  | I | U |  |  |  |
| MCA-M49 | MARKET RESEARCH (Part of Acquisition Strategy) | ● |  | ● | ● | I | U |  | U |  |  |  |  |
| MCA-M50 | MILESTONE SUMMARY REPORT | ● |  |  |  |  | I |  |  | I | I |  |  |
| MCA-M51 | Mobile Electrical Power Systems (MEPS) | ● |  | ● | ● |  | I |  |  | U | U | U |  |
| MCA-M52 | MODULAR OPEN SYSTEMS APPROACH (MOSA) (Part of Acquisition Strategy) | ● |  | ● | ● |  | I |  | I | U | U | U |  |
| MCA-M53 | MULTI-YEAR PROCUREMENT (Part of Acquisition Strategy) | ● |  | ● | ● |  | I |  | I | U | U | U |  |
| MCA-M54 | NAVWAR Compliance Determination | ● |  | ● | ● |  | I |  |  | I | I |  |  |
| MCA-M55 | Operational Test Agency (OTA) Report of OT&E Results | ● |  | ● | ● |  |  |  |  |  |  | I | I |
| MCA-M56 | OPERATIONAL TEST PLAN (OTP) | ● | ● | ● | ● |  |  |  |  |  |  | I | I |
| MCA-M57 | PESHE AND NEPA/E.O. 12114 COMPLIANCE SCHEDULE | ● |  | ● | ● |  |  |  |  | I | U | U |  |
| MCA-M58 | POST IMPLEMENTATION REVIEW (PIR) | ● |  | ● | ● |  |  |  |  |  |  |  | I |
| MCA-M59 | PRELIMINARY DESIGN REVIEW (PDR) ASSESSMENT | ● |  |  |  |  |  |  |  | I |  |  |  |
| MCA-M60 | PRESERVATION AND STORAGE OF UNIQUE TOOLING PLAN | ● |  |  |  |  |  |  |  |  | I |  | U |
| MCA-M61 | PRODUCT SUPPORT (INCLUDING SUSTAINMENT, LOGISTICS, AND MAINTENANCE) (Part of Acquisition Strategy) | ● |  | ● | ● |  | I |  |  | U | U | U |  |
| MCA-M62 | PRODUCT SUPPORT STRATEGY (PSS) | ● |  | ● | ● |  | I |  | U | U | U | U | U |
| MCA-M63 | PROGRAM COST, FIELDING, AND PERFORMANCE GOALS | ● |  |  |  |  | I |  |  |  |  |  | U |
| MCA-M64 | Program DT&E Assessment | ● |  |  |  |  |  |  | I | U | U |  | U |
| MCA-M65 | Program Protection Plan (PPP) | ● |  | ● | ● |  | I |  |  | U | U | U | U |
| MCA-M66 | RELIABILITY AND MAINTAINABILITY (Part of Acquisition Strategy) | ● |  | ● |  |  | I |  | I | U | U | U |  |
| MCA-M67 | REPLACED SYSTEM SUSTAINMENT PLAN | ● |  |  |  |  | I |  |  | I |  |  |  |
| MCA-M68 | Request for Proposal (RFP) | ● |  | ● | ● |  | I |  | I |  | I | I |  |
| MCA-M69 | RISK MANAGEMENT (Part of Acquisition Strategy) | ● |  | ● | ● |  | I |  | I | U | U | U |  |
| MCA-M70 | Should Cost Target | ● |  | ● | ● |  | I |  | I | I | I | I |  |
| MCA-M71 | SMALL BUSINESS INNOVATION RESEARCH (SBIR)/SMALL BUSINESS TECHNOLOGY TRANSFER (STTR) PROGRAM TECHNOLOGIES (Part of Acquisition Strategy) | ● |  | ● | ● |  | I |  |  |  | I |  |  |
| MCA-M72 | Spectrum Supportability Risk Assessment (SSRA) | ● |  | ● | ● |  | I |  |  | I | I |  | I |
| MCA-M73 | SUSTAINMENT REVIEW | ● |  |  |  |  |  |  |  |  |  |  | I |
| MCA-M74 | Systems Engineering Plan (SEP) | ● | ● | ● | ● |  | I |  | U | U | U | U |  |
| MCA-M75 | TECHNOLOGY READINESS ASSESSMENT (TRA) | ● |  |  |  |  |  |  | I | U | I |  |  |
| MCA-M76 | Technology Targeting Risk Assessment | ● |  | ● | ● |  | I |  |  |  |  |  |  |
| MCA-M77 | TERMINATION LIABILITY ESTIMATE (Part of Acquisition Strategy) | ● |  |  |  |  | I |  | I | U | U | U |  |
| MCA-M78 | Test and Evaluation Master Plan (TEMP) | ● |  | ● | ● |  | I |  | U | U | U | U |  |
| MCA-M79 | Validated On-line Life- cycle Threat (VOLT) Report | ● |  | ● | ● | I | U |  | U |  | U | U |  |
| MCA-M80 | Waveform Analysis Application | ● |  | ● | ● |  |  |  |  | I | U | U | U |

## Milestone and Phase Information Requirements

### MCA-M01 · 10 U.S.C. 4251 MILESTONE A COMPLIANCE

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone A (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: 10 U.S.C. 4251 DoDI 5000.85
- AAFDID note: STATUTORY for MDAPs and major subprograms. By this table, the MDA does not have authority to delegate this requirement. 1. Before granting Milestone A approval for an MDAP or a major sub-program, the MDA must ensure that the program information is sufficient to warrant entry into TMRR; cost, schedule, technical, and performance tradeoffs do not overly constrain the future trade space; and plans to proceed into EMD are sound. 2. Additional statutory requirements include, but are not limited to, a written record of the decision, the Milestone Summary Report (see row later in this table), retention of Milestone A documentation, and congressional notification within 15 days. Refer to the statute for the complete and detailed listing of Milestone A statutory requirements.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M02 · 10 U.S.C. 4252 MILESTONE B COMPLIANCE

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone B (initial)
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: MDA
- Source: 10 U.S.C. 4252 10 U.S.C. 4402 DoDI 5000.85
- AAFDID note: STATUTORY for MDAPs and major subprograms before Milestone B approval. By this table, the MDA does not have authority to delegate this requirement. Before granting Milestone B approval for an MDAP or a major subprogram, the MDA must ensure that the program is affordable; program information warrants entry into EMD; the MilDep Secretary and the Chief of the armed force concur with trade-offs; and the program complies with the modular open system approach requirements provided in 10 U.S.C. 4402. Refer to the statute for the complete and detailed listing of Milestone B statutory requirements.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M03 · 10 U.S.C. 4253 MILESTONE C COMPLIANCE

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone C (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: 10 U.S.C. 4253 DoDI 5000.85
- AAFDID note: STATUTORY. Within 15 days of granting Milestone C approval for an MDAP, the MDA must provide the congressional defense committes (and, in the case of intelligence- related programs, the congressional intelligence committees) a brief Milestone C program summary report. This requirement is also addressed in the "Milestone Summary Report" row of this table. Refer to the statute for the complete and detailed listing of Milestone C reporting requirements.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M04 · ACQUISITION APPROACH (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory if `mca_program_type is one of {mdap, acat_ii}`, otherwise Regulatory. If that is unknown, the type depends on the answer. AAFDID TYPE: Statutory
- Approval: MDA
- Source: 10 U.S.C. 4211 15 U.S.C. 631, et seq. 10 U.S.C. 4820
- AAFDID note: STATUTORY for MDAPs and major systems. Describe the top-level business and technical management approach in sufficient detail to allow the MDA to assess (1) the viability of the approach; (2) the method of implementing laws and policies; and (3) program objectives. Provide a clear explanation of how the strategy is designed to be implemented within the available resources of time, funding, and management capacity. Discuss the tailoring that will address program requirements and constraints. Where appropriate, the strategy should consider the delivery of required capability in increments, each dependent on available, mature technology, and recognizing up front the need for future capability improvements. 10 U.S.C. 4211 explicitly requires the Acquisition Approach to address industrial base considerations in accordance with 10 U.S.C. 4820.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M05 · Acquisition Decision Memorandum (ADM)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Materiel Development Decision (initial); Milestone A (initial); Development RFP Release Decision (initial); Milestone B (initial); Milestone C (initial); Full-Rate Production or Full Deployment Decision (initial); Other, as required (initial)
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: MDA
- Source: DoDI 5000.85 10 U.S.C. 4251 10 U.S.C. 4252
- AAFDID note: Regulatory. Documents MDA decisions and direction. The approved AoA study guidance and study plan will be attached to the ADM. The ADM serves as the "written record" required by U.S. Code.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M06 · ACQUISITION PROGRAM BASELINE (APB)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Development RFP Release Decision (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update); Other, as required (update)
- Type by event: if `mca_program_type is one of {mdap}`, Statutory at Milestone B, Milestone C, Full-Rate Production or Full Deployment Decision, and Regulatory at its other events. Otherwise Regulatory. If that is unknown: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: MDA
- Source: 10 U.S.C. 4214 10 U.S.C. 4377
- AAFDID note: STATUTORY for MDAPs at Milestones B and C and the FRP decision; a Regulatory requirement at all other Program Type/Event combinations, including the required draft at Development RFP Release. For the APB, the draft due at RFP Release does not require CAE approval. The APB is not approved by the MDA until Milestone B. See the introductory text for the Acquisition Program Baselines Table and the Statutory Program Breach Definitions Table for reporting requirements at other than the identified decision points.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M07 · ACQUISITION STRATEGY

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory if `mca_program_type is one of {mdap, acat_ii}`, otherwise Regulatory. If that is unknown, the type depends on the answer. AAFDID TYPE: Regulatory, Statutory
- Approval: MDA
- Source: 10 U.S.C. 4211 DoDI 5000.85
- AAFDID note: STATUTORY for MDAPs and major systems (including AIS programs that exceed the dollar thresholds for a "major system," as identified in DoDI 5000.85, Appendix 3A); Regulatory for other programs. 10 U.S.C. 4211 provides a comprehensive/detailed list of required strategy content; required content may be extended with regulatory requirements. Major changes to the program planning reflected in the Acquisition Strategy require MDA approval. 1. If the MDA revises the strategy for an MDAP or major defense subprogram because of a significant or critical change to the cost of the program or system, or a significant change to the schedule or performance of the program or system, the MDA must notify the congressional defense committees consistent with the Exceptions, Waivers, and Alternative Management and Reporting Requirements Table. 2. The MDA must review and re-approve the strategy upon a significant change to the schedule or performance of the program (or system), or if there has been a significant or critical change to the cost of the program (or system). 3. The strategy may also be reviewed and approved at any other time considered relevant by the MDA. A summary of the Product Support Strategy in the Acquisition Strategy is a regulatory requirement for all programs at all milestones and the FRP decision. Many of the acquisition strategy information requirements have a respective entry in this Table.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M08 · Affordability Analysis

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Materiel Development Decision (initial); Milestone A (update); Development RFP Release Decision (update); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: MDA
- Source: DoDI 5000.85
- AAFDID note: Regulatory. Affordability analysis will be conducted prior to Milestone A (or Milestone B, if "B" is the initial milestone) and updated if program funding changes dictate a reassessment of affordability. The Affordability Analysis is used, in part, to support the development of programs goals pursuant to 10 U.S.C. 4271 and further described in DoDI 5000.85.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M09 · ANALYSIS OF ALTERNATIVES (AoA)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (update); Milestone C (update); Other, as required (update)
- Type by event: if `mca_program_type is one of {mdap}`, Statutory at Milestone A, Capability Development Document validation, Development RFP Release Decision, Milestone B, and Regulatory at its other events. Otherwise Regulatory. If that is unknown: Statutory and regulatory. AAFDID TYPE: Statutory
- Approval: MDA (DCAPE evaluates and assesses AoAs for all ACAT I programs)
- Source: 40 U.S.C. 11312 §811, P.L. 106-398 10 U.S.C. 4251 10 U.S.C. 4252 DoDD 5105.84
- AAFDID note: STATUTORY for MDAPs at Milestone A through Milestone B. The DoD Component is responsible for performing the AoA consistent with the study guidance developed by the Director, Cost Assessment and Program Evaluation (DCAPE) and the study plan approved by DCAPE. DoDD 5105.84 details the responsibility of DCAPE for AoAs. 10 U.S.C. 4251, as amended by Section 802 of the FY2025 NDAA, allows for the conduct of early experimentation with a combatant commander to satisfy the statutory requirement for an AoA.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M10 · AoA Study Guidance and AoA Study Plan

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Materiel Development Decision (initial)
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: DCAPE or DoD Component Equivalent
- Source: 10 U.S.C. 139a and 4251 §832, P.L. 116-92 DoDD 5105.84 DoDI 5000.85
- AAFDID note: Regulatory requirements to guide the AoA. AoA Study Guidance informs the preparation of the AoA Study Plan. DCAPE will develop and issue the AoA Study Guidance for all MDAPs. AoA Study Guidance must be provided to DoD Component(s) for development of the AoA Study Plan, which the DoD Components submit to DCAPE for approval.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M11 · BANDWIDTH REQUIREMENTS REVIEW

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Development RFP Release Decision (initial); Milestone B (update); Milestone C (update)
- Type: Statutory if `mca_program_type is one of {mdap, acat_ii}`, otherwise Regulatory. If that is unknown, the type depends on the answer. AAFDID TYPE: Regulatory, Statutory
- Approval: DoD CIO
- Source: §1047, P.L. 110- 417 This Table
- AAFDID note: STATUTORY for MDAPs and major weapon systems; Regulatory for all other programs. Bandwidth requirements data will be documented in the Information Support Plan (ISP). If the ISP is waived for a program, conformance with bandwidth review will be based on data provided in the Capability Development Document (CDD), consistent with the Net-Ready guidance in Enclosure C to Chairman of the Joint Chiefs of Staff Instruction (CJCSI) 5123.01I, Charter of The Joint Requirements Oversight Council and Implementation of the Joint Capabilities Integration and Development System.
- Changed since AAFDID (JCIDS disestablished): see 20-changes-since-aafdid.md, note jcids-2025.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M12 · BENEFITS ANALYSIS AND DETERMINATION (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (update); Milestone C (update)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: 15 U.S.C. 644(a- e) 15 U.S.C. 657q
- AAFDID note: STATUTORY; applies to bundled acquisitions only. Includes MARKET RESEARCH to determine whether consolidation of the requirements is necessary and justified. Required a Milestone C, if there was no Milestone B. 15 U.S.C. 632 defines a bundled contract as a contract that is entered into to meet requirements that are consolidated in a bundling of contract requirements. The term "bundling of contract requirements" means consolidating two or more procurement requirements for goods or services previously provided or performed under separate smaller contracts into a solicitation of offers for a single contract that is likely to be unsuitable for award to a small-business concern.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M13 · BUSINESS STRATEGY (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: 10 U.S.C. 4211
- AAFDID note: STATUTORY; the business strategy will describe the rationale for the contracting approach and how competition will be maintained at the system and subsystem levels throughout the program life cycle; the strategy will detail how contract incentives will be employed to support Department goals.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M14 · Capability Development Document (CDD)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Capability Development Document validation (update); Development RFP Release Decision (update); Milestone C (update); Other, as required (update)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: JROC, JCB, or Component Validation
- Source: CJCSI 5123.01I
- AAFDID note: Regulatory. A draft CDD is required at Milestone A; a validated CDD is required at the Development RFP Release Decision Point and informs Milestone B. If a requirements change is needed prior to Milestone C, the CDD will be updated and revalidated. An equivalent DoD Component-validated requirements document will satisfy the CDD requirement for certain information systems. For approval authorities, JROC is Joint Requirements Oversight Council; JCB is Joint Capabilities Board.
- Changed since AAFDID (JCIDS disestablished): see 20-changes-since-aafdid.md, note jcids-2025.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M15 · CLINGER-COHEN ACT (CCA) COMPLIANCE

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Milestone B (initial); Milestone C (initial); Full-Rate Production or Full Deployment Decision (initial); Other, as required (initial)
- Type: Statutory if `it_type is one of {it_system, embedded_it}`, otherwise Regulatory. If that is unknown, the type depends on the answer. AAFDID TYPE: Regulatory, Statutory
- Approval: MDA and Component CIO or designee
- Source: U.S.C. Title 40, Subtitle III, Chapters 111, 113, 115 §811, P.L. 106-398 DoDI 5000.82
- AAFDID note: STATUTORY for all programs that acquire information technology (IT); Regulatory for other programs. See DoDI 5000.82 for amplifying regulatory policy. A summary of required actions is in the CCA Compliance Table. The PM will report CCA compliance to the MDA and the Component CIO or designee. For IT within an MCA program employing an incremental development model, the program manager will report CCA compliance at each Milestone and/or Limited Deployment Decision Point for the IT.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M16 · Concept of Operations/Operational Mode Summary/Mission Profile (CONOPS/OMS/MP)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (update); Milestone C (update)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DoD Component
- Source: CJCSI 5123.01, CJCSI 3010.02E JP 5-0
- AAFDID note: Regulatory. The CONOPS/OMS/MP is a Component-approved document that is derived from and consistent with the validated/approved capability requirements document. The CONOPS/OMS/MP describes the operational tasks, events, durations, frequency, and environment in which the materiel solution is expected to perform each mission and each phase of the mission. The CONOPS/OMS/MP will be provided to the MDA at the specified decision events and normally provided to industry as part of the RFP.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M17 · CONTRACT-TYPE DETERMINATION (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Development RFP Release Decision (initial); Milestone B (initial); Milestone C (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: §818, P.L. 109- 364; §811, P.L. 112-239
- AAFDID note: STATUTORY. Satisfied when the MDA approves the Acquisition Strategy with specified contract types. Only required for MDAPs at Development RFP Release and Milestones B and C. The MDA for an MDAP may conditionally approve the contract type selected for a development program at the Development RFP Release Decision Point, and give final approval at the time of Milestone B approval. The development contract type must be consistent with the level of program risk and may be either a fixed price or cost type contract. If selecting a cost-type contract or a contract utilizing certain incentive provisions, the MDA must comply with the conditions and reporting requirements listed in the Exceptions, Waivers, and Alternative Management and Reporting Requirements Table. The DoD MAY NOT enter into cost-type contracts for production of an MDAP unless compliant with the conditions and notifications listed in the Exceptions, Waivers, and Alternative Management and Reporting Requirements Table.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M18 · CONTRACTING STRATEGY (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: 10 U.S.C. 4211 10 U.S.C. 3453 41 U.S.C. 3306(a) (1) and 3307(d)
- AAFDID note: STATUTORY; discuss (1) the planned contract type and how it relates to risk management in each acquisition phase; (2) whether risk management enables the use of fixed- price elements in subsequent contracts; (3) market research; and (4) small business participation. Include the following sub-elements: CONTRACT-TYPE DETERMINATION; TERMINATION LIABILITY ESTIMATE.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M19 · COOPERATIVE OPPORTUNITIES (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: 10 U.S.C. 4211 10 U.S.C. 2350a
- AAFDID note: STATUTORY. Due at the first program milestone review. The requirement to discuss opportunities for cooperative research and development will be satisfied via the International Involvement section in the Acquisition Strategy outline and will include consideration of foreign military sales. For programs responding to urgent needs, proven capabilities will be assessed during the COURSE OF ACTION ANALYSIS.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M20 · CORE LOGISTICS DETERMINATION / CORE LOGISTICS AND SUSTAINING WORKLOADS ESTIMATE

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Development RFP Release Decision (initial); Milestone B (update); Milestone C (initial)
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: MDA/DoD Component
- Source: 10 U.S.C. 2464 10 U.S.C. 4251 10 U.S.C. 4252 §801, P.L. 112-81 DoDIs 5000.91, 4151.20, and 4151.24
- AAFDID note: STATUTORY. Only the CORE LOGISTICS DETERMINATION is required at Milestone A. Required at Milestone C if there was no Milestone B. Documented in the PSS. By Milestone A, the PM with support of the DoD Component will document its determination of applicability of core depot-level maintenance and repair capability requirements in the PSS. For Milestone B, the PM with support of the DoD Component will attach the program's estimated requirements for maintenance, repair, and workloads to the PSS. By regulation, the program's maintenance planning will ensure that core depot-level maintenance and repair capabilities and capacity are established NLT 4 years after IOC. The PM will ensure that a depot source of repair designation is made NLT 90 days after the Critical Design Review. See the LCSP row, this table. Not required for AIS programs
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M21 · Cost Analysis Requirements Description (CARD)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone A (initial); Development RFP Release Decision (update); Milestone B (initial); Milestone C (update); Full-Rate Production or Full Deployment Decision (update); Other, as required (update)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DoD Component
- Source: DoDI 5000.73
- AAFDID note: Regulatory. Procedures are specified in DoDI 5000.73. DoDI 5000.73 provides CAPE the authority to assess the sufficiency of the CARD prior to DoD Component approval. The DoD Component, with CAPE concurrence, will determine the CARD requirements for ACAT II and below programs.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M22 · Critical Design Review (CDR) Assessment

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Other, as required (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: MDA
- Source: DoDI 5000.88
- AAFDID note: Regulatory. USD(R&E) will conduct CDR assessments for ACAT ID programs. Components will conduct assessments on ACAT IB/IC programs. The CDR and associated CDR assessment are conducted after MS B and prior to MS C.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M23 · CYBERSECURITY STRATEGY

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Materiel Development Decision (initial); Milestone A (update); Development RFP Release Decision (update); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: DoD CIO or Component CIO
- Source: 40 U.S.C. 11313 DoDI 8500.01 DoDI 5000.82 §811, P.L. 106-398
- AAFDID note: STATUTORY for mission essential and mission critical technology, and a regulatory requirement for all other technology, including national security systems. The CYBERSECURITY STRATEGY reflects both the program's long-term approach for, and implementation of, cybersecurity throughout the program lifecycle. See DoDI 8500.01, DoDI 8510.01, and DoDI 5000.82. The CYBERSECURITY STRATEGY is a stand-alone appendix to the Program Protection Plan (PPP). The approved CYBERSECURITY STRATEGY is initially due before Milestone A, and will be updated, as needed, in each lifecycle phase and prior to receiving an ATO. The DoD CIO is the approval authority for MCA ACAT ID programs; the Component CIO is the approval authority for all other ACATs / acquisition pathways. See the Major Capability Acquisition Pathway Integration with Risk Management Framework guidance published on the DoD CIO Library for more information.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M24 · Depot Source of Repair (DSOR) Determination

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone B (update); Milestone C (update)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: ASD(S) or designee
- Source: 10 U.S.C. Chapter 146 DoDI 4151.18 DoDI 4151.24 DoDI 5000.91
- AAFDID note: Regulatory. The Depot Source of Repair (DSOR) determination process applies to any program with an approved JCIDS capability requirements document when the APB is approved. Initial DSOR assignments are determined jointly between the Military Departments and the Office of the USD(A&S) for ACAT III and above programs. No later than 90 calendar days after the critical design review or equivalent, the designated authority will approve the DSOR Certification and Determination. The resulting DSOR assignments will be documented in the next update of the PSS, but no later than Milestone C or equivalent programmatic decision. 10 U.S.C Chapter 146 provides statutory language related to maintenance and repair activity.
- Changed since AAFDID (JCIDS disestablished): see 20-changes-since-aafdid.md, note jcids-2025.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M25 · Development RFP Release Cost Assessment

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Development RFP Release Decision (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: CAPE
- Source: DoDI 5000.73
- AAFDID note: Regulatory. Requirements and procedures for this assessment are specified in DoDI 5000.73.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M26 · DoD Component Cost Estimate

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone A (initial); Milestone B (initial); Milestone C (initial); Full-Rate Production or Full Deployment Decision (initial); Other, as required (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DoD Component
- Source: DoDI 5000.73
- AAFDID note: Regulatory. See the direction in DoDI 5000.73. The DoD Component will determine the cost estimating requirements for ACAT II and below programs.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M27 · DoD Component Cost Position

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone A (initial); Milestone B (initial); Milestone C (initial); Full-Rate Production or Full Deployment Decision (initial); Other, as required (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DoD Component
- Source: DoDI 5000.73
- AAFDID note: Regulatory. Mandatory for MDAPs; documented DoD Component Cost Position must be signed by the appropriate DoD Component Deputy Assistant Secretary for Cost and Economics (or Defense Agency equivalent) and include a date of record.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M28 · DoD Component Live Fire Test and Evaluation (LFT&E) Report

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below; when it is on the DOT&E oversight list.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii} AND dote_oversight = yes`
- When due: Full-Rate Production or Full Deployment Decision (initial); Other, as required (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: CAE
- Source: This table DoDI 5000.89
- AAFDID note: Regulatory. Programs on the Director, Operational Test and Evaluation (DOT&E) Oversight List for LFT&E oversight only; due upon completion of LFT&E.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M29 · DOT&E REPORT ON INITIAL OPERATIONAL TEST AND EVALUATION (IOT&E)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below; when it is on the DOT&E oversight list.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii} AND dote_oversight = yes`
- When due: Full-Rate Production or Full Deployment Decision (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: DOT&E
- Source: 10 U.S.C. 4171 10 U.S.C. 139 DoDI 5000.89
- AAFDID note: STATUTORY; required for DOT&E Oversight List programs only. The DOT&E publishes an online list of programs under operational test and evaluation (OT&E) and LFT&E oversight at https://osd.deps.mil/org/dote-extranet/SitePages/Home.aspx (requires login with a Common Access Card (CAC)). A final decision to proceed beyond Low-Rate Initial Production (LRIP) or beyond Limited Deployment may not be made until the DOT&E has submitted the IOT&E Report to the Secretary of Defense, and the congressional defense committees have received that report. If DoD decides to proceed to operational use of the program or to make procurement funds available for the program before the MDA's FRP decision, the DOT&E's report will be submitted as soon as practicable after the DoD decision to proceed.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M30 · DT&E Program Assessment

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Development RFP Release Decision (initial); Milestone B (update); Milestone C (update); Other, as required (update)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: USD(R&E) or designee for ACAT IB & IC programs on DT&E oversight
- Source: DoDI 5000.89
- AAFDID note: Regulatory: For ACAT IB/IC programs on the T&E oversight list for which USD(R&E) did not conduct a DT&E sufficiency assessment, the USD(R&E) will provide the MDA with a program assessment at the Development RFP Release Decision Point and MS B and C. This will be updated to support the Operational Test Readiness Review (OTRR) or as requested by the MDA or PM.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M31 · DT&E SUFFICIENCY ASSESSMENT

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone B (initial); Milestone C (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: USD(R&E) or designee for ACAT ID; Component DT&E Official for ACAT IB & IC programs
- Source: §838, P.L. 115-91 10 U.S.C. 133a 10 U.S.C. 4252 10 U.S.C. 4253 DoDD 5137.02 DoDI 5000.89
- AAFDID note: STATUTORY: USD(R&E) or designee will conduct the MS B and MS C DT&E sufficiency assessments for MDAPs for which the USD(A&S) is the MDA and report the DT&E sufficiency assessment determinations to the USD(A&S). The senior official within the Military Department, Defense Agency, or DoD Field Activity with responsibility for DT&E will conduct the MS B and MS C DT&E sufficiency assessments for MDAPs for which the MDA is the Service or Component Acquisition Executive. The DT&E Sufficiency Assessment will be part of the Milestone C program information.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M32 · Exit Criteria

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (update); Milestone C (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: MDA
- Source: This table
- AAFDID note: Regulatory. Exit criteria are specific events and accomplishments that must be achieved before a program can proceed to the designated acquisition phase covered by the criteria; documented in the ADM.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M33 · FREQUENCY ALLOCATION APPLICATION (DD FORM 1494)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Milestone B (initial); Milestone C (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: National Telecommunications and Information Administration (NTIA)
- Source: §104, P.L. 102- 538 47 U.S.C. 305, 901-904
- AAFDID note: STATUTORY for all systems/equipment that use the electromagnetic spectrum while operating in the United States and its possessions. The DD Form 1494, Application for Equipment Frequency Allocation, is available from https://www.esd.whs.mil/Directives/forms/dd1000_1499/DD1494/ . The Title 47 STATUTORY requirement for DoD milestone decision is satisfied when the NTIA has authorized national spectrum certification(s) for the program at Stage 1, 2, 3 or 4, as applicable, in response to submitted DD Form(s) 1494 by the program manager.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M34 · Full Funding Certification Memorandum

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (initial); Milestone C (initial); Full-Rate Production or Full Deployment Decision (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: MDA
- Source: DoDI 5000.73
- AAFDID note: Regulatory. See DoDI 5000.73 for details, including coordination requirements. The requirement at "Dev RFP Rel" reflects DoDI 5000.73 policy that requires a full funding certification statement to be included at the LRIP and FRP decisions.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M35 · GENERAL EQUIPMENT VALUATION (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone C (initial); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: P.L. 101-576, Statement of Federal Financial Accounting Standards 23 and P.L. 101-576, Statement of Federal Financial Accounting Standards 6
- AAFDID note: STATUTORY; a program description that identifies contract-deliverable equipment items to include weapon systems, non-weapon systems, and other deliverable items; includes plan(s) to ensure that all deliverable equipment requiring capitalization is serially identified and valued. Only required at Milestone C; updated as necessary for the FRP Decision. The capitalization thresholds are unit costs at or above $1 million for Air Force and Navy general fund assets, and unit costs at or above $250 thousand for all internal use software and for other equipment assets for all other general and working capital funds. Ensure all contracts and contract systems are compliant with Financial Improvement and Audit Readiness (FIAR) requirements.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M36 · INDEPENDENT COST ESTIMATE (ICE)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone A (initial); Milestone B (initial); Milestone C (initial); Full-Rate Production or Full Deployment Decision (initial); Other, as required (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: DCAPE
- Source: Chapter 222 of Title 10 U.S.C.
- AAFDID note: STATUTORY for MDAPs. DoDI 5000.73 provides detailed instructions.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M37 · INDEPENDENT LOGISTICS ASSESSMENT

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone B (initial); Milestone C (initial); Full-Rate Production or Full Deployment Decision (initial); Other, as required (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: IAW CAE-directed policy
- Source: 10 U.S.C. 4325 DoDI 5000.91
- AAFDID note: STATUTORY for weapon system MDAPs only. Recurs NLT every 5 years after IOC. DoDI 5000.91 and the Independent Logistics Assessment Guidebook provide additional detail. Must be completed prior to key acquisition decision points including Milestones B and C and the FRP Decision. Results of the assessment will be reported to the Assistant Secretary of Defense (Sustainment) via the OSD Acquisition Information Repository (AIR).
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M38 · INDEPENDENT TECHNICAL RISK ASSESSMENT (ITRA)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone B (initial); Full-Rate Production or Full Deployment Decision (initial); Other, as required (initial)
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: USD(R&E) or as designated
- Source: 10 U.S.C. 4272 10 U.S.C. 4251/4252/4253 DoDI 5000.85 DoDI 5000.88
- AAFDID note: STATUTORY. ITRAs will be conducted on all MDAPs prior to Milestone A approval as required by DoDI 5000.88. ITRAs are required by 10 U.S.C. 4272 for Milestone B approval, and any decision to enter into low-rate initial production or full rate production. ITRAs may also be conducted at the direction of the Secretary or Deputy Secretary. USD(R&E) will conduct and approve ITRAs for ACAT ID programs. Components will conduct ITRAs on ACAT IB/IC programs. USD(R&E) will determine ITRA approval authority for ACAT IB/IC programs. ITRAs inform the 10 U.S.C. 4251, 4252, and 4253 requirements. For programs for which an ITRA is conducted, a separate Technology Readiness Assessment (TRA) report is not required. Additional policy associated with ITRAs is included in DoDI 5000.88, and the Defense Acquisition University website provides informative support material.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M39 · INDUSTRIAL BASE CAPABILITY CONSIDERATIONS (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory if `mca_program_type is one of {mdap}`, otherwise Regulatory. If that is unknown, the type depends on the answer. AAFDID TYPE: Regulatory, Statutory
- Approval: MDA
- Source: 10 U.S.C. 4211 10 U.S.C. 4820 DoDI 5000.60
- AAFDID note: STATUTORY for MDAPs; Regulatory for others. Summarizes the results of the industrial base capabilities' analysis. The OSD Office of Industrial Base Policy hosts a number of resources providing detailed manufacturing and industrial base policy and guidance.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M40 · Information Support Plan (ISP)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Development RFP Release Decision (initial); Milestone C (update); Other, as required (update)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DoD Component or as delegated
- Source: DoDI 8330.01
- AAFDID note: Regulatory. Applicable to all IT, including NSS. A draft[^4] is due for Development RFP Release; approved at Milestone B. Unless waived, the plan is updated at the Critical Design Review. The ISP of record is due prior to Milestone C; an updated ISP of record may be required during O&S. Enter data on-line at https://gtg.csd.disa.mil/ (requires an account and login with CAC). DoDI 8320.02 and DoDI 8410.03 provide related policy for data sharing, IT services, and network management.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M41 · Information Technology and National Security System Interoperability Certification

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Full-Rate Production or Full Deployment Decision (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: JITC or DoD Component
- Source: DoDI 8330.01
- AAFDID note: Regulatory. Applicable to all IT, including NSS. Testing completed before or during OT&E. The Joint Interoperability Test Command (JITC) certifies interoperability of IT with joint, multinational, and/or interagency interoperability requirements. DoD Components certify all other IT. Certification must occur prior to deployment.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M42 · Initial Capabilities Document (ICD)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Materiel Development Decision (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: JROC, JCB, or Component Validation
- Source: CJCSI 5123.01I
- AAFDID note: Regulatory. The ICD is the fundamental requirements document establishing validated capability requirements; required for the MDD.
- Changed since AAFDID (JCIDS disestablished): see 20-changes-since-aafdid.md, note jcids-2025.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M43 · INTELLECTUAL PROPERTY (IP) STRATEGY (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory if `mca_program_type is one of {mdap, acat_ii}`, otherwise Regulatory. If that is unknown, the type depends on the answer. AAFDID TYPE: Regulatory, Statutory
- Approval: MDA
- Source: 10 U.S.C. 3771, 3772 and 3774 10 U.S.C. 4211 DoDI 5010.44
- AAFDID note: STATUTORY for major weapon systems and subsystems; Regulatory for other program types. The IP Strategy must be updated as appropriate to support and account for evolving IP considerations associated with the award and administration of all contracts throughout the program life cycle. Becomes part of the Product Support Strategy (PSS) during Operations and Support (O&S). Title 10, Chapter 275, provides statute regarding the management of proprietary data and data rights.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M44 · Item Unique Identification Implementation Plan

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (update); Milestone B (update); Milestone C (update)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: CAE or as delegated
- Source: DoDI 8320.04
- AAFDID note: Regulatory. Design considerations related to unique identification are included in the Systems Engineering Plan (SEP).
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M45 · LFT&E REPORT

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Full-Rate Production or Full Deployment Decision (initial); Other, as required (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: DOT&E
- Source: 10 U.S.C. 4172
- AAFDID note: STATUTORY. A covered system may not proceed beyond LRIP until realistic survivability testing of the system is completed and the report is submitted to the Secretary of Defense and the congressional defense committees. A major munition program or a missile program may not proceed beyond LRIP until realistic lethality testing of the program is completed and the report is submitted to the Secretary of Defense and the congressional defense committees. 10 U.S.C. 4172 defines "realistic survivability testing" and "realistic lethality testing".
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M46 · Life-Cycle Mission Data Plan

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (update); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory and regulatory. AAFDID TYPE: Statutory, Regulatory
- Approval: DoD Component
- Source: This table Sec. 811 PL 106- 398
- AAFDID note: Regulatory; only required if the system is dependent on Intelligence Mission Data. A draft[^4] update is due for Development RFP Release; approved at Milestone B.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M47 · LIFE-CYCLE SUSTAINMENT PLAN

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update); Other, as required (update)
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: USD(A&S) or designee, CAE or designee
- Source: 10 U.S.C. 4324; OMB Circular A- 94; DoDI 5000.91
- AAFDID note: STATUTORY: An approved Life Cycle Sustainment Plan (LCSP) is required for covered systems (i.e., MDAPs) at Milestone B IAW Section 4324 of Title 10 U.S.C. Regulatory: IAW DoDI 5000.91, an LCSP4 is also required at MS A, and an update is required for the RFP Release decision point. A tailored LCSP is required for non-covered systems, starting at Milestone A. USD(A&S), or as designated, will approve the LCSP for an ACAT ID program or special interest program. DoD component heads will approve LCSPs for ACAT IB, ACAT IC, or below programs unless delegated. DoDI 5000.91 establishes policy for the LCSP and identifies statutory requirements; guidance is available at www.waru.edu/tools/product-support-manager-psm- guidebook. While the Product Support Strategy (PSS) is also identified in this table, it is part of the LCSP.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M48 · LOW-RATE INITIAL PRODUCTION (LRIP) QUANTITY

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Development RFP Release Decision (initial); Milestone B (update)
- Type: Statutory if `mca_program_type is one of {mdap, acat_ii}`, otherwise Regulatory. If that is unknown, the type depends on the answer. AAFDID TYPE: Regulatory, Statutory
- Approval: MDA
- Source: 10 U.S.C. 4231 DoDI 5000.85
- AAFDID note: STATUTORY for MDAPs and ACAT II programs; Regulatory for other programs. A preliminary quantity is determined at the Development RFP Release Decision Point; the final LRIP quantity is determined at Milestone B. The LRIP quantity will be documented in the ADM. For programs on the DOT&E Oversight List, LRIP quantities must equal or exceed the numbers required for testing as identified in the approved Test and Evaluation Master Plan (TEMP). Additional compliance details are provided in the cited section of U.S.C.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M49 · MARKET RESEARCH (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Materiel Development Decision (initial); Milestone A (update); Development RFP Release Decision (update)
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: MDA
- Source: 10 U.S.C. 3453 41 U.S.C. 3306(a) (1) and 3307(d) DoDI 5000.85
- AAFDID note: STATUTORY. A stand-alone Regulatory requirement at MDD. STATUTORY updates (as part of the ACQUISITION STRATEGY) required at Milestone A and the Development RFP release point; not required thereafter. Conducted to reduce the duplication of existing technologies and products, and to understand potential materiel solutions, technology maturity, and potential sources, to assure maximum participation of small business concerns, and possible strategies to acquire them. For programs responding to urgent needs, included in the Course of Action Approach at the Development Milestone. Note: The cited sections of U.S.C. provide statutory direction.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M50 · MILESTONE SUMMARY REPORT

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone A (initial); Milestone B (initial); Milestone C (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA through the DAE to Congress
- Source: 10 U.S.C. 4251 10 U.S.C. 4252 10 U.S.C. 4253
- AAFDID note: STATUTORY for MDAPs. Report due NLT 15 days after milestone approval for all MDAPs and major subprograms of MDAPs. Required content and reporting procedures are described in the respective section of U.S. Code. The Milestone Summary Report satisfies the statutory requirement for "a written record of the milestone decision."
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M51 · Mobile Electrical Power Systems (MEPS)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: PM Responsibility
- Source: DoDI 4120.11
- AAFDID note: Regulatory. Applicable to all programs that require MEPS equipment. PMs will coordinate through their Service MEPS Office in accordance with DoDI 4120.11. DoDI 4120.11 establishes the principal policy associated with DoD MEPS management.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M52 · MODULAR OPEN SYSTEMS APPROACH (MOSA) (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory if `mca_program_type is one of {mdap}`, otherwise Regulatory. If that is unknown, the type depends on the answer. AAFDID TYPE: Regulatory, Statutory
- Approval: MDA
- Source: 10 U.S.C. 4401 10 U.S.C. 4402 DoDI 5000.85
- AAFDID note: STATUTORY for MDAPs; Regulatory for other programs. Describe how a MOSA will or will not be used to evolve system capability, improve interoperability, reduce cost or schedule, and refresh technology. Planning will be consistent with the discussion in DoDI 5000.85, Para. 3C.3.a.(5).
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M53 · MULTI-YEAR PROCUREMENT (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: 10 U.S.C. 3501 DoDI 5000.73
- AAFDID note: STATUTORY; when appropriate, include a summary discussion of multi-year procurement (further discussed in DoDI 5000.73).
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M54 · NAVWAR Compliance Determination

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Milestone B (initial); Milestone C (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: MDA
- Source: DoDI 4650.08
- AAFDID note: Regulatory. Applicable to all programs producing or using positioning, navigation, and timing (PNT) information. The MDA confirms that the program has complied with procedures identified in DoDI 4650.08, including planned testing and evaluation.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M55 · Operational Test Agency (OTA) Report of OT&E Results

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Full-Rate Production or Full Deployment Decision (initial); Other, as required (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: OTA
- Source: This table
- AAFDID note: Regulatory. Required earlier than the FRP decision if early operational assessments or operational testing are conducted.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M56 · OPERATIONAL TEST PLAN (OTP)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Full-Rate Production or Full Deployment Decision (initial); Other, as required (initial)
- Type: Statutory if `dote_oversight = yes`, otherwise Regulatory. If that is unknown: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: DOT&E or Component equivalent
- Source: 10 U.S.C. 4171 DoDI 5000.89
- AAFDID note: STATUTORY/Regulatory. An OTP, approved before the start of OT&E, is mandatory for all programs. Approval by DOT&E is a STATUTORY requirement for programs on the DOT&E Oversight list. DoD Component-equivalent approval is a Regulatory requirement for all other programs.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M57 · PESHE AND NEPA/E.O. 12114 COMPLIANCE SCHEDULE

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone B (initial); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA or designee
- Source: 42 U.S.C. 4321 42 U.S.C., Chapter 55 E.O. 12114
- AAFDID note: STATUTORY. The Programmatic Environment, Safety, and Occupational Health Evaluation (PESHE) and National Environmental Policy Act (NEPA) / Executive Order (E.O.) 12114 Compliance Schedule is approved by the MDA or designee. Related design considerations must be included in the SEP; related operations or sustainment considerations after Milestone C will be included in the PSS.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M58 · POST IMPLEMENTATION REVIEW (PIR)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Other, as required (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: Functional Sponsor
- Source: 40 U.S.C. 11313 DoDI 5000.82
- AAFDID note: STATUTORY. Responds to statute that requires Federal Agencies to compare actual program results with established performance objectives. The PIR is a process that aggregates information needed to successfully evaluate the degree to which a capability has been achieved. The preparation of the TEMP and the MDA's decision to proceed with FRP satisfy the requirement for weapons systems. DoD Components will plan, conduct, and document the required review for IT systems and NSS post IOC. Approval by the Functional Sponsor will require coordination with the Component CIO.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M59 · PRELIMINARY DESIGN REVIEW (PDR) ASSESSMENT

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone B (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: 10 U.S.C. 4252 DoDI 5000.88
- AAFDID note: STATUTORY. USD(R&E) will conduct and approve PDR assessments for ACAT ID programs. Components will conduct PDR assessments on ACAT IB/IC programs.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M60 · PRESERVATION AND STORAGE OF UNIQUE TOOLING PLAN

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone C (initial); Other, as required (update)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: §815, P.L. 110-417
- AAFDID note: STATUTORY. Part of the PSS. The MDA must approve the plan prior to Milestone C approval; updated only as necessary thereafter. The plan must identify any contract clauses, facilities, and funding required to preserve and to store the unique tooling associated with the production of the MDAP hardware through the end of the service life of the end item. See paragraph 4.11.g in DoDI 5000.91 for details; see also PSS row, this table.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M61 · PRODUCT SUPPORT (INCLUDING SUSTAINMENT, LOGISTICS, AND MAINTENANCE) (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: 10 U.S.C. 2464 10 U.S.C. 2466 10 U.S.C. 4211
- AAFDID note: STATUTORY. For MDAPS, major systems, and business systems, content requirements of an Acquisition Strategy will ensure that each strategy will: consider requirements related to product support, logistics, maintenance, and sustainment IAW 10 U.S.C. 2464 and 2466.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M62 · PRODUCT SUPPORT STRATEGY (PSS)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (update); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update); Other, as required (update)
- Type: Statutory if `mca_program_type is one of {mdap}`, otherwise Regulatory. If that is unknown, the type depends on the answer. AAFDID TYPE: Statutory, Regulatory
- Approval: USD(A&S) or designee, CAE or designee
- Source: 10 U.S.C 4324 OMB Circular A- 94 DoDI 5000.91
- AAFDID note: STATUTORY for MDAPs; regulatory for other program. A draft[^4] update is due for the Development RFP Release; approved at Milestone B. The PSS is part of the Life Cycle Sustainment Plan and satisfies the statutory product support strategy requirement of 10 U.S.C. 4324. USD(A&S), or designee, will approve the PSS for ACAT ID programs and USD(A&S)-designated business system or special interest programs. The CAE, or designee, will approve the PSS for an ACAT IB, or IC or below program. See DoDI 5000.91 for PSS details. The PSS has the following annexes: Core Logistics Analysis (row above); IP Strategy (row above); Preservation and Storage of Unique Tooling Plan (row above); Product Support Business Case Analysis (10 U.S.C. 4324 and DoDI 5000.91); Programmatic, Environment, Safety, and Occupational Health (ESOH) (PESHE) (row below); Replaced System sustainment Plan (row below); and System Disposal Plan (10 U.S.C. 4252, DoDI 4160.28, DoD 4160.21-M, DoD 4160.28-M and DoDI 5000.91).
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M63 · PROGRAM COST, FIELDING, AND PERFORMANCE GOALS

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone A (initial); Other, as required (update)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: 10 U.S.C. 4271 DoDI 5000.85
- AAFDID note: STATUTORY. The MDA must establish program cost, fielding, and performance goals (also called targets) before funds are obligated for technology development, systems development, or production of an MDAP. These goals will replace affordability goals and caps for MDAPs proceeding through Milestone A (or the initial milestone event) after October 1, 2017. * (Other) If following Milestone A, the estimated procurement unit cost for the program or the estimated date for IOC for the baseline description for the program exceeds the program cost or fielding targets established by the MDA, the MDA will re-assess the program and, if justified, increase the program cost target and/or increase the fielding target prior to the next milestone or production decision in consultation with OSD advisors. The new goals must be approved before the program can proceed through a milestone event.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M64 · Program DT&E Assessment

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Development RFP Release Decision (initial); Milestone B (update); Milestone C (update); Other, as required (update)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: USD(R&E) or designee for ACAT IB & IC programs on DT&E oversight
- Source: DoDI 5000.89
- AAFDID note: Regulatory: For ACAT IB/IC programs on the T&E oversight list for which USD(R&E) did not conduct a DT&E sufficiency assessment, the USD(R&E) will provide the MDA with a program assessment at the Development RFP Release Decision Point and at MSs B and C. The program assessment will be based on the completed DT&E and any operational T&E activities completed to date, and will address the adequacy of the program planning, the implications of testing results to date, and the risks to successfully meeting the goals of the remaining T&E events in the program. The assessment will be updated to support the Operational Test Readiness Review or as requested by the MDA or PM.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M65 · Program Protection Plan (PPP)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update); Other, as required (update)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: USD(R&E) for ACAT ID; CAE (or designee) for all other programs
- Source: DoDI 5200.39 DoDI 5200.44 DoDI 5000.83
- AAFDID note: Regulatory. After the Full Rate Production or Full Deployment decision, the PPP will transition to the PM responsible for system sustainment and disposal. The PPP includes appropriate appendixes or links to required information. For all programs under USD(A&S) oversight, the office of the USD(R&E) will be the approval authority for the PPP; for all other ACATs, the official designated by the DoD Component head will be the approval authority.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M66 · RELIABILITY AND MAINTAINABILITY (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs and ACAT II.
- Condition code: `mca_program_type is one of {mdap, acat_ii}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: 10 U.S.C. 4328 January 31, 2019 USD(A&S) Policy Memo, "Implementation of title 10, United States Code, section 2443 - Sustainment Factors in Weapon System Design."
- AAFDID note: STATUTORY; For MDAPs and Major Systems, the PM must, as part of the ACQUISITION STRATEGY: Include measurable requirements for engineering activities and design specifications for R&M for TMRR, EMD and Production solicitations; otherwise justify in writing the determination to exclude engineering activities and design specifications for reliability or maintainability from the solicitation. Indicate if sustainment factors, including R&M, are included in the process for source selection; Describe incentive fees and penalties (as appropriate) to incentivize achievement of design specification requirements for R&M in all EMD and Production solicitations and contracts. The MDA will notify the congressional defense committees upon entering into an EMD or Production contract that includes incentive fees or penalties.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M67 · REPLACED SYSTEM SUSTAINMENT PLAN

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone A (initial); Milestone B (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: DoD Component
- Source: 10 U.S.C. 4321
- AAFDID note: STATUTORY. May be submitted as early as Milestone A, but no later than Milestone B. Required when an MDAP replaces an existing system and the capability of the old system remains necessary and relevant during fielding of and transition to the new system. The plan must provide for the appropriate level of budgeting for sustainment of the old system, the schedule for developing and fielding the new system, and an analysis of the ability of the existing system to maintain mission capability against relevant threats. Is an annex to the PSS.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M68 · Request for Proposal (RFP)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone C (initial); Full-Rate Production or Full Deployment Decision (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: MDA is release authority
- Source: Federal Acquisition Regulation (FAR) Subpart 15.203
- AAFDID note: Regulatory. RFPs are issued as necessary; they include specifications, deliverable lists, and statement of work. See also Defense Federal Acquisition Regulation Supplement (DFARS) subpart 201.170 and Class Deviation 2019-O00010, dated August 20, 2019, for peer review requirements. When the DAE is the MDA, the peer review, as described in the Defense Federal Acquisition Regulation Supplement subpart 201.170, will be conducted and provide the basis for the PM's recommendation for RFP approval to the MDA. For acquisitions where government property will be provided to a contractor for the performance of a contract, a business case analysis must be performed, demonstrating it is in the government's best interest to provide government property, otherwise the contract could not be performed. In addition, the solicitation and ensuing contract must have the appropriate government property clause and mandatory clauses incorporated. ADDITIONAL SOURCES: FAR 45.102.b and DFARS 245.103-70.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M69 · RISK MANAGEMENT (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: 10 U.S.C. 4211 10 U.S.C. 4212
- AAFDID note: STATUTORY; include a comprehensive approach to risk management and mitigation. Planning will be consistent with the risk management and competitive prototyping discussions in DoDI 5000.85. If prototyping is not used, explain why.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M70 · Should Cost Target

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (initial); Milestone C (initial); Full-Rate Production or Full Deployment Decision (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: MDA
- Source: DoDI 5000.85
- AAFDID note: Regulatory. "Should cost" is a regulatory tool designed to proactively target cost reduction and drive productivity improvement into programs. Paragraph 3C.3.c.(2) in Appendix 3C of DoDI 5000.85 provides additional detail on "Should Cost."
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M71 · SMALL BUSINESS INNOVATION RESEARCH (SBIR)/SMALL BUSINESS TECHNOLOGY TRANSFER (STTR) PROGRAM TECHNOLOGIES (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Milestone C (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA/SAE Monitor
- Source: 15 U.S.C. 638
- AAFDID note: STATUTORY. PMs will establish goals for applying SBIR and STTR technologies in programs of record and incentivize primes to meet those goals. For contracts with a value at or above $100 million, PMs will establish goals for the transition of Phase III technologies in subcontracting plans and require primes to report the number and dollar amount of Phase III SBIR or STTR contracts. Not required at Milestone B.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M72 · Spectrum Supportability Risk Assessment (SSRA)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Milestone B (initial); Milestone C (initial); Other, as required (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Component CIO or designee
- Source: DoDI 4650.01
- AAFDID note: Regulatory. Applicable to all systems/equipment that use the electromagnetic spectrum in the United States and in other host nations. Due at milestone reviews and prior to requesting authorization to operate (for other than testing) in the United States or in host nations.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M73 · SUSTAINMENT REVIEW

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Other, as required (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: CAE
- Source: 10 U.S.C. 4323 DoDI 5000.91
- AAFDID note: STATUTORY. Component Secretaries will conduct a SUSTAINMENT REVIEW (SR) of each MDAP and major weapon system no less than every 5 years after declaration of a program's/ system's IOC and throughout the program life cycle to assess the product support strategy, performance, and O&S costs of the weapon system. The results of the SR will be documented in a memorandum by the relevant decision authority. The Secretary concerned will make the memorandum and supporting documentation for each SR available to the USD(A&S) within 30 days after the review is completed. The Secretary concerned will use availability and reliability thresholds and cost estimates as the basis for the circumstances that prompt such a review.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M74 · Systems Engineering Plan (SEP)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Milestone A (initial); Development RFP Release Decision (update); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: USD(R&E) (for ACAT ID) or MDA or designee
- Source: DoDI 5000.88
- AAFDID note: Regulatory. The MDA, or designee, is the approval authority for ACAT IB/IC SEPs, and below. The SEP approval authority for ACAT ID programs will be the USD(R&E) or delegated authority. The SEP will be approved before each release of acquisition Requests for Proposal (RFP) involving prototyping, technology maturation, risk reduction, engineering and manufacturing development, or production contracts. The SEP will be updated after contract award, if needed. A SEP outline and additional engineering guidance are available at https://www.cto.mil/sea/pg/ .
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M75 · TECHNOLOGY READINESS ASSESSMENT (TRA)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Development RFP Release Decision (initial); Milestone B (update); Milestone C (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: ITRA approval authority
- Source: 10 U.S.C. 4252 10 U.S.C. 4272
- AAFDID note: STATUTORY. For programs for which an ITRA is conducted, a Technology Readiness Assessment (TRA) report is not required. Programs will continue to assess and document the technology maturity of all critical technologies consistent with the TRA Guidance.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M76 · Technology Targeting Risk Assessment

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Validation by DIA or DoD Component
- Source: This Table DIA Directive 5000.200 DIA Instruction 5000.002
- AAFDID note: Regulatory. Prepared by the DoD Component and coordinated with the DoD Component intelligence analytical centers per DoDI O-5240.24. Forms the analytic foundation for counterintelligence assessments in the associated PPP. DIA will validate the report for ACAT ID; the DoD Component will be the validation authority for ACATs IB, IC, and below.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M77 · TERMINATION LIABILITY ESTIMATE (Part of Acquisition Strategy)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Milestone A (initial); Development RFP Release Decision (initial); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: MDA
- Source: §812, P.L. 112-239
- AAFDID note: STATUTORY. Only for MDAPs. Must be documented in the ACQUISITION STRATEGY for any contract for the development or production of an MDAP for which potential termination liability could reasonably be expected to exceed $100 million. Updates may therefore be required at other than the marked events. The estimate must include how such termination liability is likely to increase or decrease over the period of performance. The PM must consider the estimate before making recommendations on decisions to enter into or terminate such contracts.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M78 · Test and Evaluation Master Plan (TEMP)

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone A (initial); Development RFP Release Decision (update); Milestone B (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: See Notes.
- Source: DoDI 5000.89
- AAFDID note: Regulatory. A draft[^4] update is due for the Development RFP Release Decision Point; approved at Milestone B. DOT&E will co-approve the TEMP for DOT&E Oversight programs (DoDD 5141.02); the DoD Component OT authority will approve the OT portion of the TEMP for all other programs. The approval of the DT&E plan within the TEMP will be consistent with the procedures specified in the Test and Evaluation Instruction. The TEMP outline guidance for OT&E is located at https://osd.deps.mil/org/dote- extranet/SitePages/Home.aspx . The TEMP guidance for DT&E content is included in the Test and Evaluation Enterprise Guidebook .
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M79 · Validated On-line Life- cycle Threat (VOLT) Report

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Materiel Development Decision (initial); Milestone A (update); Development RFP Release Decision (update); Milestone C (update); Full-Rate Production or Full Deployment Decision (update)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DIA or DoD Component
- Source: This Table DIEM-A Standard 401
- AAFDID note: Regulatory. MDAPs require a unique system-specific VOLT Report to support capability development and PM assessments of mission needs and capability gaps against likely threat capabilities at IOC. The VOLT Report uses the bi-annual Defense Intelligence Threat Library Threat Modules as its analytic foundation. The threat modules provide the PM projections of technology and adversary capability trends for the next 20 years. VOLT Reports are required for all other programs unless waived by the MDA. In conjunction with the VOLT Report, the requirements sponsor and Component capability developer will collaboratively develop critical intelligence parameters in accordance with the JCIDS. Programs on the DOT&E Oversight List require a unique, system-specific VOLT Report, unless waived by both the MDA and the DOT&E. DoD Components produce a VOLT Report. DIA validates the VOLT Report for ACAT ID programs; the DoD Component validates the VOLT Report for ACAT IB and IC programs and below.
- Changed since AAFDID (JCIDS disestablished): see 20-changes-since-aafdid.md, note jcids-2025.
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

### MCA-M80 · Waveform Analysis Application

- Pathway: MCA (Major Capability Acquisition). Table: Milestone and Phase Information Requirements.
- Status when the condition holds: Required.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Milestone B (initial); Milestone C (update); Full-Rate Production or Full Deployment Decision (update); Other, as required (update)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DoD CIO
- Source: DoDI 4630.09
- AAFDID note: Regulatory. Application to the DoD CIO for approval of the development or modification of waveforms. Required at Milestone B, C, FRP, and any time post FRP if a waveform is added or modified. Table Notes: ● 1. A dot ( ) in a cell indicates the specific applicability of the requirement to program type and life-cycle event, and represents the initial submission requirement. Moving right across a row, a checkmark ü ( ) indicates the requirement for updated information. 2. All of the "Life-Cycle Events" will not necessarily apply to all "Program Types." 3. Unless otherwise specified, when discussed in DoDI 5000.85, documentation for identified events will be submitted no later than 45 calendar days before the planned review. 4. Requires a PM- and PEO-approved draft. 5. Information requirements that have been finalized and approved by the responsible authority in support of the Development RFP Release Decision Point do not have to be re- submitted prior to Milestone B unless changes have occurred. In that case, updated documents will be provided
- Page: https://www.waru.edu/aafdid/Milestone-and-Phase-Information-Requirements

## Recurring Program Reports

### MCA-R01 · Defense Acquisition Executive Summary (DAES)

- Pathway: MCA (Major Capability Acquisition). Table: Recurring Program Reports.
- Status when the condition holds: Required (recurring).
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: For MDAPs, quarterly after initial Modernized Selected Acquisition Report (MSAR) submission. Active programs that are 75 percent or more delivered through the production phase (or 75 percent expended if RDT&E only) will submit only a Unit Cost Reporting DAES pursuant to 10 U.S.C. 4371, 4372, 4373, 4374, and 4375. For MDAPs, the DAES reporting requirement ceases after a termination MSAR is submitted (90 percent of items delivered or 90 percent of funds are expended).
- Type: Regulatory. AAFDID TYPE: Regulatory
- Procedure: Program Manager
- Source: DoDI 5000.85
- AAFDID note: Regulatory. Programs are required to begin input of required data into Defense Acquisition Visibility Environment (DAVE) and the Acquisition Information Repository (AIR) upon submission of the Program Objective Memorandum (POM) or Budget Estimate Submission (BES) that first identifies the program.
- Page: https://www.waru.edu/aafdid/Recurring-Reporting-Requirements

### MCA-R02 · MODERNIZED SELECTED ACQUISITION REPORT (MSAR)

- Pathway: MCA (Major Capability Acquisition). Table: Recurring Program Reports.
- Status when the condition holds: Required (recurring).
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Program initiation (normally Milestone B except for some ship programs) or MDAP designation. Annually (as of December) for all programs and quarterly (as of March, June, and September) on an exception basis when there is: 1. A 6-month or more schedule slip in the current estimate since the prior MSAR; or 2. A unit cost increase of 15 percent or more to the current APB objective or 30 percent or more to the original APB objective. MSAR reporting requirement ceases after 90 percent of items are delivered or 90 percent of planned expenditures under the program or subprogram have been made.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: Submitted by PM to CAE, USD(A&S) Submitted by USD(A&S) to Congress
- Source: 10 U.S.C. 4351 - 4355 10 U.S.C. 4371 - 4375 10 U.S.C. 4201 10 U.S.C. 4202 10 U.S.C. 4204
- AAFDID note: STATUTORY. Provides the status of total program cost, schedule, and performance to Congress; provides program unit cost and unit cost breach information for a specific program. The first MSAR after the MDA's 10 U.S.C. 4252 CERTIFICATION AND DETERMINATION (a row in the Milestone and Phase Information Requirements Table) will include the certification and determination. For each MDAP that receives Milestone B approval after January 1, 2019, include a brief summary description of the key elements of the modular open systems approach or, if a modular open systems approach was not used, the rationale for not using such an approach. Every MSAR must include certification by the Secretary of the Military Department and the Chief of the armed force that program requirements are stable and funding is adequate to meet program cost, schedule, and performance objectives, and the Secretary and Chief must identify and report in the MSAR any increased program risk since the last report.
- Page: https://www.waru.edu/aafdid/Recurring-Reporting-Requirements

### MCA-R03 · UNIT COST REPORT (UCR)

- Pathway: MCA (Major Capability Acquisition). Table: Recurring Program Reports.
- Status when the condition holds: Required (recurring).
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Quarterly after initial MSAR submission. Unit Cost Reporting ceases after a termination MSAR is submitted (90 percent of items delivered or 90 percent of funds are expended).
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: PM; CAE, USD(A&S) (see Note, this row)
- Source: 10 U.S.C. 4371 - 4375
- AAFDID note: STATUTORY. Reported via the DAES submission process. The PM provides the report quarterly to USD(A&S) for the 3 quarters excluding the quarter with the annual MSAR submission. The USD(A&S) provides the report to Congress annually (included in MSAR submission).
- Page: https://www.waru.edu/aafdid/Recurring-Reporting-Requirements

## Exceptions, Waivers, and Alternative Management and Reporting Requirements

### MCA-X01 · ALTERNATE LFT&E PLAN

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs, ACAT II and ACAT III and below; when it is on the DOT&E oversight list.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii} AND dote_oversight = yes`
- When due: A DoD Component- approved final draft plan is due 45 calendar days prior to the Development RFP Release decision. The final plan is required at Milestone B or as soon as practicable after program initiation.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: PM to DOT&E
- Source: 10 U.S.C. 4172
- AAFDID note: STATUTORY. Only required for programs on the DOT&E oversight list for LFT&E with or requesting a waiver from full-up, system-level testing.
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X02 · CONGRESSIONAL NOTIFICATION OF CONDUCTING DT&E WITHOUT AN APPROVED TEMP

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Notification is required not later than 30 days after any decision is made for a lead DT&E Organization to conduct any developmental
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: PM to USD(A&S) to Congress
- Source: §904, P.L. 112-239
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X03 · CONGRESSIONAL NOTIFICATION OF CORE LOGISTICS COMMERCIAL ITEM EXCEPTION

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Due upon determination that the system or equipment is a commercial item.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: DAE to Congress
- Source: 10 U.S.C. 2464
- AAFDID note: STATUTORY. The commercial item exception notice must include the justification for the determination.
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X04 · CONGRESSIONAL NOTIFICATION OF CRITICAL COST BREACH

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Due within 45 calendar days of a Program Deviation Report
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: Service Secretary to Congress
- Source: 10 U.S.C. 4371 - 4377
- AAFDID note: STATUTORY.
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X05 · CONGRESSIONAL NOTIFICATION OF INCLUDING INCENTIVE FEES OR PENALTIES IN CONTRACTS

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs and ACAT II.
- Condition code: `mca_program_type is one of {mdap, acat_ii}`
- When due: Notification required upon entering into an EMD or Production contract that includes incentive fees or penalties, based on the achievement of reliability and
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: MDA to Congress; Copy USD(A&S), USD(R&E)
- Source: 10 U.S.C. 4328
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X06 · CONGRESSIONAL NOTIFICATION OF MDA REVISION OF THE ACQUISITION STRATEGY

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs and ACAT II.
- Condition code: `mca_program_type is one of {mdap, acat_ii}`
- When due: Notification reports an MDA revision to the acquisition strategy to the congressional defense committees when the program has experienced: (1) a significant change to the cost of the program or system; (2) a critical change to the cost of the program or system; (3) a significant change to the schedule of the program or system; or (4) a significant change to the performance of the program or system.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: MDA to Congress (copy DAE)
- Source: 10 U.S.C. 4211
- AAFDID note: STATUTORY. Each level of change for dollars is defined in section 4211 with a cross reference to section 4371. A significant change in schedule is defined as a delay greater than six months. A significant change in performance is not defined in statute.
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X07 · CONGRESSIONAL NOTIFICATION OF MDAP SUBPROGRAM DESIGNATION(S)

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Due not less than 30 calendar days before approval of a subprogram APB.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: MDA to Congress (copy DAE)
- Source: 10 U.S.C. 4203
- AAFDID note: STATUTORY. Reports the DAE's determination that (1) different categories of end items in an MDAP, or (2) delivery increments or blocks of an MDAP warrant separate acquisition reporting and will be designated Major Subprograms. The APB Table provides additional policy regarding subprograms.
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X08 · CONGRESSIONAL NOTIFICATION OF PRESERVATION AND STORAGE OF UNIQUE PRODUCTION TOOLING WAIVER

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Due before Milestone C or at any time before the end of the item's service life if the Secretary determines the waiver is in the best interest of the DoD.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: DAE to Congress
- Source: §815, P.L. 110-417
- AAFDID note: STATUTORY. Based on the Secretary's written determination that such a waiver is in the best interest of the DoD.
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X09 · CONGRESSIONAL NOTIFICATION OF SIGNIFICANT COST BREACH

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Due within 45 calendar days of a Program Deviation Report
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: Service Secretary to Congress
- Source: 10 U.S.C. 4371-4375
- AAFDID note: STATUTORY. Due within 45 calendar days of a Program Deviation Report. Reporting under Chapter 325-Cost Growth-Unit Cost Reports (Nunn-McCurdy) does not apply if a program has received a limited reporting waiver under 10 U.S.C. 4351, subsection (h).
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X10 · CONGRESSIONAL NOTIFICATION OF WAIVER OF PROHIBITION ON USING COVERED TELECOMMUNICATIONS EQUIPMENT OR SERVICES FOR NUCLEAR COMMAND, CONTROL, AND COMMUNICATIONS SYSTEMS

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Required when the Secretary of Defense waives the prohibitions described in and pursuant to §1656 of P.L. 115- 912. This waiver authority is only delegable to the Deputy Secretary of Defense or the co-chairs of the Council on Oversight of the National Leadership Command, Control, and Communications System. The Secretary may only waive the prohibition for a single, one-year period.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: Agency head to Congress; Copy to USD(A&S), USD(R&E), DoD CIO
- Source: §1656, P.L. 115-91 FAR 4.2102 FAR 4.2104
- AAFDID note: The cited section of the law fully details the prohibition and the limited waiver authority of the Secretary.
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X11 · CONGRESSIONAL NOTIFICATION OF WAIVER OF PROHIBITIONS ON CERTAIN TELECOMMUNICATIONS AND VIDEO SURVEILLANCE SERVICES OR EQUIPMENT

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Required when the head of executive agency waives the prohibitions described in and pursuant to §889 of P.L. 115-232.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: Agency head to Congress; Copy to USD(A&S), USD(R&E), DoD CIO
- Source: §889, P.L. 115-232 DFARS Subpart 204.2100
- AAFDID note: The cited section of the law fully details the prohibition as well as the condition for the waivers.
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X12 · COST-TYPE DEVELOPMENT CONTRACT DETERMINATION

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Due at the Development RFP Release Decision Point upon MDA conditional approval of a cost type contract selected for a development program; due at Milestone B if the contract type changes from fixed price to a cost type contract.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: MDA Written Determination
- Source: §818, P.L. 109-364
- AAFDID note: STATUTORY. The MDA may authorize the use of a cost-type contract for a development program only upon a written determination that: (1) the program is so complex and technically challenging that it would not be practicable to reduce program risk to a level that would permit the use of a fixed-price contract; and (2) the complexity and technical challenge of the program are not the result of a failure to meet the requirements of 10 U.S.C. 4252. The MDA's written determination will include an explanation of the level of program risk, and, if the MDA determines that the program risk is high, the steps that have been taken to reduce program risk and the reasons for proceeding with Milestone B approval despite the high level of program risk. In considering program risk to determine whether a cost or fixed price engineering and manufacturing development contract meets the statutory requirement, the MDA will consider the following: the firmness of the capability requirements and maturity of the technology required; the experience level of potential offerors; and the capacity of industry to absorb potential overruns and the business case for industry to do so.
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X13 · COST-TYPE PRODUCTION CONTRACT EXCEPTION CERTIFICATION

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Applicable to contracts for the production of MDAPs: entered into, on, or after October 1, 2014, and for which the USD(A&S) has granted an exception to the prohibition against using a cost-type contract for MDAP production.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: USD(A&S) to Congress
- Source: §811, P.L. 112- 239
- AAFDID note: STATUTORY. The USD(A&S) may only grant the exception: (1) in the case of a particular cost-type contract if the USD(A&S) provides written certification to the congressional defense committees that a cost-type contract is needed to provide a required capability in a timely and cost-effective manner; (2) the USD(A&S) takes affirmative steps to make sure that the use of cost-type pricing is limited to only those line items or portions of the contract where such pricing is needed to achieve the purposes of the exception; and, (3) an explanation of the steps identified under clause (2), accompanies the written certification under clause (1).
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X14 · DT&E EXCEPTION REPORTING

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Case 1: When an MDAP proceeds with implementing a TEMP that includes a developmental test plan disapproved by the Director, DT&E (D(DT&E)). Case 2: When an MDAP proceeds to IOT&E following an assessment by the D(DT&E) that the program is not ready for operational testing.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: PM to USD(R&E) to Congress
- Source: §904, P.L. 112-239
- AAFDID note: STATUTORY The report due for Case 1 must include a description of the specific aspects of the DT&E plan determined to be inadequate; an explanation of why the program disregarded the DASD(DT&E)'s recommendations; and identification of the steps taken to address the concerns of the DASD(DT&E). The report due for Case 2 must include an explanation of why the program proceeded to IOT&E despite the DASD(DT&E) findings; a description of the aspects of the TEMP that had to be set aside to enable the program to proceed to IOT&E; a description of how the program addressed the specific areas of concern raised in the assessment of operational test readiness; and a statement of whether IOT&E identified any significant shortcomings in the program. The USD(R&E) will compile all such exception reports and annually, not later than 60 days after the end of each fiscal year through 2018, submit a report on each case to the congressional defense committees. The D(DT&E) replaced the DASD(DT&E) during the OSD re-organization pursuant to Section 901 of P.L. 114-328.
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X15 · LEAD SYSTEM INTEGRATOR EXCEPTION CERTIFICATION

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs and ACAT II.
- Condition code: `mca_program_type is one of {mdap, acat_ii}`
- When due: Due if the MDA grants an exception.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: DAE to Congress
- Source: 10 U.S.C. 4292
- AAFDID note: STATUTORY for MDAPs, ACAT II programs, and any AIS program that exceeds the dollar values for a major system as identified in Table 1 in DoDI 5000.85, Appendix 3A. Satisfies the statutory restrictions applicable to exceptional use of a lead systems integrator.
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X16 · LFT&E WAIVER FROM FULL-UP, SYSTEM-LEVEL TESTING

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs, ACAT II and ACAT III and below; when it is on the DOT&E oversight list.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii} AND dote_oversight = yes`
- When due: Due at Milestone B or as soon as practicable after program initiation.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: DAE to Congress
- Source: 10 U.S.C. 4172
- AAFDID note: STATUTORY. Only required for programs on the DOT&E Oversight List for LFT&E that are requesting a waiver from full-up, system-level testing.
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X17 · Management of Joint DoD and Director of National Intelligence (DNI) Programs

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: When the DoD participates in a National Intelligence Program acquisition that is wholly or in the majority funded by the DNI.
- Type: Regulatory. AAFDID TYPE: Regulatory
- Procedure: None
- Source: MoA.
- AAFDID note: Joint DoD and DNI oversight of wholly and majority National Intelligence Program-funded acquisition programs will be conducted in accordance with Intelligence Community Policy Guidance 801.1 and the Memorandum of Agreement (MoA) between the DNI and the Secretary of Defense.
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X18 · MDA RESPONSE TO A CONGRESSIONAL MILESTONE APPROVAL INQUIRY

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Due upon congressional inquiry.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: MDA to Congress (copy DAE)
- Source: 10 U.S.C. sections 4251, 4252, and 4153
- AAFDID note: STATUTORY for MDAPs after Milestone A, B, or C approval, or for major subprograms of MDAPs after Milestone A approval. A response to an inquiry must include the independent cost and schedule estimates and the independent technical risk assessment. A response must also include the following milestone-specific information: After Milestone A, an explanation of the basis for the "4251 WRITTEN DETERMINATION" and a copy of the determination, further information, or underlying documentation for the information in the "MILESTONE SUMMARY REPORT." After Milestone B, an explanation of the basis for the "4252 CERTIFICATION AND DETERMINATION" or further information or underlying documentation for the information in the "MILESTONE SUMMARY REPORT." DoD will submit the additional information in unclassified form, but may include a classified annex. After Milestone C, further information or underlying documentation for the information in the "MILESTONE SUMMARY REPORT."
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X19 · NUNN-MCCURDY ASSESSMENT AND CERTIFICATION

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: When a Service Secretary has reported an increase in cost that equals or exceeds the critical cost growth threshold.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: USD(A&S)
- Source: 10 U.S.C. 4376-4377
- AAFDID note: STATUTORY. The remedial actions required when a program or subprogram experiences critical cost growth. 10 U.S.C. 4376 identifies the required elements of the certification. 10 U.S.C. 4377 identifies required actions if the deficient program is not terminated.
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X20 · Program Deviation Report

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Due within 30 business days of occurrence of the deviation. Initial MDA notification is due immediately upon becoming aware of an impending deviation.
- Type: Regulatory. AAFDID TYPE: Regulatory
- Procedure: PM to MDA
- Source: Introductory text to the Acquisition Program Baselines Table, and the Statutory Program Breach Definitions Table
- AAFDID note: Regulatory. Management details are provided in the MCA AAFDID tables identified as the source of the requirement.
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X21 · ROOT CAUSE ANALYSIS

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: A root cause analysis is an essential element in the procedures to avoid the statutorily presumed termination of an MDAP (or designated subprogram) that experiences a program acquisition unity cost or procurement until cost increase equal to or greater than the critical cost
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: SecDef, D, CAPE, in Consultation with the JROC
- Source: 10 U.S.C. 4273 10 U.S.C. 4371-4377
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

### MCA-X22 · SURVIVABILITY AND LIVE FIRE TESTING STATUS REPORT

- Pathway: MCA (Major Capability Acquisition). Table: Exceptions, Waivers, and Alternative Management and Reporting Requirements.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs, ACAT II and ACAT III and below; when it is on the DOT&E oversight list.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii} AND dote_oversight = yes`
- When due: Due as soon as practicable after a decision to proceed to operational use or to make procurement funds available for a covered system is made prior to Milestone C approval.
- Type: Statutory. AAFDID TYPE: Statutory
- Procedure: DOT&E to Congress
- Source: 10 U.S.C. 4172
- AAFDID note: STATUTORY. DOT&E LFT&E Oversight programs only, including those that respond to urgent needs. Program also requires the LFT&E Report (see LFT&E Report row in the Milestone and Phase Information Requirements Table).
- Page: https://www.waru.edu/aafdid/Exceptions-Waivers-and-Alternative-Requirements

## Clinger-Cohen Act Compliance

### MCA-C01 · CCA action 1: Determine that the acquisition supports core, priority functions of the DoD.

- Pathway: MCA (Major Capability Acquisition). Table: Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: IT systems, including national security systems. Presumed satisfied for weapon systems with embedded IT and for command and control systems that are not themselves IT (AAFDID footnote 3).
- Condition code: `it_type = it_system`
- When due: Report compliance at the events in the CLINGER-COHEN ACT (CCA) COMPLIANCE row of the milestone table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: ICD, Information Systems (IS) ICD, or urgent need requirements documents.
- Footnote: These requirements are presumed to be satisfied for weapons systems with embedded IT and for command and control systems that are not themselves IT systems.
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's CCA table has no TYPE column.
- Changed since AAFDID (JCIDS disestablished): see 20-changes-since-aafdid.md, note jcids-2025.
- Page: https://www.waru.edu/aafdid/CCA-Compliance

### MCA-C02 · CCA action 2: Establish outcome-based performance measures linked to strategic goals.

- Pathway: MCA (Major Capability Acquisition). Table: Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: IT systems, including national security systems. Presumed satisfied for weapon systems with embedded IT and for command and control systems that are not themselves IT (AAFDID footnote 3).
- Condition code: `it_type = it_system`
- When due: Report compliance at the events in the CLINGER-COHEN ACT (CCA) COMPLIANCE row of the milestone table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: ICD, IS ICD, CDD, AoA, APB.
- Footnote: These requirements are presumed to be satisfied for weapons systems with embedded IT and for command and control systems that are not themselves IT systems.
- Footnote: These actions are also required to comply with section 811 of Pub. L. 106-398.
- Footnote: The APB and TEMP may be submitted in draft to expedite program assessment.
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's CCA table has no TYPE column.
- Changed since AAFDID (JCIDS disestablished): see 20-changes-since-aafdid.md, note jcids-2025.
- Page: https://www.waru.edu/aafdid/CCA-Compliance

### MCA-C03 · CCA action 3: Redesign the processes that the system supports to reduce costs, improve effectiveness and maximize the use of commercial off-the-shelf technology.

- Pathway: MCA (Major Capability Acquisition). Table: Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: IT systems, including national security systems. Presumed satisfied for weapon systems with embedded IT and for command and control systems that are not themselves IT (AAFDID footnote 3).
- Condition code: `it_type = it_system`
- When due: Report compliance at the events in the CLINGER-COHEN ACT (CCA) COMPLIANCE row of the milestone table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: ICD, IS ICD, Concept of Operations, AoA, Business Process Reengineering.
- Footnote: These requirements are presumed to be satisfied for weapons systems with embedded IT and for command and control systems that are not themselves IT systems.
- Footnote: These actions are also required to comply with section 811 of Pub. L. 106-398.
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's CCA table has no TYPE column.
- Changed since AAFDID (JCIDS disestablished): see 20-changes-since-aafdid.md, note jcids-2025.
- Page: https://www.waru.edu/aafdid/CCA-Compliance

### MCA-C04 · CCA action 4: Determine that no private sector or government source can better support the function.

- Pathway: MCA (Major Capability Acquisition). Table: Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: Programs that acquire IT, including national security systems and IT embedded in weapon systems.
- Condition code: `it_type is one of {it_system, embedded_it}`
- When due: Report compliance at the events in the CLINGER-COHEN ACT (CCA) COMPLIANCE row of the milestone table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: Acquisition Strategy, AoA.
- Footnote: These actions are also required to comply with section 811 of Pub. L. 106-398.
- Footnote: For national security systems, these requirements apply to the extent practicable (40 U.S.C. 11103).
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/CCA-Compliance

### MCA-C05 · CCA action 5: Conduct an analysis of alternatives.

- Pathway: MCA (Major Capability Acquisition). Table: Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: Programs that acquire IT, including national security systems and IT embedded in weapon systems.
- Condition code: `it_type is one of {it_system, embedded_it}`
- When due: Report compliance at the events in the CLINGER-COHEN ACT (CCA) COMPLIANCE row of the milestone table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: AoA.
- Footnote: These actions are also required to comply with section 811 of Pub. L. 106-398.
- Footnote: For national security systems, these requirements apply to the extent practicable (40 U.S.C. 11103).
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/CCA-Compliance

### MCA-C06 · CCA action 6: Conduct an economic analysis that includes a calculation of the return on investment; or for non-AIS programs, conduct a life-cycle cost estimate.

- Pathway: MCA (Major Capability Acquisition). Table: Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: Programs that acquire IT, including national security systems and IT embedded in weapon systems.
- Condition code: `it_type is one of {it_system, embedded_it}`
- When due: Report compliance at the events in the CLINGER-COHEN ACT (CCA) COMPLIANCE row of the milestone table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: Component Cost Estimate, Component Cost Position.
- Footnote: These actions are also required to comply with section 811 of Pub. L. 106-398.
- Footnote: For national security systems, these requirements apply to the extent practicable (40 U.S.C. 11103).
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/CCA-Compliance

### MCA-C07 · CCA action 7: Develop clearly established measures and accountability for program progress.

- Pathway: MCA (Major Capability Acquisition). Table: Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: Programs that acquire IT, including national security systems and IT embedded in weapon systems.
- Condition code: `it_type is one of {it_system, embedded_it}`
- When due: Report compliance at the events in the CLINGER-COHEN ACT (CCA) COMPLIANCE row of the milestone table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: Acquisition Strategy, APB, TEMP.
- Footnote: These actions are also required to comply with section 811 of Pub. L. 106-398.
- Footnote: The APB and TEMP may be submitted in draft to expedite program assessment.
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/CCA-Compliance

### MCA-C08 · CCA action 8: Ensure that the acquisition is consistent with the DoD Information Enterprise policies and architecture, as described in DoDI 5000.82.

- Pathway: MCA (Major Capability Acquisition). Table: Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: Programs that acquire IT, including national security systems and IT embedded in weapon systems.
- Condition code: `it_type is one of {it_system, embedded_it}`
- When due: Report compliance at the events in the CLINGER-COHEN ACT (CCA) COMPLIANCE row of the milestone table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: CDD NR-KPP, ISP, Applicable JIE Reference Architectures.
- Footnote: These actions are also required to comply with section 811 of Pub. L. 106-398.
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's CCA table has no TYPE column.
- Changed since AAFDID (JCIDS disestablished): see 20-changes-since-aafdid.md, note jcids-2025.
- Page: https://www.waru.edu/aafdid/CCA-Compliance

### MCA-C09 · CCA action 9: Ensure that the program has a Cybersecurity Strategy that is consistent with DoD policies, standards and architectures, to include relevant standards.

- Pathway: MCA (Major Capability Acquisition). Table: Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: Programs that acquire IT, including national security systems and IT embedded in weapon systems.
- Condition code: `it_type is one of {it_system, embedded_it}`
- When due: Report compliance at the events in the CLINGER-COHEN ACT (CCA) COMPLIANCE row of the milestone table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: Cybersecurity Strategy, Program Protection Plan, Risk Management Framework Security Plan.
- Footnote: These actions are also required to comply with section 811 of Pub. L. 106-398.
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/CCA-Compliance

### MCA-C10 · CCA action 10: Ensure, to the maximum extent practicable, (1) modular contracting has been used, and (2) the program is being implemented in phased, successive increments, each of which meets part of the mission need and delivers measurable benefit, independent of future increments.

- Pathway: MCA (Major Capability Acquisition). Table: Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: Programs that acquire IT, including national security systems and IT embedded in weapon systems.
- Condition code: `it_type is one of {it_system, embedded_it}`
- When due: Report compliance at the events in the CLINGER-COHEN ACT (CCA) COMPLIANCE row of the milestone table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: Acquisition Strategy.
- Footnote: These actions are also required to comply with section 811 of Pub. L. 106-398.
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/CCA-Compliance

### MCA-C11 · CCA action 11: Register Mission-Critical and Mission-Essential systems with the DoD CIO.

- Pathway: MCA (Major Capability Acquisition). Table: Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: Programs that acquire IT, including national security systems and IT embedded in weapon systems.
- Condition code: `it_type is one of {it_system, embedded_it}`
- When due: Report compliance at the events in the CLINGER-COHEN ACT (CCA) COMPLIANCE row of the milestone table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: DoD Information Technology Portfolio Repository.
- Footnote: These actions are also required to comply with section 811 of Pub. L. 106-398.
- Footnote: Mission-critical and mission-essential information system definitions are on the source page.
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/CCA-Compliance

## Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs

### CSDR-01 · Contractor Business Data Report

- Pathway: MCA (Major Capability Acquisition). Table: Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs.
- Status when the condition holds: May apply.
- Applies when: ACAT I and II programs and IS programs (including DBS) whose contractor business unit holds CSDR contracts expected to exceed $250M then-year. Not for business units whose only CSDR contracts are MTA contracts.
- Condition code: `(pathway = mca AND mca_program_type is one of {mdap, mais, acat_ii}) OR pathway = dbs`
- When due: Per the approved CSDR plan.
- Type: Regulatory.
- Source: DoDI 5000.73
- AAFDID note: Required for contractor business entities (e.g., plant, site, or business unit) responsible for contracts or subcontracts with CSDR requirements that are expected to exceed $250 million, then-year dollars. Not required for business units based solely on CSDR requirement Middle Tier Acquisition Program contracts.
- Tool note: Classified as regulatory by this tool (DoDI 5000.73). Program value above $100M is not asked, so IS and non-major MTA programs show these as may apply.
- Page: https://www.waru.edu/aafdid/Cost-Data-Reporting-Requirements

### CSDR-02 · Contractor Cost Data Report

- Pathway: MCA (Major Capability Acquisition). Table: Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs.
- Status when the condition holds: Required (contract-level).
- Applies when: ACAT I and II programs: contracts over $50M, or $20M to $50M at the CSDR plan authority's discretion. MTA programs over $100M: contracts over $20M. IS programs over $100M, including DBS: contracts over $50M. All then-year dollars.
- Condition code: `(pathway = mca AND mca_program_type is one of {mdap, mais, acat_ii} AND contract_value > 50,000,000) OR (pathway = mta AND mta_size is one of {major, exceeds_mdap} AND contract_value > 20,000,000)`
- May apply instead when: `(pathway = mca AND mca_program_type is one of {mdap, mais, acat_ii} AND contract_value > 20,000,000 AND contract_value <= 50,000,000) OR (pathway = mta AND mta_size = non_major AND contract_value > 20,000,000) OR (pathway = dbs AND contract_value > 20,000,000)`
- When due: Per the approved CSDR plan.
- Type: Regulatory.
- Source: DoDI 5000.73
- AAFDID note: Acat i ii programs: All contracts, subcontracts, government-performed efforts, and major components (e.g., government furnished equipment), including FMS and programs in sustainment, regardless of acquisition phase and contract type, including non-FAR agreements, valued at more than $50 million, then-year dollars, for current and former ACAT I – II programs. High-risk or high-technical-interest, as determined by the CSDR plan approval authority, or software contracts priced between $20 million and $50 million, then-year dollars. Information system programs: All contracts, subcontracts, government-performed efforts, and major components (e.g., government furnished equipment), regardless of acquisition phase and contract type, including non-FAR agreements, valued at more than $50 million, then-year dollars, for IS programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures. High-risk or high-technical-interest, as determined by the CSDR plan approval authority, or software contracts priced between $20 million and $50 million, then-year dollars. Middle tier acquisition programs: All contracts, subcontracts, government-performed efforts, and major components (e.g., government furnished equipment), regardless of acquisition phase and contract type, including non-FAR agreements, valued at more than $20 million, then-year dollars, for Middle Tier Acquisition Programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures. Other programs gt 100m: May be required at the discretion of the CSDR approval authority for all high interest or high-risk contracts, subcontracts, or government-performed efforts. Not required: Contracts on programs with anticipated acquisition expenditures less than $100 million, then-year dollars. Contracts priced below $20 million, then-year dollars. PM requests and obtains approval from the DDCA for a reporting waiver (e.g., procurement of commercial systems).
- Tool note: Classified as regulatory by this tool (DoDI 5000.73). Program value above $100M is not asked, so IS and non-major MTA programs show these as may apply.
- Page: https://www.waru.edu/aafdid/Cost-Data-Reporting-Requirements

### CSDR-03 · Maintenance and Repair Parts Data Report

- Pathway: MCA (Major Capability Acquisition). Table: Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs.
- Status when the condition holds: May apply.
- Applies when: Sustainment contracts over $50M for ACAT I and II programs and IS programs over $100M, when the PM cannot provide equivalent data, at the CSDR plan authority's discretion.
- Condition code: `(pathway = mca AND mca_program_type is one of {mdap, mais, acat_ii} AND contract_value > 50,000,000) OR (pathway = dbs AND contract_value > 50,000,000)`
- When due: Per the approved CSDR plan.
- Type: Regulatory.
- Source: DoDI 5000.73
- AAFDID note: All sustainment contracts, government-performed efforts, and major components (e.g., government furnished equipment), regardless of contract type, including non-FAR agreements, valued at more than $50 million, then-year dollars, for programs that exceed ACAT I-II level thresholds and IS programs that are anticipated to exceed $100 million, then-year dollars, when equivalent information cannot be provided by the program manager, at the discretion of the CSDR plan approval authority.
- Tool note: Classified as regulatory by this tool (DoDI 5000.73). Program value above $100M is not asked, so IS and non-major MTA programs show these as may apply.
- Page: https://www.waru.edu/aafdid/Cost-Data-Reporting-Requirements

### CSDR-04 · Program Resource Distribution Table

- Pathway: MCA (Major Capability Acquisition). Table: Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs.
- Status when the condition holds: Required (contract-level).
- Applies when: ACAT I and II programs: contracts over $50M then-year, or $20M to $50M at the CSDR plan authority's discretion.
- Condition code: `mca_program_type is one of {mdap, mais, acat_ii} AND contract_value > 50,000,000`
- May apply instead when: `mca_program_type is one of {mdap, mais, acat_ii} AND contract_value > 20,000,000 AND contract_value <= 50,000,000`
- When due: Per the approved CSDR plan.
- Type: Regulatory.
- Source: DoDI 5000.73
- AAFDID note: ACAT I-II Level Programs: All contracts, subcontracts, government-performed efforts, and major components (e.g., government furnished equipment), including foreign military sales (FMS) and programs in sustainment, regardless of acquisition phase and contract type, including non-Federal Acquisition Regulation (FAR) agreements, valued at more than $50 million, then-year dollars, for ACAT I-II level programs. High-risk or high-technical-interest, as determined by the CSDR plan approval authority, or software contracts priced between $20 million and $50 million, then-year dollars.
- Tool note: Classified as regulatory by this tool (DoDI 5000.73). Program value above $100M is not asked, so IS and non-major MTA programs show these as may apply.
- Page: https://www.waru.edu/aafdid/Cost-Data-Reporting-Requirements

### CSDR-05 · Software Resources Data Report

- Pathway: MCA (Major Capability Acquisition). Table: Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs.
- Status when the condition holds: May apply.
- Applies when: Software development, production or maintenance efforts over $20M then-year for ACAT I and II programs, IS programs over $100M (including DBS) and MTA programs over $100M.
- Condition code: `(pathway = mca AND mca_program_type is one of {mdap, mais, acat_ii} AND contract_value > 20,000,000) OR (pathway = mta AND contract_value > 20,000,000) OR (pathway = dbs AND contract_value > 20,000,000)`
- When due: Per the approved CSDR plan.
- Type: Regulatory.
- Source: DoDI 5000.73
- AAFDID note: Development and erp efforts: All contracts, subcontracts, and government-performed efforts, regardless of acquisition phase and contract type, including non-FAR agreements, for developing and/or producing software valued at more than $20 million, then-year dollars, for: Programs that exceed the ACAT I-II level thresholds. IS programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures. All contracts, subcontracts, government-performed efforts, and major components (e.g., government furnished equipment), regardless of acquisition phase and contract type, including non-FAR agreements, valued at more than $20 million, then-year dollars, for Middle Tier Acquisition Programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures. High-risk or high-technical-interest software efforts estimated below $20 million, then-year dollars, as determined by the CSDR plan approval authority, if the overall effort inclusive of non-software efforts exceeds $20 million, then-year dollars. Maintenance efforts: For all contracts, subcontracts, and government-performed efforts, regardless of acquisition phase and contract type, including non-FAR agreements, for: Programs with previous SRDR development or enterprise resource planning requirements or software maintenance efforts of more than $20 million, then-year dollars. Programs that exceed the ACAT I-II level thresholds. IS programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures.
- Tool note: Classified as regulatory by this tool (DoDI 5000.73). Program value above $100M is not asked, so IS and non-major MTA programs show these as may apply.
- Page: https://www.waru.edu/aafdid/Cost-Data-Reporting-Requirements

### CSDR-06 · Technical Data Report

- Pathway: MCA (Major Capability Acquisition). Table: Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs.
- Status when the condition holds: May apply.
- Applies when: Contracts over $50M for ACAT I and II programs and IS programs over $100M, when the PM cannot provide equivalent data, at the CSDR plan authority's discretion.
- Condition code: `(pathway = mca AND mca_program_type is one of {mdap, mais, acat_ii} AND contract_value > 50,000,000) OR (pathway = dbs AND contract_value > 50,000,000)`
- When due: Per the approved CSDR plan.
- Type: Regulatory.
- Source: DoDI 5000.73
- AAFDID note: All contracts, government-performed efforts, and major components (e.g., government furnished equipment), regardless of acquisition phase and contract type, including non-FAR agreements, valued at more than $50 million, then-year dollars, for programs that exceed the ACAT I and II level threshold and IS programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures when equivalent information cannot be provided by the program manager, at the discretion of the CSDR plan approval authority.
- Tool note: Classified as regulatory by this tool (DoDI 5000.73). Program value above $100M is not asked, so IS and non-major MTA programs show these as may apply.
- Page: https://www.waru.edu/aafdid/Cost-Data-Reporting-Requirements

## Acquisition Program Baselines

### MCA-B01 · APB rule: Original Baseline Description or Original APB

- Pathway: MCA (Major Capability Acquisition). Table: Acquisition Program Baselines.
- Status when the condition holds: Reference rule.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Not tied to one event
- Type: Not stated.
- AAFDID note: For all programs: The first APB is approved by the MDA prior to a program entering Engineering and Manufacturing Development, or at program initiation, whichever occurs later. Serves as the current baseline description until a revised APB is approved. Incorporates the KPPs from the CDD. For MDAPs: The cost/unit cost estimate parameters may be revised under 10 U.S.C. 4214 only if a breach occurs that exceeds the critical cost growth threshold for the program under 10 U.S.C. 4371.
- Changed since AAFDID (JCIDS disestablished): see 20-changes-since-aafdid.md, note jcids-2025.
- Page: https://www.waru.edu/aafdid/Acquisition-Program-Baselines

### MCA-B02 · APB rule: Current Baseline Description or Current APB

- Pathway: MCA (Major Capability Acquisition). Table: Acquisition Program Baselines.
- Status when the condition holds: Reference rule.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Not tied to one event
- Type: Not stated.
- AAFDID note: May be revised only: At milestone and FRP decisions; As a result of a major program restructure that is fully funded and approved by the MDA; As a result of a program deviation (breach); or At the MDA's discretion, if fact of life program changes are so significant that managing to the existing baseline is not practical. Circumstances authorizing changes are limited; revisions to the current baseline estimate/APB are not automatically authorized for program changes to cost, schedule, or performance parameters. Revisions to the current APB will not be authorized unless there is a significant change in program parameters. A revision to the current APB will not be authorized if proposed merely to avoid a reportable breach. The MDA determines whether to revise the APB.
- Page: https://www.waru.edu/aafdid/Acquisition-Program-Baselines

### MCA-B03 · APB rule: Deviations

- Pathway: MCA (Major Capability Acquisition). Table: Acquisition Program Baselines.
- Status when the condition holds: Reference rule.
- Applies when: For MDAPs, ACAT II and ACAT III and below.
- Condition code: `mca_program_type is one of {mdap, acat_ii, acat_iii}`
- When due: Not tied to one event
- Type: Not stated.
- AAFDID note: The PM will immediately notify the MDA when the PM becomes aware of an impending deviation from any parameter (cost, schedule, performance, etc.). Within 30 business days of occurrence of the deviation, the PM will submit a Program Deviation Report that informs the MDA of the reason for the deviation and planned actions. Within 90 business days of occurrence of the deviation: The PM will bring the program back within APB parameters; or The PM will submit information to the Overarching Integrated Product Team (OIPT) (for ACAT ID), or to an equivalent Component-level review team (for ACAT IB or IC programs), to inform a recommendation to the MDA on whether it is appropriate to approve a revision to an APB. The MDA will decide, after considering the recommendation resulting from the OIPT or equivalent Component-level review, whether it is appropriate to approve a revision to an APB.
- Page: https://www.waru.edu/aafdid/Acquisition-Program-Baselines

### MCA-B04 · APB rule: Subprograms (10 U.S.C. 4203)

- Pathway: MCA (Major Capability Acquisition). Table: Acquisition Program Baselines.
- Status when the condition holds: Reference rule.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: Not tied to one event
- Type: Not stated.
- Source: 10 U.S.C. 4203
- AAFDID note: When an MDAP requires the delivery of two or more categories of end items that differ significantly in form and function, or delivery in two or more increments or blocks, subprograms may be established for the purpose of acquisition reporting. Once one subprogram is designated, all remaining elements (increments or components) of the program will also be appropriately organized into one or more other subprograms. If a major subprogram is designated, Selected Acquisition Reports, Unit Cost Reports, and program baselines shall reflect cost; schedule and performance information for the MDAP as a whole and for each major subprogram of the MDAP so designated.
- Page: https://www.waru.edu/aafdid/Acquisition-Program-Baselines

## Statutory Program Breach Definitions

### MCA-N01 · Significant Nunn-McCurdy Unit Cost Breach

- Pathway: MCA (Major Capability Acquisition). Table: Statutory Program Breach Definitions.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: When the breach occurs.
- Type: Statutory. AAFDID TYPE: Statutory
- Source: 10 U.S.C. 4371-4377
- AAFDID note: The cost growth threshold, as it relates to the current APB, is defined to be an increase of at least 15 percent over the program acquisition unit cost (PAUC) or average procurement unit cost (APUC) for the current program as shown in the current Baseline Estimate. The cost growth threshold, as it relates to the original APB, is defined to be an increase of at least 30 percent over the PAUC or APUC for the original program as shown in the original Baseline Estimate. Only the current APB will be revised.
- Page: https://www.waru.edu/aafdid/Statutory-Program-Breach-Definitions

### MCA-N02 · Critical Nunn-McCurdy Unit Cost Breaches

- Pathway: MCA (Major Capability Acquisition). Table: Statutory Program Breach Definitions.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: When the breach occurs.
- Type: Statutory. AAFDID TYPE: Statutory
- Source: 10 U.S.C. 4371-4375
- AAFDID note: The cost growth threshold, as it relates to the current APB, is defined to be an increase of at least 25 percent over the PAUC or APUC for the program or subprogram as shown in the current Baseline Estimate/APB. The cost growth threshold, as it relates to the original APB, is defined to be an increase of at least 50 percent over the PAUC or APUC for the program or subprogram as shown in the original Baseline Estimate/APB for the program or subprogram. If the program or subprogram is certified rather than terminated, the most recent major milestone must be rescinded and a new milestone is required after certification. The program establishes a revised original Baseline Estimate/APB that reflects MDA certification and approval.
- Page: https://www.waru.edu/aafdid/Statutory-Program-Breach-Definitions

### MCA-N03 · Cost or Schedule Growth Notification for a 10 U.S.C. 4252 Certified Program

- Pathway: MCA (Major Capability Acquisition). Table: Statutory Program Breach Definitions.
- Status when the condition holds: Only if triggered.
- Applies when: For MDAPs.
- Condition code: `mca_program_type is one of {mdap}`
- When due: When the breach occurs.
- Type: Statutory. AAFDID TYPE: Statutory
- Source: 10 U.S.C. 4252
- AAFDID note: The PM for an MDAP that has received Milestone B certification will immediately notify the MDA of any changes to the program or a designated major subprogram of such program that alter the substantive basis for the certification of the milestone decision.
- Page: https://www.waru.edu/aafdid/Statutory-Program-Breach-Definitions

## EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway)

### EVM-01 · EVMS on contract, < $20M: EVMS not required; may be applied at PM discretion based on risk to the Government

- Pathway: MCA (Major Capability Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: May apply.
- Applies when: Cost-reimbursable or incentive contract of 18 months or more, valued < $20M (then-year dollars, including options).
- Condition code: `contract_cost_type = yes AND contract_value < 20,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Part 7 of Office of Management and Budget Circular A- 11 FAR 52.234-4, FAR subpart, 34.2 DFARS 234.201 DoDI 5000.85, Para. 3C.3.c.(3)
- AAFDID note: Requires business case analysis and MDA approval.
- Tool note: Classified as regulatory by this tool: the row cites OMB Circular A-11, the FAR, the DFARS and DoDI 5000.85.
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-02 · EVMS on contract, ≥ $20M &<$100M: EVMS Required; Contractor is required to have an EVMS that complies with the guidelines in EIA-748.*

- Pathway: MCA (Major Capability Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Cost-reimbursable or incentive contract of 18 months or more, valued ≥ $20M &<$100M (then-year dollars, including options).
- Condition code: `contract_cost_type = yes AND contract_value >= 20,000,000 AND contract_value < 100,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Part 7 of Office of Management and Budget Circular A- 11 FAR 52.234-4, FAR subpart, 34.2 DFARS 234.201 DoDI 5000.85, Para. 3C.3.c.(3)
- AAFDID note: The Government reserves the right to review a contractor’s EVMS when deemed necessary to verify compliance.
- Tool note: Classified as regulatory by this tool: the row cites OMB Circular A-11, the FAR, the DFARS and DoDI 5000.85.
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-03 · EVMS on contract, ≥ $100M: EVMS Required; Contractor is required to have an EVMS that has been determined to be in compliance with the guidelines in EIA-748.*

- Pathway: MCA (Major Capability Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Cost-reimbursable or incentive contract of 18 months or more, valued ≥ $100M (then-year dollars, including options).
- Condition code: `contract_cost_type = yes AND contract_value >= 100,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Part 7 of Office of Management and Budget Circular A- 11 FAR 52.234-4, FAR subpart, 34.2 DFARS 234.201 DoDI 5000.85, Para. 3C.3.c.(3)
- AAFDID note: The Contractor will provide access to all pertinent records and data requested by the Contracting Officer or duly authorized representative as necessary to permit initial and ongoing Government compliance reviews to ensure that the EVMS complies, and continues to comply, with the guidelines in EIA-748.*
- Tool note: Classified as regulatory by this tool: the row cites OMB Circular A-11, the FAR, the DFARS and DoDI 5000.85.
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-04 · IPMDAR (DI-MGMT-81861), < $20M: Not required

- Pathway: MCA (Major Capability Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: May apply.
- Applies when: Contracts under $20M: not required. The PMO may request IPMDAR cost or schedule reporting.
- Condition code: `contract_value < 20,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Integrated Program Management Data and Analysis Report (IPMDAR) DID DI-MGMT-81861
- AAFDID note: Integrated Program Management Data and Analysis Report (IPMDAR) may be used if cost and/or schedule reporting is requested by the program management office.
- Tool note: Classified as regulatory by this tool (DoDI 5000.85; DI-MGMT-81861).
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-05 · IPMDAR (DI-MGMT-81861), ≥ $20M & < $100M: Required monthly when EVMS requirement is on contract

- Pathway: MCA (Major Capability Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Monthly when an EVMS requirement is on contract ($20M to under $100M).
- Condition code: `contract_cost_type = yes AND contract_value >= 20,000,000 AND contract_value < 100,000,000`
- When due: Monthly
- Type: Regulatory.
- Source: Integrated Program Management Data and Analysis Report (IPMDAR) DID DI-MGMT-81861
- AAFDID note: All IPMDAR datasets/files must be included in the CDRL. Tailoring in accordance with DI-MGMT-81861 and Implementation Guide is allowed.
- Tool note: Classified as regulatory by this tool (DoDI 5000.85; DI-MGMT-81861).
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-06 · IPMDAR (DI-MGMT-81861), ≥ $100M: Required monthly when EVMS requirement is on contract

- Pathway: MCA (Major Capability Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Monthly when an EVMS requirement is on contract ($100M or more).
- Condition code: `contract_cost_type = yes AND contract_value >= 100,000,000`
- When due: Monthly
- Type: Regulatory.
- Source: Integrated Program Management Data and Analysis Report (IPMDAR) DID DI-MGMT-81861
- AAFDID note: IPMDAR is required. All files are required.
- Tool note: Classified as regulatory by this tool (DoDI 5000.85; DI-MGMT-81861).
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements


---

# MTA requirements: Middle Tier of Acquisition

Knowledge file 11 of the AAFDID Navigator agent pack, rules 1.0.0. Every record below belongs to the MTA pathway only.

- Governing instruction: DoDI 5000.80 (Change 1, November 2024); 10 U.S.C. 3602
- Summary: Rapid Prototyping fields a prototype with residual operational capability within 5 years. Rapid Fielding starts production within 6 months and completes fielding within 5 years. The clock starts when the decision authority signs the program-start ADM.
- Decision authority: The component acquisition executive unless delegated (DoDI 5000.80, para 2.6.a). Above MDAP thresholds, USD(A&S) must approve MTA use in writing (paras 2.1.b, 4.1.c).
- Events, in order: `entrance` = Program entrance: the ADM starts the MTA clock; `execution` = Throughout program execution; `exit` = Program exit: the outcome ADM
- Note: AAFDID's MTA overview: MTA has no milestones, and decision authorities keep discretion over documentation. The statutory and regulatory table lists requirements that may be applicable.
- Note: AAFDID's MTA tables do not separate Rapid Prototyping from Rapid Fielding. The difference shows only in the cost-estimate notes.
- AAFDID page: https://www.waru.edu/aafdid/mta

## Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs

### CSDR-02 · Contractor Cost Data Report

- Pathway: MTA (Middle Tier of Acquisition). Table: Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs.
- Status when the condition holds: Required (contract-level).
- Applies when: ACAT I and II programs: contracts over $50M, or $20M to $50M at the CSDR plan authority's discretion. MTA programs over $100M: contracts over $20M. IS programs over $100M, including DBS: contracts over $50M. All then-year dollars.
- Condition code: `(pathway = mca AND mca_program_type is one of {mdap, mais, acat_ii} AND contract_value > 50,000,000) OR (pathway = mta AND mta_size is one of {major, exceeds_mdap} AND contract_value > 20,000,000)`
- May apply instead when: `(pathway = mca AND mca_program_type is one of {mdap, mais, acat_ii} AND contract_value > 20,000,000 AND contract_value <= 50,000,000) OR (pathway = mta AND mta_size = non_major AND contract_value > 20,000,000) OR (pathway = dbs AND contract_value > 20,000,000)`
- When due: Per the approved CSDR plan.
- Type: Regulatory.
- Source: DoDI 5000.73
- AAFDID note: Acat i ii programs: All contracts, subcontracts, government-performed efforts, and major components (e.g., government furnished equipment), including FMS and programs in sustainment, regardless of acquisition phase and contract type, including non-FAR agreements, valued at more than $50 million, then-year dollars, for current and former ACAT I – II programs. High-risk or high-technical-interest, as determined by the CSDR plan approval authority, or software contracts priced between $20 million and $50 million, then-year dollars. Information system programs: All contracts, subcontracts, government-performed efforts, and major components (e.g., government furnished equipment), regardless of acquisition phase and contract type, including non-FAR agreements, valued at more than $50 million, then-year dollars, for IS programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures. High-risk or high-technical-interest, as determined by the CSDR plan approval authority, or software contracts priced between $20 million and $50 million, then-year dollars. Middle tier acquisition programs: All contracts, subcontracts, government-performed efforts, and major components (e.g., government furnished equipment), regardless of acquisition phase and contract type, including non-FAR agreements, valued at more than $20 million, then-year dollars, for Middle Tier Acquisition Programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures. Other programs gt 100m: May be required at the discretion of the CSDR approval authority for all high interest or high-risk contracts, subcontracts, or government-performed efforts. Not required: Contracts on programs with anticipated acquisition expenditures less than $100 million, then-year dollars. Contracts priced below $20 million, then-year dollars. PM requests and obtains approval from the DDCA for a reporting waiver (e.g., procurement of commercial systems).
- Tool note: Classified as regulatory by this tool (DoDI 5000.73). Program value above $100M is not asked, so IS and non-major MTA programs show these as may apply.
- Page: https://www.waru.edu/aafdid/Cost-Data-Reporting-Requirements

### CSDR-05 · Software Resources Data Report

- Pathway: MTA (Middle Tier of Acquisition). Table: Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs.
- Status when the condition holds: May apply.
- Applies when: Software development, production or maintenance efforts over $20M then-year for ACAT I and II programs, IS programs over $100M (including DBS) and MTA programs over $100M.
- Condition code: `(pathway = mca AND mca_program_type is one of {mdap, mais, acat_ii} AND contract_value > 20,000,000) OR (pathway = mta AND contract_value > 20,000,000) OR (pathway = dbs AND contract_value > 20,000,000)`
- When due: Per the approved CSDR plan.
- Type: Regulatory.
- Source: DoDI 5000.73
- AAFDID note: Development and erp efforts: All contracts, subcontracts, and government-performed efforts, regardless of acquisition phase and contract type, including non-FAR agreements, for developing and/or producing software valued at more than $20 million, then-year dollars, for: Programs that exceed the ACAT I-II level thresholds. IS programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures. All contracts, subcontracts, government-performed efforts, and major components (e.g., government furnished equipment), regardless of acquisition phase and contract type, including non-FAR agreements, valued at more than $20 million, then-year dollars, for Middle Tier Acquisition Programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures. High-risk or high-technical-interest software efforts estimated below $20 million, then-year dollars, as determined by the CSDR plan approval authority, if the overall effort inclusive of non-software efforts exceeds $20 million, then-year dollars. Maintenance efforts: For all contracts, subcontracts, and government-performed efforts, regardless of acquisition phase and contract type, including non-FAR agreements, for: Programs with previous SRDR development or enterprise resource planning requirements or software maintenance efforts of more than $20 million, then-year dollars. Programs that exceed the ACAT I-II level thresholds. IS programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures.
- Tool note: Classified as regulatory by this tool (DoDI 5000.73). Program value above $100M is not asked, so IS and non-major MTA programs show these as may apply.
- Page: https://www.waru.edu/aafdid/Cost-Data-Reporting-Requirements

## Program Information Requirements (Table 1: submissions to OSD for all MTA programs)

### MTA-T01 · Acquisition Strategy, to include security, schedule, technical, and production risks; a test strategy or an assessment of test results with validation of required cybersecurity and interoperability as applicable; and a transition plan

- Pathway: MTA (Middle Tier of Acquisition). Table: Program Information Requirements (Table 1: submissions to OSD for all MTA programs).
- Status when the condition holds: Required.
- Applies when: For major systems and programs above MDAP thresholds.
- Condition code: `mta_size is one of {major, exceeds_mdap}`
- When due: Program entrance: the ADM starts the MTA clock (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.80; 5010.44
- Footnote: For initial submission, a test strategy can be used in lieu of an assessment of test results if testing is not complete. Programs on the DOT&E oversight list may need additional documentation.
- Changed since AAFDID (DoDI 5000.80 Change 1 and 10 U.S.C. 3602): see 20-changes-since-aafdid.md, note mta-change1-2024.
- Page: https://www.waru.edu/aafdid/MTA-Program-Information-Requirements

### MTA-T02 · ADM signed by the DA

- Pathway: MTA (Middle Tier of Acquisition). Table: Program Information Requirements (Table 1: submissions to OSD for all MTA programs).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Program entrance: the ADM starts the MTA clock (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.80
- Page: https://www.waru.edu/aafdid/MTA-Program-Information-Requirements

### MTA-T03 · Approved Requirement

- Pathway: MTA (Middle Tier of Acquisition). Table: Program Information Requirements (Table 1: submissions to OSD for all MTA programs).
- Status when the condition holds: Required.
- Applies when: For major systems and programs above MDAP thresholds.
- Condition code: `mta_size is one of {major, exceeds_mdap}`
- When due: Program entrance: the ADM starts the MTA clock (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.80
- Changed since AAFDID (DoDI 5000.80 Change 1 and 10 U.S.C. 3602): see 20-changes-since-aafdid.md, note mta-change1-2024.
- Page: https://www.waru.edu/aafdid/MTA-Program-Information-Requirements

### MTA-T04 · Cost Estimate

- Pathway: MTA (Middle Tier of Acquisition). Table: Program Information Requirements (Table 1: submissions to OSD for all MTA programs).
- Status when the condition holds: Required.
- Applies when: For major systems and programs above MDAP thresholds.
- Condition code: `mta_size is one of {major, exceeds_mdap}`
- When due: Program entrance: the ADM starts the MTA clock (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.80; 5000.73
- Footnote: Per DoDI 5000.73, CAPE estimates life-cycle costs for Rapid Prototyping programs likely to exceed the ACAT I threshold, and for Rapid Fielding programs likely to exceed the ACAT I or II thresholds.
- Page: https://www.waru.edu/aafdid/MTA-Program-Information-Requirements

### MTA-T05 · Initial PID Entry

- Pathway: MTA (Middle Tier of Acquisition). Table: Program Information Requirements (Table 1: submissions to OSD for all MTA programs).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Program entrance: the ADM starts the MTA clock (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.80
- Page: https://www.waru.edu/aafdid/MTA-Program-Information-Requirements

### MTA-T06 · Lifecycle Sustainment Plan

- Pathway: MTA (Middle Tier of Acquisition). Table: Program Information Requirements (Table 1: submissions to OSD for all MTA programs).
- Status when the condition holds: Required.
- Applies when: For major systems and programs above MDAP thresholds; Rapid Fielding only.
- Condition code: `mta_size is one of {major, exceeds_mdap} AND mta_path = rf`
- May apply instead when: `mta_size is one of {major, exceeds_mdap} AND mta_path = rp`
- When due: Program entrance: the ADM starts the MTA clock (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.80; 5000.91
- Page: https://www.waru.edu/aafdid/MTA-Program-Information-Requirements

### MTA-T07 · Written decision by USD(A&S)

- Pathway: MTA (Middle Tier of Acquisition). Table: Program Information Requirements (Table 1: submissions to OSD for all MTA programs).
- Status when the condition holds: Required.
- Applies when: For programs above MDAP thresholds.
- Condition code: `mta_size is one of {exceeds_mdap}`
- When due: Program entrance: the ADM starts the MTA clock (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.80
- Changed since AAFDID (MDAP and major system thresholds raised): see 20-changes-since-aafdid.md, note thresholds-2025.
- Page: https://www.waru.edu/aafdid/MTA-Program-Information-Requirements

### MTA-T08 · Updated PID Entry

- Pathway: MTA (Middle Tier of Acquisition). Table: Program Information Requirements (Table 1: submissions to OSD for all MTA programs).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Throughout program execution (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.80
- Page: https://www.waru.edu/aafdid/MTA-Program-Information-Requirements

### MTA-T09 · An assessment of test results

- Pathway: MTA (Middle Tier of Acquisition). Table: Program Information Requirements (Table 1: submissions to OSD for all MTA programs).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Program exit: the outcome ADM (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.80
- Page: https://www.waru.edu/aafdid/MTA-Program-Information-Requirements

### MTA-T10 · Final PID capturing updated entries, to include the outcome, sustainment, and final budget of the MTA program

- Pathway: MTA (Middle Tier of Acquisition). Table: Program Information Requirements (Table 1: submissions to OSD for all MTA programs).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Program exit: the outcome ADM (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.80
- Page: https://www.waru.edu/aafdid/MTA-Program-Information-Requirements

### MTA-T11 · Outcome determination ADM signed by the DA

- Pathway: MTA (Middle Tier of Acquisition). Table: Program Information Requirements (Table 1: submissions to OSD for all MTA programs).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Program exit: the outcome ADM (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.80
- Changed since AAFDID (DoDI 5000.80 Change 1 and 10 U.S.C. 3602): see 20-changes-since-aafdid.md, note mta-change1-2024.
- Page: https://www.waru.edu/aafdid/MTA-Program-Information-Requirements

## Statutory and Regulatory Requirements that may be applicable

### MTA-S01 · Acquisition Decision Memorandum (ADM)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Decision Authority (DA)
- Source: DoDI 5000.80
- AAFDID note: Regulatory. Documents MDA decisions and direction. Per new policy update dated Oct 20, 2022 - After approval of the program for use of the MTA pathway, the DA will sign their program ADM. The ADM signature will then start the MTA clock.
- Changed since AAFDID (DoDI 5000.80 Change 1 and 10 U.S.C. 3602): see 20-changes-since-aafdid.md, note mta-change1-2024.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S02 · ACQUISITION STRATEGY

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Statutory if `mta_size is one of {major, exceeds_mdap}`, otherwise Regulatory. If that is unknown, the type depends on the answer. AAFDID TYPE: Regulatory, Statutory
- Approval: DA
- Source: DoDi 5000.80 10 U.S.C. 4211 {formerly 2431a}
- AAFDID note: STATUTORY for Major systems. Regulatory for Non-major systems. The Acquisition Strategy includes STATUTORY and Regulatory information. Major changes to the plan reflected in the Acquisition Strategy require DA approval. The DA must review and approve the strategy when there has been a significant change to the cost, schedule, or performance of the program (or system) or there has been a critical change to the cost of the program (or system). The strategy may also be reviewed and approved at any time considered relevant by the DA. The following requirements will be satisfied in the Acquisition Strategy: ACQUISITION APPROACH BENEFIT ANALYSIS AND DETERMINATION, applies to bundled acquisitions only; BUSINESS STRATEGY; CONTRACTING STRATEGY, to include CONTRACT-TYPE DETERMINATION, satisfied when the DA approves the Acquisition Strategy with specified contract types, and Termination Liability Estimate; COOPERATIVE OPPORTUNITIES; GENERAL EQUIPMENT VALUATION; Industrial Base Capabilities Considerations; INTELLECTUAL PROPERTY (IP) STRATEGY, for major weapon systems and subsystems; MARKET RESEARCH; Modular Open Systems Approach (MOSA); MULTI-YEAR PROCUREMENT; PRODUCT SUPPORT, including sustainment, logistics and maintenance; RELIABILITY AND MAINTAINABILITY; RISK MANAGEMENT, including security, schedule, technical, and production risks; SMALL BUSINESS; INNOVATION RESEARCH (SBIR)/SMALL BUSINESS TECHNOLOGY TRANSFER (STTR) PROGRAM TECHNOLOGIES; Test Strategy / Assessment of Test Results; Transition Plan – within 2 years after MTA program start.
- Changed since AAFDID (DoDI 5000.80 Change 1 and 10 U.S.C. 3602): see 20-changes-since-aafdid.md, note mta-change1-2024.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S03 · ACQUISITION APPROACH (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For major systems and programs above MDAP thresholds. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `mta_size is one of {major, exceeds_mdap}`
- When due: Not tied to one event
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: DA
- Source: 10 U.S.C. 4211(c)(2)(A-B) {formerly 2431a}
- AAFDID note: STATUTORY; Describe the top-level business and technical management approach in sufficient detail to allow the DA to assess (1) the viability of the approach; (2) the method of implementing laws and policies; and (3) program objectives. Provide a clear explanation of how the strategy is designed to be implemented within the available resources of time, funding, and management capacity. Discuss the tailoring that will address program requirements and constraints. Where appropriate, the strategy should consider the delivery of required capability in increments, each dependent on available, mature technology, and recognizing up front the need for future capability improvements.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S04 · BENEFIT ANALYSIS AND DETERMINATION (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For major systems and programs above MDAP thresholds. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `mta_size is one of {major, exceeds_mdap}`
- When due: Not tied to one event
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: DA
- Source: 15 U.S.C. 644(e)(2) 15 U.S.C. 632(o)(1-2) 15 U.S.C. 657q
- AAFDID note: STATUTORY. Applies to bundled acquisitions only. Includes MARKET RESEARCH to determine whether consolidation of the requirements is necessary and justified. 15 U.S.C. 632 defines a bundled contract as a contract that is entered into to meet requirements that are consolidated in a bundling of contract requirements. The term "bundling of contract requirements" means consolidating two or more procurement requirements for goods or services previously provided or performed under separate smaller contracts into a solicitation of offers for a single contract that is likely to be unsuitable for award to a small-business concern.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S05 · BUSINESS STRATEGY (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For major systems and programs above MDAP thresholds. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `mta_size is one of {major, exceeds_mdap}`
- When due: Not tied to one event
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: DA
- Source: 10 U.S.C. 4211(c)(2)(D) {formerly 2431a} 10 U.S.C. 4324(c)(2) {formerly 2337}
- AAFDID note: STATUTORY. The business strategy will describe the rationale for the contracting approach and how competition will be maintained at the system and subsystem levels throughout the program life cycle; the strategy will detail how contract incentives will be employed to support Department goals.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S06 · CONTRACTING STRATEGY (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For major systems and programs above MDAP thresholds. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `mta_size is one of {major, exceeds_mdap}`
- When due: Not tied to one event
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: DA
- Source: 10 U.S.C. 4211(c)(2)(E) {formerly 2431a} 10 U.S.C. 3453 {formerly 2377} 41 U.S.C. 3306(a)(1) and 3307(d)
- AAFDID note: STATUTORY. Discuss (1) the planned contract type and how it relates to risk management; (2) whether risk management enables the use of fixed-price elements in subsequent contracts; (3) market research; and (4) small business participation. Include the following sub-elements: CONTRACT-TYPE DETERMINATION Termination Liability Estimate
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S07 · CONTRACT-TYPE DETERMINATION (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For major systems and programs above MDAP thresholds. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `mta_size is one of {major, exceeds_mdap}`
- When due: Not tied to one event
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: DA
- Source: §818, P.L. 109-364 §811, P.L. 112-239 10 U.S.C. 4211(c)(2)(E) {formerly 2431a}
- AAFDID note: STATUTORY. Satisfied when the DA approves the Acquisition Strategy with specified contract types
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S08 · Industrial Base Capabilities Considerations (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For major systems and programs above MDAP thresholds. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `mta_size is one of {major, exceeds_mdap}`
- When due: Not tied to one event
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: DA
- Source: DoDi 5000.60 10 U.S.C. 4211 {formerly 2440}
- AAFDID note: Regulatory. Summarizes the results of the industrial base capabilities' analysis.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S09 · INTELLECTUAL PROPERTY (IP) STRATEGY (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: Decision Authority (DA)
- Source: DoDI 5010.44 10 U.S.C. 3771- 3775 {formerly 2320} 10 U.S.C. 4211 {formerly 2431a}
- AAFDID note: STATUTORY for Major systems and subsystems; Regulatory for Non-major systems. The IP Strategy must be updated as appropriate to support and account for evolving IP considerations associated with the award and administration of all contracts throughout the program life cycle. Becomes part of the Product Support Strategy (PSS) during Operations and Support (O&S).
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S10 · International Involvement (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: AAFDID marks no size column for this row. Its note ties it to the statutory requirement to consider cooperative opportunities, which applies to every program; DoDI 5000.80 Change 1 adds exportability when international partners are involved.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DA
- Source: DoDI 5000.80
- AAFDID note: Regulatory. Satisfies the Statutory requirement to consider Cooperative Opportunities. IAW 5000.80 Not all programs are appropriate for the MTA pathway. Major systems intended to satisfy requirements that are critical to a major interagency requirement, are primarily focused on technology development, or have significant international partner involvement are discouraged from using the MTA pathway.
- Changed since AAFDID (DoDI 5000.80 Change 1 and 10 U.S.C. 3602): see 20-changes-since-aafdid.md, note mta-change1-2024.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S11 · MARKET RESEARCH (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For major systems and programs above MDAP thresholds. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `mta_size is one of {major, exceeds_mdap}`
- When due: Not tied to one event
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: DA
- Source: 10 U.S.C. 3453 {formerly 2377} 41 U.S.C. 3306(a)(1) and 3307(d)
- AAFDID note: STATUTORY. Conducted to reduce the duplication of existing technologies and products, and to understand potential materiel solutions, technology maturity, and potential sources, to assure maximum participation of small business concerns, and possible strategies to acquire them.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S12 · Modular Open System Approach (MOSA) (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For major systems and programs above MDAP thresholds. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `mta_size is one of {major, exceeds_mdap}`
- When due: Not tied to one event
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DA
- Source: DoDI 5000.88
- AAFDID note: Regulatory. Describe how a MOSA will or will not be used to evolve system capability, improve interoperability, reduce cost or schedule, and refresh technology.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S13 · MULTI-YEAR PROCURMENT (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For major systems and programs above MDAP thresholds. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `mta_size is one of {major, exceeds_mdap}`
- When due: Not tied to one event
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: DA
- Source: 10 U.S.C. 3501 {formerly 2306b} DoDI 5000.73
- AAFDID note: STATUTORY. When appropriate, include a summary discussion of multi-year procurement (further discussed in DoDI 5000.73).
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S14 · PRODUCT SUPPORT, including sustainment, logistics, and maintenance (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For major systems and programs above MDAP thresholds. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `mta_size is one of {major, exceeds_mdap}`
- When due: Not tied to one event
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: DA
- Source: 10 U.S.C. 2464; 10 U.S.C. 2466; 10 U.S.C. 4211 {formerly 2431a} DoDI 5000.91
- AAFDID note: STATUTORY. For Major systems. Content requirements of an Acquisition Strategy will ensure that each strategy will consider requirements related to product support, logistics, maintenance, and sustainment IAW 10 U.S.C. 2464 and 2466. REGULATORY. DoD 5000.91: General Statement Up Front: Establishes policy, assigns responsibilities, and prescribes procedures for product support management to establish product support factors early in the requirements development and acquisition process to achieve effective and efficient weapon system capability and life cycle management. Prescribes procedures for program managers (PMs), product support managers (PSMs), and life cycle logisticians (LCLs) to implement the adaptive acquisition framework (AAF) tenets to: Emphasize sustainment. Make data driven decisions. Tailor product support
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S15 · RELIABILITY AND MAINTAINABILITY (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: DA
- Source: 10 U.S.C. 4328 {formerly 2443} January 31, 2019 USD(A&S) Policy Memo, "Implementation of Title 10, United States Code, Section 2443, Sustainment Factors in Weapon System Design." DoDI 5000.88
- AAFDID note: STATUTORY. For Major systems, the PM must, as part of the ACQUISITION STRATEGY: Include measurable requirements for engineering activities and design specifications for R&M; otherwise justify in writing the determination to exclude engineering activities and design specifications for reliability or maintainability. Indicate if sustainment factors, including R&M, are included in the process for source selection; Describe incentive fees and penalties (as appropriate) to incentivize achievement of design specification requirements for R&M. The DA will notify the congressional defense committees upon entering into an EMD or Production contract that includes incentive fees or penalties. DoDI 5000.88, Section 3.b.1 For all defense acquisition programs, the LSE (lead systems engineer), working for the PM, will integrate R&M engineering as an integral part of the overall engineering process and the digital representation of the system being developed. The live AAFDID note also cites the January 31, 2019 USD(A&S) policy memo on implementing 10 U.S.C. 2443 (sustainment factors).
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S16 · RISK MANAGEMENT (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For major systems and programs above MDAP thresholds. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `mta_size is one of {major, exceeds_mdap}`
- When due: Not tied to one event
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: DA
- Source: DoDI 5000.80 10 U.S.C. 4211 {formerly 2431a}; 10 U.S.C. 4212 {formerly 2431b}
- AAFDID note: STATUTORY. Include a comprehensive approach to risk management and mitigation for security, schedule, technical, and production risks. REGULATORY. DoDI 5000.80 Section 2.6. DOD AND OSD COMPONENT HEADS WITH MTA PROGRAMS. The DoD and OSD Component heads with MTA programs oversee their MTA programs through their component acquisition executives (CAEs) and program managers (PMs).
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S17 · Test Strategy/Assessment of Test results (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DA
- Source: DoDI 5000.80 DoDI 5000.89
- AAFDID note: Regulatory. DoD Components will develop a process for demonstrating performance and evaluating for current operational purposes the proposed products and technologies. This process will result in a test strategy or an assessment of test results documenting the evaluation of the demonstrated operational performance, to include validation of required cybersecurity and interoperability as applicable. The operational demonstration assessment will support the initial production decision by the DA. Programs on the DOT&E oversight list will follow applicable procedures.
- Changed since AAFDID (DoDI 5000.80 Change 1 and 10 U.S.C. 3602): see 20-changes-since-aafdid.md, note mta-change1-2024.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S18 · Transition Plan (Part of Acquisition Strategy)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DA
- Source: DoDI 5000.80
- AAFDID note: Regulatory. For each MTA program, DoD Components will develop a process for transitioning successful prototypes to new or existing acquisition programs for production, fielding, and operations and sustainment under the rapid fielding pathway or other acquisition pathway. This process will result in a transition plan, included in the acquisition strategy, which provides a timeline for completion within 2 years of all necessary documentation required for transition, as determined by the DA, after MTA program start. This applies to both major and non-major programs. MTA Transition Plan Template
- Changed since AAFDID (DoDI 5000.80 Change 1 and 10 U.S.C. 3602): see 20-changes-since-aafdid.md, note mta-change1-2024.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S19 · CLINGER-COHEN ACT (CCA) COMPLIANCE

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: DA and Component CIO or designee
- Source: DoDi 5000.82 SUBTITLE III, TITLE 40 §811, P.L. 106-398
- AAFDID note: STATUTORY for all programs that acquire information technology (IT); Regulatory for other programs. See DoDI 5000.82 for amplifying regulatory guidance. A summary of required actions is in the CCA Compliance Table. The PM will report CCA compliance to the DA and the Component CIO or designee. For IT programs employing an incremental development model, the program manager will report CCA compliance at each Limited Deployment Decision Point.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S20 · CYBERSECURITY STRATEGY

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: Component CIO
- Source: DoDi 8500.01 DoDi 5000.82 §811, P.L. 106-398 40 U.S.C. 11313
- AAFDID note: STATUTORY for mission critical and mission essential information technology programs and regulatory for all programs requiring an Authority to Operate (ATO). The Cybersecurity Strategy can serve as the System Security Plan during the Risk Management Framework process. See DoDI 8510.01 and DoDI 5000.82. The CYBERSECURITY STRATEGY is a stand-alone appendix to the Program Protection Plan (PPP). The CYBERSECURITY STRATEGY will be updated prior to receiving an ATO. The Component CIO is the approval authority.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S21 · DoD Component Cost Estimate

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DoD Component
- Source: DoDI 5000.73 DoDI 5000.80
- AAFDID note: Regulatory. See the direction in DoDI 5000.80 and DoDI 5000.73. The DoD Component will determine the cost estimating requirements for Major systems and below.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S22 · Exit Criteria

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DA
- Source: This Table
- AAFDID note: Regulatory. Exit criteria are specific events and accomplishments that must be achieved before a program can proceed; documented in the ADM.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S23 · FREQUENCY ALLOCATION APPLICATION (DD FORM 1494)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: National Telecommunications and Information Administration (NTIA)
- Source: §104, P.L. 102-538 47 U.S.C. 305, 901-904
- AAFDID note: STATUTORY for all systems/equipment that use the electromagnetic spectrum while operating in the United States and its possessions. The DD Form 1494, Application for Equipment Frequency https://www.esd.whs.mil/Directives/forms/dd1000_1499/ Allocation, is available from The Title 47 STATUTORY requirement is satisfied when the NTIA has authorized national spectrum certification(s) for the program at Stage 1, 2, 3 or 4, as applicable, in response to submitted DD Form(s) 1494 by the program manager.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S24 · Full Funding Certification Memorandum

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DA
- Source: DoDI 5000.73
- AAFDID note: Regulatory. See DoDI 5000.73 for details, including coordination requirements.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S25 · Independent Cost Estimate (ICE)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: DCAPE
- Source: 10 U.S.C. 4323 {formerly 2441} DoDI 5000.73
- AAFDID note: Regulatory. DoDI 5000.73 provides detailed instructions. (1) Rapid Prototyping Programs. CAPE will conduct an estimate of life-cycle costs for programs likely to exceed acquisition category (ACAT) I threshold pursued using the MTA rapid prototyping pathway. CAPE may, in its discretion, delegate the authority for the conduct of the cost estimate to the SCA. Estimates for rapid prototyping programs that do not exceed the ACAT I threshold must be conducted in accordance with guidance issued by the relevant SCA. (2) Rapid Fielding Programs. CAPE will conduct an estimate of life-cycle costs for programs likely to exceed ACAT I or II thresholds pursued using the MTA rapid fielding pathway. CAPE may, in its discretion, delegate the authority for the conduct of the cost estimate to the SCA. DoD Components must conduct life-cycle cost estimates for rapid fielding programs that do not exceed the ACAT II threshold in accordance with guidance issued by the relevant SCA.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S26 · Information Support Plan (ISP)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DoD Component or as delegated
- Source: DoDI 8330.01 DoDI 8320.02 DoDI 8410.03
- AAFDID note: Regulatory. Applicable to all IT, including NSS. An updated ISP of record may be required during O&S. Enter data on-line at https://gtg.csd.disa.mil/ (requires an account and login with CAC).
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S27 · Information Technology and National Security System Interoperability Certification

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: JITC or DoD Component
- Source: DoDI 5000.80 DoDI 8330.01
- AAFDID note: Regulatory. Applicable to all IT, including NSS. Testing completed before or during OT&E. The Joint Interoperability Test Command (JITC) certifies interoperability of IT with joint, multinational, and/or interagency interoperability requirements. DoD Components certify all other IT. Certification must occur prior to deployment.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S28 · LIFECYCLE SUSTAINMENT PLAN (LCSP)/PRODUCT SUPPORT STRATEGY (PSS)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Statutory and regulatory. AAFDID TYPE: Regulatory, Statutory
- Approval: CAE or designee
- Source: 10 U.S.C 4324 {formerly 2337} DoDI 5000.80 DoDI 5000.91
- AAFDID note: STATUTORY for “covered systems” before a decision to enter into system development and demonstration. The LCSP/PSS satisfies the statutory requirements of Section 4324 of Title 10 U.S.C. See DoDI 5000.91 for details about the LCSP/PSS . The PSM will support the PM in developing and implementing the LCSP/PSS (or a tailored LCSP for non-covered systems). The LCSP/PSS has required annexes that are reflective of the program's latest planned and completed activities tied to a program's life-cycle sustainment that correlate with statute. The following requirements will be satisfied in the LCSP/PSS: PRODUCT SUPPORT BUSINESS CASE ANALYSIS—The BCA and the cost-benefit analyses (CBA) satisfies statutory requirement to conduct appropriate cost, risk, and trades analyses to validate the product support strategy. CORE LOGISTICS DETERMINATION IP STRATEGY—prepared for the acquisition strategy. PRESERVATION AND STORAGE OF UNIQUE TOOLING PLAN PROGRAMMATIC, ENVIRONMENT, SAFETY, AND OCCUPATIONAL HEALTH (ESOH) (PESHE) REPLACED SYSTEM SUSTAINMENT PLAN SOFTWARE PRODUCT SUPPORT STRATEGY System Disposal Plan
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S29 · PESHE AND NEPA/E.O. 12114 COMPLIANCE SCHEDULE (Part of LCSP/PSS)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: DA or designee
- Source: 42 U.S.C. 4321-4347 E.O. 12114
- AAFDID note: STATUTORY. The Programmatic Environment, Safety, and Occupational Health Evaluation (PESHE) and National Environmental Policy Act (NEPA) / Executive Order (E.O.) 12114 Compliance Schedule is approved by the DA or designee. Related design considerations must be included in the SEP; related operations or sustainment considerations will be included in the PSS.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S30 · Program Protection Plan (PPP)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: CAE or designee
- Source: DoDI 5200.39 DoDI 5200.44
- AAFDID note: Regulatory. If applicable, after the Full Rate Production or Full Deployment decision, the PPP will transition to the PM responsible for system sustainment and disposal. The PPP includes appropriate appendixes or links to required information. The official designated by the DoD Component head will be the approval authority.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S31 · Request for Proposal (RFP)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DA is release authority
- Source: Federal Acquisition Regulation (FAR) Subpart 15.203
- AAFDID note: Regulatory. RFPs are issued as necessary; they include specifications, deliverable lists, and statement of work. See also Defense Federal Acquisition Regulation Supplement (DFARS) subpart 201.170 and Class Deviation 2019-O00010, dated August 20, 2019, for peer review requirements. For acquisitions where government property will be provided to a contractor for the performance of a contract, a business case analysis must be performed, demonstrating it is in the government's best interest to provide government property, otherwise the contract could not be performed. In addition, the solicitation and ensuing contract must have the appropriate government property clause and mandatory clauses incorporated. SOURCE: FAR 45.102.b and DFARS 245.103-70.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S32 · Sustainment Review (SR)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For major systems and programs above MDAP thresholds. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `mta_size is one of {major, exceeds_mdap}`
- When due: Not tied to one event
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: CAE
- Source: 10 USC 4323 and 4324
- AAFDID note: SRs begin 5 years after initial operational capability and repeat every 5 years thereafter. Statute only requires sustainment reviews for an MTA program that meets or breaches the MDAP dollar threshold. Submitted to Congress by 30-Sep of the fiscal year conducted.
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

### MTA-S33 · Systems Engineering Plan (SEP)

- Pathway: MTA (Middle Tier of Acquisition). Table: Statutory and Regulatory Requirements that may be applicable.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway. AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.
- Condition code: `always (every program on this pathway)`
- When due: Not tied to one event
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: DA or designee
- Source: DoDI 5000.88 This Table
- Page: https://www.waru.edu/aafdid/MTA-Statutory-Regulatory-Requirements

## EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway)

### EVM-01 · EVMS on contract, < $20M: EVMS not required; may be applied at PM discretion based on risk to the Government

- Pathway: MTA (Middle Tier of Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: May apply.
- Applies when: Cost-reimbursable or incentive contract of 18 months or more, valued < $20M (then-year dollars, including options).
- Condition code: `contract_cost_type = yes AND contract_value < 20,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Part 7 of Office of Management and Budget Circular A- 11 FAR 52.234-4, FAR subpart, 34.2 DFARS 234.201 DoDI 5000.85, Para. 3C.3.c.(3)
- AAFDID note: Requires business case analysis and MDA approval.
- Tool note: Classified as regulatory by this tool: the row cites OMB Circular A-11, the FAR, the DFARS and DoDI 5000.85.
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-02 · EVMS on contract, ≥ $20M &<$100M: EVMS Required; Contractor is required to have an EVMS that complies with the guidelines in EIA-748.*

- Pathway: MTA (Middle Tier of Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Cost-reimbursable or incentive contract of 18 months or more, valued ≥ $20M &<$100M (then-year dollars, including options).
- Condition code: `contract_cost_type = yes AND contract_value >= 20,000,000 AND contract_value < 100,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Part 7 of Office of Management and Budget Circular A- 11 FAR 52.234-4, FAR subpart, 34.2 DFARS 234.201 DoDI 5000.85, Para. 3C.3.c.(3)
- AAFDID note: The Government reserves the right to review a contractor’s EVMS when deemed necessary to verify compliance.
- Tool note: Classified as regulatory by this tool: the row cites OMB Circular A-11, the FAR, the DFARS and DoDI 5000.85.
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-03 · EVMS on contract, ≥ $100M: EVMS Required; Contractor is required to have an EVMS that has been determined to be in compliance with the guidelines in EIA-748.*

- Pathway: MTA (Middle Tier of Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Cost-reimbursable or incentive contract of 18 months or more, valued ≥ $100M (then-year dollars, including options).
- Condition code: `contract_cost_type = yes AND contract_value >= 100,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Part 7 of Office of Management and Budget Circular A- 11 FAR 52.234-4, FAR subpart, 34.2 DFARS 234.201 DoDI 5000.85, Para. 3C.3.c.(3)
- AAFDID note: The Contractor will provide access to all pertinent records and data requested by the Contracting Officer or duly authorized representative as necessary to permit initial and ongoing Government compliance reviews to ensure that the EVMS complies, and continues to comply, with the guidelines in EIA-748.*
- Tool note: Classified as regulatory by this tool: the row cites OMB Circular A-11, the FAR, the DFARS and DoDI 5000.85.
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-04 · IPMDAR (DI-MGMT-81861), < $20M: Not required

- Pathway: MTA (Middle Tier of Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: May apply.
- Applies when: Contracts under $20M: not required. The PMO may request IPMDAR cost or schedule reporting.
- Condition code: `contract_value < 20,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Integrated Program Management Data and Analysis Report (IPMDAR) DID DI-MGMT-81861
- AAFDID note: Integrated Program Management Data and Analysis Report (IPMDAR) may be used if cost and/or schedule reporting is requested by the program management office.
- Tool note: Classified as regulatory by this tool (DoDI 5000.85; DI-MGMT-81861).
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-05 · IPMDAR (DI-MGMT-81861), ≥ $20M & < $100M: Required monthly when EVMS requirement is on contract

- Pathway: MTA (Middle Tier of Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Monthly when an EVMS requirement is on contract ($20M to under $100M).
- Condition code: `contract_cost_type = yes AND contract_value >= 20,000,000 AND contract_value < 100,000,000`
- When due: Monthly
- Type: Regulatory.
- Source: Integrated Program Management Data and Analysis Report (IPMDAR) DID DI-MGMT-81861
- AAFDID note: All IPMDAR datasets/files must be included in the CDRL. Tailoring in accordance with DI-MGMT-81861 and Implementation Guide is allowed.
- Tool note: Classified as regulatory by this tool (DoDI 5000.85; DI-MGMT-81861).
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-06 · IPMDAR (DI-MGMT-81861), ≥ $100M: Required monthly when EVMS requirement is on contract

- Pathway: MTA (Middle Tier of Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Monthly when an EVMS requirement is on contract ($100M or more).
- Condition code: `contract_cost_type = yes AND contract_value >= 100,000,000`
- When due: Monthly
- Type: Regulatory.
- Source: Integrated Program Management Data and Analysis Report (IPMDAR) DID DI-MGMT-81861
- AAFDID note: IPMDAR is required. All files are required.
- Tool note: Classified as regulatory by this tool (DoDI 5000.85; DI-MGMT-81861).
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements


---

# UCA requirements: Urgent Capability Acquisition

Knowledge file 12 of the AAFDID Navigator agent pack, rules 1.0.0. Every record below belongs to the UCA pathway only.

- Governing instruction: DoDI 5000.81
- Summary: Fields capability for urgent operational needs in less than 2 years. Cost may not exceed MDAP thresholds (DoDI 5000.02, para 4.2.a).
- Decision authority: Set under DoDD 5000.71 and DoDI 5000.81; confirm with your component.
- Events, in order: `development` = Development Milestone; `production` = Production and Deployment Milestone; `other` = Other, including disposition
- Note: Documents for each event are due no later than 45 calendar days before the planned review (AAFDID UCA table note).
- Note: AAFDID's UCA overview: documentation may take any appropriate written form and evolves in parallel with the acquisition.
- AAFDID page: https://www.waru.edu/aafdid/uca

## Also review MCA entries

AAFDID's UCA page says to use the ACAT II and III entries of the MCA tables as well, with applicability set by DoDI 5000.81.

For a UCA program, go through the MCA records in 10-mca.md from tables `ms` and `exc` (codes MCA-M.. and MCA-X..):

1. If `uca_acat` is unknown, list none of them. Ask the ACAT question first, because it decides which MCA entries apply.
2. Otherwise test each record's Condition code with `mca_program_type` set to the program's `uca_acat` value (`acat_ii` stays `acat_ii`; `acat_iii` stays `acat_iii`) and every other field from the profile.
3. False: leave the record out. MDAP-only rows always drop out this way.
4. Unknown: list it under Needs an answer, naming the missing field (for example `dote_oversight`).
5. True: list it under "Also review: MCA entries AAFDID points UCA programs to", with status Also review, its MCA code, and its MCA events.

## UCA Unique Information Requirements

### UCA-01 · Assessment Approach

- Pathway: UCA (Urgent Capability Acquisition). Table: UCA Unique Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Development Milestone (initial); Production and Deployment Milestone (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: Section 4172 of Title 10 U.S.C. {formerly 2366} (see DoDI 5000.02); Section 4171 of Title 10 U.S.C. {formerly 2399} (see DoDI 5000.02)
- AAFDID note: STATUTORY; only required for programs responding to urgent capability acquisitions. - For programs under DOT&E oversight, operational and live fire test plans will be submitted to DOT&E for approval at the Development Milestone; post-deployment assessment plans will be submitted to DOT&E for approval at the Production and Deployment Milestone. DOT&E will ensure that testing is rigorous enough to rapidly evaluate critical operational issues. Test Plans submitted for DOT&E approval are required to be delivered 60 days before the start of testing. - Programs not under DOT&E oversight are approved at the Service level; the program may require a rapid and focused operational assessment and live fire testing (if applicable) prior to deploying an urgent need solution. The Acquisition Approach will identify any requirements to evaluate health, safety, operational effectiveness, suitability, environmental factors, supportability and survivability.
- Page: https://www.waru.edu/aafdid/UCA-Unique-Information-Requirements

### UCA-02 · Course of Action Analysis

- Pathway: UCA (Urgent Capability Acquisition). Table: UCA Unique Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Development Milestone (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: Meets the assessment requirements of Subtitle III of Title 40, U.S.C.
- AAFDID note: STATUTORY; replaces and serves as the Analysis of Alternatives. Approved by the MDA. For JUONs, JEONs, critical warfighter issues identified by the Warfighter SIG, and SecDef or DepSecDef RAA determinations, a copy is due to the Executive Director, JRAC, within 3 business days of MDA approval.
- Page: https://www.waru.edu/aafdid/UCA-Unique-Information-Requirements

### UCA-03 · Disposition Authority's Report to the DoD Component Head

- Pathway: UCA (Urgent Capability Acquisition). Table: UCA Unique Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Other, including disposition (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: Para. 4.5.e. of DoDI 5000.81
- AAFDID note: Regulatory. Based on the disposition official’s recommendation in the Disposition Analysis, the Component Head will determine and document the disposition of the initiative and process it in accordance with applicable Component and requirements authority procedures.
- Page: https://www.waru.edu/aafdid/UCA-Unique-Information-Requirements

### UCA-04 · Rapid Acquisition Authority (RAA) Recommendation

- Pathway: UCA (Urgent Capability Acquisition). Table: UCA Unique Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Other, including disposition (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: Section 806(c) of Public Law (PL) 107- 314
- AAFDID note: STATUTORY. Optional request to the SecDef or DepSecDef for RAA. Considered as part of the development of the Acquisition Strategy. MDA approves the decision to request RAA at the Development Milestone.
- Page: https://www.waru.edu/aafdid/UCA-Unique-Information-Requirements

## EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway)

### EVM-01 · EVMS on contract, < $20M: EVMS not required; may be applied at PM discretion based on risk to the Government

- Pathway: UCA (Urgent Capability Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: May apply.
- Applies when: Cost-reimbursable or incentive contract of 18 months or more, valued < $20M (then-year dollars, including options).
- Condition code: `contract_cost_type = yes AND contract_value < 20,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Part 7 of Office of Management and Budget Circular A- 11 FAR 52.234-4, FAR subpart, 34.2 DFARS 234.201 DoDI 5000.85, Para. 3C.3.c.(3)
- AAFDID note: Requires business case analysis and MDA approval.
- Tool note: Classified as regulatory by this tool: the row cites OMB Circular A-11, the FAR, the DFARS and DoDI 5000.85.
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-02 · EVMS on contract, ≥ $20M &<$100M: EVMS Required; Contractor is required to have an EVMS that complies with the guidelines in EIA-748.*

- Pathway: UCA (Urgent Capability Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Cost-reimbursable or incentive contract of 18 months or more, valued ≥ $20M &<$100M (then-year dollars, including options).
- Condition code: `contract_cost_type = yes AND contract_value >= 20,000,000 AND contract_value < 100,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Part 7 of Office of Management and Budget Circular A- 11 FAR 52.234-4, FAR subpart, 34.2 DFARS 234.201 DoDI 5000.85, Para. 3C.3.c.(3)
- AAFDID note: The Government reserves the right to review a contractor’s EVMS when deemed necessary to verify compliance.
- Tool note: Classified as regulatory by this tool: the row cites OMB Circular A-11, the FAR, the DFARS and DoDI 5000.85.
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-03 · EVMS on contract, ≥ $100M: EVMS Required; Contractor is required to have an EVMS that has been determined to be in compliance with the guidelines in EIA-748.*

- Pathway: UCA (Urgent Capability Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Cost-reimbursable or incentive contract of 18 months or more, valued ≥ $100M (then-year dollars, including options).
- Condition code: `contract_cost_type = yes AND contract_value >= 100,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Part 7 of Office of Management and Budget Circular A- 11 FAR 52.234-4, FAR subpart, 34.2 DFARS 234.201 DoDI 5000.85, Para. 3C.3.c.(3)
- AAFDID note: The Contractor will provide access to all pertinent records and data requested by the Contracting Officer or duly authorized representative as necessary to permit initial and ongoing Government compliance reviews to ensure that the EVMS complies, and continues to comply, with the guidelines in EIA-748.*
- Tool note: Classified as regulatory by this tool: the row cites OMB Circular A-11, the FAR, the DFARS and DoDI 5000.85.
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-04 · IPMDAR (DI-MGMT-81861), < $20M: Not required

- Pathway: UCA (Urgent Capability Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: May apply.
- Applies when: Contracts under $20M: not required. The PMO may request IPMDAR cost or schedule reporting.
- Condition code: `contract_value < 20,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Integrated Program Management Data and Analysis Report (IPMDAR) DID DI-MGMT-81861
- AAFDID note: Integrated Program Management Data and Analysis Report (IPMDAR) may be used if cost and/or schedule reporting is requested by the program management office.
- Tool note: Classified as regulatory by this tool (DoDI 5000.85; DI-MGMT-81861).
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-05 · IPMDAR (DI-MGMT-81861), ≥ $20M & < $100M: Required monthly when EVMS requirement is on contract

- Pathway: UCA (Urgent Capability Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Monthly when an EVMS requirement is on contract ($20M to under $100M).
- Condition code: `contract_cost_type = yes AND contract_value >= 20,000,000 AND contract_value < 100,000,000`
- When due: Monthly
- Type: Regulatory.
- Source: Integrated Program Management Data and Analysis Report (IPMDAR) DID DI-MGMT-81861
- AAFDID note: All IPMDAR datasets/files must be included in the CDRL. Tailoring in accordance with DI-MGMT-81861 and Implementation Guide is allowed.
- Tool note: Classified as regulatory by this tool (DoDI 5000.85; DI-MGMT-81861).
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-06 · IPMDAR (DI-MGMT-81861), ≥ $100M: Required monthly when EVMS requirement is on contract

- Pathway: UCA (Urgent Capability Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Monthly when an EVMS requirement is on contract ($100M or more).
- Condition code: `contract_cost_type = yes AND contract_value >= 100,000,000`
- When due: Monthly
- Type: Regulatory.
- Source: Integrated Program Management Data and Analysis Report (IPMDAR) DID DI-MGMT-81861
- AAFDID note: IPMDAR is required. All files are required.
- Tool note: Classified as regulatory by this tool (DoDI 5000.85; DI-MGMT-81861).
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements


---

# SWA requirements: Software Acquisition

Knowledge file 13 of the AAFDID Navigator agent pack, rules 1.0.0. Every record below belongs to the SWA pathway only.

- Governing instruction: DoDI 5000.87; 10 U.S.C. 3603
- Summary: Application and embedded software paths with a planning phase and an execution phase of iterative releases. Programs are not treated as MDAPs, and viability must be shown within 1 year of first obligating funds.
- Decision authority: The component acquisition executive unless USD(A&S) designates a special interest program or delegates otherwise (DoDI 5000.87, para 2.7.c).
- Events, in order: `planning` = Entering the planning phase; `execution_entry` = Entering the execution phase; `execution` = During the execution phase; `each_decision` = Each decision point (due at every one) (not a next event)
- Note: AAFDID calls its SWA table a draft first pass at statute tied to DoDI 5000.87. It does not separate application and embedded programs.
- AAFDID page: https://www.waru.edu/aafdid/swa

## Application and Embedded Software Information Requirements

### SWA-01 · Program Protection Plan

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Each decision point (due at every one) (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.83
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-02 · Acquisition Decision Memorandum (ADM) signed by Decision Authority authorizing use of SWP

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Entering the planning phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-03 · Draft Capability Needs Statement

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Entering the planning phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-04 · Acquisition Strategy (acquisition approach, risk management, business strategy, contract strategy, IP strategy, logistics/sustainment, etc.)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Entering the execution phase (initial)
- Type: Statutory if `swa_above_acat_ii = yes`, otherwise Regulatory. If that is unknown, the type depends on the answer. AAFDID TYPE: Statutory for major programs (> ACAT II) Regulatory for others
- Source: 10 USC 4211 {formerly 2431a} DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-05 · Bandwidth Requirements Review (part of ISP or other related document)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Entering the execution phase (initial)
- Type: Statutory if `swa_above_acat_ii = yes`, otherwise Regulatory. If that is unknown, the type depends on the answer. AAFDID TYPE: Statutory for programs (> ACAT II) Regulatory for Others
- Source: §1047, P.L. 110-417
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-06 · Capability Needs Statement

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Entering the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-07 · Clinger Cohen Act (CCA) Compliance (see CCA table)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Entering the execution phase (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: DoDI 5000.82 Subtitle III of Title 40
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-08 · Cost Analysis Requirements Document

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Entering the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.73
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-09 · Cybersecurity Strategy (may be part of Acquisition Strategy or standalone document)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Entering the execution phase (initial)
- Type: Statutory if `mission_critical_it = yes`, otherwise Regulatory. If that is unknown, the type depends on the answer. AAFDID TYPE: Statutory for Mission Critical and Mission Essential IT programs, Regulatory for others
- Source: 40 USC 11313, DoDI 5000.87, DoDI 8500.01, DoDI 5000.82
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-10 · Information Support Plan

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Entering the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 8330.01
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-11 · Intellectual Property Strategy (may be part of Acquisition Strategy)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Entering the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-12 · Market Research (Part of Acquisition Strategy)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Entering the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: 10 USC 3453 {formerly 2377}, 41 USC 3306(a)(1), 41 USC 3307(d)
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-13 · Product Support Strategy including Business Case Analysis (may be part of Acquisition Strategy)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Entering the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-14 · Program Cost Estimate and Independent Cost Estimate

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Entering the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: CAPE ICE for programs > ACAT II unless delegated
- Source: DoDI 5000.87 DoDI 5000.73
- Tool note: AAFDID's TYPE cell reads 'CAPE ICE for programs > ACAT II unless delegated'. This tool classifies the row as regulatory (DoDI 5000.87, 5000.73).
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-15 · Test Strategy (may be part of Acquisition Strategy)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Entering the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory Programs on DOT&E Oversight list may require a TEMP
- Source: DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-16 · User Agreement

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Entering the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-17 · Clinger Cohen Act (CCA) Compliance (see CCA table)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: During the execution phase (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: DoDI 5000.82 Subtitle III of Title 40
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-18 · Contractor Business Data Report (CTRs with $250M)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: May apply.
- Applies when: Contractors with $250M or more in CSDR contracts (threshold in AAFDID's row name).
- Condition code: `always (every program on this pathway)`
- When due: During the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.73
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-19 · Contractor Cost Data Report ($100M+ contracts)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required (contract-level).
- Applies when: Contracts of $100M or more.
- Condition code: `contract_value >= 100,000,000`
- When due: During the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.73
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-20 · Core Logistics Determination (CLD)/Core Logistics and Sustaining Workloads Estimate (CLSWE)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: When it needs government software maintenance.
- Condition code: `software_maintenance = yes`
- When due: During the execution phase (initial)
- Type: Statutory. AAFDID TYPE: Statutory for programs with “software maintenance"
- Source: 10 USC 2464
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-21 · DOT&E Report on Initial Operational Test and Evaluation (IOT&E)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: When it is on the DOT&E oversight list.
- Condition code: `dote_oversight = yes`
- When due: During the execution phase (initial)
- Type: Statutory. AAFDID TYPE: Statutory for programs on the DOT&E Oversight List
- Source: 10 USC 4171 {formerly 2399} 10 USC 139
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-22 · Maintenance and Repair Parts Data Report ($100M+ Programs)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: May apply.
- Applies when: Programs of $100M or more (threshold in AAFDID's row name).
- Condition code: `always (every program on this pathway)`
- When due: During the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.73
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-23 · Operational Test Plan

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: During the execution phase (initial)
- Type: Statutory if `dote_oversight = yes`, otherwise Regulatory. If that is unknown, the type depends on the answer. AAFDID TYPE: Statutory for programs on the DOT&E Oversight List
- Source: 10 USC 4171 {formerly 2399}
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-24 · Periodic updates to cost estimate and CARD

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: During the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-25 · Periodic updates to strategies (acquisition, contracting, test, cybersecurity, IP, product support)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: During the execution phase (initial)
- Type: Statutory and regulatory. AAFDID TYPE: Statutory/ Regulatory
- Source: DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-26 · Post Implementation Review

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: During the execution phase (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: 40 USC 11313 DoDI 5000.82
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-27 · Product Roadmap or equivalent

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: During the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-28 · Program Backlog or equivalent

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: During the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-29 · Program Metrics

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: During the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-30 · Semi-Annual Data Reporting to OUSD(A&S)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: During the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-31 · Software Resources Data Report ($100M+ Programs)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: May apply.
- Applies when: Programs of $100M or more (threshold in AAFDID's row name).
- Condition code: `always (every program on this pathway)`
- When due: During the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.73
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-32 · System Architecture

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: During the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-33 · Technical Data Report ($100M+ Programs)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: May apply.
- Applies when: Programs of $100M or more (threshold in AAFDID's row name).
- Condition code: `always (every program on this pathway)`
- When due: During the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.73
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

### SWA-34 · Value Assessment (at least annually)

- Pathway: SWA (Software Acquisition). Table: Application and Embedded Software Information Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: During the execution phase (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Source: DoDI 5000.87
- Page: https://www.waru.edu/aafdid/SWA-Application-and-Embedded-SW-Information-Requirements

## SWA Clinger-Cohen Act Compliance

### SWA-C01 · CCA: Conduct an analysis of alternatives

- Pathway: SWA (Software Acquisition). Table: SWA Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Report with the CCA compliance entries in the SWA table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: Acquisition Strategy (Business Strategy section).
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's SWA CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/SWA-Clinger-Cohen-Act-Compliance

### SWA-C02 · CCA: Conduct an economic analysis that includes a calculation of the return on investment; or for non-AIS programs, conduct a life-cycle cost estimate.

- Pathway: SWA (Software Acquisition). Table: SWA Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Report with the CCA compliance entries in the SWA table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: Component Cost Estimate, Component Cost Position.
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's SWA CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/SWA-Clinger-Cohen-Act-Compliance

### SWA-C03 · CCA: Determination that the acquisition supports core, priority functions of the DoD.

- Pathway: SWA (Software Acquisition). Table: SWA Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Report with the CCA compliance entries in the SWA table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: Capability Needs Statement (Capabilities section).
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's SWA CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/SWA-Clinger-Cohen-Act-Compliance

### SWA-C04 · CCA: Determine that no private sector or government source can better support the function

- Pathway: SWA (Software Acquisition). Table: SWA Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Report with the CCA compliance entries in the SWA table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: Acquisition Strategy.
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's SWA CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/SWA-Clinger-Cohen-Act-Compliance

### SWA-C05 · CCA: Develop clearly established measures and accountability for program progress.

- Pathway: SWA (Software Acquisition). Table: SWA Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Report with the CCA compliance entries in the SWA table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: Acquisition Strategy (Program Metrics, Value Assessment).
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's SWA CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/SWA-Clinger-Cohen-Act-Compliance

### SWA-C06 · CCA: Ensure that the acquisition is consistent with the DoD Information Enterprise policies and architecture, to include relevant standards.

- Pathway: SWA (Software Acquisition). Table: SWA Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Report with the CCA compliance entries in the SWA table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: System Architecture.
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's SWA CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/SWA-Clinger-Cohen-Act-Compliance

### SWA-C07 · CCA: Ensure that the program has a Cybersecurity Strategy that is consistent with DoD policies, standards and architectures, to include relevant standards.

- Pathway: SWA (Software Acquisition). Table: SWA Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Report with the CCA compliance entries in the SWA table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: Cybersecurity Strategy.
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's SWA CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/SWA-Clinger-Cohen-Act-Compliance

### SWA-C08 · CCA: Ensure, to the maximum extent practicable, (1) modular contracting has been used, and (2) the program is being implemented in phased, successive increments, each of which meets part of the mission need and delivers measurable benefit, independent of....

- Pathway: SWA (Software Acquisition). Table: SWA Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Report with the CCA compliance entries in the SWA table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: Acquisition Strategy (Contracting Strategy section).
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's SWA CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/SWA-Clinger-Cohen-Act-Compliance

### SWA-C09 · CCA: Establish outcome-based performance measures linked to strategic goals

- Pathway: SWA (Software Acquisition). Table: SWA Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Report with the CCA compliance entries in the SWA table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: Capability Needs Statement (Performance Attributes section).
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's SWA CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/SWA-Clinger-Cohen-Act-Compliance

### SWA-C10 · CCA: Redesign the processes that the system supports to reduce costs, improve effectiveness and maximize the use of commercial off-the-shelf technology.

- Pathway: SWA (Software Acquisition). Table: SWA Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Report with the CCA compliance entries in the SWA table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: Capability Needs Statement (Program Summary section).
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's SWA CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/SWA-Clinger-Cohen-Act-Compliance

### SWA-C11 · CCA: Register Mission-Critical and Mission-Essential systems with the DoD CIO.

- Pathway: SWA (Software Acquisition). Table: SWA Clinger-Cohen Act Compliance.
- Status when the condition holds: Required (compliance action).
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Report with the CCA compliance entries in the SWA table.
- Type: Statutory.
- Source: Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82
- AAFDID note: Evidenced by: DoD Information Technology Portfolio Repository.
- Tool note: Classified as statutory by this tool: the actions implement the Clinger-Cohen Act (40 U.S.C. Subtitle III). AAFDID's SWA CCA table has no TYPE column.
- Page: https://www.waru.edu/aafdid/SWA-Clinger-Cohen-Act-Compliance

## EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway)

### EVM-01 · EVMS on contract, < $20M: EVMS not required; may be applied at PM discretion based on risk to the Government

- Pathway: SWA (Software Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: May apply.
- Applies when: Cost-reimbursable or incentive contract of 18 months or more, valued < $20M (then-year dollars, including options).
- Condition code: `contract_cost_type = yes AND contract_value < 20,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Part 7 of Office of Management and Budget Circular A- 11 FAR 52.234-4, FAR subpart, 34.2 DFARS 234.201 DoDI 5000.85, Para. 3C.3.c.(3)
- AAFDID note: Requires business case analysis and MDA approval.
- Tool note: Classified as regulatory by this tool: the row cites OMB Circular A-11, the FAR, the DFARS and DoDI 5000.85.
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-02 · EVMS on contract, ≥ $20M &<$100M: EVMS Required; Contractor is required to have an EVMS that complies with the guidelines in EIA-748.*

- Pathway: SWA (Software Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Cost-reimbursable or incentive contract of 18 months or more, valued ≥ $20M &<$100M (then-year dollars, including options).
- Condition code: `contract_cost_type = yes AND contract_value >= 20,000,000 AND contract_value < 100,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Part 7 of Office of Management and Budget Circular A- 11 FAR 52.234-4, FAR subpart, 34.2 DFARS 234.201 DoDI 5000.85, Para. 3C.3.c.(3)
- AAFDID note: The Government reserves the right to review a contractor’s EVMS when deemed necessary to verify compliance.
- Tool note: Classified as regulatory by this tool: the row cites OMB Circular A-11, the FAR, the DFARS and DoDI 5000.85.
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-03 · EVMS on contract, ≥ $100M: EVMS Required; Contractor is required to have an EVMS that has been determined to be in compliance with the guidelines in EIA-748.*

- Pathway: SWA (Software Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Cost-reimbursable or incentive contract of 18 months or more, valued ≥ $100M (then-year dollars, including options).
- Condition code: `contract_cost_type = yes AND contract_value >= 100,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Part 7 of Office of Management and Budget Circular A- 11 FAR 52.234-4, FAR subpart, 34.2 DFARS 234.201 DoDI 5000.85, Para. 3C.3.c.(3)
- AAFDID note: The Contractor will provide access to all pertinent records and data requested by the Contracting Officer or duly authorized representative as necessary to permit initial and ongoing Government compliance reviews to ensure that the EVMS complies, and continues to comply, with the guidelines in EIA-748.*
- Tool note: Classified as regulatory by this tool: the row cites OMB Circular A-11, the FAR, the DFARS and DoDI 5000.85.
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-04 · IPMDAR (DI-MGMT-81861), < $20M: Not required

- Pathway: SWA (Software Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: May apply.
- Applies when: Contracts under $20M: not required. The PMO may request IPMDAR cost or schedule reporting.
- Condition code: `contract_value < 20,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Integrated Program Management Data and Analysis Report (IPMDAR) DID DI-MGMT-81861
- AAFDID note: Integrated Program Management Data and Analysis Report (IPMDAR) may be used if cost and/or schedule reporting is requested by the program management office.
- Tool note: Classified as regulatory by this tool (DoDI 5000.85; DI-MGMT-81861).
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-05 · IPMDAR (DI-MGMT-81861), ≥ $20M & < $100M: Required monthly when EVMS requirement is on contract

- Pathway: SWA (Software Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Monthly when an EVMS requirement is on contract ($20M to under $100M).
- Condition code: `contract_cost_type = yes AND contract_value >= 20,000,000 AND contract_value < 100,000,000`
- When due: Monthly
- Type: Regulatory.
- Source: Integrated Program Management Data and Analysis Report (IPMDAR) DID DI-MGMT-81861
- AAFDID note: All IPMDAR datasets/files must be included in the CDRL. Tailoring in accordance with DI-MGMT-81861 and Implementation Guide is allowed.
- Tool note: Classified as regulatory by this tool (DoDI 5000.85; DI-MGMT-81861).
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-06 · IPMDAR (DI-MGMT-81861), ≥ $100M: Required monthly when EVMS requirement is on contract

- Pathway: SWA (Software Acquisition). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Monthly when an EVMS requirement is on contract ($100M or more).
- Condition code: `contract_cost_type = yes AND contract_value >= 100,000,000`
- When due: Monthly
- Type: Regulatory.
- Source: Integrated Program Management Data and Analysis Report (IPMDAR) DID DI-MGMT-81861
- AAFDID note: IPMDAR is required. All files are required.
- Tool note: Classified as regulatory by this tool (DoDI 5000.85; DI-MGMT-81861).
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements


---

# DBS requirements: Defense Business Systems

Knowledge file 14 of the AAFDID Navigator agent pack, rules 1.0.0. Every record below belongs to the DBS pathway only.

- Governing instruction: DoDI 5000.75
- Summary: Business systems for finance, contracting, logistics, human resources and similar functions. They move through the Business Capability Acquisition Cycle and its Authority to Proceed (ATP) decision points.
- Decision authority: Set by DoDI 5000.75; confirm with your component.
- Events, in order: `solution_analysis_atp` = Solution Analysis ATP; `functional_requirements_atp` = Functional Requirements ATP; `acquisition_atp` = Acquisition ATP; `contract_award` = Contract award; `limited_deployment_atp` = Limited Deployment ATP(s); `full_deployment_atp` = Full Deployment ATP; `capability_support_atp` = Capability Support ATP
- Note: AAFDID's DBS overview: information supporting requirements validation and the annual investment certification cannot be tailored.
- Note: AAFDID prints the Limited and Full Deployment ATPs under the Functional Requirements and Acquisition Planning phase. This tool keeps AAFDID's wording.
- AAFDID page: https://www.waru.edu/aafdid/dbs

## Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs

### CSDR-01 · Contractor Business Data Report

- Pathway: DBS (Defense Business Systems). Table: Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs.
- Status when the condition holds: May apply.
- Applies when: ACAT I and II programs and IS programs (including DBS) whose contractor business unit holds CSDR contracts expected to exceed $250M then-year. Not for business units whose only CSDR contracts are MTA contracts.
- Condition code: `(pathway = mca AND mca_program_type is one of {mdap, mais, acat_ii}) OR pathway = dbs`
- When due: Per the approved CSDR plan.
- Type: Regulatory.
- Source: DoDI 5000.73
- AAFDID note: Required for contractor business entities (e.g., plant, site, or business unit) responsible for contracts or subcontracts with CSDR requirements that are expected to exceed $250 million, then-year dollars. Not required for business units based solely on CSDR requirement Middle Tier Acquisition Program contracts.
- Tool note: Classified as regulatory by this tool (DoDI 5000.73). Program value above $100M is not asked, so IS and non-major MTA programs show these as may apply.
- Page: https://www.waru.edu/aafdid/Cost-Data-Reporting-Requirements

### CSDR-02 · Contractor Cost Data Report

- Pathway: DBS (Defense Business Systems). Table: Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs.
- Status when the condition holds: Required (contract-level).
- Applies when: ACAT I and II programs: contracts over $50M, or $20M to $50M at the CSDR plan authority's discretion. MTA programs over $100M: contracts over $20M. IS programs over $100M, including DBS: contracts over $50M. All then-year dollars.
- Condition code: `(pathway = mca AND mca_program_type is one of {mdap, mais, acat_ii} AND contract_value > 50,000,000) OR (pathway = mta AND mta_size is one of {major, exceeds_mdap} AND contract_value > 20,000,000)`
- May apply instead when: `(pathway = mca AND mca_program_type is one of {mdap, mais, acat_ii} AND contract_value > 20,000,000 AND contract_value <= 50,000,000) OR (pathway = mta AND mta_size = non_major AND contract_value > 20,000,000) OR (pathway = dbs AND contract_value > 20,000,000)`
- When due: Per the approved CSDR plan.
- Type: Regulatory.
- Source: DoDI 5000.73
- AAFDID note: Acat i ii programs: All contracts, subcontracts, government-performed efforts, and major components (e.g., government furnished equipment), including FMS and programs in sustainment, regardless of acquisition phase and contract type, including non-FAR agreements, valued at more than $50 million, then-year dollars, for current and former ACAT I – II programs. High-risk or high-technical-interest, as determined by the CSDR plan approval authority, or software contracts priced between $20 million and $50 million, then-year dollars. Information system programs: All contracts, subcontracts, government-performed efforts, and major components (e.g., government furnished equipment), regardless of acquisition phase and contract type, including non-FAR agreements, valued at more than $50 million, then-year dollars, for IS programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures. High-risk or high-technical-interest, as determined by the CSDR plan approval authority, or software contracts priced between $20 million and $50 million, then-year dollars. Middle tier acquisition programs: All contracts, subcontracts, government-performed efforts, and major components (e.g., government furnished equipment), regardless of acquisition phase and contract type, including non-FAR agreements, valued at more than $20 million, then-year dollars, for Middle Tier Acquisition Programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures. Other programs gt 100m: May be required at the discretion of the CSDR approval authority for all high interest or high-risk contracts, subcontracts, or government-performed efforts. Not required: Contracts on programs with anticipated acquisition expenditures less than $100 million, then-year dollars. Contracts priced below $20 million, then-year dollars. PM requests and obtains approval from the DDCA for a reporting waiver (e.g., procurement of commercial systems).
- Tool note: Classified as regulatory by this tool (DoDI 5000.73). Program value above $100M is not asked, so IS and non-major MTA programs show these as may apply.
- Page: https://www.waru.edu/aafdid/Cost-Data-Reporting-Requirements

### CSDR-03 · Maintenance and Repair Parts Data Report

- Pathway: DBS (Defense Business Systems). Table: Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs.
- Status when the condition holds: May apply.
- Applies when: Sustainment contracts over $50M for ACAT I and II programs and IS programs over $100M, when the PM cannot provide equivalent data, at the CSDR plan authority's discretion.
- Condition code: `(pathway = mca AND mca_program_type is one of {mdap, mais, acat_ii} AND contract_value > 50,000,000) OR (pathway = dbs AND contract_value > 50,000,000)`
- When due: Per the approved CSDR plan.
- Type: Regulatory.
- Source: DoDI 5000.73
- AAFDID note: All sustainment contracts, government-performed efforts, and major components (e.g., government furnished equipment), regardless of contract type, including non-FAR agreements, valued at more than $50 million, then-year dollars, for programs that exceed ACAT I-II level thresholds and IS programs that are anticipated to exceed $100 million, then-year dollars, when equivalent information cannot be provided by the program manager, at the discretion of the CSDR plan approval authority.
- Tool note: Classified as regulatory by this tool (DoDI 5000.73). Program value above $100M is not asked, so IS and non-major MTA programs show these as may apply.
- Page: https://www.waru.edu/aafdid/Cost-Data-Reporting-Requirements

### CSDR-05 · Software Resources Data Report

- Pathway: DBS (Defense Business Systems). Table: Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs.
- Status when the condition holds: May apply.
- Applies when: Software development, production or maintenance efforts over $20M then-year for ACAT I and II programs, IS programs over $100M (including DBS) and MTA programs over $100M.
- Condition code: `(pathway = mca AND mca_program_type is one of {mdap, mais, acat_ii} AND contract_value > 20,000,000) OR (pathway = mta AND contract_value > 20,000,000) OR (pathway = dbs AND contract_value > 20,000,000)`
- When due: Per the approved CSDR plan.
- Type: Regulatory.
- Source: DoDI 5000.73
- AAFDID note: Development and erp efforts: All contracts, subcontracts, and government-performed efforts, regardless of acquisition phase and contract type, including non-FAR agreements, for developing and/or producing software valued at more than $20 million, then-year dollars, for: Programs that exceed the ACAT I-II level thresholds. IS programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures. All contracts, subcontracts, government-performed efforts, and major components (e.g., government furnished equipment), regardless of acquisition phase and contract type, including non-FAR agreements, valued at more than $20 million, then-year dollars, for Middle Tier Acquisition Programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures. High-risk or high-technical-interest software efforts estimated below $20 million, then-year dollars, as determined by the CSDR plan approval authority, if the overall effort inclusive of non-software efforts exceeds $20 million, then-year dollars. Maintenance efforts: For all contracts, subcontracts, and government-performed efforts, regardless of acquisition phase and contract type, including non-FAR agreements, for: Programs with previous SRDR development or enterprise resource planning requirements or software maintenance efforts of more than $20 million, then-year dollars. Programs that exceed the ACAT I-II level thresholds. IS programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures.
- Tool note: Classified as regulatory by this tool (DoDI 5000.73). Program value above $100M is not asked, so IS and non-major MTA programs show these as may apply.
- Page: https://www.waru.edu/aafdid/Cost-Data-Reporting-Requirements

### CSDR-06 · Technical Data Report

- Pathway: DBS (Defense Business Systems). Table: Cost Data Reporting Requirements (CSDR): ACAT I-II, IS and MTA programs.
- Status when the condition holds: May apply.
- Applies when: Contracts over $50M for ACAT I and II programs and IS programs over $100M, when the PM cannot provide equivalent data, at the CSDR plan authority's discretion.
- Condition code: `(pathway = mca AND mca_program_type is one of {mdap, mais, acat_ii} AND contract_value > 50,000,000) OR (pathway = dbs AND contract_value > 50,000,000)`
- When due: Per the approved CSDR plan.
- Type: Regulatory.
- Source: DoDI 5000.73
- AAFDID note: All contracts, government-performed efforts, and major components (e.g., government furnished equipment), regardless of acquisition phase and contract type, including non-FAR agreements, valued at more than $50 million, then-year dollars, for programs that exceed the ACAT I and II level threshold and IS programs anticipated to exceed $100 million, then-year dollars, in acquisition expenditures when equivalent information cannot be provided by the program manager, at the discretion of the CSDR plan approval authority.
- Tool note: Classified as regulatory by this tool (DoDI 5000.73). Program value above $100M is not asked, so IS and non-major MTA programs show these as may apply.
- Page: https://www.waru.edu/aafdid/Cost-Data-Reporting-Requirements

## DBS Statutory Requirements

### DBS-01 · Business Enterprise Architecture

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Solution Analysis ATP (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: 10 USC 2222(g) (B)
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

### DBS-02 · Capability Requirements

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Solution Analysis ATP (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: 10 USC 2222(d) (2)
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

### DBS-03 · Business Process Reengineering

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Functional Requirements ATP (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: 10 USC 2222(g) (A)
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

### DBS-04 · CMO Certification

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: May apply.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Acquisition ATP (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: 10 USC 2222
- Footnote: CMO certification can occur during prior phases, but must occur before the Acquisition ATP is approved.
- Footnote: SEC 901 of the 2021 NDAA repealed the CMO position; awaiting the decision on the transfer of the CMO duties and responsibilities.
- Changed since AAFDID (Chief Management Officer repealed): see 20-changes-since-aafdid.md, note cmo-2021.
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

### DBS-05 · Solution Approach (fulfills market research, analysis of alternatives, economic analysis)

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Acquisition ATP (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: 10 USC 2222(g) (C) for market research
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

### DBS-06 · Cybersecurity Strategy (for mission essential and mission critical IT)

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: Required.
- Applies when: When it is mission-critical or mission-essential IT.
- Condition code: `mission_critical_it = yes`
- When due: Acquisition ATP (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: Federal Information Security Modernization Act
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

### DBS-07 · Acquisition Strategy

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Acquisition ATP (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: 10 USC 2222(g) (1)(D)
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

### DBS-08 · Clinger-Cohen Act Compliance - Information Technology Management

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Acquisition ATP (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: Title 40, Subtitle III (Division D, E)
- Footnote: Full CCA compliance can occur during prior ATP decisions points, but must occur no later than the first Limited Deployment ATP. Separate documentation should not be needed to confirm CCA compliance.
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

### DBS-09 · Auditability Compliance

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Acquisition ATP (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: 10 USC 2222(g)(1)(E); 10 USC Chapter 9A; Federal Financial Management Improvement Act
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

### DBS-10 · Clinger-Cohen Act Compliance

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Contract award (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: Title 40, Subtitle III (Division D, E)
- Footnote: Full CCA compliance can occur during prior ATP decisions points, but must occur no later than the first Limited Deployment ATP. Separate documentation should not be needed to confirm CCA compliance.
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

### DBS-11 · Full CCA compliance at first Limited Deployment ATP ; confirmation of compliance at additional ATPs

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Limited Deployment ATP(s) (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: Title 40, Subtitle III (Division D, E)
- Footnote: Full CCA compliance can occur during prior ATP decisions points, but must occur no later than the first Limited Deployment ATP. Separate documentation should not be needed to confirm CCA compliance.
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

### DBS-12 · Confirmation of CCA compliance; Initial Operational Test and Evaluation Report (for business systems on the DOT&E oversight list)

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: Required.
- Applies when: For every defense business system. The IOT&E report part applies to business systems on the DOT&E oversight list.
- Condition code: `always (every program on this pathway)`
- When due: Full Deployment ATP (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: Title 40, Subtitle III (Division D, E)
- Footnote: Full CCA compliance can occur during prior ATP decisions points, but must occur no later than the first Limited Deployment ATP. Separate documentation should not be needed to confirm CCA compliance.
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

### DBS-13 · Capability Support Plan

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Capability Support ATP (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: 10 USC 2222(b) (4) sustainment strategy
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

### DBS-14 · DOT&E Report on IOT&E (for programs on DOT&E oversight list)

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: Required.
- Applies when: When it is on the DOT&E oversight list.
- Condition code: `dote_oversight = yes`
- When due: Capability Support ATP (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: 10 USC 139
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

### DBS-15 · Test and Evaluation Master Plan (for programs on DOT&E oversight list)

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: Required.
- Applies when: When it is on the DOT&E oversight list.
- Condition code: `dote_oversight = yes`
- When due: Capability Support ATP (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: 10 USC 139
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

### DBS-16 · Operational Test Plan (for programs on DOT&E oversight list)

- Pathway: DBS (Defense Business Systems). Table: DBS Statutory Requirements.
- Status when the condition holds: Required.
- Applies when: When it is on the DOT&E oversight list.
- Condition code: `dote_oversight = yes`
- When due: Capability Support ATP (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Source: 10 USC 139
- Page: https://www.waru.edu/aafdid/DBS-Statutory-Requirements

## EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway)

### EVM-01 · EVMS on contract, < $20M: EVMS not required; may be applied at PM discretion based on risk to the Government

- Pathway: DBS (Defense Business Systems). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: May apply.
- Applies when: Cost-reimbursable or incentive contract of 18 months or more, valued < $20M (then-year dollars, including options).
- Condition code: `contract_cost_type = yes AND contract_value < 20,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Part 7 of Office of Management and Budget Circular A- 11 FAR 52.234-4, FAR subpart, 34.2 DFARS 234.201 DoDI 5000.85, Para. 3C.3.c.(3)
- AAFDID note: Requires business case analysis and MDA approval.
- Tool note: Classified as regulatory by this tool: the row cites OMB Circular A-11, the FAR, the DFARS and DoDI 5000.85.
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-02 · EVMS on contract, ≥ $20M &<$100M: EVMS Required; Contractor is required to have an EVMS that complies with the guidelines in EIA-748.*

- Pathway: DBS (Defense Business Systems). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Cost-reimbursable or incentive contract of 18 months or more, valued ≥ $20M &<$100M (then-year dollars, including options).
- Condition code: `contract_cost_type = yes AND contract_value >= 20,000,000 AND contract_value < 100,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Part 7 of Office of Management and Budget Circular A- 11 FAR 52.234-4, FAR subpart, 34.2 DFARS 234.201 DoDI 5000.85, Para. 3C.3.c.(3)
- AAFDID note: The Government reserves the right to review a contractor’s EVMS when deemed necessary to verify compliance.
- Tool note: Classified as regulatory by this tool: the row cites OMB Circular A-11, the FAR, the DFARS and DoDI 5000.85.
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-03 · EVMS on contract, ≥ $100M: EVMS Required; Contractor is required to have an EVMS that has been determined to be in compliance with the guidelines in EIA-748.*

- Pathway: DBS (Defense Business Systems). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Cost-reimbursable or incentive contract of 18 months or more, valued ≥ $100M (then-year dollars, including options).
- Condition code: `contract_cost_type = yes AND contract_value >= 100,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Part 7 of Office of Management and Budget Circular A- 11 FAR 52.234-4, FAR subpart, 34.2 DFARS 234.201 DoDI 5000.85, Para. 3C.3.c.(3)
- AAFDID note: The Contractor will provide access to all pertinent records and data requested by the Contracting Officer or duly authorized representative as necessary to permit initial and ongoing Government compliance reviews to ensure that the EVMS complies, and continues to comply, with the guidelines in EIA-748.*
- Tool note: Classified as regulatory by this tool: the row cites OMB Circular A-11, the FAR, the DFARS and DoDI 5000.85.
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-04 · IPMDAR (DI-MGMT-81861), < $20M: Not required

- Pathway: DBS (Defense Business Systems). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: May apply.
- Applies when: Contracts under $20M: not required. The PMO may request IPMDAR cost or schedule reporting.
- Condition code: `contract_value < 20,000,000`
- When due: Not tied to one event
- Type: Regulatory.
- Source: Integrated Program Management Data and Analysis Report (IPMDAR) DID DI-MGMT-81861
- AAFDID note: Integrated Program Management Data and Analysis Report (IPMDAR) may be used if cost and/or schedule reporting is requested by the program management office.
- Tool note: Classified as regulatory by this tool (DoDI 5000.85; DI-MGMT-81861).
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-05 · IPMDAR (DI-MGMT-81861), ≥ $20M & < $100M: Required monthly when EVMS requirement is on contract

- Pathway: DBS (Defense Business Systems). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Monthly when an EVMS requirement is on contract ($20M to under $100M).
- Condition code: `contract_cost_type = yes AND contract_value >= 20,000,000 AND contract_value < 100,000,000`
- When due: Monthly
- Type: Regulatory.
- Source: Integrated Program Management Data and Analysis Report (IPMDAR) DID DI-MGMT-81861
- AAFDID note: All IPMDAR datasets/files must be included in the CDRL. Tailoring in accordance with DI-MGMT-81861 and Implementation Guide is allowed.
- Tool note: Classified as regulatory by this tool (DoDI 5000.85; DI-MGMT-81861).
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements

### EVM-06 · IPMDAR (DI-MGMT-81861), ≥ $100M: Required monthly when EVMS requirement is on contract

- Pathway: DBS (Defense Business Systems). Table: EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway).
- Status when the condition holds: Required (contract-level).
- Applies when: Monthly when an EVMS requirement is on contract ($100M or more).
- Condition code: `contract_cost_type = yes AND contract_value >= 100,000,000`
- When due: Monthly
- Type: Regulatory.
- Source: Integrated Program Management Data and Analysis Report (IPMDAR) DID DI-MGMT-81861
- AAFDID note: IPMDAR is required. All files are required.
- Tool note: Classified as regulatory by this tool (DoDI 5000.85; DI-MGMT-81861).
- Changed since AAFDID (EVMS thresholds changed by class deviation): see 20-changes-since-aafdid.md, note evms-2026.
- Page: https://www.waru.edu/aafdid/EVMS-Application-Requirements


---

# AoS requirements: Acquisition of Services

Knowledge file 15 of the AAFDID Navigator agent pack, rules 1.0.0. Every record below belongs to the AoS pathway only.

- Governing instruction: DoDI 5000.74 (Change 1, June 2021)
- Summary: Services at or above the simplified acquisition threshold, managed in three phases (Plan, Develop, Execute) and seven steps. The services category (S-CAT) sets the decision authority.
- Decision authority: S-CAT I and II: the service or component acquisition executive or designee. S-CAT III to V: the component Senior Services Manager or designee. Special Interest: USD(A&S) or designee (DoDI 5000.74, Table 1).
- Events, in order: `plan` = Plan: form the team, review the current strategy, market research; `develop` = Develop: define requirements, SRRB, acquisition strategy; `execute` = Execute: award and manage performance
- Note: AAFDID has not published an Acquisition of Services requirements table. Every AoS entry here comes from DoDI 5000.74 or the DFARS and cites its paragraph.
- Note: AAFDID's AoS overview: most regulatory information requirements are addressed in the acquisition strategy, and S-CAT decision authorities decide what regulatory information is required.
- AAFDID page: https://www.waru.edu/aafdid/aos

## Services category (S-CAT)

| S-CAT | Rule | Decision authority |
| --- | --- | --- |
| Special Interest | Designated by ASD(A); no dollar threshold | USD(A&S) or designee |
| S-CAT I | $1B or more total, or more than $300M in any one year | Service or component acquisition executive, or designee |
| S-CAT II | $250M or more, but less than $1B | Service or component acquisition executive, or designee |
| S-CAT III | $100M or more, but less than $250M | Component Senior Services Manager or designee |
| S-CAT IV | $10M or more, but less than $100M | Component Senior Services Manager or designee |
| S-CAT V | Above the simplified acquisition threshold, but less than $10M | Component Senior Services Manager or designee |

Source: DoDI 5000.74, para 3.5.a and Table 1; thresholds use the IGCE in current-year dollars (Table 1, note 1). Special Interest overrides the dollar category.

## Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table)

### AOS-01 · Independent Government Cost Estimate (IGCE)

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Plan: form the team, review the current strategy, market research (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Not stated
- Source: DoDI 5000.74, Table 1, note 1 (para 3.5.a)
- AAFDID note: The IGCE in current-year dollars sets the services category (S-CAT), and with it the decision authority.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-02 · Functional Services Manager (FSM) designation and multi-functional team

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Plan: form the team, review the current strategy, market research (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: The requiring activity designates the FSM
- Source: DoDI 5000.74, paras 3.4.a-b and 4.2.a-c
- AAFDID note: The FSM leads a multi-functional team and develops the preferred solution: initial acquisition strategy, business approach, assumptions, risks and cost.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-03 · Market research, documented

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Plan: form the team, review the current strategy, market research (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Not stated
- Source: DoDI 5000.74, paras 3.3.d(1), 4.2.e and 4.3.a
- AAFDID note: Identify providers by competency, performance and cost, and maximize reliance on the commercial marketplace. Initial market research informs the SRRB.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-04 · Requirement cost analysis

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Develop: define requirements, SRRB, acquisition strategy (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Considered by the SRRB
- Source: DoDI 5000.74, para 4.2.e
- AAFDID note: An analysis of the discrete costs within the service requirement, paired with initial market research, so the SRRB can weigh mission need, cost and affordability.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-05 · Services Requirements Review Board (SRRB) validation and approval

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: Total estimated value of $10M or more. For IDIQs, the base contract and any task order of $10M or more.
- Condition code: `svc_total_value >= 10,000,000`
- When due: Develop: define requirements, SRRB, acquisition strategy (initial)
- Type: Statutory and regulatory. AAFDID TYPE: Statutory, Regulatory
- Approval: SRRB chair in the requiring organization
- Source: DoDI 5000.74, paras 4.3.a-c and 4.3.e-f; FY2011 NDAA sec. 863 (per the AAFDID AoS overview)
- AAFDID note: The SRRB reviews, validates, prioritizes and approves the requirement before the procurement request goes to contracting. It considers mission need, alignment, risks, related requirements, workforce, projected cost through the FYDP, sensitive functions and metrics (para 4.3.g).
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-06 · Workforce analysis: insource or outsource

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: Reviewed at the SRRB: total estimated value of $10M or more.
- Condition code: `svc_total_value >= 10,000,000`
- When due: Develop: define requirements, SRRB, acquisition strategy (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: SRRB chair, coordinated with component manpower officials
- Source: DoDI 5000.74, paras 4.3.g(4) and 1.2.c(3); 10 U.S.C. 2461 and 2463
- AAFDID note: Explain why military or civilian personnel cannot do the work. The Director, Office of Small Business Programs, reviews any decision to convert small-business work to federal employees (para 1.2.c(4)).
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-07 · Review and justification of critical functions and functions closely associated with inherently governmental functions

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: Contractors will perform critical functions or functions closely associated with inherently governmental functions.
- Condition code: `svc_sensitive_functions = yes`
- When due: Develop: define requirements, SRRB, acquisition strategy (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: Not stated
- Source: DoDI 5000.74, paras 1.2.c and 4.3.g(8); 10 U.S.C. 2330a(e) as cited (now 10 U.S.C. 4505, per AAFDID's Title 10 crosswalk); FAR 7.503(e); DFARS 207.503
- AAFDID note: Reliance on contractors for these functions must be reviewed, justified, and reduced to the maximum extent practicable.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-08 · Services Acquisition Workshop (SAW)

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: Total value of $500M or more, or $250M or more in a year. For a multiple-award IDIQ, not the base award, but any task order of $100M or more.
- Condition code: `(svc_vehicle = standalone AND (svc_total_value >= 500,000,000 OR svc_annual_value >= 250,000,000)) OR (svc_vehicle = task_order AND svc_total_value >= 100,000,000)`
- When due: Develop: define requirements, SRRB, acquisition strategy (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Waiver by the component Senior Services Manager; for Special Interest acquisitions, by the decision authority
- Source: DoDI 5000.74, para 4.2.d
- AAFDID note: The team completes a SAW, or an equivalent, before the acquisition strategy is approved.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-09 · Business case analysis for requirements that overlap existing vehicles

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: $50M or more, with potential significant overlap with an existing contract, a DoD or government-wide vehicle, or a best-in-class contract.
- Condition code: `svc_total_value >= 50,000,000 AND svc_overlap = yes`
- When due: Develop: define requirements, SRRB, acquisition strategy (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Required by the component Portfolio Manager; approver not stated
- Source: DoDI 5000.74, para 3.3.d(9)
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-10 · Acquisition strategy as a written acquisition plan

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: Total cost of all contracts of $50M or more, or $25M or more in any fiscal year (DFARS 207.103(d)(i)(B)).
- Condition code: `svc_total_value >= 50,000,000 OR svc_annual_value >= 25,000,000`
- When due: Develop: define requirements, SRRB, acquisition strategy (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Decision authority for the S-CAT (DoDI 5000.74, Table 1)
- Source: DoDI 5000.74, paras 4.4.a-b; DFARS 207.103(d)(i)(B); DFARS 207.105
- AAFDID note: Content follows DFARS 207.105, with enough detail for the decision authority to judge business sense, compliance with law and policy, and affordability.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-11 · Acquisition strategy in streamlined documentation

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: Below the written acquisition plan threshold: under $50M total and under $25M in every fiscal year.
- Condition code: `svc_total_value < 50,000,000 AND svc_annual_value < 25,000,000`
- When due: Develop: define requirements, SRRB, acquisition strategy (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Decision authority for the S-CAT (DoDI 5000.74, Table 1)
- Source: DoDI 5000.74, para 4.4.c
- AAFDID note: Covers requirements development, acquisition planning, solicitation and award, significant risks, contract and performance management, and the metrics evaluation plan, including a summary of the analysis of alternatives.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-12 · Small business participation opportunities

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Develop: define requirements, SRRB, acquisition strategy (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Not stated
- Source: DoDI 5000.74, paras 1.2.d(2), 3.3.d(2) and 4.4.c(2)(e)
- AAFDID note: Opportunities for small businesses, including socio-economic concerns, as prime contractors and subcontractors.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-13 · Performance-based approach and contract type rationale

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Develop: define requirements, SRRB, acquisition strategy (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Not stated
- Source: DoDI 5000.74, para 4.4.c(2)(d)
- AAFDID note: Use performance-based services acquisition or explain why not, and give a rationale for any contract type other than firm-fixed-price.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-14 · Intellectual property management mechanisms

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Develop: define requirements, SRRB, acquisition strategy (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Not stated
- Source: DoDI 5000.74, para 1.2.d(4)
- AAFDID note: Identify and manage IP so that government and industry get a fair return and a follow-on provider can take over competitively.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-15 · Rationale and authority for other than full and open competition

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: May apply.
- Applies when: Only if other than full and open competition is planned.
- Condition code: `always (every program on this pathway)`
- When due: Develop: define requirements, SRRB, acquisition strategy (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Not stated
- Source: DoDI 5000.74, para 4.4.c(2)(g)
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-16 · Consolidation or bundling summary, coordinated with the Office of Small Business Programs

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: May apply.
- Applies when: Only if the requirement is consolidated or bundled.
- Condition code: `always (every program on this pathway)`
- When due: Develop: define requirements, SRRB, acquisition strategy (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Coordinated with the appropriate OSBP
- Source: DoDI 5000.74, paras 3.3.d(7) and 4.4.c(1)(d)
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-17 · Contract line items with Product or Service Codes

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Execute: award and manage performance (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Not stated
- Source: DoDI 5000.74, para 1.2.d(5); FAR 4.1005
- AAFDID note: Line items follow FAR 4.1005, including the required Product or Service Code.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-18 · Performance management metrics

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Execute: award and manage performance (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Not stated
- Source: DoDI 5000.74, paras 4.5.b-c
- AAFDID note: Tailored metrics that signal cost, schedule, performance, small business and competition risk, and inform renewals and re-competes.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-19 · FSM cost and metrics tracking, with deviation notice

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Execute: award and manage performance (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Notice goes to the requiring activity
- Source: DoDI 5000.74, para 3.4.f
- AAFDID note: The FSM tracks performance against cost targets and immediately notifies the requiring activity of significant cost, schedule or performance deviations.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-20 · Trained and qualified contracting officer's representative (COR)

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: For every program on this pathway.
- Condition code: `always (every program on this pathway)`
- When due: Execute: award and manage performance (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Not stated
- Source: DoDI 5000.74, Glossary G.2 (requiring activity)
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-21 · SRRB validation before exercising an option

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: Acquisitions under SRRB review: $10M or more.
- Condition code: `svc_total_value >= 10,000,000`
- When due: Execute: award and manage performance (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: SRRB
- Source: DoDI 5000.74, para 4.3.e(2)
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-22 · Independent management reviews (post-award)

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Required.
- Applies when: Post-award contracts with a total value of $100M or more, and others the component chooses.
- Condition code: `svc_total_value >= 100,000,000`
- When due: Execute: award and manage performance (initial)
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: Under component procedures
- Source: DoDI 5000.74, para 4.6.a; 10 U.S.C. 2330 as cited (now 10 U.S.C. 4501)
- AAFDID note: Periodic reviews of contract performance, contracting mechanisms, subcontractor management, oversight staffing and pass-through charges.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-23 · Review of contracts where a contractor oversees other contractors

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: May apply.
- Applies when: Only if one contractor oversees services performed by other contractors.
- Condition code: `always (every program on this pathway)`
- When due: Execute: award and manage performance (initial)
- Type: Regulatory. AAFDID TYPE: Regulatory
- Approval: Under component procedures
- Source: DoDI 5000.74, para 4.6.b
- AAFDID note: Reviews reliance on the contractor for functions closely associated with inherently governmental functions, and the prime's financial interest in the work it oversees.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf

### AOS-24 · Bridge contract status update and notifications

- Pathway: AoS (Acquisition of Services). Table: Requirements drawn from DoDI 5000.74 (AAFDID has no AoS table).
- Status when the condition holds: Only if triggered.
- Applies when: A bridge contract is used because of inadequate planning, as the S-CAT decision authority determines. Contingency, humanitarian and disaster-response actions are excluded.
- Condition code: `always (every program on this pathway)`
- When due: A bridge contract is used because of inadequate planning, as the S-CAT decision authority determines. Contingency, humanitarian and disaster-response actions are excluded.
- Type: Statutory. AAFDID TYPE: Statutory
- Approval: Requirements owner and contracting officer send the update; routing depends on the $10M threshold
- Source: DoDI 5000.74, paras 4.7.a-d; 10 U.S.C. 2329(e) as cited
- AAFDID note: First use: a status update with the rationale. A second use under $10M: notice to the armed force's Vice Chief of Staff and the service acquisition executive or agency head. Plan early enough to avoid bridges.
- Page: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500074p.pdf


---

# Changes since AAFDID's tables

Knowledge file 20 of the AAFDID Navigator agent pack.

AAFDID's What's New page lists one entry (February 2023, the MTA review redline). Its Excel exports are filed under January 2025, and no table page shows a last-updated date. The changes below came later and are not reflected in AAFDID's tables.

## thresholds-2025: MDAP and major system thresholds raised (2025-12-18)

The FY2026 NDAA (Pub. L. 119-60, sec. 1804) raised the statutory MDAP threshold to more than $1.0B RDT&E or $4.5B procurement, and the major system threshold to more than $275M RDT&E or $1.3B procurement, both in FY2024 constant dollars. DoDI 5000.85 Table 1 and AAFDID still use the older FY2020 figures ($525M / $3.065B and $200M / $920M). Confirm your program's category against the current statute and your component's direction.

- Source: 10 U.S.C. 4201 (MDAP definition): https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title10-section4201&num=0&edition=prelim
- Source: 10 U.S.C. 3041 (major system definition): https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title10-section3041&num=0&edition=prelim
- Attached to: MTA-T07
- Also matters for the intake questions: mca_program_type, mta_size, swa_above_acat_ii, uca_acat

## jcids-2025: JCIDS disestablished (2025-08-20)

The August 20, 2025 memo "Reforming the Joint Requirements Process" disestablished JCIDS. Each military service now validates its own requirements, the JROC identifies and ranks key operational problems, and a Requirements and Resourcing Alignment Board sets joint priorities. AAFDID entries that name JCIDS documents or JROC validation (ICD, CDD, KPPs) predate this change. Use your component's current requirements process.

- Source: Federal News Network, Aug 2025: DoD dismantles JCIDS: https://federalnewsnetwork.com/defense-news/2025/08/dod-dismantles-decades-old-jcids-in-joint-requirements-process-overhaul/
- Source: Memo, Reforming Joint Requirements, signed 20 Aug 2025 (WARU library): https://www.waru.edu/artifact/memo-osd-reforming-joint-requirements-signed-20-aug-2025
- Attached to: MCA-B01, MCA-C01, MCA-C02, MCA-C03, MCA-C08, MCA-M11, MCA-M14, MCA-M24, MCA-M42, MCA-M79

## was-2025: Warfighting Acquisition System (2025-11-07)

The November 7, 2025 memo renamed the Defense Acquisition System the Warfighting Acquisition System. It converts PEOs into Portfolio Acquisition Executives, makes commercial solutions the first choice and the software pathway the preferred path for software, and says the 5000-series will be revised to cut documentation and consolidate milestones. The FY2026 NDAA (sec. 1802) also creates Portfolio Acquisition Executives. No pathway's entry criteria changed as of this check.

- Source: Memo, Transforming the Defense Acquisition System into the Warfighting Acquisition System, Nov 7, 2025: https://static.carahsoft.com/concrete/files/4917/6702/9385/Memorandum_Transforming_the_Defense_Acquisition_System_into_the_Warfighting_Acquisition_System.pdf

## evms-2026: EVMS thresholds changed by class deviation (2026-02-01)

DFARS Class Deviation 2026-O0011 (DFARS 234.201, clauses 252.234-7998 and -7999), effective February 1, 2026, sets $50M as the threshold for an EIA-748-compliant EVMS and $100M for a Government-validated EVMS on cost and incentive contracts. EVMS on a firm-fixed-price contract needs a waiver. AAFDID still shows $20M and $100M. Confirm the thresholds on contract with your contracting officer.

- Source: Class Deviation 2026-O0011 memo (DPCAP): https://www.acq.osd.mil/dpap/dars/classdev/DFARS_RFO/Part-234/2026-O0011_TAB_A_Deviation_Memo_DFARS_234.pdf
- Source: Humphreys & Associates: EVMS thresholds class deviation memo: https://www.humphreys-assoc.com/earned-value-management-system-thresholds-class-deviation-memo/
- Attached to: EVM-01, EVM-02, EVM-03, EVM-04, EVM-05, EVM-06

## mta-change1-2024: DoDI 5000.80 Change 1 and 10 U.S.C. 3602 (2024-11-25)

DoDI 5000.80 Change 1 changed several MTA rules:
- The transition plan goes to OUSD(A&S) through AIR within 2 years of program start.
- Transition documentation must be complete 3 months before completion.
- A termination is reported to OUSD(A&S) within 7 days and to Congress within 30 days.
- Requirement approval may be delegated no lower than the PM.
- Test strategies cover non-kinetic threats.
- Exportability applies when international partners are involved.

10 U.S.C. 3602 (December 2024) codified MTA, and lets the service acquisition executive permit further 5-year periods. AAFDID's MTA notes cite the October 2022 policy update.

- Source: DoDI 5000.80 Original vs Change 1 briefing (Feb 2025): https://www.waru.edu/sites/default/files/2025-02/DODI%205000_80%20Original%20vs%20Change1%20Webinar%20202502%20no%20notes.pdf
- Source: 10 U.S.C. 3602: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title10-section3602&num=0&edition=prelim
- Attached to: MTA-S01, MTA-S02, MTA-S10, MTA-S17, MTA-S18, MTA-T01, MTA-T03, MTA-T11

## cmo-2021: Chief Management Officer repealed (2021-01-01)

Section 901 of the FY2021 NDAA repealed the Chief Management Officer position. AAFDID's own DBS note says the transfer of CMO duties is still pending. Ask your component who now performs the certification.

- Source: AAFDID DBS Statutory Requirements, table notes: https://www.waru.edu/aafdid/DBS-Statutory-Requirements
- Attached to: DBS-04
