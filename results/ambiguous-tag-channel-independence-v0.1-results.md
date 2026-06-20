# T86 Results: Ambiguous-Tag Channel Independence

Monte Carlo audit over 400 samples per raw-log fixture with deterministic seed 86037.

Strongest claim: Inside the current executable protocol, perturbation response and signed ancestry can be independently decisive when timing and authenticated tags are deliberately ambiguous. The result rescues those channels from immediate schema deletion, but only as pre-registered raw-log isolation tests.

Weakened claim: This does not upgrade Q1 into a detector theory. The same ambiguous-tag family with perturbation back-action or DAG truncation withholds D1 completely, so the channel claim is narrow and control-dependent.

## Fixture table

| Case | Channel | Role | Verdict | Rescue | Robust | Withhold | D1 computable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| all_channels_ambiguous_negative_control | none | negative_control | measured_conservative_withhold | False | 0.0 | 1.0 | 0.0 |
| clean_perturbation_only_rescue | perturbation_response | positive_test | robust_measured_recovery | True | 1.0 | 0.0 | 1.0 |
| backaction_contaminated_perturbation_control | perturbation_response | contamination_control | measured_conservative_withhold | False | 0.0 | 1.0 | 0.0 |
| clean_dag_only_rescue | signed_ancestry_dag | positive_test | robust_measured_recovery | True | 1.0 | 0.0 | 1.0 |
| truncated_dag_control | signed_ancestry_dag | contamination_control | measured_conservative_withhold | False | 0.0 | 1.0 | 0.0 |

## Falsification condition

T86 fails if the all-ambiguous negative control robustly recovers D1, if the clean perturbation-only or clean DAG-only families stop recovering both witness classes, or if the contaminated controls recover despite back-action/truncation.

## Q1 update

Keep Q1 partially supported only as a detector-record admissibility protocol. Perturbation and DAG channels may stay in the core schema only as independently isolated, pre-registered raw-log tests under ambiguous timing/tag controls; they are not empirical support until a T78-style real deployment supplies those logs.

## Blocker

The positive families are constructed fixture counts, not measured deployment logs. They also rely on the protocol's actual-class witness labels when computing whether recovery is correct, so the next real test must define copied and independent controls before data collection.

## Next move

Draft the T78 raw-log table needed for a real ambiguous-tag deployment: paired copied/independent controls, perturbation trials, signed ancestry exports, tag ambiguity rates, timing uncertainty, and pre-registered demotion rules.
