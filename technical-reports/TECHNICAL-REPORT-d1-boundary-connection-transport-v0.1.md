# Technical Report: D1 Boundary-Connection Transport v0.1

## Claim Under Test

T125 asks whether the T111 invariance audit can be extended into an explicit
finite transport rule for boundary-indexed D1 profiles.

The target is deliberately modest:

```text
boundary object + transport arrow + provenance-bearing delta
```

not curvature, gravity, torsion, anomaly cancellation, or a physical
observable upgrade.

## Boundary Object

The executable boundary object is:

```text
B = (
  boundary_id,
  finite D1 record system,
  D1 profile,
  provenance
)
```

The D1 tuple order is inherited from T111:

```text
(
  accessible_support,
  distinct_holder_redundancy,
  causal_branch_support,
  graph_reversal_count
)
```

The reference boundary has profile:

```text
(4, 2, 2, 2)
```

The refined and coarsened access boundaries have profiles:

```text
refined  = (2, 2, 2, 0)
coarsened = (5, 3, 3, 3)
```

## Transport Rule

Each transport arrow returns:

```text
transported_profile
boundary_delta
admissibility_verdict
provenance_trace
```

The boundary delta records profile before/after, operation kind, changed
records, changed holders, changed access boundary, changed reachability,
reversibility, and loss notes.

This delta is part of the transported object. It is not an error term and not
a gauge-invariant field strength.

## Result

T125 implements the first finite connection-prerequisite object for the
finality gauge-theory branch.

The audit verifies:

- identity transports preserve every fixture profile;
- pure observer, record, holder, and causal relabeling transports preserve the
  D1 tuple and carry only gauge provenance;
- access-boundary refinement and coarsening are admissible only as typed
  boundary deltas;
- composition preserves ordered intermediate provenance;
- closed pure-gauge loops return identity;
- closed access-boundary loops that return the same tuple still retain
  residual boundary provenance;
- hostile maps and scalarized-profile controls are undefined.

## Closed-Loop Boundary

The most important result is negative. A loop can return the same D1 tuple
without becoming gauge-trivial.

For example:

```text
B0 -> B_refined -> B0
```

returns `(4, 2, 2, 2)`, but the loop records that archive-holder access was
dropped and later restored from a retained boundary trace. T125 classifies it
as:

```text
closed_with_residual_boundary_delta
```

The same holds for the coarsen/restrict loop. Returning the same tuple is not
enough; the boundary history remains part of the transported object.

## Negative Controls

T125 rejects:

- missing boundary provenance;
- record-incidence break;
- holder-partition merge;
- causal-reachability non-isomorphism;
- scalarization of the D1 tuple before transport.

These controls prevent a future connection proposal from silently repairing
profile changes or hiding access-boundary data inside a scalar.

## What Improved

The finality gauge-theory branch now has an executable connection-definition
prerequisite.

Before any curvature or gravity language is allowed, a proposal must at least
say what its boundary objects are, how D1 profiles transport, whether identity
and composition hold, and whether closed loops are identity, residual-boundary,
or undefined.

## What Weakened

T125 weakens premature curvature language.

Profile changes across observer access boundaries are not automatically field
strength. In this finite model, they are boundary-indexed D1 changes with
provenance. A later curvature object would need an additional theorem over
these transports.

## Falsification Condition

T125 fails if:

- an identity transport changes a D1 tuple;
- pure gauge transport changes a profile;
- composition discards intermediate provenance;
- a lossy boundary loop is treated as trivial;
- a hostile map is silently repaired into admissible transport; or
- scalarization is accepted before tuple transport.

## Claim Ledger Update

D1 and D1-Field gain a formal transport prerequisite only:

```text
D1 profiles can be transported across declared finite boundary maps only with
provenance-bearing deltas.
```

No curvature, gravity, torsion, anomaly, spacetime, or physical-observable
upgrade follows from T125.

## Open Blocker

No curvature functional, flatness criterion, continuum limit, Lorentzian
covariance result, or physical reduction of branch support and graph reversal
count exists.

## Recommended Next Move

Use T125 to define a minimal flatness or holonomy audit over finite boundary
loops. The next artifact should still be a guardrail: reject gravity language
unless a nontrivial loop invariant survives relabeling and access-boundary
absorbers.

## Reproduction

```bash
python -m unittest tests.test_d1_boundary_connection_transport -v
python -m models.run_t125
```
