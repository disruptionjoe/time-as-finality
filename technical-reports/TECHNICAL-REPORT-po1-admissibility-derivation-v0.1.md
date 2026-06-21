# Technical Report: PO1 Admissibility Derivation v0.1

## Purpose

T31 identified seven admissibility conditions for PO1. T32 asks whether those
conditions are independent empirical rules or consequences of a smaller
mathematical structure inside finite `D1RestrictionSystem` projections.

The goal is not to add cases. The goal is to explain why AC1-AC7 exist.

## Verdict

Best supported hypothesis:

```text
H2 with H4 boundary
```

T32 does not support the view that AC1-AC7 are seven independent empirical
criteria. The admissibility checklist compresses to:

```text
AC1 + AC2 + AC3 + AC5 + AC6 + AC7
```

AC4 is derivable from AC6 under the current T26 definition of finite gluing
obstruction.

At the principle level, the schema compresses further to four structural
principles:

| Principle | Generates | Status |
| --- | --- | --- |
| P1 typed restriction-system pair | AC1, AC2 | intrinsic to D1RestrictionSystem |
| P2 definable finite projection | AC3 | intrinsic to D1RestrictionMorphism |
| P3 projection-created nontrivial obstruction | AC4, AC6, AC7 | intrinsic to global-section polarity |
| P4 informative forgotten structure | AC5 | not intrinsic to D1RestrictionSystem alone |

The H4 boundary matters: AC5 cannot be derived from `D1RestrictionSystem`
alone because one half of AC5 is a semantic annotation on `ProjectionCase`:
the projection must forget named structure. The system can test measurable
profile loss, but it cannot by itself know which forgotten structure is
domain-relevant.

## Dependency Graph

| Source | Target | Relation | Reason |
| --- | --- | --- | --- |
| P1 typed pair | AC1 | generates | The richer object must be a valid T26 system. |
| P1 typed pair | AC2 | generates | The restricted object must be a valid T26 system. |
| P2 definable projection | AC3 | generates | A finite projection requires a total site map. |
| P3 projection-created obstruction | AC6 | generates | The restricted target must be obstructed. |
| AC6 | AC4 | implies | `obstruction_detected` already includes local satisfiability. |
| P3 projection-created obstruction | AC7 | generates | The richer source must not already be obstructed. |
| P4 informative forgetting | AC5 | generates with extra metadata | Named forgotten structure is not part of T26 alone. |

The key derivation is:

```text
AC6 = restricted_gs.obstruction_detected
obstruction_detected = local_patches_satisfiable and not global_assignment_exists
therefore AC6 implies AC4
```

So AC4 is useful as audit language, but redundant as a formal hypothesis
unless AC6 is later weakened to mean only `global_witness_count == 0`.

## Minimality Audit

T32 removes each condition individually and checks what becomes falsely
admissible.

| Removed condition | New false positive | Failure class |
| --- | --- | --- |
| AC1 | `remove_ac1_case` | invalid richer system |
| AC2 | `remove_ac2_case` | invalid restricted system |
| AC3 | `remove_ac3_case` | non-definable projection |
| AC4 | none | redundant under current T26 semantics |
| AC5 | `remove_ac5_case` | no forgotten structure |
| AC6 | `remove_ac6_case` | no restricted obstruction |
| AC7 | `remove_ac7_case` | shared obstruction |

No condition removal rejects true positives, because removing a required
condition can only broaden the admitted set.

## Counterexample Generation

The generator enumerates all 128 Boolean condition vectors over AC1-AC7.

Result:

```text
total vectors: 128
feasible finite ProjectionCase vectors: 96
impossible vectors: 32
impossibility rule: AC6 implies AC4
```

For every feasible vector, T32 constructs an actual finite `ProjectionCase`
whose computed AC vector matches the target vector exactly. The 32 impossible
vectors are precisely those where:

```text
AC6 = true
AC4 = false
```

That impossibility is not empirical. It follows from the definition of
`global_section().obstruction_detected`.

## What Was Derived

### Derived

AC4 derives from AC6.

AC1 and AC2 derive from the typed domain of PO1: if PO1 is stated over finite
`D1RestrictionSystem` pairs, validity is part of the object boundary.

AC3 derives from finite projection definability: without a total site map,
the bridge is a category-change boundary, not a lossy projection.

### Independent

AC6 is independent. The other conditions can hold while the restricted system
has a global section.

AC7 is independent. The other conditions can hold while the richer system is
already obstructed.

AC5 is independent of T26. The other mathematical conditions can hold for a
lossless or unnamed projection. AC5 requires extra evidence that the projection
forgets named structure and loses measurable profile data.

## Theorem Schema After T32

The recommended formal statement is:

```text
Finite Projection-Obstruction Admissibility Theorem Schema

Given a finite typed pair of D1RestrictionSystems R -> S, a finite projection
is admissible PO1 evidence when:

1. R and S are valid D1RestrictionSystems.
2. The projection is definable by a total site map.
3. S has a finite gluing obstruction.
4. R has a global section.
5. The projection is informatively lossy: it forgets named structure and loses
   measurable profile data.

Then the obstruction in S is represented as projection-created rather than
non-definable, inherited, trivial, or structure-free.
```

The old AC1-AC7 checklist remains useful as an expanded audit surface:

```text
AC1 valid richer system
AC2 valid restricted system
AC3 definable projection
AC4 local compatibility
AC5 informative forgotten structure
AC6 restricted gluing obstruction
AC7 richer global section
```

But formally, AC4 should be treated as a derived line item under AC6.

## Hypothesis Evaluation

| Hypothesis | Verdict |
| --- | --- |
| H0: seven ACs are independent empirical criteria | rejected |
| H1: some ACs are derivable from others | supported |
| H2: smaller minimal axiom set generates AC1-AC7 | best supported |
| H3: one deeper structural invariant generates all ACs | not supported |
| H4: current D1RestrictionSystem is insufficient | partially supported for AC5 only |

## Recommendation

Retain PO1 at `partially_supported`, but sharpen it.

The next formal PO1 statement should not say that seven independent conditions
are required. It should say that PO1 has a four-principle basis:

```text
typed pair
definable projection
projection-created nontrivial obstruction
informative forgotten structure
```

Keep AC1-AC7 as the checklist because it is readable and catches failure
modes. Fold AC4 into AC6 in theorem statements. Keep AC5 explicit until
forgotten structure becomes first-class data inside the formal object.

## Artifacts

- `models/po1_admissibility_derivation.py`
- `models/run_t32.py`
- `tests/test_po1_admissibility_derivation.py`
- `tests/T32-admissibility-derivation.md`
- `results/po1-admissibility-derivation-v0.1.json`
- `results/po1-admissibility-derivation-v0.1-results.md`
