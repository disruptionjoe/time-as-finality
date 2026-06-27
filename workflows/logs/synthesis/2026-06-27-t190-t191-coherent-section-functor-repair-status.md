---
document_type: synthesis_status
batch_item: seventh_20_task_9
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T190-T191 Coherent-Section Functor Repair Status

## Status

This note summarizes the coherent-section functor repair boundary.

## Sources read

- `tests/T190-coherent-section-functor-base-cases.md`
- `results/T190-coherent-section-functor-base-cases-v0.1-results.md`
- `tests/T191-restricted-functoriality-under-admissible-composition.md`
- `results/T191-restricted-functoriality-under-admissible-composition-v0.1-results.md`

## Plain-English finding

Adding constraints naturally makes solution sets shrink. That means the
coherent-section object is naturally contravariant, not a forward total
`FinSets` functor.

## Technical conclusion

T190 kills the unrestricted covariant `FinSets` statement: extensions can
delete coherent sections or send a nonempty set to empty, so `F(e):F(S)->F(S')`
is partial or impossible.

T191 identifies the repair boundary:

- unrestricted honest repair: contravariant `F_op`;
- forward repair: partial maps/relations;
- covariant total `FinSets`: only on the section-preserving subcategory, which
  is mathematically legitimate but dynamically weak.

## Minimum next task

Use `F_partial : States(Ext_S) -> ParSets` for forward issuance dynamics, and
use `F_op` when the task is ordinary solution-set restriction.

## Stop condition

Stop any covariant `FinSets` claim on extension classes that can kill coherent
sections, unless the morphism class is explicitly restricted to
section-preserving arrows.

