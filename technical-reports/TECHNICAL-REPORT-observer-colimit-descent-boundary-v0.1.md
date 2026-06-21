# Technical Report: Observer-Colimit Descent Boundary v0.1

## Summary

T53 tests the boundary after T51's multi-observer apparent-finality colimit.
T51 showed that a bounded observer can see a phantom incomparability: an event
pair appears unordered in the observer's accessible records, but the ordering
reappears in the merged event-finality colimit.

T53 asks the next question:

```text
Does a valid observer colimit determine a unique canonical event-finality
structure?
```

The answer in the finite audit is no.

The best-supported verdict is:

```text
H2, H3, and H4 supported.
H0 and H1 refuted.
H5 partially supported as finite descent data, not full sheaf machinery.
```

## Core Distinction

T53 separates three properties:

```text
partial-order validity
unique global completion
axis-based reconstructability
```

T47-style acyclicity protects partial-order consistency for well-formed
PO1-admissible event structures. But it does not determine whether observer
views select one canonical completion, nor whether finality-axis dominance
reconstructs the resulting record order.

## Finite Object

The executable model defines:

```text
ObserverView = local event records accessible to one observer
CompletionCandidate = proposed global event-finality structure
EventMap = observer-local event label -> global event label
AxisProfile = causal and information finality magnitudes
```

A completion is compatible with an observer view when:

1. every observer-local event has a map into the completion;
2. observer-local source records are subsets of the global source records;
3. observer-local target records are subsets of the global target records;
4. observer-local finality-axis profiles match the mapped global event.

For each compatible completion, the model computes:

```text
record-dependency partial order
axis-dominance order
Axis Monotonicity (AM)
completion signature
```

## Witness Results

| Case | Verdict | Meaning |
| --- | --- | --- |
| `t51_positive_control` | `canonical_axis_reconstructable` | T51-style phantom incomparability is repaired by one unique AM-valid completion. |
| `ambiguous_event_identity` | `underdetermined_noncanonical` | Two observer-local chains admit either an identified two-event completion or a disjoint four-event completion. |
| `axis_failing_valid_colimit` | `valid_partial_order_axis_failure` | Record containment gives a valid order, but finality-axis dominance fails to reconstruct it. |
| `hidden_record_repair` | `repairable_by_hidden_record` | A hidden predecessor record repairs an AM mismatch, but the repair is extra data. |
| `nondefinable_overlap_boundary` | `nondefinable_projection` | No event map exists for one observer, so projection to a common completion is undefined. |

## Theorem Statement

Finite Observer-Colimit Descent Boundary Theorem:

```text
For finite FinaliEvent-style record systems, T47-style acyclicity can protect
partial-order consistency of each compatible completion, but it does not
guarantee that bounded observer views determine a unique global event-finality
structure. Canonical reconstruction additionally requires event-identity maps,
sufficient overlap data, and AM-compatible axis profiles when temporal order is
reconstructed from finality axes.
```

## Hypothesis Evaluation

### H0: T51/T52-style positive colimits cover all meaningful merges

Status: refuted.

Evidence: T53 produces underdetermined identity, axis failure, hidden-record
repair, and nondefinable overlap boundaries. These are not positive symmetric
co-reconstruction cases.

### H1: Every compatible merge has a unique canonical completion

Status: refuted.

Evidence: `ambiguous_event_identity` admits two compatible completions with
distinct signatures. The same observer-local evidence can describe either one
shared chain or two disjoint chains.

### H2: Partial-order validity can hold while uniqueness requires extra data

Status: supported.

Evidence: all compatible completions in the audit remain valid partial orders,
but some are noncanonical because observer views do not provide enough identity
or overlap information.

### H3: Axis reconstruction can fail independently of partial-order validity

Status: supported.

Evidence: `axis_failing_valid_colimit` has a valid record-dependency order, but
AM fails because one finality axis decreases along the record dependency.

### H4: Some failures are repairable; others remain noncanonical

Status: supported.

Evidence: `hidden_record_repair` is repaired by adding one hidden predecessor
record. `ambiguous_event_identity` remains noncanonical because more than one
global completion is compatible with the observer data.

### H5: Stronger descent-style formalism is required

Status: partially supported.

Evidence: finite descent data are required:

- event identity maps across observers;
- record-overlap data sufficient to choose among completions;
- AM-compatible axis profiles for axis reconstruction;
- explicit nondefinable-boundary checks.

The audit does not yet force full sheaf or categorical descent machinery.

## What T53 Adds

T51 showed:

```text
bounded apparent order + colimit -> recovered event-finality order
```

T53 shows:

```text
valid colimit does not imply canonical reconstruction
```

The new boundary is not consistency. It is uniqueness and interpretability.

## Repository Recommendation

The repository should add a new distinction:

```text
colimit-consistent
colimit-canonical
axis-reconstructable
descent-underdetermined
nondefinable
```

This strengthens the observer-relative temporal order program. It prevents the
repo from overclaiming that any successful observer merge automatically yields
one uniquely determined event-finality structure.

## Next Best Step

The next theorem should characterize minimal descent data:

```text
Given observer-local FinaliEvent structures and overlap maps, find necessary
and sufficient finite conditions for a unique AM-valid global completion.
```

That theorem would be stronger than T53. T53 only proves the need for such
conditions by executable witnesses.
