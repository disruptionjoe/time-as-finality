# T13: Signed And Interfering Readout

## Target Claims

- [C3: Signed Readout Separation](../claims/C3-signed-readout-separation.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [C2: Typed Compositional Finality](../claims/C2-typed-compositional-finality.md)

## Question

Does the observer-indexed finality profile fail to carry the readout, while
evidence, finality, and temporal reconstruction remain monotone and
observer-consistent?

## Setup

Typed extension of the T1 substrate. No T1 or T12 source is modified. Each
record carries a complex weight.

Two readout maps are compared:

- Linear readout: `R1 = sum w(r)` over accessible supporting records. For
  weights `+1` and `-1`, this factors as `P - N` through two monotone
  counters and is explicitly labeled trivial.
- Born-style readout: `R2 = |sum w(r)|^2`. Cross-terms carry interference.

Witnesses:

- W1: two evidence states have identical finality profiles and different
  readouts. Therefore no function from finality profiles to readouts exists.
- W2: a causal chain has monotonically growing evidence and profiles while
  Born-style readout follows `1, 0, 1`. Therefore no monotone relationship
  survives even along one trajectory.
- Sorkin hierarchy: `I2` is nonzero for some pairs, while `I3` cancels
  symbolically for the quadratic measure.
- Observer consistency: observers with different access each see monotone
  profiles, and readouts agree where access agrees.

## Success Criteria

1. W1 exists.
2. W2 exists.
3. Linear signed readout factors through two monotone counters.
4. `I2 != 0` and `I3 = 0`.
5. Observer consistency holds.
6. Temporal reconstruction is unaffected by weights.

## Failure Criteria

- No W1 is constructible.
- `I3 != 0` for the chosen readout.
- Reconstruction or profile monotonicity breaks when weights are added.

## Known Physics Constraints

- This is a structural result on weighted record graphs.
- It does not derive quantum mechanics, the Born rule, or an interference
  experiment.
- Phase-class counters recover the Born-style readout. The theorem's content
  is that the phase-blind finality profile cannot.

## Result

Status: implemented. T13 adds 15 passing tests, including a symbolic
coefficient check for `I3 = 0`. The current full branch suite passes `72/72`
after T14 was added.
