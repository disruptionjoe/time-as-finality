# T174 Results: Forgotten-Dims Persistence-Gap Screen

## Summary

In this finite screen, non-empty forgotten_dims plus current lower-level propagation does not generate residual holonic persistence after all lower levels recover. The apparent PG relative to micro decomposes into meso inheritance plus any explicit holonic retention rule.

## Audit Table

| Scenario | Rule | Forgotten dims | Micro PG | Meso inherited gap | Residual PG | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| `scheduled_persistence_baseline` | `scheduled_window` | `['cross-level-recovery-detail']` | `10` | `5` | `5` | `scheduled_residual_pg_positive_control` |
| `no_explicit_persistence_with_forgotten_dims` | `propagate_current_lower` | `['cross-level-recovery-detail']` | `5` | `5` | `0` | `no_residual_pg_from_forgotten_dims` |
| `no_forgotten_dims_control` | `propagate_current_lower` | `[]` | `5` | `5` | `0` | `no_residual_pg_without_forgotten_dims` |
| `explicit_recovery_retention_positive_control` | `explicit_recovery_retention` | `['cross-level-recovery-detail']` | `10` | `5` | `5` | `explicit_retention_generates_residual_pg` |

## scheduled_persistence_baseline

- Holonic rule: `scheduled_window`
- Forgotten dims: `['cross-level-recovery-detail']`
- Micro last obstructed: `24`
- Meso last obstructed: `29`
- Lower last obstructed: `29`
- Holonic last obstructed: `34`
- PG relative to micro: `10`
- Inherited meso gap: `5`
- Residual PG after lower recovery: `5`
- Residual requires explicit retention: `True`
- Forgotten dims alone generated residual PG: `False`
- Verdict: `scheduled_residual_pg_positive_control`
- Interpretation: PG relative to micro is 10, of which 5 comes from meso lag and 5 remains after lower-level recovery. The residual is scheduled by the holonic window.

## no_explicit_persistence_with_forgotten_dims

- Holonic rule: `propagate_current_lower`
- Forgotten dims: `['cross-level-recovery-detail']`
- Micro last obstructed: `24`
- Meso last obstructed: `29`
- Lower last obstructed: `29`
- Holonic last obstructed: `29`
- PG relative to micro: `5`
- Inherited meso gap: `5`
- Residual PG after lower recovery: `0`
- Residual requires explicit retention: `False`
- Forgotten dims alone generated residual PG: `False`
- Verdict: `no_residual_pg_from_forgotten_dims`
- Interpretation: PG relative to micro is still 5, but it is entirely inherited from lower-level lag (5); residual PG after lower-level recovery is zero despite non-empty forgotten_dims.

## no_forgotten_dims_control

- Holonic rule: `propagate_current_lower`
- Forgotten dims: `[]`
- Micro last obstructed: `24`
- Meso last obstructed: `29`
- Lower last obstructed: `29`
- Holonic last obstructed: `29`
- PG relative to micro: `5`
- Inherited meso gap: `5`
- Residual PG after lower recovery: `0`
- Residual requires explicit retention: `False`
- Forgotten dims alone generated residual PG: `False`
- Verdict: `no_residual_pg_without_forgotten_dims`
- Interpretation: The no-forgotten-dims control also has zero residual PG, confirming that the propagated-current-lower rule itself carries no holonic recovery memory.

## explicit_recovery_retention_positive_control

- Holonic rule: `explicit_recovery_retention`
- Forgotten dims: `['cross-level-recovery-detail']`
- Micro last obstructed: `24`
- Meso last obstructed: `29`
- Lower last obstructed: `29`
- Holonic last obstructed: `34`
- PG relative to micro: `10`
- Inherited meso gap: `5`
- Residual PG after lower recovery: `5`
- Residual requires explicit retention: `True`
- Forgotten dims alone generated residual PG: `False`
- Verdict: `explicit_retention_generates_residual_pg`
- Interpretation: Residual PG is 5, but it is produced by the explicit retention rule rather than by forgotten_dims alone.

## Governance Signal

Flag for future review only: the TS line remains useful as a diagnostic vocabulary, but PG should not be promoted as a new invariant unless a future topology screen produces residual PG without explicit retention or hidden scheduling.

## Claim Ledger Update

None. T174 is a negative boundary screen, not a claim-status change.

## Suggested Next

Run MINI-GOAL-TS-003 over tree, linear, ring, and dense TTN topologies using residual PG after lower-level recovery as the primary metric.

## Not Claimed

T174 does not prove that no TTN topology can create residual PG, does not add a recovery operation, and does not change H1, HEF, or any lifecycle state.
