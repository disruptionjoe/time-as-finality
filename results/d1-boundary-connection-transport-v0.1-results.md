# T125 Results: D1 Boundary-Connection Transport

## Strongest Claim

T125 implements a finite provenance-aware transport rule for boundary-indexed D1 profiles. Pure relabeling transports close as identity, access-boundary transports carry typed deltas, lossy loops retain residual boundary provenance, and hostile or scalarized maps are undefined.

## Boundary Objects

| Boundary | Profile | Provenance |
| --- | --- | --- |
| `B0` | `[4, 2, 2, 2]` | `['reference_boundary']` |
| `B0_observer_relabel` | `[4, 2, 2, 2]` | `['observer_relabeling']` |
| `B0_record_relabel` | `[4, 2, 2, 2]` | `['record_label_permutation']` |
| `B0_holder_relabel` | `[4, 2, 2, 2]` | `['holder_relabeling']` |
| `B0_causal_relabel` | `[4, 2, 2, 2]` | `['causal_graph_isomorphism']` |
| `B_refined` | `[2, 2, 2, 0]` | `['access_boundary_refinement']` |
| `B_coarsened` | `[5, 3, 3, 3]` | `['access_boundary_coarsening']` |
| `B_bad_record` | `[4, 1, 1, 2]` | `['negative_record_incidence_break']` |
| `B_bad_holder` | `[4, 1, 2, 2]` | `['negative_holder_partition_merge']` |
| `B_bad_causal` | `[4, 2, 1, 2]` | `['negative_causal_nonisomorphism']` |

## Transport Audit

| Arrow | Source | Target | Verdict | Transported profile |
| --- | --- | --- | --- | --- |
| `id_B0` | `B0` | `B0` | `identity` | `[4, 2, 2, 2]` |
| `id_B0_observer_relabel` | `B0_observer_relabel` | `B0_observer_relabel` | `identity` | `[4, 2, 2, 2]` |
| `id_B0_record_relabel` | `B0_record_relabel` | `B0_record_relabel` | `identity` | `[4, 2, 2, 2]` |
| `id_B0_holder_relabel` | `B0_holder_relabel` | `B0_holder_relabel` | `identity` | `[4, 2, 2, 2]` |
| `id_B0_causal_relabel` | `B0_causal_relabel` | `B0_causal_relabel` | `identity` | `[4, 2, 2, 2]` |
| `id_B_refined` | `B_refined` | `B_refined` | `identity` | `[2, 2, 2, 0]` |
| `id_B_coarsened` | `B_coarsened` | `B_coarsened` | `identity` | `[5, 3, 3, 3]` |
| `gauge_observer` | `B0` | `B0_observer_relabel` | `pure_gauge_identity_delta` | `[4, 2, 2, 2]` |
| `gauge_observer_back` | `B0_observer_relabel` | `B0` | `pure_gauge_identity_delta` | `[4, 2, 2, 2]` |
| `gauge_record` | `B0` | `B0_record_relabel` | `pure_gauge_identity_delta` | `[4, 2, 2, 2]` |
| `gauge_holder` | `B0` | `B0_holder_relabel` | `pure_gauge_identity_delta` | `[4, 2, 2, 2]` |
| `gauge_causal` | `B0` | `B0_causal_relabel` | `pure_gauge_identity_delta` | `[4, 2, 2, 2]` |
| `refine_access` | `B0` | `B_refined` | `boundary_delta` | `[2, 2, 2, 0]` |
| `restore_from_refined_trace` | `B_refined` | `B0` | `boundary_delta` | `[4, 2, 2, 2]` |
| `coarsen_access` | `B0` | `B_coarsened` | `boundary_delta` | `[5, 3, 3, 3]` |
| `restrict_from_coarsened` | `B_coarsened` | `B0` | `boundary_delta` | `[4, 2, 2, 2]` |
| `missing_boundary_provenance` | `B0` | `B_refined` | `undefined` | `None` |
| `bad_record_incidence` | `B0` | `B_bad_record` | `undefined` | `None` |
| `bad_holder_partition` | `B0` | `B_bad_holder` | `undefined` | `None` |
| `bad_causal_reachability` | `B0` | `B_bad_causal` | `undefined` | `None` |
| `scalarized_profile` | `B0` | `B0` | `undefined` | `None` |

## Composition Audit

| Composition | Arrows | Direct arrow | Verdict | Deltas preserved |
| --- | --- | --- | --- | --- |
| `pure_gauge_record_then_identity` | `['gauge_record', 'id_B0_record_relabel']` | `gauge_record` | `composes_with_declared_direct_effect` | `True` |
| `refine_then_restore` | `['refine_access', 'restore_from_refined_trace']` | `id_B0` | `composes_with_declared_direct_effect` | `True` |
| `coarsen_then_restrict` | `['coarsen_access', 'restrict_from_coarsened']` | `id_B0` | `composes_with_declared_direct_effect` | `True` |
| `undefined_middle_map` | `['missing_boundary_provenance', 'restore_from_refined_trace']` | `None` | `undefined_intermediate` | `False` |

## Closed-Loop Audit

| Loop | Arrows | Classification | Residual delta |
| --- | --- | --- | --- |
| `pure_observer_relabeling_loop` | `['gauge_observer', 'gauge_observer_back']` | `identity_loop` | `False` |
| `refinement_restore_with_trace_loop` | `['refine_access', 'restore_from_refined_trace']` | `closed_with_residual_boundary_delta` | `True` |
| `coarsen_restrict_lossy_boundary_loop` | `['coarsen_access', 'restrict_from_coarsened']` | `closed_with_residual_boundary_delta` | `True` |
| `hostile_missing_provenance_loop` | `['missing_boundary_provenance', 'restore_from_refined_trace']` | `undefined` | `True` |

## Verdict Checks

- Identity transports pass: `True`
- Pure gauge loops close: `True`
- Lossy loops report residual deltas: `True`
- Hostile maps are undefined: `True`

## What Improved

The finality gauge-theory branch now has a connection-definition prerequisite: identity, composition, and closed-loop behavior are auditable before any curvature or gravity language is allowed.

## What Weakened

This weakens curvature talk. Profile changes across access boundaries are not gauge-invariant field strength; they are boundary data unless a later theorem defines a real curvature object over these transports.

## Falsification Condition

T125 fails if an identity changes a D1 tuple, pure gauge transport changes a profile, composition discards intermediate provenance, a lossy boundary loop is treated as trivial, or a hostile map is silently repaired into an admissible transport.

## Claim Ledger Update

Add T125 to D1/D1-Field as a formal transport prerequisite: D1 profiles can be carried across declared finite boundary maps only with provenance-bearing deltas; no curvature, gravity, torsion, or physical observable upgrade follows.

## Open Blocker

No curvature functional, flatness criterion, continuum limit, Lorentzian covariance result, or physical reduction of branch support and reversal count exists.

## Suggested Next

Use T125 to define a minimal flatness/holonomy audit over boundary loops, but keep it finite and reject gravity language until a nontrivial loop invariant survives relabeling and access-boundary absorbers.

## Reproduction

```bash
python -m unittest tests.test_d1_boundary_connection_transport -v
python -m models.run_t125
```
