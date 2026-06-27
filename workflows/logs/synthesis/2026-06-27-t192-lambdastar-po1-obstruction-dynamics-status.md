---
document_type: synthesis_status
batch_item: seventh_20_task_10
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T192 lambda*(S) PO1 Obstruction Dynamics Status

## Status

This note summarizes T192's narrowing of `lambda*(S)`.

## Sources read

- `tests/T192-lambda-star-derivation-from-po1-obstruction-dynamics.md`
- `results/T192-lambda-star-derivation-from-po1-obstruction-dynamics-v0.1-results.md`
- `tests/T190-coherent-section-functor-base-cases.md`
- `tests/T191-restricted-functoriality-under-admissible-composition.md`

## Plain-English finding

PO1 helps define what counts as an obstruction, but it does not by itself tell
the system how fast to issue new extensions.

## Technical conclusion

T192 rejects the strong statement:

```text
PO1 alone determines lambda*(S)
```

The survivor is narrower:

```text
K(lambda,S) = lambda * |F(S)| * p_obs(S)
```

is PO1-native because PO1 types obstruction events. The optimum still requires
non-PO1 structure:

- proposal/growth dynamics `N`;
- reconciliation/congestion cost `C`;
- a forward partial-map or relation semantics.

Without independent `N` and `C`, the optimizer collapses to a boundary
solution.

## Minimum next task

Define a proposal process and reconciliation-cost model before using
`lambda*(S)` as more than a typed objective template.

## Stop condition

Stop if the derivation treats PO1 obstruction typing as sufficient for a
nonzero interior optimum.

