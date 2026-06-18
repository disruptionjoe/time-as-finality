# T28 Bridge Results: CAP Theorem as Finite Gluing Obstruction

Generated from `run_cap_bridge_audit()`.

## Summary

| System | Sites | Patches | Global witnesses | Obstructed |
| --- | --- | --- | --- | --- |
| cap_eventual_consistency_richer | 3 | 3 | 2 | False |
| cap_strong_consistency_restricted | 3 | 3 | 0 | True |

Morphism `cap_strong_consistency_demand_functor`:
- site_map_total: True
- local_profiles_preserved: **False** (local_profile_mismatch)
- trust_path_preserved: True
- obstruction_status_preserved: **False**
- reached: False

Hypothesis: **H1** (faithful finite bridge)

## NN-CAP Structural Comparison

| Property | Nielsen-Ninomiya | CAP |
| --- | --- | --- |
| patch_count | 3 | 3 |
| local_witness_count | 3 | 3 |
| global_witness_count | 0 | 0 |
| obstruction_detected | True | True |
| structural_identity | n/a | **True** |

Chaining pattern (both domains):

```
NN:  locality_hermitian (A=B) + translation_invariance (B=C) + exact_onsit_ua (A!=C)
CAP: consistency (A=B)        + availability (B=C)           + partition_tolerance (A!=C)
```

The three-patch chaining obstruction is domain-neutral.

## Restricted System: cap_strong_consistency_restricted

3 sites: node_A, node_B, node_C.

Patches encoding the three CAP assumptions:

- `consistency` (A, B): state_A same state_B
- `availability` (B, C): state_B same state_C
- `partition_tolerance` (A, C): state_A different state_C

All 3 patches locally satisfiable (local_witness_count=3).

Global obstruction: consistency forces A=B; availability forces B=C; therefore
A=C; partition_tolerance forces A!=C. Contradiction. global_witness_count=0.

## Richer System: cap_eventual_consistency_richer

3 sites: primary_node, replica_node, sync_protocol.

Patches:

- `write_local` (primary_node): unconstrained
- `partition_diverge` (primary_node, replica_node): state_primary different state_replica
- `sync_reconcile` (replica_node, sync_protocol): state_replica same sync_flag

Global section EXISTS: {state_primary=+1, state_replica=-1, sync_flag=-1}
satisfies all patches. global_witness_count=2.

## Forgotten Structure

The strong-consistency-demand morphism loses:

- branch_support=1 on primary and replica (restricted has branch_support=0)
- partition_diverge patch: state_primary different state_replica during partition
- sync_reconcile patch: eventual convergence mechanism replaces immediate consistency

These correspond exactly to what eventual-consistency systems supply to evade
the CAP impossibility: they relax immediate consistency by allowing divergence
during partition and reconciling asynchronously.

## Recommendation

H1 is confirmed. The CAP theorem instantiates the Projection-Obstruction Pattern
identified in T27. The structural identity with Nielsen-Ninomiya confirms that
the T26 finite obstruction is domain-neutral. The evasion mechanism is structurally
parallel: relaxing exact on-site symmetry (NN) corresponds to relaxing immediate
consistency (CAP eventual consistency).
