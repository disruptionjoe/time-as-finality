# T32 Results: PO1 Admissibility Derivation

Generated from `run_t32_derivation_audit()`.

## Summary

T32 finds that AC1-AC7 are not seven independent empirical criteria.

Best supported hypothesis:

```text
H2 with H4 boundary
```

The minimal condition basis is:

```text
AC1 + AC2 + AC3 + AC5 + AC6 + AC7
```

AC4 is derived from AC6 under current T26 semantics.

## Principle Compression

| Principle | Conditions generated | Status |
| --- | --- | --- |
| P1 typed restriction-system pair | AC1, AC2 | intrinsic |
| P2 definable finite projection | AC3 | intrinsic |
| P3 projection-created nontrivial obstruction | AC4, AC6, AC7 | intrinsic |
| P4 informative forgotten structure | AC5 | requires ProjectionCase metadata |

## Dependency Graph

| Edge | Relation |
| --- | --- |
| P1 -> AC1 | typed richer object |
| P1 -> AC2 | typed restricted object |
| P2 -> AC3 | total site map |
| P3 -> AC6 | restricted obstruction |
| AC6 -> AC4 | obstruction includes local satisfiability |
| P3 -> AC7 | richer global section |
| P4 -> AC5 | named and measurable forgotten structure |

## Removal Audit

| Removed condition | False positive admitted | Failure class |
| --- | --- | --- |
| AC1 | `remove_ac1_case` | invalid richer system |
| AC2 | `remove_ac2_case` | invalid restricted system |
| AC3 | `remove_ac3_case` | boundary non-definable |
| AC4 | none | redundant under current semantics |
| AC5 | `remove_ac5_case` | no forgotten structure |
| AC6 | `remove_ac6_case` | no new obstruction |
| AC7 | `remove_ac7_case` | shared obstruction |

## Subset Generation

The generator enumerated every Boolean vector over AC1-AC7.

| Quantity | Count |
| --- | --- |
| Total condition vectors | 128 |
| Feasible generated finite ProjectionCases | 96 |
| Impossible vectors | 32 |

The impossible vectors are exactly those with:

```text
AC6 = true
AC4 = false
```

Reason:

```text
global_section().obstruction_detected
  = local_patches_satisfiable and not global_assignment_exists
```

Therefore AC6 entails AC4.

## Main Theorem Schema

```text
Given a finite typed pair of D1RestrictionSystems R -> S, a case is
admissible PO1 evidence when:

1. R and S are valid D1RestrictionSystems.
2. The projection has a total site map.
3. S has a finite gluing obstruction.
4. R has a global section.
5. The projection forgets named structure and loses measurable profile data.
```

AC4 remains useful as checklist language, but is no longer an independent
formal hypothesis.

## Recommendation

Retain PO1 at `partially_supported`, but sharpen it:

- use the four-principle basis in formal statements;
- keep AC1-AC7 as an expanded audit checklist;
- fold AC4 into AC6;
- keep AC5 explicit because forgotten named structure is not yet first-class
  data inside `D1RestrictionSystem`.
