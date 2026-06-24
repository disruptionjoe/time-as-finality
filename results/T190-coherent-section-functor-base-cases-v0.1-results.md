# T190 Results: Coherent Section Functor Base Cases

## Outcome

`FUNCTOR-OBL-TaF-001` is **not verified as currently stated**. The covariant
claim

```text
F : States(Ext_S) -> FinSets
```

is too strong on the finite base cases because extensions can remove coherent
sections, making the proposed action partial or impossible.

## Base-Case Summary

| Fixture | Identity | Total map exists? | Composition meaningful in `FinSets`? | Result |
| --- | --- | --- | --- | --- |
| Redundant singleton chain | yes | yes | yes | survives |
| Selective-survival chain | yes | no | no | fails as stated |
| Total obstruction extension | yes | no (`1 -> 0` impossible) | no | fails as stated |

## Surviving Reading

Two narrower readings remain live:

1. `F_op : States(Ext_S)^op -> FinSets`
   where stricter-state coherent sections include into looser-state coherent
   sections.
2. `F_partial : States(Ext_S) ->` a partial-map or relation-valued category.

## What This Changes

- `FUNCTOR-OBL-TaF-001` should be treated as a **narrowing obligation**, not a
  near-verified theorem.
- `PO1-NCK-001` remains blocked until the coherent-section formal object is
  repaired.
- `T191` should test the best repair path: restricted subcategory,
  contravariant formalism, or codomain change.

## Repo-Safe Reading

Do not cite the coherent-section object as a verified covariant `FinSets`
functor. The finite evidence only supports:

```text
identity is fine;
covariance needs repair;
the natural unrestricted solution-set behavior is contravariant.
```
