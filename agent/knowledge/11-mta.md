# MTA requirements: Middle Tier of Acquisition

Knowledge file 11 of the AAFDID Navigator agent pack, rules 1.1.0. Every record below belongs to the MTA pathway only.

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
