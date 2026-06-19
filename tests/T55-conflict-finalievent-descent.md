# T55: Conflict-Enriched FinaliEvent Descent

## Target Claims

- [C1: Experienced Time As Record Finality](../claims/C1-experienced-time-as-record-finality.md)
- [D1-Field: Multiscale Observer Finality](../claims/D1-field-multiscale-observer-finality.md)
- [T48: FinaliEvent Structure](T48-finali-event-structure.md)
- [T50: Axis Monotonicity Theorem](T50-axis-monotonicity-theorem.md)
- [T54: Finite Finality Descent Theorem](T54-finite-finality-descent-theorem.md)

## Central Question

Does the T54 finite descent theorem survive when FinaliEvent structures include
explicit non-empty conflict?

T48-T54 used empty conflict. T55 asks whether mutually exclusive finality events
can be handled by the same finite quotient-union descent algorithm, or whether
conflict forces a richer event-structure formalism.

## Formal Object

T55 defines a conflict-enriched FinaliEvent structure:

```text
ConflictFinaliEventStructure = (
  events,
  record-dependency order,
  conflict relation,
  axis profiles,
  source and target records
)
```

The conflict relation is interpreted as mutual exclusivity between events, not
as ordinary incomparability. Two events may be incomparable without being in
conflict.

## Conflict Descent Conditions

T55 keeps the seven T54 descent conditions and adds four conflict conditions:

1. Conflict is irreflexive and symmetric.
2. Conflict is not asserted between comparable events.
3. Conflict is upward inherited along the reconstructed record order.
4. Explicit conflict and explicit compatibility do not disagree.

## Competing Hypotheses

H0: T54 descent only works for empty-conflict FinaliEvent structures.

H1: Conflict can be added as an independent finite relation without changing
T54.

H2: Conflict introduces new descent conditions beyond the T54 basis.

H3: Conflict forces full event-structure machinery beyond finite quotient-union
checks.

H4: FinaliEvent order and conflict cannot be reconstructed from the same data.

## Required Witnesses

T55 constructs:

- an empty-conflict special case preserving T48-T54;
- a canonical non-empty conflict descent case;
- a same-order no-conflict control;
- a hidden-conflict case repaired by colimit;
- an explicit conflict-disagreement failure;
- an upward-inheritance failure;
- a self-conflict failure after identity collapse.

## Success Criteria

T55 succeeds if it produces:

- a formal finite definition of conflict-enriched FinaliEvents;
- executable descent classification with conflict;
- at least one positive canonical conflict witness;
- at least one conflict failure witness;
- at least one hidden-conflict observer-relative witness;
- a verdict on whether T54 generalizes unchanged, generalizes with added
  conditions, or fails;
- a recommendation on whether full NPW event-structure machinery is required.

## Failure Criteria

T55 fails if:

- empty-conflict T48-T54 cases are not preserved;
- a valid non-empty conflict relation cannot descend canonically;
- conflict failures collapse into ordinary order or AM failures;
- hidden conflict cannot be repaired by finite colimit data;
- full event-structure machinery is required for all finite witnesses.

## Non-Goals

- Do not claim this solves quantum measurement.
- Do not identify conflict with incomparability.
- Do not collapse conflict into record mismatch without an executable witness.
- Do not introduce infinite sheaf or category machinery unless finite checks fail.
- Do not promote physical claims from the conflict witnesses.

## Expected Scientific Value

T55 tests the first genuinely event-structural complication after T48-T54.

If successful, the repo moves from finite partial-order reconstruction toward a
finite observer-relative event-structure theory.

If it fails, it identifies the boundary of the current FinaliEvent formalism.
