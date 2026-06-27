---
document_type: synthesis_status
batch_item: seventh_20_task_5
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T184 mu_M Composition Gate Status

## Status

This note summarizes T184 for the MTI/Cap_TI chain. It does not promote MTI.

## Sources read

- `tests/T184-mu-m-non-additivity-composition-gate.md`
- `results/T184-mu-m-non-additivity-composition-gate-v0.1-results.md`

## Plain-English finding

`mu_M` has a narrow possible escape only during architectural change. Once the
branching/gluing data is updated, much of the apparent novelty is absorbed.

## Technical conclusion

T184 separates two composition operations:

- Union composition: `mu_M` subadditivity is real, but computable from gluing
  topology when `G` encodes the branching tree.
- Sequential extension: the only discriminating case is a transition window
  where a new intermediate level changes the effective architecture before the
  gluing data has absorbed it.

The result is partial and conditional. It supports an MTI stress target, not an
independent primitive.

## Minimum next task

If pursuing this line, freeze the architecture-change timing: define when the
intermediate level exists physically, when `G` is updated, and what capability
can be predicted inside that window.

## Stop condition

Stop using `mu_M` as independent if the alleged split is computable from the
already-declared gluing topology, event count, entropy state, or updated
branching structure.

