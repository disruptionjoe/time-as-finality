# Technical Report: D1 Physical Reduction Map v0.1

## Summary

T22 audits D1's four dimensions against candidate physical observables and
implements one narrow executable reduction. The positive result is limited but
important: D1 holder redundancy can be compared directly with a
Quantum-Darwinism-style count of independent informative environment
fragments in a small system-environment model.

This does not derive D1 from quantum mechanics. It makes D1 harder to wave
around loosely: every axis now has assumptions, frame-status, supporting
tests, and a falsification condition.

## Reduction Map

| D1 dimension | Candidate observable | Current status |
| --- | --- | --- |
| accessible support | observer-readable fragments encoding the target state | partially supported; access-boundary dependent |
| holder redundancy | independent informative environment fragments | first executable reduction |
| branch support | causally independent record channels or branch families | formal with partial support; covariance open |
| reversal cost | minimum intervention, operation, or work budget needed to erase supporting records | weakest and still open |

## Executable Scenario

The toy scenario contains a binary pointer system and five environment
fragments:

| fragment | accessible | informative | independent | branch |
| --- | --- | --- | --- | --- |
| E1 | yes | yes | yes | left |
| E2 | yes | yes | yes | right |
| E3 | yes | yes | no | left |
| E4 | no | yes | yes | hidden |
| N1 | yes | no | yes | noise |

The D1 profile is:

```text
(accessible_support, holder_redundancy, branch_support, reversal_cost)
= (3, 2, 2, 4)
```

The key divergence is `E3`: it is readable and informative, so it raises
accessible support. But it is correlated with `E1`, so it does not raise
independent holder redundancy.

## Result

- raw informative accessible fragments: `3`
- independent informative accessible fragments: `2`
- D1 holder redundancy: `2`
- D1 branch support: `2`
- total informative fragments requiring reversal in this toy cost model: `4`

The result supports the narrow mapping:

```text
D1 holder redundancy = independent informative environmental fragments
```

It also rejects the sloppy mapping:

```text
D1 holder redundancy = raw environmental copies
```

## Interpretation

Plainly: this test says D1 should count independent witnesses, not repeated
echoes. Three copies of a fact are not three independent confirmations if two
copies came through the same channel.

That matters for the larger project because it gives one D1 axis a concrete
physical readout target while preserving D1's warning that finality is not one
scalar quantity.

## Guardrails

- T22 is not a detector-level Quantum Darwinism simulation.
- T22 does not solve T2.
- T22 does not prove all D1 axes are physically grounded.
- T22 does not claim reversal cost is thermodynamic work.
- T22 leaves Lorentz/covariance status open for branch support and reversal
  cost.

## Reproduction

```bash
python -m unittest tests.test_d1_physical_reduction_map -v
python -m models.run_t22
```

Result artifacts:

- [T22 result summary](results/d1-physical-reduction-map-v0.1-results.md)
- [T22 JSON output](results/d1-physical-reduction-map-v0.1.json)
