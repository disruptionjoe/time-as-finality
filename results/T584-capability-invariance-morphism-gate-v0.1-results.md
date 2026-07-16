# T584 Results: Capability Invariance Morphism Gate

## Verdict

- Verdict: `CAPABILITY_INVARIANCE_MORPHISMS_SURVIVE_FINITE_GATE_REVIEW_ONLY`
- Source contract: T583 CapabilityContract v1

## Morphism Audits

| morphism | kind | admissible? | relation | passed? | substantive change |
| --- | --- | :---: | --- | :---: | --- |
| `unit_and_interface_representation` | `representation` | True | `EQUIVALENT` | True | raw tasks, units, protocol labels, and implementation traces differ |
| `gauge_orbit_phase_shift` | `gauge` | True | `EQUIVALENT` | True | gauge phase and representative differ |
| `telemetry_coarse_graining` | `irrelevant_coarse_graining` | True | `EQUIVALENT` | True | telemetry and display fields are removed |
| `task_vocabulary_merge_counterexample` | `inadmissible_task_coarse_graining` | False | `INCOMPARABLE` | True | certification task is merged into recovery task |

## Checks

| check | passed? | reason |
| --- | :---: | --- |
| `admissible_morphisms_preserve_capability` | True | Representation, gauge, and irrelevant coarse-graining preserve the envelope. |
| `substantive_representation_change` | True | Representation changes raw units, interface names, and implementation traces. |
| `gauge_factors_through_quotient` | True | Gauge representative and phase changes do not create new capabilities. |
| `irrelevant_coarse_graining_stable` | True | Declared irrelevant metadata drops without changing the physical payload. |
| `task_merge_counterexample_caught` | True | Merging distinct task semantics changes the envelope and is rejected. |
| `capability_not_state_identity` | True | Different controller traces can remain capability-equivalent. |

## Survivor

In this finite fixture, capability factors through the declared representation, gauge, and irrelevant-coarse-graining quotient.

## Counterexample Boundary

The smallest found counterexample is a task-vocabulary merge: certification and recovery cannot be coarse-grained into one task without changing the native capability type.

## Claim Status

No claim-ledger or Canon Index update is earned.

## Not Claimed

T584 is a finite invariance gate only. It does not establish a universal capability measure, physical time, issuance, a source law, a genuine physical model, or cross-repo identity.

## Next Work

Instantiate the surviving quotient in a genuine physical system with source-derived states, operations, resources, costs, records, access, gauge quotient, and measured or law-derived task performance.
