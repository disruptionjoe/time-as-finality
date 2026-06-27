---
document_type: synthesis_preflight
primary_reader: governance
read_pattern: current_state
write_pattern: append
authority: non_authoritative
summarizable: true
source_queue_item: third_batch_9
owner_line: RL-001
support_line: RL-004
claim_status_change: none
---

# Non-Static Boundary D1 Preflight

## Status

Non-authoritative preflight artifact for third-batch task 9. This file does
not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, code, tests, results, or
open-problem files. It does not reactivate the dormant open problem by itself,
does not upgrade D1, and does not claim that the heliosphere is a proved
finality domain.

## Read Surfaces

- `open-problems/finality-under-non-static-boundaries.md`.
- `CLAIM-LEDGER.md`: D1, D1-Field, R1, B1, H-Domain, and H-Soft-Boundary rows
  where relevant.
- `CLAIM-LEDGER.md`: 2026-06-22 D1 Boundary-Connection Transport entry.

## Preflight Verdict

Current classification:

```text
The non-static-boundary question remains dormant until a local D1-only moving
boundary object is named with provenance-bearing boundary transport and a
static-boundary null comparison.
```

The live issue is not whether a physical boundary can move in ordinary time.
The issue is whether D1 can express boundary change locally, without smuggling
in a global commit clock, and whether comparable-timescale records carry any
residue beyond a sequence of static-boundary profiles.

## Required D1 Object

Any future executable artifact must freeze:

| Field | Required content |
| --- | --- |
| `boundary_family` | Local finality-domain boundary states indexed by substrate data, not by a global clock alone. |
| `transport_map` | Provenance-bearing map between boundary-indexed D1 profiles. |
| `record_class` | Records whose stabilization scale is comparable to the boundary-change scale. |
| `local_phase_data` | Observable local marker of boundary transit or permeability change. |
| `static_null_model` | Sequence or mixture of fixed-boundary profiles that should absorb the effect if motion adds nothing. |
| `r1_constraint` | Check that no global commit order is introduced. |
| `observable_signature` | Predeclared record signature expected only in the sweep regime. |
| `hostile_control` | Case where ordinary access, density, coupling, or causal reachability explains the signature. |

## Acceptance Criteria

- Boundary change is defined as local substrate/profile change, not as a
  universal time parameter.
- D1 profiles are compared only through provenance-bearing boundary transport.
- The record class has stabilization scale comparable to the boundary-change
  scale; very fast and very slow limits are controls, not the main case.
- The observable signature is declared before any example is selected.
- The static-boundary null model is strong enough to absorb ordinary density,
  particle-flux, access-window, coupling, and causal-reachability effects.
- The R1 check confirms that the model does not introduce a global commit
  order.
- The output verdict is one of:

```text
moving_boundary_residue_survives_preflight
absorbed_by_static_boundary
underspecified_d1_boundary_object
```

`moving_boundary_residue_survives_preflight` means only that a later finite
fixture or formal note is worth building.

## Null Or Demotion Conditions

Treat the route as null, dormant, or demoted back to static-boundary treatment
if any condition holds:

- Boundary motion is expressed only by a background global clock.
- The record signature is explained by ordinary particle density, coupling,
  access, or causal reachability.
- The model is just a list of fixed-boundary D1 profiles with no residual
  provenance-bearing transport effect.
- Records are only in the easy limits: stabilization much shorter or much
  longer than the boundary-change scale.
- Boundary provenance is absent when comparing D1 tuples.
- The heliosphere example is used as a metaphor without a typed record class
  and static null.
- The construction violates R1 by imposing a universal order of finalization.
- No hostile control can distinguish moving-boundary residue from static
  boundary bookkeeping.

## No-Promotion Guardrails

- Do not upgrade D1 out of `weakened`.
- Do not upgrade D1-Field, R1, B1, H-Domain, H-Soft-Boundary, or S1.
- Do not claim a spacetime derivation, gravity result, curvature result,
  heliosphere proof, or black-hole-boundary result.
- Do not treat a returned D1 tuple as enough; boundary provenance must be
  carried.
- Do not use non-static boundaries to bypass the Q1, H7, or S1 reinstatement
  gates.
- Do not edit ledger, roadmap, tests, models, results, or open problems from
  this preflight.

## Next Executable Artifact Shape

The next artifact should be a finite D1 moving-boundary fixture or formal note
with this shape:

```text
artifact_type: non_static_boundary_d1_fixture
boundary_family_id:
local_substrate_parameters:
boundary_state_index:
record_class:
stabilization_scale:
boundary_change_scale:
transport_map:
  source_boundary_state:
  target_boundary_state:
  d1_profile_before:
  d1_profile_after:
  provenance_delta:
observable_signature:
static_null_model:
controls:
  fast_record_limit:
  slow_record_limit:
  ordinary_access_or_density_control:
  relabel_only_control:
r1_no_global_commit_order_check:
verdict: moving_boundary_residue_survives_preflight | absorbed_by_static_boundary | underspecified_d1_boundary_object
claim_impact: no_status_change
```

The first run should use one finite source family and one static-null
comparison, not a survey of boundary examples.
