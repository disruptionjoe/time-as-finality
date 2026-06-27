---
document_type: synthesis_status
batch_item: seventh_20_task_4
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T179-T181 H7 Branch-Threshold Capability Kernel

## Status

This note preserves the useful H7-adjacent capability result while keeping H7
demoted.

## Sources read

- `tests/T179-fixed-accounting-capability-topology.md`
- `results/fixed-accounting-capability-topology-v0.1-results.md`
- `tests/T180-branch-support-threshold-minimality.md`
- `tests/T181-branch-failure-threshold-theorem.md`

## Plain-English finding

The branch-topology survivor is useful, but not as an arrow-of-time claim. It
says what backup structure a future task needs after ordinary accounting is
held fixed.

## Technical conclusion

T179 extracts a capability kernel from the T145 survivor:

```text
fixed absorber vector + topology profile -> future capability
```

T180 weakens exact `branch_support`: for one-branch failure, the minimal object
is the threshold `branch_support >= 2`, not exact branch multiplicity. T181
generalizes that for unnamed fixed-`k` branch failures:

```text
branch_support >= k + 1
```

Exact count becomes a margin coordinate. Branch identity matters only for named
or correlated hazard tasks.

## Minimum next task

Write the finite minimality theorem as a task-relative capability theorem, not
an H7 theorem: declare task family, absorber vector, topology coordinate, and
threshold.

## Stop condition

Stop promotion if the result is described as thermodynamic-arrow or
physical-arrow evidence, or if named hazards are reduced to raw support counts
without identity/correlation data.

