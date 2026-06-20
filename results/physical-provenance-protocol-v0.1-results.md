# T72 Results: Physical Provenance Protocol

Passive statistics held fixed: agreement 0.92; phi 0.84.

Strongest claim: A physical provenance protocol can fix D1 independence classes before finality scoring when at least one dependence channel and one independence channel clear declared reliability bounds from the protocol rather than ad hoc post hoc thresholds.

Weakened claim: The recovery is protocol-relative. If authentication, DAG observability, trust boundaries, and perturbation controls do not clear their declared reliability bounds, D1 must be withheld; in hostile regimes the protocol can create false independence or false dependence risk.

## Regime table

| Regime | Verdict | D1 computable | Threshold source |
| --- | --- | --- | --- |
| robust_recovery_protocol | robust_provenance_recovery | True | declared_physical_protocol |
| batched_clock_crypto_dag_recovery | robust_provenance_recovery | True | declared_physical_protocol |
| lossy_tags_clean_intervention_recovery | robust_provenance_recovery | True | declared_physical_protocol |
| ambiguous_withhold_low_trust | ambiguous_withhold_region | False | declared_physical_protocol |
| partial_dag_ad_hoc_threshold | ambiguous_withhold_threshold_dependent | False | ad_hoc_partial_dag_threshold |
| forged_tags_false_independence_risk | false_independence_risk | False | declared_physical_protocol |
| backaction_false_dependence_risk | false_dependence_risk | True | declared_physical_protocol |

## Minimal physical conditions

Non-arbitrary D1 detector finality requires declared clock/error bounds, authenticated tags or signed ancestry with high verification probability, trusted subsystem boundaries, bounded archive batching, and a perturbation channel whose back-action risk is below the protocol's false-risk ceiling.

## Q1 recommendation

Keep Q1 partially supported only as a detector-record provenance accounting framework under explicit physical protocol assumptions. Do not claim detector-level provenance recovery without those assumptions.

## Falsification condition

The detector branch should be demoted if physically realistic protocol parameters generically fall into withhold, false independence, or false dependence regimes, or if the acceptance floors cannot be justified independently of the desired D1 result.

## Next move

Replace the finite regime table with calibration data or a Monte Carlo protocol simulation over clock, signature, batching, DAG, trust, and back-action distributions.
