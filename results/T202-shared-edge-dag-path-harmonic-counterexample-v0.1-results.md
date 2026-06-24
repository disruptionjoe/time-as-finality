# T202 Results: Shared-Edge DAG Path-Harmonic Counterexample

## Outcome

`narrowed`

## Main Readout

T195's finite-DAG extension should be labeled a path-summary proxy only. It can
over-credit reconvergent or fanout structures with shared bottlenecks.

## Fixture

All paths share `s-a` in:

```text
s -> a
a -> b1 -> t
a -> b2 -> t
a -> b3 -> t
```

For `s-a = 100`, path enumeration supplies three reciprocal contributions, but
not three independent upstream channels.

## Absorber Pass

The discrepancy is absorbed by standard edge-flow accounting. Shared edges
require capacities/conservation.

## Verdict: narrowed

## Next Step

Run T203/T204 with an explicit edge-capacity model.
