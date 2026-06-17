# D1 Physical Reduction Map v0.1 Results

## Verdict

T22 supplies a reduction-map audit for all four D1 dimensions and one
executable physical reduction:

```text
D1 holder redundancy = independent informative environment fragments
```

within the stated toy system-environment model.

## Scenario

```text
system states: S0, S1
observer access: E1, E2, E3, N1
```

| fragment | readable | encodes system | independent channel | branch |
| --- | --- | --- | --- | --- |
| E1 | yes | yes | yes | left |
| E2 | yes | yes | yes | right |
| E3 | yes | yes | no | left |
| E4 | no | yes | yes | hidden |
| N1 | yes | no | yes | noise |

## D1 Profile

```text
(accessible_support, holder_redundancy, branch_support, reversal_cost)
= (3, 2, 2, 4)
```

## Redundancy Check

| quantity | value |
| --- | ---: |
| accessible fragments | 4 |
| raw informative accessible fragments | 3 |
| independent informative accessible fragments | 2 |
| D1 holder redundancy | 2 |
| redundancy ratio | 1.0 |

## Key Finding

`E3` carries the pointer record but is correlated with `E1`. It raises
accessible support, but it does not raise holder redundancy. This separates
D1 holder redundancy from raw copy count and makes it closer to the
Quantum-Darwinism-style notion of independent environmental witnesses.

## Guardrail

T22 does not derive D1 from quantum mechanics. It supplies one toy observable
reduction and records assumptions for every D1 axis.
