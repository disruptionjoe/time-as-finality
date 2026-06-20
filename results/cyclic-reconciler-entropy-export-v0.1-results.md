# T84 Results: Cyclic Reconciler Entropy Export

Strongest claim: In the T80 observation witness, a fixed-size cyclic reconciler does not produce monotone local retained records. Monotonicity returns only when overwritten slots are exported as history or discarded through an erasing heat-bath channel.

Weakened claim: H7's physical-arrow reading is weakened: cyclic persistence has not been separated from ordinary entropy/history export.

## T80 observation sequence

- Observed masks: `[[1, 0], [1, 1], [1, 0], [0, 0], [1, 0], [1, 1]]`
- Raw support sequence: `[1, 2, 1, 0, 1, 2]`
- Raw support monotone: `False`

## Cyclic policies

| Policy | Local support | Local monotone | Accounted support | Accounted monotone | Injective | Lost bits | Boundary |
| --- | --- | --- | --- | --- | --- | ---: | --- |
| `cyclic_reversible_export` | `[1, 3, 4, 3, 2, 3]` | `False` | `[1, 3, 4, 4, 5, 7]` | `True` | `True` | `0.0` | The fixed ring is reversible only because each overwritten slot is exported as external history; local ring support itself is not monotone. |
| `cyclic_erasing_heat_bath` | `[1, 3, 4, 3, 2, 3]` | `False` | `[1, 3, 4, 4, 5, 7]` | `True` | `False` | `2.0` | The fixed ring can be recycled only by discarding the overwritten slot; the generic finite update loses the overwritten slot bits. |

## Verdicts

- `cyclic_reversible_export`: H7 monotonicity is recovered only if exported garbage/history is counted as retained finality.
- `cyclic_erasing_heat_bath`: Counting erased support restores the same monotone accounting curve, but no longer as accessible record memory; it is ordinary erasure/heat-bath bookkeeping.

## Falsification condition

T84 fails if a fixed-capacity cyclic reconciler gives monotone local retained-record support for the T80 sequence while remaining injective and without exporting overwritten slots, erasing them, or hiding them in inaccessible garbage.

## H7 update

H7 should remain partially supported only as a conditional constructor theorem. T84 adds that cyclic reconciliation restores monotonicity only by moving old records into an exported history channel or by paying erasure cost; the autonomous local memory does not supply an independent arrow.

## Blocker

No cyclic finite observer has yet produced D1-monotone local records under reversible dynamics without an explicit export, garbage, or heat-bath account.

## Next move

Try a logically reversible compression/export model with a bounded entropy sink and ask whether any nontrivial D1 monotone survives after the sink is included in the state space.
