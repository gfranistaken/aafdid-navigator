# Agent test scenarios

Use these to check an agent built from this pack. **Do not upload this file as knowledge.**

For each scenario:

1. Start a new chat.
2. Paste the profile block.
3. Ask: "Which requirements apply?"
4. Score the answer. It should list every code in the Required, May-apply and Also-review lines, and none of the codes in the Must-not-list line.

For a fuller comparison, run the same profile through the web navigator or the engine: `node engine/cli.js <profile>`.

Also check that `TAILCHECK` returns `TAIL-OK-AAFDID-NAV-1` exactly. If it doesn't, the instructions were cut off.

## 01-mta-rf-nonmajor-f3

```
AAFDID PROFILE v1
program: F3 replacement power supply (example)
pathway: mta
event: entrance
mta_path: rf
mta_size: non_major
contract_value: 20m_to_50m
contract_cost_type: no
```

- Due at Program entrance: the ADM starts the MTA clock (2): MTA-T02, MTA-T05
- Required (6): MTA-T02, MTA-T05, MTA-T08, MTA-T09, MTA-T10, MTA-T11
- May apply (23): CSDR-02, CSDR-05, MTA-S01, MTA-S02, MTA-S09, MTA-S10, MTA-S15, MTA-S17, MTA-S18, MTA-S19, MTA-S20, MTA-S21, MTA-S22, MTA-S23, MTA-S24, MTA-S25, MTA-S26, MTA-S27, MTA-S28, MTA-S29, MTA-S30, MTA-S31, MTA-S33
- Only if triggered (0): none
- Needs an answer (0): none
- Must not list as required, may apply or also review (23): MTA-T01, MTA-T03, MTA-T04, MTA-T06, MTA-T07, EVM-01, EVM-02, EVM-03, EVM-04, EVM-05, EVM-06, MTA-S03, MTA-S04, MTA-S05, MTA-S06, MTA-S07, MTA-S08, MTA-S11, MTA-S12, MTA-S13, MTA-S14, MTA-S16, MTA-S32

## 02-mta-rp-major

```
AAFDID PROFILE v1
program: Prototype sensor pod (example)
pathway: mta
event: entrance
mta_path: rp
mta_size: major
contract_value: 100m_plus
contract_cost_type: yes
```

- Due at Program entrance: the ADM starts the MTA clock (5): MTA-T01, MTA-T02, MTA-T03, MTA-T04, MTA-T05
- Required (12): MTA-T01, MTA-T02, MTA-T03, MTA-T04, MTA-T05, MTA-T08, MTA-T09, MTA-T10, MTA-T11, CSDR-02, EVM-03, EVM-06
- May apply (35): MTA-T06, CSDR-05, MTA-S01, MTA-S02, MTA-S03, MTA-S04, MTA-S05, MTA-S06, MTA-S07, MTA-S08, MTA-S09, MTA-S10, MTA-S11, MTA-S12, MTA-S13, MTA-S14, MTA-S15, MTA-S16, MTA-S17, MTA-S18, MTA-S19, MTA-S20, MTA-S21, MTA-S22, MTA-S23, MTA-S24, MTA-S25, MTA-S26, MTA-S27, MTA-S28, MTA-S29, MTA-S30, MTA-S31, MTA-S32, MTA-S33
- Only if triggered (0): none
- Needs an answer (0): none
- Must not list as required, may apply or also review (5): MTA-T07, EVM-01, EVM-02, EVM-04, EVM-05

## 03-mta-size-unknown

```
AAFDID PROFILE v1
program: MTA program with open answers (example)
pathway: mta
mta_path: rf
unknown: mta_size, contract_value, contract_cost_type
```

- Required (6): MTA-T02, MTA-T05, MTA-T08, MTA-T09, MTA-T10, MTA-T11
- May apply (21): MTA-S01, MTA-S02, MTA-S09, MTA-S10, MTA-S15, MTA-S17, MTA-S18, MTA-S19, MTA-S20, MTA-S21, MTA-S22, MTA-S23, MTA-S24, MTA-S25, MTA-S26, MTA-S27, MTA-S28, MTA-S29, MTA-S30, MTA-S31, MTA-S33
- Only if triggered (0): none
- Needs an answer (25): MTA-T01, MTA-T03, MTA-T04, MTA-T06, MTA-T07, CSDR-02, CSDR-05, EVM-01, EVM-02, EVM-03, EVM-04, EVM-05, EVM-06, MTA-S03, MTA-S04, MTA-S05, MTA-S06, MTA-S07, MTA-S08, MTA-S11, MTA-S12, MTA-S13, MTA-S14, MTA-S16, MTA-S32
- Questions to ask: mta_size, contract_value, contract_cost_type
- Must not list as required, may apply or also review (0): none

## 04-mca-mdap-msb

```
AAFDID PROFILE v1
program: Next-gen radar (example)
pathway: mca
event: ms_b
mca_program_type: mdap
it_type: it_system
contract_value: 100m_plus
contract_cost_type: yes
unknown: dote_oversight
```

- Due at Milestone B (54): MCA-M05, MCA-M08, MCA-M23, MCA-M04, MCA-M07, MCA-M12, MCA-M13, MCA-M15, MCA-M18, MCA-M19, MCA-M21, MCA-M26, MCA-M27, MCA-M32, MCA-M33, MCA-M34, MCA-M36, MCA-M39, MCA-M43, MCA-M44, MCA-M46, MCA-M47, MCA-M50, MCA-M51, MCA-M52, MCA-M53, MCA-M54, MCA-M61, MCA-M62, MCA-M65, MCA-M66, MCA-M67, MCA-M69, MCA-M70, MCA-M72, MCA-M74, MCA-M77, MCA-M78, MCA-M06, MCA-M11, MCA-M17, MCA-M20, MCA-M30, MCA-M48, MCA-M64, MCA-M75, MCA-M02, MCA-M24, MCA-M31, MCA-M37, MCA-M38, MCA-M57, MCA-M59, MCA-M80
- Required (96): MCA-M05, MCA-M08, MCA-M23, MCA-M04, MCA-M07, MCA-M12, MCA-M13, MCA-M15, MCA-M18, MCA-M19, MCA-M21, MCA-M26, MCA-M27, MCA-M32, MCA-M33, MCA-M34, MCA-M36, MCA-M39, MCA-M43, MCA-M44, MCA-M46, MCA-M47, MCA-M50, MCA-M51, MCA-M52, MCA-M53, MCA-M54, MCA-M61, MCA-M62, MCA-M65, MCA-M66, MCA-M67, MCA-M69, MCA-M70, MCA-M72, MCA-M74, MCA-M77, MCA-M78, MCA-M06, MCA-M11, MCA-M17, MCA-M20, MCA-M30, MCA-M48, MCA-M64, MCA-M75, MCA-M02, MCA-M24, MCA-M31, MCA-M37, MCA-M38, MCA-M57, MCA-M59, MCA-M80, MCA-M79, MCA-M09, MCA-M14, MCA-M16, MCA-M68, MCA-M71, MCA-M40, MCA-M03, MCA-M35, MCA-M60, MCA-M41, MCA-M45, MCA-M55, MCA-M56, CSDR-02, CSDR-04, EVM-03, EVM-06, MCA-C01, MCA-C02, MCA-C03, MCA-C04, MCA-C05, MCA-C06, MCA-C07, MCA-C08, MCA-C09, MCA-C10, MCA-C11, MCA-R01, MCA-R02, MCA-R03, MCA-M22, MCA-M58, MCA-M73, MCA-M10, MCA-M42, MCA-M49, MCA-M01, MCA-M63, MCA-M76, MCA-M25
- May apply (4): CSDR-01, CSDR-03, CSDR-05, CSDR-06
- Only if triggered (22): MCA-N01, MCA-N02, MCA-N03, MCA-X02, MCA-X03, MCA-X04, MCA-X05, MCA-X06, MCA-X07, MCA-X08, MCA-X09, MCA-X10, MCA-X11, MCA-X12, MCA-X13, MCA-X14, MCA-X15, MCA-X17, MCA-X18, MCA-X19, MCA-X20, MCA-X21
- Needs an answer (5): MCA-M28, MCA-M29, MCA-X01, MCA-X16, MCA-X22
- Questions to ask: dote_oversight
- Must not list as required, may apply or also review (4): EVM-01, EVM-02, EVM-04, EVM-05

## 05-mca-acat3-msc-embedded

```
AAFDID PROFILE v1
program: F3 replacement actuator (example)
pathway: mca
event: ms_c
mca_program_type: acat_iii
it_type: embedded_it
contract_value: 20m_to_50m
contract_cost_type: no
unknown: dote_oversight
```

- Due at Milestone C (43): MCA-M05, MCA-M08, MCA-M23, MCA-M79, MCA-M04, MCA-M07, MCA-M09, MCA-M12, MCA-M13, MCA-M14, MCA-M15, MCA-M16, MCA-M18, MCA-M19, MCA-M32, MCA-M33, MCA-M39, MCA-M43, MCA-M44, MCA-M46, MCA-M47, MCA-M51, MCA-M52, MCA-M53, MCA-M54, MCA-M61, MCA-M62, MCA-M65, MCA-M68, MCA-M69, MCA-M70, MCA-M71, MCA-M72, MCA-M74, MCA-M78, MCA-M06, MCA-M11, MCA-M20, MCA-M40, MCA-M24, MCA-M57, MCA-M80, MCA-M35
- Required (61): MCA-M05, MCA-M08, MCA-M23, MCA-M79, MCA-M04, MCA-M07, MCA-M09, MCA-M12, MCA-M13, MCA-M14, MCA-M15, MCA-M16, MCA-M18, MCA-M19, MCA-M32, MCA-M33, MCA-M39, MCA-M43, MCA-M44, MCA-M46, MCA-M47, MCA-M51, MCA-M52, MCA-M53, MCA-M54, MCA-M61, MCA-M62, MCA-M65, MCA-M68, MCA-M69, MCA-M70, MCA-M71, MCA-M72, MCA-M74, MCA-M78, MCA-M06, MCA-M11, MCA-M20, MCA-M40, MCA-M24, MCA-M57, MCA-M80, MCA-M35, MCA-M41, MCA-M45, MCA-M55, MCA-M56, MCA-C04, MCA-C05, MCA-C06, MCA-C07, MCA-C08, MCA-C09, MCA-C10, MCA-C11, MCA-M58, MCA-M10, MCA-M42, MCA-M49, MCA-M76, MCA-M48
- May apply (0): none
- Only if triggered (5): MCA-X03, MCA-X10, MCA-X11, MCA-X17, MCA-X20
- Needs an answer (5): MCA-M28, MCA-M29, MCA-X01, MCA-X16, MCA-X22
- Questions to ask: dote_oversight
- Must not list as required, may apply or also review (61): MCA-M01, MCA-M21, MCA-M26, MCA-M27, MCA-M34, MCA-M36, MCA-M50, MCA-M63, MCA-M66, MCA-M67, MCA-M77, MCA-M17, MCA-M25, MCA-M30, MCA-M64, MCA-M75, MCA-M02, MCA-M31, MCA-M37, MCA-M38, MCA-M59, MCA-M03, MCA-M60, CSDR-01, CSDR-02, CSDR-03, CSDR-04, CSDR-05, CSDR-06, EVM-01, EVM-02, EVM-03, EVM-04, EVM-05, EVM-06, MCA-B04, MCA-C01, MCA-C02, MCA-C03, MCA-M22, MCA-M73, MCA-N01, MCA-N02, MCA-N03, MCA-R01, MCA-R02, MCA-R03, MCA-X02, MCA-X04, MCA-X05, MCA-X06, MCA-X07, MCA-X08, MCA-X09, MCA-X12, MCA-X13, MCA-X14, MCA-X15, MCA-X18, MCA-X19, MCA-X21

## 06-mca-mais-msa

```
AAFDID PROFILE v1
program: Legacy MAIS program (example)
pathway: mca
event: ms_a
mca_program_type: mais
it_type: it_system
unknown: dote_oversight, contract_value, contract_cost_type
```

- Due at Milestone A (1): MCA-M74
- Required (13): MCA-M74, MCA-M56, MCA-C01, MCA-C02, MCA-C03, MCA-C04, MCA-C05, MCA-C06, MCA-C07, MCA-C08, MCA-C09, MCA-C10, MCA-C11
- May apply (1): CSDR-01
- Only if triggered (0): none
- Needs an answer (11): CSDR-02, CSDR-03, CSDR-04, CSDR-05, CSDR-06, EVM-01, EVM-02, EVM-03, EVM-04, EVM-05, EVM-06
- Questions to ask: dote_oversight, contract_value, contract_cost_type
- Must not list as required, may apply or also review (110): MCA-M05, MCA-M08, MCA-M10, MCA-M23, MCA-M42, MCA-M49, MCA-M79, MCA-M01, MCA-M04, MCA-M07, MCA-M09, MCA-M12, MCA-M13, MCA-M14, MCA-M15, MCA-M16, MCA-M18, MCA-M19, MCA-M21, MCA-M26, MCA-M27, MCA-M32, MCA-M33, MCA-M34, MCA-M36, MCA-M39, MCA-M43, MCA-M44, MCA-M46, MCA-M47, MCA-M50, MCA-M51, MCA-M52, MCA-M53, MCA-M54, MCA-M61, MCA-M62, MCA-M63, MCA-M65, MCA-M66, MCA-M67, MCA-M68, MCA-M69, MCA-M70, MCA-M71, MCA-M72, MCA-M76, MCA-M77, MCA-M78, MCA-M06, MCA-M11, MCA-M17, MCA-M20, MCA-M25, MCA-M30, MCA-M40, MCA-M48, MCA-M64, MCA-M75, MCA-M02, MCA-M24, MCA-M31, MCA-M37, MCA-M38, MCA-M57, MCA-M59, MCA-M80, MCA-M03, MCA-M35, MCA-M60, MCA-M28, MCA-M29, MCA-M41, MCA-M45, MCA-M55, MCA-B01, MCA-B02, MCA-B03, MCA-B04, MCA-M22, MCA-M58, MCA-M73, MCA-N01, MCA-N02, MCA-N03, MCA-R01, MCA-R02, MCA-R03, MCA-X01, MCA-X02, MCA-X03, MCA-X04, MCA-X05, MCA-X06, MCA-X07, MCA-X08, MCA-X09, MCA-X10, MCA-X11, MCA-X12, MCA-X13, MCA-X14, MCA-X15, MCA-X16, MCA-X17, MCA-X18, MCA-X19, MCA-X20, MCA-X21, MCA-X22

## 07-mca-acat2-no-event

```
AAFDID PROFILE v1
program: ACAT II upgrade, no event given (example)
pathway: mca
mca_program_type: acat_ii
it_type: none
unknown: dote_oversight, contract_value, contract_cost_type
```

- Required (54): MCA-M05, MCA-M08, MCA-M10, MCA-M23, MCA-M42, MCA-M49, MCA-M79, MCA-M04, MCA-M07, MCA-M09, MCA-M12, MCA-M13, MCA-M14, MCA-M15, MCA-M16, MCA-M18, MCA-M19, MCA-M32, MCA-M33, MCA-M39, MCA-M43, MCA-M44, MCA-M46, MCA-M47, MCA-M51, MCA-M52, MCA-M53, MCA-M54, MCA-M61, MCA-M62, MCA-M65, MCA-M66, MCA-M68, MCA-M69, MCA-M70, MCA-M71, MCA-M72, MCA-M74, MCA-M76, MCA-M78, MCA-M06, MCA-M11, MCA-M20, MCA-M40, MCA-M48, MCA-M24, MCA-M57, MCA-M80, MCA-M35, MCA-M41, MCA-M45, MCA-M55, MCA-M56, MCA-M58
- May apply (1): CSDR-01
- Only if triggered (8): MCA-X03, MCA-X05, MCA-X06, MCA-X10, MCA-X11, MCA-X15, MCA-X17, MCA-X20
- Needs an answer (16): MCA-M28, MCA-M29, CSDR-02, CSDR-03, CSDR-04, CSDR-05, CSDR-06, EVM-01, EVM-02, EVM-03, EVM-04, EVM-05, EVM-06, MCA-X01, MCA-X16, MCA-X22
- Questions to ask: dote_oversight, contract_value, contract_cost_type
- Must not list as required, may apply or also review (53): MCA-M01, MCA-M21, MCA-M26, MCA-M27, MCA-M34, MCA-M36, MCA-M50, MCA-M63, MCA-M67, MCA-M77, MCA-M17, MCA-M25, MCA-M30, MCA-M64, MCA-M75, MCA-M02, MCA-M31, MCA-M37, MCA-M38, MCA-M59, MCA-M03, MCA-M60, MCA-B04, MCA-C01, MCA-C02, MCA-C03, MCA-C04, MCA-C05, MCA-C06, MCA-C07, MCA-C08, MCA-C09, MCA-C10, MCA-C11, MCA-M22, MCA-M73, MCA-N01, MCA-N02, MCA-N03, MCA-R01, MCA-R02, MCA-R03, MCA-X02, MCA-X04, MCA-X07, MCA-X08, MCA-X09, MCA-X12, MCA-X13, MCA-X14, MCA-X18, MCA-X19, MCA-X21

## 08-uca-acat3-dev

```
AAFDID PROFILE v1
program: Counter-UAS urgent need (example)
pathway: uca
event: development
uca_acat: acat_iii
contract_value: under_20m
contract_cost_type: yes
unknown: dote_oversight, it_type
```

- Due at Development Milestone (2): UCA-01, UCA-02
- Required (4): UCA-01, UCA-02, UCA-03, UCA-04
- May apply (2): EVM-01, EVM-04
- Also review (58): MCA-M04, MCA-M05, MCA-M06, MCA-M07, MCA-M08, MCA-M09, MCA-M10, MCA-M11, MCA-M12, MCA-M13, MCA-M14, MCA-M15, MCA-M16, MCA-M18, MCA-M19, MCA-M20, MCA-M23, MCA-M24, MCA-M32, MCA-M33, MCA-M35, MCA-M39, MCA-M40, MCA-M41, MCA-M42, MCA-M43, MCA-M44, MCA-M45, MCA-M46, MCA-M47, MCA-M48, MCA-M49, MCA-M51, MCA-M52, MCA-M53, MCA-M54, MCA-M55, MCA-M56, MCA-M57, MCA-M58, MCA-M61, MCA-M62, MCA-M65, MCA-M68, MCA-M69, MCA-M70, MCA-M71, MCA-M72, MCA-M74, MCA-M76, MCA-M78, MCA-M79, MCA-M80, MCA-X03, MCA-X10, MCA-X11, MCA-X17, MCA-X20
- Only if triggered (0): none
- Needs an answer (5): MCA-M28, MCA-M29, MCA-X01, MCA-X16, MCA-X22
- Questions to ask: dote_oversight, it_type
- Must not list as required, may apply or also review (4): EVM-02, EVM-03, EVM-05, EVM-06

## 09-swa-large-mcit

```
AAFDID PROFILE v1
program: Mission planning software (example)
pathway: swa
event: execution_entry
swa_above_acat_ii: yes
mission_critical_it: yes
dote_oversight: yes
software_maintenance: yes
contract_value: 100m_plus
contract_cost_type: yes
```

- Due at Entering the execution phase (14): SWA-04, SWA-05, SWA-06, SWA-07, SWA-08, SWA-09, SWA-10, SWA-11, SWA-12, SWA-13, SWA-14, SWA-15, SWA-16, SWA-01
- Required (43): SWA-04, SWA-05, SWA-06, SWA-07, SWA-08, SWA-09, SWA-10, SWA-11, SWA-12, SWA-13, SWA-14, SWA-15, SWA-16, SWA-01, SWA-17, SWA-19, SWA-20, SWA-21, SWA-23, SWA-24, SWA-25, SWA-26, SWA-27, SWA-28, SWA-29, SWA-30, SWA-32, SWA-34, EVM-03, EVM-06, SWA-C01, SWA-C02, SWA-C03, SWA-C04, SWA-C05, SWA-C06, SWA-C07, SWA-C08, SWA-C09, SWA-C10, SWA-C11, SWA-02, SWA-03
- May apply (4): SWA-18, SWA-22, SWA-31, SWA-33
- Only if triggered (0): none
- Needs an answer (0): none
- Must not list as required, may apply or also review (4): EVM-01, EVM-02, EVM-04, EVM-05

## 10-swa-small-open

```
AAFDID PROFILE v1
program: Small app, several answers open (example)
pathway: swa
swa_above_acat_ii: no
mission_critical_it: no
dote_oversight: no
unknown: software_maintenance, contract_value, contract_cost_type
```

- Required (38): SWA-02, SWA-03, SWA-04, SWA-05, SWA-06, SWA-07, SWA-08, SWA-09, SWA-10, SWA-11, SWA-12, SWA-13, SWA-14, SWA-15, SWA-16, SWA-17, SWA-23, SWA-24, SWA-25, SWA-26, SWA-27, SWA-28, SWA-29, SWA-30, SWA-32, SWA-34, SWA-01, SWA-C01, SWA-C02, SWA-C03, SWA-C04, SWA-C05, SWA-C06, SWA-C07, SWA-C08, SWA-C09, SWA-C10, SWA-C11
- May apply (4): SWA-18, SWA-22, SWA-31, SWA-33
- Only if triggered (0): none
- Needs an answer (8): SWA-19, SWA-20, EVM-01, EVM-02, EVM-03, EVM-04, EVM-05, EVM-06
- Questions to ask: software_maintenance, contract_value, contract_cost_type
- Must not list as required, may apply or also review (1): SWA-21

## 11-dbs-acq-atp

```
AAFDID PROFILE v1
program: Logistics business system (example)
pathway: dbs
event: acquisition_atp
mission_critical_it: yes
dote_oversight: no
contract_value: 50m_to_100m
contract_cost_type: yes
```

- Due at Acquisition ATP (5): DBS-05, DBS-06, DBS-07, DBS-08, DBS-09
- Required (14): DBS-05, DBS-06, DBS-07, DBS-08, DBS-09, DBS-10, DBS-11, DBS-12, DBS-13, EVM-02, EVM-05, DBS-01, DBS-02, DBS-03
- May apply (6): DBS-04, CSDR-01, CSDR-02, CSDR-03, CSDR-05, CSDR-06
- Only if triggered (0): none
- Needs an answer (0): none
- Must not list as required, may apply or also review (7): DBS-14, DBS-15, DBS-16, EVM-01, EVM-03, EVM-04, EVM-06

## 12-aos-scat4

```
AAFDID PROFILE v1
program: Engineering support services (example)
pathway: aos
event: develop
svc_total_value: 10m_to_50m
svc_annual_value: under_25m
svc_special_interest: no
svc_vehicle: standalone
svc_overlap: no
svc_sensitive_functions: no
```

- Due at Develop: define requirements, SRRB, acquisition strategy (7): AOS-04, AOS-05, AOS-06, AOS-11, AOS-12, AOS-13, AOS-14
- Required (15): AOS-04, AOS-05, AOS-06, AOS-11, AOS-12, AOS-13, AOS-14, AOS-17, AOS-18, AOS-19, AOS-20, AOS-21, AOS-01, AOS-02, AOS-03
- May apply (3): AOS-15, AOS-16, AOS-23
- Only if triggered (1): AOS-24
- Needs an answer (0): none
- Must not list as required, may apply or also review (5): AOS-07, AOS-08, AOS-09, AOS-10, AOS-22
- Services category: S-CAT IV; decision authority: Component Senior Services Manager or designee

## 13-aos-large-task-order

```
AAFDID PROFILE v1
program: Enterprise IT services task order (example)
pathway: aos
event: develop
svc_total_value: 100m_to_250m
svc_annual_value: 25m_to_250m
svc_special_interest: no
svc_vehicle: task_order
svc_overlap: yes
svc_sensitive_functions: yes
```

- Due at Develop: define requirements, SRRB, acquisition strategy (10): AOS-04, AOS-05, AOS-06, AOS-07, AOS-08, AOS-09, AOS-10, AOS-12, AOS-13, AOS-14
- Required (19): AOS-04, AOS-05, AOS-06, AOS-07, AOS-08, AOS-09, AOS-10, AOS-12, AOS-13, AOS-14, AOS-17, AOS-18, AOS-19, AOS-20, AOS-21, AOS-22, AOS-01, AOS-02, AOS-03
- May apply (3): AOS-15, AOS-16, AOS-23
- Only if triggered (1): AOS-24
- Needs an answer (0): none
- Must not list as required, may apply or also review (1): AOS-11
- Services category: S-CAT III; decision authority: Component Senior Services Manager or designee

## 14-aos-partial

```
AAFDID PROFILE v1
program: Services with only a total value (example)
pathway: aos
svc_total_value: 250m_to_500m
unknown: svc_annual_value, svc_special_interest, svc_vehicle, svc_overlap, svc_sensitive_functions
```

- Required (16): AOS-01, AOS-02, AOS-03, AOS-04, AOS-05, AOS-06, AOS-10, AOS-12, AOS-13, AOS-14, AOS-17, AOS-18, AOS-19, AOS-20, AOS-21, AOS-22
- May apply (3): AOS-15, AOS-16, AOS-23
- Only if triggered (1): AOS-24
- Needs an answer (3): AOS-07, AOS-08, AOS-09
- Questions to ask: svc_annual_value, svc_vehicle, svc_overlap, svc_sensitive_functions
- Must not list as required, may apply or also review (1): AOS-11
- Services category: S-CAT II; decision authority: Service or component acquisition executive, or designee

## 16-profile-block

```
AAFDID PROFILE v1
program: Profile block input (example)
pathway: mca
event: dev_rfp_rel
mca_program_type: acat_ii
it_type: embedded_it
contract_value: 50m_to_100m
contract_cost_type: yes
unknown: dote_oversight
```

- Due at Development RFP Release Decision (33): MCA-M05, MCA-M08, MCA-M23, MCA-M49, MCA-M79, MCA-M04, MCA-M07, MCA-M09, MCA-M12, MCA-M13, MCA-M14, MCA-M16, MCA-M18, MCA-M19, MCA-M32, MCA-M39, MCA-M43, MCA-M44, MCA-M46, MCA-M52, MCA-M53, MCA-M62, MCA-M66, MCA-M68, MCA-M69, MCA-M70, MCA-M74, MCA-M78, MCA-M06, MCA-M11, MCA-M20, MCA-M40, MCA-M48
- Required (66): MCA-M05, MCA-M08, MCA-M23, MCA-M49, MCA-M79, MCA-M04, MCA-M07, MCA-M09, MCA-M12, MCA-M13, MCA-M14, MCA-M16, MCA-M18, MCA-M19, MCA-M32, MCA-M39, MCA-M43, MCA-M44, MCA-M46, MCA-M52, MCA-M53, MCA-M62, MCA-M66, MCA-M68, MCA-M69, MCA-M70, MCA-M74, MCA-M78, MCA-M06, MCA-M11, MCA-M20, MCA-M40, MCA-M48, MCA-M15, MCA-M33, MCA-M47, MCA-M51, MCA-M54, MCA-M61, MCA-M65, MCA-M71, MCA-M72, MCA-M24, MCA-M57, MCA-M80, MCA-M35, MCA-M41, MCA-M45, MCA-M55, MCA-M56, CSDR-02, CSDR-04, EVM-02, EVM-05, MCA-C04, MCA-C05, MCA-C06, MCA-C07, MCA-C08, MCA-C09, MCA-C10, MCA-C11, MCA-M58, MCA-M10, MCA-M42, MCA-M76
- May apply (4): CSDR-01, CSDR-03, CSDR-05, CSDR-06
- Only if triggered (8): MCA-X03, MCA-X05, MCA-X06, MCA-X10, MCA-X11, MCA-X15, MCA-X17, MCA-X20
- Needs an answer (5): MCA-M28, MCA-M29, MCA-X01, MCA-X16, MCA-X22
- Questions to ask: dote_oversight
- Must not list as required, may apply or also review (49): MCA-M01, MCA-M21, MCA-M26, MCA-M27, MCA-M34, MCA-M36, MCA-M50, MCA-M63, MCA-M67, MCA-M77, MCA-M17, MCA-M25, MCA-M30, MCA-M64, MCA-M75, MCA-M02, MCA-M31, MCA-M37, MCA-M38, MCA-M59, MCA-M03, MCA-M60, EVM-01, EVM-03, EVM-04, EVM-06, MCA-B04, MCA-C01, MCA-C02, MCA-C03, MCA-M22, MCA-M73, MCA-N01, MCA-N02, MCA-N03, MCA-R01, MCA-R02, MCA-R03, MCA-X02, MCA-X04, MCA-X07, MCA-X08, MCA-X09, MCA-X12, MCA-X13, MCA-X14, MCA-X18, MCA-X19, MCA-X21

## 17-mca-aliases-mdap

```
AAFDID PROFILE v1
program: Aliases and casing (example)
pathway: mca
event: ms_b
mca_program_type: mdap
dote_oversight: yes
it_type: none
contract_value: 100m_plus
contract_cost_type: no
```

- Due at Milestone B (54): MCA-M05, MCA-M08, MCA-M23, MCA-M04, MCA-M07, MCA-M12, MCA-M13, MCA-M15, MCA-M18, MCA-M19, MCA-M21, MCA-M26, MCA-M27, MCA-M32, MCA-M33, MCA-M34, MCA-M36, MCA-M39, MCA-M43, MCA-M44, MCA-M46, MCA-M47, MCA-M50, MCA-M51, MCA-M52, MCA-M53, MCA-M54, MCA-M61, MCA-M62, MCA-M65, MCA-M66, MCA-M67, MCA-M69, MCA-M70, MCA-M72, MCA-M74, MCA-M77, MCA-M78, MCA-M06, MCA-M11, MCA-M17, MCA-M20, MCA-M30, MCA-M48, MCA-M64, MCA-M75, MCA-M02, MCA-M24, MCA-M31, MCA-M37, MCA-M38, MCA-M57, MCA-M59, MCA-M80
- Required (85): MCA-M05, MCA-M08, MCA-M23, MCA-M04, MCA-M07, MCA-M12, MCA-M13, MCA-M15, MCA-M18, MCA-M19, MCA-M21, MCA-M26, MCA-M27, MCA-M32, MCA-M33, MCA-M34, MCA-M36, MCA-M39, MCA-M43, MCA-M44, MCA-M46, MCA-M47, MCA-M50, MCA-M51, MCA-M52, MCA-M53, MCA-M54, MCA-M61, MCA-M62, MCA-M65, MCA-M66, MCA-M67, MCA-M69, MCA-M70, MCA-M72, MCA-M74, MCA-M77, MCA-M78, MCA-M06, MCA-M11, MCA-M17, MCA-M20, MCA-M30, MCA-M48, MCA-M64, MCA-M75, MCA-M02, MCA-M24, MCA-M31, MCA-M37, MCA-M38, MCA-M57, MCA-M59, MCA-M80, MCA-M79, MCA-M09, MCA-M14, MCA-M16, MCA-M68, MCA-M71, MCA-M40, MCA-M03, MCA-M35, MCA-M60, MCA-M28, MCA-M29, MCA-M41, MCA-M45, MCA-M55, MCA-M56, CSDR-02, CSDR-04, MCA-R01, MCA-R02, MCA-R03, MCA-M22, MCA-M58, MCA-M73, MCA-M10, MCA-M42, MCA-M49, MCA-M01, MCA-M63, MCA-M76, MCA-M25
- May apply (4): CSDR-01, CSDR-03, CSDR-05, CSDR-06
- Only if triggered (25): MCA-N01, MCA-N02, MCA-N03, MCA-X01, MCA-X02, MCA-X03, MCA-X04, MCA-X05, MCA-X06, MCA-X07, MCA-X08, MCA-X09, MCA-X10, MCA-X11, MCA-X12, MCA-X13, MCA-X14, MCA-X15, MCA-X16, MCA-X17, MCA-X18, MCA-X19, MCA-X20, MCA-X21, MCA-X22
- Needs an answer (0): none
- Must not list as required, may apply or also review (17): EVM-01, EVM-02, EVM-03, EVM-04, EVM-05, EVM-06, MCA-C01, MCA-C02, MCA-C03, MCA-C04, MCA-C05, MCA-C06, MCA-C07, MCA-C08, MCA-C09, MCA-C10, MCA-C11

## 18-mca-mdap-msc-dote

```
AAFDID PROFILE v1
program: MDAP at Milestone C on DOT&E oversight (example)
pathway: mca
event: ms_c
mca_program_type: mdap
dote_oversight: yes
it_type: embedded_it
contract_value: 100m_plus
contract_cost_type: yes
```

- Due at Milestone C (59): MCA-M05, MCA-M08, MCA-M23, MCA-M79, MCA-M04, MCA-M07, MCA-M09, MCA-M12, MCA-M13, MCA-M14, MCA-M15, MCA-M16, MCA-M18, MCA-M19, MCA-M21, MCA-M26, MCA-M27, MCA-M32, MCA-M33, MCA-M34, MCA-M36, MCA-M39, MCA-M43, MCA-M44, MCA-M46, MCA-M47, MCA-M50, MCA-M51, MCA-M52, MCA-M53, MCA-M54, MCA-M61, MCA-M62, MCA-M65, MCA-M66, MCA-M68, MCA-M69, MCA-M70, MCA-M71, MCA-M72, MCA-M74, MCA-M77, MCA-M78, MCA-M06, MCA-M11, MCA-M17, MCA-M20, MCA-M30, MCA-M40, MCA-M64, MCA-M75, MCA-M24, MCA-M31, MCA-M37, MCA-M57, MCA-M80, MCA-M03, MCA-M35, MCA-M60
- Required (95): MCA-M05, MCA-M08, MCA-M23, MCA-M79, MCA-M04, MCA-M07, MCA-M09, MCA-M12, MCA-M13, MCA-M14, MCA-M15, MCA-M16, MCA-M18, MCA-M19, MCA-M21, MCA-M26, MCA-M27, MCA-M32, MCA-M33, MCA-M34, MCA-M36, MCA-M39, MCA-M43, MCA-M44, MCA-M46, MCA-M47, MCA-M50, MCA-M51, MCA-M52, MCA-M53, MCA-M54, MCA-M61, MCA-M62, MCA-M65, MCA-M66, MCA-M68, MCA-M69, MCA-M70, MCA-M71, MCA-M72, MCA-M74, MCA-M77, MCA-M78, MCA-M06, MCA-M11, MCA-M17, MCA-M20, MCA-M30, MCA-M40, MCA-M64, MCA-M75, MCA-M24, MCA-M31, MCA-M37, MCA-M57, MCA-M80, MCA-M03, MCA-M35, MCA-M60, MCA-M38, MCA-M28, MCA-M29, MCA-M41, MCA-M45, MCA-M55, MCA-M56, CSDR-02, CSDR-04, EVM-03, EVM-06, MCA-C04, MCA-C05, MCA-C06, MCA-C07, MCA-C08, MCA-C09, MCA-C10, MCA-C11, MCA-R01, MCA-R02, MCA-R03, MCA-M22, MCA-M58, MCA-M73, MCA-M10, MCA-M42, MCA-M49, MCA-M01, MCA-M63, MCA-M67, MCA-M76, MCA-M25, MCA-M48, MCA-M02, MCA-M59
- May apply (4): CSDR-01, CSDR-03, CSDR-05, CSDR-06
- Only if triggered (25): MCA-N01, MCA-N02, MCA-N03, MCA-X01, MCA-X02, MCA-X03, MCA-X04, MCA-X05, MCA-X06, MCA-X07, MCA-X08, MCA-X09, MCA-X10, MCA-X11, MCA-X12, MCA-X13, MCA-X14, MCA-X15, MCA-X16, MCA-X17, MCA-X18, MCA-X19, MCA-X20, MCA-X21, MCA-X22
- Needs an answer (0): none
- Must not list as required, may apply or also review (7): EVM-01, EVM-02, EVM-04, EVM-05, MCA-C01, MCA-C02, MCA-C03

## 19-uca-acat2-production

```
AAFDID PROFILE v1
program: Urgent need entering production (example)
pathway: uca
event: production
uca_acat: acat_ii
dote_oversight: no
it_type: none
contract_value: 20m_to_50m
contract_cost_type: yes
```

- Due at Production and Deployment Milestone (1): UCA-01
- Required (6): UCA-01, EVM-02, EVM-05, UCA-03, UCA-04, UCA-02
- May apply (0): none
- Also review (62): MCA-M04, MCA-M05, MCA-M06, MCA-M07, MCA-M08, MCA-M09, MCA-M10, MCA-M11, MCA-M12, MCA-M13, MCA-M14, MCA-M15, MCA-M16, MCA-M18, MCA-M19, MCA-M20, MCA-M23, MCA-M24, MCA-M32, MCA-M33, MCA-M35, MCA-M39, MCA-M40, MCA-M41, MCA-M42, MCA-M43, MCA-M44, MCA-M45, MCA-M46, MCA-M47, MCA-M48, MCA-M49, MCA-M51, MCA-M52, MCA-M53, MCA-M54, MCA-M55, MCA-M56, MCA-M57, MCA-M58, MCA-M61, MCA-M62, MCA-M65, MCA-M66, MCA-M68, MCA-M69, MCA-M70, MCA-M71, MCA-M72, MCA-M74, MCA-M76, MCA-M78, MCA-M79, MCA-M80, MCA-X03, MCA-X05, MCA-X06, MCA-X10, MCA-X11, MCA-X15, MCA-X17, MCA-X20
- Only if triggered (0): none
- Needs an answer (0): none
- Must not list as required, may apply or also review (4): EVM-01, EVM-03, EVM-04, EVM-06

## 20-dbs-csdr

```
AAFDID PROFILE v1
program: Business system with a large contract (example)
pathway: dbs
event: limited_deployment_atp
mission_critical_it: no
dote_oversight: no
contract_value: 100m_plus
contract_cost_type: yes
```

- Due at Limited Deployment ATP(s) (1): DBS-11
- Required (13): DBS-11, DBS-12, DBS-13, EVM-03, EVM-06, DBS-01, DBS-02, DBS-03, DBS-05, DBS-07, DBS-08, DBS-09, DBS-10
- May apply (6): DBS-04, CSDR-01, CSDR-02, CSDR-03, CSDR-05, CSDR-06
- Only if triggered (0): none
- Needs an answer (0): none
- Must not list as required, may apply or also review (8): DBS-06, DBS-14, DBS-15, DBS-16, EVM-01, EVM-02, EVM-04, EVM-05

## 21-mta-major-csdr

```
AAFDID PROFILE v1
program: MTA above MDAP thresholds (example)
pathway: mta
event: execution
mta_path: rp
mta_size: exceeds_mdap
contract_value: 100m_plus
contract_cost_type: yes
```

- Due at Throughout program execution (1): MTA-T08
- Required (13): MTA-T08, MTA-T09, MTA-T10, MTA-T11, CSDR-02, EVM-03, EVM-06, MTA-T01, MTA-T02, MTA-T03, MTA-T04, MTA-T05, MTA-T07
- May apply (35): MTA-T06, CSDR-05, MTA-S01, MTA-S02, MTA-S03, MTA-S04, MTA-S05, MTA-S06, MTA-S07, MTA-S08, MTA-S09, MTA-S10, MTA-S11, MTA-S12, MTA-S13, MTA-S14, MTA-S15, MTA-S16, MTA-S17, MTA-S18, MTA-S19, MTA-S20, MTA-S21, MTA-S22, MTA-S23, MTA-S24, MTA-S25, MTA-S26, MTA-S27, MTA-S28, MTA-S29, MTA-S30, MTA-S31, MTA-S32, MTA-S33
- Only if triggered (0): none
- Needs an answer (0): none
- Must not list as required, may apply or also review (4): EVM-01, EVM-02, EVM-04, EVM-05

## 22-swa-planning-alias

```
AAFDID PROFILE v1
program: Software program entering planning (example)
pathway: swa
event: planning
swa_above_acat_ii: no
mission_critical_it: yes
software_maintenance: no
contract_value: under_20m
contract_cost_type: no
unknown: dote_oversight
```

- Due at Entering the planning phase (3): SWA-02, SWA-03, SWA-01
- Required (38): SWA-02, SWA-03, SWA-01, SWA-04, SWA-05, SWA-06, SWA-07, SWA-08, SWA-09, SWA-10, SWA-11, SWA-12, SWA-13, SWA-14, SWA-15, SWA-16, SWA-17, SWA-23, SWA-24, SWA-25, SWA-26, SWA-27, SWA-28, SWA-29, SWA-30, SWA-32, SWA-34, SWA-C01, SWA-C02, SWA-C03, SWA-C04, SWA-C05, SWA-C06, SWA-C07, SWA-C08, SWA-C09, SWA-C10, SWA-C11
- May apply (5): SWA-18, SWA-22, SWA-31, SWA-33, EVM-04
- Only if triggered (0): none
- Needs an answer (1): SWA-21
- Questions to ask: dote_oversight
- Must not list as required, may apply or also review (7): SWA-19, SWA-20, EVM-01, EVM-02, EVM-03, EVM-05, EVM-06

## 23-unrecognized-input

```
AAFDID PROFILE v1
program: Unrecognized answers (example)
pathway: mta
event: Milestone B
mta_path: rapid
international: yes
contract_value: lots
contract_cost_type: maybe
```

- Required (6): MTA-T02, MTA-T05, MTA-T08, MTA-T09, MTA-T10, MTA-T11
- May apply (21): MTA-S01, MTA-S02, MTA-S09, MTA-S10, MTA-S15, MTA-S17, MTA-S18, MTA-S19, MTA-S20, MTA-S21, MTA-S22, MTA-S23, MTA-S24, MTA-S25, MTA-S26, MTA-S27, MTA-S28, MTA-S29, MTA-S30, MTA-S31, MTA-S33
- Only if triggered (0): none
- Needs an answer (25): MTA-T01, MTA-T03, MTA-T04, MTA-T06, MTA-T07, CSDR-02, CSDR-05, EVM-01, EVM-02, EVM-03, EVM-04, EVM-05, EVM-06, MTA-S03, MTA-S04, MTA-S05, MTA-S06, MTA-S07, MTA-S08, MTA-S11, MTA-S12, MTA-S13, MTA-S14, MTA-S16, MTA-S32
- Questions to ask: mta_path, mta_size, contract_value, contract_cost_type
- Must not list as required, may apply or also review (0): none
- The agent should say it could not use: international = yes (not a profile field); mta_path = rapid (value not recognized); contract_value = lots (value not recognized); contract_cost_type = maybe (value not recognized); event = Milestone B (not an event of this pathway)

## 24-profile-block-markdown

```
AAFDID PROFILE v1
program: Services block pasted from a chat (example)
pathway: aos
event: execute
svc_total_value: 1b_plus
svc_vehicle: idiq_base
unknown: svc_annual_value, svc_special_interest, svc_overlap, svc_sensitive_functions
```

- Due at Execute: award and manage performance (6): AOS-17, AOS-18, AOS-19, AOS-20, AOS-21, AOS-22
- Required (16): AOS-17, AOS-18, AOS-19, AOS-20, AOS-21, AOS-22, AOS-01, AOS-02, AOS-03, AOS-04, AOS-05, AOS-06, AOS-10, AOS-12, AOS-13, AOS-14
- May apply (3): AOS-15, AOS-16, AOS-23
- Only if triggered (1): AOS-24
- Needs an answer (2): AOS-07, AOS-09
- Questions to ask: svc_overlap, svc_sensitive_functions
- Must not list as required, may apply or also review (2): AOS-08, AOS-11
- Services category: S-CAT I; decision authority: Service or component acquisition executive, or designee

## 25-aos-annual-only

```
AAFDID PROFILE v1
pathway: aos
svc_annual_value: 300m_plus
unknown: svc_total_value, svc_special_interest, svc_vehicle, svc_overlap, svc_sensitive_functions
```

- Required (12): AOS-01, AOS-02, AOS-03, AOS-04, AOS-10, AOS-12, AOS-13, AOS-14, AOS-17, AOS-18, AOS-19, AOS-20
- May apply (3): AOS-15, AOS-16, AOS-23
- Only if triggered (1): AOS-24
- Needs an answer (7): AOS-05, AOS-06, AOS-07, AOS-08, AOS-09, AOS-21, AOS-22
- Questions to ask: svc_total_value, svc_vehicle, svc_overlap, svc_sensitive_functions
- Must not list as required, may apply or also review (1): AOS-11
- Services category: S-CAT I; decision authority: Service or component acquisition executive, or designee

## 27-uca-acat-unknown

```
AAFDID PROFILE v1
program: Urgent need, ACAT not yet known (example)
pathway: uca
event: development
unknown: uca_acat, dote_oversight, it_type, contract_value, contract_cost_type
```

- Due at Development Milestone (2): UCA-01, UCA-02
- Required (4): UCA-01, UCA-02, UCA-03, UCA-04
- May apply (0): none
- Only if triggered (0): none
- Needs an answer (6): EVM-01, EVM-02, EVM-03, EVM-04, EVM-05, EVM-06
- Questions to ask: uca_acat, contract_value, contract_cost_type
- Must not list as required, may apply or also review (0): none

## 29-cr-only-block

```
AAFDID PROFILE v1
program: Old Mac line endings (example)
pathway: swa
event: each decision point
swa_above_acat_ii: Y
contract_value: ~$20,000,000.004
```

- Required (38): SWA-02, SWA-03, SWA-04, SWA-05, SWA-06, SWA-07, SWA-08, SWA-09, SWA-10, SWA-11, SWA-12, SWA-13, SWA-14, SWA-15, SWA-16, SWA-17, SWA-23, SWA-24, SWA-25, SWA-26, SWA-27, SWA-28, SWA-29, SWA-30, SWA-32, SWA-34, SWA-01, SWA-C01, SWA-C02, SWA-C03, SWA-C04, SWA-C05, SWA-C06, SWA-C07, SWA-C08, SWA-C09, SWA-C10, SWA-C11
- May apply (4): SWA-18, SWA-22, SWA-31, SWA-33
- Only if triggered (0): none
- Needs an answer (4): SWA-20, SWA-21, EVM-02, EVM-05
- Questions to ask: mission_critical_it, dote_oversight, software_maintenance, contract_cost_type
- Must not list as required, may apply or also review (5): SWA-19, EVM-01, EVM-03, EVM-04, EVM-06
- The agent should say it could not use: event = each decision point (not an event of this pathway)

## 30-aos-odd-values

```
AAFDID PROFILE v1
program: Services — odd spacing and a | pipe (example)
pathway: aos
svc_total_value: 500m_to_1b
svc_annual_value: 25m_to_250m
svc_special_interest: no
unknown: svc_vehicle, svc_overlap, svc_sensitive_functions
```

- Required (16): AOS-01, AOS-02, AOS-03, AOS-04, AOS-05, AOS-06, AOS-10, AOS-12, AOS-13, AOS-14, AOS-17, AOS-18, AOS-19, AOS-20, AOS-21, AOS-22
- May apply (3): AOS-15, AOS-16, AOS-23
- Only if triggered (1): AOS-24
- Needs an answer (3): AOS-07, AOS-08, AOS-09
- Questions to ask: svc_vehicle, svc_overlap, svc_sensitive_functions
- Must not list as required, may apply or also review (1): AOS-11
- Services category: S-CAT II; decision authority: Service or component acquisition executive, or designee

## 31-ranges-by-label

```
AAFDID PROFILE v1
program: Ranges given by label and id (example)
pathway: aos
event: develop
svc_total_value: 250m_to_500m
svc_annual_value: 250m_to_300m
svc_special_interest: no
svc_vehicle: idiq_base
unknown: svc_overlap, svc_sensitive_functions
```

- Due at Develop: define requirements, SRRB, acquisition strategy (7): AOS-04, AOS-05, AOS-06, AOS-10, AOS-12, AOS-13, AOS-14
- Required (16): AOS-04, AOS-05, AOS-06, AOS-10, AOS-12, AOS-13, AOS-14, AOS-17, AOS-18, AOS-19, AOS-20, AOS-21, AOS-22, AOS-01, AOS-02, AOS-03
- May apply (3): AOS-15, AOS-16, AOS-23
- Only if triggered (1): AOS-24
- Needs an answer (2): AOS-07, AOS-09
- Questions to ask: svc_overlap, svc_sensitive_functions
- Must not list as required, may apply or also review (2): AOS-08, AOS-11
- Services category: S-CAT II; decision authority: Service or component acquisition executive, or designee

## 32-contract-range-alias

```
AAFDID PROFILE v1
program: Range synonym (example)
pathway: dbs
event: acquisition_atp
mission_critical_it: yes
dote_oversight: no
contract_value: 100m_plus
contract_cost_type: yes
```

- Due at Acquisition ATP (5): DBS-05, DBS-06, DBS-07, DBS-08, DBS-09
- Required (14): DBS-05, DBS-06, DBS-07, DBS-08, DBS-09, DBS-10, DBS-11, DBS-12, DBS-13, EVM-03, EVM-06, DBS-01, DBS-02, DBS-03
- May apply (6): DBS-04, CSDR-01, CSDR-02, CSDR-03, CSDR-05, CSDR-06
- Only if triggered (0): none
- Needs an answer (0): none
- Must not list as required, may apply or also review (7): DBS-14, DBS-15, DBS-16, EVM-01, EVM-02, EVM-04, EVM-05
