# D1: Physical Finality Definition

## Claim

Physical finality is a comparative, observer-indexed schema over record
properties, not one universal physical quantity. The v0.1 preorder compares
accessible support, holder redundancy, independent branch support, and a
named reversal cost componentwise, but each dimension must be justified for
the substrate in which it is used. T22 adds a physical reduction-map audit:
holder redundancy has the first executable observable comparison, while
branch support and reversal cost remain formal-only in strong physical claims.
T23 adds a typed invariant-transport view: D1 observer access and holder
redundancy can be preserved through explicit maps, but this does not make D1
an independent physical theory.
T24 adds a multiscale field audit: the local D1 profile is retained, while
cross-observer and institutional claims require a field-valued extension.
T25 narrows that extension: the smallest earned multiscale object is a finite
graph-indexed local-to-global D1 restriction system, not full sheaf language.
T26 formalizes that object as `D1RestrictionSystem`, with scalar and vector
D1 as projections from the finite local-to-global structure.

## Class

Definition.

## Status

Weakened.

## What This Does Not Claim

- Finality is not absolute metaphysical impossibility.
- Finality is not a magic moment in time.
- Finality is not social agreement.
- The four graph quantities are not claimed to be a complete physical measure.
- Graph reversal count is not thermodynamic work.
- The four dimensions do not automatically emerge as independent quantities
  from local dynamics.
- T22 does not show that all four D1 dimensions are physically reduced.
- Reversal cost is not identified with thermodynamic work by default.
- T23 does not show that D1 is equivalent to consensus, quantum measurement,
  or any other domain.
- T24 does not replace the D1 profile with a social or institutional scalar.
- T25 does not prove full D1 sheaf theory or a full IPT representation theorem.
- T26 does not complete the physical reduction of D1; it formalizes the
  multiscale bookkeeping object.

## Why It Might Be True

Classical records can differ by redundancy, accessibility, causal
independence, and reversal cost. Keeping these dimensions separate prevents a
weighted scalar from hiding disagreement. The Emergence Laboratory shows that
access and branch structure can remain distinct, while raw binary support,
redundancy, and terminal intervention cost collapse to one Hamming count.

## How It Could Fail

- The dimensions are insufficient, redundant, or not physically meaningful.
- The graph definitions fail to survive a physics-grounded model.
- Finality becomes too broad and merely renames entropy, decoherence, or information.
- Observer-indexing contributes no useful distinction beyond bounded access.
- A proposed dimension is only a re-description of another dimension in every
  implementation.

## Tests

- [T1: Record Graph Temporal Reconstruction](../tests/T1-record-graph-temporal-reconstruction.md)
- [T2: Quantum Measurement Record Finality](../tests/T2-quantum-measurement-record-finality.md)
- [T5: Thermodynamic Record Support](../tests/T5-thermodynamic-record-support.md)
- [T17: Consensus Finality Crosswalk](../tests/T17-consensus-finality-crosswalk.md)
- [T20: Consensus-Record Theorem Transfer](../tests/T20-consensus-record-theorem-transfer.md)
- [T21: Bell Contextuality Finality](../tests/T21-bell-contextuality-finality.md)
- [T22: D1 Physical Reduction Map](../tests/T22-d1-physical-reduction-map.md)
- [T23: Invariant-Preserving Transformations](../tests/T23-invariant-preserving-transformations.md)
- [T24: D1 Multiscale Observer Field](../tests/T24-d1-multiscale-observer-field.md)
- [T25: Minimal D1 Generalization](../tests/T25-minimal-d1-generalization.md)
- [T26: D1 Restriction System](../tests/T26-d1-restriction-system.md)

## Contribution Needed

Build a dynamical observer-system and test which dimensions remain distinct
when storage, reconciliation, and action arise inside the model.

## Formal Definition

See [FORMALISM.md](../FORMALISM.md) and the executable implementation in
[`models/t1_record_graph.py`](../models/t1_record_graph.py).

## Emergence Laboratory Result

[T9](../tests/T9-emergence-laboratory.md) shows that counterfactual record
traces and observer-relative access work on reversible and irreversible local
dynamics. It also shows that logical information loss is neither necessary
nor sufficient for an observer-accessible trace, and that three raw profile
dimensions collapse in the simplest binary model.

## Consensus Finality Crosswalk Result

[T17](../tests/T17-consensus-finality-crosswalk.md) shows that distributed
finality definitions collapse or project D1 dimensions. Safety ignores
independent branch support, economic finality keeps only reversal cost, and
liveness is a protocol progress condition rather than a D1 dimension.

The bounded theorem check verifies that no admissible configuration in the
stated finite model jointly maximizes support, redundancy, branch support,
reversal cost, and bounded progress. This strengthens D1's reason to keep
dimensions separate: scalar "more final" language would hide the tradeoff.

## Consensus-Record Theorem Transfer Result

[T20](../tests/T20-consensus-record-theorem-transfer.md) gives holder
redundancy a theorem-bearing role. Redundant-holder overlap is the
physical-record analogue of quorum intersection: when `2q > n`, incompatible
certificates must share a holder, and local consistency blocks contradictory
finalization.

This supports D1's holder-redundancy dimension while preserving the caveat
that global-section existence requires T13/sheaf structure beyond quorum
safety.

## Bell Contextuality Finality Result

[T21](../tests/T21-bell-contextuality-finality.md) shows why D1 finality must
remain observer- and context-indexed. Local measurement contexts can each have
valid finality sections while no single global assignment exists. That makes
global-section existence a separate condition, not something guaranteed by
local support or redundancy alone.

## D1 Physical Reduction Map Result

[T22](../tests/T22-d1-physical-reduction-map.md) audits all four D1 dimensions
against candidate physical observables. The current confidence levels are:

| D1 dimension | Confidence | T22 verdict |
| --- | --- | --- |
| accessible support | partially supported | Measurable once an observer access boundary is declared. |
| holder redundancy | partially supported | Matches an independence-corrected Quantum-Darwinism-style `R_delta` count in the toy model. |
| branch support | formal only | Structurally useful, but physical branch independence remains open. |
| reversal cost | formal only | Requires a named cost model and is not thermodynamic work by default. |

The executable toy model gives:

```text
(accessible support, holder redundancy, branch support, reversal cost)
= (3, 2, 2, 2)
```

The positive result is narrow: holder redundancy agrees with an
independence-corrected accessible environmental redundancy count after the
pointer basis, fragment partition, access boundary, and information threshold
are fixed. D1 should therefore claim a candidate observable program, not a
completed physical definition.

## Quantum Measurement Finality Result

[T2](../tests/T2-quantum-measurement-record-finality.md) tests the T22 map in
a dynamical system-apparatus-environment substrate. Reversible CNOT
interactions generate the apparatus record and three environment fragments.

T2 strengthens D1's accessible-support distinction. In the final stage,
environmental `R_delta = 3` and pointer coherence is `0.0`, but an outside
observer with no access has:

```text
D1 = (0, 0, 0, 0)
```

This shows that decoherence and environmental redundancy do not by themselves
settle observer-relative finality. The same result keeps D1 weakened: branch
support remains `1` in the toy model because all records descend from one
pointer-measurement root, and reversal cost is only an inverse-operation
proxy.

## Invariant-Preserving Transformations Result

[T23](../tests/T23-invariant-preserving-transformations.md) treats D1 as one
participant in a typed invariant-transport kernel. Two D1-relevant reductions
pass:

- a T2 global measurement state restricts to a local observer D1 view while
  preserving pointer basis and system-record correlation;
- a T2 local observer D1 view reduces to the T22 observable schema while
  preserving holder redundancy, accessible support, pointer basis, and
  observer-access indexing.

This strengthens D1 as a transportable formal object, but it does not restore
the original broad physical claim. D1 remains weakened because branch support
and reversal cost still lack strong physical reductions, and T23 provides a
finite kernel rather than a representation theorem.

## Multiscale Observer Field Result

[T24](../tests/T24-d1-multiscale-observer-field.md) tests whether D1 should be
represented as a scalar, vector, or field across observer populations and
scales.

The result is:

```text
retain existing D1 local profile
introduce field-valued D1 extension
do not replace D1
```

Scalar D1 is recovered when one observer is fixed or when all observer sites
share the same profile over trusted connected transport. Outside those
assumptions, scalar reduction loses information. A vector captures multiple
observer profiles, but it still loses communication, trust, transport, and
gluing data. For multiscale claims, the recommended object is a D1 field:

```text
observer/scale/time site -> D1 profile
```

with transport edges and local-to-global gluing constraints.

## Minimal D1 Generalization Result

[T25](../tests/T25-minimal-d1-generalization.md) explicitly compares scalar,
vector, field-like, sheaf-like, and noncanonical alternatives.

The best-supported hypothesis is:

```text
H3: another finite local-to-global structure is required
```

The recommended next object is:

```text
GraphD1Restriction = (
  local D1 profiles,
  observer sites,
  trusted transport edges,
  optional patch constraints
)
```

This preserves D1's local profile while preventing overclaiming. Scalar D1
remains valid for fixed-observer or uniform cases. Vector D1 is enough for
observer-distribution snapshots. Graph-indexed restriction is needed when
transport or gluing matters. Full sheaf semantics and full IPT representation
remain deferred.

## D1 Restriction System Result

[T26](../tests/T26-d1-restriction-system.md) implements the T25 recommendation
as:

```text
D1RestrictionSystem = (
  finite observer sites,
  one local D1 profile per site,
  one proposition value per site,
  trusted transport edges,
  optional overlap tests,
  optional finite patch constraints,
  scalar and vector projection maps,
  compatibility and global-section predicates
)
```

The best-supported T26 hypothesis is:

```text
H1: finite graph-indexed D1 restriction system is sufficient
```

This strengthens D1's formal side without restoring a stronger physical claim.
Scalar D1 is now a fixed-site or uniform projection. Vector D1 is an
observer-distribution projection. Transport and gluing claims require the
restriction-system data. Full sheaf semantics and full IPT representation
remain deferred.
