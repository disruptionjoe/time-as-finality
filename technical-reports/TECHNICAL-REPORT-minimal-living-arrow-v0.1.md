# Technical Report: Minimal Living Arrow v0.1

## Claim Under Test

T128 asks what first lives after the obstruction stack. T80, T82, T84, T106,
T110, and T122 collectively block strict scalar finality arrows in closed
finite reversible dynamics and finite stationary Markov dynamics unless a
resource, sink, boundary, omitted reverse channel, postselection, transient
sector, or constructor restriction is named.

The purpose is not to prove a thermodynamic arrow. The purpose is to identify
the smallest finite ingredient that generates direction after the current
obstructions are respected.

## Result

The executable audit gives this classification:

- Closed reversible finite cycle: fails. T110 applies directly.
- Stationary finite Markov chain: fails. T122 applies directly.
- Finite resource drawdown: survives by leaving stationarity and closed
  reversibility; direction is finite capacity depletion.
- Maintenance cost: survives only when maintenance consumes a finite repair
  budget; it is resource drawdown plus a persistence task label.
- Open boundary: survives only when the boundary state, exported history, or
  finite sink capacity is counted; it is environmental resource accounting.
- Constructor restriction: formally survives, but direction is imported by
  excluding reverse transformations.

## Strongest Surviving Minimal Model

The strongest non-stipulative survivor is finite resource drawdown:

```text
R3 -> R2 -> R1 -> R0
```

with scalar

```text
drawdown = 3 - resource
```

and future operation sets shrinking from three available operations to none.
Every transition strictly increases drawdown. The model explicitly violates
T122 through nonstationary resource drawdown, transient support, and an
absorbing depleted boundary.

## Strongest Failed Model

The strongest failed model is the stationary Markov control. It has stochastic
motion and nontrivial transitions, but no named resource or transient branch.
The scalar can drift upward from one state only by drifting downward from
another; stationarity forces zero weighted drift.

## Smallest Ingredient Set

If stipulation is allowed, the smallest formal ingredient is constructor
restriction: define reverse transformations as inadmissible.

If stipulation is not allowed, the smallest survivor in this finite audit is
finite nonrenewed resource drawdown with an absorbing depleted boundary.

Maintenance and open-boundary models do not add independent minimal
ingredients here. They reduce to resource drawdown, exported history,
sink-capacity accounting, or explicit constructor restriction.

## Claim Impact Recommendation

Preserve H7 only as a resource-accounting or constructor lemma. Do not promote
H7 as a thermodynamic-arrow claim.

## What This Improved

T128 replaces the open blocker "find a resource-explicit model" with a finite
model family that separates failed controls from living survivors. It gives
the project a minimal executable target for the next physical calibration:
resource drawdown must be mapped to a named free-energy, capacity, memory, or
boundary variable and compared with standard thermodynamics.

## What This Weakened Or Falsified

T128 weakens maintenance and open-boundary readings as independent sources of
direction. In these finite fixtures, maintenance matters only when finite
repair capacity is depleted, and open boundary matters only when boundary
state or sink capacity is counted.

## Open Blocker

The strongest survivor is still an accounting model. A physical upgrade would
need a named free-energy or capacity variable and a direct comparison to
ordinary stochastic thermodynamics.

## Reproduction

```bash
python -m unittest tests.test_minimal_living_arrow -v
python -m models.run_t128
```
