# Technical Report: Cross-Domain Projection-Obstruction Validation v0.1

## Summary

T30 hostile-tests PO1 outside the physics and GU examples that motivated it.
The purpose is not to confirm PO1, but to see whether unrelated finite domains
break it.

The result is mixed and useful:

```text
PO1 survives one non-physics hostile case, but T30 does not justify
strengthening it beyond partially_supported.
```

T30 recommends keeping PO1 as `partially_supported` with explicit
admissibility constraints.

## Method

T30 reuses the T29 `ProjectionCase` and `analyze_projection_case` machinery.
Each hostile domain is encoded as:

```text
richer D1RestrictionSystem
projection / restriction morphism
restricted D1RestrictionSystem
classification
```

No new category or sheaf machinery was added.

## Cases

| Domain | Case | Classification | PO1 support |
| --- | --- | --- | --- |
| Git merge conflict | `git_semantic_merge` | projection-created obstruction | yes |
| Database schema migration | `database_expand_contract` | lossy projection without obstruction | no |
| Access-control policy inheritance | `access_control_inheritance` | shared obstruction | no |
| Type systems and macro expansion | `type_system_macro_expansion` | non-definable projection | no |

## Case Notes

### Git Merge Conflict

The richer object is a rename-aware semantic merge. The restricted object is a
path-only merge model.

The richer system has a global section. The restricted system is locally
satisfiable but globally obstructed. The projection is definable and forgets
rename metadata plus the semantic merge driver.

Verdict:

```text
positive PO1 instance
```

This rejects a narrow form of H0: PO1 is not only a GU or physics pattern at
the finite abstraction level.

### Database Schema Migration

The richer object is an expand-contract migration with a compatibility view
and dual-write rollout metadata. The restricted object is a flat old/app/new
schema compatibility model.

The projection loses rollout detail, but both richer and restricted systems
have global sections.

Verdict:

```text
loss alone is insufficient
```

This is a negative control against overcounting every lossy projection as PO1.

### Access-Control Policy Inheritance

The richer object carries policy provenance and priority labels. The restricted
object is a flat effective-permission policy.

Both systems are obstructed. The projection did not create the obstruction.

Verdict:

```text
shared obstruction is not PO1 support
```

This is a negative control against counting inherited contradictions as
projection-created contradictions.

### Type Systems and Macro Expansion

The richer object includes a macro-expansion phase. The restricted object has
only source, core, and runtime sites.

The source site map is incomplete because the macro-expansion phase has no
target site.

Verdict:

```text
non-definable projection boundary
```

This supports an H3-style boundary: some non-physics domains may require
richer site maps or syntax-category morphisms before PO1 is even testable.

## Hypothesis Evaluation

| Hypothesis | Status | T30 verdict |
| --- | --- | --- |
| H0: PO1 is domain-specific to GU/no-go style cases | rejected in finite scope | Git supplies one non-physics positive instance |
| H1: PO1 applies to at least one non-physics inherited domain | supported | Git merge is positive |
| H2: PO1 applies across multiple unrelated domains | not yet supported | only one positive in T30 |
| H3: PO1 requires modification for non-physics domains | partially supported | type-system macro case is non-definable |
| H4: PO1 is too broad or underconstrained | partially supported as warning | negative controls show admissibility constraints are needed |

Best supported verdict:

```text
H1 with H3/H4 constraints
```

## Recommendation

Keep PO1 at `partially_supported`.

Do not strengthen it yet. T30 shows PO1 is not merely a physics/GU artifact,
but it also shows that the schema needs explicit admissibility constraints.

Future PO1 evidence should require:

1. The projection is independently motivated by the domain.
2. The richer system has a global section.
3. The restricted system is obstructed.
4. The forgotten structure is the same structure that resolves the restricted
   obstruction.
5. Lossy projection without obstruction is excluded.
6. Shared obstruction is excluded.
7. Non-definable projections are boundary cases, not failed positives.

## Non-Claims

T30 does not claim PO1 is universal.

T30 does not prove any external theorem about Git, databases, access-control
systems, or type systems.

T30 does not promote PO1 beyond `partially_supported`.

## Artifacts

| Artifact | Path |
| --- | --- |
| Model | `models/cross_domain_projection_obstruction_validation.py` |
| Runner | `models/run_t30.py` |
| Tests | `tests/test_cross_domain_projection_obstruction_validation.py` |
| Test spec | `tests/T30-cross-domain-projection-obstruction-validation.md` |
| JSON results | `results/cross-domain-projection-obstruction-validation-v0.1.json` |
| Results summary | `results/cross-domain-projection-obstruction-validation-v0.1-results.md` |
