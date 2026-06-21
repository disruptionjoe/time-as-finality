# T126 Results: Finality-Colimit Causal-Set Embeddability Audit

## Aggregate Checks

- Descent failures blocked before causal-set claims: True
- T16 control passes causal-set gate: True
- Invalid relations rejected: True
- Valid posets can fail manifold filter: True
- Passing filter does not derive spacetime: True

## Audit Table

| Case | Classification | Causet candidate | Manifold filter | Events | Height | Width | Link density | Required next |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| `t16_positive_poset_control` | `insufficient_scale` | `True` | `False` | 4 | 4 | 1 | 1/2 (0.500) | Use the candidate only as a causal-set gate control or build a larger colimit. |
| `t16_partial_order_control` | `insufficient_scale` | `True` | `False` | 4 | 2 | 2 | 1/1 (1.000) | Use the candidate only as a causal-set gate control or build a larger colimit. |
| `descent_failure_control` | `not_descent_datum` | `False` | `False` | - | - | - | - | Repair event maps, overlap witnesses, record maps, and axis agreement first. |
| `noncanonical_boundary_control` | `noncanonical_colimit` | `False` | `False` | - | - | - | - | Supply descent data that select a unique event-finality colimit. |
| `cyclic_relation_control` | `not_poset` | `False` | `False` | - | - | - | - | Produce a reflexive, antisymmetric, transitive colimit relation before causal-set screening. |
| `phantom_gap_control` | `phantom_gap_unresolved` | `False` | `False` | 3 | 2 | 2 | 1/1 (1.000) | Separate observer-apparent order from ambient event-finality order before T126. |
| `hub_order_control` | `hub_nonlocality_obstruction` | `True` | `False` | 8 | 2 | 7 | 1/1 (1.000) | Replace the hub order with a colimit whose covering relations are locally distributed. |
| `complete_bipartite_layer_control` | `interval_profile_obstruction` | `True` | `False` | 8 | 2 | 4 | 1/1 (1.000) | Supply intervals with nontrivial interior structure or lower the claim to a finite poset control. |
| `degenerate_chain_control` | `rank_width_obstruction` | `True` | `False` | 7 | 7 | 1 | 2/7 (0.286) | Declare a different comparison class or supply a less degenerate candidate. |
| `mixed_interval_profile_control` | `order_dimension_obstruction` | `True` | `False` | 8 | 4 | 3 | 7/11 (0.636) | Match interval profiles or use a named dimension estimator with a declared tolerance. |
| `grid_filter_pass_control` | `passes_filter_only` | `True` | `True` | 9 | 5 | 3 | 4/9 (0.444) | Compare against stronger causal-set dimension, sprinkling, locality, or continuum-limit diagnostics. |

## t16_positive_poset_control

- Classification: `insufficient_scale`
- Causal-set candidate: `True`
- Manifold filter passed: `False`
- Poset failures: ``
- Reason: The relation is a finite causal-set candidate, but the witness is too small for the selected manifoldlikeness diagnostics.
- Not claimed: Passing T126 is not a faithful embedding proof and does not derive spacetime, GR, metric structure, Lorentzian geometry, or continuum physics.

Diagnostics:

- Comparable fraction: 1/1 (1.000)
- Cover relation count: 3
- Largest cover hub fraction: 2/3 (0.667)
- Rank profile: `[1, 1, 1, 1]`
- Interval counts by size: `[{'size': 0, 'count': 3}, {'size': 1, 'count': 2}, {'size': 2, 'count': 1}]`
- Profile spread obstruction: `False`

## t16_partial_order_control

- Classification: `insufficient_scale`
- Causal-set candidate: `True`
- Manifold filter passed: `False`
- Poset failures: ``
- Reason: The relation is a finite causal-set candidate, but the witness is too small for the selected manifoldlikeness diagnostics.
- Not claimed: Passing T126 is not a faithful embedding proof and does not derive spacetime, GR, metric structure, Lorentzian geometry, or continuum physics.

Diagnostics:

- Comparable fraction: 1/3 (0.333)
- Cover relation count: 2
- Largest cover hub fraction: 1/3 (0.333)
- Rank profile: `[2, 2]`
- Interval counts by size: `[{'size': 0, 'count': 2}]`
- Profile spread obstruction: `False`

## descent_failure_control

- Classification: `not_descent_datum`
- Causal-set candidate: `False`
- Manifold filter passed: `False`
- Poset failures: `causet_gate_not_reached`
- Reason: The T54-style descent gate failed or is missing, so no causal-set embeddability claim is meaningful.
- Not claimed: Passing T126 is not a faithful embedding proof and does not derive spacetime, GR, metric structure, Lorentzian geometry, or continuum physics.

## noncanonical_boundary_control

- Classification: `noncanonical_colimit`
- Causal-set candidate: `False`
- Manifold filter passed: `False`
- Poset failures: `causet_gate_not_reached`
- Reason: The observer data admit more than one compatible completion, so there is no unique finality-colimit order to audit.
- Not claimed: Passing T126 is not a faithful embedding proof and does not derive spacetime, GR, metric structure, Lorentzian geometry, or continuum physics.

## cyclic_relation_control

- Classification: `not_poset`
- Causal-set candidate: `False`
- Manifold filter passed: `False`
- Poset failures: `antisymmetry_violation, transitivity_violation`
- Reason: The candidate relation is not a finite partial order: antisymmetry_violation, transitivity_violation.
- Not claimed: Passing T126 is not a faithful embedding proof and does not derive spacetime, GR, metric structure, Lorentzian geometry, or continuum physics.

## phantom_gap_control

- Classification: `phantom_gap_unresolved`
- Causal-set candidate: `False`
- Manifold filter passed: `False`
- Poset failures: ``
- Reason: Observer-apparent phantom gaps still change the strict order, so the tested relation is not yet the event-finality colimit.
- Not claimed: Passing T126 is not a faithful embedding proof and does not derive spacetime, GR, metric structure, Lorentzian geometry, or continuum physics.

Diagnostics:

- Comparable fraction: 2/3 (0.667)
- Cover relation count: 2
- Largest cover hub fraction: 1/1 (1.000)
- Rank profile: `[2, 1]`
- Interval counts by size: `[{'size': 0, 'count': 2}]`
- Profile spread obstruction: `False`

## hub_order_control

- Classification: `hub_nonlocality_obstruction`
- Causal-set candidate: `True`
- Manifold filter passed: `False`
- Poset failures: ``
- Reason: One event supplies covering links to most of the set, producing an unnatural universal-hub profile for this screen.
- Not claimed: Passing T126 is not a faithful embedding proof and does not derive spacetime, GR, metric structure, Lorentzian geometry, or continuum physics.

Diagnostics:

- Comparable fraction: 1/4 (0.250)
- Cover relation count: 7
- Largest cover hub fraction: 1/1 (1.000)
- Rank profile: `[1, 7]`
- Interval counts by size: `[{'size': 0, 'count': 7}]`
- Profile spread obstruction: `False`

## complete_bipartite_layer_control

- Classification: `interval_profile_obstruction`
- Causal-set candidate: `True`
- Manifold filter passed: `False`
- Poset failures: ``
- Reason: Almost every comparable pair is a covering link, leaving no Alexandrov-interval structure at this scale.
- Not claimed: Passing T126 is not a faithful embedding proof and does not derive spacetime, GR, metric structure, Lorentzian geometry, or continuum physics.

Diagnostics:

- Comparable fraction: 4/7 (0.571)
- Cover relation count: 16
- Largest cover hub fraction: 4/7 (0.571)
- Rank profile: `[4, 4]`
- Interval counts by size: `[{'size': 0, 'count': 16}]`
- Profile spread obstruction: `False`

## degenerate_chain_control

- Classification: `rank_width_obstruction`
- Causal-set candidate: `True`
- Manifold filter passed: `False`
- Poset failures: ``
- Reason: The rank/width profile is degenerate for the selected finite control class.
- Not claimed: Passing T126 is not a faithful embedding proof and does not derive spacetime, GR, metric structure, Lorentzian geometry, or continuum physics.

Diagnostics:

- Comparable fraction: 1/1 (1.000)
- Cover relation count: 6
- Largest cover hub fraction: 1/3 (0.333)
- Rank profile: `[1, 1, 1, 1, 1, 1, 1]`
- Interval counts by size: `[{'size': 0, 'count': 6}, {'size': 1, 'count': 5}, {'size': 2, 'count': 4}, {'size': 3, 'count': 3}, {'size': 4, 'count': 2}, {'size': 5, 'count': 1}]`
- Profile spread obstruction: `False`

## mixed_interval_profile_control

- Classification: `order_dimension_obstruction`
- Causal-set candidate: `True`
- Manifold filter passed: `False`
- Poset failures: ``
- Reason: Equal-size intervals have incompatible internal height/width profiles, so the local effective-dimension diagnostic is unstable.
- Not claimed: Passing T126 is not a faithful embedding proof and does not derive spacetime, GR, metric structure, Lorentzian geometry, or continuum physics.

Diagnostics:

- Comparable fraction: 11/28 (0.393)
- Cover relation count: 7
- Largest cover hub fraction: 2/7 (0.286)
- Rank profile: `[2, 3, 2, 1]`
- Interval counts by size: `[{'size': 0, 'count': 7}, {'size': 1, 'count': 2}, {'size': 2, 'count': 2}]`
- Profile spread obstruction: `True`

## grid_filter_pass_control

- Classification: `passes_filter_only`
- Causal-set candidate: `True`
- Manifold filter passed: `True`
- Poset failures: ``
- Reason: No selected finite obstruction was found. This is only a necessary-condition pass.
- Not claimed: Passing T126 is not a faithful embedding proof and does not derive spacetime, GR, metric structure, Lorentzian geometry, or continuum physics.

Diagnostics:

- Comparable fraction: 3/4 (0.750)
- Cover relation count: 12
- Largest cover hub fraction: 1/2 (0.500)
- Rank profile: `[1, 2, 3, 2, 1]`
- Interval counts by size: `[{'size': 0, 'count': 12}, {'size': 1, 'count': 6}, {'size': 2, 'count': 4}, {'size': 4, 'count': 4}, {'size': 7, 'count': 1}]`
- Profile spread obstruction: `False`

## Strongest Claim

A finite finality colimit is not automatically spacetime-like. It must first be canonical descent data, then a valid finite causal-set candidate, and only then may it face manifoldlikeness necessary-condition filters. T126 finds valid posets that fail those filters.

## What This Improved

T126 turns the S1 spacetime-colimit route into an executable screen with explicit rejection modes: malformed descent data, noncanonical completion, non-poset relations, unresolved phantom gaps, hub nonlocality, degenerate rank/width profiles, interval profile failures, and local dimension-profile inconsistency.

## What This Weakened

This weakens any reading of T16/T51/T52/T54 as a spacetime derivation. A successful finite colimit can be only a small causal-set candidate, and several valid finality orders are now explicitly rejected before S1 may claim manifold-facing content.

## Falsification Condition

T126 fails if a noncanonical or malformed observer colimit can legitimately be used as embeddability evidence, or if the selected finite diagnostics reject a known-good control after its scale, dimension class, and causal-set comparison target are declared.

## S1 Update

S1 remains an open formal target. Future S1 witnesses must clear descent/canonicality, causal-set validity, phantom-gap, and finite manifoldlikeness screens before claiming spacetime-reconstruction residue.

## Claim Ledger Update

Add T126 to S1: finite finality colimits now face an executable causal-set/manifoldlikeness necessary-condition audit. Passing the screen is filter-only, while valid-but-degenerate posets weaken spacetime-derivation language.

## Open Blocker

No continuum limit, faithful embedding theorem, Lorentzian metric reconstruction, QFT algebra, or covariance result exists for the surviving finite controls.

## Suggested Next

Connect a T54/T58 canonical colimit fixture directly to T126, then compare the survivors against a named causal-set dimension or sprinkling diagnostic instead of adding new spacetime prose.
