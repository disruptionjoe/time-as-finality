---
document_type: synthesis_status
batch_item: seventh_20_task_8
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T188 PO1-NCK / Cap_TI Step-4 Recast Status

## Status

This note recasts T188 after the later correction chain. It is not a claim
promotion.

## Sources read

- `tests/T188-po1-nck-formal-claim-and-cap-ti-step4.md`
- `tests/T190-coherent-section-functor-base-cases.md`
- `tests/T192-lambda-star-derivation-from-po1-obstruction-dynamics.md`
- `tests/T207-cap-ti-minimal-statistic-after-corrections.md`

## Plain-English finding

T188 named the right formal ambition, but later tests force a narrower reading:
PO1 can type the obstruction-risk term, not the whole issuance optimum.

## Technical conclusion

T188 proposed two coupled moves:

- `PO1-NCK-001`: `K(lambda,S)` as PO1 obstruction rate.
- Cap_TI step 4: same-neighbor-data split where beta changes only through
  delivery-time metric.

After T190/T191/T192, the covariant `FinSets` story is too strong. The honest
survivor is:

```text
PO1 naturally types K(lambda,S), while N and C need additional non-PO1 dynamics.
```

After T200-T207, Cap_TI step 4 is regime-dependent rather than exact harmonic
minimality.

## Minimum next task

Rewrite T188 as two separate obligations: a PO1-native obstruction-risk term
and a declared-regime Cap_TI timing-summary capability.

## Stop condition

Stop if the result says "PO1 determines lambda*(S)" without separately typing
growth `N`, cost `C`, proposal process, and corrected objective regime.

