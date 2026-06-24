# T206: Native WBE / Allometric-Network Absorber Audit

## Target Claims

- T203 corrected finite DAG proxy
- T205 killed unweighted continuum harmonic bridge
- MTI / Cap_TI finite-to-WBE interpretation

## Origin

After T203-T205, the best finite object is capacity-aware flow, not unweighted
path harmonic. T206 asks whether that corrected object survives native
WBE/allometric-network absorption.

## Formal Target

Grant neighboring theory its native state:

```text
branching network
terminal demand
edge lengths
radii / conductances / capacities
impedance or resistance law
volume / resource constraints
optimization objective
```

Ask whether `C_flow` contains residue beyond those variables.

## Setup / Fixtures

Translate finite edge capacity to conductance-like transport capacity, edge
time to travel/resistance cost, and demand `q` to supplied terminal flow.

## Positive Control

A bottlenecked network should have worse `C_flow` than a distributed-capacity
network. Native allometric/network transport theory also predicts this from
conductance and resistance.

## Negative Control

Two networks with the same native WBE/allometric state up to isomorphism or
labeling convention must have the same corrected finite proxy.

## Absorber Pass

If `C_flow` depends only on incidence, capacities/conductances, edge costs,
demand, and the optimization objective, then the corrected proxy is absorbed by
native network transport theory. A TaF residue would require different
record/finality capability at fixed native allometric state.

## Results

The corrected finite proxy is mathematically better than unweighted path
harmonic, but its content is standard finite transport/network optimization
once WBE-native variables are granted.

## Verdict: absorbed

The corrected finite proxy is absorbed as independent WBE/allometric residue.

## Falsification Conditions

Revisit if a fixed native allometric network state admits different
TaF/finality capability values, or if a refinement theorem produces a
non-native invariant not captured by conductance, resistance, demand, or
network optimization.

## Next Step

Either build an executable `C_flow` solver suite, or search for a
fixed-native-state finality witness rather than another timing-summary proxy.
