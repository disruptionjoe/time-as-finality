---
document_type: synthesis_status
batch_item: seventh_20_task_6
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T185 lambda*(S) MSY Residue Status

## Status

This note summarizes T185's absorption result. It does not establish a new
issuance theorem.

## Sources read

- `tests/T185-lambda-star-msy-absorption-test.md`
- `results/T185-lambda-star-msy-absorption-test-v0.1-results.md`

## Plain-English finding

The issuance-rate model is not just classical maximum sustainable yield, but
its surviving difference is specific and narrow: stock-independent novelty,
quadratic coherence cost, and separately typed collapse risk.

## Technical conclusion

T185 finds partial MSY absorption. The standard MSY mechanism gets an interior
optimum from logistic growth and harvesting. The issuance model gets an
interior optimum from:

- `N(lambda)` as stock-independent novelty;
- `C(lambda) = b*lambda^2` as quadratic coherence cost;
- `K(lambda,S)` as a separately typed collapse/obstruction risk.

No exact reparameterization to logistic MSY exists when the quadratic cost is
present and novelty is stock-independent. The residue still needs PO1/native
grounding to avoid being an arbitrary optimal-control model.

## Minimum next task

Tie `C` and `K` to typed PO1 obstruction dynamics and reconciliation queues,
or demote `lambda*(S)` to a useful heuristic objective.

## Stop condition

Stop promotion if the quadratic cost, novelty process, or collapse-risk term
is chosen only to create an interior optimum and is not independently typed.

