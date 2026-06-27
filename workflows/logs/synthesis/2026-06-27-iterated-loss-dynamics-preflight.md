---
document_type: synthesis_preflight
source_queue_item: fourth_batch_5
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
source_open_problem: open-problems/iterated-loss-dynamics.md
---

# Iterated Loss Dynamics Preflight

## Status

Non-authoritative preflight artifact for fourth-batch task 5. This file does
not edit claim, roadmap, test, model, result, README, or open-problem surfaces.
It does not promote iterated loss to a main research line.

## Read Surfaces

- `open-problems/iterated-loss-dynamics.md`.
- `tests/T69-losskernel-failure-type.md`.
- `tests/T73-losskernel-composition.md`.

## Preflight Question

The source open problem asks whether repeated traversal of a finite typed
morphism, projection, transport loop, or restriction operator exposes behavior
invisible from the one-step `LossKernel(T)`.

The first executable artifact must distinguish two outcomes:

```text
nontrivial_iterated_behavior
ordinary_T73_union_saturation
```

The burden is not to name a new taxonomy. The burden is to show at least one
bounded finite operator where `LossKernel(T^n)` carries information not already
explained by the one-step kernel plus the T73 finite powerset-union law.

## Current Constraints From T69 And T73

T69 is a finite-family diagnostic for failure-type behavior. It is not a
general Cech or sheaf-cohomology theorem. Any use of failure type must state
the exact finite cover, coefficient/support semantics, and allowed loss
morphism class.

T73 verifies the current composition law:

```text
LossKernel(g after f) = LossKernel(f) union LossKernel(g)
```

This means a first iterated-loss run must actively try to kill itself as
ordinary label accumulation. A larger loss set after more steps is not enough.

## Frozen Object Required Before Execution

Any future executable run-card must freeze these fields before computing the
trajectory:

| Field | Required content |
| --- | --- |
| `operator_id` | Named finite operator `T`. |
| `operator_class` | Morphism, projection, transport loop, restriction, or finite composite. |
| `source_state_space` | Finite state, cover, or typed-structure family. |
| `losskernel_definition` | Symbolic definition used for every power without retuning. |
| `power_semantics` | How `T^2, ..., T^n` are composed. |
| `horizon_n` | Fixed iteration horizon. |
| `failure_type_semantics` | `none`, `H0`, or `H1` definitions, if used. |
| `holonomy_semantics` | Loop value definition, if used. |
| `T73_union_baseline` | Baseline trajectory predicted by ordinary union accumulation. |
| `falsification_condition` | Condition under which the proposed recurrence or invariant fails. |

If the run uses GU-adjacent geometry, the fixture must be described only as a
finite geometry-generating harness. It must not be described as GU physics.

## Required Control Family

The first run must include at least four controls:

| Control | Required behavior |
| --- | --- |
| Fixed loss | `LossKernel(T^n)` stabilizes immediately and shows no new information. |
| Monotone saturation | Loss grows only by finite union and is fully explained by T73. |
| Period-2 recurrence | A bounded fixture where a symbolic feature alternates, if such a fixture is predeclared. |
| Cycle-destroying degradation | A T69-style case where failure type or cycle data degrades under allowed loss. |

The period-2 and degradation controls may fail. If they fail, the artifact
must say so directly rather than rename the failure as evidence.

## Feature Extraction

For each trajectory `T, T^2, ..., T^n`, extract at minimum:

```text
loss_size
loss_type_vector
newly_lost_dimensions
preserved_invariant_count
failure_type
cycle_destroying
topology_preserved
holonomy_value_when_defined
recurrence_period
stabilization_time
projection_target_class
explained_by_T73_union_baseline
```

Feature extraction is for example discovery and classification. It must not
replace the symbolic `LossKernel` definitions.

## Acceptance Criteria

The next artifact is accepted as decision-grade only if all of the following
hold:

- `T`, the state space, and horizon are frozen before computing the trajectory.
- The same `LossKernel` definition is used for every power.
- `T73_union_baseline` is computed and reported.
- The run contains fixed-loss and monotone-saturation null controls.
- Any failure-type claim uses T69's finite-family caveats.
- Any holonomy or loop feature is computed from a finite declared loop object.
- At least one candidate witness is classified as one of:

```text
nontrivial_iterated_behavior
ordinary_T73_union_saturation
example_generator_only
inconclusive_missing_semantics
```

- `nontrivial_iterated_behavior` is allowed only if the trajectory shows a
  predeclared invariant, recurrence, failure-type change, or holonomy pattern
  not recoverable from the one-step kernel plus the T73 union baseline.
- A miss is recorded as evidence against the iterated-loss bet rather than a
  reason to relax the definitions.

## Null Or Demotion Conditions

Demote or kill the iterated-loss bet if any condition holds:

- Every witness reduces to one-step `LossKernel(T)` plus ordinary finite union
  saturation.
- The only apparent recurrence is a hand-chosen label sequence.
- The `LossKernel` definition changes across powers or fixtures.
- T69 failure-type language is used outside its stated finite morphism class.
- A GU-adjacent fixture is treated as validated physics.
- Feature clustering replaces the symbolic loss calculation.
- A recurrence taxonomy is promoted before a nontrivial witness family exists.
- The proposed result cannot distinguish fixed loss from monotone saturation.
- The run hides a changing operator behind the notation `T^n`.

Null result language to preserve:

```text
The iterated-loss run did not expose information beyond one-step LossKernel
and T73 union accumulation. Iteration remains an example generator or
visualization layer, not an algebra extension or independent research line.
```

## No-Promotion Guardrails

- Do not promote iterated loss to a main research line from a first bounded
  witness.
- Do not call the result a new categorical object if it is only powerset-union
  annotation.
- Do not promote a recurrence taxonomy before at least one nontrivial finite
  witness survives the T73 baseline.
- Do not promote physics, GU, geometry, holonomy, consciousness, or
  spacetime-language claims from this run.
- Do not use T69 as a general cohomology theorem.
- Do not use the open-problem's tentative `T101` label without checking the
  current test registry; use a new available T-number if implementation is
  later authorized.
- Do not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, tests, models, results, README,
  or open-problem files from this preflight.

## Next Executable Artifact Shape

Recommended next artifact:

```text
workflows/logs/synthesis/YYYY-MM-DD-iterated-loss-dynamics-run-card.md
```

Required run-card sections:

```text
operator_packet
losskernel_definition
power_semantics
horizon
control_family
T73_union_baseline
trajectory_table
feature_extraction
failure_type_caveats
holonomy_or_loop_caveats
comparison_to_baseline
verdict
no_promotion_guardrail_check
```

Minimum trajectory record:

```text
artifact_type: iterated_loss_dynamics_run_card
operator_id:
operator_class:
horizon_n:
losskernel_definition_frozen: true
T73_union_baseline:
trajectory:
  - power:
    losskernel:
    failure_type:
    cycle_destroying:
    holonomy_value:
    explained_by_T73_union_baseline:
detected_period:
stabilization_time:
final_verdict:
  nontrivial_iterated_behavior |
  ordinary_T73_union_saturation |
  example_generator_only |
  inconclusive_missing_semantics
claim_impact: no_status_change
```

If later authorized for implementation, convert the run-card into a
test/model/results triplet only after the run-card freezes its semantics:

```text
tests/TXXX-iterated-loss-dynamics.md
models/run_iterated_loss_dynamics.py
results/iterated-loss-dynamics-v0.1-results.md
```

