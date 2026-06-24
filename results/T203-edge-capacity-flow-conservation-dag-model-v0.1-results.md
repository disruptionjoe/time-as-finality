# T203 Results: Edge-Capacity / Flow-Conservation DAG Model

## Outcome

`narrowed`

## Main Readout

T203 repairs the T195 weakness by replacing independent path enumeration with a
capacitated flow-conservation model.

## Verdict: narrowed

## Result

The live finite DAG capability should be `C_flow(D,q)`, computed from
incidence, edge times, capacities, demand, and feasible path-flow allocations.

## Repo-Safe Reading

The old `T*_DAG = harmonic_mean(path times)` is no longer an exact DAG object.
It is a proxy valid only under declared independence, no-congestion, or
approximation assumptions.

## Next Step

T204 tests whether two systems can share the same free path harmonic while
differing under `C_flow`.
