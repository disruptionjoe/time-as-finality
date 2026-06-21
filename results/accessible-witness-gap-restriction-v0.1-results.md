# T92 Results: Accessible-Witness Gap Restriction

Theorem status: `supported_with_explicit_boundaries`

## Audit Summary

| System | Classification | Ambient | Audit monotone | Stable typing | Gap closed | Violations | Non-lifting |
| --- | --- | --- | --- | --- | --- | ---: | ---: |
| t19_unary_accessible_witness_gap | conditional_theorem_witness | True | True | True | True | 0 | 2 |
| non_chain_joint_witness_gap | conditional_theorem_witness | True | True | True | True | 0 | 11 |
| semantic_relabeling_control | semantic_relabeling_boundary | True | True | False | False | 1 | 1 |
| audit_monotonicity_control | audit_monotonicity_boundary | True | False | True | False | 1 | 0 |

## Patch Tables

### t19_unary_accessible_witness_gap

| Patch | A(U) | F(U) | G(U) |
| --- | --- | --- | --- |
| U_int | R_obs, R_self_finality | R_obs | R_self_finality |
| U_one_external_witness | R_obs, R_self_finality | R_obs | R_self_finality |
| U_ext | R_obs, R_self_finality | R_obs, R_self_finality | empty |

### non_chain_joint_witness_gap

| Patch | A(U) | F(U) | G(U) |
| --- | --- | --- | --- |
| U_local | O_joint_self_finality, O_left_witness, O_obs | O_obs | O_joint_self_finality, O_left_witness |
| U_left | O_joint_self_finality, O_left_witness, O_obs | O_left_witness, O_obs | O_joint_self_finality |
| U_right | O_joint_self_finality, O_left_witness, O_obs | O_obs | O_joint_self_finality, O_left_witness |
| U_joint | O_joint_self_finality, O_left_witness, O_obs | O_joint_self_finality, O_left_witness, O_obs | empty |
| U_full | O_joint_self_finality, O_left_witness, O_obs | O_joint_self_finality, O_left_witness, O_obs | empty |

### semantic_relabeling_control

| Patch | A(U) | F(U) | G(U) |
| --- | --- | --- | --- |
| U_small | R_obs, R_self_finality | R_obs | R_self_finality |
| U_large | R_obs, R_self_finality | R_obs | R_self_finality |

### audit_monotonicity_control

| Patch | A(U) | F(U) | G(U) |
| --- | --- | --- | --- |
| U_small | R_obs, R_self_finality | R_obs, R_self_finality | empty |
| U_large | R_obs, R_self_finality | R_obs | R_self_finality |

## Strongest Claim

For finite typed proposition-domain accessible-witness systems, G(U)=A(U)-F(U) restricts contravariantly when ambient truth restricts, local auditability is monotone under patch inclusion, and proposition types are not relabeled under restriction. The T19 unary gap and a non-chain joint-witness gap both satisfy these conditions.

## Weakened Claim

T92 does not prove a general cohomology theorem or a consciousness claim. It shows that the T19 accessible-witness gap can join the T56-T58 H0 gap program only under explicit proposition-typing and audit-monotonicity hypotheses.

## Falsification Condition

T92 fails if a well-typed nested proposition-domain witness satisfies ambient restriction and audit monotonicity but has a larger-patch gap whose restriction is not a smaller-patch gap.

## Claim Update

C1 may be sharpened, not upgraded: the first-person/third-person finality gap has a finite degree-0 accessible-witness form with restriction closure for typed proposition-domain witness systems.

## Open Blocker

The result is still finite and conditional. It does not place FIRST-PERSON-FINALITY in a complexity class and does not identify T19 proposition gaps with T58 order-pair gaps.

## Suggested Next

Generalize the proof sketch into a short formal lemma, then test whether T19 proposition gaps and T58 order-pair gaps share a common typed gap category or only the same H0 failure shape.
