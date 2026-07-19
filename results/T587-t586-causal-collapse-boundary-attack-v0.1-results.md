# T587 Results: T586 Causal-Collapse Boundary Attack

## Verdict

- Verdict: `T586_DOWNGRADED_TO_TYPED_RECORD_PREREQUISITE_FILTER_REVIEW_ONLY`
- Source gate: `T586-record-capability-order-gate-v0.1`
- Source verdict: `RECORD_CAPABILITY_ORDER_FINITE_PARTIAL_ORDER_REVIEW_ONLY`

## Adjudication

T587 returns a downgrade. T586 has no relation-level residual beyond ordinary task-prerequisite dependency and is absorbed by the strongest standard dependency and causal comparators on the frozen event system. What survives is a typed record-prerequisite filter: it identifies which causal dependencies are issued-record prerequisites for executable tasks.

## Comparator Attack

| comparator | status | collapse result | record-only edges | comparator-only edges |
| --- | --- | --- | ---: | ---: |
| `ordinary_task_prerequisite_dependency` | `EQUAL` | `RELATION_LEVEL_COLLAPSE` | 0 | 0 |
| `strongest_standard_dependency_order` | `RECORD_SUBRELATION` | `ABSORBED_AS_TYPED_SUBRELATION` | 0 | 2 |
| `supplied_causal_order` | `RECORD_SUBRELATION` | `ABSORBED_AS_TYPED_SUBRELATION` | 0 | 2 |
| `clock_label_order` | `OVERLAP_ONLY` | `NO_COLLAPSE` | 2 | 6 |
| `entropy_rank_order` | `OVERLAP_ONLY` | `NO_COLLAPSE` | 2 | 6 |

## Boundary-Input Screen

| class | classification | counts? | reason |
| --- | --- | :---: | --- |
| `physical_record_production` | `RECORD_ORDER_ADMISSIBLE` | True | A stable produced record with a unique producer may support a task-prerequisite edge. |
| `access_change` | `ACCESS_COMPLETION_NOT_RECORD_SOURCE` | False | Changing who can read a record changes access; it does not issue a new produced record. |
| `capability_change` | `CAPABILITY_DELTA_NOT_RECORD_SOURCE_BY_ITSELF` | False | A changed envelope is evidence for capability comparison, not an event-order edge unless an issued record is consumed. |
| `final_boundary_selection` | `SECTION_CHOICE_NOT_RECORD_SOURCE` | False | Choosing a boundary or section is a metatheoretic selection unless the source model issues a record token. |
| `observer_readout` | `READOUT_NOT_RECORD_SOURCE_BY_ITSELF` | False | Readout may reveal a record; readout alone is not native record production. |
| `physical_intervention` | `CAUSAL_INPUT_NOT_RECORD_SOURCE_BY_ITSELF` | False | An intervention can be a causal parent without being an issued-record prerequisite. |
| `autonomous_feedback` | `FEEDBACK_REQUIRES_EXPLICIT_ISSUANCE_RULE` | False | Feedback counts only when the model emits a stable record consumed by a later executable task. |
| `edge_defect_degrees_of_freedom` | `STATE_VARIABLE_NOT_RECORD_SOURCE_BY_ITSELF` | False | Edge or defect degrees of freedom are source variables until an issuance rule turns them into records. |
| `continuous_source_flux` | `FLUX_REQUIRES_FROZEN_RECORD_PACKET` | False | Continuous flux must be discretized or recorded by a declared source rule before it can enter the record order. |
| `stochastic_input` | `SAMPLE_NOT_RECORD_SOURCE_BY_ITSELF` | False | Random input is not a record-order source unless the sampled outcome is issued as a stable record. |
| `native_record_issuance_rule` | `RECORD_ORDER_ADMISSIBLE` | True | A source-owned issuance rule is the explicit bridge from physical input to produced-record prerequisite. |

## Audits

| audit | passed? | result class | reason |
| --- | :---: | --- | --- |
| `ordinary_dependency_collapse_detected` | True | `COLLAPSES_TO_TASK_PREREQUISITE_DEPENDENCY` | The untyped task-prerequisite dependency comparator exactly reproduces T586. |
| `strongest_dependency_absorbs_record_order` | True | `RECORD_ORDER_IS_TYPED_SUBRELATION` | The strongest standard dependency comparator strictly contains the T586 record order. |
| `causal_order_absorbs_record_order` | True | `CAUSAL_SUPERSET_ABSORBS_RELATION` | Every T586 record-order edge is already causally ordered in the frozen fixture. |
| `boundary_input_firebreak` | True | `ONLY_ISSUED_RECORDS_COUNT` | Access, intervention, section choice, flux, stochastic input, and observer readout are not counted without an issued record consumed by a task. |

## Checks

| check | passed? | reason |
| --- | :---: | --- |
| `source_t586_review_only_available` | True | T586 supplies the finite review-only record-capability-order fixture. |
| `dependency_and_causal_comparators_attacked` | True | The ordinary-dependency, strongest-dependency, and causal comparators all reach a definite collapse/absorption result. |
| `boundary_classes_are_typed` | True | The boundary-input screen admits only explicit record production or native record issuance. |
| `no_relation_level_residual_claimed` | True | The only survivor is a typed filter over standard dependency/causal structure, not a new temporal relation. |

## Physical Result

The T586 Landauer fixture still distinguishes issued records from access changes, interventions, observer readouts, stochastic inputs, continuous flux, and section choices. That distinction is useful as a screen against boundary-input overread, but it does not derive physical time or an independent temporal order.

## Claim Status

No claim-ledger or Canon Index update is earned.

## Not Claimed

T587 does not prove time, temporal issuance, source-law novelty, causal-order replacement, a universal capability measure, TAF3, TAF8, S1, public-posture movement, external publication, or cross-repo truth.

## Next Work

Do not continue producing T-number scaffolds from T586 alone. Reopen Lane 1 only for a provenance-valid physical source packet, a frozen capability witness, or a sharper counterexample that changes the record-issuance contract.
