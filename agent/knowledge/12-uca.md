# UCA requirements: Urgent Capability Acquisition

Knowledge file 12 of the AAFDID Navigator agent pack, rules 1.1.0. Every record below belongs to the UCA pathway only.

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
