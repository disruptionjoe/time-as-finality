# T76 Results: Measured Detector Provenance Posterior

Measured-posterior audit over 400 samples per deployment fixture with deterministic seed 76019.

Strongest claim: Detector-level D1 finality can be tested as a measured provenance-protocol claim: deployment evidence can be converted into T72/T74 posterior coordinates before D1 scoring.

Weakened claim: The measured-posterior adapter weakens T75 by replacing narrative posterior ranges with a required evidence schema. A detector stack without measured authentication, trust-boundary, perturbation, and DAG evidence does not earn D1 provenance recovery even when its timing evidence is unchanged.

## Deployment table

| Deployment | Verdict | Robust | Withhold | Threshold-dependent | False independence | False dependence | D1 computable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| measured_signed_time_tag_stack | robust_measured_recovery | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 |
| timing_only_unsigned_control | measured_conservative_withhold | 0.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| signed_stack_incomplete_preregistration_control | threshold_dependent_failure | 0.67 | 0.0 | 0.33 | 0.0 | 0.0 | 0.67 |

## Falsification condition

The detector branch should be demoted if a real deployment's measured posterior either withholds D1, produces false independence/dependence risk, or only succeeds after weakening pre-registered confidence and false-risk policy bounds.

## Q1 update

Keep Q1 partially supported only for measured, pre-registered detector provenance protocols; do not treat timing resolution alone as support.

## Next move

Populate this schema from an actual lab run: event-loss logs, signature failures, replay/forgery trials, perturbation controls, trust-boundary audits, and DAG truncation counts.
