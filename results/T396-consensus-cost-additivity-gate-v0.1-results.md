# T396 Results: Consensus-Cost Additivity Gate

## Current Strongest Claim

In the declared finite bit-consensus tasks, the minimal coarse-grained cost is
ordinary entropy reduction:

```text
H(X) - H(Y) = H(X | Y)
```

where `X` is the input record state across `k` holders and `Y` is the declared
consensus bit. No standalone consensus-structure term is earned by these
fixtures.

## Main Verdict

Direction C remains live only if a sharper, substrate-native protocol adds
constraints not represented by this finite map: reliability, communication
geometry, metastability, clocking, finite-time dissipation, or reset dynamics.
Holder count or pairwise disagreement alone is not a thermodynamic bound.

## Fixture Summary

| fixture | min erasure bits | independent reset bits | verdict |
|---|---:|---:|---|
| `root_copy_independent_k2` | 1.000000 | 1.000000 | `additive_entropy_bookkeeping_only` |
| `root_copy_independent_k3` | 2.000000 | 2.000000 | `additive_entropy_bookkeeping_only` |
| `root_copy_independent_k4` | 3.000000 | 3.000000 | `additive_entropy_bookkeeping_only` |
| `root_copy_independent_k5` | 4.000000 | 4.000000 | `additive_entropy_bookkeeping_only` |
| `root_copy_independent_k6` | 5.000000 | 5.000000 | `additive_entropy_bookkeeping_only` |
| `majority_independent_k3` | 2.000000 | 2.433834 | `independent_reset_overcounts_joint_entropy` |
| `majority_independent_k5` | 4.000000 | 4.480191 | `independent_reset_overcounts_joint_entropy` |
| `already_consensus_k5` | 0.000000 | 0.000000 | `holder_count_floor_refuted_by_correlation` |
| `single_error_majority_k5` | 2.321928 | 3.609640 | `holder_count_floor_refuted_by_correlation` |
| `constant_reset_independent_k4` | 4.000000 | 4.000000 | `additive_entropy_bookkeeping_only` |
| `parity_consensus_independent_k4` | 3.000000 | 4.000000 | `independent_reset_overcounts_joint_entropy` |

## Controls

- Root-copy independent inputs produce the expected `k - 1` bit floor.
- Already-consensus inputs cost zero despite five holders, so redundancy alone
  cannot force a positive cost.
- Majority and parity fixtures show that per-holder conditional reset can
  overcount the true joint floor; the difference is ordinary conditional
  correlation bookkeeping.
- The full-transcript control has zero closed reversible cost in every fixture,
  preserving the T110/T142/T145 boundary.

## Not Claimed

This does not prove a thermodynamic consensus theorem, does not update H7, and
does not close Direction C. It blocks one weak first rung: a consensus-cost
bound cannot be based on holder count, pairwise disagreement, or independent
reset accounting alone.

## Next Gate

Build a substrate-native stochastic-thermodynamic consensus protocol with
finite-time reliability constraints declared before D1 scoring. If that still
collapses to `H(X|Y)` plus ordinary communication or reset overhead, demote
Direction C's first rung to entropy bookkeeping plus engineering overhead.

## Reproduction

```bash
python -m unittest tests.test_consensus_cost_additivity_gate -v
python -m models.consensus_cost_additivity_gate
```

JSON result:

```text
results/T396-consensus-cost-additivity-gate-v0.1.json
```
