# T90: Weak-Measurement Reparameterization Obstruction

## Route

Quantum measurement / classical records.

## Question

When is a proposed weak-measurement finalization time a genuine TaF
discriminator, and when is it only a reparameterized threshold on standard
monitored-record statistics?

## Motivation

T132 states the non-null criterion for the open T12 route. T90 makes that
criterion executable. The goal is not to rescue the weak-measurement route. It
is to prevent a threshold on coherence loss, redundancy, or observer access
from being advertised as new measurement physics.

## Setup

Represent a monitored trajectory by time-indexed values:

- pointer-coherence witness `C(t)`;
- standard fragment redundancy;
- observer access;
- D1 holder redundancy;
- D1 branch support;
- D1 reversal cost.

The standard verdict uses only `C(t)`, fragment redundancy, and access. The TaF
verdict uses the D1 tuple. A pair of trajectories is an isolated non-null
candidate only when the standard timelines are identical while a
pre-registered independent D1 observable changes the TaF finalization time.

## Success Criteria

- A standard-only D1 protocol is classified as `null_reparameterization`.
- Two trajectories with identical coherence/redundancy/access timelines but
  different independent branch witnesses change `t_finality`.
- The same separation is rejected when the branch label is post hoc.

## Failure Criteria

- A pure coherence/redundancy/access threshold is allowed to count as a TaF
  discriminator.
- A post hoc semantic branch label is treated as an independent observable.
- T90 is described as evidence for new detector or weak-measurement dynamics.

## Claim Impact

Q1 remains `partially_supported`, but the weak-measurement branch is now an
obstruction result: T12 is non-null only after a pre-registered branch,
provenance, or reversal-cost observable changes the TaF verdict while standard
monitored-record statistics stay fixed.

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_reparameterization_obstruction -v
python -m models.run_t90
```
