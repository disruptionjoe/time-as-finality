# T28 Test Specification: CAP Theorem Bridge

## Purpose

T28 tests whether the CAP theorem (Brewer 2000; Gilbert-Lynch 2002) can be
represented as a finite D1RestrictionSystem whose restricted class exhibits a
gluing obstruction structurally identical to the Nielsen-Ninomiya restricted
system from T27.

## Acceptance criteria

The goal succeeds if:

1. The CAP restricted system is globally obstructed (global_witness_count=0)
   with all three CAP assumption patches locally satisfiable.
2. The eventual-consistency richer system has a global section
   (global_witness_count > 0).
3. The morphism is site-map-total but blocked by local_profile_mismatch.
4. The NN and CAP restricted systems are structurally identical (same
   patch_count, local_witness_count, global_witness_count, obstruction_detected).

## Test structure

| Test class | Key assertions |
| --- | --- |
| `CAPRestrictedSystemTests` | validates; 3 sites; 3 CAP patches present; obstructed; all locally satisfiable |
| `CAPRicherSystemTests` | validates; global section exists; partition_diverge and sync_reconcile patches present |
| `CAPMorphismTests` | site_map_total=True; local_profiles_preserved=False; morphism_failure=local_profile_mismatch; H1 |
| `NNCAPComparisonTests` | structural_identity=True; same patch_count=3; same local=3; same global=0; both obstructed |
| `CAPBridgeAuditResultTests` | recommendation names H1 and Nielsen; run_cap_analysis returns dict with correct keys |

## CAP restricted system

**cap_strong_consistency_restricted**

- 3 sites: node_A (consistency_observer), node_B (availability_observer),
  node_C (partition_observer)
- Site profiles: D1Profile(accessible_support=1, holder_redundancy=1,
  branch_support=0, reversal_cost=3) at each site
- Patches:
  - `consistency` (A, B): state_A same state_B
  - `availability` (B, C): state_B same state_C
  - `partition_tolerance` (A, C): state_A different state_C
- All 3 patches locally satisfiable (local_witness_count=3)
- Chaining: consistency forces A=B; availability forces B=C; therefore A=C;
  partition_tolerance forces A!=C -- contradiction
- global_witness_count=0, obstruction_detected=True

## CAP richer system

**cap_eventual_consistency_richer**

- 3 sites: primary_node (branch_support=1, reversal_cost=2), replica_node
  (branch_support=1, reversal_cost=2), sync_protocol (branch_support=0,
  reversal_cost=1)
- Patches:
  - `write_local` (primary_node): variables=(state_primary,), no constraints
  - `partition_diverge` (primary_node, replica_node): state_primary different
    state_replica
  - `sync_reconcile` (replica_node, sync_protocol): state_replica same sync_flag
- Global section EXISTS: {state_primary=+1, state_replica=-1, sync_flag=-1}
  satisfies all patches simultaneously
- global_witness_count=2, obstruction_detected=False

## Morphism

**cap_strong_consistency_demand_functor**

- Site map: primary_node -> node_A, replica_node -> node_B, sync_protocol -> node_C
- site_map_total=True
- preserved_dimensions=("reversal_cost",)
- primary_node.reversal_cost=2, node_A.reversal_cost=3 -- DIFFERENT
- local_profiles_preserved=False -> morphism_failure_kind="local_profile_mismatch"
- obstruction_status_preserved=False (richer=False, restricted=True)
- trust_path_preserved=True

## NN-CAP structural identity

| Property | NN restricted | CAP restricted |
| --- | --- | --- |
| patch_count | 3 | 3 |
| local_witness_count | 3 | 3 |
| global_witness_count | 0 | 0 |
| obstruction_detected | True | True |

The three-patch chaining pattern is identical:
- NN: locality_hermitian (A=B), translation_invariance (B=C), exact_onsit_ua (A!=C)
- CAP: consistency (A=B), availability (B=C), partition_tolerance (A!=C)

## Artifacts

- `models/cap_theorem_bridge.py` -- bridge models and audit runner
- `models/run_t28.py` -- JSON runner
- `tests/test_cap_theorem_bridge.py` -- test suite
- `results/cap-theorem-bridge-v0.1.json` -- machine-readable results
- `results/cap-theorem-bridge-v0.1-results.md` -- results summary
