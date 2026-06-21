# T142 Results: Thermodynamic Erasure Calibration

## Summary

The remaining H7 copy/branch-support survivors are absorbed by standard thermodynamic distinctions. With full source-copy correlation and reversible control they can be uncomputed without blind erasure; without that access, resetting the added record is ordinary erasure/free-energy accounting. D1 still distinguishes record topology at fixed erasure floor, but that does not by itself ground a physical arrow.

## T1 Calibrations

| Case | Strict D1 increase | D1 delta | Reverse modes | Verdict |
| --- | --- | --- | --- | --- |
| `access_grant_existing_record` | `True` | `[1, 1, 0, 1]` | `boundary_revoke` | `boundary_absorbed` |
| `copy_to_fresh_holder` | `True` | `[1, 1, 0, 1]` | `correlated_uncopy, blind_reset` | `reversible_or_landauer_absorbed` |
| `branch_spread_copy` | `True` | `[1, 1, 1, 1]` | `correlated_uncopy, blind_reset` | `reversible_or_landauer_absorbed` |
| `access_loss_without_erasure_control` | `False` | `[-1, -1, 0, -1]` | `boundary_revoke` | `non_arrow_control` |

## access_grant_existing_record

- Before profile: `[1, 1, 1, 0]`
- After profile: `[2, 2, 1, 1]`
- D1 delta: `[1, 1, 0, 1]`
- Overall verdict: `boundary_absorbed`
- Reason: The strict D1 increase is an access-profile change. It has no thermodynamic arrow content once access-control state is part of the substrate.

| Reverse mode | Erased bits | beta*W lower bound | Absorber | Verdict |
| --- | --- | --- | --- | --- |
| `boundary_revoke` | `0` | `0.0` | observer-boundary/accounting state | `reversible_boundary_change` |

## copy_to_fresh_holder

- Before profile: `[2, 2, 1, 0]`
- After profile: `[3, 3, 1, 1]`
- D1 delta: `[1, 1, 0, 1]`
- Overall verdict: `reversible_or_landauer_absorbed`
- Reason: The copy-based D1 increase has two ordinary reversals: zero blind-erasure cost if full correlation/control access permits uncopy, or a one-bit erasure/free-energy ledger if the copy is blindly reset.

| Reverse mode | Erased bits | beta*W lower bound | Absorber | Verdict |
| --- | --- | --- | --- | --- |
| `correlated_uncopy` | `0` | `0.0` | reversible computing with full correlation access | `reversible_when_full_microstate_available` |
| `blind_reset` | `1` | `0.6931471805599453` | Landauer-style erasure/free-energy accounting | `standard_erasure_cost_if_uncopy_unavailable` |

## branch_spread_copy

- Before profile: `[2, 2, 1, 1]`
- After profile: `[3, 3, 2, 2]`
- D1 delta: `[1, 1, 1, 1]`
- Overall verdict: `reversible_or_landauer_absorbed`
- Reason: The copy-based D1 increase has two ordinary reversals: zero blind-erasure cost if full correlation/control access permits uncopy, or a one-bit erasure/free-energy ledger if the copy is blindly reset.

| Reverse mode | Erased bits | beta*W lower bound | Absorber | Verdict |
| --- | --- | --- | --- | --- |
| `correlated_uncopy` | `0` | `0.0` | reversible computing with full correlation access | `reversible_when_full_microstate_available` |
| `blind_reset` | `1` | `0.6931471805599453` | Landauer-style erasure/free-energy accounting | `standard_erasure_cost_if_uncopy_unavailable` |

## access_loss_without_erasure_control

- Before profile: `[2, 2, 1, 1]`
- After profile: `[1, 1, 1, 0]`
- D1 delta: `[-1, -1, 0, -1]`
- Overall verdict: `non_arrow_control`
- Reason: The control is not a strict forward D1 increase and therefore does not supply an arrow-bearing calibration case.

| Reverse mode | Erased bits | beta*W lower bound | Absorber | Verdict |
| --- | --- | --- | --- | --- |
| `boundary_revoke` | `0` | `0.0` | observer-boundary/accounting state | `reversible_boundary_change` |

## Resource Drawdown Calibration

- Model: `test_c_resource_drawdown`
- Resource units drawn down: `3`
- Physical unit named: `False`
- Interpretation: If each unit is a blank record cell, recharge/reset is ordinary memory-preparation and erasure/free-energy accounting. If the unit is not physically typed, the finite drawdown is only an accounting token.
- Verdict: `not_physical_without_named_free_energy_or_capacity_unit`
- Reason: The T128 survivor becomes physics-facing only after the resource unit is mapped to a real free-energy, blank-memory, fuel, sink, or capacity variable. Otherwise it is a formal drawdown coordinate.

## What Improved

T142 separates three notions that were easy to conflate: D1 record topology, reversible uncopy under full microstate access, and blind erasure cost under coarse-grained reset. This makes the H7 thermodynamic absorber explicit.

## What Weakened

H7 cannot use T1 copy or branch-spread gains as independent thermodynamic-arrow evidence. Their reverse is either reversible with the correlation/control handle or absorbed by ordinary erasure/free-energy accounting. The T128 resource drawdown also stays formal until its resource unit is physically typed.

## Falsification Condition

T142 fails in H7's favor only if a physically typed record substrate gives a strict D1 increase whose reverse remains inadmissible after full reversible-correlation access, heat-bath erasure cost, blank-capacity use, sink state, and boundary conditions are all included and matched.

## H7 Update

Add T142 to H7: T1 copy/branch gains are thermodynamically absorbed, not arrow evidence. D1 topology can vary at fixed one-bit erasure floor, but reverse admissibility is still settled by reversible uncopy access or standard erasure/free-energy accounting.

## Claim Ledger Update

T142 calibrates the T141/T128 survivor against thermodynamic absorbers. Access grants are boundary changes; copied records can be reversed by correlated uncopy when the full handle remains, or by ordinary one-bit erasure/free-energy accounting when blindly reset. H7 remains a resource-accounting/constructor lemma, not a thermodynamic-arrow derivation.

## Open Blocker

Find a physically typed record substrate where D1 topology changes future operation availability at fixed free-energy, capacity, sink, boundary, provenance, and reversible-control data.

## Suggested Next

Either demote H7's paper-facing label to resource-accounting lemma, or attempt a non-equilibrium physical model with named free-energy and capacity variables fixed before D1 scoring.
