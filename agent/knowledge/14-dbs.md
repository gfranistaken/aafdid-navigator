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
