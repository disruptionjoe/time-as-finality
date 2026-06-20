# T81 Results: Measured Schema Ablation

Strongest claim: The current measured detector-provenance audit does not justify treating every T76 evidence field as equally load-bearing. Under single-category ablations, only trust-boundary evidence fully collapses the signed fixture, while incomplete pre-registration demotes it to a threshold-dependent result.

Weakened claim: In the current witness family, timing, retention/signature pass rates, spoof-resistance counts, perturbation counts, and DAG-summary counts are not independently decisive under single-category ablation. The executable detector branch is therefore narrower than the full T76 evidence schema suggests.

## Signed baseline

- verdict: `robust_measured_recovery`
- robust rate: `1.0`

## Single-category ablations

| Category | Verdict | Load-bearing | Robust rate | Threshold-dependent rate | Withhold rate |
| --- | --- | --- | --- | --- | --- |
| timing | robust_measured_recovery | False | 1.0 | 0.0 | 0.0 |
| retention_signature | robust_measured_recovery | False | 1.0 | 0.0 | 0.0 |
| spoof_resistance | robust_measured_recovery | False | 1.0 | 0.0 | 0.0 |
| trust_boundaries | measured_conservative_withhold | True | 0.0 | 0.0 | 1.0 |
| perturbation | robust_measured_recovery | False | 1.0 | 0.0 | 0.0 |
| dag_observability | robust_measured_recovery | False | 1.0 | 0.0 | 0.0 |
| preregistration | threshold_dependent_failure | True | 0.74 | 0.26 | 0.0 |

## Falsification condition

T81 fails if every declared T76 evidence category independently changes the signed fixture's verdict under a single-category ablation, or if trust-boundary and pre-registration ablations no longer change the verdict.

## Q1 update

Keep Q1 partially supported only as a measured detector-provenance audit, but narrow the current executable content: in this model the detector branch presently behaves mainly as a trust-boundary plus pre-registration gate, not as a fully identified use of all T76 evidence channels.

## Blocker

The canonical witness family does not yet make spoof, perturbation, or DAG evidence independently decisive. Those channels are argued for in prose, but not individually load-bearing in the current audit.

## Next move

Either compress the measured schema to the categories actually used by the executable audit, or extend the witness family and classifier so spoof, perturbation, and DAG evidence each control at least one false-independence or false-dependence boundary.
