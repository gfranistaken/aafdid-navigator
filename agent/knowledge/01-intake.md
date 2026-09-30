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
   - Value: a dollar amount such as `45000000`, `45M` or `1.2B`.
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
   - Value: a dollar amount such as `45000000`, `45M` or `1.2B`.
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
   - Value: a dollar amount such as `45000000`, `45M` or `1.2B`.
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
   - Value: a dollar amount such as `45000000`, `45M` or `1.2B`.
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
   - Value: a dollar amount such as `45000000`, `45M` or `1.2B`.
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
3. `svc_total_value`: What is the total estimated value, from the independent government cost estimate, in current-year dollars?
   - Value: a dollar amount such as `45000000`, `45M` or `1.2B`.
   - Why it matters: Sets the services category (S-CAT), the decision authority and most thresholds (DoDI 5000.74, Table 1).
   - Affects: AOS-05, AOS-06, AOS-08, AOS-09, AOS-10, AOS-11, AOS-21, AOS-22
4. `svc_annual_value`: What is the highest estimated value in any single year?
   - Value: a dollar amount such as `45000000`, `45M` or `1.2B`.
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
