# T77 Results: Measured Detector Policy Sensitivity

Policy-sensitivity audit over 400 samples per policy/deployment pair with deterministic seed 77023.

Strongest claim: The measured signed detector fixture is robust across strict, baseline, and permissive audit policies, but permissive policy loosening contaminates the discriminator by allowing a small timing-only unsigned recovery rate.

Weakened claim: T77 weakens the detector branch by exposing policy dependence directly. The signed fixture is not the fragile part; the fragile part is the control separation. Once policy becomes too permissive, the unsigned timing-only control begins to earn spurious positive classifications.

## Audit table

| Policy | Deployment | Verdict | Robust | Withhold | Threshold-dependent | False independence | False dependence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| strict | measured_signed_time_tag_stack | robust_under_policy | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| strict | timing_only_unsigned_control | withhold_under_policy | 0.0 | 1.0 | 0.0 | 0.0 | 0.0 |
| strict | signed_stack_incomplete_preregistration_control | threshold_dependent_under_policy | 0.695 | 0.0 | 0.305 | 0.0 | 0.0 |
| baseline | measured_signed_time_tag_stack | robust_under_policy | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| baseline | timing_only_unsigned_control | withhold_under_policy | 0.0 | 1.0 | 0.0 | 0.0 | 0.0 |
| baseline | signed_stack_incomplete_preregistration_control | threshold_dependent_under_policy | 0.68 | 0.0 | 0.32 | 0.0 | 0.0 |
| permissive | measured_signed_time_tag_stack | robust_under_policy | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| permissive | timing_only_unsigned_control | withhold_under_policy | 0.045 | 0.955 | 0.0 | 0.0 | 0.0 |
| permissive | signed_stack_incomplete_preregistration_control | threshold_dependent_under_policy | 0.675 | 0.0 | 0.325 | 0.0 | 0.0 |

## Falsification condition

Demote the detector branch if no pre-registered policy corridor keeps the signed measured deployment robust while simultaneously forcing the timing-only unsigned control to withhold and the incomplete-pre-registration control to remain threshold-dependent.

## Q1 update

Keep Q1 partially supported only as a measured detector-provenance claim inside an explicitly pre-registered policy corridor that preserves signed-versus-unsigned separation. The signed positive result is robust, but permissive policy already leaks timing-only false positives.

## Blocker

T77 still uses fixture-level measured counts rather than a real deployment log, so the policy corridor is executable but not yet empirically anchored.

## Next move

Derive a lab-facing policy floor: the loosest confidence and false-risk corridor that still preserves signed recovery, unsigned withhold, and incomplete-pre-registration failure.
