# T111 Results: D1 Gauge-Invariance Audit

## Strongest Claim

All four tested D1 dimensions are invariant under pure finite relabeling/isomorphism gauge maps in the reference audit, and all four are covariant under explicit access-boundary refinement or coarsening. Boundary changes are observer-frame data, not gauge redundancy.

## Reference Profile

- Tuple order: `['accessible_support', 'distinct_holder_redundancy', 'causal_branch_support', 'graph_reversal_count']`
- Profile tuple: `[4, 2, 2, 2]`

## Allowed Transformations

- observer relabeling
- record-label permutation preserving incidence
- holder relabeling preserving independence partitions
- causal-graph isomorphism preserving reachability
- access-boundary refinement
- access-boundary coarsening

## Transformation Audit

| Transformation | Kind | Admissible | Pure gauge | Before | After | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| observer_relabeling | observer_relabeling | True | True | `[4, 2, 2, 2]` | `[4, 2, 2, 2]` | pure gauge transformation preserved all D1 dimensions |
| record_label_permutation | record_label_permutation | True | True | `[4, 2, 2, 2]` | `[4, 2, 2, 2]` | pure gauge transformation preserved all D1 dimensions |
| holder_relabeling_preserving_independence_partitions | holder_relabeling | True | True | `[4, 2, 2, 2]` | `[4, 2, 2, 2]` | pure gauge transformation preserved all D1 dimensions |
| causal_graph_isomorphism | causal_graph_isomorphism | True | True | `[4, 2, 2, 2]` | `[4, 2, 2, 2]` | pure gauge transformation preserved all D1 dimensions |
| access_boundary_refinement | access_boundary_refinement | True | False | `[4, 2, 2, 2]` | `[2, 2, 2, 0]` | access-boundary transformation is covariant physical boundary data, not pure gauge |
| access_boundary_coarsening | access_boundary_coarsening | True | False | `[4, 2, 2, 2]` | `[5, 3, 3, 3]` | access-boundary transformation is covariant physical boundary data, not pure gauge |
| negative_record_incidence_break | negative_control | False | False | `[4, 2, 2, 2]` | `[4, 1, 1, 2]` | negative control changed D1 dimensions without an admissible transport rule |
| negative_holder_partition_merge | negative_control | False | False | `[4, 2, 2, 2]` | `[4, 1, 2, 2]` | negative control changed D1 dimensions without an admissible transport rule |
| negative_causal_graph_nonisomorphism | negative_control | False | False | `[4, 2, 2, 2]` | `[4, 2, 1, 2]` | negative control changed D1 dimensions without an admissible transport rule |

## Dimension Classification

| Dimension | Pure gauge | Boundary maps | Negative-control failures | Future status |
| --- | --- | --- | --- | --- |
| accessible_support | invariant | covariant | none | eligible only as a boundary-indexed transported coordinate |
| distinct_holder_redundancy | invariant | covariant | negative_record_incidence_break, negative_holder_partition_merge | eligible only as a boundary-indexed transported coordinate |
| causal_branch_support | invariant | covariant | negative_record_incidence_break, negative_causal_graph_nonisomorphism | eligible only as a boundary-indexed transported coordinate |
| graph_reversal_count | invariant | covariant | none | eligible only as a boundary-indexed transported coordinate |

## Verdict Checks

- Pure gauge maps preserve all D1 dimensions: `True`
- Boundary maps are not treated as gauge: `True`
- Negative controls change alleged invariants: `True`
- No curvature/gravity/anomaly claim: `True`

## Guardrail

T111 supplies only an invariance/covariance entry condition for future finality-connection work. It gives no curvature, gravity, or anomaly-cancellation upgrade.

## Recommendation

Use the four D1 components as transportable boundary-indexed profile coordinates under the stated finite maps. Do not treat values across different access boundaries as one gauge-invariant physical scalar, and keep branch support and graph reversal count at formal status until separate physical reductions are supplied.

## Reproduction

```bash
python -m unittest tests.test_t111_d1_gauge_invariance_audit -v
python -m models.run_t111_d1_gauge_invariance
```
