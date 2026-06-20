# Technical Report: D1 Gauge-Invariance Audit v0.1

## Claim Under Test

T111 asks which parts of the D1 finality profile survive finite changes of
description. The audited D1 tuple is:

```text
(
  accessible support,
  distinct-holder redundancy,
  causal branch support,
  graph reversal count
)
```

The goal is only an invariance/covariance audit. It is not a curvature,
gravity, or anomaly-cancellation result.

## Finite System

The executable model uses a finite causal record graph with two accessible
branches, one inaccessible auxiliary branch, holder independence partitions,
and an observer access boundary. The reference profile is:

```text
(4, 2, 2, 2)
```

The four components are computed as:

- accessible support: accessible active records supporting the target value;
- distinct-holder redundancy: independence classes represented by those
  records, not raw holder names;
- causal branch support: antichain width of accessible record events;
- graph reversal count: `max(0, accessible_support - threshold + 1)`.

## Allowed Transformations

The finite action contains:

- observer relabeling;
- record-label permutation preserving record-event and record-holder incidence;
- holder relabeling preserving independence partitions;
- causal-graph isomorphism preserving reachability;
- access-boundary refinement;
- access-boundary coarsening.

The first four are treated as pure gauge maps. Access-boundary refinement and
coarsening are not pure gauge: they change the observer-frame data on which
the D1 profile is evaluated.

## Result

All four D1 dimensions are invariant under the pure gauge maps in this finite
audit:

```text
(4, 2, 2, 2) -> (4, 2, 2, 2)
```

Access-boundary refinement is covariant, not invariant:

```text
(4, 2, 2, 2) -> (2, 2, 2, 0)
```

Access-boundary coarsening is also covariant:

```text
(4, 2, 2, 2) -> (5, 3, 3, 3)
```

The correct rule is to recompute the D1 profile over the transformed access
boundary. The value change is boundary data, not relabeling gauge.

## Negative Controls

Three non-admissible controls intentionally break preservation rules:

- record incidence break: `(4, 2, 2, 2) -> (4, 1, 1, 2)`;
- holder partition merge: `(4, 2, 2, 2) -> (4, 1, 2, 2)`;
- causal non-isomorphism: `(4, 2, 2, 2) -> (4, 2, 1, 2)`.

These controls show why the preservation clauses matter. Once incidence,
independence partitions, or reachability are not preserved, the D1 transport
rule is undefined rather than a gauge equivalence.

## Classification

| Dimension | Pure relabel/isomorphism maps | Access-boundary maps | Current physical status |
| --- | --- | --- | --- |
| accessible support | invariant | covariant | conditional on declared access boundary |
| distinct-holder redundancy | invariant | covariant | conditional on declared access boundary and independence partition |
| causal branch support | invariant | covariant | formal-only in current physical claims |
| graph reversal count | invariant | covariant | formal-only in current physical claims |

## Future-Connection Entry Condition

The four D1 components may be used as boundary-indexed transported profile
coordinates under the finite maps above. They should not be treated as one
access-independent physical scalar. A future connection-like formalism would
need to carry the access boundary as part of the base data and specify the
transport rule before comparing values across boundaries.

## Conservative Boundary

T111 does not strengthen D1 into a completed physical observable theory.
Accessible support and holder redundancy remain conditional on declared
access and partition data. Causal branch support and graph reversal count
remain formal-only until separate physical reductions are supplied.

No curvature, gravity, or anomaly-cancellation claim follows from this audit.

## Reproduction

```bash
python -m unittest tests.test_t111_d1_gauge_invariance_audit -v
python -m models.run_t111_d1_gauge_invariance
```
