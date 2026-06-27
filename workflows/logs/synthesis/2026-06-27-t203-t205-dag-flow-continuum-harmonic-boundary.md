---
document_type: synthesis_status
batch_item: seventh_20_task_13
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T203-T205 DAG Flow / Continuum Harmonic Boundary

## Status

This note summarizes the finite DAG repair and the continuum boundary for the
harmonic proxy.

## Sources read

- `tests/T203-edge-capacity-flow-conservation-dag-model.md`
- `results/T203-edge-capacity-flow-conservation-dag-model-v0.1-results.md`
- `tests/T205-continuum-refinement-stability-of-finite-harmonic-proxy.md`
- `results/T205-continuum-refinement-stability-of-finite-harmonic-proxy-v0.1-results.md`

## Plain-English finding

For overlapping networks, the right finite object is flow with capacities and
congestion, not a list of path times. The unweighted harmonic mean is not stable
enough to bridge to continuum claims.

## Technical conclusion

T203 repairs the DAG model with:

```text
C_flow(D,q)
```

computed from incidence, edge times, capacities, demand, congestion law, and
feasible path-flow allocations.

T205 kills unweighted path harmonic as a continuum-stable bridge object: serial
subdivision is harmless, but path-multiplicity refinement changes the harmonic
value purely by representation.

## Minimum next task

Use finite `C_flow` for corrected overlapping-DAG fixtures. For continuum or
WBE language, require a declared refinement functor, capacity measure, and
convergence theorem.

## Stop condition

Stop continuum claims based on unweighted path counting, path multiplicity, or
path-harmonic values without capacity/measure semantics.

