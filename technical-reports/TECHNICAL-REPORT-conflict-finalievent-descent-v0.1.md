# Technical Report: Conflict-Enriched FinaliEvent Descent v0.1

## Abstract

T55 extends FinaliEvent Structures from empty conflict to explicit non-empty
conflict. T48-T54 established finite observer-relative temporal reconstruction
for compatible events: PO1 morphisms become FinaliEvents, record containment
induces a partial order, Axis Monotonicity reconstructs that order from
finality-axis magnitudes, and finite descent conditions determine when bounded
observer views glue into a canonical global structure.

T55 asks whether that theorem ladder survives mutually exclusive events.

The result is positive but constrained. T54 generalizes to non-empty conflict,
but not unchanged. Conflict adds four finite conditions: irreflexivity and
symmetry, no conflict between comparable events, upward inheritance along the
record order, and no explicit conflict/compatibility disagreement.

## Theorem Statement

Conflict-Enriched FinaliEvent Descent Theorem (finite v0.1):

Given finite observer-local FinaliEvent data with T54 identity, overlap, record,
profile, partial-order, and AM conditions, plus a merged conflict relation that
is irreflexive, symmetric, comparable-conflict free, and upward inherited along
the reconstructed record order, the canonical quotient-union construction
produces a unique conflict-valid global FinaliEvent structure.

If conflict validity fails, the failure is classified rather than silently
repaired.

## Added Conflict Conditions

T55 keeps the seven T54 conditions:

1. event identity maps are total and single-valued;
2. cross-observer identified events have overlap witnesses;
3. source records merge without explicit contradiction;
4. target records merge without explicit contradiction;
5. identified events agree on finality-axis profiles;
6. the quotient-union dependency order is a valid partial order;
7. Axis Monotonicity holds on the reconstructed global structure.

T55 adds:

8. conflict is irreflexive and symmetric;
9. conflict is not asserted between comparable events;
10. conflict is upward inherited along the reconstructed order;
11. explicit conflict and explicit compatibility do not disagree.

## Executable Model

Implementation:

- `models/conflict_finalievent_descent.py`
- `models/run_t55.py`
- `tests/test_conflict_finalievent_descent.py`

Result artifacts:

- `results/conflict-finalievent-descent-v0.1.json`
- `results/conflict-finalievent-descent-v0.1-results.md`

The model defines:

```text
LocalConflictEvent
ObserverConflictView
ConflictDescentDatum
GlobalConflictEvent
ConflictCheck
ConflictCompletionResult
```

The completion algorithm:

1. quotient local event labels by identity maps;
2. merge source and target records;
3. reject record and axis-profile contradictions;
4. compute record-dependency order;
5. compute Axis Monotonicity;
6. merge conflict and explicit-compatibility pairs;
7. check conflict validity;
8. classify the result.

## Witness Results

| Witness | Classification | Theorem applies | Key result |
| --- | --- | --- | --- |
| `T48_empty_conflict_special_case` | canonical | true | T48-T54 are preserved as the empty-conflict case. |
| `canonical_conflict_descent` | canonical | true | Non-empty conflict descends when C8-C11 hold. |
| `same_order_no_conflict_control` | canonical | true | Same order and AM can exist with no conflict. |
| `hidden_conflict_repaired_by_colimit` | canonical | true | Two incomplete local conflict views jointly produce a valid global conflict relation. |
| `explicit_conflict_disagreement` | conflict_invalid | false | Explicit conflict and explicit compatibility cannot both descend. |
| `upward_inheritance_failure` | conflict_invalid | false | Order and AM can be valid while conflict alone fails. |
| `self_conflict_after_identity_collapse` | conflict_invalid | false | Local conflict cannot be erased by identifying both endpoints as one event. |

## Key Findings

### 1. Empty Conflict Is A Special Case

The T48 empty-conflict witness remains canonical. T55 therefore preserves the
T48-T54 ladder rather than replacing it.

### 2. Non-Empty Conflict Can Descend Finitely

The `canonical_conflict_descent` witness has:

```text
record order: e1 <= e3
conflict: e1 # e2, e2 # e3
```

Conflict is upward inherited because `e1 # e2` and `e1 <= e3` require
`e2 # e3`.

The completion is canonical, AM-valid, and conflict-valid.

### 3. Conflict Is Not Reconstructed From Order Or AM Alone

The `same_order_no_conflict_control` has the same record order and the same
axis profiles as the canonical conflict witness, but has no conflict relation.

Therefore conflict is independent data. It is not determined by record order or
Axis Monotonicity alone.

### 4. Hidden Conflict Can Be Repaired By Colimit

The hidden-conflict witness splits the conflict relation across two observers:

```text
Observer A sees: e1 # e2
Observer B sees: e2 # e3
```

Neither local view supplies the full relation. The quotient-union colimit
produces the complete upward-inherited global conflict relation.

This is the conflict analogue of T51/T52 phantom incomparability repair.

### 5. Conflict Adds Genuine Failure Modes

The upward-inheritance failure has a valid partial order and AM holds, but
conflict fails:

```text
e1 # e2
e1 <= e3
missing: e2 # e3
```

This proves conflict cannot be reduced to the existing T54 checks.

## Hypothesis Verdicts

| Hypothesis | Verdict | Evidence |
| --- | --- | --- |
| H0 | refuted | Non-empty canonical conflict descent exists. |
| H1 | partially supported | Conflict is finite and independent, but T54 needs C8-C11. |
| H2 | supported | Conflict introduces new descent conditions beyond T54. |
| H3 | refuted | The tested witness family is decidable by finite checks. |
| H4 | supported | Same order and AM can coexist with different conflict data. |

## Event-Structure Verdict

Full Nielsen-Plotkin-Winskel event-structure machinery can still be postponed
for the tested finite witness family.

T55 does require an NPW-shaped conflict relation, but the needed properties are
finite checks over the quotient-union completion:

```text
irreflexivity
comparable-conflict freedom
upward inheritance
explicit conflict/compatibility consistency
```

## Claim Impact

C1 is strengthened in a narrow finite sense:

```text
observer-relative temporal reconstruction can be extended from compatible
FinaliEvents to conflict-enriched FinaliEvent structures, provided the added
finite conflict descent conditions hold.
```

This does not solve quantum measurement, contextuality, or physical branching.
It only establishes the finite event-structure condition that those later
applications would need to preserve.

## Boundary

T55 does not prove:

- that all measurement alternatives are FinaliEvent conflicts;
- that conflict is physically real in any substrate;
- that conflict descent holds for infinite event structures;
- that provenance can be ignored;
- that full sheaf or category machinery will never be needed.

It proves only that the first non-empty conflict witness family can be handled
inside the finite quotient-union framework.

## Recommended Next Step

The next balancing test should be provenance-aware reconstruction:

```text
Do propagation histories carry independent reconstructive information beyond
record bases and conflict relations?
```

That test guards against treating record content plus conflict as complete
before checking whether the history of how records moved between observers is
also load-bearing.
