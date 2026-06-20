# T113 Results: Gap Presheaf Classification

## Verdict

A typed subobject of H0(G), not raw H0(G), classifies phantom incomparability in the tested finite witness family.

## Aggregate Comparison

- Raw H0(G) equals phantoms: `False`
- Typed gap sections equal phantoms: `True`
- FRP restriction closure preserved: `True`
- Malformed controls rejected: `True`
- T53 noncanonical completions block raw classification: `True`

## Section Counts

- Raw gap sections: `13`
- Typed gap sections: `10`
- Phantom sections: `10`

## Hypothesis Results

### H_RAW_H0_CLASSIFIES: refuted

Raw H0(G), taken as all computed gap sections, classifies phantom incomparability.

Evidence: raw_gap_sections=13, phantom_sections=10; extra_raw=3, missing=0

### H_TYPED_SUBOBJECT_CLASSIFIES: supported

The endpoint-accessible, canonical, well-formed local-incomparability subobject of H0(G) classifies phantom witnesses in the finite family.

Evidence: typed_gap_sections=10, phantom_sections=10; extra_typed=0, missing=0

### H_FRP_CLOSURE_PRESERVED: supported

T57 FRP gap restriction closure remains intact for the T113 covers.

Evidence: hidden_intermediary_record_lattice: holds=True; branching_dependency_record_lattice: holds=True

### H_MALFORMED_CONTROLS_REJECTED: supported

Malformed/local-reversal controls are rejected before gap sections are called phantoms.

Evidence: local_reversal: invalid_local_order_control; malformed_extra_local_order: invalid_local_order_control

### H_T53_BOUNDARY: supported

T53 underdetermined completions block raw classification and remain diagnostic only.

Evidence: t51_positive_control: canonical_control, gaps=['t51_colimit_completion']; ambiguous_event_identity: noncanonical_blocks_classification, gaps=[]; axis_failing_valid_colimit: canonical_control, gaps=[]; hidden_record_repair: noncanonical_blocks_classification, gaps=['hidden_record_repair_completion']; nondefinable_overlap_boundary: diagnostic_only, gaps=[]

## Witness Table

| Source | Case | Observer | G(U) | Typed G(U) | Phantoms | Classification |
| --- | --- | --- | --- | --- | --- | --- |
| T51 | t51 | Observer_B | `[['e1_A_locking', 'e3_composite_locking']]` | `[['e1_A_locking', 'e3_composite_locking']]` | `[['e1_A_locking', 'e3_composite_locking']]` | typed_exact_match |
| T52 | t52 | Observer_A | `[['e1_alpha_locking', 'e4_delta_locking']]` | `[['e1_alpha_locking', 'e4_delta_locking']]` | `[['e1_alpha_locking', 'e4_delta_locking']]` | typed_exact_match |
| T52 | t52 | Observer_B | `[['e1_alpha_locking', 'e3_gamma_locking']]` | `[['e1_alpha_locking', 'e3_gamma_locking']]` | `[['e1_alpha_locking', 'e3_gamma_locking']]` | typed_exact_match |
| T56 | hidden_intermediary | U_P | `[['e_j', 'e_i']]` | `[['e_j', 'e_i']]` | `[['e_j', 'e_i']]` | typed_exact_match |
| T57 | hidden_intermediary_record_lattice | U_r1_r3 | `[['e_j', 'e_i']]` | `[['e_j', 'e_i']]` | `[['e_j', 'e_i']]` | typed_exact_match |
| T57 | branching_dependency_record_lattice | U_ra_rd | `[['e_a', 'e_d']]` | `[['e_a', 'e_d']]` | `[['e_a', 'e_d']]` | typed_exact_match |
| T57 | branching_dependency_record_lattice | U_rb_rd | `[['e_b', 'e_d']]` | `[['e_b', 'e_d']]` | `[['e_b', 'e_d']]` | typed_exact_match |
| T57 | branching_dependency_record_lattice | U_ra_rb_rd | `[['e_a', 'e_d'], ['e_b', 'e_d']]` | `[['e_a', 'e_d'], ['e_b', 'e_d']]` | `[['e_a', 'e_d'], ['e_b', 'e_d']]` | typed_exact_match |
| T53 | t51_positive_control:t51_colimit_completion | Observer_B | `[['e1_A_locking', 'e3_composite_locking']]` | `[['e1_A_locking', 'e3_composite_locking']]` | `[['e1_A_locking', 'e3_composite_locking']]` | typed_exact_match |
| T53 | hidden_record_repair:hidden_record_repair_completion | Observer_A | `[['e1', 'e2']]` | `[]` | `[]` | noncanonical_ambient_diagnostic |
| T53 | hidden_record_repair:hidden_record_repair_completion | Observer_B | `[['e1', 'e2']]` | `[]` | `[]` | noncanonical_ambient_diagnostic |
| T58_CONTROL | local_reversal | local_reversal | `[['a', 'b']]` | `[]` | `[]` | invalid_local_order_control |
| T113_CONTROL | malformed_extra_local_order | malformed_extra_local_order | `[]` | `[]` | `[]` | invalid_local_order_control |

## T53 Diagnostics

| Case | Verdict | Role | Unique | Gap-bearing completions |
| --- | --- | --- | --- | --- |
| t51_positive_control | canonical_axis_reconstructable | canonical_control | `True` | `['t51_colimit_completion']` |
| ambiguous_event_identity | underdetermined_noncanonical | noncanonical_blocks_classification | `False` | `[]` |
| axis_failing_valid_colimit | valid_partial_order_axis_failure | canonical_control | `True` | `[]` |
| hidden_record_repair | repairable_by_hidden_record | noncanonical_blocks_classification | `False` | `['hidden_record_repair_completion']` |
| nondefinable_overlap_boundary | nondefinable_projection | diagnostic_only | `False` | `[]` |

## FRP Gap Checks

| Cover | Closed | Violations | Non-lifting examples |
| --- | --- | ---: | ---: |
| hidden_intermediary_record_lattice | `True` | 0 | 1 |
| branching_dependency_record_lattice | `True` | 0 | 6 |

## Finding

T113 supports a conservative classification theorem for the finite TaF witnesses: after requiring endpoint access, a canonical ambient completion, F(U) subset A(U), and local incomparability, every typed gap section is an independently computed phantom witness and every phantom witness appears as a typed gap section. Raw H0(G) remains too broad because noncanonical T53 repairs and malformed local reversals create diagnostic gaps.

## Guardrails

- This does not validate Geometric Unity or any physical torsion tensor.
- This does not prove that F sheafifies to A.
- This does not derive finality-arrow direction.
- T53-style noncanonical completions remain completion-relative diagnostics.
