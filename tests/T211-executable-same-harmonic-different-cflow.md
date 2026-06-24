# T211: Executable Same-Harmonic Different-C_flow Fixture

## Target Claims

- T204 same path harmonic, different edge congestion family
- T210 executable `C_flow` solver

## Origin

T204 promoted a hand-computed counterexample: two networks with free path times
`{2,2}` and harmonic mean `2` split under `C_flow`. T211 verifies it
executablely.

## Formal Target

Check:

```text
same free path-time multiset
same harmonic mean
different C_flow
```

## Setup / Fixtures

System D:

```text
two disjoint paths
free path times = {2,2}
C_flow = 8/3
```

System S:

```text
two paths sharing prefix s-u
free path times = {2,2}
C_flow = 10/3
```

## Positive Control

The solver finds:

```text
flows = (1/2, 1/2)
```

for both symmetric fixtures.

## Negative Control

The harmonic proxy reports the same value for both systems:

```text
T_H = 2
```

so it cannot distinguish the corrected capability.

## Absorber Pass

The split is fully absorbed by edge-incidence/capacity completion. It is a
correction to the projection, not independent MTI residue.

## Results

The executable check confirms:

```text
C_flow(D,1) = 8/3
C_flow(S,1) = 10/3
```

## Verdict: promoted

Promoted as the canonical executable counterexample to path-harmonic
sufficiency for overlapping DAGs.

## Falsification Conditions

Demote if a corrected solver or analytic derivation gives equal `C_flow` values
for the two fixtures.

## Next Step

T212 states the projection-insufficiency consequence explicitly.
