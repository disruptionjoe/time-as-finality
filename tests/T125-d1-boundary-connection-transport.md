# T125: D1 Boundary Connection Transport

## Status

Implemented v0.1. This is a finite connection-definition prerequisite, not a
curvature, gravity, torsion, anomaly, spacetime, or physical-observable
upgrade.

## Route

Gauge-theoretic reformulation / D1 boundary-indexed transport, following
[T111](T111-d1-gauge-invariance-audit.md) and the open
[finality gauge-theory problem](../open-problems/finality-gauge-theory-and-gravity.md).

## Question

Can D1 profiles be transported between observer access boundaries by an
explicit finite boundary-connection rule that preserves pure-gauge identity,
composition, closed-loop consistency, and provenance-bearing boundary deltas?

## Motivation

T111 completed the entry audit for this branch: pure observer, record, holder,
and causal relabeling maps preserve the four tested D1 dimensions, while
access-boundary refinement and coarsening are covariant boundary-data changes
rather than pure gauge. The next bounded goal is therefore not a physical
geometry result. It is a disciplined definition of transport for the
boundary-indexed D1 data that T111 left available.

This test is also constrained by the weakened status of
[D1](../claims/D1-physical-finality-definition.md): D1 is a comparative,
observer-indexed profile whose dimensions are not all physically reduced.
Branch support and graph reversal count remain formal-only in strong physical
claims. Any transport rule must preserve that status instead of converting the
profile into a single access-independent scalar.

The relativity and spacetime-facing anchors
[R1](../claims/R1-relativity-no-global-commit-order.md) and
[S1](../claims/S1-spacetime-consensus-envelope.md) supply only consistency
pressure: overlapping causal domains may reconcile locally, but there is no
assumed global commit order and no load-bearing spacetime derivation.

## Boundary Object

Define a finite boundary-indexed object:

```text
B = (
  observer_id,
  access_boundary,
  record_subgraph,
  holder_partition,
  causal_reachability,
  D1_profile,
  provenance
)
```

where the D1 profile keeps the T111 tuple order:

```text
accessible_support
distinct_holder_redundancy
causal_branch_support
graph_reversal_count
```

The provenance field must record enough information to distinguish:

- pure observer, record, holder, and causal relabeling;
- access-boundary refinement;
- access-boundary coarsening;
- overlap restriction;
- record addition or removal;
- holder-partition change;
- causal-reachability change.

## Construction

Build a finite transport category or groupoid-like test fixture whose objects
are boundary-indexed D1 systems and whose arrows are declared boundary maps.
The fixture should include the T111 reference system and at least one chain of
overlapping observer boundaries.

The transport rule for an arrow

```text
tau: B_i -> B_j
```

must return:

```text
transported_profile
boundary_delta
admissibility_verdict
provenance_trace
```

The `boundary_delta` must be provenance-bearing data, not a discarded
difference. It should state whether the profile changed because of a declared
boundary operation, because of pure relabeling, or because the map was not
admissible.

## Identity

For every boundary object `B`, define an identity transport:

```text
id_B: B -> B
```

Success requires:

- the transported profile equals the original D1 profile;
- the boundary delta is empty or explicitly typed as identity;
- the provenance trace records identity rather than omitting the check;
- no observer-access, holder, record-incidence, or causal-reachability data are
  changed.

## Composition

For composable boundary transports:

```text
B_i --tau_ij--> B_j --tau_jk--> B_k
```

define both:

```text
tau_jk after tau_ij
tau_ik
```

where `tau_ik` is the declared composite boundary map.

Success requires:

- the two transported profiles agree when the declared maps have the same
  provenance-preserving effect;
- composed boundary deltas retain the ordered provenance of intermediate
  operations;
- pure-gauge steps compose as pure gauge;
- boundary-changing steps compose as boundary data, not as erased gauge;
- non-admissible intermediate steps make the composite undefined rather than
  silently repaired.

## Closed-Loop Transport

Define finite loops of boundary objects:

```text
B_0 -> B_1 -> ... -> B_n -> B_0
```

At minimum include:

- a pure relabeling loop;
- a refinement followed by its declared inverse coarsening where the inverse is
  information-preserving in the fixture;
- an overlap-restriction loop across observers with a shared causal region;
- a hostile loop containing a non-admissible map.

Success requires:

- pure relabeling loops return the original D1 profile with identity delta;
- declared reversible boundary loops return the original profile only when the
  provenance proves that no boundary information was lost;
- lossy refinement/coarsening loops report residual boundary deltas rather than
  pretending to close;
- hostile loops are rejected or marked undefined.

## Provenance-Bearing Boundary Deltas

For every admissible non-identity transport, compute a typed delta:

```text
Delta(B_i, B_j) = (
  profile_before,
  profile_after,
  operation_kind,
  changed_records,
  changed_holders,
  changed_access_boundary,
  changed_reachability,
  reversible,
  loss_notes
)
```

The delta is part of the transported object. It is not an error term and not a
physical scalar. It exists to keep access-boundary changes visible.

The test should compare these deltas against the T111 result summary in
[d1-gauge-invariance-audit-v0.1-results.md](../results/d1-gauge-invariance-audit-v0.1-results.md):

- pure gauge maps preserve all four D1 dimensions;
- access-boundary refinement and coarsening are covariant boundary data;
- negative controls change quantities without an admissible transport rule.

## Negative Controls

Include hostile maps that intentionally break one preservation clause at a
time:

- record-incidence break;
- holder-partition merge or split without a declared independence-preserving
  rule;
- causal non-isomorphism that changes reachability;
- access-boundary change with missing provenance;
- composition through an undefined intermediate map;
- closed loop that discards records and then reintroduces only labels;
- scalarization control that collapses the D1 tuple before transport.

Each negative control must either be rejected or classified as undefined under
the transport rule. A changed D1 profile is not by itself a failure when the
change is a declared boundary delta; it is a failure only when the change is
treated as pure gauge or when provenance is missing.

## Success Criteria

- Define the finite boundary object and transport arrows explicitly.
- Prove or exhaustively test identity transport for every fixture object.
- Prove or exhaustively test composition for all declared composable arrows.
- Classify closed-loop transport as identity, residual boundary delta, or
  undefined.
- Preserve the T111 distinction between pure gauge and access-boundary data.
- Carry provenance-bearing boundary deltas through every non-identity
  transport.
- Keep all four D1 dimensions tuple-valued and boundary-indexed.
- Preserve D1's weakened status from the D1 claim.
- Stay compatible with R1's no-global-commit-order guardrail.
- Treat S1 only as an open formal target, not as a result of this test.

## Failure Criteria

- Boundary refinement or coarsening is treated as pure gauge.
- A profile change is accepted without provenance.
- Identity transport changes records, holders, access, reachability, or profile
  values.
- Composition discards intermediate boundary deltas.
- A closed loop is declared trivial after lossy boundary operations.
- Negative controls are silently repaired into admissible transports.
- The D1 tuple is collapsed into a scalar before transport.
- The test promotes a curvature, gravity, torsion, or anomaly claim.
- The test changes D1, R1, or S1 claim status directly.

## Claim Impact

If implemented and passed, T125 would supply the next formal object needed by
the finality gauge-theory branch:

```text
a finite provenance-aware transport rule for boundary-indexed D1 profiles
```

That would still be only a connection-definition prerequisite. It would not
establish a physical geometry, a spacetime derivation, or a new physical
observable.

## v0.1 Result

T125 is now implemented as a finite provenance-aware transport checker.

The executable artifact defines boundary objects, transport arrows,
boundary-delta records, composition audits, and closed-loop audits over the
T111 reference system.

The main result is:

```text
pure relabeling transports close as identity;
access-boundary transports carry typed deltas;
lossy or boundary-changing loops retain residual provenance;
hostile or scalarized maps are undefined.
```

The reference profile remains:

```text
(4, 2, 2, 2)
```

The access-refined and access-coarsened profiles are:

```text
refined  = (2, 2, 2, 0)
coarsened = (5, 3, 3, 3)
```

Pure gauge loops return identity. A refinement/restore loop and a
coarsen/restrict loop can return the same tuple, but they do not become
gauge-trivial: both retain residual boundary deltas. This is the central
guardrail for any future flatness or holonomy language.

Negative controls reject missing boundary provenance, record-incidence break,
holder-partition merge, causal non-isomorphism, and scalarization of the D1
tuple before transport.

## Executable Artifacts

```bash
python -m unittest tests.test_d1_boundary_connection_transport -v
python -m models.run_t125
```

Artifacts:

- [`models/d1_boundary_connection_transport.py`](../models/d1_boundary_connection_transport.py)
- [`models/run_t125.py`](../models/run_t125.py)
- [`tests/test_d1_boundary_connection_transport.py`](test_d1_boundary_connection_transport.py)
- [`results/d1-boundary-connection-transport-v0.1.json`](../results/d1-boundary-connection-transport-v0.1.json)
- [`results/d1-boundary-connection-transport-v0.1-results.md`](../results/d1-boundary-connection-transport-v0.1-results.md)
- [`technical-reports/TECHNICAL-REPORT-d1-boundary-connection-transport-v0.1.md`](../technical-reports/TECHNICAL-REPORT-d1-boundary-connection-transport-v0.1.md)

## Known Guardrails

- Gauge language is technical and must be earned by the finite maps.
- Access-boundary changes are observer-frame data, not coordinate artifacts.
- Provenance is load-bearing; a transported value without its boundary history
  is not enough.
- Branch support and graph reversal count remain formal-only in strong
  physical claims.
- No curvature, gravity, torsion, or anomaly claim follows from this spec.

## Contribution Needed

Define the next finite flatness or holonomy audit over the T125 transport
object. The next result should still reject curvature and gravity language
unless a nontrivial loop invariant survives pure relabeling and
access-boundary absorbers.
